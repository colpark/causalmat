"""step3b.py: for each hop the lexical matcher left unattached, is it `unrelated` or a `missing_edge`?

Step 3a showed the "coverage gap" label could not be trusted: all six unattached hops cite figures
our graph already reads. This step re-asks the question with the matcher of record (net-decompose +
complete.py) and separates three outcomes:

  resolved      the model matched a claim that IS supported. The lexical gap was a matcher miss and
                the hop now attaches.
  missing_edge  the model matched claims, none of them supported, BUT our graph does read the
                figures the hop cites. The fact and the panels are both in our graph; no `evidences`
                edge joins them to the claim the hop landed on.
  unrelated     the model matched nothing, or matched claims with no panels anywhere near the hop's
                figures. Our graph does not carry this hop's fact.

Every verdict is model against model.

  python3 trace_kit_v3/step3b.py
"""
import json, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from support import claim_support, supported


def figs_in_graph(g):
    """figure ids our graph reads, from OBS nodes carrying panels"""
    out = collections.defaultdict(list)
    for n in g['nodes']:
        for p in (n.get('panel_ids') or []):
            f = p.split('#')[1] if '#' in p else p
            out[''.join(ch for ch in f if not ch.islower() or ch == 'F').rstrip('abcdefgh')].append(n['id'])
        for f in (n.get('figs') or []): out[f].append(n['id'])
    return out


def main():
    rows = [json.loads(l) for l in open(os.path.join(ROOT, 'results/v3/unattached.jsonl'))]
    out, tally = [], collections.Counter()
    for r in rows:
        p = r['paper']
        st = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))
        g = json.load(open(os.path.join(ROOT, st['graph'])))
        d = json.load(open(os.path.join(ROOT, 'results/v3', p, 'decompose.json')))
        N = {n['id']: n for n in g['nodes']}
        sup = claim_support(g)
        fg = figs_in_graph(g)
        cs = d['hops'].get(r['hop'], {}).get('effect', {}).get('claims', [])
        att = [c for c in cs if supported(sup, c)]
        ours = sorted({f for f in fg if f in set(r['matmech_figures'])})
        if att:
            verdict, why = 'resolved', f"model matched supported claim(s) {', '.join(att)}"
        elif cs and ours:
            verdict, why = 'missing_edge', (
                f"model matched {', '.join(cs)}, none supported, but our graph reads "
                f"{', '.join(ours)} through {', '.join(sorted({n for f in ours for n in fg[f]}))[:60]}")
        elif cs:
            verdict, why = 'unrelated', (f"model matched {', '.join(cs)} but our graph reads none of "
                                         f"{', '.join(r['matmech_figures'])}")
        else:
            verdict, why = 'unrelated', 'model matched no claim at all'
        tally[verdict] += 1
        out.append({'paper': p, 'hop': r['hop'], 'stage_type': r['stage_type'],
                    'matmech_figures': r['matmech_figures'], 'our_figures_read': ours,
                    'model_claims': cs, 'supported_claims': att,
                    'step3a_label': r['appears_to_be'], 'verdict': verdict, 'why': why})
    json.dump({'rows': out, 'tally': dict(tally),
               'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v3/step3b.json'), 'w'), indent=1)
    print(f"{len(out)} hops the lexical matcher left unattached: {dict(tally)}\n")
    for o in out:
        print(f"  {o['paper'][:30]:30s} {o['hop']}  {o['verdict'].upper()}")
        print(f"      figs {o['matmech_figures']} | ours {o['our_figures_read']}")
        print(f"      {o['why']}")


if __name__ == '__main__': main()
