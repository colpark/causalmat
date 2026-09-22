# Judge review: Bioactive_Materials/j.bioactmat.2020.01.002

Mg-Zn-Y-Nd alloy vs 317L SS for biodegradable esophageal stents. Judge: senior investigator (v07 part B).

## Verdict

**Accept with minor fixes.** The spine reads as the paper's argument: 14 nodes, connected HYP -> DSC/conclusion, with two branches (degradation -> alkalisation -> acid-neutralising advantage; wettability -> fewer vital cells -> anti-restenosis). Hardness/roughness -> less pain is a side branch. Every spine STR/PRP has OBS evidence, and n15 and n16 are basis=argued. All nodes, rels, ops and modalities are v04-valid. mm_ops fit the acts. There are 4 audits (o9, o13, o14, o15), all fair and all bearing on spine claims.

## Changes

- o1 label: SS is "flat apart from scattered deep pits", not "flat within ~1 um". Its colour scale runs -2.2 to 3.0 um.
- o9 label: SS pH stays near the blank until day 9-10 and only then falls well below it. It reads ~7.05 at day 30. The image_note is extended.
- o11: label softened and image_support changed shown -> partial. Macrophages at 4 h (F9a) and L929 at 1 d (F7a) show comparable counts on both metals. SS at 3 d is confluent only for Eca109 and L929.
- o14: dropped the clause "only Eca109 and L929 stay sparse". The L929 panel is not cited on this node, and Eca109 at 3 d shows many punctate specks.
- n8: added requires_unseen (Mg dissolution stoichiometry, prior knowledge).

## Panel checks (every cited crop opened: 16 unique panels, 27 citations)

| node | panels | ruling | note |
|---|---|---|---|
| o1 | F1a | confirmed | 3D optical height maps; label tightened |
| o2 | F1b | confirmed | 57.08+/-4.65 vs 32.20+/-3.63 nm (the text says +/-4.05) |
| o3 | F2a | confirmed | 54.3 vs 198.7 HV |
| o4 | F2b | confirmed | 59.9 vs 28.4 deg, droplet insets |
| o5 | F3 | confirmed | Ecorr ~-1.5 vs ~-0.25 V; x axis unlabelled |
| o6 | F3 | confirmed | inset table values match |
| o7 | F4 | confirmed | attack is non-monotonic (10 d < 7 d); partial support kept |
| o8 | F5a | confirmed | Mg pH ~10 plateau from day 22; blank ~8.45 -> 7.5; SS min ~6.05 |
| o9 | F5a | confirmed | label corrected (divergence from day 9-10) |
| o10 | F5b | confirmed | Mg 0.13-0.38 mm/y (peak at day 7); SS <=0.07 |
| o11 | F6a, F7a, F8a, F9a | confirmed | right panels; claim overstated, softened, now partial |
| o12 | F6b, F7b, F8b, F9b | confirmed | Mg 74-88% < SS 87-98% at every time |
| o13 | F7b, F8b, F9b | confirmed | no star on L929 72 h, Het-1A 72 h, macrophage 4 h |
| o14 | F8a, F9a | confirmed | counts on Mg rise from 1 d to 3 d |
| o15 | F6a, F7a, F8a, F9a | confirmed | green only; a few yellow specks on F6a; no red EB cells |

Overturned: 0.

## Technique mismatches

None. The only cue on a cited crop is "micrograph" on F1a, which is compatible with OPTICAL:profilometry (o1). The other crops have no cue class, and F3 and F4 have no OCR. No cue overrides were needed. On read_from, o6 is correctly "annotation" (the F3 table). The printed value labels on o2, o3 and o4 are OCR tokens but not listed annotations, so "axis" is kept.

## Mode changes

None. Only n13 has two causes edges (n10, n14). "joint" is correct because no caption or figure weighs hardness against roughness.

## Source changes

n8: requires_unseen added. Its source stays prior_knowledge. All other source and requires_unseen values checked and left as they were.

## MatMech tally (read after the graph was final; graph not edited)

**supports 4 / contradicts 1 / not covered 3**

| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | polishing -> roughness 57 nm | not covered | n14 (no processing node) |
| M2 | Hank's immersion -> porous morphology | supports | n5, n6, o7 |
| M3 | roughness -> higher contact angle | not covered | n14, n11 are unlinked |
| M4 | porous morphology -> higher Icorr / corrosion rate | contradicts | n6, n7, o5, o6: porous attack is evidence of degradability; Icorr comes from unexposed discs |
| M5 | corrosion + alkaline products -> pH rise, anti-cancer | supports | n7, n8, n9, n15 (anti-cancer only argued) |
| M6 | low hardness -> less pain | supports | n10, n13 |
| M7 | higher contact angle -> cell inhibition | supports | n11, n12, n16 |
| M8 | porous structure -> resorption, no repeat procedure | not covered | n6 -> n7 is evidential; resorption absent |

MatMech record defects: M1-M3 quote +/-4.05 nm, but F1b prints +/-4.65. M8's "corrosion rate increases with time" conflicts with F5b, which peaks at day 7 and then falls. M5's "SS remains <=7.0" does not hold at day 30 (~7.05).
