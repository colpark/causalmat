# Judge review: Acta_Materialia__10.1016_j.actamat.2014.06.008

**Judge:** senior investigator  
**Verdict:** accept with minor edits

## Round-4 checklist

- **spine**: 12 spine nodes, connected: gap a1 -> method a2 / Au film a3 / thermal sweep a4 -> stimulus a5 -> initial strain a7, mean strain a8, defects a10 -> inhomogeneous strain a9 -> plastic relaxation a11 <- mechanism a12 -> conclusion a15; reads as the paper's argument
- **evidence**: a7 (o3b, o8b), a8 (o5, o7a), a9 (o6, o7b), a10 (o8a, basis argued), a11 (o5), a12 basis argued with a13 and k2; all spine claims backed or flagged
- **v04 rules**: model-vs-data pattern as OBS/signal/reference_match with overlay_model_on_data (model reference) correct; DES/method on spine realizing a7 is allowed (headline method); o7a->o10 convert_to_quantity via=position correct
- **mm_ops**: all name the figure act
- **audits**: 2 audit OBS (o10 open first loop; o11 black width markers do not widen, against caption and F4b) plus DSC/comparison a14; fair and bearing on a8/a9

## Changes

- o8a, o8b: F6c restored to panel_ids (false 'micrograph' cue on a phase-retrieval map; recorded in cue_overrides)
- o8b: image_support shown -> partial; the 240 C xy map is visibly more fragmented, so 'changes little' is only loosely true
- o3a: technique ATOM -> CALC:kinematic (the crop is a kinematic Fourier-transform calculation from the grain shape, not an atomistic simulation)
- o9, a13: projected <110> angles re-measured on F7c; g6 and g3 are each ~20 deg off g1 (was g6 ~15, g3 ~35)
- o11: image_note crop letters corrected to the cited crops

## Panel checks (every cited crop opened)

| node | panel ids | ruling | correct id | note |
|---|---|---|---|---|
| a4 | F4a | confirmed |  | three strain-temperature cycles with temperature axis |
| a5 | F5a, F5c, F5e | confirmed |  | T_u=50, 240 C and T_d=50 C written on the maps |
| a13 | F7c | confirmed |  | right panel; angles re-measured (g6 ~19 deg, g3 ~19 deg off g1), label corrected |
| o1a | F1a | confirmed |  | BSE plan view of the FIB-isolated square, equiaxed grains |
| o1a | F1b | confirmed |  | cross-section, 0.372 um film, boundaries through thickness |
| o1b | F1d | confirmed |  | EBSD map mostly blue, few red/orange grains |
| o2 | F1c | confirmed |  | pole figure, circled isolated spot at ~(13.05, -0.45 deg) |
| o4 | F2b | confirmed |  | outlined grain ~1.1 x 0.9 um against 500 nm bar |
| o3a | F3a | confirmed |  | computed 3-D isosurface, symmetric with fringe streak |
| o3a | F3b | confirmed |  | computed qz-qx slice with regular fringes |
| o3a | F3c | confirmed |  | computed qx-qy slice with straight facet streaks |
| o3b | F3d | confirmed |  | measured 3-D isosurface, asymmetric |
| o3b | F3e | confirmed |  | measured qz-qx slice, T=35 C |
| o3b | F3f | confirmed |  | measured qx-qy slice, smeared along qy |
| o5 | F4a | confirmed |  | values match; thermoelastic line steeper than all loops |
| o10 | F4a | confirmed |  | green curve -0.057 at ~20 C to -0.167 at ~20 C after cycle |
| o6 | F4b | confirmed |  | 1.3 -> 4.9 on heating, ~1.95 at end of cooling |
| o7a | F5a, F5b, F5c, F5d, F5e | confirmed |  | peak centre 0, ~-5, ~-10, ~-3, ~+2.5 x10^-3 A^-1 relative to red bar |
| o7b | F5a, F5b, F5c, F5d, F5e | confirmed |  | red core widens along qx at 240 C; partial recovery at 50 C |
| o11 | F5a, F5c, F5e | confirmed |  | black marker pairs keep ~3 x10^-3 A^-1 spacing and shift down |
| o8a | F6a, F6b, F6d, F6e | confirmed |  | xz maps: bands uniform along z, jumps along x grow on heating |
| o8a | F6c | confirmed |  | RESTORED: 240 C xz map with the most jumps; plainly the right panel, only a false micrograph cue |
| o8b | F6a, F6b, F6d, F6e | confirmed |  | xy maps banded from 50 C |
| o8b | F6c | confirmed |  | RESTORED: 240 C xy map, more fragmented than other temperatures (image_support set to partial) |
| o9a | F7b | confirmed |  | EBSD patch with g1-g6 labelled |
| o9 | F7c | confirmed |  | arrow angles re-measured; label corrected |

Distinct crops opened: 25; node-panel rulings: 26; overturned: 0.

## Technique mismatches

- {"node": "o3a", "panels": ["10.1016/j.actamat.2014.06.008#F3a", "10.1016/j.actamat.2014.06.008#F3b", "10.1016/j.actamat.2014.06.008#F3c"], "was": "ATOM", "now": "CALC:kinematic", "kind": "technique vs crop (no OCR cue involved)", "why": "panels are the strain-free pattern computed from the grain shape (Eq. 9), not an atomistic calculation"}

## Cue overrides

- {"node": "o8a", "panel": "10.1016/j.actamat.2014.06.008#F6c", "cue": "micrograph", "why": "F6c is the 240 C xz/xy phase-retrieval map (XRD:CXD); the cue comes from 'um' axis tokens read as a scale bar. It is the peak-temperature panel the jump-count reading needs; staff had dropped it."}
- {"node": "o8b", "panel": "10.1016/j.actamat.2014.06.008#F6c", "cue": "micrograph", "why": "same crop, xy half of the 240 C phase map"}

## Source / requires_unseen changes

- none

## Mode changes

- none

## MatMech comparison (read after the graph was final; graph not edited)

Tally: supports 2, contradicts 0, not covered 1.

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | PVD then annealing at 800-900 C for 30 s | columnar grains, in-plane size 0.3-3 um | not_covered | a3, a6 | effect present (a3, a6 columnar <111> film) but no deposition/annealing node: captions give no processing, so the causal link is absent |
| M2 | columnar grain structure with varied in-plane orientation | in-plane strain heterogeneity, especially along y | supports | a7, o8b, a13, a12, a10 | partial support: graph has large initial inhomogeneous strain (a7) and banded xy phase maps (o8b), and ties heterogeneity to misoriented neighbours (a13 -> a12); it does not attribute it to columnar grain size. MatMech 'reversible along x' is weaker than the graph's growing x jumps (a10) with partial recovery |
| M3 | in-plane strain heterogeneity | mechanical behaviour under thermal cycling: deviation from thermoelastic slope, quasi-reversible strain | supports | a9, a11, a8, o5, a14 | graph: a9 supports a11 (sub-thermoelastic slope, open loop). MatMech number 'average strain -0.05% to -0.35%' disagrees with F4a (loops span ~-0.18% to +0.02%); recorded, graph not edited |
