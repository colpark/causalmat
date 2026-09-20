# Judge review — Bioactive_Materials/j.bioactmat.2019.01.001 (rank 19)

*In vitro degradation and biocompatibility evaluation of typical biodegradable metals (Mg/Zn/Fe) for the application of tracheobronchial stenosis*

**Verdict: approved with changes.**

## Round-4 checklist

- **Spine.** 17 nodes. HYP(need, gap) → hypothesis → DES(base, sweep, **method**) → PRC(disk prep → immersion) → STR(corrosion-layer composition, damage extent) → PRP(corrosion rate, E/i_corr, A549 viability) → MEC(medium chemistry, ion dose) → PRF(stent suitability) → DSC/conclusion. One immersion branch and one cell branch meeting at b17 — the allowed two-branch shape.
- **b6 on the spine is correct.** `DES/method` (Gamble's solution + A549) belongs on the spine under ruling #33's sibling rule: this is a screening paper whose headline contribution *is* the test system, and b6 `realizes` the immersion that makes the rate measurable. Its being the paper's methodological move is stated in `attrs.note`.
- **Evidence.** Every spine STR/PRP claim has an incoming `evidences` edge. b17 carries `basis: argued` — right, since stent suitability is inferred, never tested. b15 and b16 are `basis: evidenced` and are indeed carried by c10 and c9 respectively.
- **Types.** b9 `STR/chemistry/composition` with `scope: corrosion product layer` vs b10 `STR/microstructure/damage` is the right split (what the layer is made of vs loss of continuity). b13 `PRP/value` with `property_family: biological` rather than a PRF node is right — viability is a property readout, and the use-condition claim is b17.
- **mm_ops.** All well chosen. `assign_features` for the FTIR band assignment (c6) and `read_characteristic_point` for the single ICP levels (c9) follow the r04 trend/characteristic-value rule.
- **Audits.** 2 audits (a1, a2) plus one `DSC/limitation` and one `DSC/comparison` — inside budget. The pH reading that would embarrass the mechanism (c10: GS ends *below* SBF) is kept on the evidence node instead of being spun into a third audit, which is the right call.

## Panel checks (crops opened)

Ruling criterion used throughout this batch: **overturned** when the cited panel does not show the node's claim *as stated* — a wrong panel, or a reading the panel contradicts; **confirmed** when the panel shows the claim, even if a number or a word needed tightening.

| node | panel_ids | ruling | finding |
|---|---|---|---|
| c8 | `#F6b` | **confirmed** | Day-5 bars measured: HP-Mg-DC 2.32, HP-Zn-DC 2.2, HP-Mg-EC 2.5, negative control 2.58, P-Fe-IC 0.45, P-Fe-EC 0.9 — the node's numbers exactly. Its `image_note` is right too: **HP-Mg-IC reaches 3.32**, well above the negative control, which the text passes over as "similar". |
| c10 | `#F4a`, `#F4b`, `#F4c` | **confirmed** | F4a (HP-Mg): GS starts at 8.4 on day 1 and settles to 7.0–7.1 by day 27; SBF starts 7.75 and holds 7.3–7.5. The ordinate runs to 10.0 but no trace exceeds 8.5. Both of the node's load-bearing readings — "no trace above 8.5" and "GS ends below SBF" — check out, and they matter: b15 cannot lean on GS being the more alkaline medium at late times. |
| a1 | `#F2a`, `#F2b` | **confirmed** | Panel ids are right. F2 is a 2×3 grid, rows HP-Mg / HP-Zn / P-Fe, GS left and SBF right, so HP-Zn-SBF is panel **D** in both the 7 d and the 14 d figure and citing both is the correct way to carry a before/after audit. The reading needed tempering (see changes); the audit itself holds. |

One extra check: **c3** (`#F2a`) confirmed — HP-Mg-GS (A) shows discrete dark pits on a still-ground surface, HP-Mg-SBF (B) a continuous cracked layer, and the only 10 µm inset is on the HP-Mg-GS panel, exactly as the `image_note` says.

No invented panel_id: all 13 cited ids appear in the packet's panel section. The single uncited panel (`#F6a`) is the culture-mode schematic.

## Changes made

1. **c7** and **a2** — `provenance: derived` → **`measured`**. Both read the F3c weight-loss corrosion rate (P_w). The input weight losses are not OBS nodes in this graph, and v04 requires an incoming `derives` edge for `derived` (83/83 derived nodes in r01–r04 have one). Both `image_note`s now state the reduction.
2. **a1** — the label overstated the audit as "broad continuous dark patches over much of the field". F2b panel D shows a **branching, connected network of dark streaks** over most of the 500 µm field — distributed, not solid coverage. Label and `image_note` rewritten so the audit says what the panel shows. The point against b10 ("HP-Zn stays largely localised") is unaffected: at 7 d the same panel really is a handful of separate spots, at 14 d it is not.

## Packet panel section

Letters, tiers and crops are correct, including the "detector only" letters on F1a, F2a, F4a, F4b and F6c.

**Two record defects, both correctly caught by the staff graph and confirmed here:**

- **Packet F4's caption is corrupted.** It reads *"Fig. 1 summarized the electrochemical results obtained from the electrochemical tests in GS or SBF. By the PDP curves (Fig. 1(a) and Fig. 4. The pH of immersion solution change curves of (a) HP-Mg, (b) HP-Zn and (c) P-Fe in immersion period."* — a fragment of the Fig. 1 discussion concatenated onto the Fig. 4 caption. The corruption propagates into the panel section, where `#F4a`'s `definition` is the nonsense string *"and Fig. 4. The pH of immersion solution change curves of HP-Mg"*. The image itself is the right one (paper Fig. 4a, HP-Mg pH) and the panel letters are right, so only the `definition` text is affected. This is the same defect class as the r04 §5 entry for `Biomaterials (02)00177-1`.
- **Packet F5 is tier C (`C3_caption_swap`) with no panels offered.** It was not opened, so the paper's cell-morphology evidence (SEM + fluorescence of A549) is carried only through the CCK-8 node c8. The graph records this in `notes` and it is the right call — an unopened figure gets `figs: []`, not a caption-derived `image_support`.
