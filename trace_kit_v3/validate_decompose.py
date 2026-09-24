"""validate_decompose.py: step 2 -- test the new matcher against known positives before trusting it.

The expectations below are **fact-level and hand-checked**, one row at a time.

They used to be figure-level: `KNOWN` was `our_claims_from_those_figures` straight out of
unattached.jsonl -- every claim our graph reads from the figures a hop cites. That is the right set
to *search within* and the wrong set to *require a hit in*. A figure carries several facts, so a hop
can cite a figure our graph reads and still have no claim stating its fact. Two of the six rows were
unsatisfiable by any correct matcher:

  adfm M4    only F6 claim is n21, "atmospheric ageing turns the SC surface into a PC-like dual
             emitter". The hop is about domain size governing the transition and PL. Shared figure,
             different fact. n21 is now a NEGATIVE: matching it is an error.
  Biomat M4  n24, "ALP activity does not differ among MBG, 2Co- and 5Co-MBG", was listed as a claim
             that could satisfy "improved osteogenesis". It cuts against it. Also a negative now.

`must` = at least one of these (the fact, stated anywhere in the paper).
`must_not` = matching any of these is an error (neighbouring fact, or the figure-level trap).
Claims in neither set are allowed but not required.
"""
import json, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RM = 'Rare_Metals__s12598-012-0515-6'
ADFM = 'Advanced_Functional_Materials__10.1002_adfm.202008088'
BIO  = 'Biomaterials__j.biomaterials.2011.11.042'
NL   = 'Nano_Letters__10.1021_acs.nanolett.6b04294'

KNOWN = {
 (ADFM, 'M3'): (['n12', 'n14', 'n2', 'n19'], [],
    'UNDERDETERMINED BY TEXT. The effect asserts a link, transition characteristics -> optoelectronic '
    'performance. n2/n19 state the whole link; n12/n14 state the transition side only. On the effect '
    'text alone n2/n19 is the better read, and the matcher argues exactly that. What picks n12/n14 out '
    'is the hop citing F2, which the matcher is deliberately not shown -- showing it would rebuild the '
    'figure-level trap this table exists to remove. So either is accepted here, and the thing that '
    'matters, whether the hop reaches any evidence at all, is measured below instead.'),
 (ADFM, 'M4'): (['n2', 'n19'], ['n21'],
    'effect is domain structure -> transition + PL, which n2/n19 state. n21 is ageing: same figure, '
    'different fact.'),
 (BIO,  'M4'): (['n16'], ['n24'],
    'anti-bacterial is n16. n24 says ALP does not differ, which cuts against improved osteogenesis.'),
 (NL,   'M1'): (['n5'], ['n4', 'n4b'],
    'mesopores is n5. n4/n4b are phase identity and fraction: different fact, same figure.'),
 (NL,   'M2'): (['n7', 'n8'], ['n18'],
    'Li-vs-Na performance is n7 and n8. n18 is why Na fades: a mechanism, not the fact.'),
 (NL,   'M3'): (['n17'], ['n18', 'n21'],
    'same fact as M2 inverted; n17 measures it as degree of oxidation, 36% vs 91%. n18 is the '
    'mechanism, n21 a downstream recommendation.'),
 (RM,   'M1'): (['s6'], [], 'carried over from step 1'),
 (RM,   'M1b'): (['s1'], [], 'carried over from step 1'),
}
PAPERS = sorted({ADFM, BIO, NL, RM, 'Acta_Materialia__10.1016_j.actamat.2021.116797'})


def main():
    ok = True
    print("=== known positives, fact-level (must reach one of `must`, must avoid every `must_not`)")
    for (p, h), (must, must_not, why) in KNOWN.items():
        hop = 'M1' if (p == RM) else h
        d = json.load(open(os.path.join(ROOT, 'results/v3', p, 'decompose.json')))
        got = d['hops'].get(hop, {}).get('effect', {}).get('claims', [])
        hit = sorted(set(got) & set(must))
        bad = sorted(set(got) & set(must_not))
        v = 'PASS' if (hit and not bad) else ('FALSE POSITIVE' if hit else 'MISS')
        print(f"  {p[:30]:30s} {h}  got={got}")
        print(f"     must={must} hit={hit}   must_not={must_not} matched={bad}   {v}")
        if v != 'PASS':
            ok = False
            print(f"     why this row: {why}")

    print("\n=== attachment reach: do the matched claims carry any image support?")
    reach = collections.Counter(); dead = []
    for p in PAPERS:
        d = json.load(open(os.path.join(ROOT, 'results/v3', p, 'decompose.json')))
        st = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))
        g = json.load(open(os.path.join(ROOT, st['graph'])))
        N = {n['id']: n for n in g['nodes']}
        for h, v in d['hops'].items():
            cs = v['effect']['claims']
            ev = [c for c in cs if N.get(c, {}).get('image_support') in ('shown', 'partial')]
            k = 'no match' if not cs else ('reaches evidence' if ev else 'text-only claims')
            reach[k] += 1
            if k == 'text-only claims': dead.append((p, h, cs))
    for k, n in reach.most_common(): print(f"  {k:20s} {n}")
    if dead:
        print("  hops matching only claims with no image support (these can carry no trace):")
        for p, h, cs in dead: print(f"    {p[:32]:32s} {h}  {cs}")

    print("\n=== agreement with the lexical matcher, per hop")
    both = only_model = only_lex = 0
    rows = []
    for p in PAPERS:
        st = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))
        d = json.load(open(os.path.join(ROOT, 'results/v3', p, 'decompose.json')))
        for h in st['hops']:
            lex = {s['claim'] for s in h['sub_claims']}
            mod = set(d['hops'].get(h['hop'], {}).get('effect', {}).get('claims', []))
            both += len(lex & mod); only_model += len(mod - lex); only_lex += len(lex - mod)
            if lex - mod: rows.append((p, h['hop'], sorted(lex - mod)))
    print(f"  matched by both: {both}   only the model: {only_model}   only lexical: {only_lex}")
    if rows:
        print("\n  'only lexical' pairs, to judge by eye (model miss, or lexical false positive):")
        for p, h, cs in rows: print(f"    {p[:32]:32s} {h}  {cs}")

    print("\n=== discrimination")
    tot_m = tot_h = pairs = 0
    for p in PAPERS:
        d = json.load(open(os.path.join(ROOT, 'results/v3', p, 'decompose.json')))
        n = d['n_spine_claims']
        for h, v in d['hops'].items():
            tot_m += len(v['effect']['claims']); tot_h += 1; pairs += n
    print(f"  {tot_m/tot_h:.2f} claims per hop (stop rule: >3)   "
          f"{tot_m}/{pairs} = {tot_m/pairs:.1%} of all hop-claim pairs (stop rule: >50%)")
    if tot_m / tot_h > 3 or tot_m / pairs > 0.5: ok = False; print("  NOT DISCRIMINATING")
    print("\n" + ("VALIDATION PASSED" if ok else "VALIDATION FAILED -- fix the agent before rerunning"))
    return ok


if __name__ == '__main__': sys.exit(0 if main() else 1)
