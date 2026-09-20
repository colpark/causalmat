# Judge review — Advanced_Composites_and_Hybrid_Materials/s42114-021-00366-2 (rank 20)

*High-temperature-resistant barium strontium titanate @Ag/poly(arylene ether nitrile) composites with enhanced dielectric performance and high mechanical strength*

**Verdict: approved with changes.**

## Round-4 checklist

- **Spine.** 20 nodes — at the ceiling, but every one earns its place. HYP(need, gap) → hypothesis → DES(base, modification, sweep) → PRC(hydroxylation/silanisation → Ag reduction → casting, a clean `feeds_into` chain) → STR(bonding, shape, interface) → PRP(permittivity, loss, Tg, tensile) → MEC(Coulomb-blockade pathway, plasticisation trade-off) → PRF → DSC/conclusion. Two property branches (dielectric, thermo-mechanical) meeting at t19.
- **Evidence.** Every spine STR/PRP/PRF claim has an incoming `evidences` edge. t17 carries `basis: argued` — correct, since the Coulomb blockade is imported from k2 and never measured. t18, by contrast, is `evidenced` and is genuinely carried by u10 through t15.
- **t18 is the best thing in this graph.** The `MEC/tradeoff` is the paper's own unstated cost: the MPTMS that buys compatibility drops Tg by 20–30 °C, and the permittivity knee in F6c sits at that lowered Tg. Typing it as `tradeoff` rather than `pathway` is right by ruling #4's logic — a net outcome explained by one contribution outweighing an opposing one.
- **Types.** t11 `STR/microstructure/shape` (core–shell geometry of a built unit) vs t12 `STR/interface` (contact state with the matrix) follows the r04 shape/interface and distribution/interface rules. t19 `PRF/service_capability` rather than `qualification` is right: no external spec is applied.
- **mm_ops.** `compare_with_reference_value` on u7 → dcp1 is correct — the earlier CCTO/PAEN composite is a quoted benchmark value, not a co-plotted curve.
- **Audits.** 3 plus a `DSC/limitation` and a `DSC/comparison`. The paper's other soft spots are kept on `image_support` rather than made into nodes (u8 `partial`, u12 `partial`, u4 `partial`), which is the right allocation under the audit budget.

## Panel checks (crops opened)

Ruling criterion used throughout this batch: **overturned** when the cited panel does not show the node's claim *as stated* — a wrong panel, or a reading the panel contradicts; **confirmed** when the panel shows the claim, even if a number or a word needed tightening.

| node | panel_ids | ruling | finding |
|---|---|---|---|
| a1 | `#F3a`, `#F3e` | **confirmed** | The strongest audit in the paper, and exactly right. F3a (unmodified BST) already shows bright rounded ~70 nm particles among the darker ones; F3e (5% Ag) is a rougher, more agglomerated mass with **no discrete decorating nanoparticles**. At 500 nm per bar an Ag decoration cannot be separated from surface roughening, so the core–shell claim does rest on FTIR, the colour ladder and the size statistics, as the node says. |
| a3 | `#F6b` | **confirmed** | The 1% curve turns up from ~0.018 at 200 kHz to **~0.065 at 1 MHz** while the 3 and 5% curves stay at 0.013–0.015. The loss ordering really does reverse at high frequency, against the paper's Ag-content ordering. u8's 100 Hz values (PAEN 0.024, 1% 0.032, 3% 0.037, 5% 0.038) also check out, as does its point that "less than 0.026" holds only near 1 kHz. |
| u9 | `#F6c` | **confirmed** | Right panel and the trend is there; the reading was too generous about flatness (see changes). The "~45% above room temperature by 140 °C" and "~20 at 180 °C" figures are right. |

One extra check: **u6** (`#F4a`–`#F4c`) confirmed — F4c (1% Ag) is a near-featureless fracture surface with **no filler visible at all**, which for a 30 wt% film does point to field selection, as the `image_note` says.

No invented panel_id: all 20 cited ids appear in the packet's panel section. The three uncited panels are the synthesis scheme (`#F1`, tier B whole figure), one fracture panel (`#F4f`) and one dielectric panel (`#F6d`).

## Changes made

1. **u9** — "flat to about 130 °C" overstated the panel. F6c shows a **~20% rise** (5.2 → 6.3) between 25 and 130 °C before the knee, and the knee sits at **~130–135 °C**. Label and `image_note` corrected; `image_support` stays `partial`.
2. **t19** — the spine claim inherited that overstatement ("hold their permittivity … up to roughly 130–140 °C"). Restated as "hold their permittivity **within about 20%** … up to roughly **130 °C**", which is what the panel supports. Nothing else in the spine changes: t18 already carries the reason the ceiling is where it is.
3. **a2** — the label asserted that particles had "pulled out". At the 1 µm bar of F4d/F4e the cavities cannot be told from ordinary fracture relief. The audit now claims protrusions and cavities, with their origin explicitly left open in `image_note`. The point against t12 is unaffected.

## Packet panel section

Nothing wrong. Letters, tiers and crops all check out, including the one OCR disagreement (`#F2b` read as "q", where the detector's "b" is right). F1 is correctly offered as a tier B whole figure — it is the synthesis scheme and has no readable sub-panels.

No summary/figure conflicts of the r04 §5 kind were found here: the graph takes its numbers from the panels rather than from Table S1 or the MatMech block, and the two places where the *paper's own text* disagrees with its figures (the 0.026 loss ceiling and the 140 °C stability limit) are recorded on u8 and u9 rather than propagated into the spine.
