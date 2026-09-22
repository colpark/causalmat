# Judge review: Advanced_Functional_Materials/10.1002_adfm.201604687

**Verdict:** accept with minor fixes

## Round-4 checklist
- Spine: 16 nodes (s1-s6, c1, c2, m1, st1, c3, m2, st2, p1, f1, d1). They read as the paper's argument: embedded-K hypothesis, lotus organs, HCl-wash control branch, pyrolysis, S > L area, the washed carbons converge, alkali identification and etching pathway, capacitance, cycling, conclusion, with celery/asparagus as the second branch. It was connected but held one cycle (m1 -> st1 -> m2 -> m1); the cycle is now removed.
- Evidence: every spine STR/PRP/PRF has an incoming evidences edge (s5 from o1; st1 from o8, o9, o13; c3 from o8, o10; st2 from o18, o19; p1 from o15; f1 from o17).
- v04: all types, rels and mm_ops are valid; every OBS-with-figure edge carries an op; no dangling edges.
- mm_ops name the reader's act. o3 now does the before/after comparison.
- Audits: 3 (o18 contrasts, l1 limitation, new o22). They are fair: the image notes record the text/figure discrepancies (o13 at 900 C, o18 CL 570 vs '<500', o12 partial).
- Total 51 nodes: above the 25-40 aim, but the extras are side claims and none are on the spine. Left as is.

## Changes
- o3 and x3: added F1a, F1c (organ SEM) to panel_ids and F1 to figs; o3 label rewritten as the before/after comparison that x3 ('organ morphology preserved') needs. The carbon SEMs alone cannot show inheritance
- removed edge m2 -> m1 (supports): it closed the spine cycle m1 -explains-> st1 -supports-> m2 -supports-> m1. m1 is still reached from s5 (causes) and reaches d1 through st1 -> m2 and st2
- m2 requires_unseen: added 'HCl wash removed most metals (ICP, Table S2)'. The decoupling identification rests on that fact, and no panel shows it
- techniques put in controlled FAMILY:mode form: SORPTION:N2/SORPTION:BET -> PHYS:surfacearea (o8, o13, o18, o19), PHYS:porosity (o9, o10 DFT PSD); TGA -> THERMAL:TGA (o11, o12); ECHEM:GCD -> ECHEM:galvanostatic (o17). ICP kept: no family exists in normalize_technique.py (maps to OTHER)
- o5 read_from axis -> annotation: the (002)/(101) indexing that the node reports is printed on the panel (OCR tokens), same treatment as o6 and o11
- s5 image_note: Zn is also (marginally) higher in the leaf
- k5: added requires_unseen []
- added audit o22 (OBS/response/trend, F1e+F3d+F5d+F5e) -qualifies-> d1 (cross_check_consistency): celery leaf K (~2 g/100g) exceeds lotus leaf K (~0.9), yet CL-carbon (~330) is far below L-carbon (~1040 m2/g) at 800 C. K ranks organs within a plant but not area across plants, which bounds d1's 'K content controls porosity'. The text concedes it ('metal ions contents are not low'). Audit count is now 3 (o18, l1, o22)

