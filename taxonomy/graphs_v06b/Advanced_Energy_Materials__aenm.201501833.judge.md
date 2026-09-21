# Judge review: Advanced_Energy_Materials/aenm.201501833

**Verdict:** accept with minor fixes

## Changes

- o1 image_support shown -> partial: NixPyOz FTIR trace sits at the sub-panel floor ~1700-1150 cm-1, so 'carboxylate bands absent' cannot be separated from saturated absorption
- o1 read_from axis -> annotation: band positions are written labels on the panel (1624cm token)
- o2 read_from axis -> annotation: restates listed annotations '91lem' (911 cm-1) and 'oEs' (530 cm-1); annotation_match added
- o10 image_support shown -> partial: only the inset high-frequency arc is smaller for NixPyOz; the main plot shows a larger NixPyOz low-frequency arc, not a Warburg line
- o11 label: cathodic range widened 0.15-0.22 V -> 0.15-0.27 V (panel b cathodic peaks at ~0.21-0.27 V)
- o12 image_note: 100 mV/s anodic values are window-end currents; cathodic peaks nearly equal between electrodes
- added audit o18 (OBS/response/trend, text_silent, panels F5a-d) qualifies n13 via cross_check_consistency: CV currents differ ~1.5x while GCD discharge times differ ~4x
- note (not changed): o9 read_from 'text' is outside pixels/annotation/axis; kept because o9 is a text_only readout with no panel

## Panel checks (every cited crop opened: 14 crops, 19 node citations)

| node | panel_ids | ruling | correct_id | note |
|---|---|---|---|---|
| n3 | F1 | confirmed |  | scheme draws Ni-BTC coordination with dashed H-bonds; chain topology not drawn, partial fair |
| n4 | F1 | confirmed |  | arrow labelled 'Sodium phosphate / Hydrothermal Synthesis', product drawn as Ni-O-P network |
| o1 | F2a | confirmed |  | right panel; 1624/1565/1436/1338 labels on Ni-MOF trace; NixPyOz trace saturated at floor 1700-1150 cm-1, image_support lowered to partial |
| o2 | F2a | confirmed |  | 1113, 1010, 938, 911, 620, 530 cm-1 labels on NixPyOz trace |
| o3 | F2b | confirmed |  | Ni-MOF drops ~78% -> ~23% at ~430-470 C, residue ~12%; NixPyOz ends ~75% |
| o4 | F3a, F3b | confirmed |  | sharp MOF reflections (max ~7700 at ~18.8 deg) vs broad humps at ~20, ~30, ~35 deg |
| o5 | F3b | confirmed |  | card sticks at ~14.5 and ~28 deg have no counterpart; no feature at 25.3 deg |
| o6 | F4a, F4b | confirmed |  | smooth faceted bars (a) vs granular-surfaced rods of same outline (b) |
| o7 | F4a, F4b | confirmed |  | against 1 um bars (different pixel lengths at x15000/x16000): ~0.5-1 um vs ~1.2-1.4 um; partial fair (few intact rods in b) |
| o8 | F4b | confirmed |  | abundant loose nanoparticle aggregates on and between rods |
| o10 | F5f | confirmed |  | right panel; image_support lowered to partial: inset arc smaller for NixPyOz but main NixPyOz arc larger than MOF's |
| o11 | F5a, F5b | confirmed |  | right panels; cathodic range widened to 0.15-0.27 V |
| o12 | F5a, F5b | confirmed |  | currents grow with sweep rate in both; high-rate anodic values are window-end |
| o13 | F5c, F5d | confirmed |  | 1 A/g discharge ~180 s (c) and ~730 s (d); d plots one curve set only |
| o14 | F5e | confirmed |  | ~1625 and ~400 F/g at 1 A/g |
| o15 | F5e | confirmed |  | ~1045 and ~85 F/g at 20 A/g; 64% and 19% written in panel |
| o16 | F5g | confirmed |  | ~1100 -> ~590 F/g over 10000 cycles, CE flat at 100% |
| o17 | F5g | confirmed |  | ~1100 -> ~840 by 2000 cycles, ~770 at 4000: steepest fade in first 2000 cycles, contradicting text |
| o18 | F5a, F5b, F5c, F5d | confirmed |  | new judge audit; same crops as o11-o13 |

## Technique mismatches

- none: F2a cue FTIR agrees with FTIR (o1, o2); F5a/F5b cue electrochemistry agrees with ECHEM:CV (o11, o12, o18); every other cited crop has no cue class. No false 'micrograph' cue in this paper; no cue overrides.

## Read_from

- o1, o2 set to annotation (see changes); o5 already annotation (JCPDS:04-010-2575). Legend-only annotations (sample names) on F2b, F3a, F5e, F5f do not make the numeric readings annotation.

## Mode changes

- none: n10 is the only claim with two causes edges (n8, n9), both 'joint'; linked text credits loose structure and conductivity together, no figure shows a choice.

## Source changes

- none: every figure-dependent sample mapping (F4 a/b, F5 c/d, F5g) is already listed in requires_unseen with source 'text'.

## MatMech tally (read after the graph was final; graph not edited)

supports 3 · contradicts 0 · not covered 1

| pair | cause | effect | verdict | graph nodes |
|---|---|---|---|---|
| M1 | hydrothermal ligand substitution of Ni-MOF with sodium phosphate | porous microrods, amorphous-crystalline texture, BTC replaced by PO4 | supports | n5, n6, n7, n8 |
| M2 | phosphate-substituted porous microrod structure | higher specific capacitance and conductivity | supports | n6, n8, n9, n10, n11 |
| M3a | capacitance and conductivity (charge transfer) | 1627 F/g at 1 A/g, 1044 F/g at 20 A/g, 53.65% retention after 10000 cycles | supports | n10, n13, n14, n15 |
| M3b | capacitance and voltage window | energy density 7.95 Wh/kg at 500 W/kg | not_covered |  |

Notes: MatMech's hollow morphology, BET area (142.24 vs 2.51 m2/g) and phosphate-reinforcement cycling attribution are text-only facts absent from the packet; MatMech's 'smaller semicircle' matches only the inset (o10 partial); graph audits o17 and o18 qualify, not contradict, the M3a figures.
