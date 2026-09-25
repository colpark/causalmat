"""pairs.py: v2.9 Step 0 -- every derived_input pair on the 24 non-pilot papers, free filters only.

  python3 -m trace_kit_v2p9.pairs

No model call. Same generator as v2.7, with the per-paper cap removed, because this run is a
production rehearsal: at 15,000 papers you make every item you can and test a sample, rather
than capping and testing everything.

Two free filters, in the order they cost nothing:

  exclusion   the new observation shares no node id and no panel id with the upstream item.
              This is the v2.7 rule and it is the whole reason a derived_input pair can need
              its input at all.

  upstream    the v2.7 widened "upstream ignored" flag, applied where it can be: a pair is
  ignored    dropped when v2.5 composed a join FROM this pair's upstream item INTO an item
              concluding this pair's target claim, and v2.7 Part C flagged that join as one
              where the downstream never used the upstream result. If the join that used this
              exact result for this exact claim was empty, the pair asks for the same thing
              again.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v3'))
sys.path.insert(0, R('trace_kit_v2p5'))
from support import claim_support  # noqa: E402
from items import panel_record, store_for, unmath  # noqa: E402

REL = {'causes', 'explains', 'supports'}
MAX_PANELS = 5


def concludes(it):
    return (it['claims'][1] if it['generator'] == 'spine_edge' and len(it['claims']) > 1
            else it['claims'][0])


def panels_of(node, store):
    out = []
    for pid in (node.get('panel_ids') or []):
        r = panel_record(store, pid) or {}
        c = r.get('crop')
        out.append({'panel_id': pid, 'suffix': pid.split('#')[-1],
                    'crop': c if c and os.path.exists(c) else None,
                    'figure': r.get('figure'),
                    'caption_span': ' '.join(unmath(r.get('span') or '').split()) or None})
    return [q for q in out if q['crop']]


def ignored_map():
    """(upstream item, claim) pairs whose v2.5 join into that claim was flagged upstream-ignored"""
    C = json.load(open(R('results/v2p7/partC.json')))['seams']
    P = json.load(open(R('results/v2p6/pruned.json')))
    D = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    V5 = {i['item']: i for i in json.load(open(R('results/v5/items.json')))['items']}
    out = set()
    for jn in P['joins']:
        k = f"{jn['from']}__{jn['to']}"
        if not (C.get(k) or {}).get('ignored'): continue
        dn = D.get(jn['to']) or V5.get(jn['to']) or {}
        for c in (dn.get('claims') or []):
            out.add((jn['from'], c))
    return out


def run():
    papers = json.load(open(R('results/v2p9/papers.json')))
    D = [i for i in json.load(open(R('results/v2p5/items.json')))['items']
         if i['generator'] != 'covariation' and i['paper'] in papers]
    IGN = ignored_map()
    pairs, drops = [], collections.Counter()
    why_none, seen = {}, set()
    for p in papers:
        gp = json.load(open(R('results/v3', p, 'stitch.json')))['graph']
        gr = json.load(open(R(gp))); N = {n['id']: n for n in gr['nodes']}
        store = store_for(R(gp))
        sup = claim_support(gr)
        obs_of = collections.defaultdict(set)
        for c, r in sup.items(): obs_of[c] |= set(r['via'])
        oe = collections.defaultdict(set)
        for e in gr['edges']:
            if e.get('rel') in REL: oe[e['src']].add(e['dst'])
        pits = [i for i in D if i['paper'] == p]
        n_before = 0
        for it in pits:
            used = {it['observation_a']['node'], it['observation_b']['node']}
            upans = {q.get('panel_id') for q in (it.get('panels') or []) if q.get('panel_id')}
            C = concludes(it)
            k = (it.get('key') or {})
            if not (k.get('proposition') or '').strip():
                drops['upstream item has no drafted key'] += 1; continue
            for tgt in sorted(oe.get(C, ())):
                for o in sorted(obs_of.get(tgt, ())):
                    n_before += 1
                    if o in used: drops['new obs is one the upstream used'] += 1; continue
                    node = N.get(o) or {}
                    if not node.get('panel_ids'): drops['new obs has no panels'] += 1; continue
                    pans = panels_of(node, store)
                    if not pans: drops['new obs panels have no usable crop'] += 1; continue
                    npans = {q.get('panel_id') for q in pans if q.get('panel_id')}
                    if npans & upans:
                        drops['new obs shares a panel with the upstream'] += 1; continue
                    if (it['item'], tgt) in IGN:
                        drops['v2.7 flagged this upstream as ignored into this claim'] += 1
                        continue
                    key = (it['item'], tgt)
                    if key in seen: drops['same (item, target claim) already taken'] += 1; continue
                    seen.add(key)
                    pairs.append({
                        'item': f"di_{it['item']}_{o}_{tgt}", 'paper': p,
                        'generator': 'derived_input',
                        'upstream_item': it['item'], 'claim_C': C, 'target_claim': tgt,
                        'input_result': (k.get('proposition') or '').strip(),
                        'input_limits': [str(x) for x in (k.get('limits') or [])],
                        'new_observation': {'node': o, 'text': (node.get('label') or '').strip(),
                                            'technique': node.get('technique')},
                        'panels': pans[:MAX_PANELS],
                        'upstream_obs_nodes': sorted(used),
                        'upstream_panel_ids': sorted(x for x in upans),
                        'upstream_panels': [q for q in (it.get('panels') or []) if q.get('crop')],
                        'edge': f'{C} -> {tgt}',
                    })
        if not any(x['paper'] == p for x in pairs):
            why_none[p] = ('no two-step item on this paper concludes a claim that points at '
                           'another claim with an unused, panel-backed observation'
                           if pits else 'no v2.5 two-step items survive on this paper')

    ids = [x['item'] for x in pairs]
    assert len(ids) == len(set(ids)), [k for k, n in collections.Counter(ids).items() if n > 1]
    for x in pairs:
        assert x['new_observation']['node'] not in x['upstream_obs_nodes'], x['item']
        assert not ({q['panel_id'] for q in x['panels']} & set(x['upstream_panel_ids'])), x['item']

    out = {'note': 'v2.9 Step 0. Every pair on the 24 non-pilot papers; free filters only.',
           'papers': len(papers), 'papers_with_pairs': len({x['paper'] for x in pairs}),
           'pairs': len(pairs), 'dropped': dict(drops),
           'papers_with_no_pairs': why_none,
           'per_paper': dict(collections.Counter(x['paper'] for x in pairs)),
           'exclusion_check': 'passed: asserted by node id and panel id on every pair',
           'pairs_out': pairs}
    json.dump(out, open(R('results/v2p9/pairs.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ('pairs_out', 'per_paper')}, indent=1))
    return out


if __name__ == '__main__': run()
