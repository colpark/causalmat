"""nextlink.py: v2.9 Step 5 -- one more link, making a depth 3 chain.

  python3 -m trace_kit_v2p9.nextlink build   candidates from every compositional item

A depth 2 item took an earlier result and one unused observation. A depth 3 chain does it again:
the item's own key proposition and limits become the earlier result, and the next observation
must be unused by the WHOLE chain, not just by the step before it. That is checked against every
node and every panel any earlier step touched -- the two observations of the original v2.5 item,
the observation this item added, and all their panels. A chain that quietly re-reads its own
first measurement at step 3 would look like it was building and would only be circling.

At most 2 next links per item, taken in a fixed order so the run reproduces.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v3'))
sys.path.insert(0, R('trace_kit_v2p5'))
from support import claim_support  # noqa: E402
from trace_kit_v2p9.pairs import panels_of, REL, MAX_PANELS  # noqa: E402
import importlib.util as _ilu  # noqa: E402
_sp = _ilu.spec_from_file_location('v2p5_items_nl', R('trace_kit_v2p5', 'items.py'))
_v25 = _ilu.module_from_spec(_sp); _sp.loader.exec_module(_v25)
store_for = _v25.store_for

MAX_NEXT = 2


def run():
    S4 = json.load(open(R('results/v2p9/step4.json')))
    K = json.load(open(R('results/v2p9/keys.json')))
    D5 = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    out, drops = [], collections.Counter()
    per_item = collections.Counter()
    for it, v in S4['items_out'].items():
        if not v['compositional']: continue
        paper = v['paper']
        gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
        gr = json.load(open(R(gp))); N = {n['id']: n for n in gr['nodes']}
        store = store_for(R(gp))
        sup = claim_support(gr)
        obs_of = collections.defaultdict(set)
        for c, r in sup.items(): obs_of[c] |= set(r['via'])
        oe = collections.defaultdict(set)
        for e in gr['edges']:
            if e.get('rel') in REL: oe[e['src']].add(e['dst'])

        up = D5[v['upstream']]
        # everything the chain has already touched, both steps of it
        used_nodes = {up['observation_a']['node'], up['observation_b']['node'],
                      v['new_observation']['node']}
        used_pans = {q.get('panel_id') for q in (up.get('panels') or []) if q.get('panel_id')}
        for x in json.load(open(R('results/v2p9/pairs.json')))['pairs_out']:
            if x['item'] == it:
                used_pans |= {q.get('panel_id') for q in x['panels'] if q.get('panel_id')}
        T = v['target_claim']
        for tgt in sorted(oe.get(T, ())):
            if per_item[it] >= MAX_NEXT: drops['over the 2-per-item cap'] += 1; continue
            for o in sorted(obs_of.get(tgt, ())):
                if per_item[it] >= MAX_NEXT: break
                if o in used_nodes: drops['observation already used in the chain'] += 1; continue
                node = N.get(o) or {}
                if not node.get('panel_ids'): drops['no panels'] += 1; continue
                pans = panels_of(node, store)
                if not pans: drops['no usable crop'] += 1; continue
                npans = {q['panel_id'] for q in pans if q.get('panel_id')}
                if npans & used_pans:
                    drops['panel already used in the chain'] += 1; continue
                per_item[it] += 1
                out.append({
                    'item': f'nl_{it}_{o}_{tgt}', 'paper': paper, 'generator': 'derived_input',
                    'depth': 3, 'parent_item': it, 'upstream_item': it,
                    'chain': [v['upstream'], it],
                    'claim_C': T, 'target_claim': tgt,
                    'input_result': (K[it].get('proposition') or '').strip(),
                    'input_limits': [str(t) for t in (K[it].get('limits') or [])],
                    'new_observation': {'node': o, 'text': (node.get('label') or '').strip(),
                                        'technique': node.get('technique')},
                    'panels': pans[:MAX_PANELS],
                    'chain_obs_nodes': sorted(used_nodes),
                    'chain_panel_ids': sorted(x for x in used_pans),
                    'edge': f'{T} -> {tgt}',
                })
    ids = [x['item'] for x in out]
    assert len(ids) == len(set(ids)), [k for k, n in collections.Counter(ids).items() if n > 1]
    for x in out:
        assert x['new_observation']['node'] not in x['chain_obs_nodes'], x['item']
        assert not ({q['panel_id'] for q in x['panels']} & set(x['chain_panel_ids'])), x['item']
    res = {'note': 'v2.9 Step 5. Next links from every compositional item.',
           'parents': sum(1 for v in S4['items_out'].values() if v['compositional']),
           'parents_with_a_next_link': len(per_item),
           'next_links': len(out), 'max_per_item': MAX_NEXT, 'dropped': dict(drops),
           'exclusion_check': 'passed: no next link reuses a node or panel from its own chain',
           'pairs_out': out}
    json.dump(res, open(R('results/v2p9/nextlink.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'pairs_out'}, indent=1))
    return res


if __name__ == '__main__': run()
