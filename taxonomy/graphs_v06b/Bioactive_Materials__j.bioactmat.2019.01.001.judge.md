# Judge review: Bioactive_Materials/j.bioactmat.2019.01.001 (v06b)

**Verdict:** accept with minor fixes

Checklist: the spine (15 nodes) reads as the paper's argument, with a degradation branch (s7-s11) and a cytocompatibility branch (s12-s13) that meet at s14 and run on to s15. Every spine STR/PRP claim has evidence, and every MEC/PRF node has basis argued. v04 validation: 0 problems. There are 4 audits (b8, b12, L1, L2) and they are fair. The mm_ops name what a reader does.

## Changes

- b4: label corrected. HP-Zn P+Ca in SBF is ~24 at% (Ca ~16 + P ~8.5), not 16. image_note adds that P-Fe runs in the opposite direction (P+Ca higher in GS), which the text does not mention.
- b5: label narrowed to what the markers show. image_support shown -> partial, because a resolved CO3 band (~1420-1480 cm-1) is clear only for HP-Mg-GS and the SBF traces are flat there.
- b9: label widened to the full SBF pH range seen in F4 (HP-Mg ~7.8-8.0 in the first 2 d; P-Fe dips to 6.9).
- b12: label narrowed, because HP-Zn IC (n) has uncovered gaps while EC (o) is confluent. image_support shown -> partial.
- b13: label corrected. At day 5 only HP-Mg-IC, HP-Zn-IC and HP-Mg-EC reach or exceed the negative control; the other Mg/Zn groups sit at 1.8-2.3 against 2.6. Day-1 note sharpened: P-Fe-IC (~0.45) equals the negative control (~0.47).
- s9, s13: requires_unseen filled in; source stays text.
- Note (not changed): the s10 -> s13 `supports` link is weak, since Mg degrading fast does not bear on Fe-ion toxicity. Kept as the paper's bridge from degradation to ion release.

## Panel checks (every cited crop opened, plus the F5 whole figure)

| node | panel_ids | ruling | correct_id | note |
|---|---|---|---|---|
| b1 | F1c | confirmed |  | bars at -1.76/-1.52 V for HP-Mg SBF/GS; icorr ~18.3 vs ~1.5 uA/cm2; HP-Zn 5.6 vs 1.7 |
| b2 | F1a, F1b | confirmed |  | Ecorr plateaus -0.70/-1.21/-1.52 (GS) and -0.77/-1.27/-1.76 V (SBF) |
| b3 | F2a, F2b | confirmed |  | HP-Mg SBF fully roughened at 7 d; HP-Zn SBF at 14 d has dense dark flakes (already in image_note) |
| b4 | F3a | confirmed |  | right panel; HP-Zn SBF value corrected |
| b5 | F3b | confirmed |  | PO4/CO3 labels and dashed markers; CO3 band weak except HP-Mg-GS |
| b6 | F3c | confirmed |  | HP-Mg bars far above Zn/Fe at 7-28 d in both media |
| b7 | F3c | confirmed |  | 28 d: 0.78/2.0, ~0.03/0.10, ~0.10/0.13 mm/y |
| b8 | F3c | confirmed |  | GS 0.13, 0.2, 0.45, 0.78; SBF 3.4, 2.5, 2.05, 2.0; large error bar on 28 d GS |
| b9 | F4a, F4b, F4c | confirmed |  | GS starts at 8.0-8.4 and crosses below SBF at ~11-13 d |
| b13 | F6b | confirmed |  | P-Fe-IC ~0.5/0.4 at d3/d5; label corrected |
| b14 | F6c | confirmed |  | Mg ~6.0, Zn ~0.25, Fe ~1.5 mM |
| b10 | (F5, no id offered) | confirmed |  | tier C whole figure: P-Fe IC (h, q) nearly empty, P-Fe EC d4 (r) sparse, Mg/Zn EC confluent |
| b12 | (F5, no id offered) | confirmed |  | k as dense as l; n has gaps vs o |

13 cited crops opened (F1a-c, F2a-b, F3a-c, F4a-c, F6b, F6c), plus the F5 whole figure. 0 overturned.

## Technique mismatches

- None. F1c (electrochemistry) matches ECHEM; F2a/F2b (micrograph) match SEM; F3b (FTIR) matches FTIR. The other crops have no cue class. read_from is correct: b5 restates the "PO"/"CO" annotations and is marked annotation.

## Mode changes

- None. No claim has two or more `causes` edges.

## Source changes

- s9: requires_unseen now lists the Table 2 medium composition and the cited film-breakdown mechanism.
- s13: requires_unseen now lists the linked-text attribution of the P-Fe viability loss to 1.52 mM Fe.

## MatMech tally (read after the graph was final; graph not edited)

supports 3 · contradicts 0 · not covered 2

| pair | cause | effect | verdict | graph nodes |
|---|---|---|---|---|
| M1 | disks cut and polished to 2000 grit | corrosion morphology; carbonate/phosphate layer | not_covered | |
| M2a | protective carbonate/phosphate layer (protein, bicarbonate, chloride) | lower corrosion rate, nobler Ecorr, lower icorr in GS | supports | s8, s8b, m2, s9, s11, b1, b7 |
| M2b | corrosion product layer | cytocompatibility | not_covered | |
| M3a | ion release in EC (Mg 6.03, Zn 0.23, Fe 1.52 mM) | Fe cytotoxic, Mg/Zn tolerated | supports | b14, s13, s12 |
| M3b | controlled degradation + cytocompatibility | HP-Mg and HP-Zn suitable for airway stents | supports | s10, s11, s12, s14, s15 |

Notes:
- The graph has no sample-preparation node. It also routes cytocompatibility through released ions rather than through the product layer.
- MatMech calls carbonate and phosphate "confirmed" on all products, but F3b resolves carbonate clearly only on HP-Mg-GS (b5 is now partial).
- MatMech says "P-Fe showed cytotoxicity at 48h"; the day-1 CCK-8 in F6b does not show this.
