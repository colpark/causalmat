# Judge review: Advanced_Functional_Materials/10.1002_adfm.202008632

**Verdict:** accept with fixes. Structure-only review: no figure or crop was opened, and no panel citation or technique was ruled on (every cited panel is checked separately by a blind second read). The graph now has 45 nodes, 57 edges and 19 spine nodes.

This is a review paper, so the OBS nodes carry `attrs.reproduced_from` and keep the source study's provenance; the spine is the review's own argument, not one experiment.

## Spine
One connected path, 19 nodes:

n1 need -> n2 gap -> n3 hypothesis -> n4 add boron (sp3 borate / sp2 Lewis-acidic) -> n5 sweep: linked vs added. From n5 the argument splits into the two incorporation modes the paper compares:

- **linked:** n6 polycondensation -> n9 backbone borate centres -> n12 anion immobilisation and n13 the -CF3 electronic mechanism -> n14 Li+ transference number; and n6 -> n7 UV cure inside a scaffold -> n10 3D crosslinked network;
- **added:** n8 in-situ layer formation -> n11 cathode interphase and n25 Li-metal SEI.

The two meet at n16 (uniform plating, caused by n25 and n14) and n17 (stable cycling, caused by n10, n16 and n11), then n18 trade-off -> n19 conclusion. Stage order holds throughout, with MEC bridging (n12, n13 between STR and PRP; n18 between PRF and DSC).

Every spine STR/PRP/PRF/MEC claim now has OBS evidence or a KNW premise (four did not before: n9, n10, n18 and the new n25). Audits: 2 (o9, the F7 panel-assignment conflict, and n23, the four remaining gaps) - within budget and fair. v04 decision rules hold; all types, rels, mm_ops and modalities are v04 entries; every figure-bearing OBS edge carries an mm_op.

## Changes
- **n9** label trimmed to the bonding claim. "leaving Li+ as the only mobile ion" restated n12/n14 and is carried by them.
- **n12** label trimmed to the anion-immobilisation mechanism. "so Li+ carries nearly all the current" is n14's claim, and n12 already explains n14. The trim also removes the one part of n12 that no panel shows.
- New premise edges k1 -> n9, k4 -> n25, plus two new KNW/fact nodes: **k5** (a 3D crosslinked network immobilises a large amount of plasticizer and keeps dimensional stability; the F5/F8 linked text) premise_for n10, and **k6** (immobilising the anion raises t+ but lowers total ionic conductivity) premise_for n18.

## Splits and merges
- **n11 -> n11 + n25.** The label stated two claims at two electrodes, and the split fixes a real routing defect: the cathode-side DFT evidence (o12) was feeding an anode claim.
  - n11 keeps the amorphous LixBOyFz cathode interphase, panels F9c/F9f, evidence o12, and now causes n17.
  - n25 (new, spine, STR/interface, basis argued) is the borate-derived SEI on the Li metal surface: F8a, k4 as premise, o11 as evidence, produced by n8, and causes n16.
- **Merges: none.** n14/n15 are different properties, n12/n13 different mechanisms, n17/n21 different service claims (ambient vs 120-140 C), and o1/o4 read different studies (refs 45 vs 61/127).
- n23 (four remaining gaps) was considered for a split and kept: splitting a limitation list into four would push the audit count to five for no gain in the argument.

## Source / read_from changes
- **n7** figure -> text: the cellulose-membrane scaffold is named only in the F8 linked text; only the PVDF fibre is written on F4a.
- **n10** figure -> text: the 3D cross-linked network and the immobilisation of the plasticizer are stated only in the F5/F8 linked text. The node's own image_note already said no packet figure images the network.
- **n13** figure -> text: F3d carries no annotations; the electron-withdrawing reading is the F3 linked text almost verbatim, while the numbers are o2's reading of F3e.
- **n18** stays "inferred" but requires_unseen was empty and now lists the text-only conductivity range.
- **o2** read_from axis -> annotation: F3e has no axis labels and all six DFT values are printed inside the panel, so the observation restates written strings.
- read_from checked on all 14 OBS nodes and otherwise unchanged. o5 already used "annotation" and matches the two strings listed for F4f. o12 stays "pixels": F9a is annotated:false and the anionic/neutral split is read from the green/red colour, not from text. o6 and o13 stay "axis" (F5 is tier C with no panel list; F10a is annotated:false).

## Mode changes
Two claims have two or more causes edges, and neither carried a mode:
- **n16** (causes n25, n14) -> "joint". The Li-side interphase and the near-unity transference number act together; no caption offers a choice.
- **n17** (causes n10, n16, n11) -> "joint". Same reasoning.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
Supports 3, contradicts 1, not covered 0.

- **M1 Processing -> Structure. Supports** (n6->n9, n7->n10, n8->n11/n25). The porous-framework (ANP-5) structure is not a node; it survives only inside o4's image_note.
- **M2 Structure -> Property. Contradicts.** The transference-number half is supported (n9 -> n12/n13 -> n14, with k2). The "improved ionic conductivity" half is contradicted: n18 states an ionic-conductivity penalty for fixing the anion, n15 puts solid single-ion conductors at the bottom of the 5e-6 to 4.2e-3 S/cm range, and n22's image_note records the conventional dual-ion reference as the outermost trace on ionic conductivity in F11a. Mechanical strength is not a node.
- **M3 Property -> Performance. Supports** (n14 -> n16 -> n17, with n10 and n11 also causing n17; o1, o3, o4, o10, o11 and o5-o8). The graph routes the gain through transference number and interphase, not conductivity, and has no mechanical-property node.
- **M4 Processing -> Performance. Supports** (n5 -> n8 -> n11/n25 -> n16 -> n17 for the additive route; n20 -> n21 with o13 and o14 for the thermal route). Two qualifications: n20 has no incoming processing edge, and the graph reads the F10a TG result as stability *unchanged* by the boron ester (the 1:1:5 and 1:1:0 curves coincide), not as the improvement over carbonate liquids the record claims.
