# Judge review: Journal_of_Advanced_Ceramics__s40145-019-0334-4

**Judge:** senior investigator  
**Verdict:** accept with minor edits

## Round-4 checklist

- **spine**: 13 spine nodes, one connected path j1->j2->j3/j4->j5->{j6,j7,j8,j9}->{j10,j11}->j14 with j12 bridging; reads as the paper's argument (in-situ reaction -> platelets + nano-SiC -> toughness/strength)
- **evidence**: every spine STR/PRP/MEC claim has an OBS evidences edge (j6 o1/o2/o3/o12, j7 o6, j8 o7/o8/o9, j9 o9/o10/o11, j10 o14, j11 o13, j12 o18)
- **v04 rules**: relative density as STR/microstructure/porosity, fracture mode as PRP/behavior_class, F4 bar chart as xy_curve, reactive HP as one PRC/synthesis with concurrent_forming: all correct
- **mm_ops**: all name the figure act; register_colocated_views on the EDS zone readings is apt (zone located on the BSE field)
- **audits**: 2 audit nodes (a1 residual ZrC/ZrSi2 at RZSZ-25; a2 density vs property maxima offset); both fair and bear on spine claims

## Changes

- o9: platelet length corrected to ~0.7-2 um (re-measured against the 500 nm bar); image_note updated
- a2: technique list completed (PHYS:density, MECH:hardness, MECH:flexural, MECH:toughness) since it reads all four F4/F7 series

## Panel checks (every cited crop opened)

| node | panel ids | ruling | correct id | note |
|---|---|---|---|---|
| j7 | F4 | confirmed |  | bar chart of relative density, RZSZ-0..25 |
| j8 | F5b | confirmed |  | BSE RZSZ-20, arrows to elongated ZrB2; many grey grains irregular, supports partial |
| j8 | F5c | confirmed |  | BSE high-mag, boxed interlocking elongated grains |
| j8 | F6 | confirmed |  | fracture surface, rod/plate ZrB2 clearly shown |
| j8 | F8d | confirmed |  | fracture surface RZSZ-20, boxed interlocking microstructure |
| j9 | F5a | confirmed |  | dotted outline "SiC-rich region", zone B marked |
| j9 | F5f | confirmed |  | EDS zone B: C 58.91, Si 34.51, Zr 6.58 at% |
| j9 | F6 | confirmed |  | nano-sized SiC clusters among platelets |
| j10 | F7 | confirmed |  | toughness 4.25/4.5/5.5/6.08/5.97 |
| j11 | F7 | confirmed |  | strength 505/533/584/655/571 MPa |
| j12 | F8f | confirmed |  | labelled deflection, bridging, pull-out, branching into SiC-rich region |
| j12 | F9 | confirmed |  | schematic of the same toughening mechanisms |
| j15 | F7 | confirmed |  | hardness 12.6/14.6/15.9/17.1/16.0 GPa |
| j16 | F8b | confirmed |  | labels intergranular and transgranular fracture of ZrB2 |
| j16 | F8c | confirmed |  | same labels, RZSZ-15 |
| o5 | F3 | confirmed |  | three computed dG(T) lines; values match label |
| o6 | F4 | confirmed |  | values match (91.7, 94.9, 98.5, 97.6, 96.4) |
| o7 | F5a, F5b | confirmed |  | BSE arrows "Elongated ZrB2 grains" |
| o8 | F5c, F8d | confirmed |  | "Interlocking microstructure" boxes in both |
| o9 | F6 | confirmed |  | platelet length re-measured: ~0.7-2 um rather than 1-2.5 um; label corrected |
| o10 | F5a | confirmed |  | dark outlined region several um across |
| o11 | F5f | confirmed |  | table and spectrum match label |
| o12 | F5e | confirmed |  | table and W L/M lines match label |
| o13 | F7 | confirmed |  | right panel, red squares |
| o14 | F7 | confirmed |  | right panel, blue triangles; 20 and 25 overlap within error bars |
| o15 | F7 | confirmed |  | left panel |
| o16 | F8b, F8c | confirmed |  | annotation strings match |
| o17 | F8e | confirmed |  | "Secondary crack", "Coarse ZrB2" |
| j17 | F8e | confirmed |  | coarse ZrB2 grains visible; coarsening vs other compositions needs caption mapping (partial) |
| o18 | F8f | confirmed |  | annotation strings match |
| a2 | F4, F7 | confirmed |  | density maximum at 15, property maxima at 20: shown |

Distinct crops opened: 15; node-panel rulings: 31; overturned: 0.

## Technique mismatches

- none

## Cue overrides

- none

## Source / requires_unseen changes

- none

## Mode changes

- none

## MatMech comparison (read after the graph was final; graph not edited)

Tally: supports 2, contradicts 0, not covered 0.

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | in-situ reactive hot pressing of ZrSi2/B4C/C with excess ZrSi2 (0-25 vol%) | platelet ZrB2, interlocking microstructure, nano-sized SiC, secondary WSi2 and ZrC at high ZrSi2 | supports | j5, j6, j8, j9, j18, a1 | graph carries reactive HP -> phases, platelets/interlocking, nano-SiC clusters; WSi2 via j18, ZrC only at RZSZ-25 via audit a1. Not covered: excess ZrSi2 refining SiC (RZSZ-0 submicron SiC only in image_note) |
| M2 | platelet ZrB2 + interlocking microstructure + nano-sized SiC | hardness, strength and toughness rise then fall, peaking at RZSZ-20 (17.1 GPa, 655 MPa, 6.08 MPa m^1/2) | supports | j8, j9, j10, j11, j15, j12, j14, j17 | j8/j9 causes j10 (joint), j8 causes j11, j12 crack-wake mechanism, j17 coarsening counteracts strength at RZSZ-25 |
