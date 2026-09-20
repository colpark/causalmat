# Judge review — Progress_in_Organic_Coatings/j.porgcoat.2016.09.010 (rank 18)

*Effects of combined surface treatments of aluminium nanoparticle on its corrosion resistance before and after inclusion into an epoxy coating*

**Verdict: approved with changes.**

## Round-4 checklist

- **Spine.** 18 nodes. HYP(need, gap) → hypothesis → DES(base, modification, sweep) → PRC(Ce conversion → APTES graft → dispersion into epoxy, a proper `feeds_into` chain) → STR(surface composition, Si-O-Al bonding, dispersion in the cured film) → PRP(particle H₂ evolution, coating |Z|, wet adhesion) → PRF(salt spray) → MEC → DSC/conclusion. The two-level shape is the paper's own argument — the treatment is validated first on the particle (s10/s11 → s12) and then in the coating (s13 → s14/s15 → s16) — and stays within the two-branch budget.
- **Evidence.** Every spine STR/PRP/PRF claim has an incoming `evidences` edge. s17 (`basis: evidenced`) is carried by q9, the phase-angle reading, which is the right evidence for "one capacitive time constant, no exposed substrate".
- **Types.** s10 as `STR/chemistry/composition` with `scope: surface layer` and s11 as `STR/chemistry/bonding` follows the composition/bonding split correctly. s16 as `PRF/service_capability` rather than `qualification` is right — ASTM B117 is the test condition, not a pass/fail threshold, so it belongs in `attrs.condition` exactly as ruling #36 says. s7 carrying `aspect: conversion` on `PRC/deposition` is ruling #20.
- **mm_ops.** `fit_model` with `form: decomposition` on q1/q2 is the intended use for XPS deconvolution. `cross_check_consistency` with `aspect: outlier` on a3 is the merged flag_outlier use.
- **Audits.** 4 (a1, a2, a3, lim1) plus q2's `contradicts`. All three kinds are kept apart properly: **figure contradicts text** for q2 (O 1s intensity ordering) and a2 (the claimed 140 min hydrogen latency); **figure does not resolve it** for a1 (no Ce 3d above noise); **within scatter** for a3.

## Panel checks (crops opened)

Ruling criterion used throughout this batch: **overturned** when the cited panel does not show the node's claim *as stated* — a wrong panel, or a reading the panel contradicts; **confirmed** when the panel shows the claim, even if a number or a word needed tightening.

| node | panel_ids | ruling | finding |
|---|---|---|---|
| q2 | `#F2c` | **confirmed** | F2c is the O 1s deconvolution and carries exactly the four assignments listed. Component peak heights measured: CeO₂ ~100, Ce₂O₃ ~285, Al–O ~380, Ce–OH ~250. The contradiction is real — Ce₂O₃ alone exceeds Ce–OH — so `image_support: contradicts` stands. |
| a1 | `#F2a` | **confirmed** | F2a is the survey with the dashed Ce 3d circle. The 820–880 eV enlargement it points to is flat scatter, ~1150–1280 counts, with no resolvable doublet. The audit holds. |
| q4 | `#F6b` | **confirmed** | F6b (paper Fig. 7b, MEK) plots **Al as a reference series** alongside Si-Al-1/2/3 and Si-Ce-Al, so the node's claim about untreated Al is readable from this panel. Al runs 3750 → 1280 NTU over 60 min; the silanised series start at 1400–2000 and end at 400–600. The node's numbers and its caveat about differing starting dispersions both check out. |

Two extra checks: **q8** (`#F10c`) confirmed — S2 (diamond) and S4 (square) sit on top of one another at ~10^10.4 at the lowest plotted frequency, S3 ~10^6.9, blank ~10^4.5, so the node's flag against the MatMech block is right; **q1** (`#F2b`) confirmed — Al₂O₃ at 75.4 eV (~17 counts) and Al at 78.2 eV (~72), metal component larger, as stated.

No invented panel_id: all 16 cited ids appear in the packet's panel section. The 11 uncited panels are the EDS pH screen (F1), the as-received particle SEM (F3), the butyl-acetate turbidity duplicate (F5), the Ce-Al MEK panel (F6a), the pull-off surface morphologies (F11) and one salt-spray panel (F9b) — all off the spine.

## Changes made

1. **q10** — `provenance: derived` → **`measured`**. The bars are the paper's own Eq. (8) reduction of dry and wet pull-off strength, but neither strength is an OBS node here, and v04 requires an incoming `derives` edge for `derived` (83/83 derived nodes in r01–r04 have one). The reduction stays visible through `k3 premise_for q10` and is now stated in `image_note`.
2. **q2** — `image_note` replaced with the measured component heights, which is what actually carries `image_support: contradicts`. It also records a figure defect: the 530 eV component is labelled **"Ce₂O"** in the panel, a typo for Ce₂O₃.
3. **a1** — `image_note` now states that the Ce 3d enlargement lies **outside the `#F2a` crop** and is visible only in the whole-figure image. A reader given the crop alone cannot check this audit.
4. **q8** — `image_note` sharpened with the overlap point and with S1's last-point drop to ~10^6.0 against its ~10^6.8 plateau.

## Packet panel section

Panels, letters and tiers are correct, including the three OCR disagreements (`#F2b` read as "q", `#F9b` and `#F11b` as "m", `#F11c` as "s"); in each case the detector letter is right and the OCR is reading a neighbouring glyph. F7 is honestly declared tier C with no panels, and the graph correctly gives its two nodes `panel_ids: []`.

**One real gap, now recorded:** the Ce 3d enlargement of Fig. 2 is a genuine sub-panel of the figure but the store offers no id for it, and it falls outside the `#F2a` crop. Any audit that rests on it (a1, and through it lim1) is uncheckable from the crops alone.

**Record defect, correctly caught by the staff graph and confirmed here:** the packet's figure ids run **one behind the paper from F4 onward** — packet F4 carries the paper's Fig. 5, and so on to packet F12 = paper Fig. 13. The paper's Fig. 4 is absent from the record. The captions in the packet say so verbatim while the ids do not. Panel ids follow the packet, which is the right convention.

**Upstream summary conflict:** the MatMech block credits S4 alone with >10^10 Ω cm², where F10c puts S2 on the same curve. Recorded in q8's `image_note`. (This is the same paper family as the r04 §5 entry for `porgcoat.2013.10.008`.)
