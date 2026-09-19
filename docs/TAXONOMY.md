# Papers as logical graphs: a node vocabulary for multimodal materials reasoning

**Date:** 2026-09-18.

**The goal.** Turn each MatMech paper into one directed graph: "this, so this, so this". The graph follows the argument spine:

hypothesis → selection/design → processing → structure → property → performance → discussion

Images and data sit in between as evidence. The graph's nodes are drawn from one shared vocabulary that is detailed, hierarchical and as general as possible.

**Where things are:**

| What | Where |
|---|---|
| Final vocabulary | [`taxonomy/vocab/v04.json`](../taxonomy/vocab/v04.json), readable tree in [`taxonomy/vocab/HIERARCHY.md`](../taxonomy/vocab/HIERARCHY.md) |
| Protocol | [`taxonomy/PROTOCOL.md`](../taxonomy/PROTOCOL.md) |
| Rulings | `taxonomy/rounds/rXX/judge.md` |
| Graphs | `taxonomy/graphs_v04/` (all 60 papers, migrated), `taxonomy/cases/` (3 reviewed showcases) |
| Rendered page | `site/argument_graphs.html`. Published privately as a claude.ai artifact; it can be shared from that page |

## Method: sweep until saturated, then merge

Two roles run in every round:

- **Staff agents (the fellow discussants).** Each decomposes its papers with the current vocabulary. It opens the figures, types every node, and names a multimodal operation (mm_op) on every edge from a figure to a claim. It proposes new entries only when no existing one fits.
- **A senior-investigator agent (the judge).** It rules on every proposal (accept, merge, reject or restructure), spot-checks graphs against the packets and figures, and writes the next vocabulary version.

The rounds doubled in size. They are stratified evenly over the 15 journals, not proportionally.

| Round | Papers | Nodes | Coverage by previous vocabulary | New leaf types per paper |
|---|---|---|---|---|
| r1 | 4 | 135 | 0% (seed had only 10 stages) | 14.5 |
| r2 | 8 | 326 | 96.9% | 0.62 |
| r3 | 16 | 519 | 98.5% | 0.12 |
| r4 | 32 | 1,129 | **100%** | **0** |

Round 4 met the stop rule: fewer than 0.1 new leaves per paper, and at least 95% coverage.

The **merge phase** then removed 7 entries and one mm_op family, using usage counts across all 60 papers (2,109 nodes, 2,625 edges). Siblings that staff could not tell apart were merged, unless the next inference differs between them. Otherwise they got a written decision rule. All 60 graphs were then migrated to v04 with 0 validation problems.

## The final vocabulary (v04)

**81 type entries:** 10 L1 stages, 7 L2 groups and 64 leaves, at most 3 levels deep. Leaves per stage:

- **Spine stages:**
  - HYP (hypothesis) 3
  - DES (design/selection) 7
  - PRC (processing) 6
  - STR (structure) 15, in the groups phase, chemistry, defect and microstructure
  - PRP (property) 4
  - PRF (performance) 3
  - MEC (mechanism, the bridge between stages) 3
  - DSC (discussion) 5
- **Evidence and premises, never on the spine:**
  - OBS (observation) 14, in the groups signal, response and morphology
  - KNW (prior knowledge) 4

**Multimodal operations: 22, in 5 families.** Each names what a reader does to a figure to get a claim.

| Family | Count | Examples |
|---|---|---|
| read | 5 | read_trend, read_characteristic_point, read_distribution_statistics |
| compare | 6 | compare_across_conditions, correlate_across_series, compare_with_reference_value |
| match | 4 | assign_features, match_to_reference, register_colocated_views, overlay_model_on_data |
| quantify | 4 | convert_to_quantity, fit_model, replot_derived_series, measure_feature_metric |
| check | 3 | cross_check_consistency, collapse_by_normalization |

**Other fields:**
- **14 relations,** for example `motivates`, `produces`, `evidences`, `causes`, `supports`, `derives`, `qualifies` and `rules_out`.
- **13 modalities,** for example micrograph, diffraction pattern, spectrum, xy curve, spatial map, orientation distribution and volume render.
- **Node fields:** `provenance` (measured, derived or computed), `image_support` (shown, partial, not_shown or contradicts, judged from the image itself), `spine`, and `text_silent`.

