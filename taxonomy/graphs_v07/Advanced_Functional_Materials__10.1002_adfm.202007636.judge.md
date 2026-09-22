# Judge review: Advanced_Functional_Materials/10.1002_adfm.202007636

**Verdict:** accept with fixes. This was a structure-only review: no figures or crops were opened, and panel citations were not ruled on. The graph has 17 spine nodes, 47 nodes and 59 edges in total. The spine is one connected path:
- need -> hypothesis -> MXene base + MF POM modification -> in-situ growth;
- from growth, two branches:
  - dispersion + particle size (joint) -> pseudocapacitive dominance -> rate capability and high-loading capability;
  - bonded interface -> cycling stability;
- a MEC links both branches;
- both feed the down-select as the LIC/SIC anode -> LIC and SIC Ragone FOMs -> conclusion.

Every spine STR/PRP/PRF/MEC node has OBS evidence, and n8 and n10 also have KNW premises. The v04 decision rules hold. There are 2 audits, o3a (F1d plates of 50-200 nm vs 10-20 nm in the text) and o15 (~37% vs the 51% rate retention stated in the text). Both are fair.

## Changes
- **Split n4 -> n4 + n4b.**
  - n4 keeps the choice of MF POM as the constituent.
  - New n4b (DES/down_select, side, source text) is the equal-mass POM:MXene ratio chosen after the ratio comparison (Fig S6d/S10d). New edge: n4b -> n5 realizes.
- **Split n12 -> n12 + n12b.**
  - n12 keeps the 1000-cycle retention at 1-4 A/g for Li and Na. Its source changed from text to figure, with o13 and o23 as evidence.
  - New n12b (PRP/value, side, source text) is "far more stable than bare MF POMs" (Fig S6). New edge: n12 -> n12b supports. The n12c contrasts edge moved from n12 to n12b.
- **n7 relabelled** to the size claim only. The comparison with micrometre prisms is already carried by n7c -> n7 contrasts.
- **Removed o3b -> n7 evidences.** An EDS uniformity map read with assess_spatial_distribution cannot evidence a size claim. Added o7t (feature_metric, text_only, source text) as n7's evidence. o3a still qualifies n7.
- **Added n11 -> n18 supports.** The spine rate-capability node was a dead end.
- Merges: none. n12c and n1 play different roles (a control value and a need). OBS/claim pairs are a readout and its claim, not duplicates.

## Source / read_from changes
- n14, n16, n17: inferred -> figure. The numbers are read from F3h/F5h and the F4f/F6f Ragone plots.
- n12: text -> figure, after the split.
- n4 and n7: requires_unseen trimmed to match their new labels.
- o3b: annotation -> pixels. The listed strings (Ti/Fe/Mo) only name the channels, and the uniformity is read from pixels.
- o6: annotation -> pixels. The listed strings are legend labels, and the reflections are read from the traces.
- o16 and o20 correctly keep annotation, because they restate the listed b-value strings.
- o17 and o21 read percentages that are printed in the bars but are not in the listed annotations. Their axis setting is left as it is.

## Mode changes
- None. n10 is the only node with two or more causes edges (n6, n7). Its mode is "joint", which is correct: no caption shows a choice between the two causes.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 0.
- M1: in-situ growth -> sandwich structure with dense, uniform dispersion. **Supports** (n5 -> n6; o1, o3b, o6).
- M2: sandwich structure -> pseudocapacitive contribution and fast diffusion. **Supports** (n6 + n7 -> n10; n13 explains). GITT diffusion is not a node.
- M3: pseudocapacitance -> rate capability, stability and high loading. **Supports** (n10 -> n11, n14). The graph attributes stability to the bonded interface (n8 -> n12), and o15 qualifies the 51% retention figure.
