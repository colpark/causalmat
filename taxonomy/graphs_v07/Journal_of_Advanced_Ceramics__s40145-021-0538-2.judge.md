# Judge review: Journal_of_Advanced_Ceramics/s40145-021-0538-2

**Verdict:** accept with fixes. This review checks structure only. No figures or crops were opened, and panel citations were not ruled on. The spine has 15 nodes: gap -> add Al2O3 to YSZ -> plasma spraying. From there it branches:
- phase branch: cubic phase (n4) -> c-to-t transition (n15) -> volume-shrinkage MEC (n16) -> spalling at 5-10 cycles (n17);
- crack branch: low crystallinity (n6) -> micro-stress MEC (n8) -> larger cracks (n9), and cycling plus cubic phase -> higher micro-strain (n11). Both feed crack propagation after 5 cycles (n12) -> spalling (n17).

YSZ staying tetragonal (n19) is the control branch. n17 -> conclusion (n20). Every spine STR/PRP/PRF/MEC node has OBS evidence or a KNW premise. There are 2 audits (a1, a2), both text_silent and both fair: a1 qualifies the 10-cycle attribution of the t features, and a2 qualifies the orientation/strain correlation. The graph now has 43 nodes, slightly above the 25-40 target because of the splits.

## Changes
- Three splits (listed below). Spine is unchanged at 15.
- Added k1 -> n19 premise_for, because the tetragonal reading of F10 uses the F1 peak-splitting lookup.
- Rewired n13 -> n20 supports to n23 -> n20, since n20's "columnar grains partly block cracks" is the n23 claim.

## Splits and merges
- **n5 -> n5 + n21.**
  - n5 keeps the Al solid solution in ZrO2 (ref [11]).
  - New n21 (MEC/pathway, attributed) is Al aggregating at grain boundaries as an amorphous phase (ref [18]).
  - New edges: n21 -> n4 explains; o2 -> n21 evidences (assign_features).
- **n7 -> n7 + n22.**
  - n7 keeps "amorphous phase near the cracks".
  - New n22 (STR/microstructure/feature_size, partial) is the grain-size gradient toward the crack.
  - New edges: n22 -> n7 supports; o5 -> n22 evidences (assess_spatial_distribution).
- **n13 -> n13 + n23.**
  - n13 keeps the crack mode: intergranular in equiaxed grains, transgranular in columnar grains.
  - New n23 (PRP/value, mechanical, basis argued) is "columnar grains partly block crack propagation".
  - New edge: n13 -> n23 supports.
- Merges: none. n8/k3 and n16/k2 are an in-paper application and its premise, not duplicates.

## Source / read_from changes
- n4: figure -> text. "Mainly tetragonal with a little cubic" needs the 43-deg lookup (k1) and the Jade ~5% value.
- n19: figure -> text. The tetragonal identity needs the peak-splitting rule (k1).
- k4: prior_knowledge -> text. Griffith's theory is stated in the F2 linked text.
- o13: figure -> text. The site 1/site 2 identities come from the caption only (F6 is tier C).
- n20: stays inferred. requires_unseen is now filled.
- New nodes n21, n22 and n23 are text, with their facts listed.
- read_from: no changes. The F5 annotation strings are axis titles and legends, and o6, o7 and a2 read axis values. F1, F9 and F10 have no OCR lists.

## Mode changes
None. n11 (n10, n4), n12 (n9, n11) and n17 (n12, n15) are all joint, which is correct. The linked text couples the causes, and no caption shows a choice.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 5, contradicts 0, not covered 1.
- M1: APS -> cubic phase, low crystallinity, amorphous grain boundaries. **Supports** (n3 -> n4, n6; n21; n7).
- M2: low crystallinity -> larger cracks -> shorter life. **Supports** (n6 -> n9 with n8; n9 -> n12 -> n17).
- M3: micro-strain -> crack propagation -> shorter life. **Supports** (n11 -> n12 -> n17). a2 qualifies the proxy.
- M4: grain morphology -> crack mode; columnar grains resist. **Supports** (n13, n14, n23).
- M5: c-to-t transition -> spalling. **Supports** (n15 -> n17 with n16, k2). a1 qualifies the timing.
- M6: transition after 10 cycles -> lower micro-strain, slower spalling. **Not covered.** No graph claim makes this link. o7 reads micro-strain plateauing at ~1.4-1.5% rather than falling significantly. o6 agrees that the orientation change falls.
