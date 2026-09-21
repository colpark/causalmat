"""cut_traces.py: cut reasoning traces from a full v05 argument graph.

Inputs : the v05 graph JSON and its collapsed spec (for necessity labels).
Output : traces.json with one record per trace, open or closed, each carrying
         root, subtype, lift, floor ruling, measured depth, mask, grader, and the
         ordered walk through the graph (node ids with roles).

Rules (see the design note):
  R1 seed at a claim where an FM-lane evidence node is necessary or corrective
  R2 site on a branch point (a choice with an alternative visible)
  R3 root from the resolving edge; subtype from mm_op
  R4 bare infer is lifted (rejection / budget / stopping rule) or closed
  R5 floor rebuilt with FM-lane evidence removed (and the grader channel held out)
  R6 measured depth by leave-one-family-out
  R7 mask by root
  R9 one group id per graph
"""
import json, sys, re, os, inspect
from collections import defaultdict
V2 = False   # cutter v2 (v06 pilot): switched on by cut() when the graph is a v06 graph (batch v06_pilot)
# v2.2 (v06c): before the solving gate only three hard rules apply (panel matches node, answer findable from what is
# given, nothing reveals the answer). The v1 filters (bare-infer closure, floor-reaches closure, plot-read and depth-one
# control strata) are off on v06 graphs unless --v1-filters is passed; when off, what they would have ruled is kept in
# t["v1_filter"] so the gate verdict can be compared against it.
V1F = "--v1-filters" in sys.argv
def here(): return f"cut_traces.py:{inspect.stack()[1].lineno}"
def mark(t, rule, effect): t.setdefault("v2_rules", []).append({"rule": rule, "where": f"cut_traces.py:{inspect.stack()[1].lineno}", "effect": effect})

FM_FAMILIES = {"SEM", "TEM", "XRD", "XAS", "ATOM"}
SUBTYPE = {"measure_feature_metric": "estimate", "read_trend": "estimate", "read_characteristic_point": "estimate",
           "assign_features": "classify", "recognize_signature": "classify", "inspect_local_feature": "classify",
           "compare_across_conditions": "rank", "cross_check_consistency": "check", "correlate_across_series": "rank"}
AUDIT_RELS = {"qualifies", "contrasts", "rules_out"}
SPINE_RELS = {"motivates", "realizes", "feeds_into", "produces", "causes", "explains", "supports"}
ORACLES = {"XRD": "pymatgen/GSAS-II pattern simulation", "ATOM": "universal MLIP + DFT single point",
           "XAS": "FEFF/OmniXAS", "TEM": "abTEM multislice", "SEM": None, "PROCESS": None}


def family(n):
    # FIX (orchestrator, 2026-09-20, cut_traces.py:31): technique_norm may be a LIST when a node's panel
    # comes from two instruments ("SEM-EDS", "AC HAADF-STEM with line profiles"); the v05 back-fill writes
    # those as lists. Take the first element, which is what the lane rule keys on too.
    t = (n.get("attrs") or {}).get("technique_norm") or (n.get("attrs") or {}).get("technique") or ""
    if isinstance(t, list):
        t = t[0] if t else ""
    return str(t).split(":")[0].upper()


def load(graph_path, spec_path):
    g = json.load(open(graph_path)); s = json.load(open(spec_path))
    N = {n["id"]: n for n in g["nodes"]}
    inn, out = defaultdict(list), defaultdict(list)
    for e in g["edges"]:
        inn[e["dst"]].append(e); out[e["src"]].append(e)
    nec = {}
    for ln in s["nodes"]:
        for m in str(ln.get("source", "")).replace(",", " ").split():
            nec[m] = ln.get("necessity")
    return g, s, N, inn, out, nec


STOPW = set("with from that this than then their there these those which while where about into onto over under after before between across along each only both also have has were been being show shows shown".split())
def cwords(s): return {re.sub(r"(ing|ed|es|s)$", "", re.sub(r"ies$", "y", w)) for w in re.findall(r"[a-z]{4,}", (s or "").lower()) if w not in STOPW}
def claim_key(label): return " ".join(sorted(cwords(label)))
def same_claim(a, b):
    A, B = cwords(a), cwords(b)
    return bool(A and B) and len(A & B) / len(A | B) >= 0.6


def is_obs(n): return n["type"].startswith("OBS")
def is_spine(n): return bool(n.get("spine"))
def shown(n): return n.get("image_support") == "shown"


def reaches_dsc(N, out, start, removed=()):
    seen, st = set(), [start]
    while st:
        u = st.pop()
        if u in removed: continue
        if N[u]["type"].startswith("DSC"): return True
        for e in out[u]:
            if e["rel"] in SPINE_RELS and e["dst"] not in seen:
                seen.add(e["dst"]); st.append(e["dst"])
    return False


def support_of(N, inn, claim, removed=()):
    """evidence nodes with image_support shown that evidence the claim (not audits)."""
    return [e["src"] for e in inn[claim] if e["rel"] == "evidences" and e["src"] not in removed
            and is_obs(N[e["src"]]) and shown(N[e["src"]])]


def leave_one_family_out(N, inn, claim, evidence_ids):
    """families whose removal leaves the claim with no shown support."""
    fams = {family(N[i]) for i in evidence_ids}
    needed = []
    for f in sorted(fams):
        removed = {i for i in N if is_obs(N[i]) and family(N[i]) == f}
        if not support_of(N, inn, claim, removed):
            needed.append(f)
    return needed


def walk(N, inn, out, claim, evidence_ids, extra=()):
    """ordered walk: upstream spine context -> claim + evidence -> downstream to DSC."""
    # upstream: follow spine edges backwards to the hypothesis
    up, cur = [], claim
    seen = {claim}
    while True:
        prev = [e["src"] for e in inn[cur] if e["rel"] in SPINE_RELS and is_spine(N[e["src"]]) and e["src"] not in seen]
        if not prev: break
        cur = prev[0]; seen.add(cur); up.append(cur)
    up = list(reversed(up))
    down, cur = [], claim
    while not N[cur]["type"].startswith("DSC"):
        nxt = [e["dst"] for e in out[cur] if e["rel"] in SPINE_RELS and is_spine(N[e["dst"]]) and e["dst"] not in seen]
        if not nxt: break
        cur = nxt[0]; seen.add(cur); down.append(cur)
    steps = [{"node": u, "role": "context"} for u in up]
    for ev in evidence_ids:
        rel = next((e["rel"] for e in inn[claim] if e["src"] == ev), "evidences")
        op = next((e.get("mm_op") for e in inn[claim] if e["src"] == ev), None)
        steps.append({"node": ev, "role": "audit" if rel in AUDIT_RELS else "evidence", "op": op,
                      "panel_ids": N[ev].get("panel_ids") or [], "verdict": N[ev].get("image_support")})
    for x in extra: steps.append(x)
    steps.append({"node": claim, "role": "claim"})
    steps += [{"node": d, "role": "downstream"} for d in down]
    return steps


