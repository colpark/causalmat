"""score.py: grade a case's arms per step and for the closing profile.

  python3 trace_kit_v2/score.py <case_dir>

No model call: the four-level scale is a closed set, so grading is exact-match against the chain's
own ground truth. Writes gate.json beside case.json.
"""
import json, os, re, sys
LEVELS = ('shown', 'partial', 'not addressed', 'contradicts')


def parse(txt):
    if not txt: return None
    m = re.search(r'\{.*\}', txt, re.S)
    if not m: return None
    try: return json.loads(m.group(0))
    except Exception: return None


def norm(x):
    s = (x or '').strip().lower().replace('_', ' ')
    return s if s in LEVELS else ('not addressed' if 'not' in s and 'address' in s else s)


def main(case_dir):
    ch = json.load(open(os.path.join(case_dir, 'case.json')))
    truth = {s['step']: s['expected_support'] for s in ch['steps']}
    gd = os.path.join(case_dir, 'gate')
    arms = {}
    for f in sorted(os.listdir(gd)):
        if not f.endswith('.out.txt'): continue
        arm = f[:-8]
        r = parse(open(os.path.join(gd, f)).read())
        if not r: arms[arm] = {'parsed': False}; continue
        got = {int(s.get('step', i + 1)): norm(s.get('level')) for i, s in enumerate(r.get('steps') or [])}
        per = {k: {'expected': v, 'got': got.get(k), 'correct': got.get(k) == v} for k, v in truth.items()}
        close_got = norm((r.get('closing') or {}).get('level'))
        arms[arm] = {'parsed': True, 'steps': per,
                     'steps_correct': sum(1 for p in per.values() if p['correct']), 'n_steps': len(truth),
                     'closing_expected': ch['closing_support'], 'closing_got': close_got,
                     'closing_correct': close_got == ch['closing_support'],
                     'missing_said': (r.get('closing') or {}).get('missing', '')[:400]}
    out = {'case': ch['case'], 'paper': ch['paper'], 'claim': ch['claim'],
           'truth': {'steps': truth, 'closing': ch['closing_support']}, 'arms': arms,
           'item_valid': bool(arms.get('full', {}).get('closing_correct')
                              and not arms.get('floor', {}).get('closing_correct')
                              and arms.get('full', {}).get('steps_correct', 0)
                              > arms.get('floor', {}).get('steps_correct', 0)),
           # the closing label is a four-level guess: "partial" is cheap to land. Per-step is the
           # discriminating signal, so record separately whether the text-only arms kept up.
           'closing_alone_discriminates': bool(arms.get('full', {}).get('closing_correct')
                                               and not arms.get('oracle_complete', {}).get('closing_correct')
                                               and not arms.get('no_image', {}).get('closing_correct')),
           'oracle_carries_the_task': bool(arms.get('oracle_complete', {}).get('steps_correct', 0)
                                           >= arms.get('full', {}).get('steps_correct', 0)
                                           and arms.get('oracle_complete', {}).get('closing_correct')),
           'note': 'Every verdict is model against model. The four-level ground truth is itself a model label.'}
    json.dump(out, open(os.path.join(case_dir, 'gate.json'), 'w'), indent=1)
    print(f"{ch['case']}  truth steps={list(truth.values())} closing={ch['closing_support']}")
    for a, v in arms.items():
        if not v['parsed']: print(f"   {a:16s} UNPARSED"); continue
        got = [v['steps'][k]['got'] for k in sorted(v['steps'])]
        print(f"   {a:16s} steps {v['steps_correct']}/{v['n_steps']}  {got}  closing={v['closing_got']} "
              f"{'OK' if v['closing_correct'] else 'x'}")
    print(f"   item_valid={out['item_valid']}  closing_alone_discriminates={out['closing_alone_discriminates']}"
          f"  oracle_carries={out['oracle_carries_the_task']}")
    return out


if __name__ == '__main__': main(sys.argv[1])
