"""graded.py: v2.7 Part B -- a graded comparer, and necessity measured against the noise floor.

  python3 -m trace_kit_v2p7.graded build     prompts for the A-vs-B and A-vs-A pairs
  python3 -m trace_kit_v2p7.graded collect   scores, the per-chain margin, and agreement

Part A showed the yes/no comparer says "changed" on 29.1% of pairs where nothing was added.
The question was binary and the thing being judged is a difference of degree, so the comparer
had to round ordinary rewording up to "yes".

Two changes. First the comparer scores 0 to 3 instead of answering yes or no, and has to name
the specific difference or say "none" -- a score with nothing to point at is a score it has to
reconsider. Second, and this is what actually removes the floor, each chain is judged against
ITSELF: the same graded comparer scores that chain's A-vs-A pairs, and necessity is counted
only when the A-vs-B score beats that chain's own A-vs-A score by at least a point, in 2 of 3
repeats. A chain whose answers wander on their own has to clear a higher bar, which is the
correct behaviour and something no single global threshold can do.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402
from trace_kit_v2p6.clean import clean  # noqa: E402
from trace_kit_v2p7.partA import chains, a_path, V6ARM  # noqa: E402

OUT = R('results/v2p7/graded')
REPEATS = 3

GRADE = """Two answers to the same question about one set of measurements. Both answerers saw exactly the same evidence. They were produced independently, so they will differ in wording whatever else is true.

THE QUESTION
{q}

ANSWER 1
{a}

ANSWER 2
{b}

Score how far the SUBSTANCE differs: the conclusion each says the evidence justifies, and the uncertainty each says is left. Ignore wording, length, ordering, tone, and which facts each one happens to mention first.

  0  the same claim held with the same confidence. Different words, same position.
  1  the same claim, but one states it with detectably more or less confidence, or names a
     caveat the other leaves out, without changing what is concluded.
  2  a materially different scope or strength of claim -- one rules something out, or commits
     to a mechanism, or withholds a commitment, where the other does not.
  3  a different conclusion. They cannot both be the position of one careful reader.

Name the specific difference in `difference`, quoting from both answers. If you cannot point to one, the score is 0 and `difference` is "none". A score above 0 with nothing quotable to point at is wrong: reconsider it before answering.

Return JSON and nothing else:
{{"score": 0 | 1 | 2 | 3,
 "difference": "the specific difference, quoting both answers, or \\"none\\"",
 "kind": "conclusion" | "uncertainty" | "both" | "none"}}"""


def b_path(ch, k):
    return os.path.join(V6ARM, f'{ch}_B{k}.out.txt')


def build():
    os.makedirs(OUT, exist_ok=True)
    jobs, miss = [], []
    for r in chains():
        ch = r['chain']
        for i in (1, 2, 3):
            for kind, fa, fb in (('AB', a_path(ch, i), b_path(ch, i)),
                                 ('AA', a_path(ch, i), a_path(ch, i + REPEATS))):
                if not (os.path.exists(fa) and os.path.exists(fb)):
                    miss.append(f'{ch}_{kind}{i}'); continue
                body = GRADE.format(q=r['q'], a=clean(open(fa).read()), b=clean(open(fb).read()))
                f = os.path.join(OUT, f'{ch}_{kind}{i}.txt')
                open(f, 'w').write(body)
                jobs.append({'id': f'{ch}_{kind}{i}', 'agent': 'net-grader', 'prompt': f,
                             'out': os.path.join(OUT, f'{ch}_{kind}{i}.out.txt')})
    json.dump(jobs, open(R('results/v2p7/graded_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} graded comparisons '
          f'({len(chains())} chains x {REPEATS} repeats x 2 pair kinds), {len(miss)} missing')
    return jobs


def score(f):
    if not os.path.exists(f): return None
    raw = open(f).read()
    o = obj(raw, 'score') or {}
    s = o.get('score')
    if isinstance(s, str) and s.strip().isdigit(): s = int(s.strip())
    if not isinstance(s, int):
        import re
        m = re.search(r'"score"\s*:\s*([0-3])', raw)
        s = int(m.group(1)) if m else None
    if s is None: return None
    return {'score': s, 'difference': (o.get('difference') or '').strip(),
            'kind': (o.get('kind') or '').strip().lower()}


def collect():
    out, unruled = {}, []
    for r in chains():
        ch = r['chain']
        ab = [score(os.path.join(OUT, f'{ch}_AB{i}.out.txt')) for i in (1, 2, 3)]
        aa = [score(os.path.join(OUT, f'{ch}_AA{i}.out.txt')) for i in (1, 2, 3)]
        if any(x is None for x in ab + aa): unruled.append(ch); continue
        margins = [ab[i]['score'] - aa[i]['score'] for i in range(REPEATS)]
        wins = sum(1 for m in margins if m >= 1)
        out[ch] = {
            'paper': r['paper'], 'depth': r['depth'],
            'ab_scores': [x['score'] for x in ab], 'aa_scores': [x['score'] for x in aa],
            'margins': margins, 'repeats_won': wins, 'necessity': 'yes' if wins >= 2 else 'no',
            'ab_unanimous': len({x['score'] for x in ab}) == 1,
            'aa_unanimous': len({x['score'] for x in aa}) == 1,
            'ab_spread': max(x['score'] for x in ab) - min(x['score'] for x in ab),
            'ab_difference': [x['difference'][:300] for x in ab],
            'ab_kind': [x['kind'] for x in ab],
        }
    n = len(out)
    allab = [s for v in out.values() for s in v['ab_scores']]
    allaa = [s for v in out.values() for s in v['aa_scores']]
    # agreement across repeats: the three repeats of a chain land on the same score
    agree_ab = sum(1 for v in out.values() if v['ab_unanimous'])
    # a looser and fairer reading for an ordinal scale: all three within one point
    near_ab = sum(1 for v in out.values() if v['ab_spread'] <= 1)
    agree_dec = sum(1 for v in out.values() if v['repeats_won'] in (0, 3))
    res = {
        'note': 'v2.7 Part B. Graded 0-3 comparer; necessity is the A-vs-B score beating that '
                "chain's own A-vs-A score by >=1 point in 2 of 3 repeats.",
        'chains': n, 'unruled': unruled,
        'ab_score_hist': dict(sorted(collections.Counter(allab).items())),
        'aa_score_hist': dict(sorted(collections.Counter(allaa).items())),
        'ab_mean': round(sum(allab) / len(allab), 3) if allab else None,
        'aa_mean': round(sum(allaa) / len(allaa), 3) if allaa else None,
        'necessity': dict(collections.Counter(v['necessity'] for v in out.values())),
        'stability': {
            'ab_all_three_same_score': agree_ab, 'ab_all_three_within_one': near_ab,
            'decision_unanimous': agree_dec, 'chains': n,
            'share_same_score': round(agree_ab / n, 3) if n else None,
            'share_within_one': round(near_ab / n, 3) if n else None,
            'share_decision_unanimous': round(agree_dec / n, 3) if n else None,
        },
        'chains_out': out,
    }
    st = res['stability']
    res['stop_rule_fired'] = bool(n and st['share_decision_unanimous'] < 2 / 3)
    json.dump(res, open(R('results/v2p7/partB.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'chains_out'}, indent=1))
    return res


if __name__ == '__main__':
    {'build': build, 'collect': collect}[sys.argv[1]]()
