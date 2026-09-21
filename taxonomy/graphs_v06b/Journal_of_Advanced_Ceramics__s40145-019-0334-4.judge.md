# Judge review: Journal_of_Advanced_Ceramics__s40145-019-0334-4

**Judge:** senior investigator  
**Verdict:** accept with minor edits

## Round-4 checklist

- **spine_nodes**: 13
- **connected**: True
- **spine_evidence**: s1 (o1,o2), s3 (o5,o10), s4 (o6,o7,o8), s5 (o9,o17), p2 (o12), m2 (o15); m1 basis argued
- **audits**: 0
- **note**: three parallel STR branches (s3 density, s4 platelets, s5 SiC size) all enter p2 as joint causes; one over the two-branch guide, tolerated because the paper names all three as causes and c1 uses them

## Changes

- o4 technique THERMO:gibbs -> ATOM (not a controlled family; note kept)
- o12 technique MECH:flexural/MECH:toughness -> bare MECH (no controlled mode)
- m0 source inferred -> text with requires_unseen
- c1, g1 requires_unseen list the vol% levels behind RZSZ-x; m3 requires_unseen [] added

## Panel checks (every cited crop opened)

| node | panel ids | ruling | correct id | note |
|---|---|---|---|---|
| o4 | F3 | confirmed |  | three dG lines: (1) -520 to -450, (3) ~-185 to -150, (2) ~-85 kJ/mol; reaction equations drawn on the plot |
| o5 | F4 | confirmed |  | bars labelled RZSZ-0..25 at ~91.8, 94.9, 98.5, 97.6, 96.4% |
| o6 | F5a, F5b | confirmed |  | arrows to elongated ZrB2 grains in both; F5a also labels WSi2 phase and SiC-rich region |
| o7 | F5c, F8d | confirmed |  | dashed boxes labelled interlocking microstructure on polished BSE and on fracture surface |
| o8 | F6 | confirmed |  | ZrB2 platelets labelled; platelet morphology plain |
| o17 | F6 | confirmed |  | nano-sized SiC clusters between platelets, ~100-200 nm against the 500 nm bar; size range in label is slightly low but of the right order |
| o9 | F8a, F8b, F8c | confirmed |  | Submicro-sized SiC in (a); Nano-sized SiC in (b), (c) |
| o10 | F8a, F8b | confirmed |  | Pores (a), Tiny pores (b) |
| o11 | F5d, F8e | confirmed |  | zone C box around a few large grains in F5d; Coarse ZrB2 in F8e; partial is fair |
| o12 | F7 | confirmed |  | hardness and strength/toughness vs RZSZ-x, all peaking at RZSZ-20 |
| o13 | F4, F7 | confirmed |  | density peak at RZSZ-15 vs property peak at RZSZ-20: offset holds |
| o14 | F8b, F8c, F8e | confirmed |  | Intergranular/Transgranular labels in (b),(c); Secondary crack and Coarse ZrB2 in (e) |
| o15 | F8f | confirmed |  | crack deflection, bridging, grain pull-out, branching into SiC-rich region, all labelled |
| o16 | F5e | confirmed |  | EDS spectrum with table C 11.42, Si 59.53, W 21.38, Zr 7.67 at% |

Distinct crops opened: 15; node-panel rulings: 23; overturned: 0.

## Technique mismatches

- none

## Cue overrides

- none

## Source / requires_unseen changes

- {"node": "m0", "from": "inferred", "to": "text", "why": "the B4C-consumed-first argument is the paper's linked-text reasoning, not readable from F3 alone"}
- {"node": "c1", "from": "text (requires_unseen [])", "to": "text", "why": "20 vol% needs the sample-name-to-vol% mapping"}
- {"node": "g1", "from": "inferred (no requires_unseen)", "to": "inferred", "why": "20 vol% needs the sample-name-to-vol% mapping"}

## Mode changes

- none

## MatMech comparison (read after the graph was final; graph not edited)

Tally: supports 2, contradicts 0, not covered 0.

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | in-situ reactive hot pressing with 0-25 vol% excess ZrSi2 | ZrB2 platelets, interlocking microstructure, nano SiC, WSi2 and ZrC at higher ZrSi2 | supports | p1, d2, m1, s4, s5, s2, s7 | graph gives no mechanism for SiC refinement (MatMech: liquid phase suppresses growth); schedule 1550 C/40 MPa not in graph |
| M2 | platelets, interlocking, nano SiC, secondary phases | hardness, strength, toughness peak at RZSZ-20 (17.1 GPa, 655 MPa, 6.08) | supports | s4, s5, s3, p2, m2, m3, s6, p3 | RZSZ-25 strength loss with retained toughness carried by s6 counteracts p2 and p3 secondary cracks |
