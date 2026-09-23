# Judge review: Advanced_Materials/10.1002_adma.202005449

**Verdict: accept with changes.**

This review checks structure only. No figures or crops were opened. Panel citations and techniques are left to the blind second read.

## Checklist
- **Spine:** 18 connected nodes, one root (n1), stage-ordered, two parallel branches out of the hypothesis n2:
  - MSC branch: n1 need -> n2 multitasking-ink hypothesis -> n3 aqueous Ti3C2Tx base -> n4 H/L concentration sweep -> n5 etch + delaminate -> n6 printable rheology (PRP) -> n7 down-select the H ink -> n8 screen printing -> n9 shear-alignment/recovery MEC -> n10 aligned lamellar film (STR) -> n11 areal capacitance vs printed layers (PRP) -> n12 10 000-cycle stability (PRF) -> n18 conclusion;
  - LIMB branch: n2 -> n13 hybrid LTO/LFP inks -> n14 stepwise printing -> n15 particles embedded in the MXene skeleton (STR/interface) -> n16 areal capacity (PRP) -> n17 self-powered integrated system (PRF) -> n18.
- **Evidence:** every spine STR/PRP/PRF/MEC claim is backed.
  - n6: o2, o3, o4, o5; c1 premise
  - n9: basis = argued, with o4 and c1 as premises
  - n10: o8, o9
  - n11: o10; k1 premise
  - n12: o13
  - n15: o18, o19
  - n16: o20
  - n17: o24, o25, o26
- **v04 rules:** pass.
  - The shape PRC (n5) -causes-> PRP (n6) -motivates-> DES/down_select (n7) -realizes-> PRC (n8) is the down_select rule ("down_select has an incoming motivates edge from a RESULT of this paper"; screen-then-choose papers put it on the spine). It is not the v04 tool/assembly exception, so n6 keeps attrs.object = "ink".
  - c2 stays PRP/descriptor: it explains n11 and is not itself the headline property. The new c8 is PRP/value, not PRF/qualification, because the benchmark it is weighed against (carbon-coated Al foil, 1.3 ohm) sits only in the SI text.
- **Audits:** 3, within the budget of 5 and all fair, since each changes the support of a spine claim: o23 (text_silent, the self-discharge curve starts at ~2.05 V, not the 2.3 V of the text), a1 (DSC/limitation, qualifies n17), o7 (the L-ink control, contrasts o6).
- **Modes:** n11 is the only claim with more than one incoming `causes` edge (n10, c2). Both already carry mode = "joint", and nothing in any caption presents the two as a choice, so "joint" is right. No changes.

## Splits and merges
- **n12 -> n12 + n19.** The node stated two different service claims. n12 (spine) keeps capacitance retention through 10 000 galvanostatic cycles, evidenced by o13. The new n19 (PRF/service_capability, side) holds the CV curves that are unchanged from flat to 180 deg bending; o14 was moved to it, n10 causes n19 and n19 supports n18. n19 is deliberately off the spine so the MSC branch keeps one PRF leaf and the graph keeps at most two parallel branches; it mirrors how the LIMB branch already carries its flexibility claim in the periphery.
- **c2 -> c2 + c8.** Two claims about two different objects. c2 keeps the electrode-film conductive network whose resistance falls with printed layers (o11), and stays a joint cause of n11. The new c8 (PRP/value, electrical) holds that printed MXene lines conduct well enough to be the metal-free collectors and interconnects; o12 (the 7.3 ohm printed line) moved to it, c2 supports c8 and c8 supports n18. This gives the "current collector, interconnect" half of hypothesis n2 a carrier, which the graph previously lacked.
- **c5 -> c5 + c7.** c5 keeps full capacity through 1000 bends; the new c7 holds ~80% retention after 1000 charge-discharge cycles. Both support n17.
- **o21 -> o21 + o27.** The OBS read two panels and stated two readings. o21 now cites only #F4j (bending) and the new o27 only #F4k (cycling, with the dips to ~65% near cycle 800 in image_note). The set of cited panels is unchanged.
- **o15 -> o15 + o28.** o15 keeps the F3e areal-capacitance bar ranking and evidences c6; the new o28 holds the F3g Ragone curve, evidences c6 and takes over the premise_for edge into c4. Both carry attrs.fig_ref because F3 is tier C with no panels offered.
- **Merges:** none. No two nodes state the same claim. The nearest pair, o13 (MSC retention) and o27 (LIMB retention), are different devices, and o23/a1 are an OBS and the limitation it reveals.

