# Judge review: Advanced_Energy_Materials/aenm.202102982

**Verdict: accept with minor changes.**

This review checks structure only. No figures or crops were opened. Panel citations and techniques are left to the blind second read.

## Checklist
- **Spine:** 13 connected nodes in stage order: need -> dual-function hypothesis -> NH4OAc modification -> single-ion electrolyte set -> plating/stripping. The path then splits into two branches:
  - NH4+ shield MEC (n6) -> dendrite-free deposit STR (n7);
  - OAc- interfacial buffer MEC (n8) -> no ZHSH STR (n10).

  Both branches are joint causes of high CE (PRP n12), which leads to the 3500 h symmetric cell (n13) and the 83.7% full cell (n14), then to the conclusion (n16).
- **Evidence:** every spine STR/PRP/PRF/MEC claim has OBS or KNW support:
  - n6: o1, o2, k2
  - n7: o13, o14
  - n8: o8, k1
  - n10: o11, with o12 qualifying it
  - n12: o15
  - n13: o16
  - n14: o18
- **v04 rules:** pass.
  - n3 stays DES/modification. The introduction frames NH4OAc as an a priori choice, although the F3 linked text says it was "adopted" after the single-ion results. The staff's reasoning is kept, and the point is recorded here.
  - n5 is PRC/stimulus because it produces argued states (n7, n10).
- **Audits:** 1 (o12, text_silent, qualifies n10). It is fair. The control claims (n17, n22, n18, n21) end in contrasts edges to the main branch.

## Splits and merges
- **n8 -> n8 + n20.**
  - n8 (spine) keeps the interfacial buffer: HOAc neutralises OH-, so interfacial pH stays near 5.3 and does not reach 7.5.
  - The new n20 (MEC/pathway, side) holds the bulk pH rise from OAc- hydrolysis, ~4.1 -> ~5.3.
  - o7 now evidences n20, k1 is premise_for n20, n20 supports n8, and n20 explains n11. The text ties bulk pH to corrosion and interfacial pH to by-products.
- **n17 -> n17 + n22.** The NH4+-only control (~970 h, o3) and the OAc--only control (~430 h, o6) are now separate claims. Both contrast n13.
- **n18 -> n18 + n21.** n18 (STR) keeps the claim that ZHSH forms with NH4+ alone. The new n21 (PRP/value, chemical_corrosion, basis argued) holds that NH4+ alone does not inhibit corrosion. n18 supports n21, and n21 contrasts n11.
- **Merges:** none. No two nodes state the same claim. o11 and o12 read the same panel in opposite directions, and that conflict is the audit.

## Source / read_from changes
- n16: source inferred -> text. The conclusion is stated in linked text F1 and F4.
- o2: source figure -> text. That the curves are chronoamperograms comes only from the caption.
- o7: source figure -> text. Only the linked text says the pH is bulk rather than interfacial.
- n13: requires_unseen now includes "ten times the blank" (linked text).
- o8: requires_unseen now includes two facts. The blank field is F2c, which is not offered as a panel, and the colour bar that maps to ~5.3 is clipped from the crop.
- o1, o7: read_from axis -> annotation. The values are printed above the bars, and the labels repeat the listed strings 'Substrate:Zn(101)' and '2MZnSO4'.
- o3, o6, o16: read_from stays axis, because the failure times are read off the time axis. Their only annotation is the test-condition string, recorded as attrs.condition_from = annotation.

## Mode changes
None. n12 is the only claim with two causes edges (n7, n10), and it is correctly "joint": only the linked text weighs dead Zn against side reactions.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 0.
- **M1** (NH4OAc -> shielding layer + suppressed ZHSH): supports (n3, n5, n6, n7, n8, n10). In the graph, ZHSH is strongly reduced rather than absent, because o12 qualifies n10.
- **M2** (shielding + no ZHSH -> CE 99.7%, 3500 h, corrosion resistance): supports (n7, n10, n12, n13, n11). In the graph, corrosion resistance comes from the buffer MECs (n8, n20), not from the structure nodes.
- **M3** (CE, cycling, corrosion -> 5000 mAh cm-2 and a stable full cell): supports (n12, n14, n15, n19). The graph adds a cathode path, n15 (attributed): NH4+ suppresses Od-NVO dissolution. The cumulative capacity appears only in the DSC/comparison node n19.
- **M4** (NH4OAc -> 3500 h, 5000 mAh cm-2, full-cell retention 32.2% -> 83.7%): supports (n3, n13, n14, n19). The controls n17 and n22 show that neither ion alone gets there.
