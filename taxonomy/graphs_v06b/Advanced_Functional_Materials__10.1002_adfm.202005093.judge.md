# Judge review: Advanced_Functional_Materials__10.1002_adfm.202005093

**Judge:** senior investigator  
**Verdict:** accept with edits

## Round-4 checklist

- **spine_nodes**: 16
- **connected**: True
- **spine_evidence**: a7 (o1,o2), a8 (o3,o4,o5,o6,o8), a9 (o7), a10 (o9), a11 (o13), a12 (o12), a13 (o14,o17), a14 (o20-o23); a15 basis attributed
- **audits**: a30, a31, a32, o23 (qualifies a15): 4, fair and each bears on a spine claim
- **modes**: a10 joint (thickness + partial oxidation, text), a14 joint (synergy, F5 groups 4-6): correct
- **note**: packet F4/F5 are paper Figs 5/6; paper Fig. 4 absent

## Changes

- F3h restored on o16 and o17; F5d on o20; F5f on o21; F5g on o22; F5e on o24 (staff had dropped all six for false micrograph cues)
- technique normalised to controlled FAMILY:mode: o4 TEM:STEM + EDS:mapping, o5 TEM:HAADF, o9 UVVIS:Tauc, o14/o19 THERMAL:IRcamera, o16/o17 THERMAL, o20/o21 ASSAY:tumour, o22 ASSAY:survival, o23 OPTICAL, o24/o25 ASSAY, o26 OTHER (photoacoustic)
- a30 and a31 requires_unseen list the text-only facts they use (3.979 A spacing; 12:5 ratio)

## Panel checks (every cited crop opened)

