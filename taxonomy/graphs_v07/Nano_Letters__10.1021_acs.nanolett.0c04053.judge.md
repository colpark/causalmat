# Judge review: Nano_Letters/10.1021_acs.nanolett.0c04053

**Verdict:** accept with fixes. Structure-only review: no figure or crop was opened, and panel citations and techniques were not ruled on (the blind second read covers those). The graph now has 44 nodes, 58 edges and 19 spine nodes.

## Spine

One connected, stage-ordered path:

- **Need and hypotheses.** n1 (need) motivates n2 (fast mixing -> smaller, narrower crystals) and n22 (one-pass co-injection -> more payload), and also n5 (add an aptamer).
- **Payload branch.** n2 -> n3 (microfluidic route) / n4 (route x cargo comparison axis) -> n6, n7 (PRC) -> n9 (STR, crystal refinement) and, through the mixing mechanism n11 and the occlusion mechanism n13, into n12 (PRP, encapsulation efficiency).
- **Targeting branch.** n5 -> n8 (PRC/deposition; n7 feeds_into n8) -> n14 (STR, aptamer layer), bridged by n16 (electrostatic adsorption), then to the two in-vivo results n17 (lymph node) and n18 (tumour), bridged by n19 (ligand-receptor recognition).
- n12, n17, n18 support n21 (conclusion); n10 and n20 support it from the periphery.

Every spine STR/PRP/PRF/MEC claim has evidence or a premise: n9 (o1, o2, o3), n12 (o5), n14 (o9), n17 (o10, o11), n18 (o12, o13); the four MEC nodes are basis=argued with KNW premises k1, k4, k2+o8, k3. 19 spine nodes is inside 10-20, and 3 audits (a1, a2, a3) is inside the budget of 5; each one bounds a spine claim it is attached to, so they are fair.

Two points I accepted rather than rewrote. (1) The targeting branch goes STR (n14) -> PRF (n17, n18) with no PRP in between; the MEC bridge n19 is exactly what the stage order allows, and the paper's only relevant PRP (n15, zeta potential) is a confirmation of the coating, not a driver of targeting, so it correctly stays off the spine. (2) Three spine edges converge on n21. Read as the paper reads it, that is two branches - payload and targeting - with the targeting branch forking at the end into the same capability tested in two animal models. No v04 type, rel, mm_op or modality violations remain; the graph validates clean against v04.

## Changes

- Split n2 (below).
- source figure -> text on n6 and n18 (below).
- o12 label cut back to one claim; the liver/kidney clause moved to attrs.image_note, where a3 already carries it quantitatively from the F6f bars.
- o13: added attrs.aspect = ranking. It is a trend read over two categorical groups, which is the v04 rule; o5, o11 and a3 already carried the attribute.
- Added n7 produces n10 and n8 produces n10. n10 states what cargo loading and aptamer coating do to the habit and the particle size, but had no incoming causal edge at all - only OBS evidence - so the claim floated free of the acts it is about.

## Splits and merges

- **n2 -> n2 + n22.** The old label stated two predictions ("smaller, narrower ZIF-8 **and** load more biomolecule"), and the two run through different nodes to different claims.
  - n2 keeps the refinement prediction and its 46%-faster-mixing premise; it motivates n3 and n4.
  - n22 is the payload prediction, source=text with the F4 linked-text sentence listed; it motivates n4. n1 motivates both.
- **Merges: none.** No two labels state the same claim. The close pairs are a readout and its claim (o5/n12, o2/n9, o8/n15, o6+o7/n10), which v04 keeps apart; o13 and a3 read the same panel but state different things (the starred aptamer-vs-neat tumour pair, and the tumour's rank against liver and kidney).

## Source / read_from changes

- **n6: figure -> text.** F3a shows both synthesis routes, but no panel carries a temperature; "at room temperature" comes from the F4 linked text. requires_unseen also lists the 35 uL/min flow rate.
- **n18: figure -> text.** F6e and F6f do show the aptamer-vs-neat tumour comparison, but no panel names the tumour type or the injection route; "prostate" and "after tail-vein injection" are linked-text facts. n17 was left at figure on purpose: its two routes are annotated on F6a and F6b ("Subcutaneousinjection", "Footpadinjection") and the node names are annotated on F6b and F6c.
- **read_from: no changes.** Every OBS node is already right against the packet's panel section. o14 is the only node that restates listed annotation strings (the F7b "Reference" row and the biomarker table) and it is already "annotation" with annotation_match. The axis nodes (o1, o2, o5, o8, o11, o13, a2, a3) read values off labelled axes and use annotations only to name the groups, which is not a restatement; the pixel nodes (o3, o6, o7, o9, o10, o12, o15, a1) read image content, with o9's dependence on the printed C/Zn/N/P channel labels already recorded in its image_note.

## Mode changes

- **None.** n12 is the only claim with two or more incoming causes edges (n9, n7). Both carry mode=joint with a mode_basis, and that is correct: no caption or panel presents crystal refinement and one-pass co-injection as a choice between two explanations - F3B/C and F4A/B/F-H are shown as acting together - so "alternative" is not available.
- After the fix n10 also has two incoming edges, but they are produces, not causes, so no mode applies.

## MatMech tally (recorded after the graph was final; graph not edited)

**Supports 5, contradicts 0, not covered 1.**

- **M1** double-spiral micromixing -> smaller, narrower, cubic crystals. **Supports** (n3, n6 -> n11 -> n9; o1, o2, o3, k1). The size and width half is the graph's own spine. The "cubic morphology" descriptor is not: o3 and n10 read a rounded polyhedral (rhombic-dodecahedral) habit, and o3's image_note records that the caption's "cubic" is not what the 1 um fields show.
- **M2** one-step encapsulation of BSA/siRNA/DOX -> morphology kept, hydrodynamic size larger. **Supports** (n7 -> n10; o6, o7). The invariance half is n10, now produced by n7 and n8. The hydrodynamic-size increase (528, 766, 722 nm) is in Figure S7, which the packet does not carry; and again the graph records the habit as rounded polyhedral, not cubic.
- **M3** cubic ZIF-8 with encapsulated biomolecules -> high encapsulation efficiency. **Supports** (n9 and n7 -> n12, explained by n13; o5, k4). The graph attributes the gain to crystal refinement and one-pass co-injection. The sodalite topology and 3.4 A aperture of the MatMech reasoning are not nodes: XRD and BET are in the Supporting Information.
- **M4** positive zeta potential of BSA@ZIF-8 -> electrostatic aptamer functionalisation. **Supports** (n8 -> n16 -> n14; o8, n15, k2, o9). o8 carries both the +25 mV start and the sign reversal; a1 flags that the TEM insets resolve no shell, so the layer claim rests on the P map and the zeta sign.
- **M5** pH-responsive ZIF-8 degradation -> controlled acidic release. **Not covered.** No node. The packet has no release curve and no acid-exposure panel: the F3 linked text points its "Figure 5A-D" acid-breakdown sentence at a Supporting figure, while packet F7 (paper Figure 5) is the biocompatibility figure.
- **M6** two-stage chip integrating synthesis and functionalisation -> better lymph-node and tumour targeting. **Supports** (n5, n8 -> n14 -> n17, n18, explained by n19; o10-o13, k3). Both result branches are on the spine, with a2 recording that one of the four node/route pairs carries no significance star and a3 that the tumour signal stays far below liver and kidney.
