# Judge review: Bioactive_Materials/j.bioactmat.2019.12.006

**Verdict:** accept with fixes. This review checks structure only. No figures or crops were opened, and no panel citations or techniques were ruled on (the blind second read checks those). Splits: 1 (n21). Merges: 0. Source changes: 2 (n8, n15). read_from changes: 1 (a1). Mode changes: 1 (n19). MatMech: 7 supports / 0 contradicts / 0 not covered.

The graph now has 49 nodes, 66 edges and 19 spine nodes. It passes the v04 validation checks (types, rels, mm_ops, panel ids, cue/technique, modes, spine connectivity and support).

## 1. Spine order

- need n1 -> hypothesis n2 -> PPAm platform n3 and dual modification n23 -> PPAm deposition n4 -> NO loading n6 -> NONOates n8 -> ~1 h burst n9 -> down-select of C-F multilayer n10 -> PPAmF build n11 -> BVLD coupling n12 -> NO loading n13. Two branches follow: surface BVLD n14 -> anti-thrombin activity n17; bulk NONOates n15 -> prolonged release n16. They meet (joint) in platelet suppression n18 -> AV-shunt thromboresistance n20 -> conclusion n22. One connected path in stage order, with two branches. The DES/down_select loop (n9 motivates n10) is allowed by v03/v04.
- Every spine STR/PRP/PRF claim is backed: n8 (o3, k2), n9 (o4), n14 (o5, o7), n15 (o6, k2), n16 (o9, o8), n17 (o10, k4), n18 (o11-o13), n20 (o15-o19).
- Spine went from 20 to 19: after the n21 split both MECs are off the spine (see section 2).
- Audits: 1 (a1: the C-F band nearly vanishes after NO loading, so the intact barrier assumed by n24/n16 is not shown). Fair.

## 2. Splits and merges

| node | into | why |
|---|---|---|
| n21 | n21, n25 | the label stated two pathways (NO-cGMP anti-platelet; BVLD thrombin inactivation) and their synergy. n21 keeps NO-cGMP (text). n25 (inferred, basis argued) carries BVLD, with k4 premise_for and n17 supports moved to it. Both explain n18 and n20; n25 also explains n19; o16 evidences both. The synergy is the joint mode on n18 |

Both MECs set spine=false: keeping both would make 21 spine nodes. n18 -> n20 was already a spine causes edge, so connectivity holds.

Other changes:
- n16 -> n19 causes added. NO-PPAmF also halves fibrinogen (F5d/e; linked text [50]), and n19's label already says so.
- o6 label trimmed to the NONOate bands that n15 uses. The H-bonded -OH band moved to image_note.

Merges: none. n8 and n15 state the same bonding in different coatings (PPAm vs PPAmF) at different stages, so they are not duplicates. n23 (surface BVLD + bulk NO) was kept as one node: it is one dual-site design decision, realized by n12 and n13.

## 3. Source and read_from changes

| node | change | requires_unseen added |
|---|---|---|
| n8 | source figure -> inferred | starred FTIR bands -> diazeniumdiolate mapping (k2, prior knowledge) |
| n15 | source figure -> inferred | same |
| a1 | read_from pixels -> annotation | it names the band by the listed F3b string 'C-F' |

The new node n25 is inferred (k4 + linked text). All other read_from values fit: o1, o2, o3, o5, o6 and o7 restate listed annotations; o4, o8-o10, o12-o14 and o17-o19 read axis values; o11, o15 and o16 read pixels (the only listed strings are sample labels).

## 4. Mode changes

- n19: single cause (n17) -> joint (n16, n17), because of the new edge. The F5 caption shows no choice.
- n18 (n16, n17) and n20 (n18, n19) were already joint. This is correct: no caption shows a choice.

## 5. MatMech tally (recorded after the graph was final; the graph was not edited)

supports 7, contradicts 0, not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | alternating PPAm/C-F plasma deposition -> water-resistant multilayer | supports | n10, n11, n24, n16 | no STR node for the layering; the barrier is MEC n24 (attributed), qualified by a1 |
| M2 | NHS-EDC grafting -> covalent BVLD on surface primary amines | supports | n23, n12, n14 | keeping bulk amines for NO is not stated |
| M3 | high-pressure NO loading -> bulk NONOates | supports | n6, n8, n13, n15, n5, k2 | |
| M4 | surface BVLD + bulk NONOates -> anti-platelet + anti-coagulant | supports | n14, n17, n15, n16, n18, n21, n25 | |
| M5 | NONOates + C-F barrier -> lower burst, release >8 h | supports | n15, n16, n24, o9 | |
| M6 | dual structure -> AV-shunt thromboresistance | supports | n18, n19, n20, n21, n25 | |
| M7 | sustained NO + BVLD activity -> fewer platelets, less Fg, less thrombus | supports | n16, n17, n18, n19, n20 | MatMech says Fg falls "only when BVLD is present", but F5d/e (n19) show NO-PPAmF halves it too. Its "32.5-fold vs NO-only" is an activation fold per the linked text |
