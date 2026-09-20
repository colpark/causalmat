# Judge review — Journal_of_Advanced_Ceramics/s40145-019-0334-4 (rank 7)

**Verdict: approved with changes.**

In-situ reactive hot pressing of ZrB2–SiC with excess ZrSi2. One processing act produces four structure claims (phases, platelet shape, SiC size, density) that converge on the property pair q12/q13, with the transient-liquid growth mechanism q11 upstream of the platelet shape and the toughening mechanism q15 downstream of it. 16 spine nodes, one connected path q1 → q16, no orphan claims, every spine STR/PRP/PRF claim evidenced or `basis: argued`. q15 carries `basis: evidenced` on the strength of the arrow-labelled crack panel, which is fair given r11's own caveat.

## Changes

1. **r5** — `image_support` lowered from `shown` to `partial`, the word "elongated" dropped from the label, and the `image_note` extended. F5c does show edge-to-edge contact inside the marked box, but most grains there are angular and near-equiaxed at that magnification, so the panel supports the *interlocking* half of q8 and only weakly the *platelet* half. (q8 keeps its other evidence: r4 and r7, and r7's 500 nm-bar fracture view is where the platelet reading is actually strong.)

## Panel checks

| node | panel_ids | ruling |
|---|---|---|
| r5 | `#F5c` | **confirmed** (support adjusted) |
| r8 | `#F7` | **confirmed** |
| r9 | `#F7` | **confirmed** |
| r11 | `#F8f` | **confirmed** |

- **r5 → F5c.** The right panel: the dash-dot box labelled "Interlocking microstructure" with a 1 µm bar is there, and the grain-size distribution inside it is visibly bimodal as the note says. Correct panel; only the strength of the reading was adjusted, as above.
- **r8 → F7.** Hardness 12.6 → 17.1 → 16.0 GPa, flexural strength 505 → 655 → 568 MPa and toughness ~4.3 → ~6.05 → ~6.0 MPa·m^1/2 from RZSZ-0 through RZSZ-20 to RZSZ-25, all peaking at RZSZ-20.
- **r9 → F7** (audit claim). The toughness bars of RZSZ-20 (~5.9–6.2) and RZSZ-25 (~5.85–6.15) overlap, while the strength bars (655 ± 18 against 568 ± 20) plainly do not. The text's reported decrease in toughness at 25 vol% is not established by the panel — the node states this as an over-read, not as a refutation, which is right.
- **r11 → F8f.** Arrow labels for crack deflection, crack bridging, grain pull-out and crack branching are all on the panel, with the branching arrow at the "SiC rich region", which is what q15 needs. The node's caveat that the classification is the paper's, not read independently, is accurate and matters here.

All 14 panel_ids used appear in the packet.

## Audits

Four, changing support in both directions. q18 with OBS r2: only the uppermost of the four stacked traces in the composition XRD figure is indexed, so neither the claimed rise of the WSi2 peak nor the threshold appearance of ZrC can be read from it — a *not resolved* finding that bounds the phase claim q7. q19 with OBS r9 bounds the toughness claim q13 and, through it, the design guidance q17. Neither is dressed up as a contradiction. Budget respected.

## What the packet got wrong

- **Figure 2 is tier C (`C1_count_mismatch`) and offers no panels**, so r1 and r2 carry `figs: ["F2"]` with empty `panel_ids`. That is the correct handling, and the graph says so explicitly in both notes.
- F5's `definition` spans lag their panels ("RZSZ-15" on F5a is right, but "EDS analysis taken from" / "the zone A and" / "the zone B in" are split across F5d–f); the staff resolved zone A and zone B from the inlaid tables, and the OCR values (C 11.42 on F5e, 58.91/34.51 on F5f) confirm the assignment.
- Several F5 and F8 panels are detector-only with no OCR letter; the letter assignment nevertheless matches the caption order on the images.
