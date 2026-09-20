# Judge review — Journal_of_Magnesium_and_Alloys/j.jma.2015.01.001 (rank 8)

**Verdict: approved with changes.**

Stir-cast AZ91–SiCp composites. Two branches leave one structure state: a room-temperature branch (t10 yield, t11 compressive, t12 tensile, t13 fracture mode) and a creep branch (t15 → t16 → t17 → t18), meeting at the conclusion. 19 spine nodes, one connected path t1 → t19, no orphan claims. The graph is honest about the paper's inconvenient result: t12 (UTS does *not* benefit) is on the spine and `qualifies` the conclusion, rather than being dropped. The diagnostic chain required by v04 is complete and correctly typed: `PRP/diagnostic` t16 → `KNW/lookup` v3 → `MEC/identification` t17, and u9/u10/u11 are derived OBS with `derives` edges from u8.

## Changes

1. **u2** — `image_support` lowered from `shown` to `partial`, the label softened from "no resolved grain boundaries" to "boundaries too faint to follow", and the `image_note` extended. F1c does keep faint discontinuous bright lines between the dark particles; they are too indistinct to size grains, which is what the t21 audit needs, but "no boundaries at all" overstated the panel.
2. **u5** — `image_note` corrected: the F3 ordinate runs 80–220 MPa, not 100–220.

## Panel checks

| node | panel_ids | ruling |
|---|---|---|
| u2 | `#F1a`, `#F1c` | **confirmed** (support adjusted) |
| u5 | `#F3` | **confirmed** |
| u10 | `#F7b` | **confirmed** |

- **u2 → F1a/F1c.** Both crops opened at their 200 µm bars. F1a resolves the light matrix with its dark boundary network cleanly; F1c is dominated by dark particle contrast with only faint bright lines. The cited panels are right and the audit holds — the quoted 34/22/21 µm matrix grain sizes cannot be read from this figure — but the statement needed softening, as above.
- **u5 → F3.** YS bars 93, 113, 124, 127, 136, 143 MPa and UTS bars 188, ~183, ~183, 182, 181, 174 MPa across 0–25 wt%, exactly as the node states. The UTS decline exceeds the error bars only at 25 wt%, which the note already says.
- **u10 → F7b.** The legend prints n_t = 5.4, 5.5, 5.6, 5.8, 5.6, 5.7 and the six lines very nearly merge on the effective-stress abscissa. `collapse_by_normalization` is the right op here (the merge *is* the evidence, per the r04 #9 ruling), and the note is right that the threshold stresses setting the abscissa are tabulated rather than plotted — which is precisely the op's own audit.

All 14 panel_ids used appear in the packet.

## Audits

Six audit nodes by the derived-ring count (t21–t24 plus the OBS u2 and u11) — one over the soft budget of five, but none is redundant and each bounds a different spine claim: t21 with u2 → grain size t8; t22 → particle distribution t7; t23 → both the clean-interface claim t9 and the fracture-mode claim t13, by naming the ×1500 and ×150 magnifications at which neither a sub-micron reaction layer nor dimples can be resolved; t24 with u11 → the diagnostic t16 (apparent exponents non-monotonic in SiCp content, each from a three-point fit). Since t23 already carries two targets in one node, collapsing further would lose a distinct claim, so the count was left as it is. The contradiction/limitation distinction is drawn correctly: only t22 and t24 are `kind: anomaly`.

## What the packet got wrong

- **Figure 6 is tier C (`C3_caption_swap`) and offers no panels**; the graph does not cite it, which is right.
- F1 is tier B (`B1_caption_empty`): F1b, F1c and F1e have empty `definition` strings, so the panel-to-composition mapping (5, 10, 15, 20, 25 wt%) comes from the panel order alone. It is consistent with the images, but nothing in the packet confirms it.
- OCR renders the burnt-in bars as "108Mm" (F2a, actually 100 µm at ×150), "10Mm" (F2b, 10 µm at ×1500) and "100Mm" (F5a/F5b); the staff read the banners from the images instead, as they should.
- F7a and F7b are detector-only with no OCR letter, but their legends (n = 7.2/7.4/7.7 and n_t = 5.4/5.5/5.6) identify them unambiguously.
