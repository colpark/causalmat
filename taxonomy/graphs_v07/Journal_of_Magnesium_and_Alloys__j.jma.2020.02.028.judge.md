# Judge review: Journal_of_Magnesium_and_Alloys/j.jma.2020.02.028

**Verdict:** accept with minor fixes. 19 spine nodes, 49 total, one connected stage-ordered path (single-T ECAP screen -> down-select variable-T ECAP -> EPT -> SRX grains -> properties -> comparison -> conclusion). 2 audits (o7, o22), fair.

## Checklist

- spine_primary_argument: yes: need -> SRX hypothesis -> AZ61 + 160 deg ECAP/EPT route and sweep -> single-T ECAP -> twins (373 K) vs DRX (423/473 K) -> stored-energy MEC -> YS vs passes -> down-select variable-T ECAP -> refined elongated grains -> EPT -> ~1 um SRX grains -> YS 330/UTS 448/15% -> above literature -> conclusion
- spine_nodes: 19
- total_nodes: 49
- connected: True
- spine_evidence: every spine STR/PRP has an evidences edge (n7 o2; n8 o3,o4; n9 o5,o6; n13 o8; n15 o15,o16; n18 o9,o10); n19 evidenced by o20; MEC n10 argued, n17 evidenced by o19
- v04_rules: types, rels, modalities valid; one connectivity fix
- mm_ops: each names the figure act; no change
- audits: 2 audit nodes (o7 F15 pass-1 crossover vs text; o22 particles barely resolved in best sample), both fair

## Changes
- added edge n3->n6 realizes: spine node n3 (AZ61 base system) had its only outgoing edge to off-spine n23, a dead end on the spine
- n13 requires_unseen += non-equiaxed/elongated grain claim (linked text of Fig. 6; not resolvable in F6 OM)
- n7 requires_unseen += stored deformation energy interpretation (linked text of Fig. 15)
- o19 image_note: the ranked panels F7c/F9c/F10d also differ in pulse parameters (30us-10min, 40us-10min, 25us-10min), so the ranking conflates ECAP state with EPT dose

## Panel checks (every cited crop opened; 14 crops, 38 node-panel citations)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| n9 | F15, F12 | confirmed | - | F15 YS vs passes: 373 K 120/200/220/300, 423 K 140/180/200/230/150 MPa as labelled; F12 shows the 4-pass curves at 373/423/473 K ranking in yield, consistent with the temperature effect |
| n13 | F6a, F6b | confirmed | - | b finer and more uniform than a (OM, 10 um bar); elongation and dislocation density not resolvable, partial is right |
| n15 | F10d, F11a | confirmed | - | F11a IPF map equiaxed grains ~0.5-1.5 um; F10d SEM features ~0.3-0.8 um, boundaries less distinct |
| n18 | F12, F13 | confirmed | - | F12 navy 423K-8+373K-3: knee ~350, max ~420, end ~0.095; F13 blue: knee ~335-340, max ~447, end ~0.15 |
| n19 | F14 | confirmed | - | this-study points ~(275,380), (295,355), (335,448) above every literature point (max YS ~240, max UTS ~318) |
| n16 | F11a, F11c | confirmed | - | pole figure maxima at the rim near TD; Max=3.85 (a) vs 4.57 (c); c grains coarser |
| n21 | F10b, F10c | confirmed | - | bright particles <0.2 um inside grains and on boundaries; identity Mg17Al12 is text |
| o5 | F15 | confirmed | - | trend read correctly |
| o6 | F12 | confirmed | - | 373K-4 max ~350 MPa ending ~0.06; as-received peak ~300 MPa at ~0.165 |
| o7 | F15 | confirmed | - | pass 1: 373 K 120 < 423 K 140 MPa; order reverses from pass 2, as stated |
| o8 | F6a, F6b | confirmed | - | as stated |
| o9 | F12, F13 | confirmed | - | values read correctly (knee ~330-340) |
| o10 | F13 | confirmed | - | max ~447 vs ~370 (red) and ~356 (black) |
| o14 | F10a, F10b, F10c | confirmed | - | a deformed elongated relief; b,c equiaxed grains ~1-3 um with grooved boundaries |
| o15 | F10d | confirmed | - | fine features ~0.3-0.8 um at the same 2 um bar |
| o16 | F11a, F11c | confirmed | - | a ~0.5-1.5 um; c ~1.5-3.5 um |
| o17 | F11a, F11c | confirmed | - | Max=3.85 and Max=4.57 annotations; read_from annotation correct |
| o19 | F7c, F9c, F10d | confirmed | - | F7c ~5-10 um, F9c ~15-35 um with twinned remnants, F10d ~0.3-0.8 um; ranking holds, but pulse parameters differ between panels (noted in image_note) |
| o20 | F14 | confirmed | - | as stated |
| o21 | F10b, F10c | confirmed | - | as stated |
| o22 | F10d, F10b, F10c | confirmed | - | d shows few, indistinct bright spots in rough relief, unlike b,c; fair audit |

