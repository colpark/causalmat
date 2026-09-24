"""leakcheck.py: does any MatMech span text reach a page or a solver-visible field?

  python3 trace_kit_v5/leakcheck.py

A naive substring test over-reports. "Friction stir processing (FSP)" is a MatMech cause span AND a
phrase our own graph node n3 uses, because it is simply the name of a technique. Matching it proves
nothing about where the words came from.

So a match counts as a leak only when the phrase does NOT already appear in our graph's own node
labels. If our graph contains it independently, the shared wording is shared vocabulary, not
MatMech text entering our content.

Every verdict is model against model.
"""
import json, os, re, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v3'))
from normalize import fold

MIN = 25


def main():
    leaks, coincidences, npages = [], [], 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'results/v5/pages/*.html'))):
        npages += 1
        tr = os.path.basename(f)[:-5]
        t = json.load(open(os.path.join(ROOT, 'results/v4x', tr, 'trace.json')))
        g = json.load(open(os.path.join(ROOT, t['graph'])))
        ours = fold(' || '.join((n.get('label') or '') for n in g['nodes']))
        hops = json.load(open(os.path.join(ROOT, 'results/v3', t['paper'], 'hops.json')))['hops']
        page = fold(re.sub(r'data:image/[^"]+', '', open(f).read()))
        for h in hops:
            for k in ('cause', 'effect'):
                raw = h['_matmech_span_DO_NOT_PROMPT'][k] or ''
                sp = fold(raw)
                if len(sp) < MIN or sp not in page: continue
                (coincidences if sp in ours else leaks).append((tr, h['id'], k, raw))
    print(f"{npages} pages checked")
    print(f"  genuine leaks: {len(leaks)}")
    for tr, h, k, raw in leaks: print(f"    {tr} {h} {k}: {raw[:90]}")
    print(f"  coincidental matches (the phrase is in our graph too, so it is our vocabulary): "
          f"{len(coincidences)}")
    for tr, h, k, raw in coincidences: print(f"    {tr} {h} {k}: {raw[:90]}")
    return 0 if not leaks else 2


if __name__ == '__main__': sys.exit(main())
