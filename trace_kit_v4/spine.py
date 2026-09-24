"""spine.py: express each confirmed link as a path of OUR spine claims, and build the dependency.

  python3 trace_kit_v4/spine.py

MatMech supplies which stretches of the spine are causal steps. Our graph supplies every word.
MatMech hop ids and stage types are recorded as provenance only and are never solver-visible.

A step's **output** is the intermediate proposition it establishes -- the claim it lands on. Its
**question** asks about the next property of whatever the previous step established, by reference
rather than by restatement: step 2 does not say "the Al6Cu6La phase", it says "the phase you
identified in step 1". The referring expression comes from the previous claim's `type`, a controlled
vocabulary, so it can name the kind of thing without naming the finding.

Every verdict is model against model.
"""
import json, os, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.environ.get('TRACES_OUT', 'results/v3/traces')
DST = os.environ.get('V4_OUT', 'results/v4')
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v3'))
from support import claim_support, supported
from v3b import prop_of

# how to refer back to what a step established, without restating it
REFERS = {
    'STR/phase/identity':              'the phase you identified',
    'STR/phase/fraction':              'the phase proportions you determined',
    'STR/phase/lattice':               'the lattice behaviour you measured',
    'STR/microstructure/feature_size': 'the feature sizes you measured',
    'STR/microstructure/porosity':     'the pore structure you characterised',
    'STR/microstructure/distribution': 'the distribution you described',
    'PRP/value':                       'the property value you measured',
    'PRF/service_capability':          'the performance you measured',
    'MEC/pathway':                     'the mechanism you identified',
    'MEC/identification':              'the mechanism you identified',
    'DSC/conclusion':                  'the conclusion you reached',
}


def refer(claims, N, step_no):
    out = []
    for c in claims:
        r = REFERS.get((N.get(c) or {}).get('type'))
        if r and r not in out: out.append(r)
    base = ' and '.join(out) if out else 'what you established'
    return f"{base} in step {step_no}"


def main():
    traces = []
    for cj in sorted(glob.glob(os.path.join(ROOT, SRC, '*/case.json'))):
        ch = json.load(open(cj))
        g = json.load(open(os.path.join(ROOT, ch['graph'])))
        N = {n['id']: n for n in g['nodes']}
        sup = claim_support(g)
        hops = {h['id']: h for h in json.load(
            open(os.path.join(ROOT, 'results/v3', ch['paper'], 'hops.json')))['hops']}
        E = [(e['src'], e['dst'], e['rel']) for e in g['edges']]

        steps = []
        for i, s in enumerate(ch['steps']):
            hop = hops[s['hop']]
            prev = steps[-1] if steps else None
            prop = prop_of(s['claims'], N)
            if prev:
                q = (f"Taking {refer(prev['claims'], N, prev['step'])} as given, what does the "
                     f"evidence below show about {prop}?")
            else:
                q = f"What does the evidence below show about {prop}?"
            # the spine edge or shared claim that joins this step to the previous one
            join = None
            if prev:
                shared = sorted(set(prev['claims']) & set(s['claims']))
                if shared:
                    join = {'kind': 'shared claim', 'detail': shared}
                else:
                    ed = [f"{a} -{r}-> {b}" for a, b, r in E
                          if (a in prev['claims'] and b in s['claims'])
                          or (b in prev['claims'] and a in s['claims'])]
                    join = {'kind': 'spine edge', 'detail': ed} if ed else \
                           {'kind': 'stage only', 'detail': []}
            steps.append({
                'step': i + 1, 'claims': s['claims'],
                'output': ' ; '.join(x for x in (s['all_effect_text'] or []) if x),
                'output_short': (N.get(s['claims'][0]) or {}).get('label'),
                'property': prop, 'question': q,
                'refers_to_previous': refer(prev['claims'], N, prev['step']) if prev else None,
                'join_to_previous': join,
                'technique': s['technique'], 'delivery': s['delivery'],
                'observations': s['observations'],
                'panels': [{k: p.get(k) for k in ('panel_id', 'suffix', 'png', 'figure', 'caption_span')}
                           for p in s['panels']],
                'support_level': (sup.get(s['claims'][0]) or {}).get('level'),
                'provenance_NOT_SOLVER_VISIBLE': {
                    'matmech_hop': s['hop'], 'stage_type': s['stage_type'],
                    'matmech_figures': hop.get('figures'),
                    'link_confirmed_by': hops[ch['chain'][i - 1]].get('link_confirmed_by') if i else None,
                    'chain_strength': hops[ch['chain'][i - 1]].get('chain_strength') if i else None},
            })
        t = {'trace': ch['case'], 'paper': ch['paper'], 'graph': ch['graph'],
             'chain': ch['chain'], 'setup': ch['setup'], 'steps': steps,
             'note': 'MatMech supplies which stretches are causal; our graph supplies the content. '
                     'Every verdict is model against model.'}
        d = os.path.join(ROOT, DST, ch['case']); os.makedirs(d, exist_ok=True)
        json.dump(t, open(os.path.join(d, 'trace.json'), 'w'), indent=1)
        traces.append(t)

    print(f"{len(traces)} traces, {sum(len(t['steps']) for t in traces)} steps\n")
    for t in traces:
        print(f"  {t['trace']:24s} {'->'.join(t['chain'])}")
        for s in t['steps']:
            j = s['join_to_previous']
            print(f"     step {s['step']} [{s['provenance_NOT_SOLVER_VISIBLE']['matmech_hop']}] "
                  f"{s['property'][:44]:44s} join={j['kind'] if j else '-'} {j['detail'] if j else ''}")
            print(f"        Q: {s['question']}")


if __name__ == '__main__': main()
