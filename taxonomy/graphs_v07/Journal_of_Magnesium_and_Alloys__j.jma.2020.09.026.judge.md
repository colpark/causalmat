# Judge review: Journal_of_Magnesium_and_Alloys/j.jma.2020.09.026

**Verdict: accept with minor changes.** Structure only. No figure or crop opened; panel citations and techniques left to the blind second read.

## Spine and rules
- **Spine:** 16 connected nodes, unchanged: need n1 -> hypothesis n2 -> AZ31 base n3 + Ti-6Al-4V n4 + 0-21 vol.% sweep n5 -> FSP n6 -> distribution n8, void-free interface n9, FSP grain refinement n10 (DRX, n11) -> joint strengthening MEC n13 -> strength rise n14 -> elongation fall n15 (deformable-particle MEC n16) -> comparison with AZ31B/SiC n20 -> conclusion n21. No PRF, because the paper reports tensile properties only. n20 on the spine is fair: the ductility comparison is the headline.
- **Evidence:** n8 has o6/o7/o8; n9 has o10/o11; n10 has o13; n11 has o14 + k6; n13 has k2/k3; n14 has o16; n15 has o17; n16 has k4; n20 has o18 + k5.
- **Branches:** n8, n9 and n10 all feed n13. This is one joint fan-in into a single mechanism (F10 linked text), not three independent branches, so it passes.
- **v04:** all types, rels and mm_ops are valid, and every edge from a figure-bearing OBS node has an op.
- **Audits:** 5 (o5, o12, o19, o21, d2). All are fair, and each bears on a spine claim or on its premise n7.

## Changes
- **n9 split.** "Continuous, void-free and free of reaction products" was two claims. n9 keeps the continuous, void-free interface (o10, o11; o12 qualifies). The new **n22** (STR/interface, side) holds "no reaction products such as Al3Ti". n6 produces n22, o9 (line scan) and o10 evidence it, and n7 now supports n22 instead of n9.
- **n10 split.** n10 keeps the FSP refinement 66.7 -> 9.1 um, and d2 still qualifies it. The new **n24** (feature_size, side) holds the further refinement 9.1 -> 4.5 um with content. o13 evidences n24 (read_trend), n8 causes n24, and n24 causes n13.
- **n11 split.** n11 keeps DRX. The new **n23** (MEC/pathway, side, basis argued) holds particle pinning and nucleation, and it explains n24.
- **Relabels:**
  - n12: "near particles" dropped, because it is not in o15 or the text.
  - o19: now one reading. The relative loss moved to image_note, which avoids adding a sixth audit.
  - o13: now the annotated values only.
  - o7: now five fields, not six.
- **Kept as one claim:**
  - n13: the paper says the four mechanisms act jointly and cannot be separated.
  - n14: UTS and YS are two measures of one strength claim.
- **Merges:** none.

## Source / read_from changes
- o1, o5, o12: figure -> text. The powder identity of F1a/F1c comes from the caption.
- o8: figure -> text. The F5b element (Ti) comes from the caption only.
- New n22, n23, n24: source text, with requires_unseen filled.
- requires_unseen added on n21 ([]), d2 (the 0 vol.% sample is base metal) and k7 (reference 2theta positions).
- read_from: no changes. o3 reads annotation and matches the F2 strings. o13 stays annotation, although the packet lists F7 as annotated:false. The other nodes use legend strings only as identifiers.

## Mode changes
- n24 -> n13 set to **joint** (new cause). n8/n9/n10/n12 -> n13 are confirmed joint: the linked text says the factors act collectively, and no caption shows a choice. No other claim has two or more causes edges.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 2, contradicts 0, not covered 1.
- **M1** FSP with 0-21 vol.% -> homogeneous distribution, DRX refinement, pinning, dislocations, intermetallic-free interface: **supports** (n6 -> n8, n9, n22, n10/n11, n24/n23, n12; n7).
- **M2** microstructure -> UTS 226 -> 322 MPa, YS 98 -> 205 MPa, elongation 14.5 -> 9.3%: **supports** (n8, n9, n10, n24, n12 -> n13 -> n14 -> n15; n16).
- **M3** microstructure -> retained ductility vs ceramic MMCs, ductile fracture: **not covered**. The graph routes the ductility advantage through particle deformability (n4, k4 -> n16 -> n15 -> n20) and has no edge from the microstructure to n15, n19 or n20. o19 also qualifies the comparison.
