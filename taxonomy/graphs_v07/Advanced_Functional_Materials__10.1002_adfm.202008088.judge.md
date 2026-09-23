# Judge review: Advanced_Functional_Materials/10.1002_adfm.202008088

**Verdict:** accept with fixes. This review checks structure only. No figure or crop was opened, and no panel citation or technique was ruled on (the blind second read checks those). Splits: 2 (n14, n18). Merges: 0. Source changes: 3 (n8, n12, n16). read_from changes: 0. Mode changes: 0. MatMech: 3 supports / 1 contradicts / 0 not covered.

The graph now has 42 nodes, 64 edges and 20 spine nodes. It passes the structural checks: v04 leaf types, rels and mm_ops throughout, an mm_op on every figure-OBS edge, `attrs.source` and `attrs.requires_unseen` on every node, `attrs.read_from` on every OBS node, `property_family` on every PRP node, `image_support` on every node with figs, a derives edge into the one derived OBS (o13), spine connectivity and spine support. Pre-judge copy: `.v07work/Advanced_Functional_Materials__10.1002_adfm.202008088.pre_judge.json`.

## 1. Spine order

The spine reads HYP -> DES -> PRC -> STR -> PRP -> PRF -> DSC with MEC bridging, in 20 connected nodes:

- gap n1 (reports disagree on the low-temperature transition) -> hypothesis n2 (domain size, through residual stress, governs it);
- three DES choices follow n2 and converge on one act: base system n3, PC/HOC/SC sweep n4 and the three growth routes n5, all realizing the crystallization n6;
- n6 produces the two structure claims that carry the argument: domain size over four decades n7 (F1a) and one and the same phase in all three states n8 (F1b,c);
- n7 causes the lattice claims n9 (state-dependent thermal expansion, F2a) and n10 (inhomogeneous residual strain, F2d with Williamson-Hall k1), which support the bridge n11 (the 2.0% volume change stores stress that grows with domain size and resists transformation);
- n11 explains the surface-triggered shrinking-core transition n12 (F4a,b) and the domain-size dependence n14; n12 causes the state-dependent PL n13 (F3a), which supports n14 (F5a,b);
- control branch: n6 feeds the grinding act n15 -> n16 (all three converge on one tetragonal band, no transition), which contrasts n13 and supports n14;
- second branch: n6 feeds the atmospheric ageing n17 -> n21 (aged surface dual, core single, F6) -> n18 (PDPL gauges SC crystallinity);
- n13, n14, n18, n11 and the comparison d1 support the conclusion n19.

n1 is the only spine node without an incoming spine edge and n19 the only one without an outgoing edge, as required. Two parallel branches (grinding control, ageing) hang off n6 and rejoin at n14 and n19.

**Evidence.** Every spine STR/PRP/PRF/MEC claim is backed: n7 by o1; n8 by o2; n9 by o4; n10 by o6 and k1; n11 by k2 with `basis: argued`; n12 by o5, o7, o8 and k6; n13 by o9 and k6; n14 by o5, o12, o13 and k6; n16 by o11 and k6; n21 by o14, o15. n18 is the one spine claim without direct evidence and now carries `basis: argued`, which is what the paper says ("these PDPL results *could* act as a gauge").

**v04 rules** hold. n12 stays STR/phase/fraction rather than microstructure/distribution: the reading is how much has transformed with a spatial gradient, not where a constituent lies (the r04 rule for the pair). n14 and n20 are PRP/value with `property_family: thermodynamic` (a property level against a design variable), not PRF: no threshold, spec or service condition is applied. n18 is PRF/service_capability because the method is claimed to work as a gauge. o13 is OBS/response/regime_map, which the r04 ruling #6 kept for exactly this reading (boundaries between states in a condition space), with `provenance: derived` and the required derives edge from o12. o6 stays OBS/response/trend: the width-vs-temperature direction is what n10 uses; the peak values sit in the label as levels of that trend.

