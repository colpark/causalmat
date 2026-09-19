"""Panel detection over MatMech figures with the MatMMExtract YOLO12 checkpoint.

One worker = one GPU. Sharding is content-based so hosts need no coordination:
    crc32(doi_folder) % n_hosts == host_idx, then % n_gpus == gpu_idx

Writes <doi_folder>/panels/panels.json (+ panels/crops/) and never touches existing files.
Resumable: a DOI folder whose panels.json already carries the same run_version is skipped.

Usage:
  python detect_panels.py --root ~/Documents/causalmat/matmech --host-idx 0 --n-hosts 2 \
      --gpu-idx 0 --n-gpus 1 --out-dir ~/panels/out [--limit 100] [--no-crops] [--overlays 20]
"""
import argparse
import json
import os
import re
import sys
import time
import zlib
from pathlib import Path

from PIL import Image, ImageDraw

WEIGHTS = "/home/aid1/matmmextract/examples/.weights_cache/10garsNWEdgzMGX9nyDE8dMABkU_3BYp9.pt"
LETTERS = "abcdefghijklmnopqrst"
# (a)  a)  (a, b)  (a-c)  (a and b)  (a1)
GROUP = re.compile(r"\(([a-tA-T][0-9]?(?:\s*(?:,|and|–|—|-|to)\s*[a-tA-T][0-9]?)*)\)")
LEAD = re.compile(r"(?:^|[\s;.])([a-tA-T][0-9]?)\)")
ITEM = re.compile(r"[a-tA-T][0-9]?")


def caption_labels(caption: str):
    """Panel labels named in a caption, lowercased, in order, ranges expanded."""
    out, seen = [], set()

    def add(lbl):
        lbl = lbl.lower()
        if lbl not in seen:
            seen.add(lbl)
            out.append(lbl)

    for m in list(GROUP.finditer(caption or "")) :
        body = m.group(1)
        parts = ITEM.findall(body)
        if re.search(r"(–|—|-|to)", body) and len(parts) == 2 and not parts[0][1:] and not parts[1][1:]:
            a, b = parts[0].lower(), parts[1].lower()
            if a in LETTERS and b in LETTERS and LETTERS.index(a) <= LETTERS.index(b):
                for c in LETTERS[LETTERS.index(a):LETTERS.index(b) + 1]:
                    add(c)
                continue
        for p in parts:
            add(p)
    for m in LEAD.finditer(caption or ""):
        add(m.group(1))
    return out


def iou_contained(inner, outer):
    """Fraction of `inner` area contained in `outer`."""
    x1, y1, x2, y2 = inner
    X1, Y1, X2, Y2 = outer
    ix, iy = max(0, min(x2, X2) - max(x1, X1)), max(0, min(y2, Y2) - max(y1, Y1))
    a = max(1, (x2 - x1) * (y2 - y1))
    return ix * iy / a


def iou(a, b):
    x1, y1, x2, y2 = a
    X1, Y1, X2, Y2 = b
    ix, iy = max(0, min(x2, X2) - max(x1, X1)), max(0, min(y2, Y2) - max(y1, Y1))
    inter = ix * iy
    ua = (x2 - x1) * (y2 - y1) + (X2 - X1) * (Y2 - Y1) - inter
    return inter / max(ua, 1)


