# Judge review: Journal_of_Advanced_Ceramics/s40145-019-0329-1

Role of Al and Ti doping in modulating electrical properties of BIVOX system

**Verdict:** accept with minor fixes.

## Round-4 checklist
- Spine: 12 connected spine nodes (HYP n1 -> DES n2/n3 -> PRC n4 -> n5 -> STR n7 -> n6 -> PRP n12 -> DSC n20; second branch n5 -> n9 -> n11 -> n12; MEC n8 explains n12). It reads as the paper's argument: co-doping stabilises tetragonal phase and vacancies, with grain growth, giving the x = 0.175 conductivity peak.
- Evidence: n6 (o1, o3, o5, o6), n9 (o11), n11 (o19), n12 (o17, o22) are evidenced; n7 and n8 carry basis argued. OK.
- v04 rules: all types and ops valid. One op fixed (o19 -> n11). n7 -> n16 causes is thin: the text blames dopant coordination, vanadium reduction and defect trapping. It is kept as the defect-trapping link.
- Audits: a1, a3, a7 (3 of 5 allowed). All three were checked against the crops and are fair. The F5 red-shift vs text blue-shift conflict stays in o15 image_note.

## Changes
- source figure -> text (+requires_unseen) on o1, o7, o11, o12, o17, a7, o19: each label carries a caption-only fact (temperature, F2 panel-to-composition map, F7 sample identity)
- n6 source figure -> inferred; requires_unseen lists the prior-knowledge peak/transition assignments (k3) and the Table 1 fraction
- o19 -> n11 mm_op recognize_signature -> assign_features: the reading assigns the dominant arc to the grain-interior process via a known (capacitance) mapping, not a shape class implying a mechanism
- technique normalised: o5, a3 FTIR -> IR; o15 UVVIS -> UVVIS:Tauc (controlled form only)

## Panel checks (every cited panel opened)

| node | panel | ruling | correct id | note |
|---|---|---|---|---|
| n6 | F1c | confirmed | - | inset: x=0.1 split/shouldered ~32.05/32.3 deg, x=0.15 partly merged, x=0.175 single peak |
| n6 | F4 | confirmed | - | sharp endotherm ~421 C (x=0.10), shallow ~400 C (x=0.15), none for x>=0.175 |
| n6 | F8 | confirmed | - | step near 1000/T~1.4 for x=0.10 only (420 C arrow) |
| n12 | F8 | confirmed | - | x=0.175 highest log(sigma T) for 1000/T>1.55 |
| n12 | F6 | confirmed | - | x=0.175 arc ~9 kOhm vs 20-28 kOhm; 200 C from caption |
| n16 | F8 | confirmed | - | x=0.10 on top for 1000/T<1.4; x=0.20/0.25 lowest |
| n18 | F5 | confirmed | - | x=0.175 Tauc line meets axis ~1.93 eV, lowest |
| o1 | F1c | confirmed | - | inset doublet merging, as labelled |
| o3 | F4 | confirmed | - | x=0 endotherms ~445 and ~540 C; x=0.10 ~421 C; x=0.15 shallow ~400 C; x>=0.175 broad drift only |
| o5 | F3 | confirmed | - | x=0.10 dip ~830 cm-1 within the 700-850 band; flat bottom for higher x |
| a3 | F3 | confirmed | - | red (0.15) and blue (0.175) coincide 700-850 cm-1 |
| o6 | F8 | confirmed | - | jump for x=0.10 at the 420 C arrow; x=0.15 kink is faint and overlaps x=0.175 points |
| o7 | F1b | confirmed | - | * reflection ~27 deg on x=0.25 trace only |
| o7 | F1c | confirmed | - | * reflection on x=0.25 trace only |
| o9 | F1e | confirmed | - | Ycal/Yobs overlay with near-flat difference line; axis 10-80 deg |
| a1 | F1d | confirmed | - | pixel peak tops ~28.54, 28.53, 28.60, 28.58, 28.56 deg for x=0.10-0.25: no monotonic low-angle shift |
| o11 | F2a, F2b | confirmed | - | larger polygonal grains in (b) than (a); 10 um bars |
| o12 | F2a, F2b, F2c | confirmed | - | bright particulate clusters over (c) only |
| o15 | F5 | confirmed | - | intercepts ~1.93 (0.175), ~2.03-2.12 (other doped), ~2.17 (x=0) |
| o17 | F6 | confirmed | - | orange x=0.175 arc ends ~9 kOhm |
| a7 | F6 | confirmed | - | x=0.15 arc ~28 kOhm > x=0.10 ~20 kOhm |
| o19 | F7 | confirmed | - | one dominant depressed arc + short low-f tail at 200-300 C; circuit inset here, not in F6 |
| o22 | F8 | confirmed | - | purple x=0.175 highest at every point with 1000/T>=1.55 |
| o23 | F8 | confirmed | - | green x=0.10 highest for 1000/T<1.4; x=0.20/0.25 lowest |

