"""writer.py: the reference reasoning, and the dependency judgement, per step.

  python3 trace_kit_v4/writer.py prompts
  python3 trace_kit_v4/writer.py collect

net-writer is the AUTHOR, not the answerer: it sees the step's claim, its observations and the
previous step's output. It never sees a MatMech span or MatMech reasoning-chain text -- the trace
carries those only under `provenance_NOT_SOLVER_VISIBLE`, and nothing from there enters a prompt.

Every sentence must carry the node id it came from; a sentence with no node id is marked
`writer inference`, so an unsourced claim is visible rather than blended in.

A step whose claims are a subset of the previous step's establishes nothing new. That is decided
here, before any dispatch, and marked `restatement` -- such a step cannot carry a dependency because
it does not advance the argument.

Every verdict is model against model.
"""
import json, os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TR = sorted(glob.glob(os.path.join(ROOT, 'results/v4/*/trace.json')))

ASK = """Write the reasoning an expert would give for this step, using ONLY the node labels above.

Five parts, in order:
1. what each observation shows - one line per panel, naming the panel
2. the intermediate proposition it supports
3. the assumption the inference needs
4. what remains open
5. what is handed to the next step

Every sentence ends with the node id it comes from, in square brackets, like [o3]. A sentence that
comes from no node ends with [writer inference] instead. Do not omit the marker on any sentence.

Then judge the dependency. Could this step's question be answered WITHOUT the previous step's
conclusion? Answer honestly; a step that stands alone is a real finding, not a failure.

Reply as JSON only:
{"observations": ["... [o3]"], "proposition": "... [n8]", "assumption": "... [writer inference]",
 "open": "... [writer inference]", "handoff": "... [n8]",
 "dependency": {"needs_previous": true or false,
                "why": "one line: why the step fails without that input, or why it stands alone"}}"""

END_ASK = """Write the end-to-end reasoning for this whole trace in the same form: what the chain
establishes, step by step, and what it rests on. Every sentence ends with a node id in square
brackets, or [writer inference].

Then name the weakest step and say why in one line.

Reply as JSON only:
{"reasoning": ["... [n8]"], "weakest_step": 2, "why_weakest": "one line"}"""


def step_block(t, s, N, prev):
    L = [f"Setting: {t['setup']}", ""]
    if prev:
        L += [f"The previous step (step {prev['step']}) established: {prev['output']}",
              f"This step's question refers back to it as: \"{s['refers_to_previous']}\"", ""]
    L.append(f"This step's question, as the solver sees it: {s['question']}")
    c = s.get('combining')
    if c:
        L += ["",
              "This step is meant to carry a CROSS-STEP inference. The proposition it should reach "
              "combines the previous step's output with this step's evidence:",
              f"  {c['proposition']}",
              f"  from step {prev['step'] if prev else '-'}: {c['from_previous']}",
              f"  from this step: {c['from_this']}",
              "Your reasoning must actually perform that combination, using both sets of numbers.",
              "The `proposition` field itself must carry the combination: it has to quote a quantity "
              "from the previous step AND a quantity from this step and state what their comparison "
              "implies. A proposition that restates only this step's finding is wrong, even if the "
              "combination appears elsewhere in your answer."]
    L.append(f"The claim this step lands on:")
    for c in s['claims']:
        L.append(f"  [{c}] {(N.get(c) or {}).get('label')}")
    L.append("")
    L.append(f"Observations behind it ({s['technique']}):")
    for p, o in zip(s['panels'], s['observations'] + [None] * len(s['panels'])):
        pass
    for i, obs in enumerate(s['observations']):
        L.append(f"  [obs{i+1}] {obs}")
    L.append("Panels cited: " + ', '.join(p['suffix'] for p in s['panels']))
    return "\n".join(L)


def prompts():
    jobs = []
    for f in TR:
        t = json.load(open(f)); d = os.path.dirname(f)
        N = {n['id']: n for n in json.load(open(os.path.join(ROOT, t['graph'])))['nodes']}
        wd = os.path.join(d, 'writer'); os.makedirs(wd, exist_ok=True)
        for i, s in enumerate(t['steps']):
            prev = t['steps'][i - 1] if i else None
            # decided before dispatch: a step landing only on claims already established
            if prev and set(s['claims']) <= set(prev['claims']):
                s['restatement'] = True
            p = os.path.join(wd, f"step{s['step']}.txt")
            open(p, 'w').write(step_block(t, s, N, prev) + "\n\n" + ASK)
            jobs.append({'id': f"{t['trace']}/step{s['step']}", 'agent': 'net-writer',
                         'prompt': os.path.abspath(p),
                         'out': os.path.abspath(os.path.join(wd, f"step{s['step']}.out.txt"))})
        L = [f"Setting: {t['setup']}", "", "The chain, step by step:"]
        for s in t['steps']:
            L.append(f"  Step {s['step']}: question -- {s['question']}")
            for c in s['claims']:
                L.append(f"     establishes [{c}] {(N.get(c) or {}).get('label')}")
            for j, obs in enumerate(s['observations']):
                L.append(f"     from [obs{j+1}] {obs}")
        p = os.path.join(wd, 'endtoend.txt')
        open(p, 'w').write("\n".join(L) + "\n\n" + END_ASK)
        jobs.append({'id': f"{t['trace']}/endtoend", 'agent': 'net-writer',
                     'prompt': os.path.abspath(p),
                     'out': os.path.abspath(os.path.join(wd, 'endtoend.out.txt'))})
        json.dump(t, open(f, 'w'), indent=1)
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v4writer.json'), 'w'), indent=1)
    print(f"{len(jobs)} writer jobs ({len(TR)} traces)")