def apply_rules(dets, labels, w=0, h=0):
    """Rules 3-7 plus two rules added after the dry run. Returns kept, other, dups, nested, flags, fired."""
    fired = []
    frame = [d for d in dets if w and h and (d["bbox"][2] - d["bbox"][0]) * (d["bbox"][3] - d["bbox"][1]) >= 0.85 * w * h]
    # 3b whole-frame stack: single-panel figures often get 2-3 overlapping full-frame boxes with different letters
    if not labels and frame and len(frame) == len(dets):
        fired.append("whole_frame")
        return [], [], [], [], True, False, False, fired
    is_single = not labels and (len(dets) <= 2 or any(d["label"] == "single" for d in dets))
    if is_single:
        fired.append("single_figure")
    letters = [d for d in dets if d["label"] in [c.upper() for c in LETTERS]]
    best, dups = {}, []
    for d in sorted(letters, key=lambda d: -d["score"]):
        if d["label"] in best:
            dups.append(d)
        else:
            best[d["label"]] = d
    if dups:
        fired.append("dedupe")
    kept, nested = [], []
    for d in best.values():
        if any(o is not d and o["label"] == d["label"] and iou_contained(d["bbox"], o["bbox"]) > 0.9 for o in best.values()):
            nested.append(d)
        else:
            kept.append(d)
    if nested:
        fired.append("nested")
    # 5b cross-label near-duplicate: same region detected under two letters, keep the higher score
    kept.sort(key=lambda d: -d["score"])
    keep2 = []
    for d in kept:
        if any(iou(d["bbox"], k["bbox"]) > 0.7 or iou_contained(d["bbox"], k["bbox"]) > 0.9 for k in keep2):
            dups.append({**d, "reason": "cross_label_overlap"})
            fired.append("cross_label_overlap") if "cross_label_overlap" not in fired else None
        else:
            keep2.append(d)
    kept = keep2
    other = [d for d in dets if d["label"] in ("single", "common")]
    detected = {d["label"].lower() for d in kept}
    mismatch = bool(labels) and detected != {l for l in labels if len(l) == 1}
    if mismatch:
        fired.append("label_mismatch")
    two_level = any(len(l) > 1 for l in labels)
    if two_level:
        fired.append("two_level")
    kept.sort(key=lambda d: d["label"])
    return kept, other, dups, nested, is_single, mismatch, two_level, fired


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--host-idx", type=int, default=0)
    ap.add_argument("--n-hosts", type=int, default=1)
    ap.add_argument("--gpu-idx", type=int, default=0)
    ap.add_argument("--n-gpus", type=int, default=1)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--no-crops", action="store_true")
    ap.add_argument("--overlays", type=int, default=0, help="write N detection overlays into <out-dir>/review")
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--conf", type=float, default=0.25)
    ap.add_argument("--iou", type=float, default=0.5)
    ap.add_argument("--tag", default="")
    ap.add_argument("--sample", type=int, default=0, help="random sample of N folders (seed 0) instead of the head")
    a = ap.parse_args()

    import hashlib

    import torch
    from ultralytics import YOLO

    sha = hashlib.sha256(open(WEIGHTS, "rb").read()).hexdigest()
    run_version = f"matmmextract-yolo12m/{sha[:12]}/imgsz{a.imgsz}/v1"
    root = Path(a.root).expanduser()
    out = Path(a.out_dir).expanduser()
    (out / "review").mkdir(parents=True, exist_ok=True)
    wid = f"h{a.host_idx}g{a.gpu_idx}{a.tag}"
    man = open(out / f"manifest_{wid}.jsonl", "a")
    err = open(out / f"errors_{wid}.jsonl", "a")

    import ultralytics
    model = YOLO(WEIGHTS)
    names = model.names
    host = os.uname().nodename
    gpu = torch.cuda.get_device_name(0)
    meta = {"run_version": run_version, "ultralytics": ultralytics.__version__, "torch": torch.__version__,
            "host": host, "gpu": gpu, "params": {"imgsz": a.imgsz, "conf": a.conf, "iou": a.iou}}

    folders = sorted(p.parent for p in root.glob("*/*/data.json"))
    mine = [f for f in folders
            if zlib.crc32(f.name.encode()) % a.n_hosts == a.host_idx
            and zlib.crc32(f.name.encode()) // a.n_hosts % a.n_gpus == a.gpu_idx]
    if a.sample:
        import random
        random.Random(0).shuffle(mine)
        mine = mine[:a.sample]
    elif a.limit:
        mine = mine[:a.limit]
    print(f"[{wid}] {len(mine)} of {len(folders)} DOI folders; run_version={run_version}", flush=True)

    t0 = time.time()
    n_fig = n_skip = n_crop = n_done = overlays = 0
    for i, folder in enumerate(mine, 1):
        pj = folder / "panels" / "panels.json"
        if pj.exists():
            try:
                if json.load(open(pj)).get("run_version") == run_version:
                    n_done += 1
                    continue
            except Exception:
                pass
        rec = json.load(open(folder / "data.json", encoding="utf-8"))
        caps = {im.get("image_path"): " ".join(im.get("image_caption") or []) for im in rec.get("image_info") or []}
        paths, metas = [], []
        for rel, cap in caps.items():
            p = folder / (rel or "")
            if not rel or p.is_dir() or not p.is_file():
                err.write(json.dumps({"doi": folder.name, "file": rel, "reason": "path is a directory" if p.is_dir() else "missing file"}) + "\n")
                n_skip += 1
                continue
            try:
                with Image.open(p) as im:
                    im.verify()
                paths.append(p)
                metas.append((rel, cap))
            except Exception as e:
                err.write(json.dumps({"doi": folder.name, "file": rel, "reason": f"unreadable: {type(e).__name__}"}) + "\n")
                n_skip += 1
        figures = []
        if paths:
            res = model.predict([str(p) for p in paths], imgsz=a.imgsz, conf=a.conf, iou=a.iou,
                                half=True, device=0, verbose=False)
            for p, (rel, cap), r in zip(paths, metas, res):
                dets = []
                for b in r.boxes:
                    x1, y1, x2, y2 = (int(round(v)) for v in b.xyxy[0].tolist())
                    dets.append({"label": names[int(b.cls)], "score": round(float(b.conf), 4), "bbox": [x1, y1, x2, y2]})
                h, w = r.orig_shape
                labels = caption_labels(cap)
                kept, other, dups, nested, is_single, mismatch, two_level, fired = apply_rules(dets, labels, int(w), int(h))
                fig = {"file": rel, "width": int(w), "height": int(h), "caption_labels": labels,
                       "is_single": is_single, "two_level": two_level, "label_mismatch": mismatch,
                       "detections": kept + other, "duplicates": dups, "nested": nested, "rules_fired": fired}
                if not a.no_crops and not is_single and kept:
                    cd = folder / "panels" / "crops"
                    cd.mkdir(parents=True, exist_ok=True)
                    with Image.open(p) as im:
                        im = im.convert("RGB")
                        for d in kept:
                            x1, y1, x2, y2 = d["bbox"]
                            if x2 - x1 < 8 or y2 - y1 < 8:
                                continue
                            name = f"{Path(rel).stem}_{d['label']}.jpg"
                            im.crop((x1, y1, x2, y2)).save(cd / name, "JPEG", quality=90)
                            d["crop"] = f"panels/crops/{name}"
                            n_crop += 1
                if overlays < a.overlays:
                    with Image.open(p) as im:
                        im = im.convert("RGB")
                        dr = ImageDraw.Draw(im)
                        for d in kept + other:
                            dr.rectangle(d["bbox"], outline=(200, 30, 30), width=3)
                            dr.text((d["bbox"][0] + 4, d["bbox"][1] + 2), f"{d['label']} {d['score']:.2f}", fill=(200, 30, 30))
                        im.save(out / "review" / f"{folder.name}__{Path(rel).stem}.jpg", "JPEG", quality=88)
                    overlays += 1
                figures.append(fig)
                man.write(json.dumps({"doi": folder.name, "journal": folder.parent.name, "file": rel,
                                      "n_detections": len(kept), "is_single": is_single, "two_level": two_level,
                                      "label_mismatch": mismatch, "labels": [d["label"] for d in kept],
                                      "caption_labels": labels, "host": host}) + "\n")
                n_fig += 1
        pj.parent.mkdir(parents=True, exist_ok=True)
        json.dump({**meta, "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "figures": figures},
                  open(pj, "w"), ensure_ascii=False)
        if i % 1000 == 0:
            dt = time.time() - t0
            print(f"[{wid}] {i}/{len(mine)} folders {n_fig} figs {n_fig/max(dt,1):.1f} fig/s "
                  f"{n_crop} crops {n_skip} skipped {n_done} resumed", flush=True)
            man.flush(); err.flush()
    dt = time.time() - t0
    print(f"[{wid}] DONE {len(mine)} folders, {n_fig} figures, {n_crop} crops, {n_skip} skipped, "
          f"{n_done} already done, {dt/60:.1f} min, {n_fig/max(dt,1):.1f} fig/s", flush=True)
    man.close(); err.close()


if __name__ == "__main__":
    sys.exit(main())
