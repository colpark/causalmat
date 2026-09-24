"""leakcheck_pages.py: does any MatMech span text reach a page outside its audit-only box?

  python3 trace_kit_v2p5/leakcheck_pages.py

A contiguous-substring test over-reports. In v5 it flagged "Friction stir processing (FSP)", a
MatMech cause span and equally the wording of our own node n3, because it is the name of a
technique. Here it flags "photothermal conversion efficiency", which a drafter wrote into a limit
from our node a13, "Photothermal conversion at 808 nm with efficiency ~19.4%" -- our words, not
MatMech's, just not contiguous in our label.

So a match counts as a leak only when its content words are NOT all present in our graph's own node
labels. Shared technical vocabulary is not a leak; shared phrasing that our graph never uses is.

Every verdict is model against model.
"""
import json, os, re, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v3'))
from normalize import fold

STOP = set('the and that this with from which they there their been have into over under about a '
           'an of in on at to for by as is are was were be it its'.split())


def words(t):
    return {w for w in re.findall(r'[a-z][a-z0-9\-]{2,}', fold(t)) if w not in STOP}


def strip_audit(h):
    """Cut every audit-only box, counting div depth.

    The first version cut with a non-greedy `<div class="audit-only">.*?</div>\\s*</div>`, which
    assumed the box held exactly one nested div. The merged-trace layout puts one <div class="hop">
    per hop inside it, so the regex stopped at the first hop's close and left the rest of the box
    on the page -- reported as 9 leaks that were the audit box itself.
    """
    out, i = [], 0
    for m in re.finditer(r'<div class="audit-only">', h):
        if m.start() < i: continue
        out.append(h[i:m.start()])
        d, j = 0, m.start()
        for t in re.finditer(r'<div\b|</div>', h[m.start():]):
            d += 1 if t.group().startswith('<div') else -1
            if d == 0:
                j = m.start() + t.end(); break
        i = j
    out.append(h[i:])
    return ''.join(out)


def main():
    papers = [x['paper'] for x in json.load(open(os.path.join(ROOT, 'results/v5_papers.json')))]
    leaks, coincid, n = [], [], 0
    for p in papers:
        f = os.path.join(ROOT, 'results/v2p5/pages', p + '.html')
        if not os.path.exists(f): continue
        h = re.sub(r'data:image/[^"]+', '', open(f).read())
        outside = strip_audit(h)
        fo = fold(outside)
        gp = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))['graph']
        g = json.load(open(os.path.join(ROOT, gp)))
        ourw = set()
        for node in g['nodes']: ourw |= words(node.get('label'))
        for x in json.load(open(os.path.join(ROOT, 'results/v3', p, 'hops.json')))['hops']:
            for k in ('cause', 'effect'):
                raw = x['_matmech_span_DO_NOT_PROMPT'][k] or ''
                sp = fold(raw)
                n += 1
                if len(sp) < 25 or sp not in fo: continue
                novel = words(raw) - ourw
                (leaks if novel else coincid).append((p, x['id'], k, raw, sorted(novel)[:5]))
    print(f"{len(papers)} pages, {n} spans checked")
    print(f"  genuine leaks: {len(leaks)}")
    for p, i, k, raw, nv in leaks:
        print(f"    {p[:44]} {i} {k}: {raw[:70]}  novel words {nv}")
    print(f"  coincidental matches, every content word already in our graph: {len(coincid)}")
    for p, i, k, raw, _ in coincid:
        print(f"    {p[:44]} {i} {k}: {raw[:70]}")
    return 0 if not leaks else 2


if __name__ == '__main__': sys.exit(main())
