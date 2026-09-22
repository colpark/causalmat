# Judge review: Progress_in_Organic_Coatings/j.porgcoat.2020.105876

**Verdict:** accept with minor fixes. 18 spine nodes, 56 total, one connected path HYP -> DSC/conclusion with two branches (A: DA-crosslinked domains -> strength/hardness; B: 130 C retro-DA / 60 C DA -> healing -> healed-coating protection) plus the low-BMI control branch. Every spine STR/PRP/PRF has an evidences edge; MEC p10 is argued. Audits o5, o14, p28 (3), fair.

## Changes
- p3 attrs.source figure -> text; requires_unseen lists the healing rationale (Scheme 1 linked text, refs 42,43)
- p4 attrs.source figure -> text; requires_unseen lists DA crosslinking and domain role (Scheme 1 shows structures only)
- p7 label: 'Diels-Alder cure' -> 'cure' (reaction not named in Scheme 1; DA carried by p4)
- p18 attrs.source figure -> text; requires_unseen lists exposure media/time and the hot-press healing step

## Panel checks (every cited crop opened: F1, F2a-d, F4a-d, F5a-d, F6b-d, F8a-d = 20 crops, 36 node-panel citations; plus whole F3, F7 and crops F6a, F8e, F8f for uncited nodes)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| p3 | F1 | confirmed | - | Scheme 1 shows FTPU with AFD disulfide and FA furan ends |
| p4 | F1 | confirmed | - | furan-pendant epoxy oligomer and BMI shown; DA and domain role are text (source fixed) |
| p6 | F1 | confirmed | - | PCDL+IPDI 70 C 3 h DMF; AFD+FA 70 C 4 h DMF as labelled |
| p7 | F1 | confirmed | - | FTPU + epoxy oligomer + BMI, 60 C 24 h -> FTxBEy; 'Diels-Alder' not written in the scheme, dropped from label |
| p20 | F1 | confirmed | - | DGEBA + FA 100 C 6 h DMF -> furan-pendant epoxy oligomer |
| o1 | F2a, F2b, F2c, F2d | confirmed | - | a smooth lobed fracture surface; b,c rough granular; d finer/smoother than c |
| p11 | F4c | confirmed | - | FTPU ~7.8, FT7BE3 ~14.3, FT5BE5 ~15.3 MPa |
| p22 | F4c | confirmed | - | ~232, ~112, ~65 % elongation |
| p27 | F4a, F4c | confirmed | - | orange lowest E' at 25 C (~1.5e2 MPa) and lowest ultimate stress ~6.4 MPa |
| o8 | F4c | confirmed | - | ranking as stated |
| o9 | F4c | confirmed | - | values as stated (FT5B0.5E5 ~130%) |
| o5 | F4a | confirmed | - | at 25 C black > blue > red > orange; all blends below FTPU |
| o6 | F4b | confirmed | - | red shoulder ~60-75 C, blue peak ~83 C, black low peak ~-30 C |
| o7 | F4b | confirmed | - | orange peaks at ~25 and ~47 C |
| p23 | F4b | confirmed | - | upper transition 60-85 C; FT7BE3 a shoulder, partial is right |
| p12 | F4d | confirmed | - | radar: blends near epoxy on adhesion and pencil hardness, all at the flexibility vertex |
| o10 | F4d | confirmed | - | red FT7BE3 trace hidden under blue; FT5B0.5E5 slightly inside |
| o11 | F5a, F5b, F5c, F5d | confirmed | - | origin vs 130 C healed curves match the values in image_note |
| o12 | F6b | confirmed | - | red stain on FTPU/FT7BE3/FT5BE5 wood scratches; dark corrosion on FT7BE3, FTPU, epoxy tinplates |
| o13 | F6c, F6d | confirmed | - | healed FT5BE5 and FT5B0.5E5 panels clean after exposure |
| o14 | F6d | confirmed | - | FTPU and epoxy wood still red-streaked; FT7BE3 tinplate dark patches |
| p18 | F6b, F6c, F6d | confirmed | - | partial is right (FT7BE3 tinplate, FTPU, epoxy not protected) |
| o17 | F8a | confirmed | - | dotted markers at 1146 and 696 cm-1; extra dips in red traces (2),(5) near 696; 1146 barely resolved; partial is right |
| o18 | F8b | confirmed | - | AFM phase uniform fine texture with scan striping, a few bright spots |
| o19 | F8c | confirmed | - | smooth featureless SEM surface (crop also contains panel d on the right) |
| o20 | F8d | confirmed | - | smooth surface, a few streaks, no granular domains |
| o2 | - (tier C / dropped) | confirmed | - | F3 tier C, whole figure opened: bright domains sparse in g,h, dense in i and its inset, fine texture in f |
| o3 | - (tier C / dropped) | confirmed | - | F3h whole-figure read: bright domains ~20-80 nm against the 200 nm bar |
| o4 | - (tier C / dropped) | confirmed | - | F3e low-contrast protrusions; F3j dark isolated domains in bright matrix |
| o15 | - (tier C / dropped) | confirmed | - | F7 tier C, whole figure: Rf=90/91/24 %, Rr=99 % written in a-c; read_from annotation correct |
| o16 | - (tier C / dropped) | confirmed | - | F7 rows: wide scratches (a-c), thin lines (d-f), near-invisible (g-i) with faint traces in g,i |
| o21 | - (tier C / dropped) | confirmed | - | F8f crop opened: 130 C(1) ~50 % at 800, cooled ~40 %, heating 25/90 C ~6 %; F8e ~10-14.5 %. Citation stays dropped (FTIR cue vs UVVIS technique) |

