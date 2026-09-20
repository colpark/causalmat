"""Collapse a full v05 argument graph to the modality-view spec the kit renders.

No prose is generated: every string is taken from the graph (labels, image notes, ids, technique_norm).

Usage: python taxonomy/collapse_modality.py --graph <graph.json> --out <spec.json> [--file name.html]
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from normalize_technique import normalize  # same rule table as part 1

# stage groups, in order; a group may split into two rows when its spine nodes form disjoint branches
GROUPS = [("S0", "HYP", "Hypothesis and design", ("HYP", "DES", "PRC")),
          ("S1", "STR", "Structure state", ("STR",)),
          ("S2", "PRP", "Property state and mechanisms", ("MEC", "PRP")),
          ("S3", "PRF", "Performance state", ("PRF",)),
          ("S4", "DSC", "Conclusion", ("DSC",))]
# MICRO/DIFF are modality-derived placeholders used when no technique string exists anywhere on the node
MODALITY_FAMILY = {"micrograph": "MICRO", "diffraction_pattern": "DIFF", "simulation_render": "ATOM"}
FM_LANES = [("micro", {"SEM", "TEM", "MICRO"}, "Microscopy"),
            ("diff", {"XRD", "DIFF"}, "Diffraction"),
            ("spec", {"XAS"}, "Spectroscopy"),
            ("atom", {"ATOM"}, "Atomistic simulation")]
LANE_SUB = {"micro": "foundation model in hand", "diff": "foundation model candidate",
            "spec": "foundation model candidate", "atom": "foundation model in hand",
            "classic": "collapsed to one node per state"}
SENT = re.compile(r"(?<=[.!?])\s+")


def tech_tags(node):
    """FAMILY:mode tags for a node, and where they came from.

    221 of 432 evidence nodes carry attrs.technique; for the rest the family is read from the node's own
    label and image note with the part-1 rule table, so it is still derived from the graph, never guessed.
    """
    t = (node.get("attrs") or {}).get("technique_norm")
    if t:
        return (t if isinstance(t, list) else [t]), "attrs"
    text = " ".join(filter(None, [node.get("label"), (node.get("attrs") or {}).get("image_note")]))
    tags, flags = normalize(text)
    if tags != ["OTHER"]:
        return tags, "label"
    # last resort: the node's own modality field. It fixes the lane without naming a technique the
    # graph never states, so MICRO/DIFF stay placeholders and are reported as modality-derived.
    m = MODALITY_FAMILY.get(node.get("modality"))
    if m:
        return [m], "modality"
    return [], "none"


def fam(node):
    tags, _ = tech_tags(node)
    return [x.split(":")[0] for x in tags] or None


def two_sentences(text):
    parts = [p for p in SENT.split(" ".join(text.split())) if p]
    return " ".join(parts[:2])


def collapse(g, file_name):
    N = {n["id"]: n for n in g["nodes"]}
    out_edges = defaultdict(list)
    in_edges = defaultdict(list)
    for e in g["edges"]:
        out_edges[e["src"]].append(e)
        in_edges[e["dst"]].append(e)
    spine = [n for n in g["nodes"] if n.get("spine")]

    # ---- states -------------------------------------------------------------------------------
    states, node_state = [], {}
    for sid, stage, title, stages in GROUPS:
        members = [n for n in spine if n["type"].split("/")[0] in stages]
        if not members:
            continue
        members.sort(key=lambda n: [s[0] for s in GROUPS].index(sid) * 100 + list(N).index(n["id"]))
        knw = []
        for m in members:
            for e in in_edges[m["id"]]:
                s = N.get(e["src"])
                if s and s["type"].startswith("KNW") and s["label"] not in knw:
                    knw.append(s["label"])
        head = two_sentences(". ".join(m["label"].rstrip(".") for m in members))
        detail = "Absorbed: " + ", ".join(f"{m['id']} ({m['type']})" for m in members)
        if knw:
            detail += ". Premises: " + "; ".join(knw)
        states.append({"id": sid, "stage": stage, "title": title, "head": head, "detail": detail,
                       "figs": [], "source": ", ".join(m["id"] for m in members)})
        for m in members:
            node_state[m["id"]] = sid

    # ---- which state does an evidence node serve? ----------------------------------------------
    def target_state(nid, depth=0, seen=None):
        seen = seen or set()
        if nid in node_state:
            return node_state[nid]
        if nid in seen or depth > 4:
            return None
        seen.add(nid)
        for e in out_edges[nid]:
            t = target_state(e["dst"], depth + 1, seen)
            if t:
                return t
        return None

    # ---- lanes --------------------------------------------------------------------------------
    obs = [n for n in g["nodes"] if n["type"].startswith("OBS")]
    fams_present = Counter()
    for n in obs:
        if n.get("figs"):
            for f in fam(n) or []:
                fams_present[f] += 1
    lanes, lane_of_family = [], {}
    for key, families, label in FM_LANES:
        if families & set(fams_present):
            techs = sorted({f for f in families if f in fams_present})
            lanes.append({"key": key, "label": f"{label}: {', '.join(techs)}", "sub": LANE_SUB[key]})
            for f in techs:
                lane_of_family[f] = key
    lanes.append({"key": "classic", "label": "Classical tools", "sub": LANE_SUB["classic"]})
    lane_index = {l["key"]: i for i, l in enumerate(lanes)}
    lane_index_keys = set(lane_index)

    MODALITY_LANE = {"micrograph": "micro", "diffraction_pattern": "diff", "simulation_render": "atom"}

    def lane_for(n):
        fams = fam(n) or []
        # a multi-technique string ("SEM-EDS", "AC HAADF-STEM with line profiles") must not set the lane
        # from its first element: the lane comes from the node's own modality and the panel's modality
        # votes, and the technique list only refines the label
        if len(fams) > 1:
            want = MODALITY_LANE.get(n.get("modality"))
            if want and want in lane_index_keys:
                return want
            if n.get("modality"):
                return "spec" if ("XAS" in fams and "spec" in lane_index_keys) else "classic"
            return "classic"
        # a node naming two families (e.g. "HAADF-STEM with EDS line profiles") is placed by the modality
        # of the panel it reads, so a spectrum does not land in the microscopy lane
        mod = n.get("modality")
        want = MODALITY_LANE.get(mod)
        if mod and not want:
            # a spectrum, curve or map is not microscopy or diffraction whatever the label mentions:
            # only XAS is FM-serviceable among these, everything else is classical
            return "spec" if ("XAS" in fams and "spec" in lane_index_keys) else "classic"
        if want and want in lane_index_keys:
            for f in fams:
                if lane_of_family.get(f) == want:
                    return want
            if want in lane_index_keys and len(fams) > 1:
                return want
        for f in fams:
            if f in lane_of_family:
                if want and lane_of_family[f] != want and n.get("modality") in MODALITY_LANE:
                    continue
                return lane_of_family[f]
        return "classic"

    def target_claim(nid, depth=0, seen=None):
        """The first spine node an evidence node feeds. A state absorbs several claims, so the removal
        test must key on the claim: otherwise evidence for one claim looks redundant because a different
        claim in the same state still has support."""
        seen = seen or set()
        if nid in seen or depth > 4:
            return None
        seen.add(nid)
        for e in out_edges[nid]:
            d = N.get(e["dst"])
            if d is not None and d.get("spine"):
                return d["id"]
        for e in out_edges[nid]:
            c = target_claim(e["dst"], depth + 1, seen)
            if c:
                return c
        return None

    # ---- support map, for the removal test ------------------------------------------------------
    def is_shown(n):
        return bool(n.get("figs")) and n.get("image_support") == "shown"

    support = defaultdict(list)          # claim id -> evidence node ids with image_support shown
    claim_of = {}
    for n in obs:
        c = target_claim(n["id"])
        claim_of[n["id"]] = c
        if c and is_shown(n):
            support[c].append(n["id"])

    # ---- lane nodes ----------------------------------------------------------------------------
    groups = defaultdict(list)
    for n in obs:
        st = target_state(n["id"])
        if not st:
            continue
        ln = lane_for(n)
        is_audit = n.get("image_support") in ("contradicts", "not_shown") or (n.get("attrs") or {}).get("text_silent")
        if ln == "classic":
            claim = next((e["dst"] for e in out_edges[n["id"]] if N.get(e["dst"], {}).get("spine")), st)
            key = (ln, st, claim)
        else:
            rel = next((e["mm_op"] for e in out_edges[n["id"]] if e.get("mm_op")), None)
            key = (ln, st, (fam(n) or ["OTHER"])[0], rel, bool(is_audit))
        groups[key].append(n)

    nodes, line_no = [], defaultdict(int)
    for key, members in sorted(groups.items(), key=lambda kv: (kv[0][1], lane_index[kv[0][0]])):
        ln, st = key[0], key[1]
        audit = bool(key[4]) if len(key) > 4 else any(
            m.get("image_support") in ("contradicts", "not_shown") or (m.get("attrs") or {}).get("text_silent")
            for m in members)
        panel_ids = list(dict.fromkeys(p for m in members for p in (m.get("panel_ids") or [])))
        figs = sorted({f for m in members for f in (m.get("figs") or [])})
        techs, tech_src = [], set()
        for m in members:
            tags, src = tech_tags(m)
            tech_src.add(src)
            for t in tags:
                if t not in techs:
                    techs.append(t)
        techs = sorted(techs)
        ops = sorted({e["mm_op"] for m in members for e in out_edges[m["id"]] if e.get("mm_op")})
        verdicts = [m.get("image_support") for m in members if m.get("image_support")]
        verdict = next((v for v in ("contradicts", "not_shown", "partial", "shown") if v in verdicts), None)
        notes = [(m.get("attrs") or {}).get("image_note") for m in members if (m.get("attrs") or {}).get("image_note")]
        conds = [c for m in members for c in ((m.get("attrs") or {}).get("panel_conditions") or [])]
        solves = ""
        for m in members:
            for e in out_edges[m["id"]]:
                d = N.get(e["dst"])
                if d and d.get("spine"):
                    solves = d["label"]
                    break
            if solves:
                break
        head = two_sentences(". ".join(m["label"].rstrip(".") for m in members))
        node = {
            "id": f"{'C' if ln == 'classic' else 'M'}{len(nodes) + 1}",
            "lane": lane_index[ln], "row": st, "line": line_no[st],
            "title": (", ".join(techs) if techs else "evidence") + (f", {', '.join(figs)}" if figs else ""),
            "tech": ", ".join(techs), "figs": figs, "panel": ", ".join(panel_ids) if panel_ids else "",
            "panel_ids": panel_ids, "head": head, "solves": solves,
            "op": ", ".join(o.replace("_", " ") for o in ops), "verdict": verdict,
            "source": ", ".join(m["id"] for m in members),
        }
        node["tech_source"] = "+".join(sorted(tech_src)) if tech_src else "none"
        if conds:
            node["panel_conditions"] = conds
        if notes:
            node["note"] = " ".join(notes)
        if audit:
            node["audit"] = True
        if ln == "classic":
            node["detail"] = "; ".join(f"{m['id']}: {m['label']}" for m in members)
            inner = [f"{m['id']}: {(m.get('attrs') or {}).get('image_note') or m['label']}"
                     for m in members
                     if m.get("image_support") in ("contradicts", "not_shown") or (m.get("attrs") or {}).get("text_silent")]
            if inner:
                node["inner_audit"] = "; ".join(inner)
        line_no[st] += 1
        nodes.append((node, members, ln, st, audit))

    # ---- necessity, by removal on the full graph -------------------------------------------------
    for node, members, ln, st, audit in nodes:
        mine = {m["id"] for m in members}
        claims = [c for c in dict.fromkeys(claim_of.get(m["id"]) for m in members) if c]
        node["claims"] = claims
        others = [i for c in claims for i in support.get(c, []) if i not in mine]
        shown_here = [m["id"] for m in members if is_shown(m)]
        if audit:
            node["necessity"] = "corrective"
            node["necessity_reason"] = (f"Changes support for {st}: "
                                        + "; ".join(f"{m['id']} {m.get('image_support') or 'text_silent'}"
                                                    for m in members if m["id"] not in shown_here)[:240])
        elif shown_here and not others:
            node["necessity"] = "necessary"
            node["necessity_reason"] = (f"Only figure-backed support with image_support shown for "
                                        f"{', '.join(claims) or st} ({', '.join(shown_here)}).")
        elif shown_here and others:
            node["necessity"] = "redundant"
            node["necessity_reason"] = (f"{', '.join(claims) or st} keeps shown support from "
                                        f"{', '.join(others[:4])} after removal.")
        elif others:
            node["necessity"] = "redundant"
            node["necessity_reason"] = (f"No member reaches image_support shown, and {', '.join(claims) or st} "
                                        f"keeps shown support from {', '.join(others[:4])}.")
        else:
            node["necessity"] = "decorative"
            node["necessity_reason"] = (f"No member reaches image_support shown and {', '.join(claims) or st} "
                                        f"has no other figure-backed support.")
    # lane-level test: an FM lane whose removal leaves every state it serves with other shown support
    lane_states = defaultdict(set)
    for node, members, ln, st, audit in nodes:
        lane_states[ln].add(st)
    fm_critical = any(n["necessity"] in ("necessary", "corrective")
                      for n, _, ln, _, _ in nodes if ln != "classic")

    # guards: this class of bug must fail loudly, not quietly flatten the view
    RANK = {"contradicts": 0, "not_shown": 1, "partial": 2, "shown": 3}
    for node, members, ln, st, audit in nodes:
        worst = min((RANK.get(m.get("image_support"), 3) for m in members), default=3)
        assert RANK.get(node["verdict"], 3) <= worst, (
            f"{node['id']}: merged verdict {node['verdict']} ranks above its worst member")
    kinds = {n["necessity"] for n, _, _, _, _ in nodes}
    # the failure this guards against is the flattening the state-keyed bug produced: every node called
    # redundant (or decorative) because some other claim in the same state kept support. Uniform
    # "necessary" is a legitimate outcome when each lane node is the sole support of its own claim.
    assert not (len(kinds) == 1 and kinds <= {"redundant", "decorative"}) or len(nodes) < 3, (
        f"all {len(nodes)} lane nodes share necessity {kinds}; the removal test is not discriminating")

    spec_nodes = [n for n, _, _, _, _ in nodes]
    edges = []
    order = [s["id"] for s in states]
    seen_pairs = set()
    for e in g["edges"]:
        a, b = node_state.get(e["src"]), node_state.get(e["dst"])
        if a and b and a != b and (a, b) not in seen_pairs and order.index(a) < order.index(b):
            seen_pairs.add((a, b))
            edges.append([a, b, e["rel"]])
    doi = g.get("paper_id", "")
    return {"file": file_name, "short": g.get("title", doi)[:60], "journal": (doi.split("/")[0] if "/" in doi else ""),
            "year": g.get("year"), "title": g.get("title", ""), "doi": doi,
            "lanes": lanes, "states": states, "nodes": spec_nodes, "edges": edges, "figs": {},
            "fm_critical": fm_critical}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--file", default=None)
    a = ap.parse_args()
    g = json.load(open(a.graph))
    spec = collapse(g, a.file or (Path(a.out).stem + ".html"))
    json.dump(spec, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(f"{a.out}: {len(spec['states'])} states, {len(spec['nodes'])} nodes, "
          f"lanes {[l['key'] for l in spec['lanes']]}, fm_critical={spec['fm_critical']}")
    print("  necessity:", dict(Counter(n["necessity"] for n in spec["nodes"])))
