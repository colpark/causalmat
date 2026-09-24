"""necessity.py: v2.6 step 5 -- does the upstream result change the last step's answer?

  python3 -m trace_kit_v2p6.necessity arms       write arm A and arm B prompts, 3 repeats each
  python3 -m trace_kit_v2p6.necessity compare    write the comparison prompts from the replies
  python3 -m trace_kit_v2p6.necessity collect    majority over the repeats -> results/v2p6/necessity.json

A merge earns the name only if the earlier result does work. So: answer the last item of the
chain twice. Arm A gets the item's question and its own evidence, panels included. Arm B gets
exactly that plus the upstream item's key proposition and limits, handed over as a settled
earlier result. A second agent reads both answers and rules whether the conclusion the evidence
is said to justify, or the uncertainty left around it, actually changed.

Three repeats of each arm, paired A1-B1, A2-B2, A3-B3, majority of three. The repeats are also
the noise measurement: if the three rulings disagree often, the check cannot be filtered on and
the run stops instead of pretending.

The upstream is the item immediately before the last one. For 6 of the 82 chains -- depth-2
chains that dedup left with more than one opener -- that predecessor is the opener and so varies
by variant; those run on the canonical opener and the alternatives are recorded.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402

ARM = R('results/v2p6/arms')
CMP = R('results/v2p6/compare')
REPEATS = 3


def items():
    D = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    V5 = {i['item']: i for i in json.load(open(R('results/v5/items.json')))['items']}
    return D, {**V5, **D}


def evidence_block(it):
    obs = []
    for k, lab in (('observation_a', 'A'), ('observation_b', 'B')):
        o = it.get(k)
        if o and o.get('text'):
            t = o['text'].strip()
            if o.get('technique'): t += f"   [{o['technique']}]"
            obs.append(f'  {lab}. {t}')
    for o in (it.get('observations') or []):
        if isinstance(o, dict) and o.get('text'):
            t = o['text'].strip()
            if o.get('technique'): t += f"   [{o['technique']}]"
            obs.append(f'  {chr(65 + len(obs))}. {t}')
    pans, caps = [], []
    for p in (it.get('panels') or []):
        f = p.get('crop') or p.get('figure')
        if not (f and os.path.exists(f)): continue
        pans.append(f'  {p.get("suffix") or "panel"}   {os.path.realpath(f)}')
        if p.get('caption_span'): caps.append(f'  {p.get("suffix") or "panel"}: {p["caption_span"].strip()}')
    s = 'What the measurements say:\n\n' + '\n'.join(obs)
    if pans:
        s += ('\n\nFigure panels. Open every one of these with the Read tool before you answer:\n'
              + '\n'.join(pans))
    if caps: s += '\n\nPanel captions as printed:\n' + '\n'.join(caps)
    return s


def question_of(it):
    return (it.get('question') or it.get('property') or '').strip()


TAIL = """Answer in prose, at most 200 words. Say what conclusion this evidence justifies, and say plainly what it leaves uncertain. Claim nothing the evidence does not carry."""

ARM_A = """{q}

{ev}

{tail}"""

ARM_B = """{q}

{ev}

An earlier step in this work already established the following, and you may treat it as settled:

{prop}
{lims}

{tail}"""

COMPARE = """Two answers to the same question about one set of measurements. Both answerers saw the same evidence. The second was additionally handed an earlier established result; the first was not.

THE QUESTION
{q}

ANSWER 1 -- evidence only
{a}

ANSWER 2 -- the same evidence, plus the earlier result
{b}

Did the earlier result do any work?

Rule "yes" only if ANSWER 2 states a different conclusion as justified by the evidence, or leaves a materially different uncertainty, than ANSWER 1 does.

Rule "no" if ANSWER 2 reaches the same conclusion with the same uncertainty -- including when it is worded differently, is longer, restates the earlier result, cites it as consistent or corroborating, or uses it only as background. Repeating a result is not using it.

