"""stitch.py: decompose each hop's effect into our spine claims, and attach panel evidence.

  python3 trace_kit_v3/stitch.py <paper>

Matching is lexical (TF-IDF cosine over character and word n-grams), which is the brief's
"embedding match" option. It needs no new agent and no restart, and every score is recorded so a
weak match is visible rather than asserted. The MatMech effect span is used HERE, for matching only;
it never reaches a solver prompt.

Writes results/v3/<paper>/stitch.json and appends to results/v3/unattached.jsonl.
"""
import json, os, re, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normalize import fold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ORACLE = {'ECHEM', 'THERMAL', 'MECH', 'TRANSPORT', 'ASSAY', 'BIO', 'PHYS', 'CHROM', 'PROFILOMETRY', 'TGA'}
MATCH_MIN = 0.12          # below this a claim is not treated as part of the hop's effect

ORACLE = {'ECHEM', 'THERMAL', 'MECH', 'TRANSPORT', 'ASSAY', 'BIO', 'PHYS', 'CHROM', 'PROFILOMETRY', 'TGA'}
MATCH_MIN = 0.12          # below this a claim is not treated as part of the hop's effect

SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')
GREEK = {'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta', 'ε': 'epsilon', 'θ': 'theta',
         'λ': 'lambda', 'μ': 'mu', 'σ': 'sigma', 'τ': 'tau', 'ω': 'omega', 'Α': 'alpha',
         'Β': 'beta', 'Γ': 'gamma', 'Δ': 'delta', 'Θ': 'theta', 'Σ': 'sigma', 'Ω': 'omega'}


def fam(t):
    if isinstance(t, list): t = t[0] if t else None
    return (t or '').split(':')[0].upper()


def graph_for(paper):
    for d in ('graphs_v07', 'graphs_v06b'):
        p = os.path.join(ROOT, 'taxonomy', d, paper + '.json')
        if os.path.exists(p): return p, json.load(open(p))
    raise FileNotFoundError(paper)


