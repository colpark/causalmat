# Judge review: Materials_Characterization/j.matchar.2017.11.052

**Verdict:** accept with minor fixes. 13 spine nodes, 39 total (16 claim nodes, 16 OBS, 7 KNW), one connected path HYP -> DES -> PRC -> two branches: (A) melt pools -> dimensional limit (PRF); (B) side-face heat removal -> intracellular Si / solute loss and fewer LABs -> slightly lower hardness; control n11 (grain size unchanged). Every spine STR/PRP/PRF claim has an evidences edge (n9 only via text_only o11, since paper Fig. 10 is absent). 1 audit (o15, overlapping hardness error bars), fair. All mm_ops name the reader's act.

## Changes
- o1 label and image_note: measured widths track 1:1 only down to ~1 mm (d_s 0.5 -> d_m 0.66), not ~0.5 mm; values listed
- n6 label: 'within ~15% down to ~1 mm; thinner plates increasingly wider, floor ~0.27 mm' (was 'down to ~0.5 mm')
- o3 image_note: scale assumption (only F4d has the bar)
- o9 label/image_note: sparse tail to ~400 nm in a,b; peak-bin difference noted
- added edge o4 -> n7 evidences (inspect_local_feature): F4c,d show powder attached to the side faces, the contact n7's heat-removal argument rests on

## Panel checks (every cited crop opened: 22 crops, 39 node-panel citations; whole F7 and F9 images also opened)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| n5 | F4a, F4b, F4c, F4d | confirmed | - | overlapping arc-shaped melt pools in all four OM crops; (d) strip is one to two pools wide |
| n6 | F1c | confirmed | - | d_m vs d_s on log axes with 1:1 dashed line; label tightened: close to 1:1 only down to ~1 mm (0.5 -> 0.66 mm is +32%) |
| n11 | F6b | confirmed | - | L 7.0-7.8 um, flat across 0.27-10.4 mm |
| n12 | F6a | confirmed | - | {001} ~0.18-0.22 below 3 mm, ~0.16-0.17 at 5-10 mm where {011} ~0.17-0.175 matches it; partial kept |
| n13 | F3 | confirmed | - | whole-figure crop; ~111.8 HV at 5.3/10.4 mm, ~106.6 HV at 0.27 mm with large error bar; partial kept |
| n16 | F8a, F8b, F8c, F8d | confirmed | - | histograms with annotated mean sizes 60/63/60/53 nm |
| o1 | F1c | confirmed | - | values re-read; label corrected (see changes) |
| o2 | F4a, F4b, F4c, F4d | confirmed | - | OM melt-pool arcs in all widths |
| o3 | F4a, F4d | confirmed | - | arcs ~100-120 px wide in F4a against ~40 px = 100 um bar in F4d -> ~250-300 um; visible heights ~70-100 um |
| o4 | F4c, F4d | confirmed | - | wavy side faces with attached powder spheres on both sides |
| o5 | F5a, F5b, F5c, F5d | confirmed | - | EBSD IPF-Z maps; red <001> elongated grains, fine grains at pool boundaries; coarse off-colour powder grains outside the strip in c,d |
| o6 | F6b | confirmed | - | as stated |
| o7 | F6a | confirmed | - | as stated |
| o8 | F7a, F7b, F7c, F7d | confirmed | - | crops are paper Fig. 8 SEM (Si strings along Z in a,b; scattered particles between strings in c,d) though their caption spans are the Fig. 7 EBSD caption; content matches the node |
| o9 | F8a, F8b, F8c, F8d | confirmed | - | as stated; tail detail added |
| o12 | F2b | confirmed | - | ~0.105 at the dashed solidus (~575 C), ~0.12 below ~300 C |
| o13 | F2a | confirmed | - | alloy-composition dashed line crosses liquid, alpha+liquid, alpha+Si+AlFeSi-beta, then +Mg2Si below ~400 C |
| o15 | F3 | confirmed | - | error bars overlap; 0.35-0.46 mm ~109.3 HV above 0.57-0.66 mm ~107.5 HV |
| o16 | F3 | confirmed | - | values re-read, as stated |

Overturned: 0. Uncited-by-id nodes: o14 and the n10 EBSD reading use the Sv(LAB) values printed on paper Fig. 7 in the whole F7 image (0.149/0.143/0.125 um^-1, confirmed); that figure has no panel ids because the F7 crops cover paper Fig. 8. n7 cites F9 (tier C, no panels); the schematic shows heat flow into powder vs bulk, as noted.

## Technique mismatches

None. o1 PHYS:dimension (F1c, no cue); o2-o4 OM (F4d micrograph cue genuine); o5 EBSD (F5d cue compatible); o6/o7 EBSD-derived plots (no cue); o8 SEM (F7d cue genuine); o12/o13 THERMO:CALPHAD (no cue); o15/o16 MECH:hardness (F3, no OCR); o14 EBSD (no panel id).

Cue overrides: F8a-d carry a false 'micrograph' cue (scale-bar detector fired on Si size histograms). They are the right panels for o9 and n16; SEM is cue-compatible anyway, recorded under review.cue_overrides.

read_from: o9 and o13 restate listed annotations -> 'annotation' (correct). o1, o6, o7, o12, o15, o16 read axis values and restate no listed string -> 'axis'. o2-o5, o8 -> 'pixels'. o14 'annotation' (strings on the paper Fig. 7 maps, not in the panel section).

## Mode changes

None. Only n13 has two causes edges (n9, n10); 'joint' is right: neither the F3 caption nor its linked text names a choice between them.

## Source checks

No changes. Text-dependent nodes (n1-n4, n7-n10, n14, n15, o8, o10, o11, o14, k1-k6) are 'text' with the unseen fact listed (width mapping of paper Fig. 8/7 panels, absent paper Fig. 10, SLM parameters, cited values); k7 is prior_knowledge. Figure-sourced nodes (n5, n6, n11, n12, n13, n16, o1-o7, o9, o12, o13, o15, o16) can be read from the cited crops (F4 and F8 panels carry their widths in the caption or in the image).

## MatMech (read after the graph was final; graph not edited)

Tally: supports 2, contradicts 0, not covered 0.

- **M1** SLM (380 W, 30 um layers, 150 um hatch, 67 deg) with sample width -> columnar <001>-textured alpha-Al cells with eutectic Si; more intracellular Si precipitates and fewer LABs in small samples: **supports** (nodes n4, n15, n12, n7, n8, n9, n10). graph splits the compound effect: n4 produces n15/n12; size effect runs n4 -> n7 -> n8 -> n9 and n7 -> n10. MatMech's 380 W laser power is not in the packet and is absent from n4
- **M2** intracellular Si precipitates (solute loss) and reduced LAB density -> hardness ~112 -> ~107 HV from 10 to 0.28 mm: **supports** (nodes n8, n9, n10, n13, k7, o15). n9 and n10 joint causes of n13; MatMech's Hall-Petch exclusion via unchanged grain size is only implicit (n11 contrasts n8, no edge to n13); o15 qualifies the hardness trend (overlapping error bars)
