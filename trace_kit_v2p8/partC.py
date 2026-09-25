"""partC.py: v2.8 Part C -- grade every answer against the item's claim list.

  python3 -m trace_kit_v2p8.partC build     one grading prompt per answer
  python3 -m trace_kit_v2p8.partC collect   per-answer scores

This is the change the whole pilot turns on. v2.6 and v2.7 asked a comparer whether two answers
differed, and v2.7 Part A measured what that costs: two samples of one prompt differ 29% of the
time, so the instrument could not see a single item. Here the target is fixed. The claim list
does not vary between arms or between samples, so every answer is measured against the same
ruler and the scores are comparable by construction.

The grader sees one answer and the claim list. It never sees the arm label, the other arms, the
earlier result, or the measurement -- only whether this answer reaches these claims. Naming the
arm would let it grade the setup instead of the text, and that is the failure v2.7 was built to
escape.

Every "stated" or "contradicted" ruling has to quote the answer. A ruling with nothing to quote
is a ruling the grader has to withdraw, which is the same discipline the v2.7 graded comparer
used and the one part of it that worked.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402
from trace_kit_v2p6.clean import clean  # noqa: E402

ARMS = R('results/v2p8/arms')
GRADE = R('results/v2p8/grade')
SAMPLES = 6

ASK = """You are checking one answer against a fixed list of claims. You are not judging whether the answer is good, and you are not comparing it with anything.

THE ANSWER
{answer}

For each numbered claim below, rule one of:

  stated        the answer asserts this claim, or asserts something that plainly carries it.
                Different wording is fine; the assertion has to be there.
  contradicted  the answer asserts something incompatible with this claim.
  absent        the answer neither asserts it nor denies it.

Quote the answer's own words for every "stated" and every "contradicted". If you cannot quote anything, the ruling is "absent" -- a claim you cannot point to in the text is not stated, however plausible it is that the answerer believed it.

Do not reward an answer for being cautious or for hedging. "Cannot be determined" is not a statement of the claim.

Return JSON and nothing else, one entry per claim, in the same order:
{{"rulings": [{{"n": 1, "verdict": "stated" | "contradicted" | "absent", "quote": "the answer's words, or \\"\\" when absent"}}, ...]}}

THE CLAIMS
{claims}"""


def claim_list(item, A):
    """combined claims first, then limits; both scored, in one stable order"""
    v = A['claims'][item]
    out = [{'claim': c['claim'], 'kind': 'combined'}
           for c in v['kept'] if c['tag'] == 'combined']
    out += [{'claim': c['claim'], 'kind': 'limit'} for c in v['limits']]
    return out


def build():
    os.makedirs(GRADE, exist_ok=True)
    A = json.load(open(R('results/v2p8/partA.json')))
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    jobs, miss, index = [], [], {}
    for s in S:
        it = s['item']
        cs = claim_list(it, A)
        index[it] = cs
        listing = '\n'.join(f"{i}. {c['claim']}" for i, c in enumerate(cs, 1))
        for arm in ('A', 'B', 'C'):
            for k in range(1, SAMPLES + 1):
                fa = os.path.join(ARMS, f'{it}_{arm}{k}.out.txt')
                if not os.path.exists(fa): miss.append(f'{it}_{arm}{k}'); continue
                body = ASK.format(answer=clean(open(fa).read()), claims=listing)
                f = os.path.join(GRADE, f'{it}_{arm}{k}.txt'); open(f, 'w').write(body)
                jobs.append({'id': f'{it}_{arm}{k}', 'agent': 'net-grader', 'prompt': f,
                             'out': os.path.join(GRADE, f'{it}_{arm}{k}.out.txt')})
    json.dump(index, open(R('results/v2p8/claim_index.json'), 'w'), indent=1)
    json.dump(jobs, open(R('results/v2p8/grade_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} gradings, {len(miss)} answers missing: {miss[:8]}')
    return jobs


def collect():
    index = json.load(open(R('results/v2p8/claim_index.json')))
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    per, unparsed = {}, []
    for s in S:
        it = s['item']; cs = index[it]
        ncomb = sum(1 for c in cs if c['kind'] == 'combined')
        nlim = sum(1 for c in cs if c['kind'] == 'limit')
        for arm in ('A', 'B', 'C'):
            for k in range(1, SAMPLES + 1):
                f = os.path.join(GRADE, f'{it}_{arm}{k}.out.txt')
                if not os.path.exists(f): unparsed.append((f'{it}_{arm}{k}', 'no reply')); continue
                o = obj(open(f).read(), 'rulings')
                if not o: unparsed.append((f'{it}_{arm}{k}', 'unparsed')); continue
                rul = {int(x['n']): x for x in o.get('rulings', [])
                       if str(x.get('n', '')).strip().isdigit()}
                comb_s = lim_s = contra = 0
                rows = []
                for i, c in enumerate(cs, 1):
                    r = rul.get(i) or {}
                    v = (r.get('verdict') or '').strip().lower()
                    q = (r.get('quote') or '').strip()
                    # a "stated" with nothing quoted is withdrawn to absent, as the prompt says
                    if v == 'stated' and not q: v = 'absent'
                    if v == 'stated':
                        if c['kind'] == 'combined': comb_s += 1
                        else: lim_s += 1
                    elif v == 'contradicted':
                        contra += 1
                    rows.append({'n': i, 'kind': c['kind'], 'claim': c['claim'],
                                 'verdict': v or 'absent', 'quote': q[:300]})
                per[f'{it}_{arm}{k}'] = {
                    'item': it, 'arm': arm, 'sample': k,
                    'combined_score': round(comb_s / ncomb, 4) if ncomb else None,
                    'limit_score': round(lim_s / nlim, 4) if nlim else None,
                    'contradictions': contra,
                    'n_combined': ncomb, 'n_limit': nlim, 'rulings': rows,
                }
    res = {'note': 'v2.8 Part C. One grading per answer against a fixed claim list.',
           'graded': len(per), 'unparsed': unparsed,
           'withdrawn_stated_without_quote': sum(
               1 for v in per.values() for r in v['rulings']
               if r['verdict'] == 'absent' and r['quote']),
           'answers': per}
    json.dump(res, open(R('results/v2p8/partC.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'answers'}, indent=1))
    return res


if __name__ == '__main__':
    {'build': build, 'collect': collect}[sys.argv[1]]()
