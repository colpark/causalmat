# Judge review: Advanced_Functional_Materials/10.1002_adfm.202008078

**Verdict:** accept with fixes. This review checks structure only. No figures or crops were opened, and no panel citation or technique was ruled on (the blind second read checks those). Splits: 3 (n16, n18, o18). Merges: 0. Source changes: 2 (o12, s3). read_from changes: 0. Mode changes: 0. MatMech: 2 supports / 1 contradicts / 0 not covered.

The graph now has 49 nodes, 66 edges and 20 spine nodes. It passes the structural checks: v04 leaf types, rels and mm_ops throughout, an mm_op on every figure-OBS edge, attrs.source and attrs.requires_unseen on every node, attrs.read_from on every OBS node, spine connectivity and spine support. Pre-judge copy: `.v07work/Advanced_Functional_Materials__10.1002_adfm.202008078.pre_judge.json`.

## 1. Spine order

The spine reads HYP -> DES -> PRC -> STR -> PRP -> PRF -> DSC with MEC bridging, in 20 connected nodes:

- need n1 -> hypothesis n2 -> three DES choices: MFN base n3, hypoxia-responsive BCP graft n4, hollow-vesicle architecture n5;
- the three converge on the acts: n6 (thiol-ene grafting) -> n7 (solvent-exchange co-assembly) -> n8 (hollow monolayer vesicle);
- n7 feeds the hypoxia exposure n9, which produces n10 (the vesicular architecture is lost), bridged by the MEC n11 (nitroreductase turns the PNIHM block hydrophilic) and supported by n8;
- n10 opens the paper's two parallel branches: Dox release n12 -> hypoxia-selective cytotoxicity n14, and catalase activity n13 -> in vivo hypoxia relief n15;
- the branches meet as joint causes of n16 (tumour volume) -> n20 (survival); n17 (relieved hypoxia plus immunogenic cell death raises CTL infiltration) bridges to n18 (relapse prevented) and to the side node n21 (lung metastasis);
- n16, n20, n18 and n15 support the conclusion n19.

**Fix.** n3 had no outgoing spine edge: the base-system choice hung off n2 as a third branch that never rejoined the path, while n4 and n5 converged at n7. Added `n3 -realizes-> n6`: the grafting act is performed on the OA-capped MFNs, so it carries out the base-system choice as well as n4. The spine is now one connected, stage-ordered path with two parallel branches and no control branch.

**Evidence.** Every spine STR/PRP/PRF/MEC claim is backed: n8 by o1, o2; n10 by o4, o5; n11 by k1 with `basis: argued`; n12 by o6; n13 by o7, o8, k2; n14 by o9; n15 by o10, o11, o12; n16 by o14; n20 by o15; n17 by o16, o17, k3; n18 by o17, o18.

**v04 rules** hold. n8 and n10 stay STR/microstructure/shape (geometry of a built unit, and its loss). n12/n13/n14 are PRP/value with kinetic, catalytic and biological property families: each is a measured level or rate against a design variable, not suitability at a use condition. n15, n16, n20, n18 and n21 are PRF/service_capability (in vivo, under the stated use condition). s3 is MEC/pathway with `mechanism_class: pharmacokinetic`, which is the r04 ruling #17. o12 stays OBS/morphology/feature_metric on an xy_curve panel: an area fraction of imaged features on a derives edge from o11, a pattern used 18 times elsewhere in v07.

**Audits:** 4 (o8, a1, a2, a3), within budget and fair. o8 is text_silent: the hypoxia-gating of intracellular H2O2 consumption is never stated in the packet text. a1 shows the abdomen outshining the circled tumour, which qualifies the biodistribution node s3. a2 shows sO2 falling back to 8.8% at 48 h against the text's "increased levels even at 48 h", which qualifies n15. a3 shows the residual H2O2 climbing over the repeat cycles, which qualifies n13.

## 2. Splits and merges

| node | into | why |
|---|---|---|
| n16 | n16, n20 | the label stated two endpoints: tumour volume near 250 mm3 at day 20 (F4B,C) and every mouse alive past day 30 (F4D). They are causally sequential, so they are now two nodes joined by `causes`; o14 evidences n16, o15 evidences n20. n20 is spine. |
| n18 | n18, n21 | the label stated two different animal models: the rechallenged tumour after resection (F5B) and lung metastasis in the separate i.v. 4T1 model (F5G,H). n18 keeps relapse prevention on the spine; n21 is the metastasis claim, spine false, explained by n17 and supporting n19, which keeps the spine at the 20-node ceiling. |
| o18 | o18, o19 | the OBS node read two panels from those two experiments in one label. o18 now reads the secondary-tumour volume, o19 the lung-nodule counts with the F5G photograph note. The staff build file had merged F5B and F5H on purpose; the merge does not survive the one-claim rule because the panels report different models. |

