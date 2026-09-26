"""step5.py: v2.9 -- depth 3 chains, and three worked examples.

  python3 -m trace_kit_v2p9.step5

A depth 3 chain counts only when BOTH links pass: the first link's item was compositional at
step 4, and the next link is compositional in its own right. Passing the second test on a first
link that failed would be a chain built on sand.

Every verdict is model against model.
"""
import json, math, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)


def wilson(k, n, z=1.96):
    if not n: return (None, None)
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(max(0.0, c - h), 4), round(min(1.0, c + h), 4))


def run():
    S4 = json.load(open(R('results/v2p9/step4.json')))
    S4n = json.load(open(R('results/v2p9/step4_nl.json')))
    NL = {x['item']: x for x in json.load(open(R('results/v2p9/nextlink.json')))['pairs_out']}
    K = json.load(open(R('results/v2p9/keys.json')))
    Kn = json.load(open(R('results/v2p9/keys_nl.json')))
    P = {x['item']: x for x in json.load(open(R('results/v2p9/pairs.json')))['pairs_out']}
    D5 = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}

    chains, passed = [], 0
    for it, v in S4n['items_out'].items():
        nl = NL[it]; parent = nl['parent_item']
        p4 = S4['items_out'].get(parent) or {}
        both = bool(v['compositional'] and p4.get('compositional'))
        passed += v['compositional']
        chains.append({'chain_id': it, 'paper': nl['paper'], 'parent': parent,
                       'first_link_passed': bool(p4.get('compositional')),
                       'next_link_passed': bool(v['compositional']),
                       'depth3': both,
                       'first_scores': p4.get('mean_combined'),
                       'next_scores': v['mean_combined']})
    d3 = [c for c in chains if c['depth3']]
    lo, hi = wilson(passed, len(chains))

    worked = []
    for c in d3[:3]:
        nl = NL[c['chain_id']]; par = P[c['parent']]; up = D5[par['upstream_item']]
        worked.append({'chain_id': c['chain_id'], 'paper': c['paper'], 'steps': [
            {'what': f"the v2.5 two-step item `{up['item']}` ({up['generator']})",
             'observation': up['observation_a']['text'] + '  +  ' + up['observation_b']['text'],
             'obs_node': f"{up['observation_a']['node']}, {up['observation_b']['node']}",
             'key': (up.get('key') or {}).get('proposition'), 'scores': None},
            {'what': f"link 1, `{c['parent']}` — its key became the next earlier result",
             'input_result': par['input_result'], 'observation': par['new_observation']['text'],
             'obs_node': par['new_observation']['node'],
             'key': (K.get(c['parent']) or {}).get('proposition'),
             'scores': c['first_scores']},
            {'what': f"link 2, `{c['chain_id']}`",
             'input_result': nl['input_result'], 'observation': nl['new_observation']['text'],
             'obs_node': nl['new_observation']['node'],
             'key': (Kn.get(c['chain_id']) or {}).get('proposition'),
             'scores': c['next_scores']}]})

    res = {'note': 'v2.9 Step 5. A depth 3 chain needs both of its links to pass.',
           'next_links_tested': len(chains), 'tested': len(chains), 'passed': passed,
           'pass_rate': round(passed / len(chains), 4) if chains else None,
           'pass_rate_95ci': [lo, hi],
           'depth2_pass_rate': S4['pass_rate'], 'depth2_95ci': S4['pass_rate_95ci'],
           'depth3_chains': len(d3),
           'first_link_failed': sum(1 for c in chains if not c['first_link_passed']),
           'mean_combined_across_items': S4n['mean_combined_across_items'],
           'mean_limit_across_items': S4n['mean_limit_across_items'],
           'N_at_or_above_threshold': S4n['N_at_or_above_threshold'],
           'borderline_count': S4n['borderline_count'],
           'borderline_flips': S4n['borderline_flips'],
           'chains': chains, 'worked': worked}
    json.dump(res, open(R('results/v2p9/step5.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k not in ('chains', 'worked')}, indent=1))
    return res


if __name__ == '__main__': run()
