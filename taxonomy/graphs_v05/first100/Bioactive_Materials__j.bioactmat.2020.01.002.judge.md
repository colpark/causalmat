# Judge review: Investigation of Mg-Zn-Y-Nd alloy for potential application of biodegradable esophageal stent material

- paper_id: `Bioactive_Materials/j.bioactmat.2020.01.002`  ·  rank 32  ·  batch v05_first100
- vocab: v04 (frozen; no new types accepted, proposals in new_types.jsonl not used)
- **verdict: approved with changes**

## Spine

317L esophageal stents stay in the body and invite restenosis (n1) -> a degradable alkalinising alloy should disappear and hold back those cells (n2) -> Mg-Zn-Y-Nd against 317L on every axis (n3, n4) plus the cell panel method (n5) -> discs prepared (n6) and exposed to physiological fluid (n7) -> surface roughness (n8) and hardness (n9), wettability (n10), electrochemistry (n11), porous corrosion layer (n12), degradation rate (n13), medium pH (n14) -> cell attachment and viability (n15), explained by alkalinisation plus an unstable poorly wetted interface (n16) -> in-vitro service capability (n17) -> conclusion (n18). 17 spine nodes, one root, the surface branch and the degradation branch meeting at n16.

Evidence or stated basis on every spine STR/PRP/PRF/MEC claim: `n8` evidenced by p1, p2; `n9` evidenced by p3; `n10` evidenced by p4; `n11` evidenced by p5; `n12` evidenced by p6; `n13` evidenced by p9; `n14` evidenced by p7; `n15` evidenced by p10, p11, p12; `n16` basis = argued; `n17` basis = argued.

Types were re-checked against the v04 decision rules, every edge whose src is an OBS node with a figure carries an mm_op from the v04 list, and each mm_op names what a reader does to that figure.

## Changes

- p8: 'a full unit below the blank control' corrected to 'nearly two units below'. Read off F5a at day 20 the blank sits near 7.95 and the steel arm at 6.05. Label, image_note and the graph notes updated; the audit is stronger than the node claimed.

## Panel checks

Three OBS nodes carrying panel_ids were picked and their crops opened.

### `p8` — CONFIRMED

- panel_ids checked: `10.1016/j.bioactmat.2020.01.002#F5a`
- the pH panel carries all three arms: the alloy rising 7.4 -> 10.0 and plateauing after about day 22 (p7), the blank peaking near 8.45 around day 4-8 and drifting to about 7.55, and the steel falling to its 6.05 minimum at day 20-21 before recovering to 7.07. Only the size of the steel/blank gap needed correcting.

### `p5` — CONFIRMED

- panel_ids checked: `10.1016/j.bioactmat.2020.01.002#F3`
- F3 is offered as a whole-figure id and holds the two Tafel curves plus the table beneath them, which prints -1.49 V / 24.93 uA cm-2 / 8450 ohm cm2 and -0.25 V / 0.017 uA cm-2 / 75190 ohm cm2. The abscissa really carries no title, and the alloy's branches meet near log i = -4.3, i.e. about 50 uA cm-2, roughly twice the tabulated value, as the node says.

### `p11` — CONFIRMED

- panel_ids checked: `10.1016/j.bioactmat.2020.01.002#F6b`
- the bar chart gives about 88, 83 and 76% on the alloy at 4, 24 and 72 h against about 95.5, 97.5 and 96.5% on the steel, with significance markers at all three times

No panel_id anywhere in this graph is invented: every one appears in the packet's panel section (checked mechanically over all nodes, not only the three above).

## What the packet's panel section got wrong

F3 and F4 are tier B and offered only as whole-figure ids, which the graph uses correctly: n11 and p5 cite F3 (polarisation curves plus the embedded table), n12 and p6 cite F4 (the seven-day SEM series). The F3 whole-figure crop does contain the table, so reading the tabulated Ecorr/Icorr/Zre values from that id is legitimate. No invented panel ids. The packet's own figure set is complete for the opened figures; F7-F9 were not opened and enter through one text-backed OBS (p12) with fig_ref, per the r04 rule on unopened figures.

## Audits

2 audits (n20 the in-vitro flat-disc scope, p8 the unexplained acidification of the steel control). Both change the support of a spine claim. Three further figure findings that qualify rather than overturn - the corrosion-rate error bars swallowing the post-day-7 decline, the electrochemical current implying a faster rate than any immersion point, and the viable fraction never falling below 76% - are correctly kept inside the image_notes of p9 and p11 rather than spawning audit nodes.
