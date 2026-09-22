# Judge review: Advanced_Energy_Materials/aenm.202103301

**Verdict: accept with minor changes.**

This review checks structure only. No figures or crops were opened. Panel citations and techniques are left to the blind second read.

## Checklist
- **Spine:** 18 connected nodes. need (n1) -> hypothesis (n2) -> WO2 base (n3) + M sweep (n4) -> computed W-M bond weakening (n5) -> dG_H* volcano (n6) -> down-select Ni (n7) -> hydrothermal NWs (n8) -> reductive anneal (n9) -> single-phase Ni-WO2 (n10) -> oxidised W (n13) -> longer, charge-depleted W-W/Ni bond (n14) -> d-d decoupling MEC (n15) and reaction-path MEC (n20) -> best M-WO2 activity (n16) -> eta10 benchmark (n17) and 100 h stability (n18) -> conclusion (n19). The computation-first loop (DES -> STR -> PRP -> down_select -> PRC) is what the down_select rule allows.
- **Evidence:** n5 (o1, o2, o3, k1); n6 (o4, k2; a1 qualifies); n10 (o5, o8; n21 supports); n13 (o10, k3); n14 (o13, o15, o16); n15 (o19; a2 qualifies); n20 (o25, o26); n16 (o18); n17 (o24); n18 (o22, o27).
- **v04 rules:** pass after one retype. n6 PRP/value -> PRP/descriptor: dG_H* is computed, is not the measured headline property, and explains the activity. n17 stays PRF/qualification, because eta10 at 10 mA/cm2 is the benchmark condition named in the definition.
- **Audits:** 2, both fair. a1: the volcano's right leg is a single broken W-Cu configuration (qualifies n6). a2 (text_silent): Co and Cu have the same dG_H* but are ~80 mV apart (qualifies n15).

## Splits and merges
- **n10 -> n10 + n21.** n10 keeps single-phase monoclinic WO2 (o5, o8). The new n21 (STR/microstructure/distribution, side) holds the uniform Ni distribution (o9, F2e). n9 produces n21, and n21 supports n10.
- **n9 -> n9 + n22.** n9 keeps the reductive anneal act. The new n22 (PRP/value, catalytic, side, source text, fig_ref Figure S19) holds the 600 C anneal optimum. n9 causes n22.
- **o22 -> o22 + o27.** o22 keeps the 100 h chronopotentiometry. The new o27 (OBS/signal/reference_match) holds the inset where the 2000th LSV overlaps the initial one. o27 evidences n18.
- **Merges:** none.

## Source / read_from changes
- n4: figure -> text. That M replaces one W site is stated only in the linked text.
- n10: figure -> text. That card 32-1393 is monoclinic comes from the linked text.
- n19: inferred -> text. The conclusion is stated in linked text F4.
- n16: "1 M KOH" appears only in the caption, so it moved from the label to attrs.condition.
- o5: read_from pixels -> annotation. The node restates 'WO2-PDF#32-1393'.
- Kept: o1, o9, o10 and o15 stay pixels, because their annotations only identify the traces or channels.

## Mode changes
None. No claim has two or more causes edges.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 1.
- **M1** (hydrothermal + 600 C Ar/H2 anneal -> monoclinic Ni-doped porous NWs with a longer W-W/Ni bond): supports (n8, n9, n10, n21, n11, n14).
- **M2** (Ni substitution, longer bond, lower W 5d occupancy -> dG_H* -0.44 eV and a lower Tafel slope): supports (n5, n6, n13, n14, n15). The Tafel slope appears only in the image_note of n16.
- **M3** (longer bond and charge redistribution -> lower work function, Rct 379 -> 51 ohm): not covered. There is no work-function node, and Rct appears only in the image_note of n16.
- **M4** (optimised dG_H*, Tafel slope and Rct -> eta10 41 mV and 100 h stability): supports (n15, n16, n17, n18).
