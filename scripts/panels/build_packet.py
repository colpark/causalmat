"""Stage 7: build the human sample packet (400 figures) for the panel match run.

200 Tier A, 120 Tier B spread over its codes, 80 Tier C spread over its codes; stratified within each
tier by journal and panel count. 80 of the 400 are assigned to two annotators.

Usage: python build_packet.py --root ~/Documents/causalmat/matmech --out <packet dir> [--seed 0]
"""
import argparse
import csv
import json
import random
import textwrap
from collections import Counter, defaultdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args()
root, out = Path(a.root).expanduser(), Path(a.out).expanduser()
(out / "figures").mkdir(parents=True, exist_ok=True)
rng = random.Random(a.seed)

rows = [json.loads(l) for l in open(root / "match_run" / "manifest.jsonl")]
figs = defaultdict(list)
for r in rows:
    figs[(r["journal"], r["doi"], r["file"])].append(r)


def bucket(k):
    r = figs[k][0]
    return r["tier"], r["reason"], r["journal"], min(len(figs[k]), 6)


keys = list(figs)
rng.shuffle(keys)
by_tier = defaultdict(list)
for k in keys:
    by_tier[figs[k][0]["tier"]].append(k)


def stratified(pool, n):
    """Spread over reason code, then journal, then panel count."""
    groups = defaultdict(list)
    for k in pool:
        t, reason, j, npan = bucket(k)
        groups[reason].append(k)
    picked, codes = [], sorted(groups, key=lambda c: -len(groups[c]))
    while len(picked) < n and any(groups[c] for c in codes):
        for c in codes:
            if not groups[c] or len(picked) >= n:
                continue
            sub = defaultdict(list)
            for k in groups[c]:
                sub[(bucket(k)[2], bucket(k)[3])].append(k)
            cell = max(sub, key=lambda s: len(sub[s]))
            k = sub[cell].pop()
            groups[c].remove(k)
            picked.append(k)
    return picked


sample = stratified(by_tier["A"], 200) + stratified(by_tier["B"], 120) + stratified(by_tier["C"], 80)
rng.shuffle(sample)
double = set(rng.sample(sample, 80))

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
except Exception:
    font = small = ImageFont.load_default()

csv_rows, made, tier_counts = [], 0, Counter()
for j, doi, rel in sample:
    folder = root / j / doi
    mj = folder / "panels" / "match.json"
    if not mj.exists():
        continue
    fig = next((f for f in json.load(open(mj))["figures"] if f["file"] == rel), None)
    img = folder / rel
    if not fig or not img.is_file():
        continue
    try:
        im = Image.open(img).convert("RGB")
    except Exception:
        continue
    W, H = im.size
    scale = min(1.0, 1400 / max(W, 1))
    if scale < 1.0:
        im = im.resize((int(W * scale), int(H * scale)))
        W, H = im.size
    panels = [p for p in fig["panels"] if p.get("bbox")]
    strip = 26 + 34 * max(len(panels), 1)
    canvas = Image.new("RGB", (W, H + strip), (255, 255, 255))
    canvas.paste(im, (0, 0))
    dr = ImageDraw.Draw(canvas)
    for p in panels:
        x1, y1, x2, y2 = [int(v * scale) for v in p["bbox"]]
        dr.rectangle([x1, y1, x2, y2], outline=(200, 30, 30), width=3)
        dr.text((x1 + 5, y1 + 3), p["label"].upper(), fill=(200, 30, 30), font=font)
    dr.text((8, H + 5), f"{doi}  fig{fig['figure_number']}  tier {fig['tier']} ({fig['reason']})", fill=(0, 0, 0), font=small)
    for i, p in enumerate(panels or [{"label": "single", "definition": fig.get("caption_preamble", ""), "definition_source": "caption_preamble"}]):
        d = " ".join((p.get("definition") or "(none)").split())[:150]
        dr.text((8, H + 26 + 34 * i), f"{p['label'].upper()}: {d}", fill=(20, 20, 20), font=small)
        dr.text((8, H + 26 + 34 * i + 16), f"    source={p.get('definition_source')}  uses={len(p.get('use') or [])}", fill=(110, 110, 110), font=small)
    name = f"{fig['tier']}_{doi[:40]}_fig{fig['figure_number']}.jpg".replace("/", "_")
    canvas.save(out / "figures" / name, "JPEG", quality=88)
    tier_counts[fig["tier"]] += 1
    made += 1
    for p in (panels or [{"label": "single"}]):
        csv_rows.append({"file": name, "doi": doi, "figure": fig["figure_number"], "label": p["label"],
                         "tier": fig["tier"], "reason": fig["reason"],
                         "double_annotated": "yes" if (j, doi, rel) in double else "no",
                         "box_correct": "", "letter_correct": "", "definition_correct": "", "use_correct": "", "note": ""})

with open(out / "annotation.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(csv_rows[0]))
    w.writeheader()
    w.writerows(csv_rows)

open(out / "INSTRUCTIONS.md", "w").write(textwrap.dedent(f"""
    # Panel match review packet

    {made} figures ({dict(tier_counts)}), {len(csv_rows)} panel rows. Open `figures/` beside `annotation.csv`
    and fill one row per panel. Rows marked `double_annotated: yes` ({len(double)} figures) are reviewed by
    two people independently, for the agreement number.

    Each image shows the figure with detected panels boxed and lettered. Under it, per panel: the
    definition span assigned to it, where that span came from, and how many "use" sentences were attached.

    Fill `box_correct`, `letter_correct`, `definition_correct`, `use_correct` with **y**, **n** or **?**.

    - **box_correct = y** when the box holds exactly one panel, whole, with its scale bar or axes intact.
      Mark **n** if it splits a panel, merges two panels, or cuts off the axis or scale bar.
    - **letter_correct = y** when the letter drawn on the box is the panel's own label in the figure.
    - **definition_correct = y** when the printed span describes *that panel and no other*. A span covering
      two panels is **n**. An empty span is **n** only if the caption does define that panel.
    - **use_correct = y** when every listed sentence refers to that panel. Mark **n** if any sentence is
      about a different panel or figure. If there are no use sentences, leave blank.
    - Put anything odd in `note` (swapped caption, missing panel, figure is a table, and so on).

    Do not consult the original paper online. Judge only what the image and the printed spans show.
    """).strip() + "\n")

print(json.dumps({"figures_in_packet": made, "panel_rows": len(csv_rows), "tiers": dict(tier_counts),
                  "double_annotated_figures": len(double), "out": str(out)}, indent=1))