## Source / read_from changes
Seven source changes, all from "figure" to "text", each with the missing fact now listed in requires_unseen:
- **n6:** "the rheology screen printing needs" is a text criterion, and which trace is the dilute ink comes from the text concentrations, not from the in-image legend.
- **n9:** F2j draws unordered ink becoming an ordered deposit, but nothing on the panel says the shear is the printing shear through the mesh, or that the viscosity recovery is what holds the printed line.
- **n11:** the mapping of the plotted series 1L/5L/10L onto 1, 5 and 10 printed layers is caption-only, and it is the causal variable of the claim.
- **n12:** PRF/service_capability is defined by its use condition, and the 3 mA cm-2 cycling condition is caption-only. attrs.condition_from already recorded this while source stayed "figure".
- **c2:** the same printed-layer mapping, plus the ~500 S cm-1 conductivity, which is text-only.
- **c3:** F4c annotates "*MXene", "MXene-LTO" and "MXene-LFP", but "spinel", "olivine" and the expansion of LTO/LFP are not on the panel.
- **a1:** the limitation is a discrepancy against a number ("2.3 V") that exists only in the linked text, so requires_unseen could not be empty.

**read_from: no changes.** o17 is correctly "annotation" (annotation_match "*MXene", a string listed for #F4c). Every other OBS reads a trend, a value or pixels rather than restating an annotation; where the authors' in-image strings only name the series or the substrates (F2a, F2b, F2d/e/f, F4b, F4l), the staff recorded them in attrs.labels_from and kept read_from as "axis" or "pixels", which is the right reading of the rule. F3 and F5 are tier C, so no annotation strings are listed for their panels and none can be forced; o12 and o25 read values written inside those figures and stay "pixels"/"axis" for that reason, which is recorded here.

## Mode changes
None.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 1.
- **M1** (printing of the shear-thinning ink -> parallel-aligned lamellar architecture): **supports** (n6, n7, n8, n9, n10, o2, o4, o9). The graph states the pathway explicitly and adds the viscosity-recovery half that the MatMech cause leaves implicit.
- **M2** (aligned nanosheets with 1.2 nm interlayer spacing -> ~1.1 F cm-2 areal capacitance): **supports** (n10, c2, k1, n11, o10). The alignment half is a joint cause of n11 with the conductive network, with k1 as the in-plane ion-transfer premise. The 1.2 nm spacing is an SI result and survives in the graph only inside c1's requires_unseen, so that half of the cause is not carried as a cause of capacitance.
- **M3** (high capacitance and energy density -> 60 V from 100 series MX-MSCs): **not covered**. The tandem pack of F3k and the series/parallel uniformity results are outside the graph, so no node holds the effect. Neither supported nor contradicted.
- **M4** (printing of MXene-LTO/LFP battery inks -> ~154 uWh cm-2 in MX-LIMBs): **supports** (n13, n14, n15, n16, c4, o22, o28). The chain is present stage by stage. Note that c4 hangs off its OBS evidence rather than from an edge out of n16; this was left unedited because the graph was final before this file was read.
- **M5** (sensor sensitivity and fast response -> body-movement sensing at 35 ms): **supports** (n17, o26). o26 carries the sensitivity and the body-motion response together and n17 is the powered-sensing capability. The graph has no separate PRP node for sensor sensitivity, and the 35 ms figure sits only in o26's image_note.
