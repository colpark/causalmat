"""graph_diff_v05_v06.py: per paper, what changed between the v05 graph (built with the MatMech block in the packet) and
the v06 graph (no MatMech, captions only). Optional args: <old_dir> <new_dir> <title> for any other pair. Spine nodes are matched by label content (Jaccard >= 0.25), then remaining
nodes whose full type is unique on both sides are paired as the same slot reworded; a matched pair whose top-level type
differs is 'retyped'. Evidence (OBS) nodes are matched by shared panel ids, else by label content. Audits are OBS nodes
with a qualifies / contrasts / rules_out edge.   python trace_kit/graph_diff_v05_v06.py <papers.txt> <out.md> <out.json>"""
import json, sys
from collections import Counter
sys.path.insert(0, 'trace_kit'); from cut_traces import cwords
AUD = {"qualifies", "contrasts", "rules_out"}
def sim(a, b):
    A, B = cwords(a), cwords(b); return len(A & B) / len(A | B) if A and B else 0
def match(A, B, key):
    pairs = sorted(((key(x, y), x["id"], y["id"]) for x in A for y in B), reverse=True)
    ua, ub, m = set(), set(), []
    for s, x, y in pairs:
        if s < 0.25 or x in ua or y in ub: continue
        ua.add(x); ub.add(y); m.append((x, y))
    Ad = {n["id"]: n for n in A}; Bd = {n["id"]: n for n in B}
    ra = [x for x in Ad if x not in ua]; rb = [y for y in Bd if y not in ub]
    ca = Counter(Ad[x]["type"] for x in ra); cb = Counter(Bd[y]["type"] for y in rb)
    for x in ra:
        t = Ad[x]["type"]
        if ca[t] == 1 and cb[t] == 1:
            y = next(y for y in rb if Bd[y]["type"] == t); ua.add(x); ub.add(y); m.append((x, y))
    return m, [x for x in Ad if x not in ua], [y for y in Bd if y not in ub]
def obs_key(x, y):
    px, py = set(x.get("panel_ids") or []), set(y.get("panel_ids") or [])
    return 1.0 if px & py else sim(x["label"], y["label"])
def audits(g):
    ids = {e["src"] for e in g["edges"] if e["rel"] in AUD}
    return [n for n in g["nodes"] if n["id"] in ids]
res = {}; L = ["# v06 graphs against v05: what the MatMech block (and the linked text) shaped", "",
               "Every verdict here is model against model; no human checked any item.", "",
               "v05 packets carried MatMech's mechanisms, tetrahedron summary and per-figure linked text; v06 packets carry captions and the panel section only (text_source: captions_only). Differences below mix two causes: the MatMech block removed, and the paper's body text removed with it.", ""]
OLD = sys.argv[4] if len(sys.argv) > 4 else "taxonomy/graphs_v05/first100"
NEW = sys.argv[5] if len(sys.argv) > 5 else "taxonomy/graphs_v06"
TITLE = sys.argv[6] if len(sys.argv) > 6 else None
if TITLE: L[0] = f"# {TITLE}"; L[4] = f"Old graphs: {OLD}. New graphs: {NEW}."
for pid in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    P = pid.replace("/", "__")
    a = json.load(open(f"{OLD}/{P}.json")); b = json.load(open(f"{NEW}/{P}.json"))
    sa = [n for n in a["nodes"] if n.get("spine")]; sb = [n for n in b["nodes"] if n.get("spine")]
    m, dr, ad = match(sa, sb, lambda x, y: sim(x["label"], y["label"]))
    A = {n["id"]: n for n in a["nodes"]}; B = {n["id"]: n for n in b["nodes"]}
    ret = [(x, y) for x, y in m if A[x]["type"].split("/")[0] != B[y]["type"].split("/")[0] or A[x]["type"] != B[y]["type"]]
    oa = [n for n in a["nodes"] if n["type"].startswith("OBS")]; ob = [n for n in b["nodes"] if n["type"].startswith("OBS")]
    om, odr, oad = match(oa, ob, obs_key)
    aa, ab = audits(a), audits(b); am, adr, aad = match(aa, ab, obs_key)
    mec_a = [n for n in a["nodes"] if n["type"].startswith("MEC")]; mec_b = [n for n in b["nodes"] if n["type"].startswith("MEC")]
    r = {"spine_v05": len(sa), "spine_v06": len(sb), "spine_matched": len(m), "spine_dropped": [(x, A[x]["type"], A[x]["label"]) for x in dr],
         "spine_added": [(y, B[y]["type"], B[y]["label"]) for y in ad], "spine_retyped": [(x, A[x]["type"], y, B[y]["type"]) for x, y in ret],
         "spine_changed_frac": round((len(dr) + len(ret)) / max(1, len(sa)), 2),
         "evidence_v05": len(oa), "evidence_v06": len(ob), "evidence_dropped": len(odr), "evidence_added": len(oad),
         "audits_v05": len(aa), "audits_v06": len(ab), "audits_dropped": [(x, A[x]["label"]) for x in adr], "audits_added": [(y, B[y]["label"]) for y in aad],
         "mec_v05": len(mec_a), "mec_v06": len(mec_b),
         "matmech": (b.get("review") or {}).get("matmech", {})}
    r["matmech"] = {k: r["matmech"].get(k) for k in ("supports", "contradicts", "not_covered")}
    res[P] = r
    L += [f"## {P}", f"- spine: {len(sa)} -> {len(sb)}; matched {len(m)}, dropped {len(dr)}, added {len(ad)}, retyped {len(ret)} (changed {r['spine_changed_frac']:.0%} of v05 spine)",
          f"- MEC nodes: {len(mec_a)} -> {len(mec_b)}", f"- evidence nodes: {len(oa)} -> {len(ob)} (dropped {len(odr)}, added {len(oad)})",
          f"- audits: {len(aa)} -> {len(ab)} (dropped {len(adr)}, added {len(aad)})",
          f"- MatMech pairs (judge, v06 graph): supports {r['matmech']['supports']}, contradicts {r['matmech']['contradicts']}, not covered {r['matmech']['not_covered']}"]
    for x, t, l in r["spine_dropped"]: L.append(f"  - dropped {x} [{t}]: {l[:110]}")
    for y, t, l in r["spine_added"]: L.append(f"  - added {y} [{t}]: {l[:110]}")
    for x, t, y, u in r["spine_retyped"]: L.append(f"  - retyped {x} [{t}] -> {y} [{u}]")
    L.append("")
open(sys.argv[2], "w").write("\n".join(L) + "\n"); json.dump(res, open(sys.argv[3], "w"), indent=1)
for P, r in res.items(): print(P[:45].ljust(46), r["spine_v05"], "->", r["spine_v06"], "changed", r["spine_changed_frac"], "MEC", r["mec_v05"], "->", r["mec_v06"], "ev", r["evidence_v05"], "->", r["evidence_v06"], "aud", r["audits_v05"], "->", r["audits_v06"])
