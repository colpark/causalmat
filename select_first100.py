"""Select the first 100 papers for graph building from the FM supply target list.

Input : fm_supply_papers.json  (written by scripts/panels/fm_supply.py beside fm_supply.json;
        16,487 records: SEM papers with 3+ FM-addressable modalities)
Output: first100.jsonl, first100_summary.json

Rule (deterministic; rerunning on the same input gives the same 100):
  Eligibility
    E1  SEM confirmed on an accepted panel: "panels" in sem_sources
    E2  at least two modalities besides SEM's own bucket are panel-sourced (figure-backed, not methods text)
    E3  4 <= n_figures <= 12, and figures_AB / n_figures >= 0.6   (bounded cost, mostly accepted figures)
    E4  year >= 2012
  Ordering
    the 8 already-graphed papers that meet the rule come first (A/B slot against the old graphs)
    then score = 2*panel_modalities + 3*coverage + formula_joinable + 0.1*min(figures_AB, 10)
    journal quota proportional to the target set, rounded, minimum 2 per journal
    ties broken by doi string
Usage: python select_first100.py --papers fm_supply_papers.json --out first100
"""
import argparse, json, math
from collections import Counter, defaultdict

PRIORITY = [  # journal/doi of graphs_v04 papers meeting SEM + >=3 FM modalities
    "Advanced_Energy_Materials/aenm.201401880", "Advanced_Energy_Materials/aenm.201701686",
    "Bioactive_Materials/j.bioactmat.2020.02.005", "Journal_of_Magnesium_and_Alloys/j.jma.2013.12.002",
    "Journal_of_Materials_Science_&_Technology/j.jmst.2019.10.041",
    "Progress_in_Organic_Coatings/j.porgcoat.2011.04.010",
    "Rare_Metals/s12598-017-0936-3", "Rare_Metals/s12598-020-01698-6",
]
SEM_BUCKET = "electron micrograph"


def eligible(r):
    if "panels" not in r.get("sem_sources", []):
        return False, "E1"
    src = r.get("modality_sources", {})
    panel_mods = [m for m, s in src.items() if "panels" in s and m != SEM_BUCKET]
    if len(panel_mods) < 2:
        return False, "E2"
    nf, ab = r.get("n_figures", 0), r.get("figures_AB", 0)
    if not (4 <= nf <= 12) or nf == 0 or ab / nf < 0.6:
        return False, "E3"
    if not isinstance(r.get("year"), int) or r["year"] < 2012:
        return False, "E4"
    return True, ""


def score(r):
    src = r.get("modality_sources", {})
    panel_mods = sum(1 for m, s in src.items() if "panels" in s and m != SEM_BUCKET)
    cov = r["figures_AB"] / max(r["n_figures"], 1)
    return 2 * panel_mods + 3 * cov + (1 if r.get("formula_joinable") else 0) + 0.1 * min(r["figures_AB"], 10)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", required=True)
    ap.add_argument("--out", default="first100")
    ap.add_argument("--n", type=int, default=100)
    a = ap.parse_args()
    rows = json.load(open(a.papers, encoding="utf-8"))
    key = lambda r: f"{r['journal']}/{r['doi']}"
    by_key = {key(r): r for r in rows}

    picked, why = [], Counter()
    for k in PRIORITY:                      # A/B slot: old graphs exist for these
        if k in by_key:
            r = dict(by_key[k]); r["slot"] = "ab_rebuild"; picked.append(r)
    chosen = {key(r) for r in picked}

    pool = []
    for r in rows:
        if key(r) in chosen:
            continue
        ok, code = eligible(r)
        if ok:
            pool.append(r)
        else:
            why[code] += 1
    pool.sort(key=lambda r: (-score(r), key(r)))

    n_rest = a.n - len(picked)
    share = Counter(r["journal"] for r in rows)
    total = sum(share.values())
    quota = {j: max(2, round(n_rest * c / total)) for j, c in share.items()}
    taken = defaultdict(int)
    for r in pool:                          # first pass: within quota
        if len(picked) >= a.n:
            break
        if taken[r["journal"]] < quota[r["journal"]]:
            r = dict(r); r["slot"] = "new"; picked.append(r); taken[r["journal"]] += 1
    for r in pool:                          # second pass: fill remaining seats by score
        if len(picked) >= a.n:
            break
        if key(r) not in {key(p) for p in picked}:
            r = dict(r); r["slot"] = "new_fill"; picked.append(r)

    with open(a.out + ".jsonl", "w", encoding="utf-8") as fh:
        for i, r in enumerate(picked, 1):
            r["rank"] = i; r["score"] = round(score(r), 3)
            fh.write(json.dumps(r) + "\n")
    summary = {"input_papers": len(rows), "eligible_pool": len(pool), "rejected_by_rule": dict(why),
               "selected": len(picked), "by_slot": dict(Counter(r["slot"] for r in picked)),
               "by_journal": dict(Counter(r["journal"] for r in picked)),
               "by_year": dict(sorted(Counter(r["year"] for r in picked).items())),
               "modality_combos": dict(Counter(" + ".join(r["modalities"]) for r in picked).most_common(10))}
    json.dump(summary, open(a.out + "_summary.json", "w"), indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
