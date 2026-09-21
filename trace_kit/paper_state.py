"""paper_state.py <paper>: after the writer pass(es), record per-trace state in results/traces/<paper>.traces.json and
results/traces/writer/<paper>/paper_state.json. A trace listed in rewrite_info.json (it failed leak or provenance on pass 1
and got one rewrite) that still fails leak or provenance is blocked. The block records whether the remaining leak hits are
in the question (writer) or only in the given node labels (cutter), since a rewrite cannot remove the second kind.
Every verdict here is model against model."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import validate_traces as V
P = sys.argv[1]; W = f'results/traces/writer/{P}'
g = json.load(open(f'taxonomy/graphs_v05/first100/{P}.json')); N = {n['id']: n for n in g['nodes']}
TT = json.load(open(f'results/traces/{P}.traces.json')); T = {t['id']: t for t in TT['traces']}
VV = {v['id']: v for v in json.load(open(f'results/traces/{P}.validation.json'))}
info = json.load(open(f'{W}/rewrite_info.json')) if os.path.exists(f'{W}/rewrite_info.json') else {}
state = []
for k, t in T.items():
    v = VV[k]; f = [x for x in v.get('fails', []) if x in ('leak', 'provenance')]
    rec = {'id': k, 'root': t['root'], 'subtype': t['subtype'], 'status': t['status'], 'verdict': v['verdict'], 'fails': v.get('fails', []),
           'warnings': v.get('warnings', []), 'rewritten': k in info, 'pass1_fails': info.get(k, {}).get('fails'), 'blocked': None}
    if k in info and f:
        where = []
        if 'leak' in f:
            L = v['nets']['leak']; q = t.get('question', '')
            inq = [b for b in L['bigrams'] if tuple(b.split()) in V.bigrams(q)] + [n for n in L['numbers'] if n in V.nums(q)]
            where.append('question' if inq else 'given context only')
        rec['blocked'] = {'reason': f[0] if len(f) == 1 else '+'.join(f), 'leak_source': where[0] if where else None,
                          'bigrams': v['nets']['leak']['bigrams'], 'numbers': v['nets']['leak']['numbers'],
                          'missing_numbers': v['nets']['provenance']['missing_numbers']}
    t['blocked'] = rec['blocked']; t['writer_passes'] = 2 if k in info else 1
    state.append(rec)
json.dump(TT, open(f'results/traces/{P}.traces.json', 'w'), indent=1)
json.dump({'paper': P, 'note': 'Every verdict here is model against model; no human checked any item.', 'traces': state}, open(f'{W}/paper_state.json', 'w'), indent=1)
nonclosed = [s for s in state if s['status'] != 'closed']
print(f"{P}: {len(state)} traces, {len(nonclosed)} non-closed, rewritten {sum(s['rewritten'] for s in state)}, blocked {sum(bool(s['blocked']) for s in state)}",
      [(s['id'], s['blocked']['reason'], s['blocked']['leak_source']) for s in state if s['blocked']])
