# Judge review: Biomaterials/j.biomaterials.2010.08.096

Optimising PEG-PMHC18 surface chemistry on SWNTs for in vivo photothermal tumor ablation. This is a structure-only review. No figures or crops were opened, and no ruling was made on panel citations or techniques.

## Verdict
Accepted with fixes. The spine runs:
- need n1 -> hypothesis n2 -> base system n3 and variable sweep n4 -> polymer synthesis n5 -> SWNT coating n6 -> coating PEG density n18 (new) -> circulation MEC n9.
- n9 splits into tumor uptake n10b and skin accumulation n11, which meet at the down-select n13.
- n13 -> laser treatment n14 -> tumor heating n15 (also caused by n10b) -> ablation n16 -> conclusion n17.

There are 15 spine nodes, one connected path with two branches (the tumor/skin trade-off). Every spine STR/MEC/PRF node has OBS evidence. n15 is basis argued, with KNW premise k1 (the heating is reported in text only). There are three audits: o2 (qualifies n7), l1 (qualifies n12) and l2 (qualifies n16). All three are fair. The graph has 39 nodes in total.

## Changes
- Removed n7 -causes-> n9. Dispersion into single tubes is not what the paper says sets circulation, and the n9 label names PEG density and length as the cause.
- Added STR/chemistry/composition n18: the coatings differ in PEG grafting density, which tracks the feed ratio. Its source is text. New edges: n6 -produces-> n18 and n18 -causes-> n9.
- Added OBS o13 (text_only, NMR PEGylation ratios from F1 linked text) -evidences-> n18.
- Moved n7 off the spine. It stays as a side claim, evidenced by o1 and qualified by o2.

## Splits and merges
- **n10 -> n10, n10b.**
  - n10 is lower RES (liver/spleen) uptake, with premise k2. It is now a side claim that still motivates n13.
  - n10b is higher tumor uptake, with premise k3 (EPR). It is on the spine and takes over the causes edge into n15, since the tumor load supplies the absorber.
  - o6 and o7 evidence both nodes.
- Merges: none. g1/n13 and n10/k2 play distinct roles.

## Source / read_from changes
- n3: figure -> text. The Hipco grade, the polymer identity and the noncovalent wrapping come from the caption and linked text.
- o2: figure -> text. "The other nine suspended" comes from the F1 caption; the table marks only 5%-2k.
- o5: figure -> text. The half-lives come from first-order decay fitting and Table 1 (F2 linked text).
- n18 and o13 are new nodes with source text. o13 is text_only. Its read_from is "axis" by the v07 convention for numeric readouts that exist only as text, because no panel exists.
- read_from: no changes. o2 and o10 already restate listed annotations. The other OBS nodes read from pixels or axes.

## Mode changes
None. n15 is the only claim with two causes edges (n14, n10b). It stays "joint": the laser and the tumor SWNT load act together, and no caption shows a choice between them.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | functionalization + purification -> single tubes / small bundles | supports | n6, n7, o1 |
| M2 | higher PEG density/length -> longer half-life, higher tumor and skin uptake | supports | n18, n9, n10b, n11, o4-o7 |
| M3 | dispersed morphology -> NIR absorption and half-life | not covered | n7, k1 |
| M4 | 12-13 h half-life, tumor ~15 / skin ~3 %ID/g -> photothermal ablation | supports | n13, n10b, n14, n15, n16, o11, o12 |
| M5 | surface chemistry choice -> effective ablation | supports | n18, n9, n10b, n13, n15, n16 |
| M6 | 5%-2k polymer, limited solubility -> fails to suspend SWNTs | supports | o2, n7 |
| M7 | 100%-5k coating -> ~29 %ID/g skin despite ~23 %ID/g tumor | supports | n11, o7, o8, o9, o10 |

supports 6 / contradicts 0 / not covered 1

Notes on the tally:
- MatMech says "covalent anchoring". The polymer is amphiphilic and wraps the tubes noncovalently (n3), so that wording is a MatMech error. It does not change any verdict.
- M4's claim of low laser power thanks to targeting is not in the graph.
