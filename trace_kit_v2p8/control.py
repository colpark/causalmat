"""control.py: v2.8b -- the same-question control, plus an arm with no evidence at all.

  python3 -m trace_kit_v2p8.control build     the 4 new arms
  python3 -m trace_kit_v2p8.control grade     grading prompts, v2.8's grader unchanged
  python3 -m trace_kit_v2p8.control collect   scores, the strict decision, split halves

v2.8 gave only arm B the full combined question. Arms A and C were asked narrower questions
matching what they held, which they had to be to be answerable at all, but it means their near
zero scores on combined claims were partly a property of the question rather than of the
evidence. This run removes that asymmetry and adds the control that matters most:

  A_full     the measurement and its panels, asked arm B's question word for word
  C_full     the earlier result and the panels ITS OWN upstream item used, same full question
  N          the full question and nothing else. No measurement, no earlier result, no panels
  B_narrow   arm B's full evidence, asked arm A's narrower question

Where an arm lacks a section, the section is present and says "not provided", so every arm sees
the same document shape and the same question text. An arm that scores well because it was asked
an easier question is an artefact; an arm that scores well with the section blanked is not.

Arm N is the one that could invalidate everything upstream of it. These are published papers.
If a model reaches the key's combined claims from the question alone, the claim was never
evidence of composition, it was evidence of memorisation.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402
from trace_kit_v2p6.clean import clean  # noqa: E402
from trace_kit_v2p8.partB import topic_of, Q_A, TAIL  # noqa: E402
from trace_kit_v2p8.partC import ASK  # noqa: E402

OUT = R('results/v2p8/control/arms')
GRADE = R('results/v2p8/control/grade')
V8ARMS = R('results/v2p8/arms')
SAMPLES = 6
NEW = ('A_full', 'C_full', 'N', 'B_narrow')
NP = '  not provided'

BODY = """{q}

What the measurement says:

{obs}

Figure panels{panhow}
{pans}
{caps}
What an earlier step already established, which you may treat as settled:

{inp}
{lims}

