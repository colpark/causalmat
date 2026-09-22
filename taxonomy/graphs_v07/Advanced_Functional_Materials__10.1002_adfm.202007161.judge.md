# Judge review: Advanced_Functional_Materials/10.1002_adfm.202007161

Hydration-induced beta-sheet crosslinking of alpha-helical-rich spider prey-wrapping silk. Structure-only review: no figures or crops were opened, and no ruling was made on panel citations or techniques.

## Verdict
Accepted with fixes. The spine reads gap n1 -> hypothesis n2 -> base_system n3 + variable_sweep n4 -> water soak n6 -> Ala beta-sheet up n9, helices kept n10, 4-6 nm domains n11 -> fibre fusion n8 (explained by MEC n12) -> fusion on prey n14 -> conclusion n15. It has 12 connected spine nodes, down from 13. Every spine STR/PRF/MEC node now has OBS evidence or a KNW premise. There are 3 audits (a1, a4, d2), all fair.

## Changes
- n13 (PRP "stiffer, no longer malleable") was taken off the spine. It is a text-only handling remark with no OBS evidence and no KNW premise. The spine stays connected through n8 -> n14 -> n15.
- The edge n8 -causes-> n19 was rewired to n6 -causes-> n19. The fused state does not cause the fusion time; the water exposure sets it.

## Splits
- **n16 -> n16, n16b.** n16 now holds only the Ala claim: wet-shear raises Ala beta-sheet to about half. n16b holds the poly(Ser) helix 5 collapse. The o10 edge (Ser C-beta) moved to n16b. n16b also gets n7 produces, contrasts n10, supports n15, and k6 premise_for.
- **d1 -> d1, d1b.** d1 is the domain-size comparison (4-6 nm vs 11 nm). d1b is the abundance comparison (41% vs 82%), fed by n9 (supports) and k2 (premise_for).
- **k2 -> k2, k2b.** k2 is the 82% Ala beta-sheet in dragline (ref 21), now premise_for d1b. k2b is the XRD crystallite size 3.02 x 4.15 x 6.71 nm (ref 8c), now premise_for d1.

## Merges
None. No two nodes state the same claim. The o2/o3 raw/deconvolved pair and the o1c/n19 observation/claim pair each play distinct roles.

## Source / read_from changes
- source: n14 changed from figure to text. The extra-oral-digestion context comes only from caption F2b, and requires_unseen already listed it.
- read_from: no changes. o7 and o9 already read "annotation". The other OBS nodes read peak growth, coincidence or morphology from pixels, or values off an axis, rather than restating an annotation string.

## Mode changes
None. n8 is the only claim with two or more causes edges (n9, n11). It stays "joint", because no caption shows a choice between beta-sheet amount and domain size.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | moisture and mechanical shear -> beta-sheet increase, minor coiled-coil unfolding | supports | n6, n7, n9, n16, n16b, n10 |

supports 1 / contradicts 0 / not covered 0