## Panel checks (every cited crop opened)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| s5 | F1e | confirmed | - | ICP bars: stem total ~3.5 vs leaf ~2.3, K ~2.5 vs ~0.9 g/100g on log axis |
| st1 | F3a, F3b | confirmed | - | isotherms annotated 1610/1039; DFT PSD with S-carbon above L-carbon at ~0.9 and ~3.4 nm |
| c3 | F3a, F3b | confirmed | - | washed carbons 909/803 m2/g, flat type-I isotherms; PSD only a ~0.8 nm peak |
| p1 | F4c | confirmed | - | S-carbon 174 -> 126, L-carbon 152 -> 97 F/g; S above L at every rate |
| x1 | F2b, F2d, F2e, F2f | confirmed | - | TEM worm-like contrast (b, d); XRD broad (002)/(101) humps (e); Raman ID/IG 1.193 / 1.174 (f) |
| x2 | F2g | confirmed | - | XPS survey with only C 1s and O 1s for both carbons |
| x3 | F1a, F1c, F2a, F2c | confirmed | - | F2a/F2c confirmed; F1a/F1c (organ SEM) added so the 'preserved' comparison is visible |
| x5 | F4c | confirmed | - | 72% vs 64% retention closes from the curve end points |
| x6 | F4a | confirmed | - | near-rectangular CVs 5-500 mV/s, no redox peaks |
| x7 | F6g | confirmed | - | AS ~155 vs AL ~102 F/g at 5 mV/s |
| o1 | F1e | confirmed | - | as s5 |
| o2 | F5d, F6d | confirmed | - | celery: stem total ~7, K ~6 vs leaf ~4.5, ~2; asparagus: stem K ~7 vs leaf ~5; leaf higher in the minor metals listed in image_note |
| o3 | F2a, F2c | confirmed | - | S-carbon polygonal channel network; L-carbon layered flake with cavities; F1a, F1c added (see changes) |
| o4 | F2b, F2d | confirmed | - | TEM disordered contrast, no fringes; pores not resolved (partial kept) |
| o5 | F2e | confirmed | - | humps at ~24 and ~44 deg labelled (002), (101) |
| o6 | F2f | confirmed | - | ID/IG values printed on the panel |
| o7 | F2g | confirmed | - | C 1s and O 1s only |
| o8 | F3a | confirmed | - | four BET values printed on the isotherms; hysteresis near P/P0 0.45-0.55 on S and L |
| o9 | F3b | confirmed | - | bimodal S and L; S-carbon extra peak at ~1.6 nm |
| o10 | F3b | confirmed | - | WS/WL only a micropore peak |
| o11 | F3c | confirmed | - | 37.8 / 30.8 (stem) and 24.8 / 20.0 (W-stem) printed at 500 and 800 C |
| o12 | F3c | confirmed | - | DTG stem peaks ~190, ~245 C absent in W-stem; ~600 C feature is a faint bump (partial kept) |
| o13 | F3d | confirmed | - | S: ~225, 600, 855, 1610, 1575; L: ~20, 380, 685, 1040, 1290 m2/g at 500-900 C |
| o14 | F4a | confirmed | - | as x6 |
| o15 | F4c | confirmed | - | 174 vs 152 F/g at 5 mV/s |
| o16 | F4c | confirmed | - | as x5 |
| o17 | F4d | confirmed | - | retention 99-102% to 10 000 cycles |
| o18 | F5e | confirmed | - | CS ~1235, 1225, 1755, 2120; CL ~330, 385, 400, 570 m2/g at 800-1100 C |
| o19 | F6e | confirmed | - | 1075 and 735 m2/g printed |
| o20 | F5g | confirmed | - | CS ~156, CL ~132 F/g at 5 mV/s (85%) |
| o21 | F6g | confirmed | - | as x7 |
| o3 | F1a, F1c | confirmed | - | added by judge: organ SEM (stem honeycomb cells, layered leaf) needed for the before/after 'morphology preserved' reading; opened |
| o22 | F1e, F3d, F5d, F5e | confirmed | - | new audit node; all four crops opened |

Crops opened: F1a, F1c, F1e, F2a-g, F3a-d, F4a, F4c, F4d, F5d, F5e, F5g, F6d, F6e, F6g (23). Overturned: 0. Added: F1a and F1c on o3/x3.

## Technique mismatches
None. Every cue class is compatible with the node's technique: micrograph->SEM/TEM, XRD, Raman, XPS, thermal->TGA, electrochemistry->ECHEM:CV. The other crops have no cue class. No false 'micrograph' cue was found, so no cue overrides. The techniques were only put into controlled form (see changes).

## Mode changes
None. p1 (st1, x2) and x5 (x3, st1) stay `joint`: no caption or figure shows a choice between the causes.

## Source changes
- m2: requires_unseen [] -> ['HCl wash removed most metals from the organs (ICP, Table S2)']
- k5: added requires_unseen [] (source prior_knowledge unchanged)

## MatMech (read after the graph was final; graph not edited)

supports 3 · contradicts 0 · not covered 1

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | Pyrolysis at 800 C, N2, 3 h -> Microporous, highly disordered texture in S-carbon | supports | s6, x1, st1, o4, o5, o6 |  |
| M2 | Microporous, highly disordered texture -> BET area 1610 m2/g in S-carbon | not_covered | st1, x1, m1, m2 | graph has no texture -> area link. It holds 1610 m2/g and the micropores in one porosity claim (st1) and credits the S/L area gap to embedded-K etching (m1, m2). Disorder is equal in S and L (x1), so the graph uses it to rule out an alternative, not as a cause |
| M3 | Specific surface area 1610 m2/g -> 174 F/g at 5 mV/s in 6 M KOH | supports | st1, x2, p1, o15 |  |
| M4 | Specific capacitance 174 F/g -> 72% retention at 500 mV/s and 10 000-cycle stability | supports | p1, f1, o17, x5, o16 | cycling stability via p1 -causes-> f1. The graph credits the 72% retention (x5) to pore structure (x3, st1), not to the capacitance level |
