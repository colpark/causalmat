"""chain.py: build one support chain from a claim in an argument graph.

  python3 trace_kit_v2/chain.py <case_id>   (reads results/v2/case_selection.json)

Plan sections 1, 2, 4, 5. One step per figure-backed evidence node, in the paper's argument order.
Ground truth per step is the node's image_support plus the edge relation; the closing label is the
claim's own support profile. Writes results/v2/cases/<paper>/<CLAIM>/case.json.
"""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cut_traces import store_for, panel_record, unmath, fig_preamble
import annotate

# plan section 4: only these are served as text; everything else hands over the real data
ORACLE = {'ECHEM', 'THERMAL', 'MECH', 'TRANSPORT', 'ASSAY', 'BIO', 'PHYS', 'CHROM', 'PROFILOMETRY'}
FM_LANE = {'SEM', 'TEM', 'STEM', 'XRD', 'XAS', 'ATOM', 'EBSD', 'AFM', 'CT', 'SAXS', 'LEED'}
# what a step tests (plan section 4, last bullet)
TESTS = {'inspect_local_feature': 'perception', 'measure_feature_metric': 'perception',
         'read_trend': 'perception', 'read_distribution_statistics': 'perception',
         'compare_across_conditions': 'selection', 'assign_features': 'selection',
         'overlay_model_on_data': 'integration', 'cross_check_consistency': 'integration',
         'convert_to_quantity': 'integration'}

def fam(t):
    if isinstance(t, list): t = t[0] if t else None
    return (t or '').split(':')[0].upper()


