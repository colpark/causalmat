"""Embed panel crops, their caption spans and their OCR facts into the modality-view specs.

Everything is copied verbatim from the stores: the crop pixels, the definition span and the use sentences
from match.json, and letter/tier/ocr_agrees/cues from panels.json, match.json and ocr.json. No caption is
generated, because the point of showing a crop beside its span is that a reader can see whether they agree.

Usage: python taxonomy/embed_panels.py --root <matmech> --specs taxonomy/specs_v05 [--max-mb 12]
"""
import argparse
import base64
import io
import json
import re
from collections import Counter
from pathlib import Path

from PIL import Image

SCALE_RX = re.compile(r"\b\d+(?:\.\d+)?\s*(?:nm|µm|μm|um|mm|Å)\b", re.I)


def encode(path, cap=900, q=80):
    with Image.open(path) as im:
        im = im.convert("RGB")
        if max(im.size) > cap:
            r = cap / max(im.size)
            im = im.resize((max(int(im.size[0] * r), 1), max(int(im.size[1] * r), 1)))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def build(root, spec_path, max_mb, figs_cap=900, crop_cap=900):
    spec = json.load(open(spec_path))
    pid = spec["doi"]                      # "<journal>/<doi folder>"
    folder = root / pid
    cited = []
    for n in spec["nodes"]:
        for p in n.get("panel_ids") or []:
            if p not in cited:
                cited.append(p)
    if not cited:
        return spec, {"panels": 0, "missing": {}, "note": None}

    match = json.load(open(folder / "panels" / "match.json"))
    det = json.load(open(folder / "panels" / "panels.json"))
    oj = folder / "panels" / "ocr.json"
    ocr = {c["crop"]: c for c in json.load(open(oj))["crops"]} if oj.exists() else None

    rec = json.load(open(folder / "data.json", encoding="utf-8"))
    order = {im.get("image_path"): i for i, im in enumerate(rec.get("image_info") or [], 1)}
    det_by_crop = {d.get("crop"): d for f in det.get("figures", []) for d in f.get("detections", []) if d.get("crop")}

    # canonical id -> (match figure record, match panel record, figure number)
    index = {}
    for f in match.get("figures", []):
        fi = order.get(f["file"], "?")
        for p in f["panels"]:
            lab = p["label"]
            key = f"F{fi}{'' if lab == 'single' else lab}"
            index[key] = (f, p, fi)

    panels, missing = {}, {}
    for cid in cited:
        key = cid.split("#")[-1]
        hit = index.get(key)
        if not hit:
            missing[cid] = "no panel record (tier C figure, inset, or id not in this paper's store)"
            continue
        f, p, fi = hit
        crop_rel = p.get("crop")
        if not crop_rel or not (folder / crop_rel).is_file():
            missing[cid] = "no crop file (single-panel figure or broken record)"
            continue
        o = ocr.get(crop_rel) if ocr else None
        entry = {
            "src": encode(folder / crop_rel, cap=crop_cap),
            "figure": f"F{fi}", "letter": p["label"],
            "tier": f["tier"],
            "ocr_agrees": (o.get("letter_agrees") if o else None),
            # verbatim from match.json; B1_caption_empty keeps an empty definition rather than a guess
            "definition": "" if f["reason"] == "B1_caption_empty" else (p.get("definition") or ""),
            "use": list(p.get("use") or []),
        }
        if o:
            cues = list(o.get("cues") or [])
            sc = SCALE_RX.search(" ".join(t["text"] for t in o.get("tokens") or []))
            if sc:
                cues.append(f"scale bar {sc.group(0)}")
            if cues:
                entry["cues"] = cues
        panels[cid] = entry

    # whole figures for context, only those a node actually cites
    figs_wanted = sorted({fg for n in spec["nodes"] for fg in (n.get("figs") or [])})
    figs = {}
    rec_imgs = {f"F{i}": im for i, im in enumerate(rec.get("image_info") or [], 1)}
    for fg in figs_wanted:
        im = rec_imgs.get(fg)
        if not im:
            continue
        p = folder / (im.get("image_path") or "")
        if p.is_file():
            cap = " ".join(im.get("image_caption") or [])
            figs[fg] = {"src": encode(p, cap=figs_cap), "caption": re.sub(r"\s+", " ", cap)[:400]}

    spec["panels"] = panels
    spec["figs"] = figs
    note = None
    size = len(json.dumps(spec)) / 1e6
    if size > max_mb:                      # budget: drop whole figures first, then shrink crops
        spec["figs"] = {}
        note = f"whole-figure images dropped to stay under {max_mb} MB (page was {size:.1f} MB)"
        size = len(json.dumps(spec)) / 1e6
        if size > max_mb:
            for cid, e in spec["panels"].items():
                src = folder / index[cid.split('#')[-1]][1]["crop"]
                e["src"] = encode(src, cap=700, q=75)
            note += "; crops re-encoded at 700 px"
    if missing:
        note = (note + "; " if note else "") + "; ".join(f"{k}: {v}" for k, v in list(missing.items())[:12])
    if note:
        spec["assets_note"] = note
    return spec, {"panels": len(panels), "missing": missing, "note": note,
                  "figs": len(spec["figs"]), "mb": round(len(json.dumps(spec)) / 1e6, 2)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--specs", required=True)
    ap.add_argument("--max-mb", type=float, default=12.0)
    a = ap.parse_args()
    root, D = Path(a.root).expanduser(), Path(a.specs).expanduser()
    rows, reasons = [], Counter()
    for sp in sorted(D.glob("*.json")):
        if sp.name in ("photo_auto.json", "ceramic_auto.json"):
            continue
        spec, st = build(root, sp, a.max_mb)
        json.dump(spec, open(sp, "w"), ensure_ascii=False)
        for v in st["missing"].values():
            reasons[v.split(" (")[0]] += 1
        rows.append({"spec": sp.name, **{k: st[k] for k in ("panels", "figs", "mb")},
                     "missing": len(st["missing"]), "note": bool(st["note"])})
        print(f"{sp.name:62s} panels {st['panels']:3d}  figs {st.get('figs', 0):2d}  {st['mb']:6.2f} MB"
              + (f"  missing {len(st['missing'])}" if st["missing"] else ""))
    json.dump(rows, open(D / "embed_report.json", "w"), indent=1)
    print(f"\n{len(rows)} specs, {sum(r['panels'] for r in rows)} panels embedded, "
          f"{sum(r['missing'] for r in rows)} ids missing, largest {max(r['mb'] for r in rows):.2f} MB")
    print("missing reasons:", dict(reasons))