def cut(graph_path, spec_path, group_id, masked_dir="results/v06/masked"):
    global V2
    g, s, N, inn, out, nec = load(graph_path, spec_path)
    V2 = str(g.get("batch", "")).startswith("v06")   # v06_pilot and v06b_pilot
    store = store_for(graph_path) if V2 else None
    traces = []
    tid = 0

    def new(**kw):
        nonlocal tid; tid += 1
        rec = {"id": f"T{tid}", "group_id": group_id, **kw}; traces.append(rec); return rec

    claims = [n["id"] for n in g["nodes"] if is_spine(n)]
    for c in claims:
        ev_in = [e for e in inn[c] if is_obs(N[e["src"]])]
        fm_ev = [e for e in ev_in if family(N[e["src"]]) in FM_FAMILIES and nec.get(e["src"]) in ("necessary", "corrective")]
        if V2:
            # v2.1 seeding (lane level): seed where an FM lane is necessary for the claim, i.e. removing every evidence node
            # of that family leaves the claim with no shown support; node-level necessity is kept as a recorded field only
            shown_c = [e["src"] for e in ev_in if shown(N[e["src"]])]
            lanes = [f for f in (leave_one_family_out(N, inn, c, shown_c) if shown_c else []) if f in FM_FAMILIES]
            fm_ev = [e for e in ev_in if family(N[e["src"]]) in lanes and e["rel"] == "evidences"] + \
                    [e for e in ev_in if e["rel"] in AUDIT_RELS and family(N[e["src"]]) in FM_FAMILIES and nec.get(e["src"]) == "corrective"]
        if not fm_ev: continue
        ctype = N[c]["type"].split("/")[0]
        all_ev = [e["src"] for e in ev_in]
        for e in fm_ev:
            ev = e["src"]; rel = e["rel"]; op = e.get("mm_op")
            fam = family(N[ev])
            # --- root
            if rel in AUDIT_RELS:
                root, sub = "explain", "rejection"
            elif ctype == "MEC":
                root, sub = "explain", "mechanism"
            else:
                root, sub = "infer", SUBTYPE.get(op, "estimate")
                if V2 and sub == "rank" and len(N[ev].get("panel_ids") or []) < 3:
                    sub = "compare"   # v2 rule 7 (rank needs three or more conditions): two conditions -> infer/compare
            # --- lift (infer only)
            lift = None
            if root == "infer":
                if any(x["rel"] in AUDIT_RELS for x in inn[c]): lift = "required rejection with written reason"
                elif op == "compare_across_conditions" and len(N[ev].get("panel_ids") or []) >= 3: lift = "budget spanning panels"
                elif any(N[x["src"]]["type"].startswith("DES/variable_sweep") for x in inn[c]): lift = "declared stopping rule (sweep)"
            # --- grader and held-out channel
            others = [x for x in all_ev if x != ev and shown(N[x]) and family(N[x]) != fam]
            held_out = others[0] if (sub == "rank" and others) else None
            if root == "infer":
                grader = (f"independent channel {held_out} ({family(N[held_out])}), held out from the model" if held_out
                          else "answer key: the numbers and labels on the evidence node, judge-confirmed")
            elif sub == "rejection":
                grader = "answer key: the audit ruling on the panel"
            else:
                grader = "certified judge against the graph's mechanism, with the rival named"
            # --- floor: FM-lane evidence removed, and the held-out channel withheld
            fm_nodes = {i for i in N if is_obs(N[i]) and family(N[i]) in FM_FAMILIES}
            removed = set(fm_nodes) | ({held_out} if held_out else set())
            floor_support = support_of(N, inn, c, removed)
            floor_reaches = bool(floor_support)
            # --- depth
            shown_ev = [x for x in all_ev if shown(N[x])]
            depth_fams = leave_one_family_out(N, inn, c, shown_ev) if shown_ev else []
            involved = sorted({family(N[x]) for x in all_ev} | ({family(N[held_out])} if held_out else set()))
            depth = max(1, len(depth_fams)) if shown_ev else 1
            # --- ruling
            if root == "infer" and lift is None:
                status, why = "closed", "bare infer: no rejection, no budget, no stopping rule"
            elif floor_reaches:
                status, why = "closed", f"floor reaches the claim without FM evidence via {floor_support}"
            elif fam in FM_FAMILIES and N[ev].get("modality") in ("xy_curve", "table") and fam not in ("XRD",):
                status, why = "control", "plot read, no domain model needed: depth-one negative control"
            else:
                status, why = "open", ""
            if status == "open" and depth == 1 and N[ev].get("modality") != "micrograph":
                status, why = "control", "depth one and not an image read: negative-control stratum"
            v1_filter = None
            if V2 and not V1F and status != "open":
                v1_filter = {"status": status, "ruling": why}; status, why = "open", ""
            mask = {"infer": "hide the observation; hand over the panel(s)",
                    "explain": "hide the mechanism; show the rival" if sub == "mechanism" else "hide the ruling; show the claim and the panel"}[root]
            w = walk(N, inn, out, c, [ev])
            if root == "infer":
                hidden = [ev, c] + [x["node"] for x in w if x["role"] == "downstream"]
            elif sub == "mechanism":
                hidden = [c]
            else:
                hidden = [ev]
            extra = {}
            if sub == "mechanism":
                # a hidden mechanism's premises are hidden too (KNW nodes with premise_for into it): showing the premise
                # hands over part of the mechanism (ceramic T7, s5). A rival exists only as a second explains edge into
                # a claim this mechanism explains, or a rules_out edge; otherwise the trace has none and says so.
                explained = {e["dst"] for e in out[c] if e["rel"] == "explains"}
                rivals = sorted({e["src"] for d in explained for e in inn[d] if e["rel"] == "explains" and e["src"] != c}
                                | {e["src"] for d in explained | {c} for e in inn[d] if e["rel"] == "rules_out"})
                mask = "hide the mechanism and its premises; show the observation"
                grader = ("certified judge against the graph's mechanism, with the rival named" if rivals
                          else "certified judge against the graph's mechanism; no rival in the graph")
                extra = {"rival": rivals or None, "rival_note": None if rivals else "no second explains edge and no rules_out edge: no rival"}
            _t = new(**extra, root=root, subtype=sub, seed_claim=c, evidence=[ev], hidden=hidden, branch=f"{rel} edge {ev} -> {c}",
                fm_family=fam, lift=lift, floor={"reaches": floor_reaches, "support": floor_support},
                depth=depth, depth_families=depth_fams, channels_involved=involved, mask=mask, grader=grader,
                status=status, ruling=why, walk=w)
            if v1_filter:
                _t["v1_filter"] = v1_filter
                mark(_t, "v1-off", f"v1 filter would have ruled {v1_filter['status']}: {v1_filter['ruling']}")
            if V2:
                _t["node_necessity"] = nec.get(ev)
                mark(_t, "seed", f"lane {fam} necessary for {c} (node-level necessity of {ev}: {nec.get(ev)})")
            if V2 and sub == "compare":
                _t["answer_format"] = "state the difference between the two conditions; do not rank"
                mark(_t, "R7", f"{len(N[ev].get('panel_ids') or [])} panels: rank became infer/compare")

    # --- non-FM audits: negative-control stratum (same shape, no domain model needed)
    for c in claims:
        for e in inn[c]:
            src = N.get(e["src"])
            if not src or not is_obs(src) or e["rel"] not in AUDIT_RELS or family(src) in FM_FAMILIES: continue
            new(root="explain", subtype="rejection", seed_claim=c, evidence=[e["src"]], hidden=[e["src"]], branch=f"{e['rel']} edge {e['src']} -> {c}",
                fm_family=family(src), lift="required rejection with written reason",
                floor={"reaches": False, "note": "the text asserts the claim; the ruling needs the plot"},
                depth=1, depth_families=[family(src)], channels_involved=[family(src)],
                mask="hide the ruling; show the claim and the panel", grader="answer key: the audit ruling on the panel",
                status="control", ruling="plot read, no domain model: depth-one negative control",
                walk=walk(N, inn, out, c, [e["src"]]))
            if V2 and not V1F:
                _a = traces[-1]; _a["v1_filter"] = {"status": _a["status"], "ruling": _a["ruling"]}
                _a["status"], _a["ruling"] = "open", ""
                mark(_a, "v1-off", "v1 filter would have ruled control: plot read, no domain model: depth-one negative control")

    # --- explain at a claim with two competing causes (branch: which cause accounts for the optimum)
    for c in claims:
        causes = [e["src"] for e in inn[c] if e["rel"] == "causes" and is_spine(N[e["src"]])]
        if len(causes) >= 2 and N[c]["type"].startswith("PRP"):
            fm_support = [i for cc in causes for i in support_of(N, inn, cc) if family(N[i]) in FM_FAMILIES]
            if not fm_support: continue
            if V2:
                # v2 rule 1 (rivals only when the graph says so): a competing-causes trace needs mode: alternative on the
                # causes edges, or a rules_out / contrasts edge touching the claim or a cause; joint causes become a mechanism trace
                modes = {e.get("mode") for e in inn[c] if e["rel"] == "causes"}
                contrast = any(e["rel"] in ("rules_out", "contrasts") for x in [c] + causes for e in inn[x])
                if "alternative" not in modes and not contrast:
                    mechs1 = sorted({e["src"] for e in inn[c] if e["rel"] == "explains"})
                    if mechs1 and any(t0["subtype"] == "mechanism" and t0["seed_claim"] == mechs1[0] for t0 in traces):
                        continue   # the mechanism already has its own explain/mechanism trace
                    if mechs1 and not (support_of(N, inn, mechs1[0]) or support_of(N, inn, c)):
                        t = new(root="explain", subtype="mechanism", seed_claim=mechs1[0], evidence=[], hidden=[mechs1[0]], branch=f"joint causes {causes} of {c}",
                                fm_family="SEM", lift=None, floor={"reaches": None}, depth=0, depth_families=[], mask="", grader="",
                                status="closed", ruling="joint causes: the explaining mechanism has no shown evidence", walk=[])
                        mark(t, "R1", f"causes {causes} into {c} are joint; mechanism {mechs1[0]} has no shown evidence: closed")
                        continue
                    if mechs1:
                        m0 = mechs1[0]; ev1 = support_of(N, inn, m0) or support_of(N, inn, c)
                        t = new(root="explain", subtype="mechanism", seed_claim=m0, evidence=ev1, hidden=[m0], branch=f"joint causes {causes} of {c}, explained by {m0}",
                                fm_family="SEM", lift=None, floor={"reaches": False, "support": []}, depth=len({family(N[i]) for i in ev1}),
                                depth_families=sorted({family(N[i]) for i in ev1}), channels_involved=sorted({family(N[i]) for i in ev1}),
                                mask="hide the mechanism and its premises; show the observation and the joint causes",
                                grader="certified judge against the graph's mechanism; causes act jointly, no rival",
                                status="open", ruling="", walk=walk(N, inn, out, m0, ev1, extra=[{"node": cc, "role": "context"} for cc in causes]))
                        mark(t, "R1", f"causes {causes} into {c} are joint (modes {sorted(x for x in modes if x)}): mechanism trace, not competing causes")
                    continue
            all_sup = [i for cc in causes for i in support_of(N, inn, cc)] + support_of(N, inn, c)
            fams = leave_one_family_out(N, inn, c, support_of(N, inn, c))
            depth = len({family(N[i]) for i in all_sup})
            rival = [cc for cc in causes if not any(family(N[i]) in FM_FAMILIES for i in support_of(N, inn, cc))]
            mechs = sorted({e["src"] for cc in [c] + causes for e in inn[cc] if e["rel"] == "explains"} |
                           {e["dst"] for cc in causes for e in out[cc] if e["rel"] == "supports" and N[e["dst"]]["type"].startswith("MEC")})
            new(root="explain", subtype="competing causes", seed_claim=c, evidence=sorted(set(all_sup)), hidden=mechs,
                branch=f"two `causes` edges into {c}: {causes}", rival=rival, fm_family="SEM",
                lift=None, floor={"reaches": False, "support": [i for i in all_sup if family(N[i]) not in FM_FAMILIES],
                                  "note": "floor holds the non-FM causes only, so it picks the rival"},
                depth=depth, depth_families=sorted({family(N[i]) for i in all_sup}),
                mask="hide the mechanism node(s) explaining the claim; show the competing causes and their evidence",
                grader="judge: the graph's explaining mechanism as key; the cross-check that the rival's optimum differs from the claim's",
                status="open", ruling="", walk=walk(N, inn, out, c, sorted(set(all_sup)),
                                                     extra=[{"node": cc, "role": "cause"} for cc in causes] +
                                                           [{"node": m, "role": "mechanism"} for m in mechs]))

    # --- intervene at a sweep with an optimum
    sweep = [n["id"] for n in g["nodes"] if n["type"].startswith("DES/variable_sweep")]
    optimum = [n["id"] for n in g["nodes"] if n["type"].startswith("DSC/design_guidance")]
    if sweep and optimum:
        series = [n["id"] for n in g["nodes"] if is_obs(n) and any(e.get("mm_op") == "compare_across_conditions" for e in out[n["id"]])]
        outcome = [n["id"] for n in g["nodes"] if is_obs(n) and n["type"].startswith("OBS/response/trend") and family(n) not in FM_FAMILIES
                   and any(N[e["dst"]]["type"].startswith("PRP") for e in out[n["id"]])] or \
                  [n["id"] for n in g["nodes"] if is_obs(n) and n["type"].startswith("OBS/response/trend") and family(n) not in FM_FAMILIES]
        fm_series = [i for i in series if family(N[i]) in FM_FAMILIES]
        w = walk(N, inn, out, optimum[0], fm_series + outcome[:1])
        later = [p for i in fm_series for p in (N[i].get("panel_ids") or [])[3:]]
        new(root="intervene", subtype="next condition", seed_claim=optimum[0], evidence=fm_series + outcome[:1],
            hidden=[optimum[0]] + outcome[:1] + [x["node"] for x in w if N[x["node"]]["type"].split("/")[0] in ("STR", "MEC", "PRP", "PRF", "DSC")], hidden_panels=later,
            branch=f"sweep {sweep[0]} with optimum {optimum[0]}", fm_family="SEM", lift=None,
            floor={"reaches": False, "note": "trend extrapolation of the classical series picks the earlier optimum"},
            depth=len({family(N[i]) for i in fm_series + outcome[:1]}),
            depth_families=sorted({family(N[i]) for i in fm_series + outcome[:1]}),
            mask="show the sweep design and the evidence for the first three conditions only (later panels hidden); hide the outcome series and the optimum; ask which condition to test next",
            grader=f"the measured outcome at the chosen condition from {outcome[0] if outcome else '?'}, held out",
            status="open", ruling="", walk=w)

    # --- generate: needs an oracle in the tool inventory for the design's family
    des = [n["id"] for n in g["nodes"] if n["type"].startswith("DES/route")]
    for d in des:
        fam = family(N[d]) or "PROCESS"
        new(root="generate", subtype="design under constraint", seed_claim=d, evidence=[], branch=f"DES/route {d}",
            fm_family=fam, lift=None, floor={"reaches": None}, depth=None, depth_families=[],
            mask="hide the route; show the constraint and the target structure",
            grader=ORACLES.get(fam) or "none in the tool inventory", status="closed" if not ORACLES.get(fam) else "open",
            ruling="" if ORACLES.get(fam) else f"no oracle for {fam}: gate 2 closes the root", walk=[])
    by_ev = defaultdict(list)
    for t in traces:
        if len(t.get("evidence", [])) == 1: by_ev[t["evidence"][0]].append(t["id"])
    for t in traces:
        if len(t.get("evidence", [])) == 1 and len(by_ev[t["evidence"][0]]) > 1:
            t["siblings"] = [x for x in by_ev[t["evidence"][0]] if x != t["id"]]
    for t in traces:
        # dedupe the walk (a node may enter as context and again as cause)
        seen, w = set(), []
        seen_claims = {}
        for st in t.get("walk", []):
            if st["node"] in seen and st["role"] in ("context", "downstream"): continue
            if V2 and st["role"] in ("context", "downstream"):
                # v2 rule 9 (deduplicate the walk by claim, not only by node id)
                k = claim_key(N[st["node"]]["label"])
                if k in seen_claims:
                    mark(t, "R9", f"{st['node']} restates {seen_claims[k]}: dropped from the walk"); continue
                seen_claims[k] = st["node"]
            seen.add(st["node"]); w.append(st)
        t["walk"] = w
        if t["root"] == "explain":
            # downstream nodes restate the conclusion: never given for explain traces
            for st in t["walk"]:
                if st["role"] == "downstream":
                    st["role"] = "redacted"; t.setdefault("hidden", []).append(st["node"])
                    t.setdefault("redactions", []).append({"node": st["node"], "why": "downstream conclusion restates the answer"})
            for st in t["walk"]:
                if st["role"] == "context" and N[st["node"]]["type"].startswith("HYP/hypothesis"):
                    st["role"] = "redacted"; t.setdefault("hidden", []).append(st["node"])
                    t.setdefault("redactions", []).append({"node": st["node"], "why": "hypothesis states the mechanism the model must produce"})
        if t["root"] == "explain" and t["subtype"] == "mechanism":
            for e in inn[t["seed_claim"]]:
                if e["rel"] == "premise_for" and N[e["src"]]["type"].startswith("KNW") and e["src"] not in t["hidden"]:
                    t["hidden"].append(e["src"])
                    t.setdefault("redactions", []).append({"node": e["src"], "why": "premise of the hidden mechanism"})
        if V2:
            t["has_sweep"] = any(n["type"].startswith("DES/variable_sweep") for n in g["nodes"])
            t["_overrides"] = {(o["node"], o["panel"]) for o in (g.get("cue_overrides") or []) + ((g.get("review") or {}).get("cue_overrides") or [])}
            v2_prelinear(t, N, inn, out, store, masked_dir, os.path.basename(graph_path)[:-5])
            t.pop("_overrides", None)
        if V2 and t["root"] == "explain" and t["subtype"] == "mechanism" and not t["evidence"]:
            t["status"] = "closed"; t["ruling"] = "mechanism trace with no shown evidence: nothing to observe"
            mark(t, "R3", "explain/mechanism with empty evidence: closed before linearising"); t["linear"] = []; continue
        t["linear"] = linearize(N, inn, out, t)
    return g, traces


