"""OCR every panel crop with RapidOCR (PP-OCRv4 models bundled in the wheel).

Reads <doi>/panels/panels.json and panels/crops/*.jpg, writes <doi>/panels/ocr.json. Nothing else is touched.
Sharding matches the detection run: crc32(doi) % n_hosts, then // n_hosts % n_procs.

Usage:
  python ocr_panels.py --root ~/Documents/causalmat/matmech --out-dir ~/panels/ocr_out \
      --host-idx 0 --n-hosts 2 --procs 18 [--limit 200] [--review 30 --review-dir ...]
"""
import argparse
import json
import os
import re
import sys
import time
import zlib
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

RUN_VERSION = "rapidocr-ppocrv4/cuda-cap900/v1"
LETTER_RX = re.compile(r"^\(?([a-tA-T])\d?\)?[.:]?$")
NUMERIC_RX = re.compile(r"^[-+]?\d[\d.,]*$")
SCALE_RX = re.compile(r"\b\d+(?:\.\d+)?\s*(?:nm|µm|μm|um|mm|Å|A°)\b", re.I)
CUES = [
    ("XRD", r"2\s*θ|2\s*theta|2\s*0\s*\(°|\(degree|\(deg"),
    ("XPS", r"binding\s*energy"),
    ("Raman", r"raman\s*shift"),
    ("FTIR", r"wavenumber"),
    ("EDS", r"energy\s*\(?\s*kev"),
    ("XAS", r"photon\s*energy|absorption.*\beV\b|XANES|EXAFS"),
    ("electrochemistry", r"vs\.?\s*RHE|potential\s*\(V|mA\s*cm|mAh"),
    ("mechanical", r"strain\s*\(%|stress\s*\(MPa"),
    ("thermal", r"heat\s*flow|weight\s*\(%.*temperature|temperature.*weight\s*\(%"),
    ("optical spectroscopy", r"wavelength\s*\(nm"),
    ("SEM", r"\bkV\b|\bWD\b|SE2|InLens|\bBSE\b|\bSEI\b"),
    ("EDS line scan", r"distance.*\b(?:[A-Z][a-z]?\s*[KL])\b"),
]
CUES = [(k, re.compile(v, re.I)) for k, v in CUES]
ENGINE = None


def engine():
    """One single-threaded engine per worker process. Without the cap, N processes x ~20 ONNX
    threads thrash the 20 cores and throughput collapses (measured 1.4 crop/s vs 3.6 capped)."""
    global ENGINE
    if ENGINE is None:
        for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
            os.environ[v] = "1"
        from rapidocr_onnxruntime import RapidOCR
        cuda = os.environ.get("OCR_CUDA", "1") == "1"
        ENGINE = RapidOCR(text_score=0.3, intra_op_num_threads=1, inter_op_num_threads=1,
                          det_limit_side_len=640, det_use_cuda=cuda, rec_use_cuda=cuda, cls_use_cuda=cuda,
                          rec_batch_num=int(os.environ.get("OCR_REC_BATCH", "32")),
                          cls_batch_num=int(os.environ.get("OCR_REC_BATCH", "32")))
    return ENGINE