**Label trims (no new node):** a3 keeps the residual-H2O2 rise only. Its second half, "the traces are straight lines with no data markers", is a rendering reading that was already recorded verbatim in `attrs.image_note`, so the audit count stays at 4.

**Not split.** n15 combines a 2.7 -> 17.5% sO2 rise with a 7% HIF-1a-positive area. These are two metrics of one state (tumour oxygenation) in one cohort, not two claims, and the graph keeps them on one node with three evidence edges. Same for o1 (three instruments on one morphology claim), o16 and o17.

**Merges:** none. No two nodes state the same claim; the OBS/claim pairs that read alike (o6/n12, o7/n13, o14/n16) are evidence and claim.

## 3. Source and read_from changes

| node | change | fact |
|---|---|---|
| o12 | source text -> figure | the claim is the three bar values (84, 76, 7%), read against the F3g axis, with the quantity written on the panel. The ImageJ / >10 micrographs line is provenance, not a fact the claim needs; requires_unseen is now empty and the fact moved to image_note. |
| s3 | source figure -> text | no panel shows that the fluorescent agent is IR780-labelled Dox-MVs, and no upstream node declares it. requires_unseen now lists the F3 caption fact. |

`attrs.requires_unseen` was added to the five nodes that lacked the key (n11, n17, n19, k1, k2), all of them source `inferred` or `prior_knowledge`; each now names the fact no panel shows. The new nodes n20, n21 and o19 carry `source: figure` with empty requires_unseen: survival curves, nodule counts and secondary tumour volumes are all read from the F4/F5 axes.

**read_from: no changes.** Two readings were checked against the packet's annotation lists and kept as they stand. o2 (F1f) is `pixels`: 'Fe' and 'Mn' are listed annotations, but they only name the channels, and the observation itself is the spatial coincidence of the two maps, which is a pixel judgement - the node's image_note already says so. o12 (F3g) is `axis`: 'Hypoxia', 'positive' and 'area' are annotations that name the ordinate, but the three values are read against the axis. o8 (F2a) and o5 (F2c) are `pixels` for the same reason: 'Normoxia'/'Hypoxia' are condition labels, not the reading.

## 4. Mode changes

None. n16 is the only claim with two or more `causes` edges (n14 and n15). Both are already `mode: joint` with a mode_basis, and that is right: the F4 linked text argues that Dox-GVs (release without catalysis) and Dox-MVs alone each fall short, so the two causes act together. No caption offers a choice between them. After the splits, n20, n18 and n21 each have at most one incoming `causes` edge.

## 5. MatMech tally (recorded after the graph was final; the graph was not edited)

supports 2, contradicts 1, not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | solvent-exchange self-assembly of BCP-tethered MFNs -> monolayer of densely packed MFNs in the membrane | supports | n5, n7, n8, o1, o2, s1, o3, s2 | n7 produces n8, evidenced by o1 (TEM/SEM/HAADF) and o2 (Fe/Mn maps). The graft-density size control of the MatMech experiment is carried by s1 and o3, with the 121 nm down-select s2. |
| M2 | monolayer of densely packed MFNs in the membrane -> catalytic activity for H2O2 decomposition | **contradicts** | n8, n10, n13, o7, o8, k2, a3 | the graph holds both endpoints and a path between them (n8 supports n10, n10 causes n13), but the sign is reversed: the intact densely packed monolayer is the inactive state. o7 reads 92% residual H2O2 and about 2 ppm O2 for intact MVs against 28% and 54 ppm for dissociated MVs, and n13 is labelled "only dissociated MVs consume H2O2 and evolve O2". Activity follows the loss of the cause state, not the cause state. The MatMech record's own deductive line names dissociation; its cause/effect pair does not. a3 further qualifies n13: residual H2O2 climbs 28 -> 38 -> 40 uM over the repeat cycles. |
| M3 | solvent-exchange self-assembly -> enhanced tumour inhibition and long-term immunological memory | supports | n7, n8, n10, n12, n13, n14, n15, n16, n20, n17, n18, n21, n19, o14-o19 | the whole spine tail carries this pair: n7 -> n8 -> n10 -> {n12, n13} -> {n14, n15} -> n16 (joint) -> n20, with n17 bridging to n18 and n21. Ten-group ranking (o14), survival (o15), CD8+/Treg and cytokines (o16), memory T cells (o17), rechallenge (o18) and lung nodules (o19) are all present. Not in the graph: the Dox-GVs inert control as its own node (it sits in o16's image_note), the T2-weighted MR panel F3c, and the H&E/TUNEL panels. |
