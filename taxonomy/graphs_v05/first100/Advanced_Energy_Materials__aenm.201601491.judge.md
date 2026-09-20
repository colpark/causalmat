# Judge review — Advanced_Energy_Materials/aenm.201601491

**Dual-redox V/Fe Prussian blue analogue cathode for aqueous batteries** (rank 13)

**Verdict: approved with changes.**

## Checklist

- **Spine.** It had **three roots**: n2 (HYP/gap), n14 (DES/down_select) and n21 (MEC/identification). n14's only parent was o5, an OBS; n21's parents were all OBS or KNW. Both are fixed (below), and the spine is now 19 nodes, one root, connected: gap → dual-redox hypothesis → V/Fe framework and acidified co-precipitation → crystallinity ranking → down-select → cycling → dual valence change → multi-electron mechanism → capacity, rate and fade → service claim → conclusion.
- **Evidence.** Every spine STR/PRP/PRF claim has an `evidences` edge; n17, n19 and n22 carry `basis: argued`. No orphan claims.
- **Types.** n12 as `STR/phase/fraction` with `proxy = XRD peak sharpness` rather than `identity` is right (n10 carries identity separately from the same figure, correctly split). o2 `reference_match` vs o3 `feature_quantification` on the same panel F1d is the r04 "whole trace against a reference" / "partial change argued" boundary applied cleanly. n21 as `identification` rather than `pathway` fits the r04 rule — a member picked from a catalogue of degradation modes.
- **mm_ops.** All accurate. `compare_with_reference_value` on o9 → n16/n28 is the right op for positioning data against the drawn oxidation-state reference lines, and the `derives` chain o8 → o9 (`replot_derived_series`) is correctly marked with `provenance: derived`.
- **Audits (3, ≤5).** o4, o9/n28 and o12. Graded correctly: o4 and o9 are "the figure does not resolve the full claim"; o12 is the one real figure-against-text conflict and is carried by `image_support: partial` plus an `image_note`, not dressed up as a contradiction.

## Panel checks

| node | panel_ids | ruling | finding |
|---|---|---|---|
| o4 | `#F1f` | **confirmed** | F1f is the HRTEM of the HCl powder, 5 nm bar, red arrows on lattice-fringed domains and white arrows on featureless ones. The amorphous regions occupy a share of the field comparable to the fringed ones, so the audit against "high crystallinity" is fair. |
| o9 | `#F3d` | **confirmed** | F3d plots Fe and V edge energies against normalised charge capacity with dashed Fe³⁺/Fe²⁺ and V⁵⁺/V⁴⁺/V³⁺ reference lines. Fe runs ~7124.5 → ~7126.3 eV, arriving on the Fe³⁺ line; V runs ~5469.75 → ~5470.5 eV, crossing V⁴⁺ and stopping short of V⁵⁺ at 5471.0. The Fe²⁺, V³⁺ and V⁵⁺ lines are never reached — exactly the n28 limitation. |
| o12 | `#F5c`, `#F5d` | **confirmed** | F5d plots Re, R_film and Rct against cycle number: Rct rises ~3 → ~28 Ω with error bars of several ohm and is still rising at cycle 250 (with a dip at 200); R_film sits near 2.5–3 Ω and Re near 0.3 Ω. The node's reading and its audit — the text's "saturates after cycle 30" is not what the panel shows — both hold. |

No invented panel ids.

## Changes applied

1. Added `n12 -motivates-> n14`. The down-select had only an OBS parent; n12 is the ranking claim the choice is actually made on (screen-then-choose).
2. `n21` → `spine: false`. It was a third root, and the only edge that could have given it a spine parent (`n20 -supports-> n21`) would have made a two-cycle against `n21 -explains-> n20`. It stays as a side claim explaining n20 and supporting the conclusion. Spine 20 → 19.

## What the packet got wrong

- **Figure ids are offset by one from the paper.** Packet F5 carries the caption "Figure 6. Changes in A) the surface morphology and B) XRD patterns of the cathodes during cycling…". The paper's Figure 5 is absent from the record. Panel ids `#F5a`–`#F5e` therefore point at the paper's Figure 6 panels. The graph records this in `notes`; the ids themselves are internally consistent and usable.
- **MatMech summary numbers disagree with the panel.** The summary quotes ~80% capacity retention; the panel in the packet (`#F2a`) shows 91 → 54 mA h/g over 250 cycles, i.e. ~59%, at a different current density. The graph reads the panel, which is what r04 ruling #37 requires.
- **A referenced figure is missing:** MatMech records the 880/1760 mA g⁻¹ long-cycling result against figure "?", and no such figure is in the packet. The graph leaves that result out rather than attaching it to a figure that does not exist.
- Panels `#F1g` (FT-IR/TGA) and `#F1h` (EDS maps) exist in the packet but are unused; that is a deliberate budget choice recorded in `notes`, not a packet fault.
