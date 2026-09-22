# Judge review: Advanced_Composites_and_Hybrid_Materials/s42114-021-00366-2

**Verdict:** accept with minor fixes. Crops checked: 20 (every cited panel, plus uncited F4d). Overturned: 0. Technique mismatches: 0. Mode changes: 0. MatMech: 5 supports / 0 contradicts / 0 not covered.

## Checklist

- The spine (18 nodes) reads as the paper's argument: need -> thiol/Ag hybrid-filler hypothesis -> PAEN + BST@Ag design, Ag sweep -> grafting, Ag reduction, casting -> bonding, Ag coverage, interface, dispersion -> permittivity, loss (MEC s15), strength -> service stability -> conclusion. It is connected and stage-ordered.
- dielectric (s13, s14/s15 meeting in s18) and mechanical (s17); within limit if the two dielectric properties are read as one branch that meets in s18.
- Every spine STR/PRP/PRF claim has an evidences edge. s15 is basis=argued.
- Audits: o6 (Ag not resolved in SEM), o8 (bare-BST contrast), o16 (F6b loss upturn contradicts '<0.026'). That is 3, and all are fair against the images.
- mm_ops name the reader's act on every figure edge. Node total is 45, above the 25-40 aim, but every OBS node is used.

## Changes

- s9: requires_unseen now lists the band assignments (text, ref 38), the unshown covalent attachment and the MPTMS decomposition range (ref 42); source stays 'inferred'
- o6: source figure -> text; requires_unseen adds 'panel F3e is BST@Ag5%' (caption only; crop carries only the letter)
- k5: requires_unseen adds the prior-knowledge fact (BST is a high-permittivity ferroelectric)
- o9: image_note records that F4b (and uncited F4d) show almost no discernible particles

## Panel checks

| node | panel | ruling | note |
|---|---|---|---|
| s4 | F1 | confirmed | Scheme 1: BST -> OH -> SH (MPTMS formula) -> Ag-dotted sphere; shows the hybrid-filler design |
| s5 | F7a | confirmed | legend/axis labels Pure PAEN, BST@Ag1/3/5% give the four levels |
| s6 | F1 | confirmed | scheme steps (1) and (2) drawn; H2O2 and conditions only in caption (source text kept) |
| s10 | F3e | confirmed | rough, coated, clustered particles; discrete Ag not resolved, so partial is right |
| s10 | F3f | confirmed | powders white (BST-SH) to brown (5%): colour proxy for Ag loading |
| s13 | F6a | confirmed | 5%>3%>1%>>PAEN; 6.05 vs 3.35 at 100 Hz = 1.8x |
| s14 | F6b | confirmed | loss ~0.014-0.04 over most of the range, but 0.038 at 100 Hz and BST@Ag1% 0.065 at 1 MHz; partial is right |
| s17 | F7a | confirmed | bars 79.3/78.3/74.4/73.5 MPa, error bars overlap |
| s18 | F6a | confirmed | permittivity falls ~10% over 100 Hz-1 MHz |
| s18 | F6c | confirmed | composite permittivity flat to a knee ~130-135 C, PAEN ~155 C |
| s18 | F6d | confirmed | composite loss flat to ~130-135 C, then peaks ~165-172 C |
| x3 | F5a | confirmed | Tg labels 176/146/149/157 C read directly |
| x4 | F5b | confirmed | all curves ~98-100% to ~500 C, sharp drop ~540 C |
| x5 | F7b | confirmed | bars 6.9/5.8/4.5/4.4% |
| o1 | F2a | confirmed | FTIR: 2930, 2864, 1122 cm-1 labelled only on BST-SH trace |
| o3 | F2b | confirmed | BST-OH cloudy in lower layer, BST-SH cloudy in upper layer |
| o5 | F3a | confirmed | bare BST: smooth round ~70 nm particles (500 nm bar), bright loose clusters |
| o5 | F3b | confirmed | BST-SH: irregular, rougher, larger particles |
| o5 | F3e | confirmed | BST@Ag5%: rough, coated, clustered |
| o6 | F3e | confirmed | no discrete Ag particles resolvable at 500 nm bar scale |
| o7 | F3f | confirmed | powders darken from white to brown |
| o7 | F4f | confirmed | films darken from off-white to dark brown |
| o8 | F4a | confirmed | loose bright particles on fracture surface, local small clusters |
| o9 | F4b | confirmed | right panel (BST-SH/PAEN), but particles barely discernible: supports 'no agglomerates' only; partial kept |
| o9 | F4c | confirmed | few faint embedded particles, no clusters |
| o9 | F4e | confirmed | many protruding particles, fairly even, a few small clusters |
| o10 | F4c | confirmed | particle outlines blurred under matrix, no interfacial gaps visible |
| o11 | F5a | confirmed | DSC steps with Tg labels |
| o12a | F5b | confirmed | composites lose ~1% at ~190-250 C; PAEN flat to ~480 C |
| o12b | F5b | confirmed | plateau to ~500 C, drop near 540 C; residue 60-64% vs ~37% |
| o13 | F6a | confirmed | ranking holds at all frequencies |
| o14 | F6a | confirmed | declines 8-12% from 100 Hz to 1 MHz |
| o15 | F6b | confirmed | 100 Hz: 0.024 < 0.032 < 0.038 ~ 0.038; curves converge ~0.014-0.018 above 10 kHz |
| o16 | F6b | confirmed | BST@Ag1% upturn above 100 kHz to ~0.065 |
| o17 | F6c, F6d | confirmed | knee ~130-135 C for composites, ~155 C for PAEN |
| o20 | F7a | confirmed | bar values legible |
| o21 | F7b | confirmed | bar values legible |

