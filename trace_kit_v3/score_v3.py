"""score_v3.py: read the arm replies and compare them, per step and at the close.

  python3 trace_kit_v3/score_v3.py

Levels, strongest first: warrants > partly warrants > does not address > contradicts.
A prose reply is parsed as a fallback so a non-JSON answer is not silently dropped -- that mistake
cost v2 eighteen replies.

What the arms are for:
  full vs floor            does seeing the panel change the ruling, or do the captions carry it?
  full vs oracle_complete  does the picture add anything over the measurement in words?
  full vs reordered        does the paper's step order carry information?
  full vs permute_image    a chain judged on the wrong pictures should not score like the right ones

Every verdict is model against model.
"""
import json, os, re, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARMS = ['full', 'floor', 'oracle_complete', 'reordered', 'permute_image']
RANK = {'warrants': 3, 'partly warrants': 2, 'does not address': 1, 'contradicts': 0}


# Order matters and is the whole point: "warrants" is a substring of "partly warrants", and
# "warranted" of "partly warranted", so a bare warrant test MUST come last. Testing it first scored
# every partial ruling as a full one and silently inflated the arms.
PATTERNS = [('does not address', ('does not address', 'not addressed', 'does not adress',
                                  'unaddressed', 'not warranted', 'unwarranted', 'not supported')),
            ('contradicts',      ('contradict',)),
            ('partly warrants',  ('partly', 'partial')),
            ('warrants',         ('warrant',))]


def norm(s, seen=None):
    s = (s or '').strip().lower().rstrip('.')
    if not s: return None
    for level, pats in PATTERNS:
        for pat in pats:
            if pat in s:
                if seen is not None and s != level: seen.append((s, level))
                return level
    return None


def answered(txt):
    """did the agent actually answer? a reply with no JSON and no level is a failed job, not a '?'"""
    t = (txt or '').strip()
    if not t: return False
    if re.search(r'\{.*\}', t, re.S): return True
    return bool(norm(t) or re.search(r'step\s*\d', t, re.I))


def parse(txt, nsteps):
    """JSON first; then prose, looking for a level near each step number"""
    m = re.search(r'\{.*\}', txt or '', re.S)
    if m:
        try:
            j = json.loads(m.group(0))
            st = {int(s['step']): norm(s.get('level')) for s in j.get('steps', []) if s.get('step')}
            cl = norm((j.get('closing') or {}).get('level'))
            if st: return st, cl, 'json'
        except Exception: pass
    st = {}
    for i in range(1, nsteps + 1):
        m = re.search(rf'step\s*{i}\b[^\n]*', txt or '', re.I)
        if m: st[i] = norm(m.group(0))
    cl = None
    m = re.search(r'(closing|overall|as a whole)[^\n]*', txt or '', re.I)
    if m: cl = norm(m.group(0))
    return st, cl, 'prose'


def main():
    rows = []
    for cj in sorted(glob.glob(os.path.join(ROOT, 'results/v3/traces/*/case.json'))):
        ch = json.load(open(cj)); d = os.path.dirname(cj)
        ns = len(ch['steps'])
        rec = {'case': ch['case'], 'paper': ch['paper'], 'chain': ch['chain'], 'n_steps': ns,
               'arms': {}}
        for a in ARMS:
            f = os.path.join(d, 'gate', f'{a}.out.txt')
            if not os.path.exists(f): continue
            st, cl, how = parse(open(f).read(), ns)
            rec['arms'][a] = {'steps': st, 'closing': cl, 'parsed': how}
        rows.append(rec)
    json.dump({'cases': rows, 'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v3/gate_scores.json'), 'w'), indent=1)

    print(f"{'case':24s} " + ' '.join(f'{a[:9]:>9s}' for a in ARMS) + "   (closing)")
    for r in rows:
        cells = []
        for a in ARMS:
            v = r['arms'].get(a, {})
            cells.append((v.get('closing') or '-')[:9])
        print(f"{r['case'][:24]:24s} " + ' '.join(f'{c:>9s}' for c in cells))

    print("\nper-step levels")
    for r in rows:
        print(f"  {r['case']}  ({'->'.join(r['chain'])})")
        for i in range(1, r['n_steps'] + 1):
            cells = [(r['arms'].get(a, {}).get('steps', {}).get(i) or '-')[:16] for a in ARMS]
            print(f"    step {i}: " + '  '.join(f'{c:16s}' for c in cells))

    print("\ndeltas against full (mean rank over steps; + means the arm scored higher)")
    agg = collections.defaultdict(list)
    for r in rows:
        f = r['arms'].get('full', {}).get('steps', {})
        if not f: continue
        base = [RANK.get(f.get(i)) for i in range(1, r['n_steps'] + 1)]
        for a in ARMS[1:]:
            o = r['arms'].get(a, {}).get('steps', {})
            pairs = [(RANK.get(o.get(i)), b) for i, b in zip(range(1, r['n_steps'] + 1), base)
                     if o.get(i) is not None and b is not None]
            if pairs: agg[a].append(sum(x - y for x, y in pairs) / len(pairs))
    for a in ARMS[1:]:
        v = agg.get(a, [])
        if v: print(f"  {a:16s} {sum(v)/len(v):+.2f}  over {len(v)} cases")
    print("\nmajority-class baseline: the share of an arm's step rulings taking its single most")
    print("common level. An arm that says one thing everywhere scores 100% and carries no signal.")
    for a in ARMS:
        lv = [r['arms'].get(a, {}).get('steps', {}).get(i)
              for r in rows for i in range(1, r['n_steps'] + 1)]
        lv = [x for x in lv if x]
        if not lv: continue
        c = collections.Counter(lv); top, n = c.most_common(1)[0]
        print(f"  {a:16s} {n}/{len(lv)} = {n/len(lv):.0%} are '{top}'   {dict(c)}")
    parsed = collections.Counter(v['parsed'] for r in rows for v in r['arms'].values())
    print(f"\nreplies parsed: {dict(parsed)}")


if __name__ == '__main__': main()
