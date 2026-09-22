# Judge review: Biomaterials/j.biomaterials.2011.11.042

**Verdict: accept with minor changes.** Structure only. No figure or crop was opened, and panel citations and techniques are left to the blind second read.

## Spine and rules
- **Spine:** 17 connected nodes, unchanged. need n1 -> hypothesis n2 -> MBG host n3 + Co-for-Ca substitution n4 + 0/2/5% sweep n5 -> self-assembly synthesis n6 -> Co incorporated n7. From n6 and n7 it goes to ordered mesostructure n8 and reduced mesoporosity n9, which MEC n10 (argued) explains. It continues to Co2+ release n11 -> HIF-1alpha MEC n12 -> VEGF expression n13. Parallel branch: ampicillin loading n14 -> release n15 (joint causes n14/n8/n9) -> antibacterial n16 -> conclusion n17. Stage order holds, with one main line and one parallel drug branch. n1 is the only spine root.
- **Evidence:** n7 has o1. n8 has o3/o5/o6 plus k2/k3. n9 has o7/o8. n11 has o10. n12 has o17 plus k1. n13 has o18. n15 has o20. n16 has o22. **n10 had no OBS evidence and no KNW premise.** I added o4 -> n10 evidences (the small-angle XRD peak falls about 8x with Co, which is loss of mesoscale order). o9 still qualifies n10, and basis stays argued.
- **v04:** all types, rels and mm_ops are valid, and every figure-bearing OBS edge has an op.
- **Audits:** 5 (o4, o9, o11, o16, o21), all fair. o4 bounds "well-ordered". o9 is a narrow 5Co PSD that runs against the disorder MEC. o11 is 2Co Si release against "unchanged". o16 is 5Co VEGF secretion not above MBG. o21 is burst release against "sustained".

## Changes
- **n1 split:** "hypoxia-like cue AND guard against infection". n1 keeps the pro-angiogenic need (spine). The new **n26** (HYP/need, side) holds the osteomyelitis need, and k4 premise_for now points to n26.
- **n2 split:** "mimic hypoxia WHILE mesopores still carry a drug". n2 keeps the Co2+ hypoxia hypothesis (spine). The new **n27** (HYP/hypothesis, side) holds the drug-carrying mesopores hypothesis, with n26 -> n27 motivates and n27 -> n14 motivates. Both new nodes stay off the spine so the spine keeps a single root. The drug branch still enters the spine through n6 feeds_into n14.
- **o11 one claim:** the label now carries only the SiO4 reading (F5b). The Ca reading (5Co ~97 vs ~120 mg/L) moved to image_note, and the F5c citation was dropped along with it. This keeps the audit count at 5.
- **Merges:** none. n13 (VEGF gene) and n20 (VEGF secretion) are different claims, and so are o8 and o9 (peak position vs peak width).

## Source / read_from changes
- n17: source stays inferred. I filled requires_unseen (BMSC identity, hypoxia framing from the title, ampicillin/2Co-MBG from the caption, drug-delivery potential from the linked text).
- n26 and n27 are new, with source text and requires_unseen from linked text F11.
- read_from: no changes. o1 is already "annotation" (Co/Ca strings). The other OBS nodes read axis values or pixels, and their legend strings serve only as sample identifiers. The p-value marks on F7 are not in the packet's annotation lists.

## Mode changes
- None. n15 is the only claim with two or more causes edges (n14, n8, n9). It is **joint**, which I confirmed because no caption shows a choice.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 1, not covered 1. I split M3 and M4 because each has a compound effect that the graph treats differently.
- **M1** Co-substituted co-templating -> hierarchical porosity, ordered mesopores, lower SSA and pore volume: supports (n6, n7, n18, n8, n9, n10). Macropores measure ~100-250 um by the scale bar vs the 300-500 um stated (o2).
- **M2** Co incorporation -> Co2+ release, higher HIF-1alpha/VEGF/OCN: supports (n7, n11, n12, n13, n20, n21), but only in part. VEGF secretion rises for 2Co only (o16), and HIF-1alpha is stronger for 5Co only (o17).
- **M3a** mesopores/SSA -> ampicillin loading and release -> antibacterial: supports (n8, n9, n14, n15, n16). o21 shows the release is burst-dominated.
- **M3b** mesopore accessibility/SSA -> sustained Co2+ release: contradicts (n7, n9, n11). The graph attributes release to Co content, and 5Co-MBG has the lowest SSA yet releases the most Co2+.
- **M4a** ampicillin release -> anti-bacterial activity: supports (n15, n16).
- **M4b** VEGF/HIF-1alpha -> improved angiogenesis and osteogenesis: not covered (n12, n13, n17, n24). The graph ends at BMSC readouts, and ALP is unchanged.
