"""confirm_links.py: a stage match is a candidate, not a link.

  python3 trace_kit_v3/confirm_links.py <paper>

Two unrelated findings that happen to share Processing->Structure and Structure->Performance will
chain by stage type and produce a causal story the paper never told. So a stage link is accepted only
when hop A's effect sub-claims and hop B's cause sub-claims share a spine claim, or are joined by a
spine edge in our graph. The joining claim or edge is recorded.

  span        text identity between A's effect and B's cause
  stage+graph stage match, confirmed through our graph
  stage_only  stage match, not confirmed -- kept for the record, excluded from traces
"""
import json, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main(paper):
    d = os.path.join(ROOT, 'results/v3', paper)
    hops = json.load(open(os.path.join(d, 'hops.json')))
    st = json.load(open(os.path.join(d, 'stitch.json')))
    g = json.load(open(os.path.join(ROOT, st['graph'])))
    N = {n['id']: n for n in g['nodes']}
    subs = {h['hop']: [s['claim'] for s in h['sub_claims']] for h in st['hops']}
    # spine edges, both directions, for the "joined by an edge" test
    adj = collections.defaultdict(set)
    for e in g['edges']:
        s, t = e.get('src'), e.get('dst')
        if s in N and t in N:
            adj[s].add((t, e.get('rel'), 'forward')); adj[t].add((s, e.get('rel'), 'back'))
    out = []
    for h in hops['hops']:
        nxt = h.get('next')
        if not nxt: out.append({**h, 'chain_strength': None}); continue
        if h.get('chain_strength') == 'span':
            h['link_confirmed_by'] = 'text identity between the two spans'
            out.append(h); continue
        A, B = set(subs.get(h['id'], [])), set(subs.get(nxt, []))
        shared = sorted(A & B)
        joined = []
        for a in A:
            for b in B:
                if a == b: continue
                for (t, rel, dirn) in adj[a]:
                    if t == b: joined.append(f"{a} -{rel}-> {b}" if dirn == 'forward' else f"{b} -{rel}-> {a}")
        if shared:
            h['chain_strength'] = 'stage+graph'
            h['link_confirmed_by'] = f"shared spine claim{'s' if len(shared) > 1 else ''}: {', '.join(shared)}"
        elif joined:
            h['chain_strength'] = 'stage+graph'
            h['link_confirmed_by'] = f"spine edge joining the two hops' claims: {joined[0]}"
        else:
            h['chain_strength'] = 'stage_only'
            h['link_confirmed_by'] = None
            h['excluded_from_traces'] = True
        out.append(h)
    hops['hops'] = out
    by = collections.Counter(h.get('chain_strength') for h in out if h.get('next'))
    hops['counts']['by_strength'] = {k: v for k, v in by.items() if k}
    hops['counts']['usable_links'] = by['span'] + by['stage+graph']
    json.dump(hops, open(os.path.join(d, 'hops.json'), 'w'), indent=1)
    print(f"{paper[:44]:44s} span={by['span']} stage+graph={by['stage+graph']} stage_only={by['stage_only']}")
    for h in out:
        if not h.get('next'): continue
        print(f"    {h['id']} -> {h['next']:3s} {str(h.get('chain_strength')):11s} {h.get('link_confirmed_by') or 'NOT CONFIRMED, excluded'}")
    return hops


if __name__ == '__main__': main(sys.argv[1])