def do_folder(args):
    folder, review_dir, review_quota = args
    folder = Path(folder)
    pj, oj = folder / "panels" / "panels.json", folder / "panels" / "ocr.json"
    if not pj.exists():
        return None
    if oj.exists():
        try:
            if json.load(open(oj)).get("run_version") == RUN_VERSION:
                return {"doi": folder.name, "resumed": True, "crops": [], "rows": [], "errors": []}
        except Exception:
            pass
    from PIL import Image
    import numpy as np
    try:
        det = json.load(open(pj))
    except Exception as e:
        return {"doi": folder.name, "resumed": False, "crops": [], "rows": [],
                "errors": [{"doi": folder.name, "file": "panels.json", "reason": str(type(e).__name__)}]}
    out_crops, rows, errors = [], [], []
    eng = engine()
    for fig in det.get("figures", []):
        for d in fig.get("detections", []):
            rel = d.get("crop")
            if not rel:
                continue
            p = folder / rel
            if not p.is_file():
                errors.append({"doi": folder.name, "file": rel, "reason": "crop missing"})
                continue
            try:
                im = Image.open(p).convert("RGB")
                w, h = im.size
                scale = 1
                if min(w, h) < 300:
                    scale = 2
                    im = im.resize((w * 2, h * 2))
                elif max(w, h) > 900:  # cap: 20% faster, same token count on the benchmark
                    scale = 900 / max(w, h)
                    im = im.resize((int(w * scale), int(h * scale)))
                res, _ = eng(np.array(im))
            except Exception as e:
                errors.append({"doi": folder.name, "file": rel, "reason": f"ocr failed: {type(e).__name__}"})
                continue
            toks, letter, lscore = [], None, None
            W, H = im.size
            for box, text, score in (res or []):
                xs = [pt[0] for pt in box]
                ys = [pt[1] for pt in box]
                bb = [int(min(xs) / scale), int(min(ys) / scale), int(max(xs) / scale), int(max(ys) / scale)]
                toks.append({"text": text, "box": bb, "score": round(float(score), 4)})
                m = LETTER_RX.match(text.strip())
                if m and letter is None:
                    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
                    if cx < 0.25 * W and cy < 0.25 * H:
                        letter, lscore = m.group(1).lower(), round(float(score), 4)
            joined = " ".join(t["text"] for t in toks)
            cues = [k for k, rx in CUES if rx.search(joined)]
            has_scale = bool(SCALE_RX.search(joined))
            if "SEM" in cues and not has_scale:
                cues.remove("SEM")
            if has_scale and not cues:
                cues.append("micrograph")
            rec = {"crop": rel, "detector_label": d["label"], "tokens": toks, "letter": letter,
                   "letter_score": lscore, "letter_agrees": (letter == d["label"].lower()) if letter else None,
                   "cues": cues, "n_tokens": len(toks),
                   "n_numeric_tokens": sum(1 for t in toks if NUMERIC_RX.match(t["text"].strip())),
                   "has_scale_bar": has_scale}
            out_crops.append(rec)
            rows.append({"doi": folder.name, "journal": folder.parent.name, "file": fig["file"], "crop": rel,
                         "detector_label": d["label"], "letter": letter, "letter_agrees": rec["letter_agrees"],
                         "cues": cues, "n_tokens": len(toks), "has_scale_bar": has_scale})
    json.dump({"run_version": RUN_VERSION, "host": os.uname().nodename,
               "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "crops": out_crops},
              open(oj, "w"), ensure_ascii=False)
    return {"doi": folder.name, "resumed": False, "crops": out_crops, "rows": rows, "errors": errors}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--host-idx", type=int, default=0)
    ap.add_argument("--n-hosts", type=int, default=1)
    ap.add_argument("--procs", type=int, default=18)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--sample", type=int, default=0)
    ap.add_argument("--tag", default="")
    ap.add_argument("--dois-file", default="", help="restrict to these DOI folder names, one per line")
    a = ap.parse_args()

    root, out = Path(a.root).expanduser(), Path(a.out_dir).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    wid = f"h{a.host_idx}{a.tag}"
    folders = sorted(p.parent for p in root.glob("*/*/data.json"))
    if a.dois_file:
        keep = {l.strip() for l in open(a.dois_file) if l.strip()}
        folders = [f for f in folders if f.name in keep]
    mine = [f for f in folders if zlib.crc32(f.name.encode()) % a.n_hosts == a.host_idx]
    if a.sample:
        import random
        random.Random(2).shuffle(mine)
        mine = mine[:a.sample]
    elif a.limit:
        mine = mine[:a.limit]
    print(f"[{wid}] {len(mine)} folders, {a.procs} procs, run_version={RUN_VERSION}", flush=True)

    man = open(out / f"manifest_{wid}.jsonl", "a")
    err = open(out / f"errors_{wid}.jsonl", "a")
    t0 = time.time()
    n_crop = n_letter = n_agree = n_resumed = n_empty = 0
    cues = Counter()
    with Pool(a.procs) as pool:
        for i, res in enumerate(pool.imap_unordered(do_folder, ((str(f), None, 0) for f in mine), chunksize=4), 1):
            if not res:
                continue
            n_resumed += bool(res["resumed"])
            for r in res["rows"]:
                man.write(json.dumps(r) + "\n")
                n_crop += 1
                n_empty += r["n_tokens"] == 0
                if r["letter"]:
                    n_letter += 1
                    n_agree += bool(r["letter_agrees"])
                cues.update(r["cues"])
            for e in res["errors"]:
                err.write(json.dumps(e) + "\n")
            if i % 500 == 0:
                dt = time.time() - t0
                print(f"[{wid}] {i}/{len(mine)} folders {n_crop} crops {n_crop/max(dt,1):.1f} crop/s "
                      f"letters {n_letter} agree {n_agree} resumed {n_resumed}", flush=True)
                man.flush(); err.flush()
    dt = time.time() - t0
    print(f"[{wid}] DONE {len(mine)} folders, {n_crop} crops, {n_letter} with a letter, {n_agree} agreeing, "
          f"{n_empty} with no tokens, {n_resumed} resumed, {dt/60:.1f} min, {n_crop/max(dt,1):.1f} crop/s", flush=True)
    print(f"[{wid}] cues: {dict(cues.most_common())}", flush=True)
    man.close(); err.close()


if __name__ == "__main__":
    sys.exit(main())
