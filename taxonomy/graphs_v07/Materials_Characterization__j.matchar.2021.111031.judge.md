# Judge review: Materials_Characterization/j.matchar.2021.111031

**Verdict: accept with minor changes.** Structure only; no figure or crop opened, panel citations and techniques left to the blind second read.

## Spine and rules
- **Spine:** 14 connected nodes (was 13): need n1 -> hypothesis n2 -> BCN base n3 + exfoliation route n4 -> exfoliation n5 -> few-layer sheets n6 + pore perforation n18 -> SSA/mesopore volume n7; branch A bandgap n9 -> absorption n10; branch B charge separation n11; n7, n10, n11 jointly cause 3.3x H2 evolution n13, explained by MEC n12 (argued, KNW k8 premise) -> conclusion n14. Stage order holds; one main line with two parallel property branches.
- **Evidence:** every spine STR/PRP/PRF claim has an OBS evidences edge (n6 o1/o2; n18 o1; n7 o5/o6; n9 o11/o12/o10; n10 o10; n11 o12/o13; n13 o14). MEC n12 is basis=argued with premise k8.
- **v04:** all types, rels and mm_ops valid; every figure-bearing OBS edge carries an op.
- **Audits:** 1 (a1, XRD (002) not weakened, qualifies n6). Fair as a structural audit of the few-layer claim.

## Changes
- **n6 split:** "few-layer, pore-perforated 2D nanosheets" held two claims. n6 keeps the few-layer sheets; new **n18** (STR/microstructure/porosity, spine) holds the 30-50 nm pore perforation. n5 produces n18, n18 causes n7, o1 evidences n18. n18 notes that the BET insets (o6) peak at 11 nm, not 30-50 nm.
- **n10 split / merge into n9:** "absorbs more over 250-800 nm" stays in n10; "red-shifted absorption edge" is the same claim as the narrower gap and merges into **n9** (lower id kept). o10 now also evidences n9. The n9->n10 causes edge notes that the gap explains only the visible tail.
- **n17 split:** radical generation stays in n17; growth with illumination time becomes new **n19** (PRP/value, photochemical, side), evidenced by o15 and o16 (o16 partial: 5 and 10 min alike); n19 supports n17.
- **n11 relabelled** to one claim ("charges separate more efficiently"); the paper uses EIS as a second proxy for the same claim, so no split.
- **n16 relabelled:** "O attributed to adsorbed water" moved to attrs.note.

## Source / read_from changes
- n11: source inferred -> text (stated in linked text F5); requires_unseen now lists the k4/k5 premises and the linked-text sentence.
- n12: source stays inferred; requires_unseen filled (surface proton reduction, prior knowledge).
- read_from: no changes. Annotation readings (o5, o7, o8, o9, o11, o14, o15, o16) are already "annotation"; the others use legend strings only as identifiers.

## Mode changes
- n6->n7 and n18->n7: set **joint** (n7 gained a second cause from the split; no caption shows a choice).
- n7/n10/n11 -> n13 already joint; confirmed.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 1.
- **M1** exfoliation -> mesoporous few-layer sheets, higher SSA: supports (n5, n6, n18, n7).
- **M2** nanosheet structure -> narrower gap, lower transfer resistance: supports (n6 -> n9, n6 -> n11).
- **M3** mesoporous structure -> better light absorption, mass transport: not covered. The graph routes absorption through the bandgap (n9 -> n10), not pore light scattering, and has no mass-transport claim.
- **M4** narrower gap, lower resistance, better absorption -> 3.3x H2: supports (n10, n11, n12, n13).
- **M5** SSA, mesopores, thin sheets -> 3.3x H2: supports (n7, n12, n13).
