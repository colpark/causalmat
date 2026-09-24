"""reach.py: matched vs attachable, per hop.

matched    = net-decompose returned at least one claim stating the hop's fact.
attachable = at least one matched claim is supported, where support is derived in `support.py`
             from a **direct `evidences` edge out of an observation node that carries panels**.

**Reach is one step.** The observation must point at the matched claim itself. No paths through
intermediate claims, and no `qualifies` / `contrasts` / `rules_out` edges, which are caveats rather
than support. A claim two hops from a panel is not attachable here.

Support is never read off a claim node's own `image_support` field. Three of the five graphs barely
set it -- Acta Materialia 0 of 30 claims, Rare Metals 0 of 19, Biomaterials 1 of 31 -- while storing
the evidence on OBS nodes instead, so the field measures where a graph keeps support rather than
whether the paper shows the thing. `support.py` is the single place this is derived.

The gap between matched and attachable is the finding. A matched-but-not-attachable hop lands on a
claim the paper asserts in text rather than shows in a figure, so it can carry no trace however good
the match. For each of those we look for a nearer claim that IS attachable, within 3 undirected
edges; if one exists the matcher had somewhere better to land and did not, which is a remaining
completeness miss logged as a finding.

Every verdict is model against model.

  python3 trace_kit_v3/reach.py [--pre]
"""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from support import claim_support, supported
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PAPERS = ['Rare_Metals__s12598-012-0515-6', 'Biomaterials__j.biomaterials.2011.11.042',
          'Advanced_Functional_Materials__10.1002_adfm.202008088',
          'Nano_Letters__10.1021_acs.nanolett.6b04294',
          'Acta_Materialia__10.1016_j.actamat.2021.116797']


def load(p, pre=False):
    st = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))
    g = json.load(open(os.path.join(ROOT, st['graph'])))
    f = 'decompose.prefix.json' if pre else 'decompose.json'
    d = json.load(open(os.path.join(ROOT, 'results/v3', p, f)))
    return st, g, d


def near(nid, N, adj, sup, maxd=3):
    """attachable claims within maxd undirected edges, nearest first"""
    seen, out, q = {nid}, [], [(nid, 0)]
    while q:
        cur, dd = q.pop(0)
        if dd >= maxd: continue
        for m in adj.get(cur, ()):
            if m in seen: continue
            seen.add(m); q.append((m, dd + 1))
            if (N[m].get('type') or '').startswith('OBS'): continue   # an observation, not a claim
            if supported(sup, m): out.append((dd + 1, m, (N[m].get('label') or '')[:80]))
    return sorted(out)


def run(pre=False):
    rows, findings = [], []
    for p in PAPERS:
        st, g, d = load(p, pre)
        N = {n['id']: n for n in g['nodes']}
        sup = claim_support(g)
        adj = collections.defaultdict(set)
        for e in g['edges']:
            adj[e['src']].add(e['dst']); adj[e['dst']].add(e['src'])
        for h in st['hops']:
            hid = h['hop']
            cs = d['hops'].get(hid, {}).get('effect', {}).get('claims', [])
            att = [c for c in cs if supported(sup, c)]
            rows.append({'paper': p, 'hop': hid, 'stage_type': h.get('stage_type'),
                         'claims': cs, 'matched': bool(cs), 'attachable': bool(att),
                         'attachable_claims': att,
                         'panels': sorted({q for c in att for q in sup[c]['panels']}),
                         'chain_strength': h.get('chain_strength')})
            if cs and not att:
                alts = []
                for c in cs: alts += near(c, N, adj, sup)
                alts = sorted({a[1]: a for a in alts}.values())[:3]
                findings.append({'paper': p, 'hop': hid, 'landed_on': cs,
                                 'landed_labels': {c: (N.get(c, {}).get('label') or '')[:90] for c in cs},
                                 'nearer_attachable': [{'dist': a[0], 'claim': a[1], 'label': a[2]} for a in alts]})
    return rows, findings


def main():
    pre = '--pre' in sys.argv
    rows, findings = run(pre)
    m = sum(r['matched'] for r in rows); a = sum(r['attachable'] for r in rows)
    print(f"{'PRE-FIX' if pre else 'POST-FIX'}: {len(rows)} hops, {m} matched, {a} attachable "
          f"= {a}/{m} of matched ({a/m:.0%})")
    print(f"\n{'paper':34s} {'hops':>4s} {'matched':>7s} {'attachable':>10s}")
    by = collections.defaultdict(lambda: [0, 0, 0])
    for r in rows:
        b = by[r['paper']]; b[0] += 1; b[1] += r['matched']; b[2] += r['attachable']
    for p, b in by.items(): print(f"{p[:34]:34s} {b[0]:4d} {b[1]:7d} {b[2]:10d}")
    print(f"\nunreachable hops ({len(findings)}):")
    for f in findings:
        print(f"  {f['paper'][:30]:30s} {f['hop']}  landed on {f['landed_on']}")
        for c, l in f['landed_labels'].items(): print(f"      {c}: {l}")
        if f['nearer_attachable']:
            print(f"      COMPLETENESS MISS -- a nearer attachable claim exists:")
            for al in f['nearer_attachable']:
                print(f"        d={al['dist']} {al['claim']}: {al['label']}")
        else:
            print(f"      no attachable claim within 3 edges: the paper asserts this in text")
    if not pre:
        json.dump({'rows': rows, 'findings': findings,
                   'note': 'support from direct evidences edges only, one step. '
                           'Every verdict is model against model.'},
                  open(os.path.join(ROOT, 'results/v3/reach.json'), 'w'), indent=1)
    return rows, findings


if __name__ == '__main__': main()
