# Judge review: Acta_Materialia/10.1016_j.actamat.2021.116763

**Verdict:** accept with fixes. This is a structure-only review. No figures or crops were opened, and panel citations and techniques were not ruled on.

After the fixes the graph has 53 nodes, 77 edges and 17 spine nodes. The spine is one connected path in stage order: gap (n1) -> hypothesis (n2) -> base system, temperature/time sweep and the CALPHAD+DFT+microscopy method (n3, n4, n5) -> casting (n6) -> anneal (n7) -> structure. From there it runs in two branches that meet at the performance node:

- **Sigma branch:** n8 (two FCC phases up to 600 C) -> n12 (MEC: thermodynamic driving force plus sluggish diffusion) -> n9 (Cr-rich tetragonal sigma at 800 C) -> n16 (MEC: coarse sigma concentrates stress) -> n14 (drop to ~530/~305 MPa, ~15 %).
- **Nanoprecipitate branch:** n11 (finer precipitates at 600 C) -> n15 (MEC: obstacle density) -> n13 (peak strength at 600 C, elongation down to ~22 %).

Both reach n18 (usable window only up to 600 C) and then n19 (conclusion). The 1000 C states (n10, n21, n17, n20) stay off the spine and feed n18. Every spine STR/PRP/PRF/MEC claim now has OBS evidence or a KNW premise; n15 had neither before this review. The v04 decision rules hold: n11 is feature_size (how big) while s2 and n21 are distribution (where); s1 is chemistry/composition (what a phase is made of) while n8, n9, n10 and s4 are phase/identity, which here rests on SAED indexing and on ref [31], not on stoichiometry; n18 is service_capability, not qualification, because no external spec is applied. There are 4 audits (a1-a4) and all are fair: each one bounds a spine claim (the F1d mislabel, the magnification threshold behind "8 h", the unresolvable 4.5 -> 3.5 nm refinement, and the sub-kT DFT energy separations).

## Changes
- Split n10 into n10 + n21, and the evidence node o7 into o7 + o15 to match.
- Trimmed n9 and n19, each of which duplicated a claim already carried by another node (s2, n12).
- Added k6 (KNW/lookup) as premise_for n15.
- Rewrote the s1 label so that it states the claim rather than restating o10's printed table.
- No mode changes and no source changes.

## Splits and merges
- **n10 -> n10 + n21.** The label stated two claims: the sigma phase dissolves at 1000 C, and branched Cu segregation zones form. Only the second is what n17 (segregation softening) and n20 (near-elastic fracture at ~110 MPa) rest on.
  - n10 keeps the dissolution claim (STR/phase/identity, spine=false, image_support partial: absence read on a 40 um-bar panel).
  - New **n21** is the Cu segregation claim, typed STR/microstructure/distribution, whose definition names segregation explicitly. image_support partial, because "Cu" is the authors' in-image label and no map supports it.
  - Edges moved: n21 -> n17 supports and n21 -> n20 causes (both were from n10); added n7 -> n21 produces and o15 -> n21 evidences (assess_spatial_distribution). o7 -> n10 evidences stays.
- **o7 -> o7 + o15.** One OBS node held two readings of F1f from two different sources. o7 now reads only the absence of the bright chains (read_from pixels, compare_across_conditions into n10); new **o15** reads the in-image label (read_from annotation, annotation_match "Cu segregation zone").
- **Merged into existing nodes (label trims):**
  - **n9**: "in chains along the interdendritic boundaries" is s2's claim, and n9 -> s2 produces already carries it. n9 now states only the identity claim (Cr-rich sigma, tetragonal).
  - **n19**: its second conjunct ("the phase content ... is set jointly by thermodynamics and diffusion kinetics") restated n12. The conclusion keeps only "sigma formation is deleterious to the tensile properties"; n12 -> n19 supports is kept, so nothing is lost and the spine keeps a single terminus.
- **Not merged:** the readout/claim pairs (o8/s4, o9/s5, o10/s1, o13-o14/n13-n14, o11/s3) are OBS readings and the claims they evidence, not duplicates. s1's label was nevertheless rewritten to the per-phase composition claim, because it had repeated o10's table digit for digit.

## Source / read_from changes
None were needed beyond the o7 split.

- **read_from kept as pixels** on o2, o5, o6, o10, o11, a2 and a3. Rule applied: a panel-identity label (an element name, "600 C/2h", "Sigma phase") that only says which panel is being read does not turn a pixel reading into an annotation reading; the claim itself must restate the string. o6 reads map brightness, not the words "Cr" and "Cu"; o11 reads how much of the field the particles cover; a3 measures against the 50 nm bar. The F4 crop carries no OCR at all, which o10's image_note records.
- **read_from kept as annotation** on o1, o3, o4, o12, a1 and (new) o15; each carries annotation_match and each restates a string listed for its panel.
- **read_from kept as axis** on o8, o9, o13 and o14.
- **source**: every node that needs a fact no panel shows is already text (n1, n3, n5, n6, n8, n11, n12, n16, n17, s6, k1, k2, k3, k5) or inferred (n2, n15, n19, s7) or prior_knowledge (k4, and new k6), with the missing fact listed in requires_unseen. n11 is the important one: the ~4.5 -> ~3.5 nm sizes exist only in the F7/F8 linked text, so it is text with image_support not_shown, and a3 qualifies it. The figure-source nodes all have an empty requires_unseen.
- **Added k6** (KNW/lookup, prior_knowledge): finer, more closely spaced precipitates raise the obstacle density to dislocation glide. n15 is a spine MEC that had no OBS evidence and no KNW premise; the only other input to it was n11, which it explains.

## Mode changes
None.
- **n18** takes three causes (n13, n14, n20) and is already "joint" with a mode_basis. Kept: no caption shows a choice, and F7b plots all six conditions on one axis, so the window is set by the rise and both falls together.
- n13, n14 and n20 each have one causes edge and correctly carry no mode. n20's cause is now n21 instead of n10, and is still single.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 0.

- **M1: 800 C / 2 h -> Cr- and Co-rich tetragonal sigma. Supports.** Nodes n7 -> n9, evidenced by o3 (labelled bead-like chains), o4 (SAED indexed tetragonal) and o6 (Cr map), with n12 and s4 behind it. One qualification: the graph does not carry the "Co-rich" half. o6's image_note records that the Co, Mn and Ni maps show no visible enrichment at the particles, although the linked text gives sigma ~27 at.% Co.
- **M2: sigma formation -> lower yield strength, UTS and elongation. Supports.** n9 -> n14 causes, explained by n16 (coarse, inhomogeneously distributed sigma concentrates stress and nucleates cracks) with s2 and k4 as inputs; n19 is the same conclusion. The graph's F7 readings (~530 MPa UTS, ~305 MPa yield, ~15 %) agree with MatMech's 530 / 303 / 15.
- **M3: 600 C for >8 h -> delayed sigma formation, sluggish diffusion. Supports.** s3 (first detected at 8 h, area fraction growing to 12 h, from o11) supports n12, with s4 (CALPHAD: sigma stable below ~870 C) and k5 as the other inputs. The graph adds an audit MatMech does not have: a2 records that sigma is visible only in the two 10 um-bar panels, so "8 h" is a detection threshold at the magnification shown, not a measured incubation time.
