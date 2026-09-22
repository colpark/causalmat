# Judge review: Advanced_Materials/10.1002_adma.202004707

**Verdict:** accept with fixes. This was a structure-only review: no figures or crops were opened, and panel citations and techniques were not ruled on.

After the fixes the graph has 19 spine nodes and 49 nodes in total. The spine is one connected path: need -> fused-network hypothesis -> HAB+PTK design + TFMSA route -> condensation -> pyrazine-fused bonding (n6) and ABC-stacked lattice (n8). From there it splits into two branches:
- **Mobility.** Conjugation MEC n17 -> mobility n16 -> highest-in-class comparison n23. The flake/thickness sub-branch (n13 -> n12 -> on/off n14) now rejoins at n23.
- **Doping.** HCl design n19 -> vapour treatment n18 -> conductivity trend n20 and two-orders claim n29, with the dopant MEC n21 explaining both.

Both branches end at conclusion n22. Every spine STR/PRP/MEC node has OBS evidence or a KNW premise; the mobility (n16) rests on text-only o20 (Table S5). There are 4 audits: o6, o9, o18 and n28. All are fair. o18's arithmetic checks out: 1/(900 ohm x 43 nm) ~ 260 S/cm.

## Changes
- **Split n21 -> n21 + n29.**
  - n21 keeps only the mechanism: physically adsorbed HCl acts as a surface dopant.
  - New spine n29 (PRP/value, source text) is "two orders of magnitude over pristine".
  - New edges: n20->n29 supports, n21->n29 explains, o19->n29 evidences (read_trend), n29->n22 supports.
  - The o18 qualifies edge moved from n21 to n29, because o18 contradicts the magnitude, not the mechanism.
- **Split n7 -> n7 + n30.**
  - n7 is now "XPS detects only C, N and O" (source figure, evidence o8).
  - New side node n30 is the basal-plane C5N / C30H17N6 stoichiometry (source text, Fig. S1).
  - New edges: n5->n30 produces, n30->n6 supports.
- **Rewire n14->n22 to n14->n23 (supports).** The on/off ratio is the "discernible on/off" condition of the comparison. The change also keeps the argument to two branches.
- **Merges: none.** Claim/readout pairs such as n16/o20, n20/o19 and n14/o16 are not duplicates.

## Source / read_from changes
- n7: text -> figure after the split. The facts from Fig. S1 and S4 moved to n30 or the note.
- n29 and n30 are new nodes with source text. Their facts are listed in requires_unseen.
- n21: requires_unseen narrowed to the mechanism.
- o18 stays inferred. requires_unseen now lists the relation sigma = 1/(R_sq t) and "R_DS*W/L is the sheet resistance".
- read_from: no changes.
  - o8 restates the listed F3c strings C1s/N1s/O1s and is correctly annotation.
  - o3 and o7 use unlisted OCR tokens, so annotation is acceptable.
  - o1, o2, o5, o6 (F2a) and o13 (F3a) use the listed legend strings only to name traces. The reading itself is taken off the axis. They stay axis, and I added attrs.trace_id_from = annotation.
  - F4 is tier C and has no annotation list.

## Mode changes
None. n24 is the only claim with two causes edges (n6, n10). It is "joint", which is correct: the F3 linked text credits the fused rings and the large grains together, and no caption shows a choice between them.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 0.
- M1: condensation in TFMSA at 175 C -> fused network, ABC stacking, 3.40 A. **Supports** (n4, n5 -> n6, n8, n9).
- M2: fused ABC network -> 996/501 cm2/Vs. **Supports** (n6, n8 -> n17 -> n16). In the graph this link is attributed/inferred, and the mobility is text only.
- M3: mobilities -> highest in pristine polymers without doping. **Supports** (n16 -> n23).
- M4: HCl doping at 160 C -> 1038 S/cm. **Supports** (n18 -> n20, n29). The graph adds the o18 audit: pristine flakes already conduct at ~260-450 S/cm, which weakens the "two orders" claim but not the value.
