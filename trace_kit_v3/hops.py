"""hops.py: the causal hops of one paper, from its MatMech record.

  python3 trace_kit_v3/hops.py <paper>

Writes results/v3/<paper>/hops.json. From MatMech we take ONLY: the hop structure (stage type), the
effect-to-cause chaining, the figure links, the experiment techniques, and the imported-knowledge
list. The cause and effect spans are kept in a separate field marked `_matmech_span_DO_NOT_PROMPT`
so a leak into a solver prompt is greppable, and the reasoning-chain sentences are never read.
"""
import json, os, re, sys, difflib
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()


def paraphrase(text, n=14):
    """a short neutral description of an imported-knowledge item: its head words, not its claim"""
    w = re.sub(r'\s+', ' ', (text or '').strip()).split()
    return ' '.join(w[:n]) + ('…' if len(w) > n else '')


def figures_of(hop, doi_dir):
    """packet-style figure ids for the images this hop links, by position in data.json image_info"""
    d = json.load(open(os.path.join(doi_dir, 'data.json')))
    order = {im.get('image_path'): i for i, im in enumerate(d.get('image_info') or [], 1)}
    out = []
    for im in hop.get('images') or []:
        p = im.get('image_path')
        if p in order: out.append(f"F{order[p]}")
        elif p: out.append(os.path.basename(p))
    return list(dict.fromkeys(out))


def main(paper):
    j, _, doi = paper.partition('__')
    dd = os.path.join(ROOT, 'matmech', j, doi)
    d = json.load(open(os.path.join(dd, 'data.json')))
    ms = d.get('mechanism') or []
    hops = []
    for i, m in enumerate(ms, 1):
        ek = m.get('external_knowledge') or []
        if isinstance(ek, str): ek = [ek] if ek.strip() else []
        exp = m.get('experiment') or {}
        techs = [t.strip() for t in re.split(r'[,/;]| and ', exp.get('type') or '') if t.strip()]
        hops.append({
            'id': f"M{i}", 'stage_type': m.get('link'),
            'figures': figures_of(m, dd),
            'techniques': techs,
            'experiment_name': exp.get('name'),
            'knowledge_imported': {'count': len(ek), 'items': [paraphrase(x if isinstance(x, str) else json.dumps(x)) for x in ek]},
            'next': None, 'chain_basis': None,
            '_matmech_span_DO_NOT_PROMPT': {'cause': m.get('cause'), 'effect': m.get('effect')},
        })
    # chain: next = the hop whose cause matches this hop's effect
    for a in hops:
        ea = norm(a['_matmech_span_DO_NOT_PROMPT']['effect'])
        if not ea: continue
        best, score = None, 0.0
        for b in hops:
            if b is a: continue
            cb = norm(b['_matmech_span_DO_NOT_PROMPT']['cause'])
            if not cb: continue
            s = 1.0 if ea == cb else difflib.SequenceMatcher(None, ea, cb).ratio()
            if s > score: best, score = b, s
        if score >= 0.90:
            a['next'] = best['id']
            a['chain_basis'] = 'exact string identity' if score == 1.0 else f'string similarity {score:.2f}'
            a['chain_strength'] = 'span'
    # Secondary basis: the stage types chain even where the spans do not. "Processing -> Structure"
    # followed by "Structure -> Property" is a causal hop by MatMech's own stage vocabulary, and
    # without it three of the five papers yield no multi-hop trace at all. Marked distinctly so a
    # span-chained link is never confused with a stage-chained one.
    STAGE = {'processing': 0, 'structure': 1, 'property': 2, 'properties': 2, 'performance': 3}
    def ends(h):
        t = (h.get('stage_type') or '').replace('->', '\u2192')
        parts = [x.strip().lower() for x in t.split('\u2192')]
        return (parts[0], parts[-1]) if len(parts) >= 2 else (None, None)
    for a in hops:
        if a['next']: continue
        _, ae = ends(a)
        if ae is None: continue
        cands = [b for b in hops if b is not a and ends(b)[0] == ae]
        if len(cands) == 1:
            a['next'] = cands[0]['id']
            a['chain_basis'] = f"stage type: {ae} is this hop's effect stage and the next hop's cause stage"
            a['chain_strength'] = 'stage'
        elif len(cands) > 1:
            a['chain_candidates'] = [b['id'] for b in cands]
    out = os.path.join(ROOT, 'results/v3', paper); os.makedirs(out, exist_ok=True)
    chained = sum(1 for h in hops if h['next'])
    by_span = sum(1 for h in hops if h.get('chain_strength') == 'span')
    by_stage = sum(1 for h in hops if h.get('chain_strength') == 'stage')
    orphans = [h['id'] for h in hops if not h['next'] and not any(x['next'] == h['id'] for x in hops)]
    obj = {'paper': paper, 'doi': d.get('doi'), 'title': d.get('title'),
           'casual_chain': d.get('casual_chain'), 'hops': hops,
           'counts': {'hops': len(hops), 'chained_pairs': chained, 'chained_by_span': by_span,
                      'chained_by_stage': by_stage, 'orphans': len(orphans), 'orphan_ids': orphans},
           'note': 'Every verdict is model against model. MatMech cause/effect spans are kept only under '
                   '_matmech_span_DO_NOT_PROMPT and must never reach a solver prompt.'}
    json.dump(obj, open(os.path.join(out, 'hops.json'), 'w'), indent=1)
    print(f"{paper[:44]:44s} {len(hops)} hops, {chained} chained ({by_span} by span, {by_stage} by stage), {len(orphans)} orphan")
    for h in hops:
        print(f"    {h['id']} {str(h['stage_type']):26s} figs={h['figures']} tech={h['techniques'][:4]} "
              f"knw={h['knowledge_imported']['count']}" + (f"  -> {h['next']} ({h['chain_basis']})" if h['next'] else ""))
    return obj


if __name__ == '__main__': main(sys.argv[1])
