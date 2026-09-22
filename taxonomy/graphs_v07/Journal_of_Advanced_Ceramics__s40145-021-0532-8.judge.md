# Judge review: Journal_of_Advanced_Ceramics/s40145-021-0532-8

**Verdict:** accept with changes. 19 spine nodes, 64 total, one connected stage-ordered path with one parallel branch (Tm2 -> TCC).

Spine: n1 need -> n2 hypothesis -> n3/n4 base+modification -> n5 sweep -> n6 sintering -> n8 Sr vacancies -> n10 octahedral distortion -> n13 relaxor (n12 PNR MEC) -> n16 slim loops -> n18 Wrec/eta FOM -> n20 down-select -> n19/n21 service -> n23; branch n8 -> n14 Tm2 (n15 MEC) -> n17 TCC qualification.

Audits: 4 (o9, o24, o19 qualifies; o26 rules_out n24); fair: each records a figure reading that bounds a spine claim (abrupt nu3 drop vs 'no abrupt change'; F2d vs F5b wavenumber disagreement; Wd +68% vs 'temperature stability').

Note: 64 nodes, above the 25-40 aim; left as written (evidence nodes are distinct readings).

## Changes
- n10 split: 'TiO6 octahedral distortion strengthens' kept in n10 (spine); 'unit-cell polarity increases' -> new n25 (STR/phase/lattice, side; n8 causes n25, o3 evidences n25, k3 premise_for n25, o24 qualifies n25)
- n14 split: Tm2 emergence and upward shift kept in n14 (spine, explained by n15); 'Tm1 maximum suppressed' -> new n26 (PRP/value, side; n8 causes n26, o6 evidences n26, n26 causes n17)
- n19 split into three service claims: temperature 30-150 C kept in n19 (spine); frequency 1-100 Hz -> new n27; fatigue 10^5 cycles -> new n28 (both PRF/service_capability, side, realized by n20, support n23); o16 -> n27, o17 -> n28, o29 now also evidences n27, n28
- n21 split: fast pulse discharge (t0.9 ~0.1 us) kept in n21 (spine); temperature-stable peak current -> new n29 (PRF/service_capability, side, realized by n20, supports n23); o28 evidences and o19 qualifies moved from n21 to n29
- n12 (spine MEC, basis argued) had no OBS evidence or KNW premise: added k6 KNW/lookup (diffuse switching peaks and slim loops mark PNRs replacing long-range domains) premise_for n12
- n8 (spine STR, basis imposed) had no OBS evidence or KNW premise: added k7 KNW/fact (charge balance: 2 Bi3+ for 3 Sr2+ leaves one A-site vacancy) premise_for n8
- n24 (alternative: Tm2 = abrupt FE-PE transition) contrasts moved from n14 to n15, the mechanism it competes with; o9 (abrupt nu3 drop near Tm2) now also evidences n24, so the paper-ignored alternative carries the figure reading that favours it
- mode joint on n14->n17 and n26->n17 (n17 gained a second cause from the n14 split)
- n7, n24 source changed to text; n13 requires_unseen filled

## Splits and merges
- split n10 -> n10, n25
- split n14 -> n14, n26
- split n19 -> n19, n27, n28
- split n21 -> n21, n29
- merges: none (no two nodes state the same claim; n15 and n24 are competing mechanisms, kept apart)

## Source / read_from changes
- n7: source figure -> text; requires_unseen filled. 'pseudocubic perovskite' identification is stated in F1 linked text; the panel shows indexed reflections only
- n24: source inferred -> text; requires_unseen filled. F5 linked text itself says Tm2 corresponds to the FE-PE transition temperature
- n13: source inferred -> inferred; requires_unseen filled. 'toward an ideal relaxor' needs gamma=2 limit (prior knowledge)
- new nodes n25-n29, k6, k7 carry source and requires_unseen
- read_from: no changes. o4, o7, o3f are already 'annotation'; o27/o18/o28 cite field labels ('40kV/cm', '@80kV/cm') only as conditions, their values are read from the axes, so 'axis' stays; other listed annotations are OCR fragments or instrument strings

## Mode changes
- n14->n17, n26->n17: joint. n17 gained a second cause from the n14 split; F4 linked text credits Tm1 suppression/widening gap and the new Tm2 peak together; no caption shows a choice
- no other claim has two or more causes edges

## MatMech (read after the graph was final; graph not edited)

Supports 5 · contradicts 0 · not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | pressureless solid-state sintering with Bi-for-Sr substitution -> single pseudocubic perovskite with Sr vacancies, PNRs, grain growth and densification | supports | n6, n7, n8, n11, n12 | sintering schedule (1180-1240 C, 2 h) is not in the packet |
| M2 | Sr vacancies and PNRs -> lower Pr, PNR thermal evolution, dielectric temperature stability, stronger relaxor behaviour | supports | n8, n12, n13, n16, n15, n14, n17 | graph also carries o9 qualifying the 'no abrupt transition' step and the n24 alternative |
| M3 | increased lattice distortion and reduced grain-boundary effects -> higher eta and Wrec | supports | n10, n13, n16, n18 | distortion route only (via relaxor and slim loops); grain-boundary effects not in the graph, and grain size (n11) is side with no property link |
| M4 | Wrec 1.8 J/cm3 and eta 72% at 110 kV/cm -> pulsed-power suitability with fast discharge and fatigue endurance | supports | n18, n20, n21, n28, n19, n23 | graph links them by down-select and supports, not causes; MatMech Wd ~1.5 J/cm3 at 110 kV/cm is not on the graph (o18 has 0.44 J/cm3 at 80 kV/cm) |
| M5 | sintering with A-site defect engineering -> Wrec 1.8 J/cm3, TCC within +/-15% 40-350 C, 10^5-cycle endurance | supports | n4, n5, n6, n8, n18, n17, n28 |  |