# ======================= cutter v2 (v06 pilot): rules 3-6 and 8, applied before linearize =======================
CUE_TECH = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cue_technique.json")))
KNOWLEDGE_PILE = []

def store_for(graph_path):
    name = os.path.basename(graph_path)[:-5]; j, _, d = name.partition("__")
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "matmech", j, d)
    mj = json.load(open(f"{base}/panels/match.json")); pj = json.load(open(f"{base}/panels/panels.json"))
    ocr = {c["crop"]: c for c in json.load(open(f"{base}/panels/ocr.json"))["crops"]} if os.path.exists(f"{base}/panels/ocr.json") else {}
    return base, mj, pj, ocr

def panel_record(store, pid):
    """crop path (absolute), caption span, OCR record for a canonical panel id; the figure number maps to the image via match.json."""
    base, mj, pj, ocr = store
    m = re.match(r".*#F(\d+)([a-z]?)$", pid)
    if not m: return None
    n, let = int(m.group(1)), m.group(2).upper()
    fig = next((f for f in mj["figures"] if f["figure_number"] == n), None)
    if not fig: return None
    pf = next((f for f in pj["figures"] if f["file"] == fig["file"]), {})
    if let:
        det = next((d for d in pf.get("detections", []) if d.get("label", "").upper() == let and d.get("crop")), None)
        span = next((p.get("definition") for p in fig["panels"] if p.get("label", "").upper() == let), None)
        if not det: return {"crop": None, "span": span, "ocr": {}, "figure": os.path.join(base, fig["file"])}
        return {"crop": os.path.join(base, det["crop"]), "span": span, "ocr": ocr.get(det["crop"], {}), "figure": os.path.join(base, fig["file"])}
    return {"crop": os.path.join(base, fig["file"]), "span": fig.get("caption_preamble"), "ocr": {}, "figure": os.path.join(base, fig["file"])}

