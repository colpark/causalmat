"""Migrate every round graph to the final vocabulary v04 and validate it.

Usage: python taxonomy/migrate.py
Writes taxonomy/graphs_v04/<paper_id with / -> __>.json. Applies the v01-v04 rename chains, v04 rename_attrs,
the three v04 conditional renames and the node fixes listed in rounds/r04/judge.md section 3.
"""
import glob
import json
import os
from collections import Counter

TAX = os.path.dirname(os.path.abspath(__file__))
OUT = f"{TAX}/graphs_v04"
os.makedirs(OUT, exist_ok=True)
v04 = json.load(open(f"{TAX}/vocab/v04.json"))
R = {}
for i in (1, 2, 3, 4):
    R.update(json.load(open(f"{TAX}/vocab/v0{i}.json")).get("renames", {}))
RA = v04.get("rename_attrs", {})

MODEL_REF_EDGES = {("Nature_Materials/10.1038_nmat2713", "b23"), ("Nano_Letters/10.1021_nl201541y", "a21"),
                   ("Nature_Materials/10.1038_s41563-024-01862-8", "d12")}
OBJECT_TRACK_EDGES = {("Advanced_Functional_Materials/10.1002_adfm.201901327", "o20", "s8"),
                      ("Advanced_Energy_Materials/aenm.201902373", "o26", "e6")}
NODE_FIX = {  # judge.md r04 section 3, items 3-4
    ("Biomaterials/j.biomaterials.2013.05.005", "d13"): {"type": "MEC/pathway"},
    ("Biomaterials/j.biomaterials.2013.05.005", "d14"): {"type": "PRF/service_capability"},
    ("Biomaterials/j.biomaterials.2013.05.005", "d23"): {"type": "OBS/response/distribution"},
    ("Progress_in_Organic_Coatings/j.porgcoat.2015.05.014", "n20"): {"type": "OBS/signal/feature_assignment", "modality": "spectrum"},
}
EDGE_FIX = {("Advanced_Materials/10.1002_adma.200903105", "a31", "a32"): "measure_feature_metric"}


def res(x):
    orig, seen = x, set()
    while x in R and x not in seen:
        seen.add(x)
        x = R[x]
    return x, [RA[s] for s in [orig, *seen] if s in RA]


types, ops, rels, mods = set(v04["types"]), set(v04["mm_ops"]), set(v04["rels"]), set(v04["modalities"])
problems, applied = [], Counter()
for f in sorted(glob.glob(f"{TAX}/rounds/r0*/graphs/*.json")):
    g = json.load(open(f))
    pid = g["paper_id"].replace("__", "/")
    g["paper_id"], g["vocab_version"], g["migrated_from"] = pid, "v04", f.split("/rounds/")[1]
    ids = {}
    for n in g["nodes"]:
        n["type"], extra = res(n["type"])
        for a in extra:
            n.setdefault("attrs", {}).update(a)
        for k, v in NODE_FIX.get((pid, n["id"]), {}).items():
            n[k] = v
            applied["node_fix"] += 1
        ids[n["id"]] = n
        if n["type"] not in types:
            problems.append(f"{pid}#{n['id']} type {n['type']}")
        if n["type"].startswith("OBS") and n.get("modality") not in mods:
            problems.append(f"{pid}#{n['id']} modality {n.get('modality')}")
    for e in g["edges"]:
        e["rel"], _ = res(e["rel"])
        if e["rel"] not in rels:
            problems.append(f"{pid} rel {e['rel']}")
        if e.get("mm_op"):
            op, extra = res(e["mm_op"])
            st = ids.get(e["src"], {}).get("type", "")
            if op == "track_feature_across_series" and st.startswith("OBS/signal"):
                op = "compare_across_conditions"; applied["track->compare"] += 1
            elif op == "compare_across_conditions" and (pid, e["src"], e["dst"]) in OBJECT_TRACK_EDGES:
                op = "track_feature_across_series"; applied["compare->track"] += 1
            elif op == "match_to_reference" and (pid, e["src"]) in MODEL_REF_EDGES:
                op = "overlay_model_on_data"; applied["match->overlay"] += 1
            if (pid, e["src"], e["dst"]) in EDGE_FIX:
                op = EDGE_FIX[(pid, e["src"], e["dst"])]; applied["edge_fix"] += 1
            for a in extra:
                e.setdefault("attrs", {}).update(a)
            e["mm_op"] = op
            if op not in ops:
                problems.append(f"{pid} {e['src']}->{e['dst']} mm_op {op}")
    json.dump(g, open(f"{OUT}/{pid.replace('/', '__')}.json", "w"), indent=1, ensure_ascii=False)

print(f"migrated {len(glob.glob(OUT + '/*.json'))} graphs; applied {dict(applied)}; problems {len(problems)}")
for p in problems[:30]:
    print("  !", p)
