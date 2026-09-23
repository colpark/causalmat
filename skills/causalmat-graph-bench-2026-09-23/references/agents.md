# The subagents and the relay discipline

Seven `net-*` agents. Copy `agents/*.md` to `.claude/agents/`. **Restart Claude Code after any edit** —
the registry is cached, and a stale definition is invisible until you dispatch and read back the rules.

| agent | tools | sees | returns |
|---|---|---|---|
| `net-reread` | `Read` | exactly one image file | a description of that panel |
| `net-panel-judge` | `Read` | the crop, the node label, the reader's description, the grader's verdict | `{"ruling": "real"\|"ok", "why": ...}` |
| `net-fullarm` | `Read` | context, panel captions, question, the panel image paths | an answer, ≤6 sentences |
| `net-floor` | none | the same text, no images | an answer, ≤5 sentences |
| `net-grader` | none | a candidate answer and the key | `CORRECT`/`PARTIAL`/`WRONG`/`ABSTAIN` + why |
| `net-writer` | none | the whole trace including hidden nodes | question, key, grading, `asks_for` |
| `net-judge` | none | the graph and the packet, no images | structural rulings, JSON only |

The graph-building **staff** and the **inspector** are general-purpose subagents pointed at a prompt file
(`taxonomy/prompts/v07_staff.md`, the generated `inspect.md`), not `net-*` agents, because they need
`Read`, `Write` and `Bash`.

## Why the tool lists are what they are

`net-floor` having **no tools at all** is what makes the floor a floor. If it can read a file it is not a
text-only arm. `net-reread` having only `Read` and one image is what makes the second read blind — it
cannot look up the caption that would tell it which sample the panel shows, which is exactly the
condition the check is meant to simulate and also the source of most of its false positives.

## The relay

Batches of jobs go through a **relay**: a general-purpose subagent that reads each job's prompt file and
dispatches the named agent with the file's content byte for byte.

```
python3 trace_kit/relay.py instructions <jobs.json> [parallel]   # the relay's prompt
python3 trace_kit/v07_batch.py merge <name> <stage> <papers...>  # one relay across several papers
python3 trace_kit/v07_batch.py harvest <name> <relay_id>         # verify and collect
```

**The relay is not trusted.** `harvest` reads every dispatched agent's own transcript, checks the prompt
it actually received against the prompt file, and writes the reply from the transcript — not from
anything the relay says. A job whose prompt differs comes back `DIFFERS`; a job with no reply comes back
`MISSING`. Both mean: rebuild those jobs into a redo batch and re-dispatch.

This is not paranoia. In the reference run relays altered prompts three times and one relay ended its
hand-back by pasting the replies and asserting "the payloads above are the only copy" — which was false;
the replies were in the subagents' transcripts, where harvest found them.

Relay prompt rules worth keeping:

- "Dispatch at most N at a time and wait for replies before dispatching more."
- "If a dispatch is refused (for example a concurrency limit), wait and dispatch it again."
- "If a dispatched agent fails with an API error, dispatch it once more; if it fails again, skip it and
  carry on." — one relay died mid-batch on a transient API error and lost 8 of 12 jobs.
- "Do not write any files, and **do not paste the replies into your hand-back**."

## Concurrency

The cap is 20 including relay children. Four relays at 5 children each is already at the cap and
everything else queues. In practice: two or three relays, 4–6 children each, and let the rest wait.

## Dispatch accounting

`python3 trace_kit/v07.py log <P> <kind> <agent_id>` records a staff, judge, inspector or relay dispatch
so `batch.csv`'s `subagent_dispatches` and `wall_minutes` are real. Harvested job files carry their own
agent ids. Without this, cost per paper is a guess.