**Design principles (from the judge):**

1. A distinction is a type only if it changes the next inference. Everything else is an attribute.
2. Types name roles in the argument. Techniques and materials never become types, and the op names the act on the figure.
3. The skeleton is fixed. New cases are absorbed by decision rules between siblings before any leaf is added.

## Showcase decompositions (reviewed by the judge)

| Paper | Nodes / edges / spine | Key multimodal steps |
|---|---|---|
| Nano-diamond / ZK60 Mg composite (J. Mg Alloys 2021) | 47 / 62 / 17 | HAADF image, EDX maps and line scan registered, and converging with XRD, to name MgZn2 · grain size × yield across the series do not co-vary, so Hall-Petch is not the lead term · strain curves converted to CTE and checked against the text |
| Amorphous Ni–Co hydroxide nanocages for OER (Adv. Energy Mater. 2015) | 45 / 54 / 16 | measured activity volcano × DFT O\* binding share their rank order, the only bridge from reactivity to activity · ring/disk currents turned into a charge balance (4e⁻ path) · EDS line scan registered on the TEM cage to show a hollow shell, while the spectrum shows Cu and S that the formula omits |
| HAP/PLLA/PGA bone scaffold (Bioactive Mater. 2020) | 49 / 63 / 19 | XRD, FTIR and DSC converge on one phase claim (FTIR keeps HAP where XRD loses it) · water uptake × weight loss across the ratio series · "exposed HAP" particles are more than 10× the raw needle size, so exposure ≠ bare filler |

## What this says about multimodal reasoning in materials papers

Six recurring patterns appear across the 60 papers:

1. **Convergence.** Several modalities point to one claim, for example diffraction, a spectrum and thermal analysis all identifying one phase. No single figure is enough.
2. **Registration.** Views of the same region are overlaid: an element map on a micrograph, SAED spots on bright-field positions, an indent map on an etched weld.
3. **Series correlation.** Two quantities read across the same sample series are correlated. This is often the paper's only support for a mechanism, and it stays correlational.
4. **Transformation.** Raw readouts are turned into derived quantities: a slope into an activation energy, currents into Faradaic efficiency, a calibration curve into a modulus.
5. **Normalization collapse.** Curves that collapse onto one line after rescaling support a governing variable.
6. **Figure-versus-text consistency.** Across the 60 graphs, 42 papers (70%) have a figure that shows something the text never states, and 8 (13%) have a figure that contradicts the text. Either case occurs in 46 papers (77%). Examples:
   - capacities 1.35× off;
   - strengths 1000× off;
   - an activation energy stated as 68 kJ/mol where the plot implies about 2;
   - aggregation where the text claims dispersion;
   - swapped ring labels.

These audits are the richest source of checkable multimodal reasoning items.

## Data defects found in MatMech

- **Records whose image path points to a folder:** 1,525 of 425,295, affecting 1,265 papers; 1 image file is missing.
- **Figure alignment:** staff found caption/image swaps, a missing figure that shifts the numbering, and a figure file containing two paper figures.
- **Extracted numbers:** MatMech's summary numbers disagreed with the figures in 3 of 4 papers in one staff batch.
- **Extracted claims:** in one showcase, the MatMech summary put an interface on the wrong phase, although the paper's text and figure agree with each other.

**Do not use MatMech's extracted values as answer keys without checking them against the figure.**

## Limits

- **Coverage is by agent consensus.** Staff and judge are all LLM agents. No human materials scientist has audited the vocabulary, and "100% coverage" means staff found an existing type acceptable, which is not proof that the type is correct.
- **Figures were checked selectively.** Staff opened about 4 figures per paper in rounds 3 and 4. Nodes resting on unopened figures carry no image_support verdict. Only the 3 showcases opened every figure.
- **Inputs are packets, not papers.** Packets hold MatMech's figure-linked text, not the full paper, so introduction and discussion nodes are partly inferred (`attrs.inferred`).
- **Sampling.** Stratifying evenly over journals over-represents the small journals relative to the corpus.