def build(case):
    P, claim = case['paper'], case['claim']
    gp = os.path.join(ROOT, 'taxonomy', case['graphs'], P + '.json')
    g = json.load(open(gp)); N = {n['id']: n for n in g['nodes']}
    st = store_for(gp)
    order = [n['id'] for n in g['nodes']]                      # the paper's argument order
    inc = [(e['src'], e['rel'], e.get('mm_op')) for e in g['edges'] if e['dst'] == claim]
    ev = [(s, r, op) for s, r, op in inc if s in case['evidence']]
    ev.sort(key=lambda x: order.index(x[0]))

    steps, dropped = [], []
    for i, (nid, rel, op) in enumerate(ev, 1):
        n = N[nid]; tech = n.get('attrs', {}).get('technique'); f = fam(tech)
        pids = list(dict.fromkeys(n.get('panel_ids') or []))
        delivery = 'oracle' if f in ORACLE else 'crop'
        panels = []
        for pid in pids:
            r = panel_record(st, pid) or {}
            crop = r.get('crop')
            toks = (r.get('ocr') or {}).get('tokens') or []
            sp = annotate.split(crop, toks) if crop and os.path.exists(crop) else {'ok': False, 'method': 'none', 'why': 'panel id does not resolve to a crop', 'regions': [], 'coverage': 0.0}
            panels.append({'panel_id': pid, 'suffix': pid.split('#')[1],
                           'crop': crop if crop and os.path.exists(crop) else None,
                           'figure': r.get('figure'),
                           'caption_span': ' '.join(unmath(r.get('span') or '').split()) or None,
                           'ocr_tokens': len(toks),
                           'split_ok': sp['ok'], 'split_method': sp['method'],
                           'split_coverage': round(sp.get('coverage', 0.0), 4),
                           'n_regions': len(sp.get('regions') or []),
                           # ocr_boxes catches text only; the plan forbids hiding words while arrows stay
                           'hiding_compliant': sp['ok'] and sp['method'] == 'saturation',
                           'split_why': sp.get('why')})
        if delivery == 'crop' and not any(p['crop'] for p in panels):
            dropped.append({'node': nid, 'technique': tech, 'panel_ids': pids,
                            'reason': 'no crop resolves for any cited panel; cannot hand the data over'})
            continue
        steps.append({'step': len(steps) + 1, 'node': nid, 'relation': rel, 'mm_op': op,
                      'technique': tech, 'family': f, 'delivery': delivery,
                      'tests': TESTS.get(op, 'integration'),
                      'lane': 'fm' if f in FM_LANE else ('oracle' if f in ORACLE else 'other'),
                      # the plan: ground truth is image_support PLUS the edge relation. A node entering by
                      # qualifies/contrasts is a caveat on the claim, not support for it: the data may be
                      # plainly shown and still cut against what the claim asserts.
                      'expected_support': ('contradicts' if n.get('image_support') == 'contradicts'
                                           else 'partial' if n.get('image_support') in ('shown', 'partial')
                                           else 'not addressed') if rel in ('qualifies', 'contrasts')
                                          else (n.get('image_support') or 'not addressed'),
                      'support_basis': (f"{n.get('image_support')} in the panel, entering by a {rel} edge: a caveat on the claim"
                                        if rel in ('qualifies', 'contrasts') else f"image_support {n.get('image_support')}"),
                      'observation': n.get('label'),
                      'read_from': n.get('attrs', {}).get('read_from'),
                      'requires_unseen': n.get('attrs', {}).get('requires_unseen') or [],
                      'image_note': n.get('attrs', {}).get('image_note'),
                      'panels': panels})

    # closing profile: the claim's own support, and what no panel shows
    sups = [s['expected_support'] for s in steps]
    claim_unseen = N[claim].get('attrs', {}).get('requires_unseen') or []
    missing = list(dict.fromkeys(claim_unseen + [u for s in steps for u in s['requires_unseen']]))
    # The closing label is the claim's own support profile. A claim that carries requires_unseen is not
    # fully carried by its panels however many steps read "shown": part of it lives only in the text.
    if 'shown' not in sups and 'partial' not in sups: closing = 'not addressed'
    elif claim_unseen or 'contradicts' in sups or 'partial' in sups: closing = 'partial'
    elif sups.count('shown') >= 2: closing = 'shown'
    else: closing = 'partial'
    closing_why = ('the claim names a fact no panel carries: ' + '; '.join(claim_unseen) if claim_unseen
                   else 'a step contradicts the claim' if 'contradicts' in sups
                   else 'a step is only partial' if 'partial' in sups
                   else 'two or more channels show it and nothing is missing')

    # plan section 5: structural leave-one-out at CHANNEL level, no model calls
    chans = sorted({s['family'] for s in steps})
    nec = {}
    for c in chans:
        rest = [s for s in steps if s['family'] != c]
        keeps_shown = any(s['expected_support'] == 'shown' for s in rest)
        sole_contrast = (any(s['mm_op'] == 'compare_across_conditions' for s in steps if s['family'] == c)
                         and not any(s['mm_op'] == 'compare_across_conditions' for s in rest))
        nec[c] = {'structural': 'necessary' if (not keeps_shown or sole_contrast) else 'redundant_by_single_loo',
                  'why': ('no shown support survives removing this channel' if not keeps_shown
                          else 'sole channel carrying the across-condition comparison the claim needs' if sole_contrast
                          else 'a shown support survives without it; single leave-one-out cannot separate redundant pairs'),
                  'confidence': 'high' if (not keeps_shown or sole_contrast) else 'low'}

    return {'case': case['case'], 'paper': P, 'graph': os.path.relpath(gp, ROOT), 'claim': claim,
            'claim_type': N[claim].get('type'), 'claim_text': N[claim].get('label'),
            'n_steps': len(steps), 'channels': chans, 'n_channels': len(chans),
            'lanes': {'fm': sum(1 for s in steps if s['lane'] == 'fm'),
                      'oracle': sum(1 for s in steps if s['lane'] == 'oracle'),
                      'other': sum(1 for s in steps if s['lane'] == 'other')},
            'tests': {k: sum(1 for s in steps if s['tests'] == k) for k in ('perception', 'selection', 'integration')},
            'steps': steps, 'dropped_panels': dropped,
            'closing_support': closing, 'closing_why': closing_why, 'closing_missing': missing,
            'necessity': nec, 'note': 'Every verdict is model against model.'}


def main(case_id):
    sel = json.load(open(os.path.join(ROOT, 'results/v2/case_selection.json')))
    case = next(c for c in sel['cases'] if c['case'] == case_id)
    ch = build(case)
    d = os.path.join(ROOT, 'results/v2/cases', ch['paper'], ch['claim'])
    os.makedirs(d, exist_ok=True)
    json.dump(ch, open(os.path.join(d, 'case.json'), 'w'), indent=1)
    print(f"{ch['case']}: {ch['n_steps']} steps, {ch['n_channels']} channels {ch['channels']}, "
          f"lanes {ch['lanes']}, closing={ch['closing_support']}, dropped={len(ch['dropped_panels'])}")
    for s in ch['steps']:
        p = ','.join(x['suffix'] for x in s['panels'])
        print(f"   {s['step']}. {s['node']:4s} {str(s['technique'])[:14]:14s} {s['delivery']:6s} {s['tests']:11s} "
              f"{s['expected_support']:12s} [{p}]")
    for dp in ch['dropped_panels']: print(f"   DROPPED {dp['node']}: {dp['reason']}")
    print(f"   necessity: { {k: v['structural'] for k, v in ch['necessity'].items()} }")
    return d


if __name__ == '__main__': main(sys.argv[1])