def _objects(txt):
    """every balanced {...} run, longest first -- a reply may hold more than one object"""
    out, depth, start = [], 0, None
    for i, c in enumerate(txt or ''):
        if c == '{':
            if depth == 0: start = i
            depth += 1
        elif c == '}' and depth:
            depth -= 1
            if not depth: out.append(txt[start:i + 1])
    return sorted(out, key=len, reverse=True)


def parse(txt):
    """A greedy {.*} span breaks on two objects in one reply ("Extra data") and on a single
    malformed one. Try each balanced object, prefer one carrying `dependency`, and if none parses,
    recover the judgement by regex rather than discard a decision the reply plainly states."""
    best = None
    for o in _objects(txt):
        try: j = json.loads(o)
        except Exception: continue
        if 'dependency' in j: return j
        best = best or j
    if best: return best
    m = re.search(r'"needs_previous"\s*:\s*(true|false)', txt or '', re.I)
    if m:
        w = re.search(r'"why"\s*:\s*"([^"]{0,400})', txt or '')
        return {'_recovered_by_regex': True,
                'dependency': {'needs_previous': m.group(1).lower() == 'true',
                               'why': w.group(1) if w else None}}
    return None


def collect():
    # once v4b has re-judged on the data, its labels are the labels. The writer's own
    # needs_previous answer is kept in the reasoning but no longer decides anything.
    v4b = {}
    f4 = os.path.join(ROOT, 'results/v4/dependency_v4b.json')
    if os.path.exists(f4):
        for r in json.load(open(f4))['rows']:
            v4b[(r['trace'], r['step'])] = r
    tally = collections.Counter()
    for f in TR:
        t = json.load(open(f)); d = os.path.dirname(f)
        dep = []
        for i, s in enumerate(t['steps']):
            j = parse(open(os.path.join(d, 'writer', f"step{s['step']}.out.txt")).read()) \
                if os.path.exists(os.path.join(d, 'writer', f"step{s['step']}.out.txt")) else None
            s['reference_reasoning'] = j
            prev = t['steps'][i - 1] if i else None
            if not prev:
                rec = {'step': s['step'], 'output': s['output'], 'input_from_previous': None,
                       'dependency': 'first step', 'why': 'no predecessor'}
            elif s.get('restatement'):
                rec = {'step': s['step'], 'output': s['output'],
                       'input_from_previous': prev['output'], 'dependency': 'none',
                       'why': 'restatement: this step lands only on claims step '
                              f"{prev['step']} already established ({', '.join(s['claims'])})"}
            elif (t['trace'], s['step']) in v4b:
                r4 = v4b[(t['trace'], s['step'])]
                rec = {'step': s['step'], 'output': s['output'],
                       'input_from_previous': prev['output'], 'dependency': r4['new'],
                       'why': r4.get('proposition') or r4.get('why_none'),
                       'kind': r4.get('kind'), 'from_previous': r4.get('from_previous'),
                       'from_this': r4.get('from_this'), 'v4_label': r4.get('old')}
            else:
                dd = (j or {}).get('dependency') or {}
                need = dd.get('needs_previous')
                rec = {'step': s['step'], 'output': s['output'],
                       'input_from_previous': prev['output'],
                       'dependency': 'real' if need else ('none' if need is False else 'unjudged'),
                       'why': dd.get('why')}
            tally[rec['dependency']] += 1
            dep.append(rec)
        e = os.path.join(d, 'writer', 'endtoend.out.txt')
        t['end_to_end'] = parse(open(e).read()) if os.path.exists(e) else None
        json.dump(t, open(f, 'w'), indent=1)
        json.dump({'trace': t['trace'], 'steps': dep,
                   'note': 'Every verdict is model against model.'},
                  open(os.path.join(d, 'dependency.json'), 'w'), indent=1)
    print(f"dependency across {sum(tally.values())} steps: {dict(tally)}")
    linked = sum(v for k, v in tally.items() if k != 'first step')
    none = tally['none']
    print(f"\nSTOP RULE -- steps with a predecessor: {linked}; marked none: {none} "
          f"({none/linked:.0%} of them)" if linked else "")
    print("  FIRED" if linked and none > linked / 2 else "  not fired")


if __name__ == '__main__': {'prompts': prompts, 'collect': collect}[sys.argv[1]]()
