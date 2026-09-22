# Judge review: Nano_Letters/10.1021_acs.nanolett.6b04294

**Verdict:** accept with minor fixes. 19 spine nodes, 54 nodes, 72 edges, all v04-valid. One connected path n1a -> n2 -> n3 -> n4/n5 -> n7/n8 -> n1 (gap raised by the Na fading) -> n9, which splits into the Li in operando branch (n10 -> n12 -> n13), the Na branch (n11 -> n15 -> n16) and the AIMD claim n17. All of these meet in MEC n18, which explains n8 and supports n20. Every spine STR/PRP/PRF claim has an evidences edge; n22 is basis=argued. Audits (4, all fair): a1 (Li capacity falls after cycle ~17), a2 (Na 1st discharge ~865 mAh/g despite minor reaction), o6 (TGA residual MOF), o17 (no peak shift rules out intercalation). The mm_ops name the reader's act. Caveat: n9 fans out to three lines (Li, Na, AIMD); the AIMD line is a single claim, so it is tolerated as the control branch.

## Changes
- n7, n8: source text -> figure, requires_unseen cleared (F2a/F2c axes carry 'vs. Li/Li+'/'vs. Na/Na+' and show the 1st and 40th cycles); image_notes added
- o5: particle size re-measured against the 500 nm bar, ~250-500 nm (was ~200-400 nm)
- o11: discharge window of the low-q bend corrected to ~6-11 h (was ~1-11 h)
- o13: type OBS/signal/feature_presence -> OBS/signal/feature_quantification; label now records the small residual change at ~0.03-0.1 A-1 (paper argues 'much smaller', not absent)
- o15: 'fade to nothing' -> 'fade to a weak broad bump' (residual ~18.9 deg feature visible)
- o21: read_from axis -> annotation (end-of-charge 1.06/1.48/2.11 A values are author-drawn in the image); annotation_match added
- edge n19 -> n16: causes (mode alternative) -> contrasts; n15 -> n16 mode/mode_basis removed (single cause now)

