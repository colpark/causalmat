# Judge review: New insights into single-grain mechanical behavior from temperature-dependent 3-D coherent X-ray diffraction

- paper_id: `Acta_Materialia/10.1016_j.actamat.2014.06.008`  ·  rank 25  ·  batch v05_first100
- vocab: v04 (frozen; no new types accepted, proposals in new_types.jsonl not used)
- **verdict: approved with changes**

## Spine

Intra-grain strain heterogeneity has never been mapped in 3-D (a1) -> map it by 3-D CXD with phase retrieval on one grain during thermal cycling (a2) -> choose Au on silica and the CXD method and the thermal sweep (a3, a4, a5) -> PVD then flame anneal (a6, a7) -> columnar grains and a characterised neighbourhood (a10, a13); thermal cycling loads the grain (a9) and stores defects (a14) -> the average lattice strain runs a shallow hysteresis loop (a15) and the heterogeneity is anisotropic and grows with temperature (a16) -> it is quasi-reversible (a17), explained by defect trapping at the misoriented boundaries (a18) -> the method returns both quantities through a full cycle (a19) -> conclusion (a20). 17 spine nodes, one root at a1, two branches (processing/structure and loading) meeting at a16, stage-ordered throughout. The DES/method node on the spine is licensed by the `realizes` definition for a headline measurement, and the notes say so explicitly.

Evidence or stated basis on every spine STR/PRP/PRF/MEC claim: `a10` evidenced by o1; `a13` evidenced by o15, o16; `a14` basis = argued; `a15` evidenced by o7, o8; `a16` evidenced by o5, o10, o12, o13; `a17` evidenced by o13; `a18` evidenced by o17; `a19` evidenced by o13.

Types were re-checked against the v04 decision rules, every edge whose src is an OBS node with a figure carries an mm_op from the v04 list, and each mm_op names what a reader does to that figure.

## Changes

- o1: label and image_note corrected - the F1b cross-section shows rounded grains with curved boundaries spanning the film thickness, not boundaries running straight from substrate to surface
- a10: label softened from 'boundaries normal to the substrate' to 'boundaries running from the substrate to the surface', which is what F1b shows

## Panel checks

Three OBS nodes carrying panel_ids were picked and their crops opened.

### `o1` — CONFIRMED

- panel_ids checked: `10.1016/j.actamat.2014.06.008#F1b`
- F1b is the cross-sectional SEM; the 0.372 um in-panel marker against the stated 475 nm film is real, as the node's image_note says. Only the 'straight boundaries' wording needed correction.

### `o10` — CONFIRMED

- panel_ids checked: `10.1016/j.actamat.2014.06.008#F4b`
- dqx rises from about 1.35e-3 at 35 C (red, heating) to 4.9e-3 at 265 C; the printed dq^Size = 6.61e-4 annotation that o12 reads is in the same panel, and the cooling branch returns to about 1.95e-3, as o11 states

### `o16` — CONFIRMED

- panel_ids checked: `10.1016/j.actamat.2014.06.008#F7c`
- the <110> projection diagram carries g1/g5, g4, g2 within about 10 deg of each other, with g6 and g3 further away on opposite sides, as the node states

No panel_id anywhere in this graph is invented: every one appears in the packet's panel section (checked mechanically over all nodes, not only the three above).

## What the packet's panel section got wrong

The packet's F2b and F7b crops are labelled 'letter q (OCR DISAGREES with detector b)'; both really are panel (b) and the graph is right to cite F7b. No panel_id in this graph is invented: every one appears in the packet's panel section. The graph's own notes already record the F3(f) axis-label conflict and the F1b thickness marker, and both survive inspection.

## Audits

3 audits (a22 method limitation, o11 non-recovering peak width, o18 stress conversion that does not reproduce the text's 95/250 MPa). All three change the support of a spine claim and are stated as arithmetic or figure readings, not as accusations. The o18 conversion checks out: 1.2 x 188.6 GPa x 0.0005 = 113 MPa and x 0.00167 = 378 MPa.
