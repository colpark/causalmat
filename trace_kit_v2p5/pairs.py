"""pairs.py: find pairs of observations the graph already links, where an answer needs both.

  python3 trace_kit_v2p5/pairs.py

v5 took its units from MatMech's hops and needed a confirmed link between two of them, which cost
16 of 32 papers: their hops attached to evidence and then nothing joined them. v2.5 takes the unit
from our own graph instead, so a paper yields items whenever its graph links two observations,
whether or not MatMech recorded a hop over them. Depth 2 holds by construction.

Three generators:

  covariation    two observations carrying series of the same length over the same samples, in
                 different quantities. There is no `panel_conditions` field in these graphs, so a
                 series is detected from the observation text: a label reporting three or more
                 numbers in one sweep. Two such series pair when they are the same length and hang
                 off the same claim or the same `attrs.object`. This is a proxy and is recorded as
                 one on every item.
  complementary  two observations from different technique families that evidence the SAME claim,
                 so each carries part of the support and neither carries all of it.
  spine_edge     a `causes`, `produces` or `explains` edge between two claims that both have
                 figure-backed evidence. A MatMech hop is attached where one confirms the edge and
                 is not required.

Every verdict is model against model.
"""
import json, os, re, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v3'))
from support import claim_support

FM = {'SEM', 'TEM', 'STEM', 'XRD', 'XAS', 'ATOM', 'EBSD', 'AFM', 'CT', 'SAXS', 'LEED'}
SPINE_RELS = ('causes', 'produces', 'explains')
NUM = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?)(?![\w.])')


def fam(t):
    if isinstance(t, list): t = t[0] if t else None
    return (t or '').split(':')[0].upper()


def series(label):
    """numbers reported as a sweep. Three or more in one label, and not a year or a figure number."""
    vals = [float(x) for x in NUM.findall(label or '')]
    vals = [v for v in vals if not (1900 < v < 2100 and v == int(v))]
    return vals if len(vals) >= 3 else []


def obs_of(g):
    return [n for n in g['nodes'] if (n.get('type') or '').startswith('OBS') and n.get('panel_ids')]


def main():
    papers = [x['paper'] for x in json.load(open(os.path.join(ROOT, 'results/v5_papers.json')))]
    out, tally = [], collections.Counter()
    perpaper = collections.defaultdict(collections.Counter)
    for p in papers:
        st = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))
        g = json.load(open(os.path.join(ROOT, st['graph'])))
        N = {n['id']: n for n in g['nodes']}
        sup = claim_support(g)
        ev_by_claim = collections.defaultdict(list)
        claim_of = collections.defaultdict(list)
        for e in g['edges']:
            if e.get('rel') == 'evidences' and e['src'] in N and e['dst'] in N:
                if N[e['src']].get('panel_ids'):
                    ev_by_claim[e['dst']].append(e['src'])
                    claim_of[e['src']].append(e['dst'])
        O = obs_of(g)

        # 1 covariation
        ser = {n['id']: series(n.get('label')) for n in O}
        ser = {k: v for k, v in ser.items() if v}
        ids = sorted(ser)
        for i, a in enumerate(ids):
            for b in ids[i + 1:]:
                if len(ser[a]) != len(ser[b]): continue
                sha = set(claim_of[a]) & set(claim_of[b])
                oa = (N[a].get('attrs') or {}).get('object')
                ob = (N[b].get('attrs') or {}).get('object')
                same_obj = bool(oa) and oa == ob
                if not sha and not same_obj: continue
                if fam((N[a].get('attrs') or {}).get('technique')) == \
                   fam((N[b].get('attrs') or {}).get('technique')) and not sha: continue
                out.append({'paper': p, 'kind': 'covariation', 'a': a, 'b': b,
                            'series_len': len(ser[a]),
                            'basis': 'shared claim ' + ', '.join(sorted(sha)) if sha
                                     else f'same object: {oa}',
                            'claims': sorted(sha) or sorted(set(claim_of[a]) | set(claim_of[b]))})
                tally['covariation'] += 1; perpaper[p]['covariation'] += 1

        # 2 complementarity
        for c, evs in ev_by_claim.items():
            byfam = collections.defaultdict(list)
            for e in evs: byfam[fam((N[e].get('attrs') or {}).get('technique'))].append(e)
            fams = [f for f in byfam if f]
            for i, fa in enumerate(fams):
                for fb in fams[i + 1:]:
                    a, b = byfam[fa][0], byfam[fb][0]
                    out.append({'paper': p, 'kind': 'complementary', 'a': a, 'b': b,
                                'basis': f'both evidence {c}: {fa} and {fb}', 'claims': [c]})
                    tally['complementary'] += 1; perpaper[p]['complementary'] += 1

        # 3 spine edge
        hops = json.load(open(os.path.join(ROOT, 'results/v3', p, 'hops.json')))['hops']
        for e in g['edges']:
            if e.get('rel') not in SPINE_RELS: continue
            u, d = e.get('src'), e.get('dst')
            if u not in N or d not in N: continue
            if (N[u].get('type') or '').startswith('OBS') or (N[d].get('type') or '').startswith('OBS'):
                continue
            if not (ev_by_claim.get(u) and ev_by_claim.get(d)): continue
            hop = next((h['id'] for h in hops
                        if h.get('link_confirmed_by') and
                        (u in str(h.get('link_confirmed_by')) or d in str(h.get('link_confirmed_by')))), None)
            out.append({'paper': p, 'kind': 'spine_edge', 'a': u, 'b': d, 'rel': e['rel'],
                        'basis': f"{u} -{e['rel']}-> {d}", 'claims': [u, d],
                        'evidence_a': ev_by_claim[u], 'evidence_b': ev_by_claim[d],
                        'matmech_hop': hop})
            tally['spine_edge'] += 1; perpaper[p]['spine_edge'] += 1

    json.dump({'pairs': out, 'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v2p5/pairs.json'), 'w'), indent=1)
    print(f"{len(out)} pairs over {len(papers)} papers: {dict(tally)}")
    withany = sum(1 for p in papers if perpaper[p])
    print(f"papers with at least one pair: {withany} of {len(papers)}  "
          f"(v5 had 16 of 32 with a surviving item)")
    print(f"\n{'paper':50s} {'cov':>4s} {'comp':>5s} {'edge':>5s}")
    for p in papers:
        c = perpaper[p]
        print(f"{p[:50]:50s} {c['covariation']:4d} {c['complementary']:5d} {c['spine_edge']:5d}")


if __name__ == '__main__': main()
