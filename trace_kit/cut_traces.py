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
import json, sys, re
from collections import defaultdict

FM_FAMILIES = {"SEM", "TEM", "XRD", "XAS", "ATOM"}
SUBTYPE = {"measure_feature_metric": "estimate", "read_trend": "estimate", "read_characteristic_point": "estimate",
           "assign_features": "classify", "recognize_signature": "classify", "inspect_local_feature": "classify",
           "compare_across_conditions": "rank", "cross_check_consistency": "check", "correlate_across_series": "rank"}
AUDIT_RELS = {"qualifies", "contrasts", "rules_out"}
SPINE_RELS = {"motivates", "realizes", "feeds_into", "produces", "causes", "explains", "supports"}
ORACLES = {"XRD": "pymatgen/GSAS-II pattern simulation", "ATOM": "universal MLIP + DFT single point",
           "XAS": "FEFF/OmniXAS", "TEM": "abTEM multislice", "SEM": None, "PROCESS": None}


def family(n):
    # FIX (orchestrator, 2026-09-20): technique_norm may be a LIST when a node's panel comes from two
    # instruments ("SEM-EDS", "AC HAADF-STEM with line profiles"); the back-fill writes those as lists.
    # Take the first element, which is the instrument the lane rule also keys on.
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


def cut(graph_path, spec_path, group_id):
    g, s, N, inn, out, nec = load(graph_path, spec_path)
    traces = []
    tid = 0

    def new(**kw):
        nonlocal tid; tid += 1
        rec = {"id": f"T{tid}", "group_id": group_id, **kw}; traces.append(rec); return rec

    claims = [n["id"] for n in g["nodes"] if is_spine(n)]
    for c in claims:
        ev_in = [e for e in inn[c] if is_obs(N[e["src"]])]
        fm_ev = [e for e in ev_in if family(N[e["src"]]) in FM_FAMILIES and nec.get(e["src"]) in ("necessary", "corrective")]
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
            mask = {"infer": "hide the observation; hand over the panel(s)",
                    "explain": "hide the mechanism; show the rival" if sub == "mechanism" else "hide the ruling; show the claim and the panel"}[root]
            w = walk(N, inn, out, c, [ev])
            if root == "infer":
                hidden = [ev, c] + [x["node"] for x in w if x["role"] == "downstream"]
            elif sub == "mechanism":
                hidden = [c]
            else:
                hidden = [ev]
            new(root=root, subtype=sub, seed_claim=c, evidence=[ev], hidden=hidden, branch=f"{rel} edge {ev} -> {c}",
                fm_family=fam, lift=lift, floor={"reaches": floor_reaches, "support": floor_support},
                depth=depth, depth_families=depth_fams, channels_involved=involved, mask=mask, grader=grader,
                status=status, ruling=why, walk=w)

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

    # --- explain at a claim with two competing causes (branch: which cause accounts for the optimum)
    for c in claims:
        causes = [e["src"] for e in inn[c] if e["rel"] == "causes" and is_spine(N[e["src"]])]
        if len(causes) >= 2 and N[c]["type"].startswith("PRP"):
            fm_support = [i for cc in causes for i in support_of(N, inn, cc) if family(N[i]) in FM_FAMILIES]
            if not fm_support: continue
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
        for st in t.get("walk", []):
            if st["node"] in seen and st["role"] in ("context", "downstream"): continue
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
        t["linear"] = linearize(N, inn, out, t)
    return g, traces


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
    # FIX (orchestrator, 2026-09-20): same list-valued technique_norm as in family() above
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
        p = add("puzzle", [c] + ev_of(c), f"Observation to explain: {N[c]['label']}. Its optimum: {target} vol%.")
        k = add("candidates", causes, "Candidate causes: " + " | ".join(f"{x}: {N[x]['label'][:70]}" for x in causes), [p])
        # test the rivals first so the rejection comes early
        def ruling(x):
            ev = ev_of(x); o = optimum(N, x) or next((optimum(N, i) for i in ev if optimum(N, i)), None)
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
    json.dump({"paper_id": g["paper_id"], "title": g["title"], "traces": traces}, open(out_path, "w"), indent=1)
    from collections import Counter
    print(f"{len(traces)} traces:", dict(Counter((t['root'], t['status']) for t in traces)))
    for t in traces:
        print(f"  {t['id']:3s} {t['root']:9s} {t['subtype']:16s} seed={t['seed_claim']:4s} ev={t['evidence']} depth={t['depth']} {t['status']:7s} {t['ruling'][:70]}")