def main(paper):
    out = os.path.join(ROOT, 'results/v3', paper)
    hops = json.load(open(os.path.join(out, 'hops.json')))
    gp, g = graph_for(paper)
    N = {n['id']: n for n in g['nodes']}
    # our spine claims: the things a hop's effect could decompose into
    claims = [n for n in g['nodes'] if n.get('spine') and not (n.get('type') or '').startswith('OBS')]
    if not claims: claims = [n for n in g['nodes'] if not (n.get('type') or '').startswith('OBS')]
    # support comes from support.py: a direct `evidences` edge out of an observation with panels.
    # `qualifies` / `contrasts` / `rules_out` are caveats and are recorded separately, not counted.
    ev_by_claim, caveat_by_claim = {}, {}
    for e in g['edges']:
        s, t, r = e.get('src'), e.get('dst'), e.get('rel')
        if s not in N or t not in N: continue
        if not (N[s].get('panel_ids') or N[s].get('figs')): continue
        if r == 'evidences':
            ev_by_claim.setdefault(t, []).append((s, r))
        elif r in ('qualifies', 'contrasts', 'rules_out'):
            caveat_by_claim.setdefault(t, []).append((s, r))

    texts = [fold(c.get('label')) for c in claims]
    effects = [fold(h['_matmech_span_DO_NOT_PROMPT']['effect']) for h in hops['hops']]
    vw = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), sublinear_tf=True, min_df=1)
    vc = TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5), sublinear_tf=True, min_df=1)
    Mw = vw.fit_transform(texts + effects); Mc = vc.fit_transform(texts + effects)
    sw = cosine_similarity(Mw[len(texts):], Mw[:len(texts)])
    sc_ = cosine_similarity(Mc[len(texts):], Mc[:len(texts)])
    sim = 0.5 * sw + 0.5 * sc_          # words catch shared terms, chars catch formula variants

    rows, unatt = [], []
    for hi, h in enumerate(hops['hops']):
        order = sim[hi].argsort()[::-1]
        subs = []
        for ci in order[:5]:
            sc = float(sim[hi][ci])
            if sc < MATCH_MIN: continue
            c = claims[ci]
            evs = []
            for nid, rel in ev_by_claim.get(c['id'], []):
                n = N[nid]; tech = n.get('attrs', {}).get('technique')
                evs.append({'node': nid, 'relation': rel, 'technique': tech, 'family': fam(tech),
                            'panel_ids': n.get('panel_ids') or [], 'figs': n.get('figs') or [],
                            'image_support': n.get('image_support'),
                            'read_from': n.get('attrs', {}).get('read_from'),
                            'delivery': 'oracle' if fam(tech) in ORACLE else 'crop',
                            'observation': n.get('label')})
            cavs = [{'node': nid, 'relation': rel, 'observation': N[nid].get('label'),
                     'panel_ids': N[nid].get('panel_ids') or []}
                    for nid, rel in caveat_by_claim.get(c['id'], [])]
            subs.append({'claim': c['id'], 'claim_type': c.get('type'), 'claim_text': c.get('label'),
                         'match_score': round(sc, 3), 'n_evidence': len(evs), 'evidence': evs,
                         'n_caveats': len(cavs), 'caveats': cavs})
        n_ev = sum(s['n_evidence'] for s in subs)
        mods = sorted({e['family'] for s in subs for e in s['evidence'] if e['family']})
        rows.append({'hop': h['id'], 'stage_type': h['stage_type'], 'next': h['next'],
                     'chain_strength': h.get('chain_strength'),
                     'matmech_figures': h['figures'], 'matmech_techniques': h['techniques'],
                     'knowledge_imported': h['knowledge_imported']['count'],
                     'sub_claims': subs, 'n_sub_claims': len(subs), 'n_evidence': n_ev,
                     'modalities': mods})
        if n_ev == 0:
            ours = sorted({p.split('#')[1].split('a')[0] if '#' in p else p
                           for c in claims for nid, _ in (ev_by_claim.get(c['id'], [])
                                                          + caveat_by_claim.get(c['id'], []))
                           for p in (N[nid].get('panel_ids') or N[nid].get('figs') or [])})
            kind = ('coverage gap: our graph cites figures, so the hop names figures we did not read'
                    if ours else 'no figure-backed evidence anywhere in our graph')
            if not h['figures']:
                kind = 'MatMech invention: the hop links no figure at all'
            unatt.append({'paper': paper, 'hop': h['id'], 'stage_type': h['stage_type'],
                          'matmech_figures': h['figures'], 'our_figures': ours[:20],
                          'best_match': subs[0]['match_score'] if subs else None,
                          'appears_to_be': kind})
    obj = {'paper': paper, 'graph': os.path.relpath(gp, ROOT), 'spine_claims': len(claims),
           'match': 'TF-IDF cosine, mean of word 1-2 grams and char_wb 3-5 grams, over text '
                    'normalised for Unicode subscripts and Greek; MATCH_MIN %.2f' % MATCH_MIN,
           'hops': rows,
           'counts': {'hops': len(rows), 'hops_with_evidence': sum(1 for r in rows if r['n_evidence']),
                      'hops_without_evidence': sum(1 for r in rows if not r['n_evidence']),
                      'evidence_nodes': sum(r['n_evidence'] for r in rows)},
           'note': 'Every verdict is model against model. The MatMech effect span was used for matching '
                   'only and never reaches a solver prompt.'}
    json.dump(obj, open(os.path.join(out, 'stitch.json'), 'w'), indent=1)
    if unatt:
        keep = [l for l in open(os.path.join(ROOT, 'results/v3/unattached.jsonl'))
                if json.loads(l).get('paper') != paper] \
            if os.path.exists(os.path.join(ROOT, 'results/v3/unattached.jsonl')) else []
        open(os.path.join(ROOT, 'results/v3/unattached.jsonl'), 'w').writelines(keep)
        with open(os.path.join(ROOT, 'results/v3/unattached.jsonl'), 'a') as f:
            for u in unatt: f.write(json.dumps(u) + '\n')
    print(f"{paper[:44]:44s} {obj['counts']['hops_with_evidence']}/{len(rows)} hops with evidence, "
          f"{obj['counts']['evidence_nodes']} evidence nodes")
    for r in rows:
        top = r['sub_claims'][0] if r['sub_claims'] else None
        print(f"    {r['hop']} {str(r['stage_type'])[:24]:24s} subs={r['n_sub_claims']} ev={r['n_evidence']:2d} "
              f"mods={r['modalities']}" + (f"  top={top['claim']}@{top['match_score']}" if top else "  NO MATCH"))
    return obj


if __name__ == '__main__': main(sys.argv[1])
