# Judge review: Bioactive_Materials/j.bioactmat.2020.02.005

**Verdict:** accept with minor fixes. 18 spine nodes, 55 total, one connected path. The Er screen and down-select lead into the Ce sweep. Gap narrowing, carrier separation and Er up-conversion join in the degradation claim, which leads through ROS to light-driven killing. A side branch covers dark killing by Ce ions. 3 audits (o15, o21, o24), each fair.

## Checklist
- spine_primary_argument: yes: need -> hypothesis -> Er screen/down-select -> Ce sweep -> dopant incorporation -> gap narrowing + carrier separation (+ Er up-conversion) -> dye degradation -> ROS -> light-driven bacteria killing -> conclusion
- spine_nodes: 18
- total_nodes: 55
- connected: True
- spine_evidence: every spine STR/PRP/PRF has an evidences edge (b6 o1/o2, b7 o3, b11 o19/o20, b13 o5/o6, b15 o7/o8/o9, b17 o10, b19 o11/o13); MEC b16 attributed, b18 argued
- v04_rules: types, rels, modalities and ops valid; no change
- mm_ops: each names the figure act; no change
- audits: 3 audit nodes (o15, o21, o24), each fair against the opened crop

## Changes
- o13 label corrected: 'Light-exposed plates of Er0.5Ce0.2Ti-O carry the fewest colonies for both S. aureus and E. coli; dark plates stay densely covered' -> 'Er0.5Ce0.2Ti-O light plates carry the fewest colonies for both strains; dark plates stay covered, sparser for doped samples' (F10a/b dark rows: doped plates are visibly sparser than control/TiO2); image_note added

## Panel checks (every cited crop opened; 25 crops, 32 node-panel citations; F5a opened too, uncited)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| b5 | F1 | confirmed | - | scheme: stirring, sol, 60 C 2 h gel, ageing/washing/drying/grinding/annealing; product drawn as Er and Ce co-doped TiO2 |
| o1 | F2 | confirmed | - | sharp lines at ~452, 488, 522, 545, 654 nm on Er-doped curves only; TiO2 flat |
| o2 | F2 | confirmed | - | 522 nm peak ~0.38 Er0.5, ~0.34 Er0.75, ~0.20 Er1, ~0.12 Er0.25; ranking as stated |
| o3 | F3a, F3b | confirmed | - | a: peak ~3.8e5 vs ~1.3e5 at ~565 nm, green only; b: ~1.2e5 vs ~1.8e4, green plus red 640-690 nm |
| o5 | F4b | confirmed | - | TiO2 sharp edge ~410 nm; co-doped curves tail to ~550 nm; Ce0.2 highest |
| o6 | F4c | confirmed | - | intercepts printed at arrows 2.20 (Ce0.2), 2.32 (Ce0.3), 2.46 (Ce0.1), 2.90 (TiO2) |
| o24 | F4c | confirmed | - | doped-sample dash lines fitted over hv ~2.3-2.6 where the Er line near 2.37 eV sits; audit fair |
| o14 | F4a | confirmed | - | R labels only on the Ce0.1 trace; faint ~27.4 deg peak on Ce0.2; A peaks on all |
| o15 | F4a | confirmed | - | Ce0.3 trace labelled A only, no reflection at ~27.4 deg; audit fair |
| o18 | F4d | confirmed | - | Eg(1) ~145 cm-1 on all traces; extra broad bands ~280 and ~620 cm-1 on doped traces (strongest Ce0.3); partial is right |
| o16 | F5d | confirmed | - | fringes labelled 0.233 nm A(112) and 0.328 nm R(110) in one HRTEM field |
| o17 | F5e | confirmed | - | SAED rings labelled R(101) 0.246 nm, A(105) 0.179 nm, A(101) 0.360 nm; OCR 'micrograph' cue comes from the scale bar, but TEM is a compatible family so no conflict |
| o19 | F5b | confirmed | - | C dominant, Ti, O; small Er ~1.4 keV and Ce ~4.9 keV peaks; partial is right |
| o20 | F6a, F6b, F6c | confirmed | - | Ti 2p 458.5/464.2 eV (a), O 1s 529.0/531.2/533.0 eV (b), Er 4d 168.8 eV fit over noisy data (c); partial is right |
| o21 | F6c, F6d | confirmed | - | Ce 3d is noise with dashed u/v markers only; Er 4d envelope sits above most data points; audit fair |
| o22 | F5c | confirmed | - | polyhedral crystallites ~20-50 nm in one ~250 nm aggregate |
| o7 | F7 | confirmed | - | TiO2 band 390-420 nm strongest, Er0.5Ti-O ~0.4-0.5 of it, Er0.5Ce0.2 lowest; no y ticks |
| o10 | F8 | confirmed | - | 60 min: Ce0.2 ~46, Ce0.3 ~41, Ce0.1 ~31, TiO2 ~20%; same order at 20 and 40 min |
| o8 | F9a | confirmed | - | Er0.5Ce0.2Ti-O small arc to ~1.5 kOhm then tail; TiO2 near vertical; partial is right |
| o9 | F9b | confirmed | - | light-on ~7e-6 vs ~5.3e-6 A/cm2, dark ~3e-6 for both; partial is right |
| o11 | F10c, F10d | confirmed | - | light: Ce0.2 ~91/93, Ce0.3 ~87/88, Ce0.1 ~68/73, TiO2 ~45, control ~4/7% |
| o12 | F10c, F10d | confirmed | - | dark: Ce0.1 ~28/33, Ce0.2 ~43, Ce0.3 ~45/47, TiO2 ~6, control ~0% |
| o13 | F10a, F10b | confirmed | - | light row Ce0.2 sparsest for both strains; dark row doped plates sparser than control/TiO2 (label corrected) |
| b16 | F11 | confirmed | - | schematic draws Ce3+/Ce4+ exchange at CB and VB |
| b18 | F11 | confirmed | - | schematic draws ROS from the particle destroying E. coli and S. aureus |

