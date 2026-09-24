"""qkind.py: does a key's proposition compare quantities of different kinds?

  python3 trace_kit_v5/qkind.py prompts
  python3 trace_kit_v5/qkind.py collect

The per-statement audit rules whether each STATED limit is true. It never asks whether a NEEDED
limit is missing, so a key can pass every statement and still compare two things that are not
comparable. Nano Letters is the case that exposed it: the auditor correctly struck an unsupported
Na-specific mechanism, and its own replacement then compared Li CHARGE capacity against Na DISCHARGE
capacity. Nothing in the audit could catch that, because no statement in the key was false.

This is one extra question per key, asked of all 29, and it is the first measure of what the
per-statement audit cannot see.

Every verdict is model against model.
"""
import json, os, re, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

ASK = """Does this proposition compare quantities of DIFFERENT KINDS?

A comparison is only meaningful between quantities of the same kind. Mismatches to look for:

  charge capacity against discharge capacity
  a rate against an accumulated or cumulative amount
  a test temperature against a service temperature
  a yield stress against a fracture stress or a flow stress
  an instantaneous value against a time-averaged one
  a normalized value against an absolute one
  a value at one cycle, time or condition against a value at a different one

Rule `same_kind` or `mixed`. If mixed, quote BOTH quantities exactly as the proposition or the
observations state them, name the kind of each, and say whether the observations contain a
same-kind pair that could be used instead. If they do not, say so -- the correct repair is then to
state the mismatch as a limit rather than to swap in numbers that are not there.

Reply as JSON only:
{"ruling": "same_kind" or "mixed",
 "quantity_a": "...", "kind_a": "...", "quantity_b": "...", "kind_b": "...",
 "same_kind_pair_available": true or false,
 "fix": "corrected proposition" or null,
 "limit_to_add": "..." or null}"""


def prompts():
    I = {i['item']: i for i in json.load(open(os.path.join(ROOT, 'results/v5/items.json')))['items']}
    S = [r['item'] for r in json.load(open(os.path.join(ROOT, 'results/v5/survival_v5b.json')))['surviving']]
    d = os.path.join(ROOT, 'results/v5/qkind'); os.makedirs(d, exist_ok=True)
    jobs = []
    for s in S:
        it = I[s]; k = it['key']
        L = [f"Property under test: {it['property']}", ""]
        if it['previous_output']:
            L += [f"Previous step established: {it['previous_output']}", ""]
        L.append(f"Observations ({it['technique']}):")
        for n, o in enumerate(it['observations'], 1): L.append(f"  [obs{n}] {o}")
        L += ["", f"Proposition under test: {k.get('proposition')}", "", ASK]
        f = os.path.join(d, s + '.txt'); open(f, 'w').write("\n".join(L))
        jobs.append({'id': s, 'agent': 'net-judge', 'prompt': os.path.abspath(f),
                     'out': os.path.abspath(os.path.join(d, s + '.out.txt'))})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v5qkind.json'), 'w'), indent=1)
    print(f"{len(jobs)} quantity-kind checks (all surviving items)")


def _obj(t):
    out, depth, start = [], 0, None
    for i, c in enumerate(t or ''):
        if c == '{':
            if depth == 0: start = i
            depth += 1
        elif c == '}' and depth:
            depth -= 1
            if not depth: out.append(t[start:i + 1])
    for o in sorted(out, key=len, reverse=True):
        for cand in (o, re.sub(r',(\s*[}\]])', r'\1', o)):
            try:
                j = json.loads(cand)
                if 'ruling' in j: return j
            except Exception: continue
    return None


def collect():
    D = json.load(open(os.path.join(ROOT, 'results/v5/items.json')))
    I = {i['item']: i for i in D['items']}
    jobs = json.load(open(os.path.join(ROOT, '.v07work/batch_v5qkind.json')))
    tally = collections.Counter(); fixed = []
    for j in jobs:
        r = _obj(open(j['out']).read()) if os.path.exists(j['out']) else None
        if not r: tally['unparsed'] += 1; continue
        it = I[j['id']]; k = it['key']
        rule = 'mixed' if str(r.get('ruling', '')).lower().startswith('mix') else 'same_kind'
        tally[rule] += 1
        it['quantity_kind'] = {'ruling': rule, 'a': r.get('quantity_a'), 'kind_a': r.get('kind_a'),
                               'b': r.get('quantity_b'), 'kind_b': r.get('kind_b'),
                               'same_kind_pair_available': r.get('same_kind_pair_available')}
        if rule == 'mixed':
            if r.get('fix'):
                k.setdefault('proposition_before_quantity_fix', k['proposition'])
                k['proposition'] = r['fix']
            if r.get('limit_to_add'):
                k.setdefault('limits', []).append(r['limit_to_add'])
            k['scoring']['required_elements'] = [k['proposition']] + list(k.get('limits') or [])
            k['scoring']['n_required'] = len(k['scoring']['required_elements'])
            fixed.append((j['id'], r.get('kind_a'), r.get('kind_b'),
                          bool(r.get('same_kind_pair_available'))))
    json.dump(D, open(os.path.join(ROOT, 'results/v5/items.json'), 'w'), indent=1)
    n = tally['same_kind'] + tally['mixed']
    print(f"{n} keys ruled: {tally['same_kind']} same_kind, {tally['mixed']} mixed"
          + (f", {tally['unparsed']} unparsed" if tally['unparsed'] else ''))
    if n: print(f"mixed rate: {tally['mixed']}/{n} = {tally['mixed']/n:.0%}")
    for a, ka, kb, avail in fixed:
        print(f"   {a:34s} {str(ka)[:26]:26s} vs {str(kb)[:26]:26s} "
              f"{'same-kind pair available' if avail else 'NO same-kind pair -- stated as a limit'}")


if __name__ == '__main__': {'prompts': prompts, 'collect': collect}[sys.argv[1]]()
