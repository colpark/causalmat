"""Aggregate the v05 first-batch outputs: batch.csv, ab.json for the prior-graph ranks, summary.json.

Usage: python taxonomy/aggregate_v05.py --papers taxonomy/first100.jsonl --dir taxonomy/graphs_v05/first100 --n 32
"""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--papers", required=True)
ap.add_argument("--dir", required=True)
ap.add_argument("--n", type=int, default=32)
a = ap.parse_args()
D = Path(a.dir)
rows = [json.loads(l) for l in open(a.papers)][:a.n]


def base(r):
    return f"{r['journal']}__{r['doi']}".replace("/", "_")


def stats(g):
    obs = [n for n in g["nodes"] if n["type"].startswith("OBS")]
    return {
        "n_nodes": len(g["nodes"]), "n_edges": len(g["edges"]),
        "spine": sum(1 for n in g["nodes"] if n.get("spine")),
        "n_obs": len(obs),
        "n_obs_with_panel_ids": sum(1 for n in obs if n.get("panel_ids")),
        "n_panel_ids": sum(len(n.get("panel_ids") or []) for n in obs),
        "shown": sum(1 for n in g["nodes"] if n.get("image_support") == "shown"),
        "partial": sum(1 for n in g["nodes"] if n.get("image_support") == "partial"),
        "contradicts": sum(1 for n in g["nodes"] if n.get("image_support") == "contradicts"),
        "not_shown": sum(1 for n in g["nodes"] if n.get("image_support") == "not_shown"),
        "audits": sum(1 for n in g["nodes"] if n.get("image_support") in ("contradicts", "not_shown")
                      or (n.get("attrs") or {}).get("text_silent")),
        "panel_conditions": sum(1 for n in g["nodes"] if (n.get("attrs") or {}).get("panel_conditions")),
    }


out_rows, ab, missing = [], [], []
for r in rows:
    p = D / f"{base(r)}.json"
    if not p.exists():
        missing.append(r["rank"])
        continue
    g = json.load(open(p))
    s = stats(g)
    b = {}
    bp = D / f"{base(r)}.build.json"
    if bp.exists():
        b = json.load(open(bp))
    rev = g.get("review") or {}
    checks = rev.get("panel_checks") or []
    out_rows.append({
        "rank": r["rank"], "doi": r["doi"], "journal": r["journal"], "year": r.get("year"),
        "tier_A_share": r["tier_A_share"], "ocr_present": r["ocr_present"],
        "n_nodes": s["n_nodes"], "n_obs": s["n_obs"], "n_obs_with_panel_ids": s["n_obs_with_panel_ids"],
        "n_panel_ids": s["n_panel_ids"], "panels_offered": b.get("panels_offered"),
        "panels_cited": b.get("panels_cited"), "n_audits": s["audits"],
        "judge_verdict": rev.get("verdict", "pending"),
        "panel_checks": len(checks),
        "panel_checks_overturned": sum(1 for c in checks if c.get("ruling") == "overturned"),
        "new_type_proposals": 0,
    })
    if r.get("prior_graph"):
        old_path = Path(r["prior_graph"])
        if old_path.exists():
            old = json.load(open(old_path))
            o = stats(old)
            ab.append({"rank": r["rank"], "doi": r["doi"], "old_file": str(old_path),
                       "old": {k: o[k] for k in ("n_nodes", "spine", "shown", "partial", "audits", "n_obs_with_panel_ids")},
                       "new": {k: s[k] for k in ("n_nodes", "spine", "shown", "partial", "audits", "n_obs_with_panel_ids")},
                       "delta_nodes": s["n_nodes"] - o["n_nodes"], "delta_spine": s["spine"] - o["spine"],
                       "evidence_nodes_now_linked": s["n_obs_with_panel_ids"]})

nt = D / "new_types.jsonl"
n_new_types = sum(1 for _ in open(nt)) if nt.exists() else 0
for row in out_rows:
    row["new_type_proposals"] = n_new_types

with open(D / "batch.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out_rows[0]))
    w.writeheader()
    w.writerows(out_rows)
json.dump(ab, open(D / "ab.json", "w"), indent=1)

tot = {k: sum(r[k] or 0 for r in out_rows) for k in ("n_nodes", "n_obs", "n_obs_with_panel_ids", "n_panel_ids",
                                                     "panels_offered", "panels_cited", "n_audits",
                                                     "panel_checks", "panel_checks_overturned")}
summary = {
    "papers": len(out_rows), "missing_ranks": missing, "new_type_proposals": n_new_types,
    "totals": tot,
    "share_obs_linked": round(tot["n_obs_with_panel_ids"] / max(tot["n_obs"], 1), 3),
    "share_panels_cited": round(tot["panels_cited"] / max(tot["panels_offered"], 1), 3) if tot["panels_offered"] else None,
    "panel_check_overturn_rate": round(tot["panel_checks_overturned"] / max(tot["panel_checks"], 1), 3),
    "verdicts": dict(Counter(r["judge_verdict"] for r in out_rows)),
    "by_journal": dict(Counter(r["journal"] for r in out_rows).most_common()),
}
json.dump(summary, open(D / "summary.json", "w"), indent=1)
print(json.dumps(summary, indent=1))
