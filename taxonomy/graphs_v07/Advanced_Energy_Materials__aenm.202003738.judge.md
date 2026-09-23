# Judge review: Advanced_Energy_Materials/aenm.202003738

**Verdict: accept with minor changes.**

This review checks structure only. No figures or crops were opened. Panel citations, techniques and `image_support` are left to the blind second read.

## Checklist

- **Spine:** 19 connected nodes in stage order, one path from the first HYP to the conclusion:

  need for 4.5 V NCM523||graphite cells that the SOTA EC-based electrolyte cannot meet (n1) -> hypothesis that eliminating EC removes the failure (n2) -> comparison axis EC:EMC 3:7 vs EMC (n3) -> formulate the two electrolytes (n4) -> galvanostatic 2.8-4.5 V cycling (n5) -> surface-layer LixPOyFz (n12) and TM on the anode (n8) -> TM scavenging by LixPOyFz (n13) -> positive-crosstalk pathway (n14) -> colocalized TM and dendrite spots only in the EC-based cell (n7) -> dendrite penetration with micro short-circuits (n10) and capacity decay (n11), bridged by the negative-crosstalk pathway (n9) -> rollover collapse at cycle ~45 against stable ~160 mAh/g (n6) -> LiDFP addition (n15, n16) -> rollover suppressed in the EC-based electrolyte only (n17) -> LixPOyFz identified as the operative agent (n18) -> conclusion (n19).

  Two parallel branches: the surface-chemistry branch (n12 -> n13 -> n14) and the deposit/dendrite branch (n8 -> n7 -> n10, n11), which meet at n14 -> n8 and again at the conclusion. The Al2O3-coating arc (n24, n25, n23) and the physicochemical control arc (n20, n21, n22) stay off the spine.
- **Evidence:** every spine STR/PRP/PRF/MEC claim has OBS evidence, a KNW premise, or `attrs.basis` != evidenced:
  - n6: o5 | n7: o7, o8, o9 | n8: o9, o12 | n9: basis argued, premise k1 | n10: o10, o11, premise k3
  - n11: o10 | n12: o13 | n13: o15 | n14: basis argued, premise k4, supported by n26 and n28 | n17: o16, o17 | n18: o16
- **v04 rules:** pass.
  - n5 stays PRC/stimulus: the cycling produces argued states (n7, n8, n12), which is the r04 rule for stimulus against a PRF `attrs.condition`.
  - n8 and n12 are STR/chemistry/composition, not STR/phase/fraction: element content and an amorphous species, per the r04 composition-vs-fraction rule. n26 is STR/chemistry/bonding, a binding-energy difference within the same species, against n12's amount.
  - n7 is STR/microstructure/distribution (where the constituent lies) against n8's amount, the r04 distribution rule applied to deposits.
  - n18 is MEC/identification by decoupling experiment (r04 ruling 26) against n14's built pathway; n15 is DES/modification (added to a named base), not DES/down_select.
- **Audits:** 3 (a1, a2, a3), all `text_silent`, all fair and each bounding a spine claim: a1 bounds n7 (at the 100 um field the SEM resolves no dendrite morphology, so the dendrite identity rests on the F map and ref. 20), a2 bounds n6 (partial recovery after cycle 85 and about +/-40 mAh/g cell-to-cell spread), a3 bounds n12 (total degraded LiPF6 is nearly unchanged; only the high-F part grows). n21, n22 and n23 carry `contrasts`/`rules_out` edges but are claim nodes, not audit readouts.

## Splits and merges

- **n12 -> n12 + n28.** The label stated two compositional claims read from the same stacked-bar panel.
  - n12 (spine) keeps the LixPOyFz content: ~8-10 at% high-F LixPOyFz on both electrodes of the EC-free cells. o13 evidences it and a3 still qualifies it.
  - The new n28 (STR/chemistry/composition, side) holds the carbonate content: ~4.5 against ~11 at% on the anode. n5 produces n28, o13 evidences it, and n28 supports n14, since less solvent decomposition is the other half of the "without EC, LiPF6 is preferentially reduced" pathway that k4 premises.
- **n11 label trimmed, not split.** "Dendritic Li consumes active Li" restates the n9 pathway and the n7 -> n11 `causes` edge, so splitting it out would have created a duplicate that the merge half of the same rule would then remove. n11 now states one claim, the decay to ~130 mAh/g by cycle 100, and `attrs.note` records where the other half lives.
- **Considered and not split.** n5 names one cycling act applied to two cell builds; the build is carried by the DES nodes n24 and n25 that point into it, per the v04 rule that a distinction is an attribute unless it changes the next inference. n6, n7 and n17 each state one comparative claim across the study's comparison axis n3, which is one claim. n9 and n14 are pathways, which MEC/pathway is defined to state as a chain. o13 and o15 are single readings of single panels (one stacked-bar composition; one photograph carrying printed ppm values), and OBS nodes split by panel kind, not by how many claims are drawn from them.
- **Merges:** none. n8 (how much TM), n7 (where the TM and the dendrites lie) and o9/o12 (the readouts) are distinct; n9 is the paper's pathway where k1 is the cited precedent used as a premise; n14 is a pathway where n18 is an identification by decoupling; n19 is the conclusion where n27 is design guidance; n6 is the uncoated cell where n23 is the Al2O3-coated one.

