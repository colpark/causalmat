# Judge review: Bioactive_Materials/j.bioactmat.2020.01.001

**Verdict:** accept with fixes. This review covers structure only. No figures or crops were opened, and panel citations were not ruled on.

The graph now has 17 spine nodes, 54 nodes in total and 66 edges. The spine is one connected path:
- need -> hypothesis -> HA-on-Ti base + Si-for-P modification -> hydrothermal growth -> nanorod array (n7) and Si incorporation (n9).
- Topography branch: n7 + n9 jointly -> 1-d adhesion (n14), explained by MEC n19.
- Ion branch: n9 -> SiO4 on PO4 sites (n10) -> lattice distortion (n11) -> Ca + Si release (n12) -> MEC n18 -> fibrogenic genes (n16) -> collagen (n17).
- The two branches meet: n14 + n17 jointly -> in-vivo skin seal (n20) -> conclusion (n21).

Every spine STR/PRP/PRF/MEC node has OBS evidence or a KNW premise. n19 did not have one before this review; o17 was added to fix that. There are 3 audits (o12, o15, o22), all fair:
- o12: about 1/3 of the Si 2p area is a non-lattice silicate.
- o15: the (002) shift does not match the reported c value, and delta-a is at the error level.
- o22: the 3-d gene data do not follow the ranking the text states.

## Changes
- Split n7 and n9 (details below). The spine stays at 17 nodes.
- Added o17 -> n19 evidences (compare_across_conditions). n19 is a spine MEC that had neither OBS evidence nor a KNW premise. Protein adsorption on the nanorod surfaces is the first step of its pathway.
- Source fixes on o11, o18, o19, o20 and o23.
- No merges, no read_from changes, no mode changes.

## Splits and merges
- **n7 -> n7 + n23.** The old label stated two claims: the shape and the size of the rods.
  - n7 keeps "hexagonal nanorod arrays growing from Ti; Si does not change morphology", with o1 as evidence.
  - New n23 (STR/microstructure/feature_size, off-spine) is "~70 nm diameter, ~3 um long". o2 and o3 were moved to n23. New edge: n6 -> n23 produces.
- **n9 -> n9 + n22.** The old label stated two claims: Si incorporation (composition) and its top-to-bottom gradient (distribution). The build step had merged the gradient into n9.
  - n9 keeps "Si incorporated at ~3-5%, absent in HA", with o7-o10 as evidence.
  - New n22 (STR/microstructure/distribution, off-spine) is the gradient. New edges: o8 -> n22 evidences (register_colocated_views) and n6 -> n22 produces.
- Merges: none. o13/o15 and o21/o22 read the same panels but make different claims (a reading and its audit). n13 is a property and n19 a pathway.

## Source / read_from changes
- o11: text -> figure. The label states only the asymmetric envelope and the two fitted positions, and the panel shows both. The component assignment is carried by k1.
- o18, o19: figure -> text. The panel shows "Absorbance" at 450 nm. That the assay is CCK-8 is a caption fact.
- o20: figure -> text. The actin/nucleus stain identity, and which surface and day each image shows, come from the F7 caption. F7 has no annotation list.
- o23: figure -> text. The axis shows only "Absorbance540". That the stain is Sirius Red is a caption fact.
- read_from: no changes. Every annotation-derived OBS (o4, o7, o8, o9, o10, o14, o15, o25) is already "annotation". The F4b labels "101.8eV" and "103.1eV" are OCR tokens, not listed annotations, so "axis" stands for o11.

## Mode changes
None. There are two claims with two or more causes edges, and both stay joint:
- n14 (causes from n7, n9): joint.
- n20 (causes from n14, n17): joint.
No caption presents either pair as alternatives.

## MatMech tally (recorded after the graph was final; graph not edited)
Tally: supports 3, contradicts 1, not covered 0.
- M1 (alkali-heat + hydrothermal treatment with Si -> Si-HA nanorods with lattice distortion): **supports**. Nodes n6, n7, n23, n9, n10, n11. The alkali-heat pretreatment is not in the packet or the graph.
- M2 (Si substitution / lattice distortion -> more Ca and Si release; topography preserved): **supports**. Nodes n11 -> n12 with the k3 premise, and n7. o15 qualifies the lattice evidence. Wettability is not covered.
- M3a (ions + topography -> fibrogenic genes, collagen, reduced down-growth / biosealing): **supports**. Nodes n12, n18, n16, n17, n7, n14, n19, n20.
- M3b (ions + topography -> the highest fibroblast proliferation on Si-HA): **contradicts**. Nodes n15 and o19. In the graph, Si-HA proliferation only recovers to the Ti level (7 d: Ti ~2.51, Si-HA ~2.48), and HA is lowest.
