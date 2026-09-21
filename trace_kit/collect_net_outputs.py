"""collect_net_outputs.py: turn subagent outputs into verdicts.

Claude Code writes each subagent's reply to nets/<paper>/<packet-name>.out.txt, and each grader reply to
nets/<paper>/<packet-name>.grade.txt (first word CORRECT | PARTIAL | WRONG | ABSTAIN).

  python collect_net_outputs.py --dir nets/<paper> --out nets/<paper>/verdicts.json
Also emits the grader packets it needs, if any .out.txt has no .grade.txt yet:
  nets/<paper>/<packet-name>.grader.json  ({"system","user"}) for the grader subagent.
"""
import argparse, glob, json, os, re
from collections import defaultdict

GRADE_SYS = "You grade a short answer against an answer key. Reply with one word first: CORRECT, PARTIAL, WRONG, or ABSTAIN (if the answer says CANNOT DETERMINE), then one sentence why."


def first_word(path):
    if not os.path.exists(path): return None
    w = open(path).read().strip().split()
    return w[0].strip(".,:").upper() if w else None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dir", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    keys = json.load(open(os.path.join(a.dir, "_keys.json")))
    packets = {os.path.basename(p)[:-5]: json.load(open(p)) for p in glob.glob(os.path.join(a.dir, "T*.json")) if not p.endswith((".grader.json",))}
    verdicts = defaultdict(dict); pending = 0
    for name, pk in packets.items():
        tid, net = pk["trace"], pk["net"]
        out_p = os.path.join(a.dir, name + ".out.txt"); grade_p = os.path.join(a.dir, name + ".grade.txt")
        if not os.path.exists(out_p): verdicts[tid].setdefault("missing", []).append(name); continue
        ans = open(out_p).read().strip()
        if net in ("floor", "floor_masked", "fullarm"):
            if "CANNOT DETERMINE" in ans.upper(): g = "ABSTAIN"
            else:
                g = first_word(grade_p)
                if g is None:
                    json.dump({"system": GRADE_SYS, "user": f"Question: {pk['user'].split('Question:')[-1].split(chr(10))[0].strip()}\nAnswer key: {keys[tid]['answer_key']}\nCandidate answer: {ans}"},
                              open(os.path.join(a.dir, name + ".grader.json"), "w"), indent=1); pending += 1; g = "PENDING"
            verdicts[tid][net] = {"grade": g, "answer": ans[:500]}
        elif net == "reread":
            pid = name.split(".reread.")[1]
            g = first_word(grade_p)
            if g is None:
                obs = "\n".join(keys[tid]["observations"].values())
                json.dump({"system": GRADE_SYS.replace("answer key", "reference observation"), "user": f"Reference observation (from the graph): {obs}\nCandidate description of panel {pid}: {ans}\nDoes the description agree with the reference for this panel?"},
                          open(os.path.join(a.dir, name + ".grader.json"), "w"), indent=1); pending += 1; g = "PENDING"
            verdicts[tid].setdefault("reread", {})[pid] = {"grade": g, "description": ans[:400]}
        elif net == "judge":
            try: j = json.loads(re.search(r"\{.*\}", ans, re.S).group(0))
            except Exception: j = {"raw": ans[:400]}
            verdicts[tid]["judge"] = {"pass": bool(j.get("answerable_from_given")) and all(j.get("steps_follow", [])), "verdict": j}
    # derived flags per trace
    for tid, v in verdicts.items():
        f, fm, fa = v.get("floor", {}).get("grade"), v.get("floor_masked", {}).get("grade"), v.get("fullarm", {}).get("grade")
        v["flags"] = {
            "floor_pass": f in ("WRONG", "ABSTAIN", "PARTIAL"),
            "memory": f == "CORRECT" and fm != "CORRECT",
            "text_sufficient": f == "CORRECT" and fm == "CORRECT",
            "reread_pass": all(x["grade"] in ("CORRECT", "PARTIAL") for x in v.get("reread", {}).values()) if v.get("reread") else None,
            "quarantine": f in ("WRONG", "ABSTAIN") and fa in ("WRONG", "ABSTAIN"),
            "judge_pass": v.get("judge", {}).get("pass"),
        }
    json.dump(verdicts, open(a.out, "w"), indent=1)
    n = len(verdicts); flags = [v["flags"] for v in verdicts.values()]
    summ = {k: sum(1 for x in flags if x.get(k)) for k in ("floor_pass", "memory", "text_sufficient", "quarantine", "judge_pass")}
    summ["reread_pass"] = sum(1 for x in flags if x.get("reread_pass") is True); summ["traces"] = n; summ["pending_grades"] = pending
    print(json.dumps(summ)); print("every verdict here is model against model; no human checked any item")


if __name__ == "__main__":
    main()
