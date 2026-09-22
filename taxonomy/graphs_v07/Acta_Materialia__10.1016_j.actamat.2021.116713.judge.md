# Judge review: Acta_Materialia/10.1016_j.actamat.2021.116713

**Verdict:** accept with fixes. This is a structure-only review. No figures or crops were opened, and panel citations and techniques were not ruled on.

After the fixes the graph has 48 nodes, 58 edges and 18 spine nodes. The spine is one connected path: gap -> hypothesis -> diffusion-couple base system + statistical EBSD/STEM-EDX method -> 650 C anneals -> per-layer composition. From there it runs in two branches:
- **Layer growth:** parabolic diagnostic -> diffusion control (via k1) -> flux-balance MEC -> growth-rate ranking and Kirkendall-shift MEC -> thicker Ni3Al layer on the NiAl side. The two causes of the thicker layer are joint.
- **Nucleation:** OR fraction -> oriented-nucleation MEC. Separately, bimodal nucleation density -> switch at parent grain boundaries, and similar grain-size distributions.

Both branches end at n20. Every spine STR/PRP/MEC claim now has OBS evidence or a KNW premise; n17 lacked both before this review. The v04 decision rules hold: n8 diagnostic -> k1 lookup -> n10 identification; n6 composition carries phase_named_from=stoichiometry. There are 4 audits (o16, n24, a2, a3), and all are fair.

## Changes
- Split n7 into n7 + n26 (see below).
- Added **k6** KNW/model, "heterogeneous nucleation energetics", as premise_for n17. n17 is a spine MEC with basis=argued and had no OBS evidence or KNW premise. The energy argument is prior knowledge, so k6 has source prior_knowledge.
- read_from changes on o1, o2, o3 and o14. Source changes on n16, n21, n23, o10, o11, o12 and o17.
- No merges and no mode changes. The spine stays at 18 nodes, and the audit count stays at 4.

## Splits and merges
- **n7 -> n7 + n26.** The old label stated two claims: a thicker layer and larger grains.
  - n7 keeps the layer-thickness asymmetry (1.35 vs 0.5 um) and stays on the spine.
  - New n26 is the grain-size asymmetry (0.82 vs 0.48 um), as a side claim (spine=false).
  - New edges: n9->n26 and n12->n26 causes (joint), because the F2 text gives the same "in combination" attribution; o4->n26 evidences (measure_feature_metric).
  - n22 (immobile small-angle/twin boundaries slow grain growth) explained n7; it now explains n26, since it accounts only for grain size.
- **Merges:** none. The readout/claim pairs (o5/n8, o6/n9, o7/n14, o13/n16) are not duplicates.

## Source / read_from changes
- **read_from -> annotation.** Each of these OBS nodes restates strings listed for its panel:
  - o1: NiAl, (Ni), pure (Ni) as plateau identities;
  - o2: which side is NiAl or (Ni);
  - o3: STEM BF, and the region labelled pure (Ni);
  - o14: the high/low nucleation rate legend.

  Each node now also records `annotation_match`. o7, o8 and o9 were already annotation. o13 and o17 stay axis, and o4, o10, o11 and o12 stay pixels.
- **n16: figure -> text.** The 1.5 grains/um class boundary comes from the F5 text. The histogram shows only an empty gap.
- **n23: figure -> text.** The F4 panels carry no labels. That a grain boundary lies in NiAl (a) or in (Ni) (b), and that NiAl is on top, are caption and text facts.
- **n21: figure -> text.** "Grain growth little sensitive to interface crystallography" is the paper's inference. The two F5b histograms use different y-axes.
- **o10: figure -> text.** The colour key (red, green, blue layers) and "highlighted = OR grains" come from the caption.
- **o11, o12: figure -> text.** Which parent phase lies above or below, and which parent holds the grain boundary, come from the caption and text.
- **o17: text -> figure.** The label reads only the dashed line and the plateau. The Kirkendall meaning is now in image_note and is used by n12, which is already text.

## Mode changes
None.
- **n7** (causes from n9 and n12) is "joint", and that is kept. No caption shows a choice, and the F2 text says "in combination".
- **n26** is new, with the same two causes and mode "joint".

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 2, contradicts 2, not covered 0.
- **M1: 650 C annealing -> two Ni3Al layers with K-S (to NiAl) / near cube-on-cube (to (Ni)) ORs. Supports.** Nodes: n5 -> n6, n13, with n14 and n15.
- **M2: K-S ORs of grains grown into NiAl -> reduced boundary mobility, slower growth. Contradicts.** In the graph, the immobile small-angle and twin boundaries sit at the (Ni)/Ni3Al interface in the second, near-cube-on-cube layer (n15 -> n22 -> n26). The K-S layer on the NiAl side is the faster-growing, thicker and coarser one (n9, n7, n26).
- **M3: longer annealing -> OR fraction ~50% -> ~80%. Supports.** Nodes: n5 -> n13. The selective-growth mechanism MatMech adds is not in the graph.
- **M4: Al-enriched (Ni) grains -> diffusion-induced recrystallization and accelerated (Ni) grain growth. Contradicts.** The graph runs the opposite direction: DIR driven by grain-boundary diffusion produces the Al-enriched grains (k5 -> n19 explains n6). MatMech's size comparison (1.6 um vs "surrounding Ni grains ~0.48 um") mixes in the Ni3Al grain size; the text gives 50-500 um for the parent (Ni) grains.
