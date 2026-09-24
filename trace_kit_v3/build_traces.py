"""build_traces.py: turn confirmed hop chains into traces. One step per hop.

  python3 trace_kit_v3/build_traces.py

A v2 trace asked "does this evidence support the claim?", one step per evidence node. A v3 trace
asks, for each **hop**, whether the evidence warrants the step from the previous hop's effect to
this one's. The hop is the step.

A chain is a maximal path over confirmed links (`span` or `stage+graph`) through hops that are
attachable and not excluded. One-hop traces are not built: a single hop has no step to warrant.

**MatMech's cause and effect spans never enter a trace.** Every word a solver sees is our own claim
text from the graph. The spans were used to match and to chain, upstream of here, and stay in
`_matmech_span_DO_NOT_PROMPT`.

Every verdict is model against model.
"""
import json, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
from support import claim_support, supported
from cut_traces import store_for, panel_record, unmath

ORACLE = {'ECHEM', 'THERMAL', 'MECH', 'TRANSPORT', 'ASSAY', 'BIO', 'PHYS', 'CHROM', 'PROFILOMETRY', 'TGA'}
FM_LANE = {'SEM', 'TEM', 'STEM', 'XRD', 'XAS', 'ATOM', 'EBSD', 'AFM', 'CT', 'SAXS', 'LEED'}
PAPERS = ['Acta_Materialia__10.1016_j.actamat.2021.116797', 'Rare_Metals__s12598-012-0515-6',
          'Advanced_Functional_Materials__10.1002_adfm.202008088',
          'Biomaterials__j.biomaterials.2011.11.042',
          'Nano_Letters__10.1021_acs.nanolett.6b04294']


def fam(t):
    if isinstance(t, list): t = t[0] if t else None
    return (t or '').split(':')[0].upper()


def chains(hops, ok):
    """maximal paths over confirmed links through usable hops"""
    H = {h['id']: h for h in hops}
    nxt = {h['id']: h['next'] for h in hops
           if h.get('next') and h.get('chain_strength') in ('span', 'stage+graph')
           and ok(h['id']) and ok(h['next'])}
    tails = set(nxt.values())
    out = []
    for s in [h['id'] for h in hops if h['id'] in nxt and h['id'] not in tails]:
        path, cur = [s], s
        while cur in nxt:
            cur = nxt[cur]; path.append(cur)
        if len(path) > 1: out.append(path)
    return out


def main():
    made, skipped = [], []
    for P in PAPERS:
        st_j = json.load(open(os.path.join(ROOT, 'results/v3', P, 'stitch.json')))
        gp = os.path.join(ROOT, st_j['graph'])
        g = json.load(open(gp)); N = {n['id']: n for n in g['nodes']}
        sup = claim_support(g)
        store = store_for(gp)
        d = json.load(open(os.path.join(ROOT, 'results/v3', P, 'decompose.json')))
        hops = json.load(open(os.path.join(ROOT, 'results/v3', P, 'hops.json')))['hops']
        H = {h['id']: h for h in hops}

        def usable(hid):
            h = H.get(hid) or {}
            if h.get('excluded_from_traces'): return False
            cs = d['hops'].get(hid, {}).get('effect', {}).get('claims', [])
            return any(supported(sup, c) for c in cs)

        for path in chains(hops, usable):
            steps, drop = [], []
            for i, hid in enumerate(path, 1):
                cs = d['hops'][hid]['effect']['claims']
                att = [c for c in cs if supported(sup, c)]
                obs = sorted({o for c in att for o in sup[c]['via']})
                techs = [N[o].get('attrs', {}).get('technique') for o in obs]
                f = fam(next((t for t in techs if t), None))
                panels = []
                for o in obs:
                    for pid in dict.fromkeys(N[o].get('panel_ids') or []):
                        r = panel_record(store, pid) or {}
                        c = r.get('crop')
                        panels.append({'panel_id': pid, 'suffix': pid.split('#')[1],
                                       'crop': c if c and os.path.exists(c) else None,
                                       'figure': r.get('figure'), 'obs': o,
                                       'caption_span': ' '.join(unmath(r.get('span') or '').split()) or None})
                delivery = 'oracle' if f in ORACLE else 'crop'
                if delivery == 'crop' and not any(p['crop'] for p in panels):
                    drop.append({'hop': hid, 'reason': 'no crop resolves for any cited panel'})
                    continue
                steps.append({
                    'step': len(steps) + 1, 'hop': hid, 'stage_type': H[hid]['stage_type'],
                    'node': att[0], 'claims': att,
                    'effect_text': ' '.join(N[c].get('label') or '' for c in att[:1]),
                    'all_effect_text': [N[c].get('label') for c in att],
                    'observation': ' '.join(N[o].get('label') or '' for o in obs[:1]),
                    'observations': [N[o].get('label') for o in obs],
                    'technique': next((t for t in techs if t), None), 'family': f,
                    'delivery': delivery,
                    'lane': 'fm' if f in FM_LANE else ('oracle' if f in ORACLE else 'other'),
                    'expected_support': sup[att[0]]['level'],
                    'link_from_previous': H[path[i - 2]].get('link_confirmed_by') if i > 1 else None,
                    'panels': panels})
            if len(steps) < 2:
                skipped.append({'paper': P, 'path': path, 'reason': 'fewer than two usable steps'})
                continue
            case = {'case': f"{P.split('__')[0][:12].lower()}_{'_'.join(path)}", 'paper': P,
                    'graph': os.path.relpath(gp, ROOT), 'chain': path,
                    'chain_strength': [H[h].get('chain_strength') for h in path[:-1]],
                    'setup': N[[n['id'] for n in g['nodes']][0]].get('label'),
                    'steps': steps, 'dropped': drop,
                    'note': 'One step per MatMech hop. MatMech spans never enter a prompt. '
                            'Every verdict is model against model.'}
            out = os.path.join(ROOT, 'results/v3/traces', case['case'])
            os.makedirs(out, exist_ok=True)
            json.dump(case, open(os.path.join(out, 'case.json'), 'w'), indent=1)
            made.append((case['case'], P, path, len(steps), sum(len(s['panels']) for s in steps)))
    print(f"{len(made)} traces built\n")
    for c, p, path, ns, np_ in made:
        print(f"  {c:34s} {p[:28]:28s} {'->'.join(path):12s} {ns} steps, {np_} panels")
    for s in skipped: print(f"  SKIPPED {s['path']} in {s['paper'][:28]}: {s['reason']}")


if __name__ == '__main__': main()
