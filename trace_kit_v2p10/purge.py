"""purge.py: v2.10 Step 1 -- drop anything the model could reach from the paper's name.

  python3 -m trace_kit_v2p10.purge

No model call. v2.9 already asked arm N, which gets the paper's real title and journal and is
told to guess and not refuse. Where it scored 0.25 or more on the key's combined claims, the
item is not a test of reasoning over evidence: a model that knows the paper can supply the
answer without looking. Those items are removed here rather than reported as a caveat, and a
chain dies if ANY of its links is flagged -- a chain is only as clean as its dirtiest step.

The flagged items are kept in full, with their arm N answers, because "the model already knew
this one" is a finding about the corpus and not a defect to be swept up.

Every verdict is model against model.
"""
import collections, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
NBAR = 0.25


def run():
    S4 = json.load(open(R('results/v2p9/step4.json')))
    S4n = json.load(open(R('results/v2p9/step4_nl.json')))
    S5 = json.load(open(R('results/v2p9/step5.json')))
    NL = {x['item']: x for x in json.load(open(R('results/v2p9/nextlink.json')))['pairs_out']}

    def nscore(v): return v['mean_combined']['N']

    flag2 = {k: v for k, v in S4['items_out'].items() if nscore(v) >= NBAR}
    flag3 = {k: v for k, v in S4n['items_out'].items() if nscore(v) >= NBAR}

    # depth 2: an item survives if it passed and is not flagged
    live2 = {k: v for k, v in S4['items_out'].items()
             if v['compositional'] and k not in flag2}

    # depth 3: both links must pass AND neither may be flagged
    chains3 = []
    for c in S5['chains']:
        par = c['parent']
        bad = [x for x in (par, c['chain_id']) if x in flag2 or x in flag3]
        chains3.append({**c, 'flagged_links': bad,
                        'survives': bool(c['depth3'] and not bad)})
    live3 = [c for c in chains3 if c['survives']]

    def answer_of(item, arm='N'):
        for d in ('results/v2p9/arms', 'results/v2p9/arms_nl'):
            f = R(d, f'{item}_{arm}1.out.txt')
            if os.path.exists(f): return open(f).read().strip()
        return None

    record = []
    for k, v in list(flag2.items()) + list(flag3.items()):
        record.append({'item': k, 'paper': v['paper'], 'depth': 2 if k in flag2 else 3,
                       'N': nscore(v), 'B': v['mean_combined']['B'],
                       'was_compositional': v['compositional'],
                       'arm_N_answer': (answer_of(k) or '')[:1200]})

    res = {
        'note': 'v2.10 Step 1. Arm N >= 0.25 means the paper name alone reached the claims.',
        'threshold': NBAR,
        'depth2': {'before': S4['compositional'], 'flagged': len(flag2),
                   'flagged_and_passing': sum(1 for v in flag2.values() if v['compositional']),
                   'after': len(live2)},
        'depth3': {'before': S5['depth3_chains'], 'flagged_links': len(flag3),
                   'chains_killed': sum(1 for c in chains3 if c['depth3'] and c['flagged_links']),
                   'after': len(live3)},
        'flagged_depth2': sorted(flag2), 'flagged_depth3': sorted(flag3),
        'per_paper_flagged': dict(collections.Counter(
            v['paper'] for v in list(flag2.values()) + list(flag3.values()))),
        'live_depth2': sorted(live2), 'live_depth3': [c['chain_id'] for c in live3],
        'chains3': chains3,
        'memorised_record': record,
    }
    json.dump(res, open(R('results/v2p10/purge.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items()
                      if k not in ('chains3', 'memorised_record', 'live_depth2',
                                   'live_depth3', 'flagged_depth2', 'flagged_depth3')}, indent=1))
    return res


if __name__ == '__main__': run()
