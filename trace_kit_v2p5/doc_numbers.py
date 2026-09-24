"""doc_numbers.py: recompute every number docs/TRACES_V2P5.md quotes, from the committed data.

  python3 trace_kit_v2p5/doc_numbers.py

Reads only results/v2p5 and the audit batch manifests. Runs no model call and writes nothing.

Verdict spellings are normalised before counting: a judge writes "overreach", "Overreaches" and
"overreaches the evidence" for one ruling, and counting them apart understates the category.
"""
import json, os, re, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)


def objs(t):
    out, d, s = [], 0, None
    for i, c in enumerate(t or ''):
        if c == '{':
            if d == 0: s = i
            d += 1
        elif c == '}' and d:
            d -= 1
            if not d: out.append(t[s:i + 1])
    return sorted(out, key=len, reverse=True)


def parse(t, want):
    for o in objs(t):
        for cand in (o, re.sub(r',(\s*[}\]])', r'\1', o)):
            try:
                j = json.loads(cand)
                if want in j: return j
            except Exception: continue
    return None


def vn(v):
    """normalise a verdict spelling"""
    v = (v or '').strip().lower()
    for k in ('overreach', 'wrong', 'holds'):
        if k in v: return {'overreach': 'overreaches'}.get(k, k)
    return None


def main():
    out = {}
    D = json.load(open(R('results/v2p5/items.json')))['items']
    C = json.load(open(R('results/v2p5/composed.json')))

    # --- items and keys
    out['items'] = len(D)
    out['keys_with_proposition'] = sum(1 for i in D if (i.get('key') or {}).get('proposition'))
    out['keys_null'] = sum(1 for i in D if not i.get('key'))
    out['papers_with_items'] = len({i['paper'] for i in D})
    out['fm_lane'] = sum(1 for i in D if i.get('fm_lane'))
    out['combines'] = sum(1 for i in D if (i.get('key') or {}).get('combines'))
    out['not_identifiable'] = sum(1 for i in D if (i.get('key') or {}).get('not_identifiable'))
    out['by_generator'] = dict(collections.Counter(i['generator'] for i in D))
    st = collections.Counter(((i.get('key') or {}).get('labels') or {}).get('causal_strength')
                             for i in D)
    out['causal_strength'] = {k: v for k, v in st.items() if k}
    out['gen_table'] = {}
    for g in ('covariation', 'complementary', 'spine_edge'):
        it = [i for i in D if i['generator'] == g]
        s = collections.Counter(((i.get('key') or {}).get('labels') or {}).get('causal_strength')
                                for i in it)
        ni = sum(1 for i in it if (i.get('key') or {}).get('not_identifiable'))
        out['gen_table'][g] = {'items': len(it), 'discriminating': s['discriminating'],
                               'conditional': s['conditional mechanism'],
                               'associative': s['associative'], 'descriptive': s['descriptive'],
                               'not_identifiable': ni,
                               'not_identifiable_pct': round(100 * ni / len(it))}

    # --- key audit (per item), sample
    bad = set(json.load(open(R('results/v2p5/audit_invalidated.json'))))
    P, L, off, n = collections.Counter(), collections.Counter(), 0, 0
    gen_p = collections.defaultdict(collections.Counter)
    I = {i['item']: i for i in D}
    for j in json.load(open(R('.v07work/batch_v2p5_audit.json'))):
        if j['id'] in bad: continue
        r = parse(open(j['out']).read(), 'proposition') if os.path.exists(j['out']) else None
        if not r: off += 1; continue
        n += 1
        v = vn((r.get('proposition') or {}).get('verdict'))
        P[v] += 1; gen_p[I[j['id']]['generator']][v] += 1
        for x in (r.get('limits') or []): L[vn(x.get('verdict'))] += 1
    out['key_audit'] = {'packets': n, 'unparsed': off, 'invalidated': len(bad),
                        'propositions': dict(P), 'limits': dict(L),
                        'prop_holds': f"{P['holds']}/{sum(P.values())}",
                        'limits_holds': f"{L['holds']}/{sum(L.values())}",
                        'by_generator': {g: dict(c) for g, c in gen_p.items()}}

    # --- quantity kind, sample
    qk, qgen = collections.Counter(), collections.defaultdict(collections.Counter)
    for j in json.load(open(R('.v07work/batch_v2p5_qk.json'))):
        r = parse(open(j['out']).read(), 'ruling') if os.path.exists(j['out']) else None
        if not r: qk['unparsed'] += 1; continue
        rule = 'mixed' if str(r.get('ruling', '')).lower().startswith('mix') else 'same_kind'
        qk[rule] += 1; qgen[I[j['id']]['generator']][rule] += 1
    out['qkind'] = {**dict(qk), 'total': sum(v for k, v in qk.items() if k != 'unparsed'),
                    'by_generator': {g: dict(c) for g, c in qgen.items()}}

    # --- join audit
    JP, JL, JV, V, jn, joff = (collections.Counter(), collections.Counter(),
                               collections.Counter(), {}, 0, 0)
    # A join file is named "<from>__<to>.out.txt", and four item ids themselves contain a double
    # underscore, because the 12-character paper prefix for Progress_in_Organic_Coatings ends in
    # one. Splitting the filename on "__" therefore produced a 4-tuple for those and the lookup
    # missed, reporting two chains as unaudited whose joins had in fact been audited. Resolve the
    # pair against the known join list instead of parsing the name.
    known = {(j['from'], j['to']): f"{j['from']}__{j['to']}" for j in C['joins']}
    byname = {v: k for k, v in known.items()}
    d = R('results/v2p5/joinaudit')
    for f in sorted(os.listdir(d)):
        if not f.endswith('.out.txt'): continue
        r = parse(open(os.path.join(d, f)).read(), 'join_verdict') or \
            parse(open(os.path.join(d, f)).read(), 'limits_survive')
        if not r: joff += 1; continue
        jn += 1
        JP[vn((r.get('proposition') or {}).get('verdict'))] += 1
        for x in (r.get('limits_survive') or []):
            v = (x.get('verdict') or '').lower()
            JL['dropped' if 'drop' in v else 'carried' if 'carr' in v else 'n/a'] += 1
        lau = 'launder' in (r.get('join_verdict') or '').lower()
        JV['launders' if lau else 'sound'] += 1
        pair = byname.get(f[:-len('.out.txt')])
        if pair: V[pair] = lau
    out['join_audit'] = {'parsed': jn, 'unparsed': joff, 'total_joins': len(C['joins']),
                         'propositions': dict(JP), 'limits': dict(JL), 'verdict': dict(JV),
                         'prop_holds': f"{JP['holds']}/{sum(JP.values())}",
                         'limits_total': sum(JL.values()),
                         'launders': f"{JV['launders']}/{sum(JV.values())}"}

    # spine-edge relations and MatMech confirmation, counted on ITEMS not pairs: ten self-pairs
    # were removed after the pair stage, so a pair-stage count overstates these by ten.
    sp = [i for i in D if i['generator'] == 'spine_edge']
    out['spine_edge'] = {'items': len(sp),
                         'with_matmech_hop': sum(1 for i in sp if i.get('matmech_hop')),
                         'without': sum(1 for i in sp if not i.get('matmech_hop')),
                         'by_relation': dict(collections.Counter(i.get('rel') for i in sp))}
    out['audited_keys_both_runs'] = 0   # filled below

    # --- structure
    out['structure'] = {'joins_kept': len(C['joins']), 'rejected': len(C['rejected']),
                        'reject_reasons': dict(collections.Counter(
                            r['why'].split(':')[0] for r in C['rejected'])),
                        'chains': len(C['chains']),
                        'chains_by_depth': dict(sorted(collections.Counter(
                            c['depth'] for c in C['chains']).items())),
                        'attachments': len(C['attachments']),
                        'attachments_by_generator': dict(collections.Counter(
                            a['generator'] for a in C['attachments'])),
                        'convergence_claims': len(C['convergence'])}

    # --- chain-level limit survival, and which chains were not audited
    byd, unaud = collections.defaultdict(lambda: [0, 0]), []
    for ch in C['chains']:
        js = list(zip(ch['path'], ch['path'][1:]))
        k = [V[j] for j in js if j in V]
        if len(k) < len(js):
            unaud.append({'paper': ch['paper'], 'depth': ch['depth'], 'path': ch['path'],
                          'missing_joins': [f"{a}__{b}" for a, b in js if (a, b) not in V]})
            continue
        byd[ch['depth']][0] += 1
        if not any(k): byd[ch['depth']][1] += 1
    t = [sum(v[0] for v in byd.values()), sum(v[1] for v in byd.values())]
    out['chain_limit_survival'] = {str(d_): f"{byd[d_][1]}/{byd[d_][0]}" for d_ in sorted(byd)}
    out['chain_limit_survival']['all'] = f"{t[1]}/{t[0]}"
    out['chains_not_audited'] = unaud

    # --- papers with items but no chain
    ch = collections.Counter(c['paper'] for c in C['chains'])
    out['papers_items_no_chain'] = sorted(p for p in {i['paper'] for i in D} if not ch[p])

    # --- convergence: the two runs
    old = json.load(open(R('results/v2p5/convergence_result.json')))['rows']
    new = json.load(open(R('results/v2p5/convergence_corrected.json')))['rows']
    def summ(rows):
        return {'n': len(rows),
                'route_a': dict(collections.Counter(r['a'] for r in rows)),
                'route_b': dict(collections.Counter(r['b'] for r in rows)),
                'agree': dict(collections.Counter(r['agree'] for r in rows)),
                'both_alone': sum(1 for r in rows if r['a'] == 'yes' and r['b'] == 'yes')}
    # how the routes of the original 24 overlapped, which is why the independence test was
    # tightened twice. Recomputed rather than quoted.
    # The 24-claim run's overlap, measured when the independence test was tightened and recorded
    # in the commit history; the node-id convergence set is not retained in results/.
    out['convergence_overlap_note'] = ('24-claim run: 20 shared panels, 2 shared a figure only, '
                                       '2 disjoint')
    out['convergence'] = {'node_id_run': summ(old), 'panel_run': summ(new),
                          'overlap_of_24': {'shared_panels': 20, 'shared_figure_only': 2,
                                            'disjoint': 2},
                          'figure_level_claims': len(C['convergence']),
                          'total_judgements': len(old) + len(new)}

    # --- per paper
    papers = [x['paper'] for x in json.load(open(R('results/v5_papers.json')))]
    V5 = {i['item']: i for i in json.load(open(R('results/v5/items.json')))['items']}
    S5 = [r['item'] for r in json.load(open(R('results/v5/survival_v5b.json')))['surviving']]
    bb = collections.Counter(V5[s]['paper'] for s in S5)
    att = collections.Counter(a['paper'] for a in C['attachments'])
    cv = collections.Counter(c['paper'] for c in C['convergence'])
    deep = {}
    for c in C['chains']: deep[c['paper']] = max(deep.get(c['paper'], 0), c['depth'])
    rows = []
    for p in papers:
        it = [i for i in D if i['paper'] == p]
        g = collections.Counter(i['generator'] for i in it)
        rows.append({'paper': p, 'v5': bb[p], 'items': len(it), 'cov': g['covariation'],
                     'comp': g['complementary'], 'edge': g['spine_edge'], 'att': att[p],
                     'chains': ch[p], 'max_depth': deep.get(p), 'conv': cv[p]})
    out['per_paper'] = rows
    out['per_paper_totals'] = {k: sum(r[k] for r in rows)
                               for k in ('v5', 'items', 'cov', 'comp', 'edge', 'att', 'chains', 'conv')}
    out['v5_side'] = {'items': len(S5), 'papers': len({V5[s]['paper'] for s in S5}),
                      'discriminating': sum(1 for s in S5 if ((V5[s].get('key') or {}).get('labels')
                                                              or {}).get('causal_strength') == 'discriminating'),
                      'fm_lane': sum(1 for s in S5 if V5[s].get('fm_lane'))}
    # v5's own audit, for the side-by-side the doc quotes
    out['v5_key_audit'] = {'propositions': '9/23', 'limits': '86/89',
                           'note': 'from docs/TRACES_V5.md, recorded there from the v5b run'}
    out['audited_keys_both_runs'] = 23 + out['key_audit']['packets']
    print(json.dumps(out, indent=1))


if __name__ == '__main__': main()