## Other structural changes

- **Edge added, n5 produces n8.** The TM deposit on the anode had no processing origin and hung only off the MEC n14 that explains it, which left that arc with STR upstream of PRC.
- **Edge added, n6 supports n19.** The headline performance claim is the subject of the conclusion but was a directed dead end; the spine now reaches n19 through the performance node as well as through n14, n18 and n9.

## Source / read_from changes

- n8: source figure -> text. The claim needs the specimen identity (graphite-based anode, 100 cycles), which neither F4 nor F6 carries. The electrolyte assignment is annotated on F6a/F6b and is therefore not listed.
- n13: source figure -> text. F8c prints +PO3F2- and the ppm values, but that PO3F2- stands for the LixPOyFz species, and that the vials hold EC-based electrolyte with added Co2+ and Ni2+, are caption facts.
- n21: source figure -> text. Reading the ~5.5 V plateau as the electrolyte decomposition limit, and the working electrode as an LNMO composite, are caption facts; the former `attrs.note` is now the second `requires_unseen` entry.
- o2: source figure -> text, for the same two caption facts. The coincidence of the two traces, which is what the node reads, is on the panel.
- n18: source inferred -> text. The identification of LixPOyFz as the key difference and TM scavenger is stated in the F8/F9 linked text, so it is not the annotator's inference.
- **read_from: no changes.** o11 and o15 already restate strings listed for their panels ("Voltagenoise"; the Co2+/Ni2+ ppm pairs) and carry `annotation_match`. o12 stays `pixels`: the element labels are annotated but the reading is peak strength on panels with no counts axis. o13 and o14 stay `axis`: they quantify against the at.% and binding-energy axes rather than restate the stack and species labels. o7, o8, o9 and a1 are spatial readings, hence `pixels`.

## Mode changes

None. n6 is the only claim with two or more incoming `causes` edges (n10 and n11). "joint" is correct and keeps its `mode_basis`: F5a shows both effects inside the same rollover window and no caption offers them as a choice. The two edges added in this review are `produces` and `supports`, so no new multi-cause claim appears.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)

**Supports 2, contradicts 0, not covered 0.**

- **M1** (EC-free electrolyte, 1.0 M LiPF6 in EMC, no additives -> reduced TM deposits and suppressed Li dendrites on graphite, altered SEI with more LixPOyFz): **supports** (n3, n4, n5, n12, n28, n8, n7, n13, n14, k4; o7, o8, o9, o12, o13, o14, o15). The graph carries both halves of the effect, the SEI/CEI change on n12 with the carbonate half now on n28, and the reduced TM with the absent dendrite spots on n8 and n7, and it routes the pair through the scavenging property n13 and the positive-crosstalk pathway n14 instead of asserting it directly. Two record sub-claims sit elsewhere: "TM deposits are nucleation sites for Li dendrites" is the precedent k1, used for n9 rather than for M1, and the chelation step is inside n14's label. Audit a3 bounds the XPS half, since the total degraded LiPF6 on the anode is nearly unchanged and only its high-F part grows; audit a1 bounds the dendrite half.
- **M2** (reduced TM deposits and dendrites with the LixPOyFz-rich SEI -> rollover-free 4.5 V performance with suppressed fade): **supports** (n7, n8, n12, n9, n10, n11, n6, n15, n16, n17, n18, n19, k3; o5, o10, o11, o16, o17). The graph states the pair in its failure direction, which is how the paper argues it: the colocalized spots n7 cause dendrite penetration n10 and active-Li loss n11, which jointly cause the rollover n6, with the negative-crosstalk pathway n9 explaining it; the EC-free cell is the other level of the same comparison axis n3. The record's confirmation step, LiDFP added to the EC-based electrolyte, is the n15 -> n16 -> n17 -> n18 arc, and its voltage-noise lookup is k3 with o11. Audit a2 qualifies the rollover description. Two record details are not carried: the cells behind F4, F5 and F8 are Al2O3-NCM523||graphite rather than the NCM523||graphite named in the M2 params, a distinction the graph keeps on n24 and n25, and the 1C rate is a caption fact recorded in n5's `requires_unseen`.
