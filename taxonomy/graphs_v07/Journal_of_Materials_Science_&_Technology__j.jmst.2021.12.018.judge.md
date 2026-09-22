# Judge review: Journal_of_Materials_Science_&_Technology/j.jmst.2021.12.018

**Verdict:** accept with fixes. This was a structure-only review. No figures or crops were opened, and panel citations and techniques were not ruled on. The graph has 16 spine nodes and 48 nodes in total. The spine is one connected, stage-ordered path: need n1 -> hypothesis n2 -> host n3 + S-modification n4 -> polycondensation n5 -> exfoliation n6 -> hydrothermal S loading n7 -> pyrolysis n8. From n8 it runs in two branches. Branch 1: C-S-C bonding n9 -> isotype S-scheme interface n11 -> MEC n12 -> charge separation n13. Branch 2: porosity n10. Both branches act jointly on the H2 rate n14, which leads to cycling n15 and the conclusion n16. Every spine STR/PRP/PRF/MEC node has OBS evidence, except n11 and n12, which rest on the KNW/model k4 with basis=argued. That is allowed, and n30 flags it. There are 5 audits (o8, o19, o25, o28, n30), all fair: each qualifies a spine claim (n9, n15, n13, n13, n12).

## Changes
- Split k5 into k5 and k7 (details below).
- Trimmed the o21 label to one claim, the 450-700 nm absorbance ranking. The absorption-edge position (~400 vs ~430 nm), which no node uses, moved to attrs.image_note.
- Filled requires_unseen on n9, n13 and n26.
- Changed read_from on o10, o16 and o17.
- No merges and no mode changes. The spine is unchanged.

## Splits and merges
- **k5 -> k5 + k7.** The old label stated two lookups, each a premise for a different claim.
  - k5 keeps "photocurrent / PL quench / lifetime -> charge separation" and stays premise_for n13.
  - New k7 is "smaller Nyquist arc -> lower Rct", with source prior_knowledge. The edge k5->n26 was rewired to k7->n26.
- Merges: none. The claim/readout pairs n10/o12, n14/o16, n18/o2 and n25/o21 are a claim and its evidence, not duplicates. o18 and o19 both read F6c, but one states persistence and the other the decline, so they are different claims.

## Source / read_from changes
- n9 (inferred, kept): requires_unseen now lists two facts. The S 2p 164.5-164.7 eV = C-S-C assignment comes from k2 (linked text F4, ref 39). S on N sites comes from the F1 inset and linked text F4.
- n13 (inferred, kept): requires_unseen now lists the k5 lookup and the text-only fitted lifetimes (Table S3, o28).
- n26 (inferred, kept): requires_unseen now lists the k7 lookup (arc = Rct).
- o10: axis -> annotation. It restates the listed "S2p" label and the printed 164.5 / 168.5 eV peak labels.
- o16: axis -> annotation. 5548.1 is the printed bar label in F6d.
- o17: axis -> annotation. 3.31% / 0.43% / 0.25% are printed point labels in F6b.
- Kept as they are:
  - o8, o9 and o12 are already annotation.
  - The other OBS nodes are axis or pixel readings.
  - o28 is text_only with source text. Its read_from "axis" is nominal, because it has no panel.

## Mode changes
- None. Only n14 has two or more causes edges (n13, n10). It is "joint", and that is correct: no caption presents porosity and charge separation as alternatives, and the linked text (F5, F7 "Secondly", F8 "Thirdly") lists them as co-acting.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 5, contradicts 0, not covered 0.
- M1: hydrothermal S loading + pyrolysis -> S-doped/S-free heterojunction, porous lamellar structure. **Supports** (n7, n8 -> n9, n10, n18; n9 -> n11). Reduced crystallinity and the (002) shift are not nodes. The lamellar shape n22 comes from exfoliation n6.
- M2: heterojunction + porosity -> charge separation, lifetime, photocurrent. **Supports** (n11 -> n12 -> n13; o22, o24, o26). The graph has no porosity -> separation edge. The lifetime gain is qualified by o28 (1-5%) and the PL argument by o25.
- M3: surface area / porosity -> active sites -> activity. **Supports** (n10 -> n14, joint). Active sites are not a node.
- M4: S doping -> extended visible absorption. **Supports** (n9 -> n25; o21). The o21 image_note records that the main edge is blue-shifted (Eg 2.85 > 2.75 eV), against MatMech's "red-shifted" wording. The support rests on the 450-700 nm tail.
- M5: properties -> 5548.1 umol/g/h with robust durability. **Supports** for the rate (n13, n10 -> n14, and n25 -> n14 supports). Durability is qualified: n15 is partial, and o19 reads ~11% loss where the text says "negligible".