def annotations(rec):
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "taxonomy"))
    from build_packets_v06 import classify
    return [t for t in (rec.get("ocr") or {}).get("tokens", []) if classify(t["text"]) == "annotation"]

def shares_content(a, labels):
    A = cwords(a); H = set().union(*[cwords(l) for l in labels]) if labels else set()
    return sorted({x for x in A for h in H if len(x) >= 5 and len(h) >= 5 and x[:5] == h[:5]})

def mask_crop(src, boxes, dst):
    from PIL import Image
    import statistics
    im = Image.open(src).convert("RGB"); px = im.load(); W, H = im.size
    for x0, y0, x1, y1 in boxes:
        x0, y0, x1, y1 = max(0, x0 - 2), max(0, y0 - 2), min(W - 1, x1 + 2), min(H - 1, y1 + 2)
        ring = [px[x, y] for x in range(max(0, x0 - 3), min(W, x1 + 4)) for y in (max(0, y0 - 3), min(H - 1, y1 + 3))] + \
               [px[x, y] for y in range(max(0, y0 - 3), min(H, y1 + 4)) for x in (max(0, x0 - 3), min(W - 1, x1 + 3))]
        fill = tuple(int(statistics.median(c[i] for c in ring)) for i in range(3))
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1): px[x, y] = fill
    os.makedirs(os.path.dirname(dst), exist_ok=True); im.save(dst, quality=95)