## Panel checks (every cited crop opened: 24 crops, 43 node-panel citations)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| n4 | F1a | confirmed | - | Rietveld fit with Co3O4 and CoO tick rows, flat difference curve |
| n5 | F1c, F1d | confirmed | - | F1c type IV isotherm with hysteresis P/P0 ~0.45-1.0, inset PSD peaks ~5.4/6.8 nm; F1d SEM shows open porous agglomerates only (mesopores not resolved), F1c carries the claim |
| n7 | F2a, F2b | confirmed | - | F2a (Li/Li+ axis) 1st charge ~870, 40th ~850 mAh/g; F2b charge ~870 -> ~1050 (cycle ~17) -> ~840 at 40; partial kept; source text -> figure |
| n8 | F2c, F2d | confirmed | - | F2c (Na/Na+ axis) 1st discharge ~865, 40th ~60-70; F2d discharge 870 -> ~480 -> ~70; source text -> figure |
| n13 | F3a, F3b | confirmed | - | F3a (Li/Li+ axis) low-q contours bend to lower q ~6-11 h and stay; F3b 0.02 V and 3 V curves below OCV, hump at ~0.2-0.3 A-1 |
| n16 | F3c, F3d | confirmed | - | F3c (Na/Na+ axis) contours nearly straight; F3d curves nearly overlap, small drop at ~0.03-0.1 A-1 |
| n17 | F6d | confirmed | - | Li-Co3O4 ~91%, Na-Co3S4 ~59%, Na-Co3O4 ~36% at 2 ps |
| n4b | F1a | confirmed | - | weight fractions 78.6%/21.4% written on panel |
| o1 | F1a | confirmed | - | as stated |
| o2 | F1a | confirmed | - | annotations Wt(Co3O4)=78.6%, Wt(CoO)=21.4% present; read_from annotation correct |
| o3 | F1c | confirmed | - | hysteresis from P/P0 ~0.45-0.5 to 1.0, max uptake ~110 cm3/g |
| o4 | F1c | confirmed | - | inset PSD peaks ~5.4 and ~6.8 nm, low tail below 4 nm |
| o5 | F1d | confirmed | - | faceted agglomerates; sizes re-measured against the 500 nm bar: ~250-500 nm (was ~200-400 nm) |
| o6 | F1b | confirmed | - | drop from ~250-300 C to ~390 C, flat at 95.8 wt% (annotation) above 400 C |
| o7 | F2a | confirmed | - | plateau ~1.05 V to ~1330 mAh/g; charge plateau ~2.0 V to ~870 |
| o8 | F2b | confirmed | - | as stated; CE ~96% |
| a1 | F2b | confirmed | - | discharge ~1100 at cycle ~17 falls steadily to ~870 at 40 |
| o9 | F2d | confirmed | - | as stated |
| o10 | F2c | confirmed | - | plateau ~0.15 V; 1st charge ~470; 40th ~60-70 |
| a2 | F2c | confirmed | - | 1st Na discharge ~865 mAh/g, close to Li reversible level |
| o11 | F3a | confirmed | - | bend occurs ~6-11 h (after the 1.07 V plateau), not from ~1 h; label corrected |
| o12 | F3b | confirmed | - | OCV and 1.07 V overlap; lower curves at 0.01-0.1 A-1; 0.02 V hump at ~0.2-0.3 |
| o13 | F3c, F3d | confirmed | - | small but visible deviation in F3d; type feature_presence -> feature_quantification, label corrected |
| o15 | F4a | confirmed | - | 16.4/19.2/20.1 deg reflections fade; a weak broad ~18.9 deg bump remains; label corrected |
| o16 | F4b | confirmed | - | reflections persist with modest intensity loss |
| o17 | F4b | confirmed | - | 19.25 deg peak stays in place through discharge/charge |
| o18 | F5b | confirmed | - | 1st/2nd discharge white line ~0.97, shape of Co foil; charged curves differ from OCV |
| o19 | F5d | confirmed | - | discharged white line ~1.25 at ~7728 eV; charged ~1.32 at ~7727 eV between CoO and Co3O4 |
| o20 | F5a, F5c | confirmed | - | F5a white-line max vanishes at ~5.5 and ~13.5 h and returns on charge; F5c max persists; F5c panel says 0.1 C |
| o21 | F5e | confirmed | - | (Li/Li+ axis) oxide peaks replaced by ~2.1 A peak; drawn arrows 1.06/1.48/2.11 at end of charge; read_from axis -> annotation |
| o22 | F5f | confirmed | - | (Na/Na+ axis) ~1.5 and ~2.5 A peaks persist with small decrease |
| o23 | F6a, F6b | confirmed | - | Li penetrates and disorders top layers; Na stays mostly above; partial kept |
| o24 | F6d | confirmed | - | as stated; Na-Co3O4 flat from 0.8 ps |
| o25 | F6b, F6c | confirmed | - | Na mixes into Co3S4 top layers more than into Co3O4; partial kept |

Overturned: 0.

## Technique mismatches

None. Cue-bearing crops: F1d 'micrograph' vs o5 SEM (compatible); F2a-c 'electrochemistry' vs ECHEM:GCD (compatible). All other crops (F1a-c, F2d, F3, F4, F5, F6) carry no cue class, so there is nothing to check there. No cue overrides.

read_from: o21 changed from axis to annotation, because the end-of-charge R values are drawn in the image. o2 and o6 are 'annotation', which is correct. o12, o18, o19, o22 and o24 read curve positions against legend entries and do not restate the strings, so they stay 'axis'.

## Mode changes

- n16: causes from n15 and n19 were marked 'alternative' on the basis of F4b. The choice between minor conversion and intercalation is posed only in the F3 linked text; no caption or figure shows it (F4b only rules intercalation out, which o17 -> n19 rules_out already carries). Setting 'joint' would claim that a ruled-out intercalation co-causes n16. The edge n19 -> n16 was therefore demoted to contrasts, and n15 is now the single cause.

## Source checks

- n7, n8: text -> figure. The F2a and F2c axes identify the Li and Na cells and show the 1st and 40th cycles.
- The other text-sourced nodes (n12, n15, o8, a1, o9, o12, o15-o20, o23, o25) correctly list the caption-only cell identity or colour key. n18, n20 and n21 are inferred; k7 is prior_knowledge.

## MatMech (read after the graph was final; graph not edited)

| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | Co-MOF decomposition -> porous nanoparticle/mesopore structure | supports | n3, n5, o3, o4, o5 |
| M2 | porous structure -> Li storage better than Na | contradicts | n5, n22, n7, n8, n18, n31: the graph attributes the Li/Na gap to poor sodiation activity, not to porosity favouring Li+ |
| M3 | Co-MOF decomposition -> Na storage worse than Li | supports | n3, n4, n8, n17, n18 (the mechanism differs: AIMD activity, not ionic radius) |

Tally: supports 2, contradicts 1, not covered 0.