Overturned: 0.

## Technique mismatches

None. Cue classes on cited panels: F4a XRD (o14, o15 XRD:powder), F4b optical spectroscopy (o5 UVVIS), F6a-d XPS (o20, o21 XPS:region), F5c/F5d micrograph (o22, o16 TEM). F5e also carries a 'micrograph' cue, which comes from the scale bar on a SAED pattern. It is compatible with o17's TEM:SAED family, so no override is needed. All other cited crops have no cue class.

read_from: o6, o14, o16, o17, o18, o19 and o20 restate printed labels or values and are 'annotation'. o13, o15, o21 and o24 read pixels. The rest read axes. No change.

## Mode changes

None. The only claim with two or more causes edges is b17 (b13, b15, b7). It is 'joint', and no caption or figure shows a choice between the causes.

## Source checks

No changes. Text-dependent facts are listed in requires_unseen: NIR excitation (b7), MO dye (b17), strain and panel mapping plus simulated sunlight (b19), sample identity of F5/F6 (b11, b26), and the dopant roles and optima (b2, b24). b15 is 'inferred' through the premises k3 and k6. Nodes sourced to 'figure' can be read from their cited panels.

## MatMech (judge only, graph not edited): supports 5, contradicts 0, not covered 1

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | sol-gel synthesis + calcination (800 C per MatMech) | mixed anatase-rutile phase with Er3+ and Ce3+/Ce4+ incorporated | supports | b10, b25, b11, o14, o16, o17, o15, o21 | graph has b10 produces b25/b11; o15 qualifies (Ce0.3 has no rutile) and o21 qualifies the Ce valence reading; anneal temperature in graph is 700 C (Raman legend), 800 C not in packet |
| M2 | doped mixed-phase structure | reduced band gap, more visible absorption, lower PL/recombination, NIR up-conversion | supports | b11, b13, b14, b15, b7, b5 | graph gap values 2.90 -> 2.20 eV from F4c, not MatMech 3.2 -> ~2.4 eV; mixed phase itself is not a cause in the graph |
| M3 | surface Ce3+/Ce4+ mixed valence | better carrier separation and photocatalytic activity | supports | b11, b16, b15, b17, o21 | graph carries it as attributed MEC (b16) and flags that F6d does not resolve the Ce 3d peaks (o21) |
| M4 | enhanced visible absorption + suppressed recombination | ~91% S. aureus / ~93% E. coli killing under light | supports | b13, b15, b17, b18, b19, o11 | joint causes into b17, then ROS (b18, argued) into b19 |
| M5 | calcination at 800 C (vs 700/900 C) | optimal mixed phase, minimum gap | not_covered | - | no calcination-temperature series in the packet |
| M6 | optimal doping 0.5 mol% Er / 0.2 mol% Ce (+800 C) | maximum antibacterial efficiency | supports | b8, b9, b24, b19, o11 | Ce optimum shown in antibacterial data (o11); Er optimum in the graph comes from the optical screen (b6, b7), not from an antibacterial Er sweep as MatMech states |
