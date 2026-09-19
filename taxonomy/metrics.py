"""Validate a round's graphs and compute saturation metrics.

Usage: python taxonomy/metrics.py <round>
Reads rounds/rXX/graphs/*.json, vocab v(r-1) (used by staff) and v(r) (written by the judge, if present).
Appends one line to taxonomy/metrics.jsonl and prints it.
"""
import glob
import json
import os
import sys
from collections import Counter

TAX = os.path.dirname(os.path.abspath(__file__))
r = int(sys.argv[1])
old = json.load(open(f"{TAX}/vocab/v{r - 1:02d}.json"))
newp = f"{TAX}/vocab/v{r:02d}.json"
new = json.load(open(newp)) if os.path.exists(newp) else None

graphs = [json.load(open(f)) for f in sorted(glob.glob(f"{TAX}/rounds/r{r:02d}/graphs/*.json"))]
problems, types, rels, ops, mods = [], Counter(), Counter(), Counter(), Counter()
n_nodes = n_edges = covered = obs_fig_edges = obs_fig_edges_with_op = 0
for g in graphs:
    ids = {n["id"]: n for n in g["nodes"]}
    for n in g["nodes"]:
        n_nodes += 1
        types[n["type"]] += 1
        covered += n["type"] in old["types"]
        if n["type"].startswith("OBS"):
            mods[n.get("modality")] += 1
            if not n.get("modality"):
                problems.append(f"{g['paper_id']}#{n['id']} OBS without modality")
    for e in g["edges"]:
        n_edges += 1
        rels[e["rel"]] += 1
        if e["src"] not in ids or e["dst"] not in ids:
            problems.append(f"{g['paper_id']} edge {e} references a missing node")
            continue
        s = ids[e["src"]]
        if s["type"].startswith("OBS") and s.get("figs"):
            obs_fig_edges += 1
            if e.get("mm_op"):
                obs_fig_edges_with_op += 1
                ops[e["mm_op"]] += 1

row = {
    "round": r, "papers": len(graphs), "nodes": n_nodes, "edges": n_edges,
    "nodes_per_paper": round(n_nodes / max(len(graphs), 1), 1),
    "coverage_by_prev_vocab": round(covered / max(n_nodes, 1), 3),
    "distinct_types_used": len(types), "distinct_mm_ops_used": len(ops),
    "obs_figure_edges_with_mm_op": f"{obs_fig_edges_with_op}/{obs_fig_edges}",
    "vocab_types_prev": len(old["types"]), "vocab_mm_ops_prev": len(old.get("mm_ops", {})),
}
if new:
    added = set(new["types"]) - set(old["types"])
    removed = set(old["types"]) - set(new["types"])
    leaves = lambda v: {t for t in v if not any(u.startswith(t + "/") for u in v)}
    add_leaves = leaves(new["types"]) - leaves(old["types"])
    row.update({
        "vocab_types_new": len(new["types"]), "types_added": len(added), "types_removed": len(removed),
        "leaves_added": len(add_leaves), "leaves_added_per_paper": round(len(add_leaves) / max(len(graphs), 1), 2),
        "mm_ops_added": len(set(new.get("mm_ops", {})) - set(old.get("mm_ops", {}))),
        "rels_added": len(set(new["rels"]) - set(old["rels"])),
        "modalities_added": len(set(new["modalities"]) - set(old["modalities"])),
    })
row["validation_problems"] = len(problems)
with open(f"{TAX}/metrics.jsonl", "a") as f:
    f.write(json.dumps(row) + "\n")
print(json.dumps(row, indent=1))
for p in problems[:20]:
    print("  !", p)
print("top types:", types.most_common(12))
print("modalities:", dict(mods))
print("rels:", dict(rels))
