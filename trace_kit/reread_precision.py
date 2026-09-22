"""reread_precision.py (v07 F): how often a second-read flag is a real citation error.

  reread_precision.py build <out_dir> <reread_dir>...   one judge prompt per flagged unit (node, panels): the crops, the
                                                       node label, the net-reread descriptions, the grader's verdict
                                                       -> <out_dir>/units.json, <out_dir>/<k>.judge.txt, jobs.json
  reread_precision.py harvest <out_dir> <jobs.json.harvest.json>...   rulings from the replies relay.py harvest wrote
                                                       (each prompt checked against its file) -> units.json
  reread_precision.py tally <out_dir>                  counts per ruling and precision (real over all)
A flag is a unit (evidence node, cited panels) the grader ruled WRONG; one unit can flag several traces.
Every verdict is model against model.
"""
import json, os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reread import clean

RULINGS = ("real", "wording", "partial", "unclear")

def prompt(u):
    imgs = "\n".join(f"- panel {p}: {u['images'][p]}" for p in u["panels"])
    descs = "\n\n".join(f"Panel {p}:\n{clean(u['descs'][p])}" for p in u["panels"])
    return f"""You are a judge. A blind second reader described figure panel(s) without the paper; a grader compared the description with the paper graph's evidence node and ruled WRONG (a contradiction). Decide whether that flag is a real citation error.

Open every image below with the Read tool and look at it yourself before ruling. Do not open any other file.
{imgs}

Evidence node {u['node']} (what the graph says these panels show):
{u['label']}

Second reader's description(s):
{descs}

Grader's verdict:
{u['why']}

Rule one of:
- real: the panel(s) do not show what the node says (a different kind of data, a different sample or quantity, or the image contradicts the node). The citation or the node is wrong.
- wording: the panel(s) do show what the node says; the flag comes from the reader naming or framing the same features differently, or from the grader reading a difference in words as a contradiction.
- partial: some of what the node says is shown and some is not (for example one of several panels is wrong, or the node overstates what is visible).
- unclear: you cannot tell from the image(s).

Reply with JSON only: {{"ruling": "real|wording|partial|unclear", "why": "one or two sentences naming what the image shows"}}"""

def build(out, *dirs):
    os.makedirs(out, exist_ok=True); U = {}
    for R in dirs:
        rr = json.load(open(os.path.join(R, "reread.json"))); P = rr["paper"].replace("/", "__")
        for key, u in rr.get("units", {}).items():
            if u.get("verdict") != "WRONG": continue
            t = [rr["tasks"][p] for p in u["panels"]]
            k = f"u{len(U)+1:02d}"
            U[k] = {"paper": P, "unit": key, "node": u["node"], "panels": u["panels"], "traces": u["traces"],
                    "label": t[0]["node_labels"][u["node"]], "why": u["why"],
                    "images": {p: rr["tasks"][p].get("image") or rr["tasks"][p]["crop"] for p in u["panels"]},
                    "crops": {p: rr["tasks"][p]["crop"] for p in u["panels"]},
                    "descs": {p: open(os.path.join(R, f"{p}.reread.out.txt")).read() for p in u["panels"]}, "reread_dir": R}
            open(os.path.join(out, f"{k}.judge.txt"), "w").write(prompt(U[k]))
    json.dump(U, open(os.path.join(out, "units.json"), "w"), indent=1)
    json.dump([{"id": k, "agent": "general-purpose", "prompt": os.path.join(out, f"{k}.judge.txt"), "out": os.path.join(out, f"{k}.judge.out.txt")} for k in U],
              open(os.path.join(out, "jobs.json"), "w"), indent=1)
    print(f"{len(U)} flagged units, {sum(len(u['traces']) for u in U.values())} trace flags")

def harvest(out, *harvest_files):
    """rulings from the <k>.judge.out.txt files relay.py harvest wrote (it checked each prompt against its file)"""
    U = json.load(open(os.path.join(out, "units.json")))
    H = {j["id"]: j for h in harvest_files for j in json.load(open(h))["jobs"]}
    for k, u in U.items():
        f = os.path.join(out, f"{k}.judge.out.txt")
        if k not in H or H[k].get("status") != "ok" or not os.path.exists(f): continue
        reply = open(f).read(); m = re.search(r"\{.*\}", reply, re.S); j = json.loads(m.group(0)) if m else {}
        u.update({"agent": H[k]["agent_id"], "prompt_exact": H[k]["prompt_exact"], "ruling": j.get("ruling", "UNPARSED"), "ruling_why": j.get("why", reply.strip())})
        print(k, u["ruling"], "exact" if u["prompt_exact"] else "DIFFERS")
    json.dump(U, open(os.path.join(out, "units.json"), "w"), indent=1)

def tally(out):
    U = json.load(open(os.path.join(out, "units.json")))
    c = {r: sum(u.get("ruling") == r for u in U.values()) for r in RULINGS}
    print(c, f"precision {c['real']}/{len(U)} = {100*c['real']/max(1,len(U)):.0f}%")
    return c

if __name__ == "__main__":
    {"build": build, "harvest": harvest, "tally": tally}[sys.argv[1]](*sys.argv[2:])