def num_of(s):
    m = re.search(r"(\d+(?:\.\d+)?)", s or ""); return float(m.group(1)) if m else None

SPAN_GENERIC = set("panel panels caption captions figure fig only the and of in on for with shows show shown is are a an to at as by from sample samples label labelled labeled named name given text linked (caption caption; condition conditions".split())

def fig_preamble(store, pid):
    m = re.match(r".*#F(\d+)", pid)
    fig = next((f for f in store[1]["figures"] if m and f["figure_number"] == int(m.group(1))), None)
    return fig.get("caption_preamble") if fig else None

def graded_targets(t, N):
    red = {r["node"] for r in t.get("redactions", [])}
    if t["root"] == "infer": return [e for e in t["evidence"] if e in N and N[e]["type"].startswith("OBS")]
    if t["root"] == "intervene":
        outc = [e for e in t["evidence"] if family(N[e]) not in FM_FAMILIES]
        return [t["seed_claim"]] + outc
    if t["subtype"] == "competing causes": return [h for h in t.get("hidden", []) if h not in red and N.get(h, {}).get("type", "").startswith("MEC")] or [h for h in t.get("hidden", []) if h not in red]
    if t["subtype"] == "rejection": return t["evidence"][:1]
    return [t["seed_claim"]]

def targets_of(t):
    red = {r["node"] for r in t.get("redactions", [])}
    if t["root"] == "infer": return [t["evidence"][0], t["seed_claim"]]
    if t["subtype"] == "competing causes": return [h for h in t.get("hidden", []) if h not in red]
    if t["subtype"] == "rejection": return t["evidence"][:1]
    return [t["seed_claim"]]

