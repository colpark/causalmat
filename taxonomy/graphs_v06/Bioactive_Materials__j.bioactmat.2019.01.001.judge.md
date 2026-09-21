# Judge review: Bioactive_Materials/j.bioactmat.2019.01.001

**Verdict:** accept with minor fixes

## Changes

- o10 image_support shown -> partial: at 2 d HP-Zn IC is sparse and HP-Mg IC sub-confluent; 'Mg, Zn near-confluent' holds only at 4 d
- o11 image_note: HP-Zn-EC (~1.85) and P-Fe-DC (~1.7) are also below the negative control at day 5 (bears on b12's 'Zn supports growth in EC')
- source text + requires_unseen on o4 (7/14 d and F2b row identity caption/layout only), b8 and o5 ('corrosion products' caption-only), o14 and o15 (EC medium caption-only)
- mode_basis added to the two joint causes edges into b12 (mode unchanged)
- checked and kept: techniques IR / ASSAY / OTHER are the normalize_technique.py families; F5 (tier C) citations correctly carry figs=[F5] with panel_ids []

## Panel checks (every cited crop opened)

| node | panel_ids | ruling | correct_id | note |
|---|---|---|---|---|
| b4 | F3c | confirmed |  | GS/SBF at 7, 14, 21, 28 d on the axis |
| b5 | F6a | confirmed |  | DC / IC (Transwell) / EC schematic |
| b16 | F6b | confirmed |  | Day 1, 3, 5 CCK-8 |
| o1 | F1a, F1b | confirmed |  | Ecorr Fe -0.70/-0.77, Zn -1.21/-1.27, Mg -1.52/-1.77 V |
| o2 | F1c | confirmed |  | icorr Mg-SBF ~18.2, Zn-SBF ~5.6, others <2 uA/cm2 |
| o3 | F1c | confirmed |  | GS: Mg ~1.4, Zn ~1.7, Fe ~1.1 uA/cm2 |
| o4 | F2a, F2b | confirmed |  | Mg pits (GS) and deep relief (SBF); source set to text (time points caption-only, F2b unlabeled rows) |
| o5 | F3a | confirmed |  | Ca/P fractions match; source set to text (corrosion products caption-only) |
| o6 | F3b | confirmed |  | PO4 3- and CO3 2- dashed markers labelled |
| o12 | F3b | confirmed |  | HP-Mg-GS 1030/560 bands as strong as or stronger than HP-Mg-SBF |
| o7 | F3c | confirmed |  | Mg-SBF 3.4 -> 2.0 mm/y; Zn <=0.55, Fe <=0.27; GS <=0.8 |
| o8 | F4a, F4b, F4c | confirmed |  | pH 7.4-8.4 start, 6.8-7.5 later; legend only in F4a |
| o9 |  | confirmed |  | F5 tier C, whole figure opened: cracked layer on HP-Mg DC (a, j), elongated cells on P-Fe (g, p) |
| o10 |  | confirmed |  | F5 whole figure opened; image_support lowered to partial (HP-Zn IC sparse at 2 d) |
| o11 | F6b | confirmed |  | day-5 values match; note added on HP-Zn-EC and P-Fe-DC below control |
| o13 | F6b | confirmed |  | HP-Mg-DC ~0.88 vs control ~1.93 at day 3; ~2.33 vs ~2.57 at day 5 |
| o14 | F6c | confirmed |  | Mg ~6.0, Fe ~1.5, Zn ~0.25 mM |
| o15 | F6c | confirmed |  | Fe ~6x Zn |

## Technique mismatches

- none (every cited crop's cue classes agree with attrs.technique)

## Mode changes

- none

## Source changes

- o4 figure -> text
- b8 figure -> text
- o5 figure -> text
- o14 figure -> text
- o15 figure -> text

## MatMech tally (read after the graph was final; graph not edited)

supports 2 · contradicts 1 · not covered 1

| pair | cause | effect | verdict | graph nodes |
|---|---|---|---|---|
| M1 | disk cutting and SiC polishing to 2000 grit | corrosion morphology and carbonate/phosphate product layers (protein, bicarbonate effects) | not_covered | b6, b7, b8 |
| M2 | carbonate/phosphate corrosion-product layer, medium composition | corrosion rate, Ecorr, icorr (slower in GS than SBF) and cytocompatibility | supports | b8, b11, b9, b10, b13, b12 |
| M3a | degradation rate and ion release (Mg 6.03, Zn 0.23, Fe 1.52 mM) | HP-Mg and HP-Zn cytocompatible, P-Fe cytotoxic | supports | b10, b13, b12, o14 |
| M3b | controlled degradation plus cytocompatibility | HP-Mg (as well as HP-Zn) suitable as tracheobronchial stent material | contradicts | b14, b15 |

Notes: M1's cause (specimen polishing) is not an argued step in the graph, which attributes the product layers to immersion (b6); its effect side is covered by b7/b8. M3b: MatMech names both HP-Mg and HP-Zn as suitable; the staff-inferred b14 singles out HP-Zn because Mg degrades fastest (b15). With captions only, the graph's verdict is inference, not a misreading of any figure.
