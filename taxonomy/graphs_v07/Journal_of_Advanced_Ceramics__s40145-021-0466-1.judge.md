# Judge review: Journal_of_Advanced_Ceramics/s40145-021-0466-1

This paper makes porous N-doped carbon spheres for oxygen reduction (ORR) and argues that nanopore confinement drives the 4-electron path. Judge: senior investigator (v07 part B).

## Verdict

**Accept with minor fixes.** The spine reads as the paper's argument: 16 nodes, connected from HYP to DSC/conclusion. The path is need -> confinement hypothesis -> spheres/urea/ZnCl2/temperature sweep -> carbonization -> ZnCl2-evaporation pores -> fine/medium porosity -> confinement mechanism -> 4e path -> best E1/2 -> durability and methanol tolerance -> conclusion. There is one control branch: active-N content, which is lowest in NPC-1000 and is set against activity. Every spine STR/PRP/PRF node and m12 have OBS evidence, and m9 is basis=argued. All types, rels and ops are v04-valid, and the mm_ops fit the acts. There are 4 audits (a1, a2, o9, o11a), all fair. a1 is the strongest: NC-1000, made without ZnCl2, reaches the same ~-5 mA/cm2 plateau.

## Changes

- o17: panel id F6b restored (was dropped for a false 'micrograph' cue); cue_conflict attr removed; recorded under cue_overrides
- o3: read_from pixels -> annotation (label restates listed annotations 'flakes', 'spheres'); increase still judged from pixels (image_note)
- h1: source inferred -> text; requires_unseen lists the need statement in F4 linked text and DMFC motivation
- d3: label drops 'Biomass-derived' (a text word not on F1a); source figure kept
- o15: source figure -> inferred; requires_unseen lists the K-L constants needed to turn the slope into n
- m_aN, m_aS: attrs.mechanism_class added (v04 MEC requirement)
- o16: image_note added: F6a and F6b plot the same five MD runs, so peroxide density is not varied independently of pore size (text silent); o17 image_note extended likewise

## Panel checks (every cited crop opened: 16 unique panels incl. restored F6b, 34 citations)

| node | panels | ruling | note |
|---|---|---|---|
| d3 | F1a | confirmed | F1a schematic: glucose solution -> polymerization -> hydrothermal carbon sphere |
| d4 | F1a | confirmed | F1a shows urea mixed in and N-doped product; role as N source is text (partial kept) |
| d5 | F1a | confirmed | F1a shows ZnCl2 mixed in and porous product; porogen role is text (partial kept) |
| p7 | F1a | confirmed | F1a: glucose solution -> Delta polymerization -> hydrothermal carbon sphere |
| p8 | F1a | confirmed | F1a: mixing with urea+ZnCl2 -> Delta carbonization -> N-doped porous carbon; no conditions shown |
| s10 | F2d, F2e | confirmed | F2d plateau ~280/~390/~540 cm3/g; F2e fine (~0.5 nm) and medium (~1.3-2 nm) peaks grow, ~35 nm peak ~0.3-0.4 |
| s11 | F3b | confirmed | F3b stacked bars: pyridinic+graphitic ~3.4/2.3/1.3 (NPC) vs ~1.7 (NC-1000) |
| r14 | F4b | confirmed | F4b: NPC-1000 curve right of Pt/C at half-wave (~0.86 vs ~0.85 V) |
| f15 | F4c, F4d | confirmed | F4c NPC-1000 ~76% vs Pt/C ~70% at 8 h; F4d NPC-1000 back to ~100%, Pt/C ~60-66% |
| s_ph | F1b | confirmed | F1b: sharp g-C3N4 peaks in NPC-300, weak at ~13 deg in NPC-800, amorphous hump only in NPC-900/1000 |
| s_sh | F2a, F2b | confirmed | F2a SEM and F2b TEM: ~200 nm spheres; flakes increase to large sheets in NPC-1000 |
| s_N | F3a | confirmed | F3a: N ~5.9/3.8/1.8 at% NPC, ~2.3 NC-1000; C ~87/91/95/95 |
| o1 | F1b | confirmed | XRD patterns as labelled; hump marker shifts ~25 -> ~20 deg |
| o3 | F2a | confirmed | SEM of three samples; flakes grow; read_from changed to annotation (restates 'flakes'/'spheres') |
| o4 | F2b | confirmed | TEM with SAED insets; halos diffuse in all three |
| o6 | F2d | confirmed | type-I isotherms, plateau values as labelled |
| o7 | F2e | confirmed | PSD values as labelled; medium band ends ~3 nm |
| o8 | F3a | confirmed | element bars as labelled; small Zn bar on NC-1000 |
| o9 | F3b | confirmed | species bars as labelled |
| o10 | F4a | confirmed | O2 CV reduction peaks ~0.73/0.80/0.83 V, Pt/C ~0.84 V |
| o11a | F4b | confirmed | LSV ranking as labelled |
| o11b | F4b | confirmed | limiting currents ~-3.4/-3.5 vs ~-5.0 as labelled |
| o12 | F4c | confirmed | i-t at 8 h ~76% vs ~70% |
| o13 | F4d | confirmed | methanol arrow at ~190 s; Pt/C to ~60%, recovers to ~66% at 400 s; NPC-1000 spike to ~160% |
| o14 | F5a | confirmed | LSV 225-2025 rpm, limiting current ~2.1 -> ~5.5; K-L inset lines overlap |
| o15 | F5a | confirmed | K-L inset slope ~2.0 (J^-1 0.18 -> 0.45 over w^-1/2 0.07 -> 0.21); n from slope needs constants (source -> inferred) |
| o16 | F6a | confirmed | linear, R2 = 0.9998, 4.3 -> 12 over 0.36-1.0 nm^-3; same points as F6b |
| o17 | F6b | confirmed | right panel (collision frequency vs 1/D, 10/7/5/3/1 nm labels); citation restored, 'micrograph' cue is the OCR scale-bar misfire on the '1 nm'/'3 nm' point labels |
| o18 | F5b | confirmed | Tafel slopes printed on panel as labelled |
| a2 | F4c | confirmed | gap ~13 points at 1 h, ~6 at 8 h; NPC-1000 still falling |
| a1 | F4b | confirmed | NC-1000 plateau ~-5.1 mA/cm2, half-wave ~0.77 V |