def v2_prelinear(t, N, inn, out, store, masked_dir, paper):
    if t["status"] == "closed" or not t.get("walk"): return
    hidden = set(t.get("hidden", []))
    # v2 rule 4 part 2 (nothing from after the answer, all roots): no context node may share a claim with a hidden node
    for st in t["walk"]:
        if st["role"] == "context" and any(same_claim(N[st["node"]]["label"], N[h]["label"]) for h in hidden if h in N):
            st["role"] = "redacted"; t.setdefault("hidden", []).append(st["node"])
            t.setdefault("redactions", []).append({"node": st["node"], "why": "shares a claim with a hidden node"})
            mark(t, "R4", f"context {st['node']} shares a claim with a hidden node: redacted")
    # v2 rule 4 part 1 (intervene): withhold every panel at or beyond the decision condition and every series panel;
    # the key must name the condition directly after the last one given
    if t["root"] == "intervene":
        sweep = next((n for n in N.values() if n["type"].startswith("DES/variable_sweep")), None)
        # levels: the sweep label's first number list and its unit ("0, 5, 10, 20 mL"); a panel's level is read only as
        # number+that unit, so sample suffixes (RGO-Cu2S-3) and other quantities (26.8 wt%) are never taken for levels
        mlev = re.search(r"((?:\d+(?:\.\d+)?\s*(?:,|and|or|to)\s*)+\d+(?:\.\d+)?)\s*([A-Za-z%°][\w%/°]*)", sweep["label"]) if sweep else None
        levels = sorted({float(x) for x in re.findall(r"\d+(?:\.\d+)?", mlev.group(1))}) if mlev else []
        unit = mlev.group(2) if mlev else None
        # sample names count as levels only when the sweep label ties the first and last level to them (RZSZ-0 to RZSZ-25)
        stem = None
        if levels:
            lo, hi = (f"{x:g}" for x in (levels[0], levels[-1]))
            ms = re.search(r"([A-Za-z][\w]*)-" + re.escape(lo) + r"\b.*\b\1-" + re.escape(hi) + r"\b", sweep["label"])
            stem = ms.group(1) if ms else None
        def level_of(txt):
            if not txt or not unit: return None
            m = re.search(r"(\d+(?:\.\d+)?)\s*" + re.escape(unit), txt)
            if not m and stem: m = re.search(re.escape(stem) + r"-(\d+(?:\.\d+)?)\b", txt)
            return float(m.group(1)) if m and float(m.group(1)) in levels else None
        decision = level_of(N[t["seed_claim"]]["label"])
        if decision is None: decision = num_of(N[t["seed_claim"]]["label"])
        given, withheld = [], []
        for ev in t["evidence"]:
            conds = (N[ev].get("attrs") or {}).get("panel_conditions") or []
            for i, pid in enumerate(N[ev].get("panel_ids") or []):
                rec = panel_record(store, pid) or {}
                v = level_of(conds[i]["condition"]) if i < len(conds) and conds[i].get("condition") else level_of(rec.get("span"))
                if family(N[ev]) not in FM_FAMILIES or v is None or decision is None or v >= decision: withheld.append(pid)
                else: given.append((v, pid))
        t["hidden_panels"] = sorted(set(withheld))
        t["given_panels"] = list(dict.fromkeys(p for _, p in sorted(given)))
        nxt = next((l for l in levels if given and l > max(v for v, _ in given)), None)
        mark(t, "R4", f"given {t['given_panels']}, withheld {t['hidden_panels']} (decision {decision}, levels {levels} {unit})")
        if not given or decision is None or nxt != decision:
            t["status"] = "closed"; t["ruling"] = f"decision {decision} is not the condition directly after the last given ({nxt})"
            mark(t, "R4", t["ruling"]); return
    given_panels = t.get("given_panels") or [p for ev in t["evidence"] for p in (N[ev].get("panel_ids") or []) if p not in set(t.get("hidden_panels", []))]
    t["given_panels"] = given_panels
    # v2 rule 6 (panel check): an evidence panel whose OCR cue class contradicts the node's technique blocks the trace
    for ev in t["evidence"]:
        tech = family(N[ev])
        for pid in N[ev].get("panel_ids") or []:
            cues = ((panel_record(store, pid) or {}).get("ocr") or {}).get("cues") or []
            if cues and tech and not any(tech in CUE_TECH.get(c, []) for c in cues) and (ev, pid) in t.get("_overrides", ()):
                mark(t, "R6", f"{ev} technique {tech} vs {pid} cues {cues}: judge cue_override honoured, not blocked")
            elif cues and tech and not any(tech in CUE_TECH.get(c, []) for c in cues):
                t["blocked"] = {"reason": "panel_modality", "node": ev, "panel": pid, "technique": tech, "cues": cues}
                mark(t, "R6", f"{ev} technique {tech} vs {pid} cues {cues}: blocked panel_modality")
    # v2.1 rule 3 (the answer must be readable from what the solver is given). Graded target: infer -> the observation(s)
    # read from the given panels (the claim drawn from them is downstream and not graded); explain -> the hidden mechanism
    # or ruling; intervene -> the decision and its outcome. A target passes when source is figure; or source is text and
    # every requires_unseen fact is stated in the caption span of a given panel; or (explain only) source is inferred and
    # every node it is inferred from is given or is itself a passing target.
    def unmath(txt):
        # OCR captions wrap formulas in LaTeX ($\\mathsf { N i } _ { x }$): drop commands, braces and inner spaces
        txt = txt.replace("\\gamma", "y").replace("γ", "y").replace("\\cdot", "-")
        return re.sub(r"\$([^$]*)\$", lambda m: re.sub(r"\\[A-Za-z]+|[{}_^\s]", "", m.group(1)), txt)
    spans = unmath(" ".join(((panel_record(store, p) or {}).get("span") or "") + " " + (fig_preamble(store, p) or "") for p in given_panels)).lower()
    span_words = set(re.findall(r"[a-z0-9]+", spans))
    given_nodes = {st["node"] for st in t["walk"] if st["role"] not in ("redacted",) and st["node"] not in set(t.get("hidden", []))}
    tg = graded_targets(t, N)
    t["graded_targets"] = tg
    verdicts, why = {}, []
    def idents(txt):
        # sample names and formulas: hyphen chains with a capital or digit (Al-Cu-Mn, RZSZ-10, Ni-MOF), formulas (Cu2S,
        # NixPyOz), numbers with units (20 vol%); bare panel letters, figure numbers and lower-case words are not identifiers
        out = []
        for w in re.findall(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)+|[A-Z][a-z]?(?:\d+|[A-Z][a-z]?|[xyz]|\d*\.\d+)+|\d+(?:\.\d+)?\s?(?:vol%|wt%|at%|mL|°C|K|h|min|nm|um|μm|%)", txt):
            if "-" in w and not re.search(r"[A-Z0-9]", w): continue
            if re.fullmatch(r"F\d+[a-z]?|\d{1,2}", w): continue
            out.append(w.lower())
        return out
    def ident_seen(w):
        if w.replace(" ", "") in spans.replace(" ", ""): return True
        comps = [c for c in w.split("-") if len(c) >= 3 and not c.isdigit()]
        return "-" in w and bool(comps) and all(c in span_words for c in comps)
    def in_spans(fact, label=""):
        # every identifier of the fact must be in the given caption spans; when the target's own label uses some of them,
        # only those count (a caption mapping that also lists panels not given is not needed for them); a fact with no
        # identifier falls back to 60% of its content words
        ids = idents(fact); own = [w for w in ids if w in set(idents(label))]
        if own: ids = own
        if ids: return all(ident_seen(w) for w in ids)
        toks = [w for w in re.findall(r"[a-z]{3,}", fact.lower()) if w not in SPAN_GENERIC]
        return bool(toks) and sum(w in span_words for w in toks) / len(toks) >= 0.6
    for x in tg:
        a = N[x].get("attrs") or {}; src = a.get("source"); ru = a.get("requires_unseen") or []
        if src == "figure":
            verdicts[x] = (True, "figure")
        elif src == "text":
            left = [f for f in ru if not in_spans(f, N[x]["label"])]
            ok = not left and (bool(ru) or in_spans(N[x]["label"]))
            verdicts[x] = (ok, "text, facts in given caption spans" if ok else f"text, not in given captions: {left or [N[x]['label'][:80]]}")
        else:
            verdicts[x] = (None, src)
    for x in tg:
        if verdicts[x][0] is None:
            src = verdicts[x][1]
            if src == "inferred" and t["root"] == "explain":
                prem = [e["src"] for e in inn[x] if e["rel"] in ("evidences", "premise_for", "supports", "causes", "explains", "derives")]
                bad = [p for p in prem if p not in given_nodes and not (verdicts.get(p, (False,))[0])]
                verdicts[x] = (not bad, "inferred from given nodes" if not bad else f"inferred from nodes not given: {bad}")
            else:
                verdicts[x] = (False, f"source {src}")
    t["target_verdicts"] = {x: {"pass": v[0], "why": v[1]} for x, v in verdicts.items()}
    why = [f"{x}: {v[1]}" for x, v in verdicts.items() if not v[0]]
    ann_only = [ev for ev in t["evidence"] if (N[ev].get("attrs") or {}).get("read_from") == "annotation"]
    if ann_only: t["annotation_read_evidence"] = ann_only   # recorded, not gating (rule 5 masks shared annotations)
    if why:
        t["status"] = "closed"; t["ruling"] = "not derivable from given panels: " + "; ".join(why)
        mark(t, "R3", t["ruling"])
        KNOWLEDGE_PILE.append({"paper": paper, "trace": t["id"], "root": t["root"], "subtype": t["subtype"], "targets": tg,
                               "why": why, "requires_unseen": {x: (N[x].get("attrs") or {}).get("requires_unseen") for x in tg},
                               "labels": {x: N[x]["label"] for x in tg}})
        return
    mark(t, "R3", "graded targets readable: " + "; ".join(f"{x} ({v[1]})" for x, v in verdicts.items()))
    # v2 rule 5 (annotation masking): mask annotation strings that share content with a hidden target
    hid_labels = [N[h]["label"] for h in set(t.get("hidden", [])) | set(targets_of(t)) if h in N]
    for pid in given_panels:
        rec = panel_record(store, pid)
        if not rec or not rec.get("crop"): continue
        hits = [(tok, shares_content(tok["text"], hid_labels)) for tok in annotations(rec)]
        hits = [(tok, w) for tok, w in hits if w]
        # author-written values (0.227 nm, 14 nm, 0.69 eV) are classed as scale/tick tokens by the packet builder; mask
        # one when its number appears in a hidden target label (staff C, v06 build: these carried audit answers)
        hid_nums = set(re.findall(r"(?<![A-Za-z\d.])\d+(?:\.\d+)?", " ".join(hid_labels)))
        for tok in (rec.get("ocr") or {}).get("tokens", []):
            v = re.findall(r"(?<![A-Za-z\d.])\d+(?:\.\d+)?", tok["text"])
            if v and any(x in hid_nums and (("." in x) or len(x) >= 2) for x in v) and re.search(r"[A-Za-zµμÅ%°]", tok["text"]):
                if all(tok is not h for h, _ in hits): hits.append((tok, [x for x in v if x in hid_nums]))
        if hits:
            dst = os.path.join(masked_dir, paper, t["id"], pid.split("#")[1] + ".jpg")
            mask_crop(rec["crop"], [tok["box"] for tok, _ in hits], dst)
            t.setdefault("masked_panels", []).append({"panel": pid, "masked_crop": os.path.relpath(dst), "strings": [tok["text"] for tok, _ in hits], "shared_words": sorted({x for _, w in hits for x in w})})
            mark(t, "R5", f"{pid}: masked {[tok['text'] for tok, _ in hits]}")
    # v2 rule 8 (partial answers are keys too): the writer must declare answer_scope full | partial on the key
    t["answer_scope_required"] = True
    # v2 rule 6, enforced: a trace whose evidence panel is a different kind of figure than the observation's technique
    # cannot be served (the solver would be handed the wrong image); it closes rather than stay open with a block on it
    if t.get("blocked") and t["status"] == "open":
        b = t["blocked"]
        t["status"] = "closed"; t["ruling"] = f"panel_modality: {b['node']} is {b['technique']} but {b['panel'].split('#')[1]} reads as {'/'.join(b['cues'])}"
        mark(t, "R6", "open trace with a panel_modality block: closed")