**Audits:** 3 (a1, a2, a3), within budget and fair. a1 is text_silent: a blank band with no data from ~150 to ~165 K in the SC TDPL map, exactly where the abrupt SC transition is claimed, so it qualifies n12. a2 records the packet's own normalisation conflict, caption `sigma(700 K)` against linked text `sigma(100 K)` with data stopping near 270 K, which qualifies n10. a3 is text_silent and `image_support: contradicts`: the 300 and 400 um spectra are already single peaks, so dual emission ends between 200 and 300 um, against the linked text's "above 500 um"; it qualifies n14. n16 carries a `contrasts` edge but is a control result, not an audit.

## 2. Splits and merges

| node | into | why |
|---|---|---|
| n14 | n14, n20 | the label stated two claims across a semicolon: the monotone domain-size dependence (T_trans rises, window narrows) and the small-domain limiting case (smallest domains stay tetragonal at all temperatures). They rest on different readings - the F5b boundary against the two top spectra of F5a - and the limiting case is the piece that reconciles the nanocrystal literature. n20 is spine false, which keeps the spine at the 20-node ceiling; it is caused by n7, explained by n11, evidenced by o12 and o13, supported by the grinding result n16 and supports d1. Its label now says "in the mapped window", because F5b spans 80-190 K only; `image_support` is partial for the same reason. |
| n18 | n21, n18 | the label stated an observed state and the capability drawn from it ("... so PDPL gauges SC crystallinity"). n21 (PRP/value, optical, spine) keeps the aged-surface/core finding with the F6 evidence, caused by the ageing act n17; n18 keeps only the gauge claim, supported by n21, with `basis: argued`, `figs: []` and `attrs.fig_ref: F6`. |

**Not split.** n14's remainder keeps "transition temperature rises and the transition window narrows as domain size grows": these are two metrics of one transition behaviour against one design variable, read from the same F5b boundary and explained by the same MEC n11 (stress raises T_trans, and its release narrows the window). n12 keeps "starts at the domain surface and moves inward, finishing within <10 K": the temperature span is the scope of the one propagation claim, and it is the SC case of n14's window, not a second claim. n9 keeps the SC/PC/HOC contrast, which is one statement about how expansion depends on the crystalline state. o4 and o5 read different features of F2a (the trend of 2theta and the step plus coexistence band) and stay two OBS nodes.

**Merges: none.** The closest pair is n16 (ground powders converge on one tetragonal band) and the new n20 (crystallites below ~50 nm stay tetragonal). They are not duplicates: different material states (nanoparticles ground under N2 against gently crushed crystallites), different figures (F3b against F5a,b) and different roles (control branch against limiting case of the size series). The graph records the relation as `n16 supports n20`. The other look-alike pairs (o9/n13, o11/n16, o12/n14) are evidence and claim, not duplicates.

## 3. Source and read_from changes

| node | change | fact |
|---|---|---|
| n8 | source figure -> inferred | the node was the only one with `source: figure` and a non-empty `requires_unseen`, which is contradictory. The claim "all three states are the same MAPbI3 phase of the same composition" needs the compound name, which no panel shows, so it is inferred; requires_unseen now names only that, since "Theoretical" is a listed annotation of F1b and the green trace therefore is shown. |
| n12 | source figure -> inferred, requires_unseen filled | F4a and F4b carry no phase label (their annotations are the three laser lines and the three penetration depths), so "orthorhombic-to-tetragonal" needs the 750/780 nm assignment from the linked text, and "<10 K" is a text figure. Added `k6 premise_for n12`. |
| n16 | source figure -> inferred, requires_unseen filled | F3b is annotated "After grinding" with PC/HOC/SC and the axes only, so "tetragonal-like" needs the linked-text assignment. Added `k6 premise_for n16`. |

The two new nodes carry `source: figure` with empty requires_unseen: n20 reads the F5a top spectra and the field annotated "(Tetragonal phase)" in F5b, both on the panel; n21 reads the "1 day / 1 month / 3 month" maps and the "i Shell" / "ii Core" sub-panels of F6. n14 keeps `source: figure`: F5b annotates "(Orthorhombic phase)", "Dual emission", "(Tetragonal phase)" and "Domain size (um)", so the claim needs no off-panel fact.

