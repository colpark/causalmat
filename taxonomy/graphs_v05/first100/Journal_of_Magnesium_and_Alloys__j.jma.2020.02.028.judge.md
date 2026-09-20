# Judge review — Journal_of_Magnesium_and_Alloys/j.jma.2020.02.028 (rank 6)

**Verdict: approved with changes.**

Variable-temperature 160° ECAP plus a short electropulse on AZ61. Screen-then-choose process paper: the single-temperature ECAP trials (n7a → n11) feed the mechanism n10 that motivates the down-select n9, and the spine then runs ECAP → stored dislocations → electropulse → ultrafine grains and weak texture → strength and ductility, closed by the trade-off n18 with a `counteracts` edge from the lost dislocation strengthening n27. 20 spine nodes — at the ceiling, but the extra length is earned by the screening branch the paper's argument depends on. One connected path n1 → n21; every spine STR/PRP/PRF claim is evidenced or carries `basis: argued`.

## Changes

1. **o9** — type changed from `OBS/morphology/feature_metric` to `OBS/response/distribution`, and the mm_op on `o9 → n15` from `measure_feature_metric` to `read_distribution_statistics`. F11b/F11d are misorientation-angle histograms: the spread of a non-imaged quantity over the boundary ensemble, read from a plotted distribution, not a metric measured on imaged features. The v04 sibling rule ("read from a plotted quantity vs variable → response") applies. Panel ids, modality (`xy_curve`, correct for a bar chart), image_support and the reading itself are unchanged. Verified against F11b before the change: a spike of 0.155 frequency below 3° plus a broad band peaking near 30°.

## Panel checks

| node | panel_ids | ruling |
|---|---|---|
| o5 | `#F10a`, `#F10d` | **confirmed** |
| o7 | `#F11a`, `#F11c` | **confirmed** |
| o8 | `#F11a`, `#F11c` | **confirmed** |
| o10 | `#F13` | **confirmed** |

- **o5 → F10a/F10d.** Both crops opened at their 2 µm bars. F10d shows fine elongated lath-like features aligned in one direction, close in character to the deformed F10a and unlike the equiaxed panels between them. The text reads F10d as uniform ultrafine equiaxed grains of ~1 µm, so n23 is a real *figure contradicts text* audit, not a resolution complaint.
- **o7 → F11a.** The panel holds the (0001) pole figure and the IPF map side by side; the map shows densely packed equiaxed grains of ~1–2 µm against its 5 µm bar. Splitting the `spatial_map` reading (o7) from the `orientation_distribution` reading (o8) on the same panel id is the correct handling of a panel that holds two panel kinds.
- **o8 → F11a.** `Max = 3.85` is printed under the pole figure and the density maximum sits off-centre toward TD, as claimed. The panel carries no as-received or as-ECAPed pole figure, which independently confirms the n24 audit.
- **o10 → F13.** The 423K-8 + 373K-3 + 25 µs-10 min curve yields near 330 MPa, peaks at ~448 MPa and ends at true strain ~0.148, above the other two (peaks ~370 MPa at 0.17 and ~357 MPa at 0.195). Every number in the node is on the panel.

All 18 panel_ids used appear in the packet.

## Audits

Five, at budget, each bounding a different spine claim: n22 (sub-2 µm grain claims rest on optical panels that cannot resolve them) and n23 with OBS o5 both qualify the grain-size claim n14; n24 qualifies the texture claim n15; the n25 contrast branch sets the 89 µm starting state against it. n23 is a contradiction and is labelled `kind: anomaly`; n22 and n24 are not-resolved findings and are labelled `kind: method`. The distinction is drawn correctly in every case.

## What the packet got wrong

- The OCR cue line for F11 **mistakes the 4.57 mrd pole-figure maximum for a "4.57 µm scale bar"** (the staff flagged this; confirmed). F11c is detector-only with no OCR letter.
- The panel `definition` spans for F10 and F11 are pulse-parameter fragments ("30 µs–5 min sample", "25 µs–10 min sample") that identify the panels correctly here.
- F13 and F14 are tier-B whole-figure records, cited as single ids, which is right.