PEAK = re.compile(r"(?:peak\w*|maxim\w*|highest|optimum|best)\s+(?:at|for|near|is)\s+(\d+(?:\.\d+)?)\s*vol%", re.I)
FOR = re.compile(r"\bfor\s+(\d+(?:\.\d+)?)\s*vol%", re.I)
def optimum(N, i, claim=False):
    """the composition a node's label puts its peak at, only from explicit peak wording
    (a claim may also say 'X and Y for 20 vol%')."""
    lab = N[i]["label"]
    m = PEAK.findall(lab) or (FOR.findall(lab) if claim else [])
    return m[0] if m else None


def linearize(N, inn, out, t):
    """one legal single-direction walk through the DAG, with explicit dependencies."""
    # FIX (orchestrator, 2026-09-20, cut_traces.py:297): same list-valued technique_norm as family()
    fam = lambda i: family(N[i])
    ev_of = lambda i: [e["src"] for e in inn[i] if e["rel"] == "evidences" and N[e["src"]]["type"].startswith("OBS")]
    pre_of = lambda i: [e["src"] for e in inn[i] if e["rel"] == "premise_for"]
    hid = set(t.get("hidden", []))
    steps = []
    def add(role, nodes, text, needs=None):
        steps.append(dict(step=len(steps) + 1, role=role, nodes=nodes, depends_on=needs or [],
                          hidden=(role not in ("read", "context", "puzzle", "candidates", "claim") or role == "claim" and t["root"] == "infer") and any(n in hid for n in nodes), text=text)); return len(steps)
    c = t["seed_claim"]
    if t["root"] == "explain" and t["subtype"] == "competing causes":
        causes = [e["src"] for e in inn[c] if e["rel"] == "causes"]
        target = optimum(N, c, claim=True) or next((optimum(N, i) for i in ev_of(c) if optimum(N, i)), None)
        if V2 and not (t.get("has_sweep") and target):
            # v2 rule 2 (optimum test only with a sweep): no DES/variable_sweep or no stated optimum -> causes are kept or
            # rejected on their own evidence, never on optima
            target = None; mark(t, "R2", "no sweep with a stated optimum: causes judged on their evidence")
        p = add("puzzle", [c] + ev_of(c), f"Observation to explain: {N[c]['label']}. Its optimum: {target} vol%.")
        k = add("candidates", causes, "Candidate causes: " + " | ".join(f"{x}: {N[x]['label'][:70]}" for x in causes), [p])
        # test the rivals first so the rejection comes early
        def ruling(x):
            ev = ev_of(x); o = optimum(N, x) or next((optimum(N, i) for i in ev if optimum(N, i)), None)
            if V2 and target is None:
                sup = [i for i in ev if shown(N[i])]
                return ("keep", f"its evidence ({', '.join(sup)}) shows it") if sup else ("untested", "no shown evidence for it")
            if o and target and o != target: return "reject", f"its own optimum is at {o} vol%, not {target}: necessary at most, not the differentiator"
            if o and target: return "keep", f"its optimum coincides with the claim's ({o} vol%)"
            fm = [i for i in ev if fam(i) in {'SEM','TEM','XRD','XAS','ATOM'}]
            return ("keep", f"its evidence ({', '.join(ev)}) is most developed at the claim's optimum") if fm else ("untested", "no evidence states an optimum")
        rulings = {x: ruling(x) for x in causes}
        order = sorted(causes, key=lambda x: (rulings[x][0] != "reject", x))
        survivors = []
        for x in order:
            r, why = rulings[x]; ev = ev_of(x)
            add("test", [x] + ev, f"Test {x} ({N[x]['label'][:60]}) against {', '.join(ev)} [{', '.join(sorted({fam(i) for i in ev}))}]: {r.upper()}, {why}", [k])
            if r != "reject": survivors.append(x)
        last = len(steps)
        for m in t.get("hidden", []):
            add("mechanism", [m] + pre_of(m) + ev_of(m), f"Why the surviving cause works: {N[m]['label'][:120]}  [premise: {', '.join(pre_of(m)) or 'none'}; evidence: {', '.join(ev_of(m)) or 'none'}]", [last]); last = len(steps)
        rej = [x for x in causes if rulings[x][0] == "reject"]
        add("adjudication", survivors, f"The optimum is set by {', '.join(survivors)}; {', '.join(rej) or 'no rival'} is necessary but not sufficient.", [last])
        down = [e["dst"] for e in out[c] if e["rel"] == "supports"]
        if down: add("prediction", down, f"What follows: {N[down[0]]['label'][:120]}", [len(steps)])
    elif t["root"] == "explain" and t["subtype"] == "mechanism":
        ev = t["evidence"]; p = add("puzzle", ev, f"Observation: {N[ev[0]]['label'][:120]}  [panels {', '.join(x.split('#')[1] for x in N[ev[0]].get('panel_ids') or [])}]")
        add("mechanism", [c] + pre_of(c), f"Mechanism that produces it: {N[c]['label'][:120]}  [premise: {', '.join(pre_of(c)) or 'none'}]", [p])
        down = [e["dst"] for e in out[c] if e["rel"] in ("explains", "supports")]
        if down: add("prediction", down, f"What it explains: {N[down[0]]['label'][:120]}", [2])
    elif t["root"] == "explain":  # rejection
        p = add("claim", [c], f"Claim under test: {N[c]['label'][:120]}")
        ev = t["evidence"]; add("read", ev, f"Read the panel: {', '.join(x.split('#')[1] for x in N[ev[0]].get('panel_ids') or [])} [{fam(ev[0])}]", [p])
        add("ruling", ev, f"Ruling: {N[ev[0]]['label'][:140]}", [2])
    elif t["root"] == "infer":
        ctx = [x["node"] for x in t["walk"] if x["role"] == "context"]
        p = add("context", ctx, "What was made and why: " + " -> ".join(N[x]["label"][:50] for x in ctx))
        ev = t["evidence"][0]
        add("read", [ev], f"Open the panels {', '.join(x.split('#')[1] for x in N[ev].get('panel_ids') or [])} [{fam(ev)}] and {t['subtype']} ({t['walk'][len(ctx)].get('op','').replace('_',' ') if len(t['walk'])>len(ctx) else ''})", [p])
        add("observation", [ev], f"Observation: {N[ev]['label'][:140]}", [2])
        add("claim", [c], f"Claim it establishes: {N[c]['label'][:140]}", [3])
        down = [x["node"] for x in t["walk"] if x["role"] == "downstream"]
        if down: add("downstream", down, f"Feeds: {N[down[0]]['label'][:100]}", [4])
    elif t["root"] == "intervene":
        ctx = [x["node"] for x in t["walk"] if x["role"] == "context" and N[x["node"]]["type"].split("/")[0] in ("HYP", "DES", "PRC")]
        p = add("context", ctx, "Hypothesis, design, processing: " + " -> ".join(N[x]["label"][:50] for x in ctx))
        fmev = [i for i in t["evidence"] if fam(i) in {'SEM','TEM','XRD','XAS','ATOM'}]
        given = [x.split('#')[1] for i in fmev for x in (N[i].get("panel_ids") or []) if x not in set(t.get("hidden_panels", []))]
        add("read", fmev, f"Results so far, as panels only: {', '.join(given)} [{', '.join(sorted({fam(i) for i in fmev}))}]", [p])
        add("decision", [c], f"Decide the next condition: {N[c]['label'][:120]}", [2])
        oc = [i for i in t["evidence"] if i not in fmev]
        if oc: add("outcome", oc, f"Outcome at that condition (grader): {N[oc[0]]['label'][:120]}", [3])
    else:
        add("closed", [c], t.get("ruling", "closed"))
    return steps


if __name__ == "__main__":
    gp, sp, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    g, traces = cut(gp, sp, group_id=g_id if (g_id := None) else json.load(open(gp))["paper_id"])
    json.dump({"paper_id": g["paper_id"], "title": g["title"], "cutter": ("v2.2" + ("+v1-filters" if V1F else "")) if V2 else "v1", "traces": traces,
               "knowledge_pile": KNOWLEDGE_PILE}, open(out_path, "w"), indent=1)
    from collections import Counter
    print(f"{len(traces)} traces:", dict(Counter((t['root'], t['status']) for t in traces)))
    for t in traces:
        print(f"  {t['id']:3s} {t['root']:9s} {t['subtype']:16s} seed={t['seed_claim']:4s} ev={t['evidence']} depth={t['depth']} {t['status']:7s} {t['ruling'][:70]}")
