# Judge review: Journal_of_Magnesium_and_Alloys/j.jma.2020.11.023

High thermoelectric performance at room temperature of n-type Mg3Bi2-based materials by Se doping

**Verdict:** accept with minor fixes. 53 nodes, 87 edges, 18 spine nodes. There is one connected HYP -> DSC/conclusion path with two branches. The electrical branch runs Se donor (n8) -> n_H, mu_H (n10, n11) -> rho (n12) -> PF (n13). The thermal branch runs single phase (n7) -> alloy scattering (n15) -> low kappa_L+kappa_b (n14). The branches meet jointly at RT ZT (n16) and efficiency (n17). Every spine STR/PRP/PRF claim has an OBS evidences edge, and n15 is basis=attributed. Every mm_op names a figure act. There are 3 audits (a1, a2, s8), and all are fair against the crops after the a2 reframe. All types, rels and ops are v04-valid. The node total (53) is above the 25-40 aim; nothing was dropped, so ids stay stable.

## Changes

- o4 label: 'K, M and Gamma drop ... to E_F' -> 'M, K and L drop from ~0.15 eV to E_F; Gamma CB stays ~0.35-0.4 eV up' (F2c/F2d read; the Gamma feature at E_F in c is the VB top)
- o5 label: 'M, K, Gamma and L within ~0.1 eV' -> 'M, K and L at E_F; Gamma ~0.35-0.4 eV higher'; image_note records text/figure conflict on Gamma
- n9 label: valley list (M, K, Gamma, L) -> (M, K, L); Gamma conflict recorded in image_note
- o8 label: 'lies above all literature points' corrected (x=0.04 at ~125 is below the ~139 Ref.39 point); read_from axis -> annotation (legend 'This work')
- o12 label: 'x=0 below 5' -> 'x=0 at most ~5' (x=0 reaches ~5.2 at 600-623 K)
- o16 read_from axis -> annotation (label restates listed annotation 'n-Bi,Te,Ref.8'); values still read from axis
- o18 read_from axis -> annotation (label restates listed annotations 'Ref.22', 'Ref.39'); bar heights read from axis
- a2 label/image_note: judge recomputation added. ZT ~0.82 for x=0.005 IS reproduced from S, rho, kappa; what fails is the plotted PF and the ranking x=0.005 > x=0.01. Qualifies edge to n16 kept, now aimed at the 'highest in series' part
- n16 attrs.note rewritten to match a2
- edge added o13 -> a2 derives (convert_to_quantity, via known_relation): a2 uses kappa from F5d
- n7, o1: source figure -> text; requires_unseen lists the reference-phase identity (F1b ticks carry hkl only)

## Panel checks (every cited crop opened: 23 crops, 31 node citations; 0 overturned)

| node | panels | ruling | note |
|---|---|---|---|
| k1 | F1a | confirmed | Mg3Sb2 cell with Mg(1), Mg(2), Sb labels; space group not in crop (source text kept) |
| o1 | F1b | confirmed | five patterns, all peaks on the hkl tick set, no extra reflections; (002)/(011) intensity ratio changes with x; phase name of ticks is text |
| o2 | F3a, F3b | confirmed | SEM fracture surface, 10 um and 5 um bars; stepped lamellar cleavage facets >10 um; no pores; grains not delineated (partial kept) |
| o3 | F3c, F3d, F3e, F3f | confirmed | Mg, Bi, Sb, Se maps at 50 um bar; even signal, shared dark zone right side in Mg/Bi; Se sparse near background (partial kept) |
| o4 | F2c, F2d | confirmed | panel c: M, K, L CBM ~0.15 eV above E_F; panel d: M, K at E_F, L ~0.05 eV. Gamma CB ~0.35-0.4 eV in d; the Gamma feature at E_F in c is the VB top. Citation confirmed, label corrected (Gamma removed) |
| o5 | F2d | confirmed | M, K, L valleys at E_F; Gamma CB not near E_F. Citation confirmed, label corrected |
| o6 | F4a | confirmed | n_H at 300 K: ~0.5 (x=0), 1.75, 2.6, 3.0, 3.3e19; doped curves rise above ~500 K |
| o7 | F4b | confirmed | doped mu_H falls with guide lines T^-0.5, T^-1, T^-1.5; x=0 rises; y-axis unit misprinted 10^19 cm^-3 |
| o8 | F4c | confirmed | stars at ~160, 170, 143, 125 cm2/Vs; highest literature point ~139 (Ref.39); x=0.04 star below it. Citation confirmed, label corrected |
| o9 | F4d | confirmed | 300 K squares on the orange SPB curve; 400 K circles and 500 K triangles below their curves; m*=1.2 m_e printed |
| o10 | F5a | confirmed | pixel reads rho(300 K): x=0 ~650, x=0.005 22.5, x=0.01 11.8 micro-ohm m; doped rise with T, x=0 falls |
| o11 | F5b | confirmed | S(300 K) ~-350, -241, -189, ~-183, ~-173 uV/K; x=0.005 |S| peaks ~450 K |
| o12 | F5c | confirmed | PF(300 K) x=0.01 28.8, x=0.02 ~26.3, x=0.04 ~23.6, x=0.005 23.2, x=0 ~1.7; x=0 reaches ~5.2 at 623 K |
| o13 | F5d | confirmed | kappa(300 K) 0.95-1.24 doped, x=0 ~1.28; minima 400-500 K; x=0 highest above ~325 K |
| o14 | F5e | confirmed | kappa_e 0.27-0.42 doped vs ~0.07 x=0 at 300 K |
| o15 | F5f | confirmed | x=0.01 ~0.69 at 300 K, ~0.60 at 400-450 K |
| o16 | F6a | confirmed | ZT(300 K) 0.84, 0.78, 0.69, 0.63; dashed n-Bi2Te3 Ref.8 curve ~0.88 at 300 K |
| o17 | F6a | confirmed | x=0.01 peak ~1.25 at ~500-525 K |
| o18 | F6b | confirmed | bars 0.82 (this work), 0.75 Ref.24, 0.70 Ref.22, 0.62 Ref.39, 0.32 Ref.40 |
| o19 | F7c | confirmed | eta at Th=623 K: x=0.01 ~11.8%, x=0.02 ~10.6%, x=0.005 and 0.04 ~9.5-9.7% |
| a1 | F5f | confirmed | x=0 curve 1.1-1.42 vs doped 0.6-0.92 at every T; gap ~0.4-0.6; audit fair |
| a2 | F5a, F5b, F5c, F5d, F6a | confirmed | judge re-read all five panels; arithmetic holds but the conclusion was reframed (ZT 0.82 reproduces from S, rho, kappa; ranking x=0.005 > x=0.01 does not) |