## Technique mismatches

None. The F3 crops carry the 'micrograph' cue, and the SEM nodes citing them are compatible. F2a carries the FTIR cue, which matches o1. No other cited crop has a cue class. No cue overrides were needed.

read_from: o1, o11, o20, o21 = annotation (Tg/bar/band labels and legends); o3, o5-o10 = pixels (the only annotation strings on those panels are sample labels, and the observations read positions, colours and morphology); o12a, o12b, o13-o17 = axis. No change.

## Source changes

- o6: figure -> text; unseen: F3e = BST@Ag5% (caption)
- s9: inferred -> inferred; unseen: band assignments; covalent attachment; MPTMS decomposition range
- k5: prior_knowledge -> prior_knowledge; unseen: BST high-permittivity ferroelectric

## Mode changes

None. Two claims have two causes edges and both are correctly joint:
- s17 (s11, s12): text attributes strength retention to compatibility and homogeneity together; no figure or caption shows a choice
- x3 (s9, s10): plasticising MPTMS and rigid Ag act together in every composite

## MatMech tally (recorded after the graph was final; graph not edited)

supports 5, contradicts 0, not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | MPTMS grafting + in situ Ag reduction -> Ag-decorated core-shell particles; better interfacial compatibility and dispersion in PAEN | supports | s6, s7, s9, s10, s11, s12, o1, o5, o9, o10 | graph marks Ag decoration as unresolved in SEM (o6); M1's 'confirming core-shell' is stronger than the images |
| M2 | core-shell BST@Ag, homogeneous dispersion -> higher permittivity, low loss (<0.026), stability below 140 C | supports | s10, s13, s15, s14, s18, o13, o15, o17 | cause->effect supported; the '<0.026' number is contradicted by F6b (o16 qualifies s14 and s18) |
| M3 | core-shell BST@Ag, homogeneous dispersion -> tensile strength >73 MPa retained | supports | s11, s12, s17, o20 |  |
| M4 | core-shell BST@Ag, homogeneous dispersion -> Tg lowered to 146-157 C; T5% >520 C kept | supports | s9, s10, x3, s8, x4, o11, o12b |  |
| M5 | MPTMS grafting, Ag reduction, casting -> high-temperature dielectric with stability <140 C and >73 MPa | supports | s6, s7, s8, s18, s17, s19 |  |
