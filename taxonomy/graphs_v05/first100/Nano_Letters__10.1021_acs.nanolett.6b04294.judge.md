# Judge review — Nano_Letters/10.1021_acs.nanolett.6b04294

**In operando study of why porous cobalt oxide stores Li well and Na badly** (rank 11)

**Verdict: approved with changes.**

## Checklist

- **Spine.** 20 nodes, one root (n2, HYP/gap), connected. Two parallel branches — the Li branch (n14 → n16 → n18 → n12) and the Na branch (n15 → n17 → n13) — meeting at n19 (MEC/identification) and n21. That is exactly the two-branch allowance in the protocol, and it is the right shape for a comparative paper.
- **Evidence.** Every spine STR/PRP claim has an `evidences` edge from an OBS node. n21 carries `basis: argued`; n19 and n20 are supported by claim-level `supports` edges plus computed OBS (o13, o14). No orphan claims.
- **Types.** o1 as `signal/reference_match` with `overlay_model_on_data` is the r04 #12 rule applied correctly (Rietveld calculated pattern = model reference → overlay, not match). n14/n15 as `STR/phase/fraction` (loss of crystallinity, degree of transformation) rather than `identity` is right. n19 `MEC/identification` vs n20 `MEC/pathway` follows the r04 rule: n19 picks the operative step from a known catalogue, n20 builds the bonding argument.
- **mm_ops.** All name a real act. `compare_across_conditions` on o13 (AIMD frames for three Li/Na, oxide/sulfide systems) is defensible rather than `track_feature_across_series`: what licenses the claim is the difference between the three systems, not the identity of one atom through frames, which is the r04 #1 boundary.
- **Audits (3, ≤5).** o4 (SEM does not resolve the 10–20 nm particles the text claims), n27/o2 (TGA leaves ~4 wt% undecomposed MOF), and the note inside o9 that the Li reflections are gone near 1 V rather than at the 0.01 V endpoint. All three are "the figure does not show what the text says" rather than "the figure contradicts it", and the graph states them that way.

## Panel checks

| node | panel_ids | ruling | finding |
|---|---|---|---|
| o4 | `#F1d` | **confirmed** | F1d is the SEM, data bar `ANL-EMC 15.0kV 8.3mm x70.0k SE(M)`, 500 nm scale. Interconnected rough blocks of ~100–200 nm; surface texture visible, no 10–20 nm nanograins resolved. The audit is fair and `partial` is the right `image_support`. |
| o9 | `#F4a` | **confirmed** | F4a is the Li/PCO in operando SXRD waterfall, 16–21°, with the 0.1 C voltage profile co-plotted against time 0–25 h. The 16.4° and 19.2° peaks are strong at t = 0, flat from ~5–6 h (near 1 V on the co-plotted curve), and never return through the charge to 3 V. Both the claim and the node's audit note are visible in the panel. |
| o12 | `#F5d`, `#F5f` | **confirmed** | F5d is the Na/PCO XANES with Co foil, CoO and Co3O4 references. The four cycled traces are bunched and sit on the Co3O4 reference, far from Co foil — the node's claim. The OCV trace stands further off than the node's note allowed (white line 1.49 vs ~1.30), so the note was tightened; the citation is correct. |

No invented panel ids; every id in the graph is in the packet's panel section.

## Changes applied

1. `o12.attrs.image_note` rewritten with the values on F5d: OCV white line ~1.49 against ~1.30 for every cycled state, cycled curves lying on the Co3O4 reference, F5f keeping the 1.56 and 2.48 Å shells. The old note's "a little sharper" understated the OCV offset. The conclusion (nothing approaches the Co-foil edge) stands.
2. `notes` corrected: it claimed the SAXS line-profile panels F3b/F3d were not carried by the packet. They are — `#F3b` "typical SAXS data at different charge/discharge states of Li/PCO cell" and `#F3d` the Na equivalent — and o8 already cites and reads both.

## What the packet got wrong

- **OCR reads the panel letter `d` as `p` in four figures** (`#F2d`, `#F3d`, `#F5d`, `#F6d`), each flagged "OCR DISAGREES with detector d". I opened `#F5d` and it is the Na/PCO XANES, matching the detector's `d` and the caption's (d). The detector letter is right in all four; the `p` is the OCR misreading the italic serif d. The graph uses the detector ids throughout, which is correct.
- `#F5f`'s `definition` is the fragment "Na/PCO cell", because the caption writes "(e) Fourier Transform … of (e) Li/PCO cell and (f) Na/PCO cell" — the caption itself repeats "(e)", and the packet's splitter inherits that. The crop is the Na FT, so the id is still usable.
- Several panels (`#F1d`, `#F3b`, `#F3c`, `#F5a`, `#F5e`, `#F5f`, `#F4b`) are detector-only, with no OCR letter. All the ones I opened carry the expected content.
