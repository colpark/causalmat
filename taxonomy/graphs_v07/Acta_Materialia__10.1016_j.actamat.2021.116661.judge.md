# Judge review: Acta_Materialia/10.1016_j.actamat.2021.116661

**Verdict:** accept with fixes. This was a structure-only review: no figures or crops were opened, and panel citations and techniques were not ruled on. The graph now has 45 nodes, 56 edges and 15 spine nodes (spine unchanged).

The spine is one connected path: need -> hypothesis -> Mo modification -> austenitize/quench -> H charging + SSRT. From the processing step it splits in two:
- **Segregation branch:** PAGB segregation (n7) -> cohesion MEC (n15).
- **Solute branch:** dissolved Mo (n9) -> lower D_app (n10) -> HELP-localisation MEC (n16). n9 also feeds a solute-drag MEC (n17).

n15 and n16 explain the crack path (n13). Then n13 -> fracture mode (n12) -> elongation retention (n14) -> conclusion (n18). n17 also explains n14.

Every spine STR/PRP/PRF/MEC node has OBS evidence or a KNW premise. n16 and n17 are basis=argued and have KNW premises. The solute branch forks into two MECs, which is within the paper's own three-mechanism argument, so I accept it. There is 1 audit (a1, limitation) and it is fair. No v04 violations.

## Changes
- Split o5, o14 and o15 (details below).
- Modality spatial_map -> xy_curve on o4, o5 and o7. These are APT line-profile plots, i.e. concentration vs distance.
- a1 label reworded. It now reads "deep-trap H 0.02 vs 0.01 wt ppm, small". The old "doubles" overstated a difference the paper calls not apparent.

## Splits and merges
- **o5 -> o5 + o23.** Old o5 read two panel kinds.
  - o5 keeps the F3 matrix line profile (xy_curve, axis).
  - New o23 is the F4 Mo iso-surface (volume_render, pixels), with evidences -> n9 (assess_spatial_distribution).
  - The F4 assignment follows the split. The blind second read will verify it.
- **o14 -> o14 + o21.**
  - o14 keeps breakthrough time (F8b).
  - New o21 is steady-state current (F8a), with evidences -> n10. The plateau image_note moved to o21.
- **o15 -> o15 + o22.**
  - o15 keeps D_app, with evidences -> n10.
  - New o22 is C0R (diffusible H). Edges: o21 derives o22 (convert_to_quantity, via=known_relation), and o22 evidences n16 next to o13. This is the paper's "similar charged H content" premise.
- Merges: none. No two labels state the same claim. OBS/claim pairs such as o15/n10 and o12/n19 are a readout and its claim.

## Source / read_from changes
- o16: figure -> text. That F7c is the dark-gray area of the Ref surface comes from linked text, as does 3 mA/cm2 (caption).
- o17: figure -> text. The centre/edge identity of F7g/F7h comes from linked text.
- read_from: no changes. Every OBS node that restates listed annotations is already "annotation": o1, o6b, o9, o15, o16, o17, o19, o20, and new o22. o12 and o13 are in-image inset strings on an un-OCR'd crop, which is acceptable.

## Mode changes
- None. No claim has two or more incoming causes edges. n13 has produces + explains edges, not causes.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 0.
- M1: Mo addition -> PAGB segregation of Mo, C and B. **Supports** (n3, n4 -> n7; o3, o4).
- M2: PAGB segregation -> grain-boundary cohesion. **Supports** (n7 -> n15; o17, n12).
- M3: Mo addition -> lower H diffusivity. **Supports** (n4 -> n9 -> n10; o14, o15). The Oriani/strain-field reading is not a node, and a1 flags that (Mo,Ti)C trapping is not separated.
- M4: lower diffusivity -> less ductility loss. **Supports** (n10 -> n16 -> n13 -> n12 -> n14).
