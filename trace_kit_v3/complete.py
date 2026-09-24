"""complete.py: graph completion after net-decompose. Deterministic, no model call.

A matched claim with no support cannot carry a trace. When the paper states the same fact again one
edge away, on a claim that IS supported, this step **replaces** the unsupported claim with that one.
It never adds beside: the hop is meant to land on the evidence-bearing statement of its fact, not to
accumulate restatements.

Two guards, because a supported neighbour is usually NOT the same fact. `n20 --supports--> n21`
joins "PCO is poorly Na-active" to "metal sulfides are better sodiation hosts", a downstream
recommendation; `n17 --supports--> n24` joins a scaffold claim to "ALP activity does not differ".
Both are `must_not` rows in the frozen test, so a careless completion would manufacture the very
errors the test forbids. So a candidate must:

  1. be supported under support.py (direct `evidences` edge from an observation with panels),
  2. match the hop's effect at least as well as the claim it replaces, by the same TF-IDF cosine
     stitch.py uses (word 1-2 grams + char_wb 3-5 grams over the shared normaliser), and
  3. clear MATCH_MIN = 0.12 absolutely -- stitch.py's existing threshold for "counts as part of
     this hop's effect".

Guard 3 is not optional. Without it guard 2 is satisfied by noise whenever the replaced claim
scores near zero, and the first run of this step duly proposed `n17 -> n24` on Biomaterials M4
(0.055 -> 0.084), inserting "ALP activity does not differ" -- a `must_not` row -- and
`n20 -> n12` on Nano Letters M2/M3 (0.009 -> 0.052), swapping the Li-vs-Na comparison for a
lithiation mechanism. Both cleared guard 2. Neither clears 0.12.

Guards 2 and 3 are what make the step a restatement rather than a walk: the replacement has to look
like the effect itself, not merely sit next to something that does.

The floor also rejects `n19 -> n14` on adfm M3/M4 (0.027 -> 0.054), which would have been a good
replacement -- n14 is the transition measurement. adfm's effect span is abstract enough that nothing
in that graph clears the floor, so the lexical signal cannot separate the good swap from the bad
ones. That is a limit of the method, recorded rather than tuned around.

Reach stays one step. A claim two edges from a supported restatement is not completed -- Nano
Letters n17 is exactly that case, a sibling of the matched n20 through n18 rather than a neighbour.

Every verdict is model against model.

  python3 trace_kit_v3/complete.py        rewrites results/v3/<paper>/decompose.json in place
"""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normalize import fold
from support import claim_support, supported

MATCH_MIN = 0.12   # stitch.py's threshold: below this a claim is not part of the hop's effect
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

PAPERS = json.load(open(os.path.join(ROOT,'results/v5_papers.json')))
PAPERS = [x['paper'] for x in PAPERS]


def sims(claim_ids, labels, effects):
    vw = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), sublinear_tf=True, min_df=1)
    vc = TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5), sublinear_tf=True, min_df=1)
    t = [fold(l) for l in labels]; e = [fold(x) for x in effects]
    Mw = vw.fit_transform(t + e); Mc = vc.fit_transform(t + e)
    s = 0.5 * cosine_similarity(Mw[len(t):], Mw[:len(t)]) + \
        0.5 * cosine_similarity(Mc[len(t):], Mc[:len(t)])
    return s


def run(write=True):
    log = []
    for p in PAPERS:
        st = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))
        g = json.load(open(os.path.join(ROOT, st['graph'])))
        hops = json.load(open(os.path.join(ROOT, 'results/v3', p, 'hops.json')))
        d = json.load(open(os.path.join(ROOT, 'results/v3', p, 'decompose.json')))
        N = {n['id']: n for n in g['nodes']}
        sup = claim_support(g)
        nb = {}
        for e in g['edges']:
            s, t = e.get('src'), e.get('dst')
            if s in N and t in N:
                nb.setdefault(s, set()).add(t); nb.setdefault(t, set()).add(s)
        cids = [n['id'] for n in g['nodes'] if not (n.get('type') or '').startswith('OBS')]
        idx = {c: i for i, c in enumerate(cids)}
        hids = [h['id'] for h in hops['hops']]
        S = sims(cids, [N[c].get('label') or '' for c in cids],
                 [h['_matmech_span_DO_NOT_PROMPT']['effect'] for h in hops['hops']])
        for hi, hid in enumerate(hids):
            rec = d['hops'].get(hid, {}).get('effect')
            if not rec: continue
            out, seen = [], set()
            for c in rec['claims']:
                if supported(sup, c) or c not in idx:
                    if c not in seen: out.append(c); seen.add(c)
                    continue
                base = S[hi][idx[c]]
                best = None
                for m in nb.get(c, ()):
                    if m not in idx or not supported(sup, m): continue
                    if S[hi][idx[m]] < base: continue        # guard 2: at least as good as what it replaces
                    if S[hi][idx[m]] < MATCH_MIN: continue    # guard 3: and good enough absolutely
                    if best is None or S[hi][idx[m]] > S[hi][idx[best]]: best = m
                if best is None:
                    if c not in seen: out.append(c); seen.add(c)
                    continue
                log.append({'paper': p, 'hop': hid, 'replaced': c, 'with': best,
                            'sim_replaced': round(float(base), 3),
                            'sim_with': round(float(S[hi][idx[best]]), 3),
                            'replaced_label': (N[c].get('label') or '')[:90],
                            'with_label': (N[best].get('label') or '')[:90]})
                if best not in seen: out.append(best); seen.add(best)
            rec['claims_before_completion'] = rec.get('claims_before_completion') or rec['claims']
            rec['claims'] = out
        if write:
            d['graph_completion'] = 'complete.py: unsupported matched claims replaced by a supported ' \
                                    'one-edge neighbour that matches the effect at least as well'
            json.dump(d, open(os.path.join(ROOT, 'results/v3', p, 'decompose.json'), 'w'), indent=1)
    return log


def main():
    log = run(write=True)
    print(f"{len(log)} replacements\n")
    for r in log:
        print(f"  {r['paper'][:28]:28s} {r['hop']}  {r['replaced']} -> {r['with']}   "
              f"sim {r['sim_replaced']} -> {r['sim_with']}")
        print(f"      was : {r['replaced_label']}")
        print(f"      now : {r['with_label']}")
    json.dump(log, open(os.path.join(ROOT, 'results/v3/completion_log.json'), 'w'), indent=1)


if __name__ == '__main__': main()
