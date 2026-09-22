# Judge review: Progress_in_Organic_Coatings/j.porgcoat.2021.106157

A PCL/lawsone bilayer coating on alkali-treated AZ31 for corrosion resistance and antibacterial activity. This is a structure-only review. No figures or crops were opened, and no ruling was made on panel citations or techniques.

## Verdict
Accepted with fixes.

The spine runs:
- need n1 -> hypothesis n2 -> base system n3, modification n4 (lawsone) and architecture n5 (bilayer);
- n3 -> alkaline treatment n6 -feeds_into-> deposition n7;
- n6 -> Mg(OH)2 layer n8; n7 -> coverage n9 and lawsone in the inner layer n10;
- n8, n9, n10 -> corrosion-resistance ranking n11 (joint), explained by barrier n12 and lawsone complexation n13;
- n10 -> 7-day barrier retention n14 (n13 explains) -> with n11 -> immersion protection n15 (joint);
- n10 -> antibacterial n16;
- n15 and n16 -> conclusion n17.

There are 17 spine nodes, one connected stage-ordered path, with two branches (corrosion, antibacterial). Every spine STR/PRP/PRF/MEC node has OBS evidence or a KNW premise: n10 is basis argued with k2 as its premise, and n13 is attributed with k6 as its premise. There are two audits, both fair: o6 qualifies n10 because the PCL-LS FTIR equals PCL, and o21 is text_silent (the F9C post-immersion FTIR). There are no cycles. The graph now has 54 nodes and 68 edges.

## Changes
- Split n9 and n11 (see below). o12 now evidences n11b instead of n11. I added four edges: n7 -produces-> n9b, o4 -evidences-> n9b (inspect_local_feature), n9b -supports-> n12, and n9 -causes-> n11b.
- The spine is unchanged: n9b and n11b are side claims.

## Splits and merges
- **n9 -> n9, n9b.** n9 is defect-free, uniform coverage (STR/microstructure/distribution; o3, o4, o7). n9b is the absence of a gap at the coating/oxide/substrate interfaces (STR/interface; o4).
- **n11 -> n11, n11b.** n11 is the ranking AZ31 < AZ31-OH < PCL < PCL-LS (PRP/value). n11b is pitting breakdown on the uncoated samples and none on the coated ones (PRP/behavior_class; o12).
- **Merges: none.** The claim/OBS/KNW pairs (n18/o5, n13/k6, n23/k5) have distinct roles.

## Source / read_from changes
- **n11: inferred -> text.** The test medium (Hank's solution) is given only in the linked text.
- **n15: inferred -> text.** The medium and 37 C come from the F8/F9 captions. The F8 row order comes from the linked text.
- **n22: inferred -> text.** The hFOB cell type and the extract exposure come from the caption and linked text.
- **New nodes.** n11b is text (the pitting attribution, ref. [47]). n9b is inferred.
- **read_from: no changes.** o1, o7, o2 and o12 are already annotation. o8 and o14-o17 cite legend strings but read values off the axis.

## Mode changes
None. Both multi-cause claims stay joint, because no caption shows a choice between the causes:
- n11 (n8, n9, n10);
- n15 (n11, n14).

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | alkaline pretreatment + bilayer casting -> bilayer, Mg(OH)2 layer | supports | n5, n6, n7, n8, n9, n9b, n10 |
| M2 | bilayer + Mg(OH)2 -> low Icorr/high IE, CA 96 deg, inhibition zones | supports | n8-n13, n16, n19 |
| M3 | bilayer -> >85% hFOB viability | supports | n11, n22, o23 |
| M4 | bilayer + Mg(OH)2 -> less H2, lower pH, intact surface | supports | n8-n11, n15, o18-o20 |
| M5 | lawsone in bilayer -> stable impedance over 7 d | supports | n7, n10, n13, n14, o14-o17 |
| M6 | alkaline pretreatment -> adhesion 4B vs 3B, lower initial corrosion | supports | n6, n8, n20, n21, n11 |

supports 6 / contradicts 0 / not covered 0

Notes on the tally:
- **M2:** contact angle n19 has no causes edge from structure. It reaches the corrosion claim only through n19 -supports-> n12.
- **M3:** structure reaches viability only indirectly, through n11 -causes-> n22 (lower degradation).
