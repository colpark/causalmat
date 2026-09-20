# Judge review: Tensile deformation behavior and mechanical properties of a bulk cast Al0.9CoFeNi2 eutectic high-entropy alloy

- paper_id: `Journal_of_Materials_Science_&_Technology/j.jmst.2020.05.053`  ·  rank 29  ·  batch v05_first100
- vocab: v04 (frozen; no new types accepted, proposals in new_types.jsonl not used)
- **verdict: approved with changes**

## Spine

Need strength with ductility from a castable bulk route (f1), and the phase-by-phase substructure evolution is unmeasured in a Cr-free eutectic HEA (f2) -> staged yielding hypothesis (f3) -> alloy choice and the interrupted-test method (f4, f5) -> induction casting (f6) and tension (f7) -> dual-phase L12+B2 and the lamellar eutectic (f8, f9) -> the three staged substructure claims (f12, f13, f14) -> yield/UTS/elongation (f15), three-stage hardening (f16) and mixed fracture (f17), explained by f18 and f19 -> conclusion (f20). 18 spine nodes, one root. Putting DES/method on the spine is justified: the staged substructure record is the paper's contribution and f5 realizes f13.

Evidence or stated basis on every spine STR/PRP/PRF/MEC claim: `f8` evidenced by g1, g2; `f9` evidenced by g3, g4; `f12` evidenced by g8, g9; `f13` evidenced by g10; `f14` evidenced by g12, g13; `f15` evidenced by g5; `f16` evidenced by g6; `f17` evidenced by g7; `f18` basis = argued; `f19` basis = argued.

Types were re-checked against the v04 decision rules, every edge whose src is an OBS node with a figure carries an mm_op from the v04 list, and each mm_op names what a reader does to that figure.

## Changes

- g14: removed attrs.aspect = 'outlier'. aspect=outlier is an mm_op attribute of cross_check_consistency (r04 ruling #7) and belongs on the edge, and in any case this node does not set a deviating point aside - it reports that a comparison cannot be made because the two panels are at different magnifications.

## Panel checks

Three OBS nodes carrying panel_ids were picked and their crops opened.

### `g6` — CONFIRMED

- panel_ids checked: `10.1016/j.jmst.2020.05.053#F2b`
- the hardening-rate panel starts at about 85 GPa, falls to about 14 GPa at the stage I/II dashed line near true strain 0.009, declines to about 5 GPa by 0.057 and drops to about -10 GPa; the inset true-stress curve ends near 1080 MPa at 0.06. Every number in the node is on the panel. Note the packet labels this crop 'letter a (OCR DISAGREES with detector b)': the crop is (b), and the graph is right to use F2b.

### `g11` — CONFIRMED

- panel_ids checked: `10.1016/j.jmst.2020.05.053#F4c`
- the lamella interior is filled with curved, closed cell walls, not straight coplanar arrays, so the wavy-slip reading that cuts against the paper's low-SFE argument is what the panel shows. The in-panel 'Dislocations pileup' label that g10 reports is on this crop.

### `g13` — CONFIRMED

- panel_ids checked: `10.1016/j.jmst.2020.05.053#F5b`
- F5b is the post-fracture B2 panel (0.2 um bar). It shows a dominant family of long straight parallel dislocations with a second, darker set inclined across it, so image_support = partial and the node's disagreement with the text's 'single parallel set' is fair. The packet labels this crop 'letter q'; it is (b).

No panel_id anywhere in this graph is invented: every one appears in the packet's panel section (checked mechanically over all nodes, not only the three above).

## What the packet's panel section got wrong

The packet's F2b crop is labelled 'letter a (OCR DISAGREES with detector b)' and the F5b crop 'letter q'; both are really (b), and both were opened and confirmed as such, so the graph's ids are right and the packet's letters are the thing at fault. No invented panel ids.

## Audits

3 audits (f22 method limitation, g11 the wavy-slip signature contradicting the paper's planar-slip reading, g14 the magnification mismatch). g11 is the valuable one and is stated correctly as 'the panel shows X, which cuts against the paper's reading', not as an error. g14 correctly distinguishes 'the figure does not resolve it' from 'the figure contradicts the text'.