Overturned: 0.

## Technique mismatches

- o21 (F8f): cue FTIR vs technique UVVIS. The axis is mislabelled 'Wavenumber (cm-1)' on a 400-800 visible-wavelength transmittance plot; the crop is the right panel but the cue is not the known 'micrograph' misfire, so the staff drop of the citation stands (figs F8, panel_ids []).
- All other cited panels agree: F4c, F5a-d mechanical cue vs MECH:tensile; F6c, F6d micrograph cue vs OPTICAL:photograph (compatible); F8a FTIR vs FTIR; F8b micrograph vs AFM; F2, F4a,b,d, F6b, F8c,d have no cue. No cue_overrides needed.
- read_from: o12 restates 'Contaminated and corroded coatings' and is 'annotation' (correct); o15 reads Rf/Rr written in F7 and is 'annotation' (correct); o13 does not restate the F6d string and stays 'pixels'; axis-read nodes (o5-o11, o17, o21) do not restate listed strings.

## Mode changes

None. Only p11 has two causes edges (p8, p9); mode 'joint' is right, no caption or figure shows a choice between them.

## Source changes

- p3, p4: figure -> text (healing rationale, DA crosslinking and domain role are linked text; Scheme 1 shows only structures and conditions).
- p18: figure -> text (exposure media/time and hot-press healing come from F6 linked text).
- p7 label trimmed so the figure-sourced node claims only what Scheme 1 shows.

## MatMech (read after the graph was final; graph not edited)

Supports 4 · contradicts 0 · not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | blend FTPU + epoxy oligomer + BMI, cure 60 C 24 h -> DA-induced nanoscale phase-separated epoxy domains, disulfide bonds, interfacial bonding | supports | p7, p8, p9, p26 |  |
| M2 | phase-separated domains + interfacial bonding -> higher tensile strength, modulus, pencil hardness, storage modulus; Tg shift | supports | p8, p9, p10, p11, p12, p23 | strength, hardness, Tg covered; 'storage modulus increased' conflicts with o5 (all blends below FTPU at 25 C), which qualifies p10; tensile modulus not on graph |
| M3 | phase-separated domains + disulfide bonds -> shape memory Rf 91/Rr 99, healing efficiency ~80 %, anticorrosion | supports | p24, p16, p17, p18 | graph routes healing through retro-DA domain dissolution (p15) and shape-memory closure (p24) into p16; domains-as-netpoints link not drawn |
| M4 | blending and curing process -> healing efficiency ~80 % and anticontamination/anticorrosion | supports | p7, p13, p16, p17, p18 | 3.5 % NaCl and 5-7 days not in packet |
