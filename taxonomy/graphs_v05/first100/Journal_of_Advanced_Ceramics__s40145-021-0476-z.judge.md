# Judge review: Enhanced electromagnetic wave absorption property of binary ZnO/NiCo2O4 composites

- paper_id: `Journal_of_Advanced_Ceramics/s40145-021-0476-z`  ·  rank 27  ·  batch v05_first100
- vocab: v04 (frozen; no new types accepted, proposals in new_types.jsonl not used)
- **verdict: approved with changes**

## Spine

Absorbers need loss and impedance matching together (c1) -> a binary hybrid adds heterointerfaces (c2) -> ZnO base, NiCo2O4 modification, alkalinity sweep, coaxial method (c3-c5, c8) -> hydrothermal then calcination (c6, c7) -> two phases, heterointerfaces, morphology, porosity (c9-c12) -> permittivity (c13), loss tangent and attenuation (c15), explained by interfacial polarisation (c16), with the magnetic control branch ending at c14 -> impedance matching (c18) -> -33.49 dB absorption (c19) -> conclusion (c20). 18 spine nodes, one root, two branches plus the magnetic control branch, which is exactly the allowance in the protocol.

Evidence or stated basis on every spine STR/PRP/PRF/MEC claim: `c9` evidenced by r1, r4; `c10` evidenced by r3, r5; `c11` evidenced by r2; `c12` evidenced by r6; `c13` evidenced by r7; `c14` evidenced by r9; `c15` evidenced by r8, r14; `c16` evidenced by r12; `c18` evidenced by r13; `c19` evidenced by r15, r16.

Types were re-checked against the v04 decision rules, every edge whose src is an OBS node with a figure carries an mm_op from the v04 list, and each mm_op names what a reader does to that figure.

## Changes

- r13: OBS/response/regime_map -> OBS/response/trend with attrs.dimension = 2D. v04's written sibling rule is 'a single response's contours over two variables is trend (dimension=2D); boundaries between qualitatively different states is regime_map'. The F7 panels are continuous colour contours of one quantity (the matching parameter) over frequency and thickness; the matched/unmatched split comes from the externally imposed |delta| < 0.4 criterion, not from a state boundary in the material. The mm_op read_characteristic_point is unchanged - r04 ruling #6 already puts 'locating a sample relative to a boundary' there - and c18 reads the same thing either way.

## Panel checks

Three OBS nodes carrying panel_ids were picked and their crops opened.

### `r5` — CONFIRMED

- panel_ids checked: `10.1007/s40145-021-0476-z#F2d`
- the EDS strip shows Co nearly as even as Zn and only Ni visibly clustered, so the node is right that the text's 'both Ni and Co discontinuous' is not what the maps show

### `r8` — CONFIRMED

- panel_ids checked: `10.1007/s40145-021-0476-z#F5c`
- the -10 trace (blue) is highest at every frequency and reaches about 0.10 at 18 GHz while -7 (red) reaches about 0.07, with -5 (black) touching or crossing it around 10-13 GHz; the record's claim that the best absorber has the highest loss tangent does not survive this panel

### `r15` — CONFIRMED

- panel_ids checked: `10.1007/s40145-021-0476-z#F8c`
- panel (c) is the -7 map and its colour bar bottoms at -33.50 dB, in the top-right corner near 18 GHz and 5 mm. This also settles the packet/text conflict in the node's favour: the paper's running text cites 8(d) for this minimum, i.e. its panel letters are one row off, and the graph follows the image. F7a was opened as a spot check and its colour bar reads 0.55, as r13 states.

No panel_id anywhere in this graph is invented: every one appears in the packet's panel section (checked mechanically over all nodes, not only the three above).

## What the packet's panel section got wrong

The packet's F3a crop is labelled 'letter l (OCR DISAGREES with detector a)' and its F2b cue line reads 'scale bar 0.26 nm', which is the marked d-spacing and not the 10 nm bar; the graph's r3 image_note already says so. More important is a defect in the paper rather than the packet: the running text cites Fig. 8(b), (d) and (f) for the three reflection-loss minima while the colour bars put them in (a), (c) and (e). F8c was opened and reads -33.50 dB, so the graph's image-led ids are right and the paper's letters are one row off. No invented panel ids.

## Audits

3 audits (c22 the -10 dB band being about 1 GHz wide at the edge of the measurement, r8 and r10 contradicting the paper's loss-mechanism reading). All three genuinely change support for c19 and c14, and each is phrased as a panel reading with the panel named. The r10 audit is the strongest and is correctly built from two panels on a shared abscissa via compare_coplotted_quantities.
