# Judge review: Advanced_Functional_Materials__10.1002_adfm.202005093

**Judge:** senior investigator  
**Verdict:** accept with edits

## Round-4 checklist

- **spine**: 14 spine nodes, connected: need -> hypothesis -> bulk Bi -> exfoliation -> reduction -> metallic Bi + 2D plates -> 0.69 eV gap -> 808 nm absorption -> photothermal / (branch) 660 nm ROS -> joint cause of tumour eradication with synergy MEC -> conclusion
- **evidence**: every spine STR/PRP/PRF/MEC claim has OBS evidence (s1 o1/o3/o4, s2 o6/o7, p1 o8, p2 o9, p3 o10/o11/o13, p4 o12, m1 o15, f1 o14)
- **v04 rules**: PRP property_family set (optical, thermal, photochemical); o9/o11 fitted_parameter with fit_model; pharmacokinetic MEC/pathway for accumulation (r04 #17) correct
- **mm_ops**: all name the figure act
- **audits**: 3 (o2 residual oxide reflection, o5 XPS dominated by Bi2O3, l1 7 W cm-2 dose); fair and bearing on s1 and f1

## Changes

- o11, o14, o15: cue-dropped panels restored (F3h, F5f, F5d); false 'micrograph' cues on plots recorded in cue_overrides; fig_panel attrs removed
- o7, s2: bismuthene plate size corrected to ~250-350 nm (re-measured on F2c)
- o12, o13, o16, o17, o18: source figure -> text; each needs a caption-only fact (laser wavelength, tumour site, 28 d)
- p4, f1, f2, f3, m2: requires_unseen filled with the caption-only facts they inherit
- m2: note that CT contrast still rises at 6 h while PA peaks at 4 h

## Panel checks (every cited crop opened)

| node | panel ids | ruling | correct id | note |
|---|---|---|---|---|
| h2 | F1b | confirmed |  | schematic: PA/CT imaging, 660 nm ROS, 808 nm ablation by BNs-BSA |
| d1 | F1a | confirmed |  | bulk Bi as feedstock in schematic |
| c1 | F1a | confirmed |  | intercalation & exfoliation with H2O, 5.62 A |
| c2 | F1a | confirmed |  | NaBH4 reduction step |
| c3 | F1a | confirmed |  | surface modification with BSA -> BNs-BSA |
| o1 | F2k | confirmed |  | red (012),(104),(110)... on bismuthene trace, PDF#05-0519 |
| o2 | F2k | confirmed |  | black (321) on bismuthene trace near 33 deg |
| o3 | F2l | confirmed |  | bismuthene: ~70, ~97 cm-1 only; oxide bands absent |
| o4 | F2h | confirmed |  | 0.227 nm fringes |
| o5 | F2m | confirmed |  | bismuthene Bi 4f: Bi2O3 doublet larger than Bi0 doublet; Bi0 grows vs oxide sample |
| o6 | F2j | confirmed |  | AFM profile 14 nm, one flake |
| o7 | F2c | confirmed |  | plate size re-measured against 200 nm bar: ~250-350 nm (was 150-250 nm); label and s2 corrected |
| o8 | F2n | confirmed |  | 0.69 eV intercept; fit window ~0.7-1.7 eV |
| o19 | F2o | confirmed |  | 1665/1542 cm-1 bands in BSA and BNs-BSA |
| o9 | F3c | confirmed |  | alpha = 6.4 L g-1 cm-1, R2 0.9999 |
| o10 | F3e | confirmed |  | IR images by concentration and time; staff re-pointed from F3d (false micrograph cue) to F3e, which also plainly shows the series; kept |
| o11 | F3h | confirmed |  | RESTORED: heating/cooling curve and -ln(theta) fit with tau_s 133.4, eta 19.4%; false micrograph cue |
| o12 | F3b | confirmed |  | 0.73 vs ~0.93 at 30 min; axis says 421 nm (caption 470 nm) |
| o16 | F4f | confirmed |  | data labels 0.26, 0.13, 0.32, 0.94, 0.60, 0.31 |
| o17 | F4h | confirmed |  | ~70 -> ~125 HU over 6 h |
| o18 | F4a | confirmed |  | bars within error except WBC ~50 vs ~35 |
| o13 | F5c | confirmed |  | ~49 vs ~41 C at 5 min; axis ends at 5 min |
| o14 | F5f | confirmed |  | RESTORED: day-22 ranking matches label; false micrograph cue |
| o15 | F5d | confirmed |  | RESTORED: individual growth curves; 808-only regrowth in 4/5 mice; false micrograph cue |

Distinct crops opened: 20; node-panel rulings: 24; overturned: 0.

## Technique mismatches

- none

## Cue overrides

- {"node": "o11", "panel": "10.1002/adfm.202005093#F3h", "cue": "micrograph", "why": "F3h is the photothermal heating/cooling plot with the -ln(theta) fit; no scale bar exists, the cue is an OCR misfire. It is the only panel carrying tau_s and eta."}
- {"node": "o14", "panel": "10.1002/adfm.202005093#F5f", "cue": "micrograph", "why": "F5f is the mean tumour-volume vs time plot; false scale-bar hit. It is the panel the day-22 ranking is read from."}
- {"node": "o15", "panel": "10.1002/adfm.202005093#F5d", "cue": "micrograph", "why": "F5d is the individual tumour-growth curves; false scale-bar hit. It is the panel showing 808 nm-only regrowth."}

## Source / requires_unseen changes

- {"node": "o12", "was": "figure", "now": "text", "requires_unseen": ["660 nm irradiation (F3 caption)", "DPBF as the ROS probe (F3 caption)"]}
- {"node": "o13", "was": "figure", "now": "text", "requires_unseen": ["808 nm laser at 7 W cm-2 (F5 caption)", "readout is the tumour site of 4T1-bearing mice (F5 caption)"]}
- {"node": "o16", "was": "figure", "now": "text", "requires_unseen": ["PA signal is measured in tumour tissue (F4 caption)"]}
- {"node": "o17", "was": "figure", "now": "text", "requires_unseen": ["CT contrast is measured at the tumour (F4 caption)"]}
- {"node": "o18", "was": "figure", "now": "text", "requires_unseen": ["28 days post-injection, Kunming mice, n=3 (F4 caption)"]}
- {"node": "p4", "was": "inferred", "now": "inferred", "requires_unseen": ["660 nm irradiation and DPBF probe (F3 caption)"]}
- {"node": "f1", "was": "inferred", "now": "inferred", "requires_unseen": ["4T1 tumour-bearing mice, 7 W cm-2 808 nm (F5 caption)"]}
- {"node": "f2", "was": "inferred", "now": "inferred", "requires_unseen": ["PA/CT readouts are at the tumour (F4 caption)"]}
- {"node": "f3", "was": "inferred", "now": "inferred", "requires_unseen": ["28 days post-injection (F4 caption)"]}
- {"node": "m2", "was": "inferred", "now": "inferred", "requires_unseen": ["PA signal is from the tumour (F4 caption)"]}

## Mode changes

- none

## MatMech comparison (read after the graph was final; graph not edited)

Tally: supports 5, contradicts 0, not covered 0.

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | water-mediated freezing-thawing exfoliation + NaBH4 reduction | few-layer 2D ultrathin bismuthene nanosheets | supports | c1, c2, s1, s2, o6, o7 | graph has water intercalation/exfoliation (c1) -> 2D plates (s2) and reduction (c2) -> metallic Bi (s1); freezing-thawing itself is not in the captions. Graph reads 14 nm as tens of layers (o6), not 'few- or single-layered' |
| M2 | few-layer 2D bismuthene | strong NIR absorption; 0.69 eV gap | supports | s1, s2, p1, p2, o8, o9 | s1+s2 joint cause p1 (0.69 eV) -> p2 (6.4 L g-1 cm-1 at 808 nm) |
| M3 | photothermal conversion efficiency (19.4%) | photothermal tumour ablation | supports | p3, f1, m1, o11, o13, o15 | p3 causes f1 jointly with p4; o15 shows 808 nm alone leaves regrowth, which the graph uses for the synergy MEC |
| M4 | ROS generation under 660 nm | photodynamic tumour cell death | supports | p4, f1, m1, o12 | graph routes PDT into the joint therapy claim; 660 nm alone only slows growth (o15 note). MatMech '410 nm' disagrees with the F3b axis (421 nm) and the caption (470 nm) |
| M5 | 2D bismuthene nanosheets | PA/CT imaging-guided treatment | supports | p2, k1, m2, f2, o16, o17 | graph attributes imaging to NIR absorption (p2 -> f2) and high Z of Bi (k1), with tumour accumulation (m2); it does not credit the 2D morphology directly |
