"""deeper.py: v2.10 Step 2 and 3 -- one more link on top of a surviving chain.

  python3 -m trace_kit_v2p10.deeper 4   depth 4 candidates from the depth 3 chains
  python3 -m trace_kit_v2p10.deeper 5   depth 5 candidates from the depth 4 chains

The rule that matters is the exclusion, and it gets stricter with every step: the new
observation must be unused by the WHOLE chain, checked by node id and by panel id against every
earlier link. At depth 4 that is four observations and all their panels; at depth 5, five. A
chain that re-reads its own first measurement at the end would look like it was building and
would only be going in circles, and the deeper it goes the easier that is to do by accident.

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
_sp = _ilu.spec_from_file_location('v2p5_items_d', R('trace_kit_v2p5', 'items.py'))
_v25 = _ilu.module_from_spec(_sp); _sp.loader.exec_module(_v25)
store_for = _v25.store_for

MAX_NEXT = 2


def chain_of(leaf, P2, NL3, NL4, D5):
    """every (observation node, panel ids) the chain has already spent, and its step ids"""
    steps, node, pans = [], set(), set()
    cur = leaf
    while True:
        rec = NL4.get(cur) or NL3.get(cur) or P2.get(cur)
        if rec is None: break
        steps.append(cur)
        node.add(rec['new_observation']['node'])
        pans |= {q.get('panel_id') for q in rec['panels'] if q.get('panel_id')}
        nxt = rec.get('parent_item') or rec.get('upstream_item')
        if nxt in D5:                      # the v2.5 item at the root
            up = D5[nxt]
            steps.append(nxt)
            node |= {up['observation_a']['node'], up['observation_b']['node']}
            pans |= {q.get('panel_id') for q in (up.get('panels') or []) if q.get('panel_id')}
            break
        cur = nxt
    return list(reversed(steps)), node, pans


def run(depth):
    PU = json.load(open(R('results/v2p10/purge.json')))
    P2 = {x['item']: x for x in json.load(open(R('results/v2p9/pairs.json')))['pairs_out']}
    NL3 = {x['item']: x for x in json.load(open(R('results/v2p9/nextlink.json')))['pairs_out']}
    D5 = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    if depth == 4:
        leaves = list(PU['live_depth3'])
        KEY = json.load(open(R('results/v2p9/keys_nl.json')))
        NL4 = {}
    else:
        S = json.load(open(R('results/v2p10/step4_d4.json')))
        # a depth 4 link only becomes a depth 5 leaf if it passed; its parents already had to
        # pass to be a depth 3 chain, so a passing link here means all three links below it held
        leaves = [k for k, v in S['items_out'].items() if v['compositional']]
        KEY = json.load(open(R('results/v2p10/keys_d4.json')))
        NL4 = {x['item']: x for x in
               json.load(open(R('results/v2p10/deeper_d4.json')))['pairs_out']}

    out, drops = [], collections.Counter()
    per = collections.Counter()
    for leaf in leaves:
        rec = NL4.get(leaf) or NL3[leaf]
        paper = rec['paper']
        gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
        gr = json.load(open(R(gp))); N = {n['id']: n for n in gr['nodes']}
        store = store_for(R(gp)); sup = claim_support(gr)
        obs_of = collections.defaultdict(set)
        for c, r in sup.items(): obs_of[c] |= set(r['via'])
        oe = collections.defaultdict(set)
        for e in gr['edges']:
            if e.get('rel') in REL: oe[e['src']].add(e['dst'])
        steps, used_nodes, used_pans = chain_of(leaf, P2, NL3, NL4, D5)
        T = rec['target_claim']
        k = KEY.get(leaf) or {}
        if not (k.get('proposition') or '').strip():
            drops['leaf has no drafted key'] += 1; continue
        for tgt in sorted(oe.get(T, ())):
            if per[leaf] >= MAX_NEXT: drops['over the 2-per-chain cap'] += 1; continue
            for o in sorted(obs_of.get(tgt, ())):
                if per[leaf] >= MAX_NEXT: break
                if o in used_nodes:
                    drops['observation already used in the chain'] += 1; continue
                node = N.get(o) or {}
                if not node.get('panel_ids'): drops['no panels'] += 1; continue
                pans = panels_of(node, store)
                if not pans: drops['no usable crop'] += 1; continue
                np_ = {q['panel_id'] for q in pans if q.get('panel_id')}
                if np_ & used_pans:
                    drops['panel already used in the chain'] += 1; continue
                per[leaf] += 1
                out.append({
                    'item': f'd{depth}_{leaf}_{o}_{tgt}', 'paper': paper,
                    'generator': 'derived_input', 'depth': depth,
                    'parent_item': leaf, 'upstream_item': leaf,
                    'chain': steps, 'claim_C': T, 'target_claim': tgt,
                    'input_result': (k.get('proposition') or '').strip(),
                    'input_limits': [str(t) for t in (k.get('limits') or [])],
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
    res = {'note': f'v2.10 depth {depth} candidates.', 'depth': depth,
           'leaves': len(leaves), 'leaves_with_a_link': len(per),
           'candidates': len(out), 'max_per_chain': MAX_NEXT, 'dropped': dict(drops),
           'exclusion_check': f'passed: no depth {depth} link reuses a node or panel from any '
                              f'earlier step of its own chain',
           'pairs_out': out}
    json.dump(res, open(R(f'results/v2p10/deeper_d{depth}.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'pairs_out'}, indent=1))
    return res


if __name__ == '__main__': run(int(sys.argv[1]))
