# Judge review — Acta_Materialia/10.1016_j.actamat.2015.04.055

**Carbon distribution between γ, α2 and β_o in a TNM γ-TiAl alloy, and its effect on phase hardness** (rank 12)

**Verdict: approved with changes.**

## Checklist

- **Spine.** 20 nodes. It had **two roots**: n2 (HYP/gap) and n18 (MEC/identification), because n18's only support came through n28 (PRP/diagnostic), which is off-spine. Two claim→claim `supports` edges were added (n14 and n26 into n18) — both are premises the node's own label states — and the spine is now one connected graph from n2 to n21.
- **Evidence.** Every spine STR/PRP claim has an `evidences` edge. n15, n18 and n20 carry `basis: argued`; n19 is `evidenced` through o9/o10. No orphan claims.
- **Types.** The paper's own reasoning chain is reproduced correctly and is exactly the case r04 ruling #10 kept `PRP/diagnostic` for: n28 (β_o hardness read as a presence test) ← n22 (`KNW/lookup`, literature hardness of β_o vs β_o+ω_o) → n18 (`MEC/identification`). n11 as `phase/fraction` and n12/n26 as `chemistry/composition` follow the r04 "amount of a crystalline phase → fraction; element content → composition" rule. `n17 -counteracts-> n20` is the right rel for the softening term against the performance claim.
- **mm_ops.** Accurate throughout, including the two `derives` chains (APT reconstruction → proximity histogram, `replot_derived_series`) and `read_distribution_statistics` on the hardness histograms, which is the rare op the r04 merge phase deliberately kept.
- **Audits (2, ≤5).** o4 (γ and α2 hardness histograms overlap heavily, frequency axes unlabelled) and n25 (0.15 at.% C unaccounted for in the rule-of-mixtures balance). Both are stated as "does not fully resolve", not as contradictions, which matches the figures.

## Panel checks

| node | panel_ids | ruling | finding |
|---|---|---|---|
| o1 | `#F1a`, `#F1b` | **confirmed** | F1a is the TNM BSE — globular, with β_o, γ and α2 arrowed and a bright interconnected β_o network. F1b is TNM0.75C — lamellar colonies plus globular grains, with only a few isolated white specks. Right panels, and the β_o contrast collapse (19% → 2%) is plainly visible. The node's "largely lamellar" was too strong; corrected. |
| o5 | `#F3c`, `#F3f` | **confirmed** | F3c is titled "TNM β_o phase", F3f "TNM0.75C β_o phase". F3c's mode is near 10 GPa with bars past 11 GPa; F3f is narrow, mode ~8.9 GPa, nothing above ~9.7. The node's note that only F3f carries the 8.0–12.0 GPa axis labels is also correct. |
| o10 | `#F5c` | **confirmed** | F5c is the Mo proximity histogram, ω_o and β_o labelled on either side of the interface: ~0.4 at.% in ω_o, dashed c_max at ~4.7 at.% about 3 nm into β_o, falling to ~3.0 at.%. Every number in the node label is on the panel. |

No invented panel ids. o7 (SAD) correctly carries empty `panel_ids`: the patterns are unlisted insets inside F4a and F4b.

## Changes applied

1. Added `n14 -supports-> n18` and `n26 -supports-> n18` (spine connectivity; n18 was a second root).
2. `o1` label and `image_note` corrected against the F1b crop: TNM0.75C mixes coarse lamellar colonies with globular grains rather than being "largely lamellar". The β_o reading that carries n11 is unchanged.
3. `o7 -> n14`: the `orientation_relationship` aspect moved onto the edge, where v04 puts `assign_features`' op attribute.

## What the packet got wrong

- **No XRD figure.** The MatMech record cites a figure "?" for the phase-fraction result, and the packet carries no such figure. The 19% → 2% β_o and 11% → 37% α2 numbers therefore rest on the text and a table; n11 records this with `attrs.proxy = XRD Rietveld phase analysis` and takes its figure evidence from the BSE contrast in o1. That is the right handling, but a reader should know the quantitative XRD is not in the record.
- **Tables 2–4** (APT compositions, mean hardnesses) are not in the packet either; n26 flags this in `attrs.source`.
- **Unlisted insets.** The Figure 4 SAD patterns and the Figure 2 isosurface legends are insets that the panel detector did not separate, so no ids exist for them. o7 handles this correctly with empty `panel_ids` plus an `image_note`, rather than citing F4a/F4b for content that is only in the inset.
- `#F3c` carries no axis numbers of its own — they sit under `#F3f` in the shared column. Anyone reading the F3c crop alone cannot place the mode; the graph says so in o5's `image_note`.
