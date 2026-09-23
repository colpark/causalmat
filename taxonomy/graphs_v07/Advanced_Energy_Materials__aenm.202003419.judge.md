# Judge review: Advanced_Energy_Materials/aenm.202003419

**Verdict:** accept with fixes. This is a structure-only review. No figures or crops were opened, and panel citations and techniques were not ruled on (the F2d citation drop on o7 was left as the staff recorded it).

**Final graph:** 20 spine nodes, 54 nodes and 64 edges, v04-valid.

**Spine.** Two cycles, as the paper argues: a preliminary study on the plain carbon host, then the doped-host study.

- gap (n1) -> C HS model host (n2) -> carbonisation (n3) -> Zn plating (n4) -> deposition-sequence MEC (n5, F1d) -> initial sites govern deposition (n20) -> hypothesis (n7);
- n4 also produces the three coexisting Zn forms (n6), which n5 explains;
- n7 -> DFT screen (n8, DES/method, headline) -> exothermic Zn binding on N-doped graphene (n9) -> down_select CnC HS with the C HS control (n10) -> polydopamine-derived N shell (n11a) -> N in the shell (n11) -> Zn-N bonds at pyridinic N (n12) -> pyridinic N identified as the active site (n13) -> spacious-vs-dense nucleation MEC (n15) -> planar vs dendritic deposit (n14) -> lower overpotential (n16) -> cycling capability (n17) -> conclusion (n19).

n12 reaches n14 by two routes (directly by `causes`, and through n13 -> n15 which `explains` n14): one branch pair, within budget. Every spine STR/PRP/PRF/MEC claim has OBS evidence or a KNW premise (n20 rests on k3; n15 on F3f/F3g with k3). The v04 decision rules hold: composition vs distribution for n11/s3, shape for n14, identification vs pathway for n13/n15, value for n9 and n16, service_capability for n17 and n18.

**Audits:** 3 (a1, a2, a3), all fair. Each one bounds a spine claim it is attached to: the single-atom features at the noise level (n6), the ~1200 cm-1 Raman feature inside the noise band (n12), and the unequal-length CE records (n17).

## Changes

1. **n5 split** (below).
2. **n11 split** (below).
3. **o4 split** (below).
4. **n18 moved off the spine.** The Zn-MnO2 full cell and the phone photograph are an applied demonstration, not a step the conclusion needs; n17 is the performance claim the paper itself calls "confirmatory evidence of the positive impact of optimized nucleation". Added n17 -> n19 `supports`; n17 -> n18 and n18 -> n19 kept, so nothing was lost. This also kept the spine at 20 after the n5 split added a node.
5. **Six source changes** (below).
6. **No merges.** The OBS/claim pairs (o1/s1, o8/s2, o14/n14, o17-o18/n16, o15-o16-o19/n17) are a readout and its claim, not duplicates, and n5 (the generic deposition sequence on C HS) and n15 (with vs without zincophilic sites) are two different pathways.

## Splits and merges

Rule applied: split when the clauses are separate propositions that take different evidence and license different next steps, or that need different node fields. A comparative claim stated against its own control (n14, n15) is one claim, and so is one property claim supported by two quantities (n16, n17).

- **n5 -> n5 + n20.** The label joined the three-stage sequence (single atom -> cluster -> network, F1d) with the separate claim that the distribution of initial sites induces later deposition and sets performance. n5 keeps the sequence, the F1d citation, o2 as evidence and the `explains` edge into n6. New spine node **n20** (MEC/pathway, argued) carries the second claim; k3 (`premise_for`) and the `supports` edge into the hypothesis n7 moved to it, and n5 -> n20 `supports` was added. This is the paper's own "therefore".
- **n11 -> n11 + s3.** The label joined a composition claim (N in the CnC HS shell, absent in C HS; F2g spectra, o10) with a spatial-distribution claim (evenness; F2f map, o9) - different STR types and different evidence. New off-spine node **s3** (STR/microstructure/distribution) takes o9, and s3 -> n15 `supports`, which is the paper's step "because of a wide distribution of zincophilic sites, the distribution of Zn nuclei is spacious".
- **o4 -> o4 + o22.** The label joined a pixel reading (localised charge hotspot at the nitrogen) with a restatement of the panel's annotated Bader charges, which forced one read_from value to be wrong. o4 keeps the hotspot (pixels); new **o22** (OBS/response/characteristic_value, F2a) carries the annotated values and evidences sN with `read_characteristic_point`.
- **Merges:** none.

## Source / read_from changes

Rule applied: a claim whose sample, species or test condition is given only by a caption or the linked text is "text", with that fact listed; a claim stays "figure" when the panel or its own annotations carry the identity and only the reading is at stake.

- **o2, o3, a1 -> text.** F1b/F1c show bright features and one annotation (`Zn=0.25nm`); that the sample is zinc-loaded carbon and that the three enlargements are single atoms, clusters and the porous network is the caption's colour key.
- **s1 -> text.** F1a is marked only with the Zn and Ti card numbers; that the foil is the plated carbon host comes from the linked text.
- **s2 -> text.** F2e shows hollow spheres with a 200 nm bar; "carbon" is the caption.
- **n17 -> text.** The panels give efficiency vs cycle number and voltage vs time; the areal capacity, the current density and the symmetric-cell configuration are caption facts, and n17 carries them in attrs.condition.
- **read_from:** the o4/o22 split only. Every other OBS node is right: o1, o3, o16, o18 and o22 restate strings written on the panel ("annotation"); o5, o7, o10-o13, o15, o17, o19, o20 and a2 read plotted data and use the on-panel `CnCHS`/`CHS`/site labels only to name the series ("axis"); o2, o6, o8, o9, o14, o21 and a1 are pixel judgements.

## Mode changes

None. n17 is the only claim with two or more incoming `causes` edges (n14 and n16). Both already carry `"mode": "joint"`, which is right: no caption or figure weighs the deposit morphology against the overpotential, and the linked text credits them together. No other multi-cause claim exists; n6 and n12 each have one `causes` edge plus `produces`/`explains`.

## MatMech tally (recorded after the graph was final; graph not edited)

Supports 5, contradicts 0, not covered 0.

- **M1 Processing -> Structure.** **Supports** (n3, n11a -> n11 -> n12 -> n13). The mesoporous zinc network in the record's effect is read in the graph on the undoped C HS host (n5, n6, F1), so it is not an effect of the doping step.
- **M2 Structure -> Property.** **Supports** (n12 -> n13 -> n15 -> n14 -> n16, with n9 for the bond strength). Coulombic efficiency sits in the graph as performance (n17, from o15), not as a property node.
- **M3 Structure -> Property.** **Supports** (n14 -> n16 `causes`, explained by n15, evidenced by o17 and o18). The record's "39 mV vs 43 mV at 0.5 mA cm-2" misstates the condition: 39/43 mV are the F4d initial-discharge values; the 0.5 mA cm-2 pair in the linked text is 20 vs 27 mV.
- **M4 Property -> Performance.** **Supports** (n16 -> n17 `causes`, joint with n14; n17 -> n18). Dendrite suppression is placed upstream in the graph, as the deposit morphology n14 explained by n15, not as an effect of the properties.
- **M5 Processing -> Performance.** **Supports** as the full chain n11a -> n11 -> n12 -> n13 -> n15/n14 -> n16 -> n17 -> n18; the graph has no direct processing -> performance edge.
