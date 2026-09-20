# Judge review: Self-healing polymer coatings of polyurea-urethane/epoxy blends with reversible and dynamic bonds

- paper_id: `Progress_in_Organic_Coatings/j.porgcoat.2020.105876`  ·  rank 31  ·  batch v05_first100
- vocab: v04 (frozen; no new types accepted, proposals in new_types.jsonl not used)
- **verdict: approved with changes**

## Spine

Coatings must repair themselves without losing hardness or adhesion (j1) -> disulfide bonds plus Diels-Alder crosslinks (j2) -> FTPU base, epoxy/BMI modification, ratio sweep (j3-j5) -> polymerisation then coating and cure (j6, j7) -> DA adducts (j8) and nanoscale epoxy domains (j9) -> mechanical and thermal properties and shape memory (j10-j12) -> the healing cycle (j21) produces the homogeneous state (j20), and the MEC node (j14) ties retro-DA, shape-memory closure and disulfide exchange to healing efficiency (j13) -> barrier performance after healing (j15) -> conclusion (j16). 18 spine nodes, one root. Making the healing stimulus its own PRC node is right under r04 ruling #36: the exposure produces an argued structural state (j20).

Evidence or stated basis on every spine STR/PRP/PRF/MEC claim: `j8` evidenced by m10; `j9` evidenced by m1, m3; `j10` evidenced by m4, m6, m7; `j11` evidenced by m5; `j12` evidenced by m9; `j20` evidenced by m11, m12, m13; `j14` evidenced by m9; `j13` evidenced by m8; `j15` evidenced by m14.

Types were re-checked against the v04 decision rules, every edge whose src is an OBS node with a figure carries an mm_op from the v04 list, and each mm_op names what a reader does to that figure.

## Changes

- m5: the FTPU loss peak read from F4b is at about -30 C, not -33 C; label and image_note corrected to drop the false precision. The node's finding that the text's -25 C is wrong is unaffected.

## Panel checks

Three OBS nodes carrying panel_ids were picked and their crops opened.

### `m5` — CONFIRMED

- panel_ids checked: `10.1016/j.porgcoat.2020.105876#F4b`
- the tan delta panel shows the FTPU peak just left of -25 C, the half-BMI blend on a broad 20-60 C plateau with its maximum near 45-50 C, a shoulder on the 7:3 trace near 60-70 C and a 5:5 peak near 80 C - all four readings as stated

### `m8` — CONFIRMED

- panel_ids checked: `10.1016/j.porgcoat.2020.105876#F5c`
- the FT5BE5 panel shows the healed (red) curve lying above the original (black) from about 20% strain to its end near 15.6 MPa at 50%, against 15.3 MPa at 65% for the original, so the sub-unity efficiency of that blend does come entirely from the lost elongation

### `m14` — CONFIRMED

- panel_ids checked: `10.1016/j.porgcoat.2020.105876#F6d`
- F6d is the healed-then-corroded panel (caption: healed coatings before (c) and after (d) corrosion; both (b) and (d) carry the same in-panel title 'Contaminated and corroded coatings'). In it the three blends are clean while the FTPU wood board still carries red staining and the epoxy board a red blotch, with matching blooms on their tinplates - the node's point that the improvement belongs to the blends alone

No panel_id anywhere in this graph is invented: every one appears in the packet's panel section (checked mechanically over all nodes, not only the three above).

## What the packet's panel section got wrong

F3 (AFM, 10 panels) and F7 (scratch SEM, 9 panels) are tier C with no panel ids offered, and the four nodes that read them (j9, j12, m1, m2, m9) correctly carry figs with panel_ids = [] rather than inventing ids. One point where the packet could mislead: the in-panel title of F6d reads 'Contaminated and corroded coatings', the same title as F6b, so the crop alone does not say it is the healed arm. The caption does - 'healed coatings before (c) and after (d) corrosion' - and the graph reads it correctly. No invented panel ids.

## Audits

3 audits (j18 the best efficiency belonging to the unblended control and no repeated healing, m2 the AFM panel without a z scale, m13 the undescribed transmittance panels). Each changes the support of a spine claim, and the two image audits keep the right distinction: m2 says the figure does not resolve the quoted height differences, m14's in-node finding says the figure shows something the text does not. The nodes reading the two tier-C figures (F3, F7) correctly carry figs with panel_ids = [], since no ids are offered.
