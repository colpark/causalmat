# Judge review: Journal_of_Advanced_Ceramics/s40145-021-0536-4

**Verdict: accept with minor changes.**

This review checks structure only. No figures or crops were opened. Panel citations and techniques are left to the blind second read.

## Checklist
- **Spine:** 17 connected nodes. need (n1) -> hypothesis (n2) -> three binders (n3) + temperature sweep (n4) -> SPS (n5) -> S1/S3 binder reaction (n6), unreacted S2 binder (n21), porosity (n8) -> cBN/binder bonding (n9; CTE-mismatch MEC n10 for S2) -> fracture mode (n11) -> hardness (n12), strength (n13), toughness (n14) -> down-select S1 (n15) -> RT-800 C retention (n16) -> conclusion (n18).
- **Evidence:** n6 (o1, o3, o6); n21 (o2, o6); n8 (o7, o8, o16); n9 (o14, o15, o18; k3); n10 (basis argued; k1); n11 (o14, o15, o17, o18, o19; k4); n12 (o9); n13 (o11; k2; o13 qualifies); n14 (o12); n16 (o20).
- **v04 rules:** pass. n3 is modification (binder added to a cBN base). n15 is down_select, motivated by n12-n14. n11 is behavior_class (failure mode). n16 is service_capability.
- **Audits:** 1, fair. o13 (text_silent): S2 strength falls from 1650 to 1700 C while its porosity keeps falling (qualifies n13).

## Splits and merges
- **n6 -> n6 + n21.** The n6 label stated two claims about different samples. n6 keeps the S1/S3 binder reaction (o1, o3, o6). The new n21 (STR/phase/identity, spine) holds the unreacted S2 binder (o2 moved here; o6 also evidences it). n5 produces n21.
- Rewired: n6 -> n10 supports became n21 -> n10, because the CTE-mismatch pathway rests on unreacted Al2O3 in S2. Added n21 causes n9 and n21 causes n12 (both joint), carrying the S2 share of the old n6 causes edges.
- **Merges:** none.

## Source / read_from changes
None. Every claim that depends on the caption's panel-to-sample mapping is already "text", and that mapping is listed in requires_unseen. o1-o4 restate the F2 legend strings and are "annotation". o7, o8 and o11 stay "axis": their listed annotations are OCR'd axis titles ('Apparentporosity(%)', 'Bulk', '(MPa)'), which the nodes do not restate as content. o14 stays "annotation" (region identity comes from the 'CBNE' and 'Sialon' strings). o15-o19 are pixels, with no listed annotation restated.

## Mode changes
None. n9 (n6, n7, n21), n12 (n8, n6, n21) and n13 (n11, n8) are all "joint". No caption shows an either/or choice.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 5, contradicts 0, not covered 0.
- **M1** (SPS -> SiAlON in S1, low porosity, no hBN in S1/S2): supports (n5, n6, n21, n8, n7). SPS suppression of hBN and uniform cBN distribution are not covered.
- **M2** (SiAlON + low porosity in S1 -> best strength, toughness and hardness): supports (n6, n8, n9, n11, n12-n14).
- **M3** (unreacted Al2O3-ZrO2 with CTE mismatch in S2 -> low strength and toughness despite low porosity): supports (n21, n10, n9, n11, n13, n14, o13).
- **M4** (Ti-Al binder, high porosity in S3 -> inferior properties): supports (n6, n7, n8, n9, n13, n14). MatMech says S3 is "lowest", but the graph ranks S3 above S2 in strength and toughness (n14, o11). Agglomeration is not covered.
- **M5** (S1 RT properties -> retained at 800 C): supports (n12-n16, n17, n20).
