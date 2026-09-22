# Judge review: Acta_Materialia/10.1016_j.actamat.2021.116710

**Verdict:** accept with fixes. This is a structure-only review: no figure or crop was opened, and panel citations were not ruled on. The graph has 16 spine nodes, 42 nodes and 59 edges. The spine is one connected path: gap -> hypothesis -> NN-BNT base + x sweep -> sintering. From there it splits into two branches:
- **NN-rich branch:** Pbma -> P+R -> Pnma phases (n6) -> reversible switching in polarization (n10) -> full P-E/S-E reversibility for AFE_O R (n11, explained by n12) -> ~0.44% strain at x=0.16 (n19) -> actuator candidate (n15).
- **BNT-rich branch:** PE/relaxor-AFE/R3c phases (n7) -> APNR domains (n8) -> random-field MEC (n17) -> near-linear response (n13).

Both branches end in the conclusion (n16). Every spine STR/PRP/MEC node has OBS evidence. n10 and n12 also have KNW premises. n15 (argued) now has premise k7. The only audit is a1 (x=0.18 barely switches within 30 kV/mm, so reversibility is shown only at x=0.16), and it is fair. n23 is a side comparison that qualifies n15. All types, rels and ops are v04-valid.

## Changes
- **n12 label trimmed.** The clause "Pnma returns to itself" restated n11. n12 now states only the Pbma -> metastable poled AFE mechanism. Its edges are unchanged.
- **n13 retyped** from PRP/value to PRP/behavior_class. "Near-linear response, no AFE-FE switching" is a categorical loop-shape class, the counterpart of n10 and n11.
- **k7 added** (KNW/lookup, prior_knowledge): a fully recoverable large strain is what actuators require. k7 is premise_for n15, which before had neither OBS evidence nor a KNW premise.

## Splits and merges
None. n10 and n11 state different reversibility claims (polarization only from x>=0.1; polarization and strain from x>=0.16). n9 and o5, and n19 and o17, are each a readout paired with its claim.

## Source / read_from changes
- n9: figure -> text. o5: figure -> text. In both, identifying the permittivity step as T_P-R comes from the F4 linked text.
- n10: figure -> inferred. The AFE-FE reading of a double loop needs the lookup k5.
- n11: figure -> inferred. "AFE_O R compositions" is a text phase assignment, and the reversibility reading needs k5.
- n13: figure -> inferred. The PE and relaxor-AFE classes of x=0.2-0.8 come from text.
- o12: figure -> text. The mode labels nu3-nu6 and the fitting come from the linked text and caption. F6b has no mode labels.
- read_from: no changes. No OBS label restates a listed annotation string: F6a/F6b labels and F9b '@10 Hz' are not used. The F8 x= labels only identify the curves. o4 and o21 are annotation, read from in-image strings of unlisted panels, which is acceptable.

## Mode changes
None. No claim has two or more incoming causes edges.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 1, contradicts 1, not covered 1.
- **M1** (solid-state sintering -> dense microstructure, composition-dependent grain size): **not covered**. n5 has no grain-size node, because F2 was left off as a sub-result.
- **M2** (Pbma/Pnma phases -> T_P-R permittivity peak ~365 C): **supports** (n9, o5, k1, n18).
- **M3** (relaxor AFE P4bm -> low-hysteresis high strain, 0.38% at x=0.9): **contradicts**.
  - In the graph, P4bm compositions (x~0.5-0.78) respond near-linearly with S-E <=0.075% (n13, o19).
  - x=0.9 is R3c at the ergodic/nonergodic boundary (n7), not P4bm.
