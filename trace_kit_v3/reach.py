"""reach.py: matched vs attachable, per hop.

matched    = net-decompose returned at least one claim stating the hop's fact.
attachable = at least one matched claim has panels behind it. Two readings, both reported:

  strict   the claim's own image_support is shown/partial AND panels are behind it. This is the
           briefed definition.
  evidence panels are reachable from the claim -- on the claim itself, or on an OBS node joined to
           it -- whatever the claim's image_support field says.

They differ because the graphs do not share a convention. Of the five papers, Acta Materialia has 0
of 30 claims carrying image_support and 23 OBS nodes carrying panels; Rare Metals (v06b) has 0 of
19 and 8; Biomaterials 1 of 31 and 20. adfm (12 of 27) and Nano Letters (8 of 28) put evidence on
the claims themselves. So the strict count reports Acta and Rare Metals as 0 attachable for a
reason that is about how the graph was written, not about whether the paper shows the figure.
`evidence` is the reading that answers "can this hop carry a trace", since a trace is built from
panels and a claim. Both are printed; the strict one is not the headline.

The gap between the two is the finding. A matched-but-not-attachable hop lands on a claim the paper
asserts in text rather than shows in a figure, so it can carry no trace however good the match.

For each matched-but-not-attachable hop we also look for a nearer, more specific claim that IS
attachable, within 3 undirected edges. If one exists, the matcher had somewhere better to land and
did not: that is a remaining completeness miss, logged as a finding.

Every verdict is model against model.

  python3 trace_kit_v3/reach.py [--pre]
"""
import json, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PAPERS = ['Rare_Metals__s12598-012-0515-6', 'Biomaterials__j.biomaterials.2011.11.042',
          'Advanced_Functional_Materials__10.1002_adfm.202008088',
          'Nano_Letters__10.1021_acs.nanolett.6b04294',
          'Acta_Materialia__10.1016_j.actamat.2021.116797']
SHOWN = ('shown', 'partial')


def load(p, pre=False):
    st = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))
    g = json.load(open(os.path.join(ROOT, st['graph'])))
    f = 'decompose.prefix.json' if pre else 'decompose.json'
    d = json.load(open(os.path.join(ROOT, 'results/v3', p, f)))
    return st, g, d


def panels_of(nid, N, adj):
    """panels on the claim itself, else on an evidence node one edge away"""
    n = N.get(nid) or {}
    if n.get('panel_ids'): return list(n['panel_ids']), 'self'
    for m in adj.get(nid, ()):
        e = N.get(m) or {}
        if e.get('panel_ids') and (e.get('type') or '').startswith('OBS'):
            return list(e['panel_ids']), m
    return [], None


def attachable_claim(nid, N, adj, strict=True):
    n = N.get(nid) or {}
    if strict and n.get('image_support') not in SHOWN: return False, [], None
    pans, via = panels_of(nid, N, adj)
    return bool(pans), pans, via


def near(nid, N, adj, maxd=3):
    """attachable nodes within maxd undirected edges, nearest first"""
    seen, out, q = {nid}, [], [(nid, 0)]
    while q:
        cur, dd = q.pop(0)
        if dd >= maxd: continue
        for m in adj.get(cur, ()):
            if m in seen: continue
            seen.add(m); q.append((m, dd + 1))
            if (N[m].get('type') or '').startswith('OBS'): continue   # an observation, not a claim
            ok, pans, _ = attachable_claim(m, N, adj, strict=False)
            if ok: out.append((dd + 1, m, (N[m].get('label') or '')[:80]))
    return sorted(out)


def run(pre=False):
    rows, findings = [], []
    for p in PAPERS:
        st, g, d = load(p, pre)
        N = {n['id']: n for n in g['nodes']}
        adj = collections.defaultdict(set)
        for e in g['edges']:
            adj[e['src']].add(e['dst']); adj[e['dst']].add(e['src'])
        for h in st['hops']:
            hid = h['hop']
            cs = d['hops'].get(hid, {}).get('effect', {}).get('claims', [])
            att = [c for c in cs if attachable_claim(c, N, adj, True)[0]]
            ev  = [c for c in cs if attachable_claim(c, N, adj, False)[0]]
            rows.append({'paper': p, 'hop': hid, 'claims': cs, 'matched': bool(cs),
                         'attachable_strict': bool(att), 'attachable': bool(ev),
                         'attachable_claims': ev, 'strict_claims': att,
                         'chain_strength': h.get('chain_strength')})
            if cs and not ev:
                alts = []
                for c in cs: alts += near(c, N, adj)
                alts = sorted({a[1]: a for a in alts}.values())[:3]
                findings.append({'paper': p, 'hop': hid, 'landed_on': cs,
                                 'landed_labels': {c: (N.get(c, {}).get('label') or '')[:90] for c in cs},
                                 'nearer_attachable': [{'dist': a[0], 'claim': a[1], 'label': a[2]} for a in alts]})
    return rows, findings


def main():
    pre = '--pre' in sys.argv
    rows, findings = run(pre)
    m = sum(r['matched'] for r in rows)
    a = sum(r['attachable'] for r in rows); sa = sum(r['attachable_strict'] for r in rows)
    print(f"{'PRE-FIX' if pre else 'POST-FIX'}: {len(rows)} hops, {m} matched, "
          f"{a} attachable (evidence) = {a}/{m} of matched;  {sa} attachable (strict) = {sa}/{m}")
    print(f"\n{'paper':34s} {'hops':>4s} {'matched':>7s} {'attach(ev)':>10s} {'attach(strict)':>14s}")
    by = collections.defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        b = by[r['paper']]; b[0] += 1; b[1] += r['matched']
        b[2] += r['attachable']; b[3] += r['attachable_strict']
    for p, b in by.items():
        print(f"{p[:34]:34s} {b[0]:4d} {b[1]:7d} {b[2]:10d} {b[3]:14d}")
    if findings:
        print(f"\nmatched but not attachable: {len(findings)}")
        for f in findings:
            print(f"  {f['paper'][:30]:30s} {f['hop']}  landed on {f['landed_on']}")
            for c, l in f['landed_labels'].items(): print(f"      {c}: {l}")
            if f['nearer_attachable']:
                print(f"      nearer attachable claim exists -> COMPLETENESS MISS:")
                for al in f['nearer_attachable']:
                    print(f"        d={al['dist']} {al['claim']}: {al['label']}")
            else:
                print(f"      no attachable claim within 3 edges: the paper asserts this in text")
    if not pre:
        json.dump({'rows': rows, 'findings': findings,
                   'note': 'Every verdict is model against model.'},
                  open(os.path.join(ROOT, 'results/v3/reach.json'), 'w'), indent=1)
    return rows, findings


if __name__ == '__main__': main()
