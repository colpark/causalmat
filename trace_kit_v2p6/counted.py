"""counted.py: v2.6 step 6 -- which merges count.

  python3 -m trace_kit_v2p6.counted

Three gates, all of them must pass:

  step 3  the seam is not "upstream ignored"
  step 4  the seam's scope verdict is "supports" or "supports only narrower"
  step 5  the chain's necessity verdict is "yes"

Steps 3 and 4 rule one seam. Step 5 rules one chain, by testing the last step in it. So the
funnel is counted over CHAINS: a chain clears step 3 when no seam in it is flagged, clears
step 4 when every seam in it has an acceptable scope verdict, and clears step 5 on its own
necessity ruling. A chain through all three is compositional.

A seam is counted when it passes its own two gates and lies on at least one compositional
chain. A seam that fails, or that lies only on chains that fail, stays on the page and is
labelled a failed merge: it is a negative example, not a deletion.

Every verdict is model against model.
"""
import collections, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)

SCOPE_OK = ('supports', 'supports only narrower')


def run():
    P = json.load(open(R('results/v2p6/pruned.json')))
    IG = json.load(open(R('results/v2p6/ignored.json')))['seams']
    SC = json.load(open(R('results/v2p6/scope.json')))['seams']
    NE = json.load(open(R('results/v2p6/necessity.json')))['chains_out']

    seams = {}
    for j in P['joins']:
        k = f"{j['from']}__{j['to']}"
        ig = bool((IG.get(k) or {}).get('ignored'))
        sc = (SC.get(k) or {}).get('verdict')
        seams[k] = {'paper': j['paper'], 'from': j['from'], 'to': j['to'],
                    'on_claim': j['on_claim'], 'upstream_ignored': ig, 'scope': sc,
                    'gate3': not ig, 'gate4': sc in SCOPE_OK,
                    'scope_why': (SC.get(k) or {}).get('why'),
                    'ignored_signals': (IG.get(k) or {}).get('signals') or []}

    chains = []
    for c in P['chains']:
        ks = [f'{a}__{b}' for a, b in zip(c['path'], c['path'][1:])]
        rows = [seams.get(k) or {} for k in ks]
        n = NE.get(c['chain']) or {}
        g3 = all(not r.get('upstream_ignored') for r in rows)
        g4 = all(r.get('scope') in SCOPE_OK for r in rows)
        g5 = n.get('necessity') == 'yes'
        chains.append({**c, 'seams': ks, 'gate3': g3, 'gate4': g4, 'gate5': g5,
                       'necessity': n.get('necessity'), 'votes': n.get('votes'),
                       'unanimous': n.get('unanimous'),
                       'compositional': bool(g3 and g4 and g5)})

    on_good = {k for c in chains if c['compositional'] for k in c['seams']}
    for k, s in seams.items():
        s['on_compositional_chain'] = k in on_good
        s['counted'] = bool(s['gate3'] and s['gate4'] and k in on_good)

    # funnel, over chains, each stage applied on top of the last
    f3 = [c for c in chains if c['gate3']]
    f4 = [c for c in f3 if c['gate4']]
    f5 = [c for c in f4 if c['gate5']]
    fun = P['funnel']
    funnel = [
        ('chains in v2.5', fun['chains_v2p5']),
        ('after dropping covariation', fun['after_drop_covariation']),
        ('after collapsing chains that share a tail', fun['after_dedup']),
        ('after step 3, no seam ignores the upstream result', len(f3)),
        ('after step 4, every seam passes the scope check', len(f4)),
        ('after step 5, the upstream changes the last answer', len(f5)),
    ]
    per_paper = collections.defaultdict(lambda: collections.Counter())
    for c in chains:
        p = per_paper[c['paper']]
        p['chains'] += 1
        p['gate3'] += c['gate3']; p['gate4'] += c['gate3'] and c['gate4']
        p['compositional'] += c['compositional']
    for k, s in seams.items():
        p = per_paper[s['paper']]
        p['seams'] += 1; p['ignored'] += s['upstream_ignored']; p['counted'] += s['counted']

    res = {
        'note': 'v2.6 step 6. A merge counts only through all three gates.',
        'funnel': funnel,
        'chains': len(chains), 'compositional': len(f5),
        'seams': len(seams), 'seams_counted': sum(1 for s in seams.values() if s['counted']),
        'seam_gates': {'upstream_ignored': sum(1 for s in seams.values() if s['upstream_ignored']),
                       'scope_failed': sum(1 for s in seams.values() if not s['gate4']),
                       'scope': dict(collections.Counter(s['scope'] for s in seams.values()))},
        'lost_at': {'step3': len(chains) - len(f3), 'step4': len(f3) - len(f4),
                    'step5': len(f4) - len(f5)},
        'depth_compositional': dict(sorted(collections.Counter(
            c['depth'] for c in f5).items())),
        'depth_after_dedup': dict(sorted(collections.Counter(c['depth'] for c in chains).items())),
        'per_paper': {k: dict(v) for k, v in sorted(per_paper.items())},
        'chains_out': chains, 'seams_out': seams,
    }
    json.dump(res, open(R('results/v2p6/counted.json'), 'w'), indent=1)
    return res


if __name__ == '__main__':
    r = run()
    print(json.dumps({k: v for k, v in r.items()
                      if k not in ('chains_out', 'seams_out', 'per_paper')}, indent=1))
