"""Select the first 100 papers for the v05 argument-graph batch.

Ranks 1-8  : papers already graphed in taxonomy/graphs_v04 that meet the SEM + 3-modality rule.
Ranks 9-100: new papers, journal-stratified, requiring
             - SEM confirmed on an accepted (tier A/B) panel, not just in the methods text
             - two or more further figure-backed modalities
             - 4 to 12 figures with at least 60% of them in tier A or B
             - year 2012 or later

Usage: python taxonomy/select_first100.py --root ~/Documents/causalmat/matmech \
         --supply ~/panels/fm_supply_papers.json --out taxonomy/first100.jsonl
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, "/home/aid1/panels")
from panel_modalities import classify  # noqa: E402

SEM_RX = re.compile(r"\bSEM\b|scanning electron|FE-?SEM|\bBSE\b image|secondary electron", re.I)
MICRO_MODS = {"electron micrograph"}

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
ap.add_argument("--supply", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--n", type=int, default=100)
a = ap.parse_args()
root = Path(a.root).expanduser()
supply = {r["doi"]: r for r in json.load(open(Path(a.supply).expanduser()))}
graphed = {}
for p in Path("taxonomy/graphs_v04").glob("*.json"):
    g = json.load(open(p))
    graphed[g["paper_id"].split("/")[-1]] = p.name


def inspect(doi, journal):
    """Panel-level evidence for one paper."""
    folder = root / journal / doi
    mj = folder / "panels" / "match.json"
    if not mj.exists():
        return None
    try:
        m = json.load(open(mj))
        rec = json.load(open(folder / "data.json", encoding="utf-8"))
    except Exception:
        return None
    figs = m.get("figures", [])
    if not figs:
        return None
    tiers = Counter(f["tier"] for f in figs)
    ab = tiers["A"] + tiers["B"]
    sem_panel, fig_mods, n_panels = False, set(), 0
    for f in figs:
        if f["tier"] == "C":
            continue
        pre = f.get("caption_preamble") or ""
        for p in f["panels"]:
            n_panels += 1
            text = f"{p.get('definition') or ''} {pre}"
            if SEM_RX.search(text):
                sem_panel = True
            techs, form = classify(text)
            for t in techs:
                fig_mods.add(t)
    other = {t for t in fig_mods if t not in ("SEM",)}
    return {"doi": doi, "journal": journal, "year": rec.get("year"), "title": rec.get("title"),
            "material": rec.get("material_object"), "n_figures": len(figs),
            "tier_A": tiers["A"], "tier_B": tiers["B"], "tier_C": tiers["C"],
            "tier_A_share": round(tiers["A"] / max(len(figs), 1), 3),
            "tier_AB_share": round(ab / max(len(figs), 1), 3),
            "sem_on_panel": sem_panel, "panel_techniques": sorted(fig_mods),
            "n_other_figure_modalities": len(other), "n_panels": n_panels,
            "ocr_present": (folder / "panels" / "ocr.json").exists(),
            "supply_modalities": supply[doi]["modalities"] if doi in supply else []}


rows, seen = [], set()
# ranks 1-8: already graphed and in the SEM + 3-modality set
prior = []
for doi, fname in sorted(graphed.items()):
    if doi in supply:
        journal = supply[doi]["journal"]
        info = inspect(doi, journal)
        if info:
            info["prior_graph"] = f"taxonomy/graphs_v04/{fname}"
            prior.append(info)
prior.sort(key=lambda r: (-r["tier_AB_share"], -r["n_panels"]))
for r in prior[:8]:
    r["rank"] = len(rows) + 1
    rows.append(r)
    seen.add(r["doi"])
print(f"ranks 1-{len(rows)}: prior graphs meeting the rule ({len(prior)} candidates)")

# ranks 9-100: new, journal-stratified
cands = defaultdict(list)
for doi, s in supply.items():
    if doi in seen or not isinstance(s.get("year"), int) or s["year"] < 2012:
        continue
    info = inspect(doi, s["journal"])
    if not info:
        continue
    if not info["sem_on_panel"] or info["n_other_figure_modalities"] < 2:
        continue
    if not (4 <= info["n_figures"] <= 12) or info["tier_AB_share"] < 0.6:
        continue
    cands[s["journal"]].append(info)
for j in cands:
    cands[j].sort(key=lambda r: (-r["tier_A_share"], -r["n_other_figure_modalities"], -r["n_panels"], r["doi"]))
print("candidates per journal:", {k: len(v) for k, v in sorted(cands.items())})

journals = sorted(cands, key=lambda j: -len(cands[j]))
while len(rows) < a.n and any(cands[j] for j in journals):
    for j in journals:
        if len(rows) >= a.n or not cands[j]:
            continue
        r = cands[j].pop(0)
        r["rank"] = len(rows) + 1
        r["prior_graph"] = None
        rows.append(r)
        seen.add(r["doi"])

with open(a.out, "w") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"wrote {len(rows)} papers to {a.out}")
print("by journal:", dict(Counter(r["journal"] for r in rows).most_common()))
print("ocr present:", sum(r["ocr_present"] for r in rows), "| median figures:",
      sorted(r["n_figures"] for r in rows)[len(rows) // 2])
