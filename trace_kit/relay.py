"""relay.py (v07): dispatch net-* subagents through a relay subagent, and harvest their replies from their own transcripts.

The net-* agents take their packet inline. At 200 papers the packets cannot all pass through the main session, so a relay
(a general-purpose subagent) reads each prompt file and dispatches the named agent with the file's content. The relay is
not trusted: harvest reads every dispatched agent's own transcript, checks the prompt it received against the prompt file
(harvest.read, the same check as v06c), and writes the reply from that transcript, not from anything the relay wrote.

  relay.py instructions <jobs.json> [parallel]   the relay's prompt
  relay.py harvest <jobs.json> <relay_id> [<tasks_dir>]
      jobs.json: [{"id", "agent", "prompt": path, "out": path}]; writes each job's reply to its out path and
      <jobs.json>.harvest.json (per job: agent id, prompt exact, dispatches); exits 2 when a job is missing or differs
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harvest import read

def instructions(jobs_path, parallel="5"):
    jobs = json.load(open(jobs_path))
    return (f"You are a relay. The file {os.path.abspath(jobs_path)} lists {len(jobs)} jobs, each with an \"agent\" type and a "
            "\"prompt\" file path. For every job: read the prompt file (cat it with Bash so you see the raw bytes), then call the "
            "Agent tool with subagent_type set to the job's agent, a short description (the job id), and as prompt the file's "
            "content byte for byte: no preamble, no edits, no trimming inside the text, and no wrapper of any kind (the prompt "
            "starts with the file's first character, never with a tag such as <result> or <output>). Dispatch at most "
            f"{parallel} at a time and wait for replies before dispatching more. Do not answer any job yourself, do not read the "
            "replies closely, and do not write any files. If a dispatch is refused (for example a concurrency limit), wait for a "
            "running agent to finish and dispatch it again. When every job has a reply, hand back one line: "
            "\"DONE <n dispatched> <n replies>\".")

TASK_DIRS = "/tmp/claude-1000/-home-aid1-Documents-causalmat/*/tasks"

def transcript(aid, tasks_dir=None):
    """an agent's transcript: in tasks_dir, else in any session's tasks dir on this host (the session id changes on restart)"""
    if tasks_dir and os.path.exists(os.path.join(tasks_dir, aid + ".output")): return os.path.join(tasks_dir, aid + ".output")
    hits = glob.glob(os.path.join(TASK_DIRS, aid + ".output"))
    return hits[0] if hits else os.path.join(tasks_dir or "", aid + ".output")

def dispatches(relay_tr):
    """Agent tool_use calls in the relay transcript: (subagent_type, prompt, agent id)."""
    uses, ids = {}, {}
    for line in open(relay_tr):
        try: m = json.loads(line)
        except ValueError: continue
        c = (m.get("message") or {}).get("content")
        if not isinstance(c, list): continue
        for b in c:
            if b.get("type") == "tool_use" and b.get("name") == "Agent":
                uses[b["id"]] = (b["input"].get("subagent_type"), b["input"].get("prompt", ""))
            elif b.get("type") == "tool_result" and b.get("tool_use_id") in uses:
                txt = json.dumps(b.get("content"))
                mm = re.search(r"agentId: (\w+)", txt)
                if mm: ids[b["tool_use_id"]] = mm.group(1)
    return [(uses[k][0], uses[k][1], ids.get(k)) for k in uses]

def unescape(s):
    """a JSON \\uXXXX escape inside a packet and the character it encodes are the same text; relays decode them"""
    return re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)

def same(p, want): return p.strip() == want or unescape(p.strip()) == unescape(want)

def harvest(jobs_path, relay_id, tasks_dir):
    jobs = json.load(open(jobs_path))
    D = dispatches(transcript(relay_id, tasks_dir))
    rep, bad = [], 0
    for j in jobs:
        want = open(j["prompt"]).read().strip()
        cand = [(a, p, i) for a, p, i in D if a == j["agent"] and same(p, want) and i]
        rec = {"id": j["id"], "agent": j["agent"], "dispatches": len(cand)}
        done = None
        for a, p, i in reversed(cand):
            tr = transcript(i, tasks_dir)
            if not os.path.exists(tr): continue
            prompt, reply = read(tr)
            if reply and reply.strip():
                done = (i, same(prompt, want), reply); break
        if not done:
            near = [i for a, p, i in D if a == j["agent"] and not same(p, want) and p.strip()[:200] == want[:200]]
            rec.update({"status": "DIFFERS" if near else "MISSING"}); bad += 1
        else:
            i, exact, reply = done
            os.makedirs(os.path.dirname(os.path.abspath(j["out"])), exist_ok=True)
            open(j["out"], "w").write(reply)
            rec.update({"status": "ok" if exact else "DIFFERS", "agent_id": i, "prompt_exact": exact})
            bad += not exact
        rep.append(rec)
    json.dump({"relay": relay_id, "n_dispatches": len(D), "jobs": rep}, open(jobs_path + ".harvest.json", "w"), indent=1)
    print(f"{len(jobs)} jobs, {len(D)} dispatches, {sum(r['status'] == 'ok' for r in rep)} ok,"
          f" {[r['id'] + ':' + r['status'] for r in rep if r['status'] != 'ok']}")
    if bad: sys.exit(2)

if __name__ == "__main__":
    if sys.argv[1] == "instructions": print(instructions(*sys.argv[2:]))
    else: harvest(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
