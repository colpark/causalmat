# Judge review: Journal_of_Magnesium_and_Alloys/j.jma.2013.12.002

Effect of Ca addition on grain refinement of Mg-9Li-1Al alloy

**Verdict:** accept with minor fixes. 36 nodes, 47 edges, 14 spine nodes, one connected HYP -> DSC path with two branches (as-cast alpha-Mg; as-extruded beta-Li) joined by the heterogeneous-nucleation MEC. Every spine STR claim has OBS evidence; s12 and s13 carry basis=argued. No PRP/PRF stage, which is faithful: the paper reports no property data. Audits: n2, n8, l1 (3, all fair). All ids are v04-valid.

## Changes

- s12 image_support shown -> partial: F6 shows the OR and paired spots, not the fd<6% mismatch that the claim rests on
- n8 source inferred -> prior_knowledge; requires_unseen now lists the EDS interaction-volume fact and the F2b particle size; read_from pixels -> annotation (restates the Mg/Al label placement, 'AI' listed for F2d); image_support shown -> partial
- edge n8->c1 mm_op inspect_local_feature -> assign_features (the reader judges peak-to-element assignment and overlap in a spectrum, not a local image feature)
- edge n7->c1 mm_op register_colocated_views -> assign_features (n7 cites only the spectra F2c/F2d; the A/B point locations come from the caption, listed in requires_unseen; no co-located view is read on this node)
- n12 label: 'zigzag' -> 'pseudo-zigzag' ([1-1-2] is marked 'ps' in F5)
- added k6 -> n9 premise_for: n9 names beta grains and alpha bands from the light/dark contrast lookup
- s14 source inferred -> text; requires_unseen lists the text-only mean sizes and the paper's crystallographic conclusion
- c1: dropped attrs.phase_named_from=stoichiometry (c1 names elements only, no phase; the phase is named in s8 from XRD+EDS)

## Panel checks (every cited crop opened: 16 crops, 20 node citations)

| node | panels | ruling | note |
|---|---|---|---|
| s7 | F1c, F1d | confirmed | XRD of as-cast LA91 (alpha, beta markers only) and LA91-0.2Ca (Al2Ca diamonds added) |
| s8 | F2a, F2b | confirmed | BSE: bright particles along boundary lines (F2a); isolated particle A and boundary spot B (F2b) |
| s9 | F1a, F1b | confirmed | OM: long alpha laths (a) vs blocky islands (b) |
| s10 | F3a, F3b | confirmed | OM as-extruded: beta grains visibly finer in b |
| s11 | F4a, F4b | confirmed | BSE as-extruded: uniform scatter (a); particles in light and dark regions (b); no A/B markers |
| s12 | F6 | confirmed | simulated superposed pattern with the stated OR; confirmed as the right panel, image_support lowered to partial |
| c1 | F2c, F2d | confirmed | EDS spectra with Mg, Al, Ca labels |
| n1 | F1a, F1b | confirmed | alpha-Mg/beta-Li arrow labels printed in both |
| n2 | F1a | confirmed | 100 um bar ~66 px; lath widths ~10-25 px (15-38 um), longest lath ~230 px (~350 um): audit holds |
| n3 | F1b | confirmed | granules ~15-35 px, ~20-50 um; consistent with 28.32 um text value |
| n4 | F1c | confirmed | all reflections carry alpha or beta markers |
| n5 | F1c, F1d | confirmed | Al2Ca diamonds at ~29.5, ~37 (on alpha peak) and ~80.5 deg in d only |
| n6 | F2a, F2b | confirmed | SEM:BSE, micrograph cue on F2a matches |
| n7 | F2c, F2d | confirmed | EDS spectra; Ca Ka ~3.7 keV, Mg/Al peak ~1.3 keV |
| n8 | F2c, F2d | confirmed | Mg and Al labels on one peak; confirmed |
| n9 | F3a, F3b | confirmed | 25 um bar ~60 px; beta grains ~25-50 px (a) vs ~10-20 px (b) |
| n10 | F4a, F4b | confirmed | SEM:BSE; micrograph cues match; ~2-3 um bright cluster top of F4b |
| n11 | F4c, F4d | confirmed | EDS spectra with printed Mg/Al/Ca labels (OCR missed them) |
| n12 | F5 | confirmed | (311) Al2Ca atom configuration; [1-1-2] marked 'ps' |
| n13 | F6 | confirmed | spot pairs 110L/311A, 22-2L/715A, 11-2L/404A; dashed habit-plane trace |

Overturned: 0.

## Technique mismatches

None. Micrograph cues on F1a, F1b, F2a, F3a, F3b, F4a, F4b match OPTICAL / SEM:BSE; all other crops have no cue class. No cue overrides needed. read_from checked: n4, n5, n7, n13 correctly annotation; n8 changed to annotation.

## Mode changes

None: no claim has two or more incoming causes edges (s9 <- s8 only, s10 <- s11 only).

## Source changes

- n8: inferred -> prior_knowledge (interaction-volume fact is not shown in any panel; now listed in requires_unseen)
- s14: inferred -> text (the conclusion restates the paper's text-only numbers and crystallographic conclusion; now listed)

## MatMech (read after the graph was final; graph not edited)

supports 1 · contradicts 0 · not covered 1

- M1 (melting, casting and hot extrusion (250 C, ratio 28.2) of LA91-0.2Ca -> alpha-Mg rod -> granular (28.32 um) and beta-Li refined to 4.56 um via Al2Ca heterogeneous nucleation): **supports**. graph carries cast -> Al2Ca -> alpha-Mg granular and extrude -> Al2Ca in alpha+beta -> beta 10.3 -> 4.6 um, both explained by s13 heterogeneous nucleation. Differences: the graph sets DRX (m1) apart as the refinement shared by both alloys rather than Al2Ca-stimulated DRX nucleation; E2EM matching is graphed only for beta-Li (F5/F6), the alpha-Mg matching is outside the packet; the graph's audit n2 finds the 1371.56 um rod length exceeds the imaged field
- M2 (refined alpha-Mg and beta-Li from Al2Ca nucleation -> improved mechanical properties (implied, not quantified)): **not_covered**. no property data in the packet; the graph has no PRP/PRF stage, correctly
