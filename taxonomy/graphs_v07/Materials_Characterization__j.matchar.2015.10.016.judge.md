# Judge review: Materials_Characterization/j.matchar.2015.10.016

**Verdict:** accept with minor fixes. 46 nodes, 14 spine nodes in two branches (HP: AlN liquid-phase sintering -> full density -> hardness max at 1 wt%; PS: gas entrapment -> rising porosity -> hardness loss). Every spine STR/PRP has evidence; m1 argued, m2 attributed. Two audits (o18, o19), both fair. The mode on r1 (joint) is correct.

## Checklist
- Spine reads as the primary argument: yes (h1 -> d1/d2/d3 -> p0 -> p1/p2 -> s1 -> m1 -> s2 -> r1 / s3 -> r2 -> c1).
- Spine size 14, connected, 2 branches: pass.
- Evidence on spine claims: s1 (o9, o11, o12, o21), s2 (o1, o7), r1 (o3), s3 (o2, o6, o10b), r2 (o4): pass.
- v04 types, rels and ops: all valid (checked against vocab/v04.json).
- mm_ops name the reader's act: pass.
- Audits: 2 (<= 5), both change support of a side claim (s4 BN, s8 Al2OC): fair.

## Changes
- o12, o14: restored panel_ids F5a / F5b (EDS spectrum is part of each crop); removed fig_ref; cue overrides recorded
- o16: image_support shown -> partial; AlN markers in F1b share peaks with SiC
- s5: requires_unseen extended (AlN consumption rests on text)
- o18, o19: read_from pixels -> annotation (restate legend strings AI,OC/ZrB and BN/C(Graphite))
- o6: image_note corrected (thick vs thin arrow meaning per linked text)
- o17: image_note notes BN marker in PS5 pattern

## Panel checks (every cited crop opened)

| node | panel | ruling | note |
|---|---|---|---|
| o1 | F2a | confirmed | HP series 97.5/100/99.3/100% read |
| o2 | F2a | confirmed | PS series 85.5/78.4/70.7/70.0% read |
| o3 | F2b | confirmed | HP 18.0/20.3/19.4/19.2 GPa, error bars ~+/-1 GPa |
| o4 | F2b | confirmed | PS 12.0/9.1/7.1/6.8 GPa |
| o6 | F3a | confirmed | HP0 dense faceted surface, few pores; arrow meaning corrected in image_note |
| o6 | F3b | confirmed | PS0 more dark cavities, necks |
| o7 | F4a | confirmed | dense surface, large flat transgranular facets |
| o9 | F4a | confirmed | point A spectrum: Si dominant, Zr, minor Al, N, C, B |
| o10 | F4b | confirmed | point B spectrum: Zr dominant, Si, C, B, O, small N and Al |
| o10b | F4b | confirmed | open skeleton of faceted grains with large pores |
| o10b | F3b | confirmed | PS0 comparison panel |
| o11 | F5a | confirmed | extended layered interfacial phase at thick arrows |
| o12 | F5a | confirmed (restored) | EDS spectrum lower half of F5a crop; build had dropped the id on a cue conflict |
| o13 | F5b | confirmed | rounded grains with growth terraces, necks, pores |
| o13b | F5b | confirmed | flaky agglomerate at arrow |
| o13b | F4b | confirmed | same agglomerate type at point B |
| o14 | F5b | confirmed (restored) | EDS spectrum lower half of F5b crop; build had dropped the id on a cue conflict |
| o15 | F6a | confirmed | markers ZrB2, SiC, C (Graphite), BN; no AlN/Al2O3 marker |
| o16 | F1b | confirmed | AlN markers present but stacked on SiC markers; image_support lowered to partial |
| o16 | F6a | confirmed | no AlN marker |
| o17 | F6b | confirmed | markers ZrB2, SiC, Al2OC, BN; low-angle hump |
| o18 | F6b | confirmed | all three Al2OC markers (~33, 58, 64 deg) stacked on ZrB2-marked peaks |
| o19 | F6a | confirmed | single BN marker shares ~26.5 deg peak with graphite marker |
| o21 | F7a | confirmed | bright layer ~10-40 nm (100 nm bar ~93 px) |
| o22 | F7b | confirmed | band of parallel dark fringes along boundaries at a triple junction; graphite identity from caption only |

Overturned: 0. Crops checked: 13 distinct (25 node-panel pairs; F1a is not cited).

## Technique mismatches
- o12 on F5a: EDS vs cue ['micrograph']. citation restored; crop is SEM micrograph + EDS spectrum composite, cue detector saw only the micrograph half (cue override)
- o14 on F5b: EDS vs cue ['micrograph']. citation restored; same composite crop (cue override)

Cue overrides:
- o12 / F5a / micrograph: crop holds the HP5 micrograph above its EDS spectrum; the node reads the spectrum, which is plainly in this crop; no separate EDS panel id exists
- o14 / F5b / micrograph: crop holds the PS5 micrograph above its EDS spectrum; the node reads the spectrum; no separate EDS panel id exists

Also checked read_from: o18 and o19 restate legend annotation strings, so they changed to annotation. Other OBS read_from values stand.

## Mode changes
- None. r1 has two causes edges (s2, s6); no caption or figure shows a choice between them, so joint stands.

## Source changes
- s5: requires_unseen += AlN consumption stated in text; figure cannot separate AlN from SiC peaks

## MatMech (read after the graph was final; graph not edited)

Supports 6, contradicts 0, not covered 0.

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | HP 1900C/10MPa with 1 wt% AlN | liquid phase (glassy/spinel layers) enabling full density | supports | p1, s1, m1, s2, k2 | graph carries B2O3+AlN -> Al2O3-SiO2 liquid -> LPS -> ~100% RD; metakaolinite spinel naming not in graph |
| M2 | PS with increasing AlN | increased porosity by gas entrapment; Al2OC forms | supports | p2, s3, m2, s8 | Al2OC identity qualified by o18 (all markers on ZrB2 peaks) |
| M3 | HP with 5 wt% AlN | nano-graphite at grain boundaries and BN | supports | p1, s4, s6, k1 | BN qualified by o19 (single marker shared with graphite 002) |
| M4 | fully dense HP1 with glassy phase | highest Vickers hardness in HP1 | supports | s2, r1 |  |
| M5 | high porosity and Al2OC in PS5 | lowest hardness in PS5 | supports | s3, r2 | porosity->hardness covered; Al2OC->hardness not in graph (no text basis in packet) |
| M6 | HP vs PS at 1 wt% AlN | HP1 much harder than PS1 via density difference | supports | p1, p2, s2, s3, r1, r2, c1 | MatMech PS1 RD ~92% disagrees with F2a (~78.4%); graph follows figure |