**read_from: no changes.** Each OBS reading was checked against the annotation list of its panel in the packet. o8 (F4b) and o12 (F5a) are already `annotation` and their `annotation_match` strings are in the packet lists ('5=493.7nm', '0=60.6nm', '8=19.6nm'; '=50nm', 'D=10um', 'D=50um', 'D=300um', 'D>500um'). o13 (F5b) is `annotation` and restates the four regime labels verbatim. The `axis` readings stay: o1, o2, o4, o5, o6, o7, o9 and o11 name annotated condition labels (PC/HOC/SC, the laser lines, "After grinding") only to identify which trace is read, while the reading itself is a position or level off the 2theta, wavelength, temperature or FWHM axis. o14 and o15 stay `axis`: F6 is tier C with no panels offered, so the packet lists no annotation strings for it at all. a1 and a3 stay `pixels`: a missing data band and the shape of a spectrum are pixel judgements.

## 4. Mode changes

None. No claim in the graph has two or more incoming `causes` edges, before or after the splits: n9, n10, n13, n14, n16, n20 and n21 each have exactly one, and the multi-parent claims (n14 with n7 causes plus n8, n13, n16 supports and n11 explains; n19 with five supports) are joined by rels that mode does not apply to. No `attrs.mode` was added or removed.

## 5. MatMech tally (recorded after the graph was final; the graph was not edited)

supports 3, contradicts 1, not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | three growth routes -> PC, HOC and SC of different domain size | supports | n4, n5, n6, n7, o1 | n5 realizes n6, which produces n7; o1 reads the inset histograms of F1a. The record's per-route sizes (<200 nm, ~70 um, >1000 um) are text values: o1 and n7 record the histogram reading (~0.1 um, 10-100 um, 1e2-1e3 um) and keep the text numbers in `image_note`, with `image_support: partial`, because the SC bar sits short of 1000 um. |
| M2 | PC/HOC/SC of different domain size -> dual PL peaks in PC, single peak in SC | supports | n7, n10, n11, n12, n13, o9, k6, n15, n16, o11, n14, n20, o12 | the graph holds the whole path: n7 causes n10, n10 supports n11, n11 explains n12, n12 causes n13, evidenced by o9. The record's third line, that grinding releases the stress and aligns all samples on the tetragonal PL, is the control branch n15 -> n16 with o11, and its non-referenced premise (volume expansion generates residual stress) is k2 into n11. |
| M3 | photoluminescence behaviour -> phase-transition characteristics influencing optoelectronic device performance | **contradicts** | n12, n13, n18, n21, n9, n10, o4, o5 | the graph holds both endpoints but runs the causation the other way: n12 (the transition) causes n13 (the PL pattern), and nothing in the graph makes PL a cause of a phase-transition characteristic. The only sense in which PL comes first is diagnostic - n18, PDPL as a gauge of crystallinity - and that node is `basis: argued`, the paper's own "could act as a gauge". Two further mismatches, recorded but not ruled on: the record's evidence block cites Raman spectra from 80-300 cm-1, and the packet contains no Raman figure (F1, F2 are XRD, F3-F6 PL); and "optoelectronic device performance" has no node, because the paper builds no device. What the record's XRD half does state - SC sharp at ~150 K, PC broad - is in the graph as o4, o5 -> n9, n12, n14. |
| M4 | PC/HOC/SC of different domain size -> phase-transition behaviour and PL in optoelectronic applications | supports | n7, n11, n14, n20, n17, n21, n18, o12, o13, o14, o15 | n7 causes n14 and n20, bridged by n11, which is exactly the record's inductive line (residual stress proportional to domain size). The ageing study it cites is the second branch n17 -> n21 -> n18, with o14 (PDPL after 1 day, 1 month, 3 months) and o15 (split crystal, shell against core). Not in the graph: the record's "macroscopic cracks" in SC, which no packet figure or caption shows; the graph's nearest audit, a3, moves the dual-emission boundary down to 200-300 um and qualifies n14. |
