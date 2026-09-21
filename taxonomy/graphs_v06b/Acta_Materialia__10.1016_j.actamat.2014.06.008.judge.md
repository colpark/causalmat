# Judge review: Acta_Materialia__10.1016_j.actamat.2014.06.008

**Judge:** senior investigator  
**Verdict:** accept with edits

## Round-4 checklist

- **spine_nodes**: 15
- **connected**: True
- **spine_evidence**: a10 (o2), a11 (o4,o5,o6b), a13 (o6,o8,o10,o11), a14 (o15,o16), a15 (o13,o14); a16 basis argued; a17 (o3,o7)
- **audits**: a22 limitation, a20 ruled-out alternative, o17 partial: 3, fair
- **mm_ops**: all name the figure act; o4 overlay (model reference), o7->o13 convert_to_quantity via position

## Changes

- o11 and o6: F6c (240 C phase maps) restored; staff had dropped it for a false micrograph cue. o11 label now includes 240 C
- o6, o6b, o11 technique BCDI -> XRD:CXD (controlled form, same cue family)
- o3 technique XRD:pole_figure -> XRD:poleFigure (controlled mode)
- o5 image_support shown -> partial: F3e shows a long q_z streak, so 'compact along q_z' holds for the core only
- o14 and a15 source figure -> text: 'Lab cycle = film average' comes from the caption

## Panel checks (every cited crop opened)

| node | panel ids | ruling | correct id | note |
|---|---|---|---|---|
| o1 | F1b | confirmed |  | cross-section: boundaries run through the film to the substrate; 0.372 um label vs 475 nm in text noted |
| o2 | F1d | confirmed |  | EBSD map mostly blue with a few red/orange grains |
| o3 | F1c | confirmed |  | {111} pole map with tens of separate spots; dashed red circle around an isolated one |
| o4 | F3b, F3c, F3e, F3f | confirmed |  | calculated slices (b,c) show fringes and sharp rods; measured (e,f) broad, fringes washed out |
| o5 | F3e, F3f | confirmed |  | right panels; q_y spread ~10e-3 and narrow q_x confirmed, but q_z shows a long streak: image_support lowered to partial |
| o6 | F6a, F6b, F6c, F6d, F6e | confirmed |  | xz maps show only vertical bands at every temperature; F6c restored (cue override) |
| o6b | F6a | confirmed |  | 50 C xy map: stripes varying along y |
| o7 | F5a, F5c, F5e | confirmed |  | peak centre q_z ~0 (50 C), ~-10e-3 (240 C), ~+2e-3 (50 C after cooling) |
| o8 | F5a, F5c, F5e | confirmed |  | q_x extent of the intense peak larger at 240 C, back after cooling; guide lines barely move, partial fair |
| o10 | F4b | confirmed |  | heating 1.3e-3 -> 4.9e-3 A-1, cooling back to ~1.95e-3; size width 6.61e-4 printed |
| o11 | F6a, F6b, F6c, F6d, F6e | confirmed |  | phase jumps along x: few (50 C) -> several (140 C) -> many (240 C) -> fewer on cooling; F6c restored (cue override) |
| o13 | F4a | confirmed |  | Syn loops far flatter than the cyan thermoelastic line, branches do not coincide |
| o14 | F4a | confirmed |  | Lab and Syn cycle 2 loops nearly coincide; Syn cycle 1 heating branch above both |
| o15 | F7c | confirmed |  | g1/g5 coincide, g4 and g2 slightly off, g6 ~10-15 deg one side, g3 ~30 deg the other |
| o16 | F7b | confirmed |  | g4, g2 above and g5 below g1; g6 left, g3 right |
| o17 | F7a | confirmed |  | dark grooves at g1-g6 and g1-g3 boundaries, but g1-g5/g1-g2 also dark in places: partial fair |

Distinct crops opened: 20; node-panel rulings: 32; overturned: 0.

## Technique mismatches

- {"node": "o11", "panel": "10.1016/j.actamat.2014.06.008#F6c", "technique": "XRD:CXD (was BCDI)", "cue": "micrograph", "ruling": "false cue; citation restored (see cue_overrides)"}
- {"node": "o6", "panel": "10.1016/j.actamat.2014.06.008#F6c", "technique": "XRD:CXD", "cue": "micrograph", "ruling": "false cue; citation added (see cue_overrides)"}

## Cue overrides

- {"node": "o11", "panel": "10.1016/j.actamat.2014.06.008#F6c", "cue": "micrograph", "why": "crop is the 240 C xz/xy phase-map panel, the peak of the x-heterogeneity the node reads; the scale-bar detector fired on the colour bar. Staff had dropped it"}
- {"node": "o6", "panel": "10.1016/j.actamat.2014.06.008#F6c", "cue": "micrograph", "why": "same crop; node claims uniform phase along z at every temperature, and 240 C is one of them"}

## Source / requires_unseen changes

- {"node": "o14", "from": "figure", "to": "text", "requires_unseen": ["Lab cycle = average over many (111) grains, Syn cycles = the single grain (caption)"]}
- {"node": "a15", "from": "figure", "to": "text", "requires_unseen": ["Lab cycle = film average over many (111) grains (caption)"]}

## Mode changes

- none

## MatMech comparison (read after the graph was final; graph not edited)

Tally: supports 1, contradicts 0, not covered 2.

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | PVD + 30 s flame anneal at 800-900 C | columnar grains, in-plane size 0.3-3 um | not_covered | a7, a8, a9 | columnar shape is a9 (evidenced by o1) but the graph has no a8 -> a9 produces edge and no grain-size node; a9 serves only the grain-location method |
| M2 | columnar grains with varying in-plane orientation | in-plane strain heterogeneity, mainly y, growing along x on heating | supports | a8, a11, a12, a14, a13, a16 | graph is more specific: residual y-heterogeneity from deposition/anneal (a11), x-growth caused jointly by thermal strain and misoriented neighbours g3/g6 (a14), biaxial-modulus alternative ruled out (a20) |
| M3 | in-plane strain heterogeneity | mechanical behaviour under thermal cycling; average strain -0.05% -> -0.35% | not_covered | a13, a15, a16 | graph explains both a13 and a15 by a16 but has no a13 -> a15 link. MatMech's -0.35% disagrees with F4a, where the lowest single-grain strain is about -0.18% (record defect) |
