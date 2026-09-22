# Judge review: Materials_Characterization/j.matchar.2020.110138

**Verdict:** accept with changes (structure only; figures, panel citations and techniques not ruled on).

## Spine
17 spine nodes form one connected, stage-ordered path from n1 to n17: HYP n1/n2 -> DES n3/n4 -> PRC n5 -> STR n6, n9, n7, n11, n12, n13 (MEC n10, n8 bridging) -> PRP n14 -> MEC n15 -> PRF n16 -> DSC n17. Every spine STR/PRP/PRF/MEC claim has OBS evidence or a KNW premise (n8 k3, n15 k2). There are 5 audits (a1, a2, a3, L1, L2), and each one changes the support of a spine claim.

## Changes
- Removed **n9 -> n7 causes**. PAG morphology does not cause the martensite-only state, which n8 already explains. Added **n9 -> n17 supports** so the PAG result reaches the conclusion that names it.
- Removed **n13 -> n14 causes**. It ran against the paper's direction: residual stress distorts the lattice (F10 linked text). The IQ-vs-RS comparison already lives in n13 -> n16 and n14 -> n16.
- Added **n8 -> n12 explains** and **n8 -> n13 explains**. A uniform martensite-only state (n7) cannot by itself explain zone gradients. The paper ties the strain variation to zone-dependent cooling and dislocation density [11].
- o3 label: "Reconstructed grains:" became "Grain maps:". Reconstruction is a caption fact that the panel does not show.

## Splits and merges
None. Each label states one claim, and no two labels duplicate each other.

## Source / read_from changes
- source: **o5** figure -> text. The F2 panels carry no zone labels, so assigning BZ(C)/DZ(C)/DZ(I) and reading the map as PQ laths needs the caption. Both facts are now listed in requires_unseen.
- read_from: none. o1 and a3 are already "annotation". The remaining pixel and axis readings do not restate listed annotation strings.

## Mode changes
None. n14 is the only claim with two or more causes edges (n11, n12, after n13 -> n14 was removed). It stays "joint" because no caption shows a choice between them.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
**Supports 3 · contradicts 0 · not covered 0**

| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | laser cladding -> PAG morphology, martensite substructure, zone size/aspect variation | supports | n5, n10, n9, n8, n7, n11, n18 |
| M2 | PAG/substructure/size -> GOS, IQ | supports | n7, n8, n12, n13, k2, k4. The graph routes this through the martensitic transformation and cooling. PAG shape and size are not linked to GOS/IQ |
| M3 | GOS, IQ -> IQ inversely tracks RS, usable for RS mapping | supports | n12-n16. Qualified by a2 (inverse to signed RS in BZ/HAZ but to \|RS\| in DZ, so MatMech's "high IQ = compressive DZ" pairing does not hold), a3 (IQ comparable only within a scan) and a1 (GOS and IQ disagree in HAZ) |
