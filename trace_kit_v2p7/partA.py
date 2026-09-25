"""partA.py: v2.7 Part A -- the noise floor of the v2.6 necessity check.

  python3 -m trace_kit_v2p7.partA arms      3 more arm A samples per chain
  python3 -m trace_kit_v2p7.partA compare   v2.6's yes/no comparer on arm A vs arm A
  python3 -m trace_kit_v2p7.partA collect   the false-positive rate

v2.6 asked a comparer whether arm B differed from arm A, where arm B had the upstream result
appended. It said yes 53.7% of the time. That number is meaningless on its own, because two
samples of the SAME prompt also differ -- different wording, different hedges, sometimes a
different emphasis. If the comparer calls that a change too, then 53.7% is measuring sampling
variation and not the upstream result.

So: answer arm A three more times from the byte-identical prompt, pair the new samples against
the old ones, and put the same comparer on them. Whatever it says yes to here is a false
positive. The prompts are read straight out of results/v2p6/arms/, unchanged, so the only
difference between this and the v2.6 run is which sample sits on each side.

Every verdict is model against model.
"""
import collections, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402
from trace_kit_v2p6.clean import clean  # noqa: E402
from trace_kit_v2p6.necessity import COMPARE  # noqa: E402

V6ARM = R('results/v2p6/arms')          # read only, never written
OUT = R('results/v2p7/armsA')
CMP = R('results/v2p7/compareAA')
REPEATS = 3
NEW = (4, 5, 6)                          # the three extra arm A samples


def chains():
    ids = set(json.load(open(R('results/v2p7/partA_chains.json'))))
    rows = [r for r in json.load(open(R('results/v2p6/necessity_rows.json')))
            if r['chain'] in ids]
    assert len(rows) == len(ids), (len(rows), len(ids))
    return rows


def arms():
    os.makedirs(OUT, exist_ok=True)
    jobs = []
    for r in chains():
        p = os.path.join(V6ARM, f"{r['chain']}_A.txt")
        assert os.path.exists(p), p
        for k in NEW:
            jobs.append({'id': f"{r['chain']}_A{k}", 'agent': 'net-fullarm', 'prompt': p,
                         'out': os.path.join(OUT, f"{r['chain']}_A{k}.out.txt")})
    json.dump(jobs, open(R('results/v2p7/partA_arm_jobs.json'), 'w'), indent=1)
    print(f'{len(chains())} chains, {len(jobs)} extra arm A calls '
          f'(the v2.6 prompt files, unchanged)')
    return jobs


def a_path(ch, k):
    """arm A sample k: 1-3 are v2.6's, 4-6 are this run's"""
    return (os.path.join(V6ARM, f'{ch}_A{k}.out.txt') if k <= REPEATS
            else os.path.join(OUT, f'{ch}_A{k}.out.txt'))


def compare():
    os.makedirs(CMP, exist_ok=True)
    jobs, miss = [], []
    for r in chains():
        for i, k in enumerate(NEW, start=1):
            fa, fb = a_path(r['chain'], i), a_path(r['chain'], k)
            if not (os.path.exists(fa) and os.path.exists(fb)):
                miss.append(f"{r['chain']}_{i}"); continue
            # clean() strips the framing fragments and MCP notes, as in v2.6
            body = COMPARE.format(q=r['q'], a=clean(open(fa).read()), b=clean(open(fb).read()))
            f = os.path.join(CMP, f"{r['chain']}_{i}.txt")
            open(f, 'w').write(body)
            jobs.append({'id': f"{r['chain']}_{i}", 'agent': 'net-grader', 'prompt': f,
                         'out': os.path.join(CMP, f"{r['chain']}_{i}.out.txt")})
    json.dump(jobs, open(R('results/v2p7/partA_cmp_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} A-vs-A comparisons, {len(miss)} pairs missing a sample: {miss[:8]}')
    return jobs


def vote(f):
    if not os.path.exists(f): return None
    raw = open(f).read()
    o = obj(raw, 'changed') or {}
    v = (o.get('changed') or '').strip().lower()
    if not v:
        m = re.search(r'"changed"\s*:\s*"(yes|no)"', raw, re.I)
        if m: v = m.group(1).lower()
    return 'yes' if v.startswith('y') else ('no' if v.startswith('n') else None)


def collect():
    N6 = json.load(open(R('results/v2p6/necessity.json')))['chains_out']
    out, unruled = {}, []
    for r in chains():
        ch = r['chain']
        vs = [vote(os.path.join(CMP, f'{ch}_{i}.out.txt')) for i in (1, 2, 3)]
        vs = [v for v in vs if v]
        if not vs: unruled.append(ch); continue
        c = collections.Counter(vs)
        out[ch] = {'votes': vs, 'yes': c['yes'], 'majority': c.most_common(1)[0][0],
                   'unanimous': len(c) == 1 and len(vs) == REPEATS,
                   'depth': r['depth'], 'paper': r['paper'],
                   'ab_votes': (N6.get(ch) or {}).get('votes'),
                   'ab_majority': (N6.get(ch) or {}).get('necessity')}
    nv = sum(len(v['votes']) for v in out.values())
    ny = sum(v['yes'] for v in out.values())
    # the same 63 chains on v2.6's A-vs-B run, so the two rates are comparable
    ab = [v for k, v in N6.items() if k in out]
    abv = sum(len(v['votes']) for v in ab); aby = sum(v['votes'].count('yes') for v in ab)
    res = {
        'note': "v2.7 Part A. v2.6's comparer on arm A vs arm A: the false positive floor.",
        'chains': len(out), 'unruled': unruled,
        'aa': {'rulings': nv, 'yes': ny, 'yes_rate': round(ny / nv, 3) if nv else None,
               'chains_majority_yes': sum(1 for v in out.values() if v['majority'] == 'yes'),
               'unanimous': sum(1 for v in out.values() if v['unanimous'])},
        'ab_same_chains': {'rulings': abv, 'yes': aby,
                           'yes_rate': round(aby / abv, 3) if abv else None,
                           'chains_majority_yes': sum(1 for v in ab if v['necessity'] == 'yes'),
                           'unanimous': sum(1 for v in ab if v['unanimous'])},
        'chains_out': out,
    }
    res['lift'] = (round(res['ab_same_chains']['yes_rate'] - res['aa']['yes_rate'], 3)
                   if nv and abv else None)
    res['stop_rule_fired'] = bool(nv and res['aa']['yes_rate'] >= 0.40)
    json.dump(res, open(R('results/v2p7/partA.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'chains_out'}, indent=1))
    return res


if __name__ == '__main__':
    {'arms': arms, 'compare': compare, 'collect': collect}[sys.argv[1]]()
