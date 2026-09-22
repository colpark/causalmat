# Judge review: Advanced_Composites_and_Hybrid_Materials/s42114-021-00398-8

**Verdict:** accept with fixes. Structure only: no figures or crops were opened, and no panel citations or techniques were ruled on (the blind second read checks those). Splits: 5 (s15, k3, o1, o3, o5). Merges: 0. Source changes: 4, plus requires_unseen added on 2 more nodes. read_from changes: 0. Mode changes: 0. MatMech: 4 supports / 0 contradicts / 0 not covered.

Graph now has 52 nodes, 64 edges and 18 spine nodes. It passes the v04 validation checks (types, rels, mm_ops, panel ids, cue/technique, derived chains, modes, spine connectivity and support).

## 1. Spine order

- The spine reads need s1 -> hypothesis s2 -> ternary design s3, sponge carrier s4, loading sweep s5 -> hydrothermal composite s7 -> dip deposition s8 -> phases s9, distribution s10, p-n junction s11 -> MEC s15 (junction transfer) and s22 (MXene conduction) -> lower recombination s14 -> activity ranking s16. A parallel loading branch runs s8 -> optimum s17 -> down-select s18. The two meet at recycling s19 -> conclusion s20. It is one connected path in stage order, with 18 nodes and two branches.
- Every spine STR/PRP/PRF claim has an evidences edge. s11 (argued) has premise k1. Of the MECs, s15 has k1 and s22 has k3.
- v04 rules hold. s18 down_select is reached by motivates from s17. s16/s17 are PRP/value (catalytic) and s19 is PRF/service_capability. s14 PRP/descriptor carries proxy = PL.
- Audits: 5, all fair. o9, o14, o15 and o17 bear on spine claims. o12 qualifies s13, which is off-spine but joins s16 by causes.
- o6 (FTIR: OH/H2O bands) is weak evidence for s9 phase identity. The edge is kept and the weakness is noted in image_note.

## 2. Splits and merges

| node | into | why |
|---|---|---|
| s15 | s15, s22, s23 | three mechanisms in one label: junction charge transfer (s15, spine), MXene electron conduction (s22, spine, explains s14), radical oxidation of HCHO (s23, off-spine, explains s16) |
| k3 | k3, k6 | conductivity (-> s22) and surface hydrophilicity/dangling bonds (-> s24) are two facts |
| o1 | o1, o19 | BiOCl reflections and the Ti3C2 ~7.8 deg peak come from two traces; o19 evidences s9 |
| o3 | o3, o20, o21 | three samples' morphologies (F3a, F3b, F3c), one node each; all evidence s10 |
| o5 | o5, o22 | Bi/Cl co-localization (F3e/f/i/j) vs diffuse Sn/O (F3g/h); o22 evidences s10 |

Other structural changes:
- **s24 added** (off-spine MEC/pathway, argued): the HCHO-affinity claim. s12 (supports) and k4 (premise_for) had been wired into s15, whose label never stated this claim. Both edges were moved to s24, and s24 explains s16.
- **s11** label trimmed to the junction claim. Its "on conductive Ti3C2" clause is now s22.
- **o6** trimmed to one reading. The absent ~520 cm-1 band moved to image_note: the audit budget is full, and that reading does not change s9's support.
- **o10** trimmed to the visible-absorbance ranking. The edge positions moved to image_note, which also notes that the legend order on F7a equals the ranking.

Merges: none. No two nodes state the same claim.

## 3. Source and read_from changes

| node | source | requires_unseen added |
|---|---|---|
| s12 | figure -> text | the 90 deg hydrophobic/hydrophilic threshold (linked text) |
| s17 | figure -> text | nSFBS = number of immersions (linked text) |
| o16 | figure -> text | nSFBS = number of immersions (linked text) |
| o9 | figure -> text | text states Ti3C2/BiOCl/SnO2 PL is stronger than FBS |
| s14 | inferred (kept) | weaker PL = less radiative recombination (prior knowledge, k2) |
| s20 | inferred (kept) | junction rests on text-only n/p types; 'optimal loading' needs nSFBS meaning |

New nodes carry their own source: s22, s23, s24, k6, o19, o20 and o21 are text; o22 is figure.

read_from: no changes. o7 and o11 are annotation (sample labels and angle/eV values drawn on F5 and F7b). The o5/o22 channel keys ('Bi', 'Sn', 'Ti') are only keys, and the reading is the spatial pattern, so they stay pixels. o10 reads curve heights, so it stays axis. F2, F4, F6 and F8-F10 have no listed annotations.

## 4. Mode changes

None. Only s16 has two or more causes edges (s14, s13). Both are joint, which is correct: the F8 caption shows no choice between charge separation and light absorption.

## 5. MatMech tally (recorded after the graph was final; graph not edited)

supports 4, contradicts 0, not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | hydrothermal mixing + dip deposition -> 2D/2D heterojunction, p-n junction, hydrophilic surface | supports | s7, s8, s9, s10, s11, s12 | MatMech '12 h' vs scheme 10 h (s7) differ in the number, not the link |
| M2 | heterojunction -> reduced PL, lower band gap, 16 deg contact angle | supports | s10, s11, s14, s13, s12, o8, o9, o11, o12, o7 | graph qualifies PL (o9) and band-gap values (o12) |
| M3 | heterojunction, hydrophilic Ti3C2 -> 90.3% degradation, '85.2% retention' after 5 runs | supports | s11, s14, s13, s15, s22, s24, s16, s19, s4, o13, o18 | MatMech 85.2% is 100-14.8; F10/text give 75.3% in run 5 (o18) |
| M4 | dip-cycle count -> activity peaks at 3SFBS then falls | supports | s5, s8, s17, s21, o16, o17 | o17 qualifies the optimum (overlapping error bars) |
