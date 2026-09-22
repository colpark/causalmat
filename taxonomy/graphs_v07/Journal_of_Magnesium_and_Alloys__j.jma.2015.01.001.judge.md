# Judge review: Journal_of_Magnesium_and_Alloys/j.jma.2015.01.001

**Verdict:** accept with minor fixes. There are 18 spine nodes and 40 nodes in total. The spine is one connected, stage-ordered path with two branches (yield strength; creep) that meet at n21. There are 3 audits (o5, o7, o16), all fair. Every spine STR/PRP/PRF claim has evidence or a stated basis (n9 argued). The v04 rules hold: PRP/diagnostic n17 -> KNW/lookup k2 -> MEC/identification n19; the o15 collapse op; the o12/o13/o14 derives chain.

## Changes
- o5: label and image_note corrected. F1c shows faint grain-boundary lines between the particles, weaker in d-f, so "not resolved in b-f" overstated it. The label now reads "at most faintly traced (c), not measurable". Panel a cell size re-estimated at ~50-100 um (the 200 um scale bar is ~70 px).
- n18: attrs.basis changed from evidenced to attributed. The existence of a threshold stress is evidenced (o13, o15), but its origin in dislocation-SiCp interaction comes from the text, and o16 qualifies it (AZ91 alone shows sigma_thr ~24 MPa). basis_note added.
- n21: requires_unseen filled with the grain sizes (F1 linked text) and the threshold-stress attribution (F6/F7 linked text).

## Panel checks (every cited crop opened: 15 crops + F6 whole figure, 18 nodes)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| n13 | F3 | confirmed | - | YS ~93, 113, 124, 127, 136, 142 MPa; largest steps at 0->5 and 5->10 wt% |
| n16 | F7a | confirmed | - | 15/20/25 wt% lie below AZ91 at every stress; 5/10 wt% overlap it |
| n17 | F7b | confirmed | - | n_t 5.4-5.8 in the legend |
| n20 | F7a | confirmed | - | same reading as n16, limited to >=15 wt% |
| n14 | F4 | confirmed | - | UCS ~310 -> 363 MPa, monotonic |
| o2 | F1b-f | confirmed | - | particles across the whole field; clusters in e; streaks in f |
| o3 | F2a | confirmed | - | X150, bright slivers spread evenly; partial is right |
| o4 | F2b | confirmed | - | angular particles ~10-22 um on a debris-covered background; not a polished section; partial is right |
| o5 | F1a-f | confirmed | - | network clear in a; faint traces in c (label fixed) |
| o6 | F3 | confirmed | - | values correct |
| o7 | F3 | confirmed | - | UTS ~188 -> 174 MPa; error bars overlap for 0-20 wt% |
| o8 | F4 | confirmed | - | values correct |
| o9 | F5a, F5b | confirmed | - | tear-ridge network in both; dimples not resolved at X150 |
| o12 | F7a | confirmed | - | at 120 MPa, 5/10 wt% ~1.2e-5 vs AZ91 ~9e-6 |
| o13 | F7a | confirmed | - | n 7.2 -> 8.9; 15 wt% (8.5) > 20 wt% (8.4) |
| o14 | F7b | confirmed | - | n_t 5.4-5.8 |
| o15 | F7b | confirmed | - | series in a narrow band, spread ~x2; partial is right |
| o16 | F7a, F7b | confirmed | - | AZ91 at ~56/96 MPa sigma_eff for 80/120 MPa applied -> ~24 MPa; 25 wt% ~34 MPa |

o11 cites F6 by fig_ref only (tier C, no panels offered). I read the whole figure: the minima of ~1.8e-7, ~1.3e-6 and ~6e-6 s-1, the ~2-5% strain at the minimum and the ~95/22/7 h test times are all correct.

Overturned: 0.

## Technique mismatches
None. The micrograph cue fits OPTICAL on F1 and SEM on F2 and F5. F3, F4 and F7 have no cue class, and MECH:tensile, compression and creep match the plotted quantities. MECH:compression and MECH:creep are not in the MECH mode list of normalize_technique.py, but they are the established v07 forms, so I left them. No cue overrides.

read_from: o13 and o14 restate the listed F7 annotations and are correctly "annotation". The other OBS nodes read pixels or axes.

## Mode changes
None. Only n13 has two or more causes edges (n7, n8, n9). It is joint, and that is right: the F3 text lists co-acting mechanisms, and no caption or figure shows a choice.

## Source checks
One change: n21 requires_unseen (see Changes). All other nodes were checked and are consistent.

## MatMech (read after the graph was final; graph not edited)

| pair | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | stir casting -> grain refinement, dispersion, clean interface | supports | n6, n7, n8, n9, n11 |
| M2 | refinement + dispersion + interface -> YS, UCS up; UTS about unchanged | supports | n7, n8, n9, n12, n13, n14, o7 |
| M3a | structure -> lower minimum creep rate, higher n | supports | n7, n16, n18, o12, o13 (graph: only >=15 wt%, via threshold stress, not grain refinement) |
| M3b | structure -> higher true stress exponent n_t | contradicts | n17, o14 (n_t flat at 5.4-5.8, AZ91 included) |
| M4 | properties -> creep resistance at 175 C | supports | n16, n20, n21 |
| M5 | stir casting -> performance | supports | n6 -> n7 -> n16 -> n20; n13 |

**Tally:** supports 5, contradicts 1, not covered 0. M3 was split in two because its effect bundles one supported readout and one contradicted readout.
