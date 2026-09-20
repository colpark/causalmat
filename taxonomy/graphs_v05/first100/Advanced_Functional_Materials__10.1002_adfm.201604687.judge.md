# Judge review — Advanced_Functional_Materials/10.1002_adfm.201604687 (rank 22)

*Biomass Organs Control the Porosity of Their Pyrolyzed Carbon*

**Verdict: approved with changes.** One panel check **overturned**.

## Round-4 checklist

- **Spine.** 17 nodes. HYP(need, gap) → hypothesis → DES(base, sweep, **route with `purpose: decouple`**) → PRC(wash/freeze-dry → pyrolyse) → STR(organ chemistry, inherited architecture, porosity, **washed-control porosity**) → MEC(in-situ alkali activation) → PRP(capacitance) → PRF(rate and cycling) → STR(cross-species repeat) → DSC/conclusion. The shape is right for what this paper is: a decoupling argument in which the HCl-washed control branch (w6 → w12) is what turns an organ/porosity correlation into a causal claim. `DES/route` with `purpose: decouple` is ruling #27 applied exactly as intended.
- **Evidence.** Every spine STR/PRP/PRF/MEC claim has an incoming `evidences` edge; none needs a `basis` escape. w12 is correctly flagged `role: control branch` and joined to w11 by `contrasts`.
- **Types.** w10 `shape` (inherited architecture) vs w11/w12/w16 `porosity` (void amount and connectivity) follows the r04 shape/porosity rule. w14 is `PRP/value` rather than `PRF/figure_of_merit`: specific capacitance here is argued from structure as a level, not used as a ranking convention — the right side of ruling #11.
- **mm_ops.** `read_distribution_statistics` on x7 is the correct op for a pore-size distribution, `recognize_signature` on x11 for reading rectangularity as double-layer behaviour, and `correlate_across_series` on a2 respects its correlational-only licence.
- **Audits.** Were 7, now **5** after the change below — at budget. The division of labour is good: a2 and lim1 bound the weakest half of the argument (porosity → capacitance), and alt1 is a properly stated alternative that x5 rules out with a real measurement (I_D/I_G 1.193 vs 1.174) rather than by assertion.

## Panel checks (crops opened)

Ruling criterion used throughout this batch: **overturned** when the cited panel does not show the node's claim *as stated* — a wrong panel, or a reading the panel contradicts; **confirmed** when the panel shows the claim, even if a number or a word needed tightening.

| node | panel_ids | ruling | finding |
|---|---|---|---|
| a1 | `#F1e`, `#F5d`, `#F6d` | **OVERTURNED** | The three cited panels are the right ICP panels, but **F1e does not show the claim as stated**. In lotus, Al (0.044 vs 0.037 g/100 g) and Fe (0.019 vs 0.014) are higher in the **stem**, as are Na and Cu. Only Ca and Mg invert in all three species. Celery (F5d) and asparagus lettuce (F6d) do behave as the node claimed. No other panel would support the original claim, so there is no `correct_id`; the node has been corrected instead. |
| x7 | `#F3b` | **confirmed** | Exactly right, and it is the load-bearing panel of the paper. S-carbon peaks at ~0.9 nm (1.2 cm³ nm⁻¹ g⁻¹), ~1.6 nm (0.3) and ~3.4 nm (0.3); L-carbon at ~0.95 nm (0.65) with a weak ~3.3 nm hump (~0.09); WS and WL show only the ~0.85 nm peak and **nothing above ~1.5 nm**. Leaching does remove the mesopore population outright, and the caption never says so. |
| a2 | `#F4c`, `#F5e`, `#F5g`, `#F6e`, `#F6g` | **confirmed** | F5e gives CS 1240 m²/g and CL ~330 at 800 °C; F5g gives CS ~157 F/g and CL ~132 at the lowest scan rate. A near four-fold area difference moves the capacitance by ~16%, which is what the audit claims. |

One extra check: **x13** (`#F5d`, `#F5e`) confirmed — F5e reads CS-carbon 1240 / 1225 / 1750 / **2115** m²/g at 800–1100 °C and CL-carbon 330–570, so the node's flag that the text quotes ~2200 for a bar that reads ~2115 is right.

No invented panel_id: all 21 cited ids appear in the packet's panel section. The 13 uncited panels are photographs, schematics, the XRD/XPS panels, the celery/asparagus micrographs and the single-rate CVs — all off the argument or duplicated by a cited panel.

## Changes made

1. **a1 — the overturned audit.** Label rewritten to *"Across all three plants only K and the total metal are higher in the stem; Ca and Mg are always higher in the leaf, and Al and Fe only in celery and asparagus lettuce"*; `image_support` lowered **shown → partial**; `image_note` now gives the per-species reading including the lotus counter-examples. The audit's conclusion — that the paper's "alkali **or alkaline earth**" framing of the activation holds only for the alkali — survives, now carried by Ca and Mg alone.
2. **x6, x7, x10, x14** — `provenance: derived` → **`measured`**. Each reads a quantity the instrument or the paper reduced from data in the same panel (BET area, DFT pore-size distribution, specific capacitance), but none has an OBS parent in this graph, and v04 requires an incoming `derives` edge for `derived`. Each `image_note` now names the reduction.
3. **x7 and x9** — `attrs.text_silent` removed. Both are primary evidence nodes with `evidences` edges into spine claims; the protocol reserves `text_silent` for content that earns **a node of its own** and otherwise sends it to `image_note`, which is where it now sits, verbatim. This also brings the audit ring from 7 to 5.

## Packet panel section

Nothing wrong: 34 panels across six figures, all tier A, all letters agreeing with OCR where OCR read one. The `definition` fields are sentence fragments carved out of long multi-panel captions (`#F1c` = *"a leaf, and"*, `#F2b` = *"S-carbon and"*), which is a known consequence of splitting a running caption and does not mislead — each fragment still lands on the right panel, and the graph's `panel_conditions` entries reconstruct the condition correctly.

**Text/figure conflict recorded in the graph and confirmed here:** the paper quotes ~2200 m²/g for the 1100 °C celery stem carbon where F5e reads ~2115. This flows into `dcw1` ("the highest reported for biomass carbonization"), which is therefore stated against a number the figure does not quite give. x13's `image_note` carries it.
