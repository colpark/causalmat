# Judge review: Journal_of_Materials_Science_&_Technology/j.jmst.2021.11.026

**Verdict: accept with minor changes.** Structure only; no figure or crop opened, panel citations and techniques left to the blind second read.

## Spine and rules
- **Spine:** 19 connected nodes. need n1 -> hypothesis n2 -> two branches: DFT (method n3 -> imposed registries n4 -> EB ranking n5, explained by charge-redistribution MEC n6) and experiment (modification n7 + loading sweep n8 -> hydrothermal growth n9 -> coating n10; n9 -> hierarchical shape n11 + MoS2 identity n12; n10 -> agglomeration n13 -> barrier n14 and wear rate n15). The branches meet at the sliding MEC n16 (from n5, n11, n12). The agglomeration MEC n17 explains n14 and n15; n14 -> 9-d service n18 -> conclusion n19. Stage order holds.
- **Evidence:** n5 (o1-o3; k1, k2), n6 (o4), n11 (o6, o7), n12 (o8), n14 (o11, o12; k3, k6), n15 (o15, o16), n16 (k5), n17 (o11, k6; added), n18 (o13, o14; k3). n4 is basis=imposed (in-silico construction). **n13 (agglomeration at 0.5 wt%) is basis=argued with no OBS or KNW in the packet**. It stays visible as an unsupported link, with a judge_note.
- **v04:** all types, rels and mm_ops valid; every figure-bearing OBS edge carries an op.
- **Audits:** 2 (o1: strong OH binding qualifies the sliding MEC n16; o10: Ti3C2Tx (002) absent, qualifies n11). Both fair.

## Changes
- **n23 split:** EP adhesive/fatigue wear stays in n23 (F11a). New **n26** (PRP/behavior_class, side) holds the plastic fish-scale wear of the 0.1 and 0.3 coatings without furrows (F11b,c). o17 evidences n26, and n26 supports n25 (replaces n23 -> n25). n26 contrasts n23.
- **k3 split:** k3 keeps "larger arc/|Z|/Rc = better resistance". New **k6** holds "second time constant = electrolyte at the substrate"; it is premise_for n14 and n17.
- **o11 evidences n17** (added): the day-1 second time constant of EP and -0.5 is the packet's only evidence of a less compact coating.
- **n12 -> n16 supports** (added): n12 was a spine dead end; mechanism (b) needs MoS2 layers.
- **n12 relabelled** "Crystalline MoS2 forms in the composite": "hexagonal" appears on neither the figure nor the text.
- n19 kept as one summary node (DSC/conclusion joins both branches by definition). No duplicates found; no merges.

## Source / read_from changes
- o4 figure -> text: which F3 slice is OH/O/F comes from the caption (F3 is tier C, no annotation list).
- o5 figure -> text, n20 figure -> text: F4 curve-to-system mapping comes from the caption.
- read_from: no changes. o5, o8, o9 are already "annotation". The other OBS use legend strings only as identifiers.

## Mode changes
- None. After the edits no claim has two or more incoming causes edges.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 1, not covered 1.
- **M1** hydrothermal growth -> hierarchical 2D, MoS2 anchored: supports (n9, n11, o6, o7; o10 qualifies).
- **M2** vdW interface, config VI -> EB < -1 eV, charge redistribution: supports (n4, n5, n6, o1, k1). MatMech's -1.2 eV is not on F2a (-1.09 to -1.13).
- **M3a** hierarchical structure -> barrier (tortuous path): not covered. The graph has no structure -> barrier link.
- **M3b** hierarchical structure -> self-lubrication: supports (n11, n12, n16, n25, n15, n26).
- **M4** structure at 0.1 wt% -> best corrosion and wear protection: supports (n11, n16, n15, n14, n18, n19). The graph ties agglomeration to 0.5 wt% only, not to 0.3.
- **M5** strong interfacial binding -> low wear (less delamination): contradicts. The graph, like the paper, credits WEAK interlayer interaction for sliding (n16), and o1 qualifies it. The EB is in-silico, not a product of the hydrothermal step.