{tail}"""


def items():
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    DI = {x['item']: x for x in json.load(open(R('results/v2p7/derived_input.json')))['items_out']}
    D5 = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    return [(s, DI[s['item']], D5[s['upstream']]) for s in S]


def panel_block(pans):
    if not pans:
        return ('.', NP, '\n')
    lines = '\n'.join(f"  {p['suffix']}   {os.path.realpath(p['crop'])}"
                      for p in pans if p.get('crop') and os.path.exists(p['crop']))
    caps = [f"  {p['suffix']}: {p['caption_span'].strip()}"
            for p in pans if p.get('caption_span')]
    cap = ('\nPanel captions as printed:\n' + '\n'.join(caps) + '\n') if caps else '\n'
    return ('. Open every one of these with the Read tool before you answer:', lines, cap)


def build():
    os.makedirs(OUT, exist_ok=True)
    jobs = []
    for s, x, up in items():
        q_full = x['question']
        q_narrow = Q_A.format(topic=topic_of(q_full))
        obs = '  ' + x['new_observation']['text']
        inp = x['input_result']
        lims = ('\nThe qualifications recorded on that earlier result:\n'
                + '\n'.join('  - ' + t for t in x['input_limits'])) if x['input_limits'] \
            else '\nNo qualifications were recorded on that earlier result.'
        own = [p for p in x['panels'] if p.get('crop') and os.path.exists(p['crop'])]
        ups = [p for p in (up.get('panels') or []) if p.get('crop') and os.path.exists(p['crop'])]

        spec = {
            # the measurement and its panels; the earlier result blanked
            'A_full': dict(q=q_full, obs=obs, pans=own, inp=NP, lims=''),
            # the earlier result and the panels its OWN upstream item read; measurement blanked
            'C_full': dict(q=q_full, obs=NP, pans=ups, inp=inp, lims=lims),
            # nothing but the question
            'N': dict(q=q_full, obs=NP, pans=[], inp=NP, lims=''),
            # arm B's evidence, arm A's narrower question
            'B_narrow': dict(q=q_narrow, obs=obs, pans=own, inp=inp, lims=lims),
        }
        for arm, v in spec.items():
            how, plines, caps = panel_block(v['pans'])
            body = BODY.format(q=v['q'], obs=v['obs'], panhow=how, pans=plines, caps=caps,
                               inp=v['inp'], lims=v['lims'], tail=TAIL)
            f = os.path.join(OUT, f"{x['item']}_{arm}.txt")
            open(f, 'w').write(body)
            ag = 'net-floor' if not v['pans'] else 'net-fullarm'
            for k in range(1, SAMPLES + 1):
                jobs.append({'id': f"{x['item']}_{arm}{k}", 'agent': ag, 'prompt': f,
                             'out': os.path.join(OUT, f"{x['item']}_{arm}{k}.out.txt")})
    json.dump(jobs, open(R('results/v2p8/control/arm_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} answers from {len({j["prompt"] for j in jobs})} prompts '
          f'(8 items x {len(NEW)} arms x {SAMPLES} samples)')
    return jobs


def grade():
    os.makedirs(GRADE, exist_ok=True)
    index = json.load(open(R('results/v2p8/claim_index.json')))
    jobs, miss = [], []
    for s, x, up in items():
        it = x['item']
        listing = '\n'.join(f"{i}. {c['claim']}" for i, c in enumerate(index[it], 1))
        for arm in NEW:
            for k in range(1, SAMPLES + 1):
                fa = os.path.join(OUT, f'{it}_{arm}{k}.out.txt')
                if not os.path.exists(fa): miss.append(f'{it}_{arm}{k}'); continue
                body = ASK.format(answer=clean(open(fa).read()), claims=listing)
                f = os.path.join(GRADE, f'{it}_{arm}{k}.txt'); open(f, 'w').write(body)
                jobs.append({'id': f'{it}_{arm}{k}', 'agent': 'net-grader', 'prompt': f,
                             'out': os.path.join(GRADE, f'{it}_{arm}{k}.out.txt')})
    json.dump(jobs, open(R('results/v2p8/control/grade_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} gradings, {len(miss)} answers missing: {miss[:6]}')
    return jobs


def score_one(f, cs):
    o = obj(open(f).read(), 'rulings') if os.path.exists(f) else None
    if not o: return None
    rul = {int(r['n']): r for r in o.get('rulings', [])
           if str(r.get('n', '')).strip().isdigit()}
    nc = sum(1 for c in cs if c['kind'] == 'combined')
    nl = sum(1 for c in cs if c['kind'] == 'limit')
    cs_, ls_, con, rows = 0, 0, 0, []
    for i, c in enumerate(cs, 1):
        r = rul.get(i) or {}
        v = (r.get('verdict') or '').strip().lower()
        q = (r.get('quote') or '').strip()
        if v == 'stated' and not q: v = 'absent'
        if v == 'stated':
            if c['kind'] == 'combined': cs_ += 1
            else: ls_ += 1
        elif v == 'contradicted': con += 1
        rows.append({'n': i, 'kind': c['kind'], 'claim': c['claim'],
                     'verdict': v or 'absent', 'quote': q[:300]})
    return {'combined_score': round(cs_ / nc, 4) if nc else None,
            'limit_score': round(ls_ / nl, 4) if nl else None,
            'contradictions': con, 'rulings': rows}


def collect():
    import statistics as st
    index = json.load(open(R('results/v2p8/claim_index.json')))
    V8 = json.load(open(R('results/v2p8/partC.json')))['answers']
    D8 = json.load(open(R('results/v2p8/partD.json')))['items_out']
    per, out, unparsed = {}, {}, []
    for s, x, up in items():
        it = x['item']; cs = index[it]
        arms = {}
        for arm in ('A', 'B', 'C'):           # reused from v2.8, unchanged
            arms[arm] = [V8[f'{it}_{arm}{k}'] for k in range(1, SAMPLES + 1)
                         if f'{it}_{arm}{k}' in V8]
        for arm in NEW:
            got = []
            for k in range(1, SAMPLES + 1):
                r = score_one(os.path.join(GRADE, f'{it}_{arm}{k}.out.txt'), cs)
                if r is None: unparsed.append(f'{it}_{arm}{k}')
                else: got.append(r)
            arms[arm] = got
            for k, r in enumerate(got, 1): per[f'{it}_{arm}{k}'] = {**r, 'item': it, 'arm': arm}
        if any(len(v) < SAMPLES for v in arms.values()):
            out[it] = {'error': 'incomplete', 'have': {a: len(v) for a, v in arms.items()}}
            continue
        m = {a: round(st.mean([r['combined_score'] for r in v]), 4) for a, v in arms.items()}
        ml = {a: (round(st.mean([r['limit_score'] for r in v if r['limit_score'] is not None]), 4)
                  if any(r['limit_score'] is not None for r in v) else None)
              for a, v in arms.items()}
        con = {a: round(st.mean([r['contradictions'] for r in v]), 3) for a, v in arms.items()}

        def dec(mm):
            return (mm['B'] - mm['A_full'] >= 0.25, mm['B'] - mm['C_full'] >= 0.25,
                    mm['N'] < 0.25)
        bA, bC, nlow = dec(m)
        halves = {}
        for name, sl in (('first', slice(0, 3)), ('second', slice(3, 6))):
            hm = {a: round(st.mean([r['combined_score'] for r in arms[a][sl]]), 4) for a in arms}
            h = dec(hm)
            halves[name] = {'means': hm, 'beats_A_full': h[0], 'beats_C_full': h[1],
                            'N_below': h[2], 'compositional': all(h)}
        out[it] = {
            'paper': s['paper'], 'journal': s['journal'], 'cs': s['cs'],
            'upstream': s['upstream'], 'up_gen': s['up_gen'],
            'n_combined': D8[it]['n_combined'], 'n_limit': D8[it]['n_limit'],
            'mean_combined': m, 'mean_limit': ml, 'mean_contradictions': con,
            'B_minus_A_full': round(m['B'] - m['A_full'], 4),
            'B_minus_C_full': round(m['B'] - m['C_full'], 4),
            'beats_A_full': bA, 'beats_C_full': bC, 'N_below_threshold': nlow,
            'strictly_compositional': bool(bA and bC and nlow),
            'v2p8_compositional': D8[it]['compositional'],
            'B_narrow_reaches': bool(m['B_narrow'] >= 0.5),
            'halves': halves,
            'halves_agree': halves['first']['compositional'] == halves['second']['compositional'],
        }
    good = [v for v in out.values() if 'error' not in v]
    nfail = [k for k, v in out.items() if 'error' not in v and not v['N_below_threshold']]
    res = {
        'note': 'v2.8b. Same full question for every arm, plus an evidence-free arm N.',
        'items': len(good),
        'mean_combined_across_items': {
            a: round(st.mean([v['mean_combined'][a] for v in good]), 4)
            for a in ('A', 'B', 'C', 'A_full', 'C_full', 'N', 'B_narrow')},
        'mean_limit_across_items': {
            a: round(st.mean([v['mean_limit'][a] for v in good
                              if v['mean_limit'][a] is not None]), 4)
            for a in ('A', 'B', 'C', 'A_full', 'C_full', 'N', 'B_narrow')},
        'strictly_compositional': sum(1 for v in good if v['strictly_compositional']),
        'v2p8_compositional': sum(1 for v in good if v['v2p8_compositional']),
        'dropped_out': sorted(k for k, v in out.items()
                              if 'error' not in v and v['v2p8_compositional']
                              and not v['strictly_compositional']),
        'beats_A_full': sum(1 for v in good if v['beats_A_full']),
        'beats_C_full': sum(1 for v in good if v['beats_C_full']),
        'N_at_or_above_threshold': len(nfail), 'N_items': sorted(nfail),
        'B_narrow_reaches': sum(1 for v in good if v['B_narrow_reaches']),
        'halves_agree': sum(1 for v in good if v['halves_agree']),
        'unparsed': unparsed,
        'stop_halves': bool(sum(1 for v in good if v['halves_agree']) < 6),
        'stop_memorisation': bool(len(nfail) >= 3),
        'items_out': out, 'answers': per,
    }
    json.dump(res, open(R('results/v2p8/control/control.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items()
                      if k not in ('items_out', 'answers')}, indent=1))
    return res


if __name__ == '__main__':
    {'build': build, 'grade': grade, 'collect': collect}[sys.argv[1]]()