Overturned: 0. Uncited whole figures F1-F5, F7-F9 were also opened; the OBS/claim labels citing them by figs (o1-o4, o11-o13, n4, n7, n8, n22, n24) match the images.

## Technique mismatches

None.

No cited panel conflicts with its cue classes: F6a/b, F10a/c/d, F11c carry 'micrograph', compatible with OM/SEM/EBSD; F7c, F9c, F10b, F11a have no cue; F12-F15 have no OCR. o18 (EBSD misorientation histograms) keeps its staff-dropped citation of F11b/F11d: their XRD cue (from 'Angle(deg)') is a misfire, but the override rule covers only false 'micrograph' cues, so the node carries figs=[F11] with fig_panel_read F11b,d. read_from: o17 restates 'Max=3.85'/'Max=4.57' and is 'annotation'; no other OBS restates a listed annotation.

## Mode changes

None. n18 is the only claim with >=2 causes edges (n15, n21); no caption or figure shows a choice between them, joint kept

## Source checks

- n13 requires_unseen extended (elongated/non-equiaxed grains are text only)
- n7 requires_unseen extended (stored-energy interpretation is text only)
- all other source/requires_unseen fields checked: table-only values (Tables 1-4) and sample identities from captions are listed; figure-sourced nodes (n4, n9, n18, n19) are readable from the cited figures

## MatMech (read after the graph was final; graph not edited)

Supports 6 · contradicts 0 · not covered 1

| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | 160 deg ECAP at 373 K, 4 passes -> high dislocation density, limited DRX | supports | n6, n7 |
| M2 | variable-temperature ECAP 423 K-8 + 373 K-3 -> elongated, highly deformed structure, high dislocation density, suppressed DRX | supports | n12, n13 |
| M3 | EPT 25 us-10 min on variable-T ECAPed AZ61 -> ultrafine equiaxed ~1 um grains, high HAGB fraction | supports | n14, n15, n16 |
| M4 | ultrafine grains with high HAGB fraction -> higher YS and UTS | supports | n15, n18 |
| M5 | fine Mg17Al12 precipitates dispersed at boundaries -> precipitation strengthening, higher YS/UTS | supports | n21, n18, o22 |
| M6 | weakened basal texture and more HAGBs -> higher tensile elongation (15%) | not_covered | n16 |
| M7 | combined variable-T ECAP + EPT 25 us-10 min -> YS 330, UTS 448 MPa, TEF 15%, best of all samples | supports | n12, n14, n15, n18, n19, n20 |

Notes: M4 is supported for the grain-size term only; the graph does not link HAGB fraction (n16) to strength. M5 is supported but qualified by o22 (particles barely resolved in the best sample F10d). M6 is not covered: n16 (texture, HAGB) has no edge to a property claim.