24 checks over 13 distinct crops (F1b, F1c, F1d, F1e, F2a, F2b, F2c, F3, F4, F5, F6, F7, F8): 24 confirmed, 0 overturned.

## Technique mismatches
- None. Every OBS technique is compatible with its panel's cue classes; F1b/F1d/F1e and F3-F8 have no cue class. No cue overrides.
- Normalisations only (not mismatches): o5 FTIR -> IR; a3 FTIR -> IR; o15 UVVIS -> UVVIS:Tauc
- read_from: none of the cited panels' listed annotation strings is restated by an observation. o6 and o7 keep 'annotation' (the 420 C arrow label, the * marker).

## Mode changes
- None. n12 is the only claim with two or more causes edges (n6, n11). It stays joint: the text gives both as concurrent reasons ('is also the reason', 'is also a cause').

## Source changes
- o1: figure -> text; requires_unseen += ['sintering temperature 800 C of the inset patterns (caption only)']
- o7: figure -> text; requires_unseen += ['heat-treatment states 750 C and 800 C of F1b/F1c (caption only)']
- o11: figure -> text; requires_unseen += ['panel-to-composition mapping (a) x = 0.10, (b) x = 0.175 (caption only)']
- o12: figure -> text; requires_unseen += ['panel-to-composition mapping (a) x = 0.10, (b) x = 0.175, (c) x = 0.25 (caption only)']
- o17: figure -> text; requires_unseen += ['measurement temperature 200 C (caption only)']
- a7: figure -> text; requires_unseen += ['measurement temperature 200 C (caption only)']
- o19: figure -> text; requires_unseen += ['sample identity x = 0.175 of F7 (caption only)']
- n6: figure -> inferred; requires_unseen += ['assignment of the ~32 deg doublet to orthorhombic (020)/(200) and the singlet to tetragonal (110), and of the DSC endotherm / conductivity step to the beta-gamma transition (prior knowledge, k3)', 'x = 0.15 is 59.6% tetragonal (Table 1 fit, text)']

## MatMech (read after the graph was final; graph not edited)
Tally: supports 3, contradicts 0, not covered 1.

- M1: solid-state calcination 650/750 C + sintering 800 C (with co-doping) -> tetragonal phase stabilised for x>=0.175: **supports** (n4, n5, n7, n6)
- M2: stabilised tetragonal phase, disorder, more oxygen vacancies -> enhanced intermediate-T conductivity; grain-interior dominance: **supports** (n6, n7, n8, n12, n11)
- M3: sintering-induced grain growth (max at x=0.175) -> enhanced ionic conductivity: **supports** (n5, n9, n11, n12)
- M4: c-parameter expansion + vacancy concentration -> lower activation energy, higher conductivity: **not_covered** (n19, n7, a1)

- Note: M4: graph has lattice expansion only as support for vacancy creation (n19->n7, qualified by a1); no lattice->Ea/conductivity link and no Ea node. MatMech band gap 1.95 eV vs ~1.93 eV read from F5.
