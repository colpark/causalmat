# Judge review: Acta_Materialia/10.1016_j.actamat.2021.116731

**Verdict:** accept with fixes. This is a structure-only review. No figures or crops were opened, and panel citations and techniques were not ruled on.

After the fixes the graph has 56 nodes, 82 edges and 19 spine nodes. The spine is one connected, stage-ordered path: gap -> hypothesis -> NiTi base system + [001] vs [112] comparison axis -> solution treatment -> pillar machining -> compression. From the compression act it runs in two branches that reconverge:

- **[001] branch:** localized deformation band -> deformation-twinned austenite (29 deg rotation across the band) -> the competition MEC. In parallel the austenitic starting state and the load jointly cause the superelastic response.
- **[112] branch:** whole-pillar single-slip traces -> no superelasticity, ~12% permanent strain.

Both branches feed the common martensite structure (B19' + B2 -> (001)B19' compound twins in a herringbone), which identifies the herringbone MT; that, with the MT-stress ranking from the two curves and the MD map, gives the orientation-dependent competition MEC and the conclusion. Every spine STR/PRP/MEC claim now has OBS evidence or a KNW premise. The v04 decision rules hold: n13 is behavior_class (how it fails to recover) against n9/n18 value; n11 and n16 are both defect/extended but at different scales (austenite deformation twins vs (001)B19' compound twins); n17 is identification (a member picked from a known catalogue, conventional vs herringbone MT) while n12 and n19 are pathways. There are 4 audits (a1, a2, a3 and the contrasting readout o5), all fair: a1 and a2 are both discrepancies the panels carry and the text plays down, and a3 is the paper's own MD caveat.

## Changes
- Split n9 into n9 + n27 (see below), with n12 retargeted onto n27.
- Moved n12 off the spine and added n11 -> n19 `supports`.
- Source change on n22 (figure -> text). No read_from changes and no mode changes.
- Spine 20 -> 19 nodes; audits stay at 4; no merges.

## Splits and merges
- **n9 -> n9 + n27.** The old label stated the Fig. 2 claim ("near-complete strain recovery on unloading in every cycle") while its incoming MEC n12 and part of its evidence o5 carry the opposite Fig. 3a fact: ~7.3% residual strain, larger than the ~6.3% strain burst. Those cannot be one claim.
  - n9 keeps the superelasticity claim: a stress-induced transformation plateau from ~430 MPa and hysteresis loops that close on unloading. It stays on the spine.
  - New **n27** (PRP/value, mechanical, spine=false): after the large burst the [001] pillar keeps ~7.3% residual strain, more than the ~6.3% burst, so part of the stress-induced martensite does not revert.
  - New edges: n27 -> n9 `qualifies`; o5 -> n27 `evidences` (read_characteristic_point). o5 -> n9 is kept for the plateau.
  - n12 `explains` moved from n9 to n27. n12's label is about the residual strain exceeding the burst, which is exactly n27.
- **n12 off the spine.** Its only target is now the side claim n27, and it never reached the conclusion n20. To keep the [001] structural branch on the spine, **n11 -> n19 `supports`** was added: the observed austenite deformation twinning is the observation that the competition MEC cites as the near-maximal {112}<-1-11> Schmid factor at [001] (o19 already evidences n11), and before this review that observation never reached the competition claim.
- **Merges:** none. n9/n18, n10/n14, n11/n23/n24 and n15/n16 all state different claims; n17 (which MT mode operates) and n25 (the CRSS comparison that argues for it) are an identification and its DSC comparison, not duplicates.

## Source / read_from changes
- **n22: figure -> text.** F1b gives the four transformation temperatures, but the step from Af = 293 K to "austenitic and superelastic at ambient temperature" needs the test temperature, which no panel shows. `requires_unseen` now records that the tests run at ambient temperature (~293-300 K), as stated in the F1 linked text.
- **read_from: no changes.** Every annotation node restates strings listed for its panel (F1b DSC markers; F5b, F6b/d and F7a-f labels and Schmid-factor values); o1 restates the B2 / Ti4Ni2O legend and the hkl indices, which the packet lists for F1a as axis labels and tokens although the panel is flagged annotated:false, and the node already says so. The F4 nodes (o10, o11, o12) are tier C with no crops; their `annotation_match` already records that the packet lists no strings for that figure. o3, o5, o7, o21, o22 and a2 stay `axis` (values read off stress-strain axes or MPa colour bars, none of them written on the panel), and o4, o6, o8, o9, o13, o17 and a1 stay `pixels`. o17 is the only close call: it references the listed "(001)compound" label to locate the twin boundaries, but the ~5-8 nm it reports is measured against the scale bar, so `pixels` is right.
- n27 is the only new node; it carries source=figure with an empty `requires_unseen`, because both numbers (the ~5.7% -> ~12% burst and the ~7.3% reload arrow) sit on the F3a strain axis.

## Mode changes
None.
- **n9** is the only claim with two `causes` edges (n8 austenitic starting state, n7 compression). It is "joint" and that is kept: no caption shows a choice, and both are needed for the superelastic loops. The split did not change its causes.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 2, contradicts 1, not covered 0.
- **M1: micro-compression of [001] and [112] pillars -> herringbone microstructure of (001)B19' compound twins. Supports.** Nodes: n7 produces n10 and n14, both supporting n15 (B19' + B2), which supports n16 (herringbone (001)B19' compound twins), evidenced by o16, o17 and o18. The graph carries the caveat MatMech does not: n16 is source=text, because F6 shows the [112] pillar and the matching [001] microstructure is only in Fig. S2.
- **M2: herringbone microstructure -> superelastic recovery. Contradicts.** The graph puts the same herringbone structure in the pillar that has no superelasticity: n16 is evidenced from the deformed [112] pillar (o16, o17, F6a-b), and n13 says that pillar unloads linearly with ~12% permanent strain. In the graph what selects recovery is orientation, not the twin structure: n19 explains n9 and n13 from the same herringbone MT through the Schmid factors. There is a support path (n16 -> n17 -> n19 -> explains n9), but it runs through the identification of the transformation mode, not through any reversibility of the compound twins, and MatMech's premise that compound twins are energetically favourable for reversibility appears nowhere.
- **M3: micro-compression of [001] and [112] pillars -> superelastic recovery. Supports.** Nodes: n4 -> n6 -> n7, with n7 and n8 jointly causing n9, and n19 explaining it. MatMech's own reasoning ("the [001] orientation suppresses dislocation slip and favours reversible MT") is n19 verbatim: zero slip Schmid factor at [001] against 0.520 for the herringbone MT. The graph qualifies the recovery with n27 (~7.3% residual strain), which MatMech records only as "partial residual strain".
