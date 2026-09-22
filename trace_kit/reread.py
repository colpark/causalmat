"""reread.py (v07 A2): a second read of every given panel of every open trace, graded against the evidence node.

  reread.py build <cut.traces.json> <graph.json> <out_dir>
      writes <out_dir>/reread.json (one task per distinct given panel: crop path, the traces and evidence nodes that cite
      it) and <out_dir>/<panel>.reread.txt, the net-reread prompt (the image path only: no label, no question)
  reread.py graph <graph.json> <out_dir> [img_dir]
      the graph-time panel check (v07 G): one task per panel cited by any node of the graph, before the cut. Units are
      (node, all its panel_ids) under the pseudo-trace "G". A panel already read (its .reread.out.txt exists for the same
      crop) is not read again.
  reread.py grade <out_dir> <map.txt> <tasks_dir>
      map lines 'agent panel': takes each reread reply from its transcript, writes <panel>.reread.out.txt and one
      net-grader prompt per (panel, evidence node): <panel>.<node>.grader.txt
  reread.py apply <out_dir> <map.txt> <tasks_dir>
      map lines 'agent panel node': takes each grader reply, writes <panel>.<node>.grader.out.txt, then reread.json gets
      the verdicts and a per-trace flag list. A WRONG verdict (the second read contradicts the evidence node) flags the
      trace: it goes to inspect with cause graph before the full and floor arms are spent on it.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cut_traces import panel_record, store_for
from harvest import read

def pname(pid): return pid.split("#")[1]

def clean(desc):
    # the reader's housekeeping lines (which file it read, remarks about its own context) are not part of the description
    desc = re.sub(r"</?(invoke|message|parameter)[^>]*>", "", desc).replace("\ufffd", "")   # stray tool markup, undecodable bytes
    keep = [l for l in desc.strip().splitlines() if not re.match(r"\s*(File( path)? read:|Note:|Image: /|I read only this image|I did not identify)", l)]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(keep)).strip()

def grader_prompt(descs, node_label):
    """descs: [(panel name, reread reply)] for the given panels the evidence node cites, graded together: a node that
    states a trend across panels cannot be confirmed by one panel alone, and one panel read alone is not a contradiction"""
    many = len(descs) > 1
    cand = "\n\n".join((f"Panel {p}: " if many else "") + clean(d) for p, d in descs)
    return (f"Question: What {'do these figure panels' if many else 'does this figure panel'} show?\n\n"
            f"Answer key (answer_scope: full - what the paper's evidence node says {'these panels show' if many else 'this panel shows'}): {node_label}\n\n"
            "Grading note: the candidate is " + ("a set of independent descriptions, one per panel, each written from that panel alone "
            "without the paper and without seeing the other panels. " if many else "an independent description of the panel image, written without the paper. ") +
            "CORRECT if it agrees with the key on what the key says is visible; PARTIAL if it does not mention the key's "
            "feature, or does not draw a comparison the key draws, but does not contradict it; WRONG only if it contradicts the key "
            "(a different feature, trend, shape or technique).\n\n"
            f"Candidate answer:\n{cand.strip()}")

def units(R):
    """grading units: (node, given panels of one trace that the node cites), deduplicated across traces"""
    U = {}
    for p, k in R["tasks"].items():
        for c in k["cited_by"]:
            for n in c["nodes"]:
                U.setdefault((c["trace"], n), []).append(p)
    out = {}
    for (T, n), ps in U.items():
        key = n + "." + "+".join(sorted(ps))
        out.setdefault(key, {"node": n, "panels": sorted(ps), "traces": []})["traces"].append(T)
    return out

def build(cut_path, graph_path, out, img_dir=None):
    # img_dir: the crop is copied there under a hashed name, so the path the reader sees names no journal or paper
    cut = json.load(open(cut_path)); g = json.load(open(graph_path)); N = {n["id"]: n for n in g["nodes"]}
    store = store_for(graph_path)
    os.makedirs(out, exist_ok=True)
    tasks = {}
    for t in cut["traces"]:
        if t["status"] != "open": continue
        for pid in t.get("given_panels") or []:
            rec = panel_record(store, pid) or {}
            nodes = [ev for ev in t["evidence"] if pid in (N[ev].get("panel_ids") or [])] or list(t["evidence"])
            k = tasks.setdefault(pname(pid), {"panel": pid, "crop": rec.get("crop"), "cited_by": []})
            k["cited_by"].append({"trace": t["id"], "nodes": nodes})
    for k in tasks.values():
        k["node_labels"] = {n: N[n]["label"] for c in k["cited_by"] for n in c["nodes"]}
        k["crop"] = os.path.realpath(k["crop"])
        if img_dir:
            import hashlib, shutil; os.makedirs(img_dir, exist_ok=True)
            k["image"] = os.path.join(os.path.realpath(img_dir), hashlib.sha1(k["panel"].encode()).hexdigest()[:16] + os.path.splitext(k["crop"])[1])
            shutil.copyfile(k["crop"], k["image"])
        open(os.path.join(out, f"{pname(k['panel'])}.reread.txt"), "w").write(k.get("image") or k["crop"])
    json.dump({"paper": cut["paper_id"], "tasks": tasks}, open(os.path.join(out, "reread.json"), "w"), indent=1)
    print(f"{len(tasks)} panels to reread, {sum(len(k['node_labels']) for k in tasks.values())} grader checks")

def graph(graph_path, out, img_dir=None):
    import hashlib, shutil
    g = json.load(open(graph_path)); store = store_for(graph_path); os.makedirs(out, exist_ok=True)
    old = json.load(open(os.path.join(out, "reread.json")))["tasks"] if os.path.exists(os.path.join(out, "reread.json")) else {}
    tasks = {}
    for n in g["nodes"]:
        for pid in n.get("panel_ids") or []:
            rec = panel_record(store, pid) or {}
            if not rec.get("crop"): continue
            k = tasks.setdefault(pname(pid), {"panel": pid, "crop": os.path.realpath(rec["crop"]), "cited_by": [{"trace": "G", "nodes": []}], "node_labels": {}})
            k["cited_by"][0]["nodes"].append(n["id"]); k["node_labels"][n["id"]] = n["label"]
    for p, k in tasks.items():
        if img_dir:
            os.makedirs(img_dir, exist_ok=True)
            k["image"] = os.path.join(os.path.realpath(img_dir), hashlib.sha1(k["panel"].encode()).hexdigest()[:16] + os.path.splitext(k["crop"])[1])
            shutil.copyfile(k["crop"], k["image"])
        o = os.path.join(out, f"{p}.reread.out.txt")
        if os.path.exists(o) and (old.get(p) or {}).get("crop") != k["crop"]: os.remove(o)   # the panel id now names another crop
        open(os.path.join(out, f"{p}.reread.txt"), "w").write(k.get("image") or k["crop"])
    json.dump({"paper": g["paper_id"], "graph_time": True, "tasks": tasks}, open(os.path.join(out, "reread.json"), "w"), indent=1)
    todo = [p for p in tasks if not os.path.exists(os.path.join(out, f"{p}.reread.out.txt"))]
    print(f"{len(tasks)} cited panels, {len(todo)} to read, {len(units({'tasks': tasks}))} grader units")
    return todo

def grade(out, mp, tasks_dir):
    R = json.load(open(os.path.join(out, "reread.json")))
    for line in open(mp):
        a, p = line.split()[:2]
        tr = os.path.join(tasks_dir, a + ".output")
        if not os.path.exists(tr): print("MISSING", p); continue
        prompt, reply = read(tr)
        ok = prompt.strip() == open(os.path.join(out, f"{p}.reread.txt")).read().strip()
        open(os.path.join(out, f"{p}.reread.out.txt"), "w").write(reply)
        for n, lab in R["tasks"][p]["node_labels"].items():
            open(os.path.join(out, f"{p}.{n}.grader.txt"), "w").write(grader_prompt(reply, lab))
        print(p, "prompt", "exact" if ok else "DIFFERS", "|", reply.strip()[:70].replace("\n", " "))

def apply(out, mp, tasks_dir):
    R = json.load(open(os.path.join(out, "reread.json")))
    for line in open(mp):
        a, p, n = line.split()[:3]
        tr = os.path.join(tasks_dir, a + ".output")
        if not os.path.exists(tr): print("MISSING", p, n); continue
        prompt, reply = read(tr)
        ok = prompt.strip() == open(os.path.join(out, f"{p}.{n}.grader.txt")).read().strip()
        open(os.path.join(out, f"{p}.{n}.grader.out.txt"), "w").write(reply)
        m = re.match(r"\W*(CORRECT|PARTIAL|WRONG|ABSTAIN)", reply.strip().upper())
        R["tasks"][p].setdefault("verdicts", {})[n] = {"verdict": m.group(1) if m else "UNPARSED", "why": reply.strip(), "prompt_exact": ok}
    flags = {}
    for p, k in R["tasks"].items():
        for c in k["cited_by"]:
            for n in c["nodes"]:
                v = (k.get("verdicts") or {}).get(n, {}).get("verdict")
                if v == "WRONG": flags.setdefault(c["trace"], []).append({"panel": k["panel"], "node": n, "why": k["verdicts"][n]["why"]})
    R["flags"] = flags
    json.dump(R, open(os.path.join(out, "reread.json"), "w"), indent=1)
    print("flags:", {t: [f"{pname(f['panel'])}/{f['node']}" for f in v] for t, v in flags.items()})

if __name__ == "__main__":
    {"build": build, "graph": graph, "grade": grade, "apply": apply}[sys.argv[1]](*sys.argv[2:])