Overturned: 0.

## Technique mismatches

None. Cue classes on cited crops: F1b XRD (o1 XRD ok), F2b micrograph (o4 TEM/TEM:SAED ok), F4a electrochemistry (o10 ECHEM:CV ok), F5a electrochemistry (o14, o15 ECHEM:LSV ok), F6b micrograph (o17 ATOM:MD; false cue, override). All other cited crops have no cue class. read_from: o1, o4, o18 correctly annotation; o3 changed to annotation; o13's 'Methanol' arrow only marks the event, values read from axis, kept axis.

Cue override: o17 / F6b / 'micrograph'. F6b is an ATOM:MD xy plot (collision frequency vs 1/D); OCR read the '1 nm'/'3 nm'/'10 nm' point labels as a scale bar. Crop plainly is the right panel for o17.

## Mode changes

None. no claim has two or more causes edges (p8->m9, s10->r13, r13->r14 each single); no mode field needed.

## Source changes

- h1: inferred -> text, with requires_unseen added.
- o15: figure -> inferred, with requires_unseen listing the K-L constants.
- d3: the label was trimmed so that source=figure holds.
All other source and requires_unseen values were checked and left as they were.

## MatMech tally (read after the graph was final; graph not edited)

**supports 2 / contradicts 0 / not covered 0**

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | carbonization of carbon spheres with urea and ZnCl2 at 1000 C -> abundant fine (<1 nm) and medium pores in microflakes | supports | d5, d6, p8, m9, s10, o6, o7 | localisation of pores in microflakes is not a graph claim (s_sh is unlinked to s10); NC-1000 pore comparison is ESM Fig. S2, not in packet |
| M2 | porous microstructure with fine/medium pores -> ORR performance at or above Pt/C with better stability and methanol tolerance | supports | s10, m12, r13, r14, f15, c16, o16, o17 | graph routes pores -> confinement -> 4e -> E1/2 -> f15; a1 (NC-1000 reaches the 4e plateau) and a2 (durability gap narrows) qualify it; MatMech Pt/C Tafel 68.5 mV/dec disagrees with F5b (81.5) |
