"""support.py: the one place v3 derives claim-level support.

A claim's support is NOT read off the claim node's `image_support` field. Three of the five graphs
barely set it -- Acta Materialia 0 of 30 claims, Rare Metals 0 of 19, Biomaterials 1 of 31 -- while
storing the evidence on OBS nodes instead. Reading the field measures where a graph happens to keep
support, not whether the paper shows the thing.

Instead: a claim is supported when an observation node with panels points at it through a direct
`evidences` edge. **One step, and only `evidences`.** No paths through intermediate claims, and not
`qualifies` / `contrasts` / `rules_out`, which are caveats rather than support.

Every verdict is model against model.
"""
RANK = {'shown': 3, 'partial': 2, 'contradicts': 1}


def claim_support(g):
    """{claim_id: {'level', 'panels', 'via'}} from direct `evidences` edges out of OBS nodes."""
    N = {n['id']: n for n in g['nodes']}
    out = {}
    for e in g['edges']:
        if e.get('rel') != 'evidences': continue
        s, t = e.get('src'), e.get('dst')
        src, dst = N.get(s), N.get(t)
        if not src or not dst: continue
        if not (src.get('type') or '').startswith('OBS'): continue
        pans = src.get('panel_ids') or []
        if not pans: continue
        r = out.setdefault(t, {'level': None, 'panels': [], 'via': []})
        r['via'].append(s)
        r['panels'] += [p for p in pans if p not in r['panels']]
        lv = src.get('image_support')
        if RANK.get(lv, 0) > RANK.get(r['level'], 0): r['level'] = lv
    return out


def supported(sup, cid, levels=('shown', 'partial')):
    r = sup.get(cid)
    return bool(r and r['level'] in levels and r['panels'])