Return JSON and nothing else:
{{"changed": "yes" | "no",
 "what_changed": "conclusion" | "uncertainty" | "both" | "nothing",
 "why": "at most 50 words, quoting the words in ANSWER 1 and ANSWER 2 that decide it"}}"""


def chain_rows():
    P = json.load(open(R('results/v2p6/pruned.json')))
    D, ALL = items()
    rows = []
    for c in P['chains']:
        fin, up = c['path'][-1], c['path'][-2]
        f_it, u_it = ALL[fin], ALL[up]
        q = question_of(f_it)
        k = (u_it.get('key') or {})
        prop = (k.get('proposition') or '').strip()
        if not q or not prop: continue
        lims = [str(x).strip() for x in (k.get('limits') or []) if str(x).strip()]
        rows.append({'chain': c['chain'], 'paper': c['paper'], 'depth': c['depth'],
                     'final': fin, 'upstream': up, 'path': c['path'],
                     'openers': c['openers'],
                     'predecessor_varies': c['depth'] == 2 and len(c['openers']) > 1,
                     'q': q, 'ev': evidence_block(f_it), 'prop': prop, 'lims': lims})
    return rows


def arms():
    os.makedirs(ARM, exist_ok=True)
    rows, jobs = chain_rows(), []
    for r in rows:
        a = ARM_A.format(q=r['q'], ev=r['ev'], tail=TAIL)
        lims = ('\nThe qualifications recorded on that earlier result:\n'
                + '\n'.join('  - ' + x for x in r['lims'])) if r['lims'] else \
               '\nNo qualifications were recorded on that earlier result.'
        b = ARM_B.format(q=r['q'], ev=r['ev'], prop=r['prop'], lims=lims, tail=TAIL)
        for arm, body in (('A', a), ('B', b)):
            f = os.path.join(ARM, f"{r['chain']}_{arm}.txt")
            open(f, 'w').write(body)
            for k in range(1, REPEATS + 1):
                jobs.append({'id': f"{r['chain']}_{arm}{k}", 'agent': 'net-fullarm',
                             'prompt': f, 'out': os.path.join(ARM, f"{r['chain']}_{arm}{k}.out.txt")})
    json.dump(rows, open(R('results/v2p6/necessity_rows.json'), 'w'), indent=1)
    json.dump(jobs, open(R('results/v2p6/arm_jobs.json'), 'w'), indent=1)
    print(f'{len(rows)} chains, {len(jobs)} arm calls '
          f'({len(rows)} x 2 arms x {REPEATS} repeats)')
    return jobs


def compare():
    os.makedirs(CMP, exist_ok=True)
    rows = json.load(open(R('results/v2p6/necessity_rows.json')))
    jobs, miss = [], []
    for r in rows:
        for k in range(1, REPEATS + 1):
            fa = os.path.join(ARM, f"{r['chain']}_A{k}.out.txt")
            fb = os.path.join(ARM, f"{r['chain']}_B{k}.out.txt")
            if not (os.path.exists(fa) and os.path.exists(fb)):
                miss.append(f"{r['chain']}_{k}"); continue
            body = COMPARE.format(q=r['q'], a=open(fa).read().strip(), b=open(fb).read().strip())
            f = os.path.join(CMP, f"{r['chain']}_{k}.txt")
            open(f, 'w').write(body)
            jobs.append({'id': f"{r['chain']}_{k}", 'agent': 'net-grader', 'prompt': f,
                         'out': os.path.join(CMP, f"{r['chain']}_{k}.out.txt")})
    json.dump(jobs, open(R('results/v2p6/compare_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} comparisons, {len(miss)} pairs missing an arm reply: {miss[:10]}')
    return jobs


def collect():
    rows = {r['chain']: r for r in json.load(open(R('results/v2p6/necessity_rows.json')))}
    out, unruled = {}, []
    for ch, r in rows.items():
        votes = []
        for k in range(1, REPEATS + 1):
            f = os.path.join(CMP, f'{ch}_{k}.out.txt')
            if not os.path.exists(f): continue
            o = obj(open(f).read(), 'changed') or {}
            v = (o.get('changed') or '').strip().lower()
            v = 'yes' if v.startswith('y') else ('no' if v.startswith('n') else None)
            if v: votes.append({'vote': v, 'what': (o.get('what_changed') or '').strip().lower(),
                                'why': (o.get('why') or '').strip()})
        if not votes: unruled.append(ch); continue
        c = collections.Counter(v['vote'] for v in votes)
        maj = c.most_common(1)[0][0]
        out[ch] = {'necessity': maj, 'votes': [v['vote'] for v in votes],
                   'unanimous': len(c) == 1 and len(votes) == REPEATS,
                   'n_votes': len(votes), 'paper': r['paper'], 'depth': r['depth'],
                   'final': r['final'], 'upstream': r['upstream'],
                   'predecessor_varies': r['predecessor_varies'],
                   'why': [v['why'] for v in votes], 'what': [v['what'] for v in votes]}
    full = [v for v in out.values() if v['n_votes'] == REPEATS]
    agree = [v for v in full if v['unanimous']]
    res = {'note': 'v2.6 step 5. Two arms x 3 repeats per chain, one comparison per repeat.',
           'chains': len(rows), 'ruled': len(out), 'unruled': unruled,
           'necessity': dict(collections.Counter(v['necessity'] for v in out.values())),
           'stability': {'chains_with_3_votes': len(full), 'unanimous': len(agree),
                         'share': round(len(agree) / len(full), 3) if full else None},
           'by_depth': {str(d): dict(collections.Counter(
               v['necessity'] for v in out.values() if v['depth'] == d))
               for d in sorted({v['depth'] for v in out.values()})},
           'chains_out': out}
    json.dump(res, open(R('results/v2p6/necessity.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'chains_out'}, indent=1))
    return res


if __name__ == '__main__':
    {'arms': arms, 'compare': compare, 'collect': collect}[sys.argv[1]]()