## Technique mismatches

None. F1b carries the XRD cue and o1 is XRD. F3b-F3f carry the micrograph cue: o2 is SEM and o3 is SEM:EDS (family SEM), and both are admitted. The other cited crops carry no cue class. No cue overrides were needed.

read_from: o8, o16 and o18 were changed to annotation because their labels restate listed legend or annotation strings. o5 and o9 were already annotation.

## Source changes

- n7: figure -> text (reference ticks in F1b carry hkl only; that they are Mg3Sb2 (P-3m1) is text)
- o1: figure -> text (same: phase name of the tick set is not in the panel)

## Mode changes

None. Four claims have two or more causes edges: n12 (n10, n11, s2), n16 and n17 (n13, n14), and s6 (n13, n14). All are joint, and no caption or figure presents a choice.

## MatMech (read after the graph was final; graph not edited)

supports 5 / contradicts 0 / not covered 0

| pair | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | ball milling + DC hot-pressing (1053 K, 45 MPa) -> single-phase, uniform, coarse-grained | supports | n6, n7, s1, s2 | graph has n6 -> n7, s1, s2; route itself absent from packet (n6 route 'not stated') |
| M2 | enhanced valley degeneracy (alloying + Se) -> high n_H and high mu_H at 300 K | supports | n9, n10, n11, n8, o4, o5 | n9 explains n10; mobility carried by n8 -> n11. Figure shows M, K, L valleys only (record lists Gamma too); record mu_H 150 for x=0.01 vs ~170 in F4b |
| M3 | Mg3Bi2-Mg3Sb2 alloying and Se doping -> kappa_L 0.6-0.7 W/mK at low T | supports | n15, n14, k6, a1 | n15 explains n14; a1 qualifies the alloy-only attribution (drop tracks Se doping), which is consistent with the record naming Se as co-cause |
| M4 | high PF and low kappa_L -> ZT 0.82 at 300 K, peak 1.24 at 498 K | supports | n13, n14, n16, s6 | joint causes edges into n16 and s6. Record assigns RT 0.82 to x=0.01; F6a gives 0.82-0.84 for x=0.005 and 0.78 for x=0.01 |
| M5 | hot-pressed coarse grains (low grain-boundary density) -> ZT_eng ~0.9 and ~12% efficiency | supports | s2, n12, n13, n17 | chain s2 -> n12 -> n13 -> n17 carries it; hot-press route not in packet; record's ZT_eng 0.9 vs ~0.84 in F7b (o19 note); 'PF_eng ~12%' is a record error (12% is efficiency) |

The record has three problems. It assigns RT ZT 0.82 to x=0.01, but F6a gives it to x=0.005. It lists Gamma among the conduction-band valleys, which F2d does not show. It writes 'PF_eng ~12%', but 12% is the efficiency.
