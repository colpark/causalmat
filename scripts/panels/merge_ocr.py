"""Merge both hosts' OCR output into <root>/ocr_run/ with a summary and a review sample.

Usage: python merge_ocr.py --root ~/Documents/causalmat/matmech --out <root>/ocr_run \
         --parts ~/panels/ocr_out ~/panels/ocr_out_h1 ~/panels/ocr_100 ~/panels/ocr_100_h1 \
         [--review 200 --review-disagree 100]
"""
import argparse
import glob
import json
import random
import time
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--parts", nargs="+", required=True)
ap.add_argument("--review", type=int, default=200)
ap.add_argument("--review-disagree", type=int, default=100)
a = ap.parse_args()
root, out = Path(a.root).expanduser(), Path(a.out).expanduser()
(out / "review").mkdir(parents=True, exist_ok=True)

rows, errs = [], []
seen = set()
with open(out / "manifest.jsonl", "w") as mf:
    for part in a.parts:
        for f in sorted(glob.glob(f"{Path(part).expanduser()}/manifest_*.jsonl")):
            for line in open(f):
                r = json.loads(line)
                k = (r["doi"], r["crop"])
                if k in seen:
                    continue
                seen.add(k)
                mf.write(line)
                rows.append(r)
with open(out / "errors.jsonl", "w") as ef:
    for part in a.parts:
        for f in sorted(glob.glob(f"{Path(part).expanduser()}/errors_*.jsonl")):
            for line in open(f):
                ef.write(line)
                errs.append(json.loads(line))

with_letter = [r for r in rows if r.get("letter")]
agree = [r for r in with_letter if r.get("letter_agrees")]
disagree = [r for r in with_letter if r.get("letter_agrees") is False]
cues = Counter(c for r in rows for c in (r.get("cues") or []))
summary = {
    "run_version": "rapidocr-ppocrv4/cuda-cap900/v1",
    "scope": "SEM + 3-modality subset (16,487 papers)",
    "crops_processed": len(rows),
    "crops_with_no_tokens": sum(1 for r in rows if r.get("n_tokens") == 0),
    "crops_with_letter": len(with_letter),
    "letter_agreement_rate": round(len(agree) / max(len(with_letter), 1), 4),
    "letter_disagreements": len(disagree),
    "crops_with_scale_bar": sum(1 for r in rows if r.get("has_scale_bar")),
    "cue_histogram": dict(cues.most_common()),
    "errors": len(errs),
    "error_reasons": dict(Counter(e.get("reason") for e in errs)),
    "papers": len({r["doi"] for r in rows}),
    "per_host": dict(Counter(r.get("host") or "?" for r in rows)),
    "merged_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}

# review: crops spread over cue classes, plus letter disagreements, each drawn with its OCR boxes
rng = random.Random(0)
by_cue = {}
for r in rows:
    for c in (r.get("cues") or ["(none)"]):
        by_cue.setdefault(c, []).append(r)
pick, per = [], max(1, a.review // max(len(by_cue), 1))
for c, lst in by_cue.items():
    pick += rng.sample(lst, min(per, len(lst)))
pick = pick[:a.review] + rng.sample(disagree, min(a.review_disagree, len(disagree)))

drawn = 0
for r in pick:
    folder = root / r["journal"] / r["doi"]
    crop = folder / r["crop"]
    oj = folder / "panels" / "ocr.json"
    if not crop.is_file() or not oj.exists():
        continue
    try:
        rec = next((c for c in json.load(open(oj))["crops"] if c["crop"] == r["crop"]), None)
        im = Image.open(crop).convert("RGB")
    except Exception:
        continue
    if not rec:
        continue
    dr = ImageDraw.Draw(im)
    for t in rec.get("tokens") or []:
        dr.rectangle(t["box"], outline=(200, 30, 30), width=2)
        dr.text((t["box"][0] + 2, max(t["box"][1] - 12, 0)), f"{t['text'][:14]} {t['score']:.2f}", fill=(200, 30, 30))
    tag = "DIS_" if r.get("letter_agrees") is False else ""
    cue = (r.get("cues") or ["none"])[0].replace(" ", "_")
    im.save(out / "review" / f"{tag}{cue}__{r['doi'][:36]}__{Path(r['crop']).stem[:14]}.jpg", "JPEG", quality=88)
    drawn += 1
summary["review_crops"] = drawn
json.dump(summary, open(out / "summary.json", "w"), indent=1)
print(json.dumps({k: v for k, v in summary.items() if k != "cue_histogram"}, indent=1))
print("cues:", summary["cue_histogram"])