| node | panel ids | ruling | correct id | note |
|---|---|---|---|---|
| o1 | F2a | confirmed |  | thin semi-transparent square sheets ~100-200 nm against the 200 nm bar |
| o2 | F2j | confirmed |  | height profile with 14 nm label; flakes ~100-200 nm |
| o3 | F2a, F2c | confirmed |  | bare smooth sheets in (a); sheets densely dotted with dark particles in (c) |
| o4 | F2e | confirmed |  | HAADF bright particles; Bi and O maps both cover the sheet, particles only faintly visible in Bi map: partial fair |
| o5 | F2h | confirmed |  | lattice fringes with 0.227 nm label |
| o6 | F2k | confirmed |  | bismuthene trace indexed in red to Bi (PDF#05-0519) with a (321) oxide peak near 33 deg |
| o7 | F2m | confirmed |  | bismuthene: Bi 4f7/2 (Bi) grown vs oxide sample, Bi2O3 doublet still larger |
| o8 | F2l | confirmed |  | bismuthene shows only ~69 and ~95 cm-1 modes (red dashed lines); oxide bands absent |
| o9 | F2n | confirmed |  | red tangent intercept at 0.69 eV; data curve bends away below ~1.1 eV |
| o10 | F2o | confirmed |  | 1665 and 1542 cm-1 dips strong in BNs-BSA and BSA; bismuthene trace nearly flat there |
| o11 | F3a | confirmed |  | DPBF band ~420-450 nm, 0.79 -> 0.54 over 30 min |
| o12 | F3b | confirmed |  | 421 nm relative absorbance 0.73 (bismuthene) vs 0.93 (water) at 30 min |
| o13 | F3c | confirmed |  | linear A/L vs concentration, alpha = 6.4, R2 = 0.9999 |
| o14 | F3e, F3g | confirmed |  | IR spots brighten with concentration (e) and with power density (g); water stays blue |
| o16 | F3h | confirmed |  | heating to ~57.5 C at ~6 min, cooling to ~30 C by ~15 min; restored (cue override) |
| o17 | F3h | confirmed |  | -ln(theta) vs time line with tau_s = 133.4, eta = 19.4%; restored (cue override) |
| o19 | F5c | confirmed |  | BNs-BSA ~49 C at 5 min vs PBS ~41 C |
| o20 | F5d | confirmed |  | BNs-BSA + Lasers: all curves at 0 after day 2; +808 nm: most curves regrow after ~day 14; restored (cue override) |
| o21 | F5f | confirmed |  | day-22 ranking BNs-BSA ~2350 > PBS ~2100 > Lasers ~1750 > +660 ~1470 > +808 ~370 > combination 0; restored (cue override) |
| o22 | F5g | confirmed |  | combination 100% to ~day 54, +808 nm lost by ~day 42, others by ~day 28; axis reads morbidity-free survival; restored (cue override) |
| o23 | F5i | confirmed |  | H&E cellularity drops in laser groups; TUNEL/Ki-67 show no clear stain contrast |
| o24 | F5e | confirmed |  | all groups 18-20.5 g over 14 days; restored (cue override) |
| o25 | F4a | confirmed |  | PBS vs BNs-BSA bars overlap within error except WBC (~50 vs ~35) |
| o26 | F4f | confirmed |  | data labels 0.26, 0.13, 0.32, 0.94, 0.60, 0.31 |
| o27 | F4h | confirmed |  | CT contrast ~70 -> 92 -> 117 -> 125 HU at 0-6 h |

Distinct crops opened: 25; node-panel rulings: 27; overturned: 0.

## Technique mismatches

- {"node": "o16", "panel": "10.1002/adfm.202005093#F3h", "cue": "micrograph", "ruling": "false cue; citation restored"}
- {"node": "o17", "panel": "10.1002/adfm.202005093#F3h", "cue": "micrograph", "ruling": "false cue; citation restored"}
- {"node": "o20", "panel": "10.1002/adfm.202005093#F5d", "cue": "micrograph", "ruling": "false cue; citation restored"}
- {"node": "o21", "panel": "10.1002/adfm.202005093#F5f", "cue": "micrograph", "ruling": "false cue; citation restored"}
- {"node": "o22", "panel": "10.1002/adfm.202005093#F5g", "cue": "micrograph", "ruling": "false cue; citation restored"}
- {"node": "o24", "panel": "10.1002/adfm.202005093#F5e", "cue": "micrograph", "ruling": "false cue; citation restored"}

## Cue overrides

- {"node": "o16", "panel": "10.1002/adfm.202005093#F3h", "cue": "micrograph", "why": "temperature-time heating/cooling curve, the panel this node reads; the micrograph cue is the scale-bar detector firing on a plot. Staff had dropped it"}
- {"node": "o17", "panel": "10.1002/adfm.202005093#F3h", "cue": "micrograph", "why": "same panel; tau_s and eta printed on it; the micrograph cue is the scale-bar detector firing on a plot. Staff had dropped it"}
- {"node": "o20", "panel": "10.1002/adfm.202005093#F5d", "cue": "micrograph", "why": "individual tumour-growth curves, the panel this node reads; the micrograph cue is the scale-bar detector firing on a plot. Staff had dropped it"}
- {"node": "o21", "panel": "10.1002/adfm.202005093#F5f", "cue": "micrograph", "why": "mean tumour-volume curves, the panel this node reads; the micrograph cue is the scale-bar detector firing on a plot. Staff had dropped it"}
- {"node": "o22", "panel": "10.1002/adfm.202005093#F5g", "cue": "micrograph", "why": "survival step curves, the panel this node reads; the micrograph cue is the scale-bar detector firing on a plot. Staff had dropped it"}
- {"node": "o24", "panel": "10.1002/adfm.202005093#F5e", "cue": "micrograph", "why": "body-weight curves, the panel this node reads; the micrograph cue is the scale-bar detector firing on a plot. Staff had dropped it"}

## Source / requires_unseen changes

- {"node": "a30", "from": "inferred, requires_unseen []", "to": "inferred", "requires_unseen": ["3.979 A interlayer distance from VASP (linked text)"]}
- {"node": "a31", "from": "inferred, requires_unseen []", "to": "inferred", "requires_unseen": ["12:5 oxide:metal area ratio stated in linked text"]}

## Mode changes

- none

## MatMech comparison (read after the graph was final; graph not edited)

Tally: supports 5, contradicts 0, not covered 0.

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | water freeze-thaw + NaBH4 reduction | few-layer 2D nanosheets ~200 nm, ~14 nm | supports | a4, a5, a6, a7, a23, a30 | graph adds audit a30: 14 nm is ~35 layers, so 'few-layer' is overstated |
| M2 | few-layer ultrathin nanosheets | strong NIR absorbance; band gap ~0.69 eV | supports | a7, a9, a10, a8, a11 | graph routes the band gap through thinness + partial oxidation (a7, a9 -> a10) and NIR absorbance through the Bi nanoflakes (a8 -> a11), not through thinness alone |
| M3 | photothermal conversion (19.4%) | photothermal tumour ablation | supports | a13, a19, a14 | 27.3 C rise at 200 ug/mL is in o14/F3d; PTT alone regrows after day 14 (o20) |
| M4 | ROS generation under 660 nm | photodynamic tumour-cell killing | supports | a10, a12, a14, a15 | PDT alone gives only partial inhibition (o21); graph carries it as a joint cause of a14 |
| M5 | 2D nanosheets | PA/CT imaging-guided therapy | supports | a8, a11, a20, o26, o27 | graph attributes PA contrast to NIR absorbance (a11 -> a20); Bi X-ray attenuation for CT is not a separate node |
