"""paper_chains.py: build a support chain for every qualifying claim in ONE paper.

  python3 trace_kit_v2/paper_chains.py <paper>

Qualifying = two or more figure-backed evidence nodes, from results/v2/candidates.json.
Writes results/v2/paper/<paper>/<claim>/case.json plus panels, one folder per claim.
"""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chain as CH
import materialize as MAT


def main(paper):
    cands = [c for c in json.load(open(os.path.join(ROOT, 'results/v2/candidates.json')))
             if c['paper'] == paper]
    if not cands: print('no qualifying claims'); return
    out = os.path.join(ROOT, 'results/v2/paper', paper)
    built = []
    for c in sorted(cands, key=lambda x: (not x['spine'], x['claim'])):
        case = {'case': f"{paper}:{c['claim']}", 'paper': paper, 'claim': c['claim'],
                'graphs': c['graphs'], 'evidence': c['evidence']}
        try:
            ch = CH.build(case, use_contrib=False)
        except Exception as e:
            print(f"  {c['claim']:5s} skipped: {type(e).__name__}: {e}"); continue
        if ch['n_steps'] < 2:
            print(f"  {c['claim']:5s} skipped: {ch['n_steps']} step after panel resolution"); continue
        d = os.path.join(out, c['claim']); os.makedirs(d, exist_ok=True)
        ch['spine'] = c['spine']; ch['claim_type'] = c['claim_type']
        json.dump(ch, open(os.path.join(d, 'case.json'), 'w'), indent=1)
        MAT.main(d)
        ch = json.load(open(os.path.join(d, 'case.json')))
        built.append(ch)
        print(f"  {c['claim']:5s} {ch['n_steps']} steps, {ch['n_channels']} channels {ch['channels']}, "
              f"{sum(1 for s in ch['steps'] for p in s['panels'] if p.get('png'))} panels"
              + (f", {len(ch['dropped_panels'])} dropped" if ch['dropped_panels'] else ""))
    json.dump({'paper': paper, 'claims': len(built),
               'note': 'Every verdict is model against model.'},
              open(os.path.join(out, 'index.json'), 'w'), indent=1)
    print(f"\n{len(built)} chains built for {paper}")


if __name__ == '__main__': main(sys.argv[1])
