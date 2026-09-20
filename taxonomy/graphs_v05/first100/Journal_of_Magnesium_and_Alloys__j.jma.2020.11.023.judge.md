# Judge review — Journal_of_Magnesium_and_Alloys/j.jma.2020.11.023

**Se-doped Bi-rich Mg3Sb2 Zintl as a Te-free n-type room-temperature thermoelectric** (rank 15)

**Verdict: approved with changes.**

## Checklist

- **Spine.** 20 nodes, one root (n2), connected and stage-ordered: gap → alloy-and-dope hypothesis → Mg3.2Bi1.4Sb0.6 + Se + coarse-grain route → ball mill and hot press → single phase, layered dense body → valley degeneracy and carrier/mobility descriptors → transport mechanism → resistivity/Seebeck, power factor, lattice κ → trade-off → ZT → module capability → conclusion. Two parallel property branches (electronic and thermal) meeting at n19/n20, which is the allowance.
- **Evidence.** Every spine STR/PRP/PRF claim carries an `evidences` edge; n19 is `argued`, n13 and n15 are `evidenced`. No orphan claims.
- **Types.** n13 and n14 as `PRP/descriptor` (valley degeneracy; carrier concentration and mobility) is the v04 definition word for word — microscopic descriptors standing between structure and the measured property. n20 as `PRF/figure_of_merit` and n21 as `service_capability` is the r04 #11 split applied correctly (ZT is the field's ranking convention; the module efficiency is the use condition). o10 as `OBS/response/component_partition` is exactly the case r04 ruling #5 refused to merge into `trend`.
- **mm_ops.** Accurate, including `overlay_model_on_data` for the Pisarenko curves (a model reference, per r04 #12) and `compare_with_reference_value` for the literature ZT bars.
- **Audits (4, ≤5).** o4/n27, o6/n26, o8 and o13. **One of these was not stated fairly** and has been rewritten — see below. The others are correctly graded as "the figure does not resolve it" or "the panel value is slightly below the quoted one", not as contradictions.

## Panel checks

| node | panel_ids | ruling | finding |
|---|---|---|---|
| o4 | `#F3c`–`#F3f` | **confirmed** | F3f is the Se map, labelled "Se" and "(f)", 50 µm bar, and it is sparse single-pixel noise with no resolvable structure. The n27 audit — Se is near the EDS detection limit so the map cannot establish uniformity — is exactly what the panel shows, and `partial` is the right `image_support`. |
| o6 | `#F4b` | **confirmed** | F4b is Hall mobility vs temperature with T⁻⁰·⁵, T⁻¹ and T⁻¹·⁵ guides. The node's packet-defect claim is verified on the crop: **the ordinate reads `μ_H (10¹⁹ cm⁻³)`**, i.e. it carries F4a's carrier-concentration units instead of cm² V⁻¹ s⁻¹. 300 K values ~170 / 160 / 148 / 127 for the doped samples and ~15 for x = 0, matching the node. |
| o8 | `#F5a`, `#F5b` | **confirmed** (citation) | F5a is resistivity and F5b the Seebeck coefficient — the right panels. But **the node's reading of F5a was wrong**, and with it the audit built on it. See below. |

No invented panel ids.

## Changes applied

1. **`o8` label and `image_note` rewritten.** The node claimed resistivity "falls monotonically with Se, so the text's claim that it rises to a maximum at x = 0.01 does not match the panel". F5a at 300 K reads **600 (x = 0), 23 (0.005), 11.5 (0.01), 13 (0.02), 15 (0.04) µΩ·m** — a *minimum* at x = 0.01, not a monotonic fall. The audit as written was therefore unfair to the paper. There is still a real conflict, but it is a sign slip: the text says "the resistivity increases first, and reaches the maximum limit when x = 0.01" where the panel shows a minimum there (the sentence plainly means conductivity). The second half of the original audit was correct and is kept with its evidence: the text says "both the resistivity and Seebeck coefficient continuously increase with the increasing temperature", while the undoped resistivity falls with temperature throughout and the undoped |S| peaks near 400 K and then falls. F5b values added: −350 / −260 / −212 / −208 / −178 µV K⁻¹.
2. **Removed `n16 -counteracts-> n17`.** The graph carried both `causes` and `counteracts` between the same pair, asserting and denying one link. The Seebeck loss term is already named in n19 (`MEC/tradeoff`), which is where v04 puts it.
3. **`n16` and `n17` `property_family` `thermal` → `electrical`.** Resistivity, Seebeck and the power factor S²/ρ are electrical transport quantities; n18 keeps `thermal`, so n19's trade-off now runs between the two families it actually spans.

## What the packet got wrong

- **`#F4b`'s ordinate is mislabelled in the paper itself**: `μ_H (10¹⁹ cm⁻³)`, F4a's units on F4b's mobility axis. Confirmed on the crop. The graph records it in o6's `image_note`, which is the right place.
- **OCR misreads two panel letters**: `#F2b` read as "q" and `#F5b` read as "g", both flagged as detector/OCR disagreements. I opened `#F5b` and it carries "(b)"; the detector letter is right in both.
- Several panels (`#F3f`, `#F5a`) are detector-only with no OCR letter; both carry their letters in the image.
- Paper-level, not packet-level: the text quotes a Seebeck range of −175 to −239 µV K⁻¹ for the doped samples, while `#F5b` reads −178 to −260 at 300 K; and the text's engineering ZT and efficiency (0.9, 12%) are slightly above the ~0.84 and ~11.8% on `#F7b`/`#F7c`. Both are recorded in `image_note`s rather than used as label values, per r04 ruling #37.
