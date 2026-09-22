# Judge review: Nano_Letters/10.1021_acs.nanolett.0c03945

**Verdict:** accept with fixes. This is a structure-only review. No figures or crops were opened, and panel citations were not ruled on. The graph has 16 spine nodes and 40 nodes in total.

The spine is one connected, stage-ordered path:
- gap (n1) -> hot-electron hypothesis (n2) -> Au/Al2O3/p-Si junction (n3) + bar architecture (n4) + resonance sweep (n18) + divide-and-fit method (n5)
- -> deposition (n6) -> lithography (n7) -> isolated bars (n8) -> ~2 eV plasmon (n10) -> plasmon-decay heating MEC (n13) -> two-slope T_e (n14) -> ATLE (n12) -> conclusion (n16)
- One control branch: n8 -> 1.3 eV device (n19) -> lower T_e (n17), which contrasts n14 and feeds n16.

Every spine STR/PRP/PRF/MEC node has OBS evidence: n8 (o1), n10 (o4, o5, plus premise k3), n13 (o8, o12, plus premise k4), n14 (o9, o11), n12 (o2, o4, o6, o7), n19 (o14) and n17 (o13). The graph has 2 audits (a1, n21), and both are fair:
- a1 bounds the high-voltage slope.
- n21 bounds the cutoff-level choice behind the o12 correlation.

## Changes
- Split n17 into n17 and n22 (details below).
- Trimmed the n13 label. Its clause "k_B T_e scales with the plasmon energy" repeated premise k4, which is premise_for n13. The scaling now lives only in k4.
- Changed the o2 label. "Diffraction-limited" is a linked-text fact that no panel shows, so it is now "small".
- n8 -> n19 (causes) is kept because it is the only v04-valid spine link into the control branch. It is flagged: the F2b bars are the 2.0 eV device, and the 1.3 eV device's geometry is only in the Supporting Information. That fact is now listed in n19's requires_unseen.
- Added a1 -> n22 (qualifies). The large high-voltage error bars also bound the slope comparison.

## Splits and merges
- **n17 -> n17 + n22.** The old label stated two claims about the 1.3 eV device.
  - n17 keeps "T_e much lower than the 2.0 eV device". It stays on the spine with its edges: n19 causes, o13 evidences, contrasts n14, supports n16.
  - New n22 is "above 1.3 V, T_e rises with the same slow slope as the 2.0 eV device above 2 V". It is off-spine to avoid a fork inside the control branch. New edges: n19 -> n22 causes, o13 -> n22 evidences (compare_across_conditions), n22 -> n16 supports, a1 -> n22 qualifies.
- Merges: none. The pairs o11/n14, o14/n19 and o13/n17 are each a readout and its claim, not duplicates. The overlap between n13 and k4 was fixed by trimming the n13 label, not by a merge.

## Source / read_from changes
- n19: stays text. Added to requires_unseen: the second device's bar geometry (Supporting Information).
- n22 (new): source text. requires_unseen lists that the red series is the second device and that its resonance is at 1.3 eV (caption and linked text).
- No other source changes. Every node has attrs.source and requires_unseen. The text-sourced claims (n1, n9, n10, n15, n17, n19) list their unseen facts.
- read_from: no changes.
  - o9 stays "annotation". The fitted values are written in the F4 image, even though the uncropped F4 has no listed annotation strings.
  - No axis or pixel node restates a listed annotation string. The listed strings are 'I!I', '(mA)', 'rent', 'in', 'sec', '(eV)', '(photons'.

## Mode changes
- None. Only n12 has two or more causes edges (n14, n10, n9). It is "joint", and that is correct: no caption presents the causes as alternatives. The F4 caption divides each spectrum by the plasmon spectrum, which treats emission as the plasmon envelope times the hot-electron distribution.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 0.
- **M1:** ALD, Au evaporation and EBL -> Au bar array on p-Si with an Al2O3 barrier. **Supports** (n6 -> n7 -> n8).
- **M2:** bar array -> emission spectrum and electron temperature. **Supports** (n8 -> n10 -> n14).
- **M3:** emission spectrum and T_e -> ATLE. **Supports** (n10 and n14 joint into n12).
- Side note: M3 says "ATLE fraction increases with voltage". This conflicts with o7, where the shaded fraction shrinks from 1.6 to 2.2 V. The M3 cause->effect pair itself is supported.
