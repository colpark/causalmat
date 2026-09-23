"""score.py: grade a case's arms per step and for the closing profile.

  python3 trace_kit_v2/score.py <case_dir>

No model call: the four-level scale is a closed set, so grading is exact-match against the chain's
own ground truth. Writes gate.json beside case.json.
"""
import collections, json, os, re, sys
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


def disputes(ch, arms):
    """finding C: where the full arm disagrees with image_support AND gives a reason, the step goes to
    the review queue. It is still scored as the graph says; the file is what a human would audit."""
    full = arms.get('full') or {}
    if not full.get('parsed'): return []
    by_step = {s['step']: s for s in ch['steps']}
    out = []
    for k, p in (full.get('steps') or {}).items():
        if p['correct'] or not p['got']: continue
        st = by_step.get(k) or {}
        why = (full.get('_why') or {}).get(k, '')
        if len(why.strip()) < 25: continue          # a bare label is not a reasoned disagreement
        out.append({'case': ch['case'], 'paper': ch['paper'], 'claim': ch['claim'],
                    'step': k, 'node': st.get('node'), 'technique': st.get('technique'),
                    'panel_ids': [x['panel_id'] for x in st.get('panels', [])],
                    'graph_label': p['expected'], 'arm_label': p['got'], 'arm_reason': why,
                    'graph_observation': st.get('observation'),
                    'note': 'scored as the graph says; queued for human review'})
    return out


def main(case_dir):
    ch = json.load(open(os.path.join(case_dir, 'case.json')))
    truth = {s['step']: s['expected_support'] for s in ch['steps']}
    # a constant-answer baseline: with a skewed target, an arm that never looks still scores. Report it
    # beside every arm so the comparison cannot be read as skill when it is the class prior.
    _tv = list(truth.values())
    _maj = collections.Counter(_tv).most_common(1)[0] if _tv else (None, 0)
    out_majority = {'answer': _maj[0], 'steps_correct': _maj[1], 'n_steps': len(_tv),
                    'rate': round(_maj[1] / len(_tv), 3) if _tv else None}
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
                     '_why': {int(x.get('step', i + 1)): (x.get('why') or '') for i, x in enumerate(r.get('steps') or [])},
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
           'majority_class_baseline': out_majority,
           'note': 'Every verdict is model against model. The four-level ground truth is itself a model label.'}
    # control: permute the answer key across cases. No dispatch -- the full arm's real reply is scored
    # against another case's expected levels, which must be wrong.
    import glob as _g
    other = None
    for f in sorted(_g.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'results/v2/cases/*/*/case.json'))):
        o = json.load(open(f))
        if o['case'] != ch['case']: other = o; break
    full = arms.get('full') or {}
    if other and full.get('parsed'):
        okeys = {s2['step']: s2['expected_support'] for s2 in other['steps']}
        got = {k: v['got'] for k, v in full['steps'].items()}
        n = sum(1 for k in got if k in okeys)
        arms['permute_answer'] = {'parsed': True, 'permuted_from': other['case'],
            'steps_correct': sum(1 for k, v in got.items() if k in okeys and v == okeys[k]),
            'n_steps': n, 'closing_expected': other['closing_support'],
            'closing_got': full.get('closing_got'),
            'closing_correct': full.get('closing_got') == other['closing_support'],
            'steps': {k: {'expected': okeys.get(k), 'got': v, 'correct': v == okeys.get(k)} for k, v in got.items() if k in okeys}}

    dsp = disputes(ch, arms)
    out['gt_disputes'] = len(dsp)
    if dsp:
        q = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'results/v2/gt_disputes.jsonl')
        seen = set()
        if os.path.exists(q):
            seen = {(json.loads(l)['case'], json.loads(l)['step']) for l in open(q) if l.strip()}
        with open(q, 'a') as f:
            for d in dsp:
                if (d['case'], d['step']) not in seen: f.write(json.dumps(d) + '\n')
    for a in arms.values(): a.pop('_why', None)
    json.dump(out, open(os.path.join(case_dir, 'gate.json'), 'w'), indent=1)
    print(f"{ch['case']}  truth steps={list(truth.values())} closing={ch['closing_support']}")
    for a, v in arms.items():
        if not v['parsed']: print(f"   {a:16s} UNPARSED"); continue
        got = [v['steps'][k]['got'] for k in sorted(v['steps'])]
        print(f"   {a:16s} steps {v['steps_correct']}/{v['n_steps']}  {got}  closing={v['closing_got']} "
              f"{'OK' if v['closing_correct'] else 'x'}")
    print(f"   majority-class baseline: always '{out_majority['answer']}' scores {out_majority['steps_correct']}/{out_majority['n_steps']}")
    print(f"   item_valid={out['item_valid']}  closing_alone_discriminates={out['closing_alone_discriminates']}"
          f"  oracle_carries={out['oracle_carries_the_task']}  gt_disputes={out['gt_disputes']}")
    return out


if __name__ == '__main__': main(sys.argv[1])
