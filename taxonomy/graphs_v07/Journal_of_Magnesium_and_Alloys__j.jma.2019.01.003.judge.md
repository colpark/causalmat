# Judge review: Journal_of_Magnesium_and_Alloys/j.jma.2019.01.003

**Verdict:** accept with minor fixes. 14 spine nodes, 42 total, one connected path with two FSP branches (dispersion -> COF/wear mechanism; DRX grain refinement -> hardness) meeting at f1, plus the stir-cast control branch. 1 audit (o13), fair. p1, p2 and m1 are basis argued because Table 3 is not in the packet.

## Changes
- d1 attrs.requires_unseen [] -> [mean grain size ~4 um (Table 3), 33% lower wear rate (linked text), route identity from captions]; source stays 'inferred'
- s5 attrs.source figure -> text; requires_unseen += route identity of XRD patterns a/b from caption (the 'FSP pattern' clause needs the caption)
- o13 label and image_note: crossover tightened to ~300-400 s (stir-cast curve first reaches FSP near 300 s, dips below at ~410 s)

## Panel checks (every cited crop opened; 26 crops + F9 whole figure, 34 node-panel citations; F8a/F8b also opened)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| o1 | F1a, F1b | confirmed | - | FESEM of loose FA: spherical cenospheres plus angular/irregular particles, ~1 to >25 um; in-image Mag 1.00 KX / 2.00 KX vs caption 2000x/5000x noted in image_note |
| o2 | F2a, F2b | confirmed | - | legend markers Mg, SiO2 on both patterns; Al2O3 triangle only in b at ~32.5 deg on a Mg peak; no MgO/Mg2Si/MgAl2O4 markers in a |
| o3 | F2a, F2b | confirmed | - | SiO2 peaks at ~26.5 and ~58 deg visibly taller in b on the same axis |
| o4 | F3a, F3b, F3c, F3d | confirmed | - | dark FA clusters beside sparsely reinforced cells in all four fields; etched cellular network |
| o6 | F4a, F4b, F4c, F4d | confirmed | - | eroded/porous particle interiors in a-b; round outlines mostly kept; polygonal chain of second-phase particles in d; partial is right |
| o7 | F5a, F5b, F5c, F5d | confirmed | - | fine dark particles evenly scattered, no particle-free area in any field |
| o8 | F6a, F6b, F6c, F6d | confirmed | - | particles ~2-15 um in a-b, some angular; one ~20 um particle in c; fine debris in c-d not resolved as nanometric; partial is right |
| o9 | F6c, F6d | confirmed | - | particle/matrix contact without visible rim at 2000x SE; thin layer unresolvable; partial is right |
| o10 | F7a, F7b | confirmed | - | b: equiaxed grains ~2-4 um (50 um bar); a: colour domains ~150-250 um across with extensive unindexed speckle; no boundary lines drawn |
| o12 | F9 | confirmed | - | whole figure (tier B): FSP ~240 um, stir casting ~350 um at ~1160 s; stir-cast curve jagged with drops at ~180 and ~410 s; legend names routes |
| o13 | F9 | confirmed | - | FSP above stir casting until ~300 s; curves cross between ~300 and ~400 s (label tightened from '330-350 s') |
| o14 | F10a | confirmed | - | annotated Groove and Crater; elongated crater with piled edges |
| o15 | F10b | confirmed | - | annotated Debris; fine debris over shallower grooves, no crater |
| o16 | F11a, F11b | confirmed | - | a: flat flakes ~30-40 um (20 um bar); b: mostly fine particles with loose agglomerates, one ~25 um flake top left |
| o17 | F10a, F10b | confirmed | - | parallel grooves along one direction in both panels |
| o11 | (none; F8 whole figure) | confirmed | - | no panel cited (figs F8, whole figure). Opened F8a and F8b anyway: they are the right panels (EBSD misorientation histograms); LAGB <15 deg ~0.25 in a vs ~0.35+0.06+0.05 in b; high-angle bar ~0.17 near 88 deg in a; one small bar beyond 93 deg in a. Citation stays dropped because the OCR cue is XRD, not the micrograph misfire that allows an override |

Overturned: 0.

## Technique mismatches
- o11 (EBSD) vs F8a/F8b cue class XRD: already dropped by staff; kept dropped. The crops are the right panels, but the override rule covers only the false micrograph cue. No other mismatch: SEM/OM/EBSD nodes on micrograph or SEM cues, XRD nodes on XRD cues, F9 has no cue.
- read_from: o2, o14, o15, o17 restate panel annotations and are 'annotation'; the rest read pixels or axes. No change.

## Source changes
- s5 figure -> text (the 'FSP pattern' clause needs the caption's a/b mapping).
- d1 stays inferred; requires_unseen now lists the Table 3 grain size, the text wear-rate gain and the caption route identity.

## Mode changes
- none. f1 is the only claim with two causes edges (p1, p2); 'joint' is right: the linked text adds COF to the hardness effect and no figure shows a choice.

## MatMech (read after the graph was final; graph not edited)

Tally: supports 5, contradicts 0, not covered 0.

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | Conventional stir casting -> inhomogeneous FA dispersion, coarse grains (145 um), interfacial reactions (MgO, Mg2Si, MgAl2O4) | supports | n4, s4, s6, s2, k4 |  |
| M2 | Friction stir processing -> homogeneous dispersion, fine equiaxed grains (4 um), particle disintegration, no interfacial reaction | supports | n5, s1, s2, m1, s3, s8 |  |
| M3 | homogeneous dispersion, fine grains, clean interfaces (FSP) -> higher microhardness and lower wear rate | supports | s2, k1, p1, s1, p2, m2, f1 | Orowan contribution of dispersion to hardness and the interface -> property link are not in the graph; hardness values (94 vs 62 HV) not in packet |
| M4 | inhomogeneous dispersion, coarse grains, interfacial reactions (stir cast) -> lower microhardness and higher wear rate | supports | s4, p4, f1, s2, p1 | graph carries it as the control branch (plowing from particle-free zones) and the comparative s2->p1; reaction-weakened bonding not covered |
| M5 | higher microhardness and lower COF -> superior sliding wear resistance | supports | p1, p2, f1, k2 | joint causes, as in the graph; COF 0.35 vs 0.48 not in packet |
