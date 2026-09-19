"""Stage 4: merge both hosts' worker outputs into <root>/panels_run/.

Usage: python merge_run.py --root ~/Documents/causalmat/matmech --out ~/Documents/causalmat/matmech/panels_run \
         --parts ~/panels/out [--remote-parts /tmp/h1_out] --review 200 --review-mismatch 50
"""
import argparse
import glob
import json
import os
import random
import shutil
import time
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--parts", nargs="+", required=True, help="directories holding manifest_*.jsonl / errors_*.jsonl")
ap.add_argument("--review", type=int, default=200)
ap.add_argument("--review-mismatch", type=int, default=50)
a = ap.parse_args()

root, out = Path(a.root).expanduser(), Path(a.out).expanduser()
(out / "review").mkdir(parents=True, exist_ok=True)

man_rows, err_rows = [], []
with open(out / "manifest.jsonl", "w") as mf:
    for part in a.parts:
        for f in sorted(glob.glob(f"{Path(part).expanduser()}/manifest_*.jsonl")):
            for line in open(f):
                mf.write(line)
                man_rows.append(json.loads(line))
with open(out / "errors.jsonl", "w") as ef:
    for part in a.parts:
        for f in sorted(glob.glob(f"{Path(part).expanduser()}/errors_*.jsonl")):
            for line in open(f):
                ef.write(line)
                err_rows.append(json.loads(line))

hosts = Counter(r["host"] for r in man_rows)
hist = Counter(r["n_detections"] for r in man_rows)
labelled = [r for r in man_rows if r.get("caption_labels")]
crops = sum(1 for _ in glob.glob(str(root / "*/*/panels/crops/*.jpg")))
disk = sum(os.path.getsize(p) for p in glob.glob(str(root / "*/*/panels/crops/*.jpg"))) if crops else 0
folders = {p.parent.parent.name for p in root.glob("*/*/panels/panels.json")}
all_folders = {p.parent.name for p in root.glob("*/*/data.json")}
runs = {}
for p in list(root.glob("*/*/panels/panels.json"))[:200]:
    d = json.load(open(p))
    runs[d.get("run_version")] = runs.get(d.get("run_version"), 0) + 1

summary = {
    "figures_processed": len(man_rows),
    "figures_skipped": len(err_rows),
    "skip_reasons": dict(Counter(r["reason"] for r in err_rows)),
    "doi_folders_total": len(all_folders),
    "doi_folders_with_panels_json": len(folders),
    "doi_folders_missing": sorted(all_folders - folders)[:50],
    "panel_count_histogram": dict(sorted(hist.items())),
    "fraction_is_single": round(sum(r["is_single"] for r in man_rows) / max(len(man_rows), 1), 4),
    "fraction_two_level": round(sum(r["two_level"] for r in man_rows) / max(len(man_rows), 1), 4),
    "figures_with_caption_labels": len(labelled),
    "fraction_label_mismatch_of_labelled": round(sum(r["label_mismatch"] for r in labelled) / max(len(labelled), 1), 4),
    "caption_agreement_of_labelled": round(1 - sum(r["label_mismatch"] for r in labelled) / max(len(labelled), 1), 4),
    "figures_per_host": dict(hosts),
    "crops_written": crops,
    "crops_disk_bytes": disk,
    "run_versions_seen": runs,
    "merged_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}
json.dump(summary, open(out / "summary.json", "w"), indent=1)

# review overlays: random figures plus a mismatch-only sample
rng = random.Random(0)
by_file = {}
for r in man_rows:
    by_file[(r["journal"], r["doi"], r["file"])] = r
keys = list(by_file)
sample = rng.sample(keys, min(a.review, len(keys)))
mm_keys = [k for k in keys if by_file[k]["label_mismatch"]]
sample += rng.sample(mm_keys, min(a.review_mismatch, len(mm_keys)))
drawn = 0
for j, doi, rel in sample:
    folder = root / j / doi
    pj = folder / "panels" / "panels.json"
    if not pj.exists():
        continue
    figs = {f["file"]: f for f in json.load(open(pj))["figures"]}
    fig = figs.get(rel)
    img = folder / rel
    if not fig or not img.is_file():
        continue
    try:
        im = Image.open(img).convert("RGB")
    except Exception:
        continue
    dr = ImageDraw.Draw(im)
    for d in fig["detections"]:
        dr.rectangle(d["bbox"], outline=(200, 30, 30), width=3)
        dr.text((d["bbox"][0] + 4, d["bbox"][1] + 2), f"{d['label']} {d['score']:.2f}", fill=(200, 30, 30))
    tag = "MM_" if fig["label_mismatch"] else ""
    im.save(out / "review" / f"{tag}{doi}__{Path(rel).stem[:16]}.jpg", "JPEG", quality=88)
    drawn += 1
summary["review_overlays"] = drawn
json.dump(summary, open(out / "summary.json", "w"), indent=1)
print(json.dumps({k: v for k, v in summary.items() if k != "doi_folders_missing"}, indent=1))
