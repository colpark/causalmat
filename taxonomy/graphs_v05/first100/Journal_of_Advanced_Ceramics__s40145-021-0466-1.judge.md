# Judge review — Journal_of_Advanced_Ceramics/s40145-021-0466-1

**Nanopore space confinement, not N active-site density, drives four-electron ORR on N-doped porous carbon** (rank 14)

**Verdict: approved with changes.**

## Checklist

- **Spine.** It had **three roots**: n1 (HYP/need, correct), n14 (PRP/diagnostic) and n15 (PRP/value). Both PRP nodes are read straight off the RDE data and feed n16; nothing upstream on the spine produced them, and manufacturing a parent would have meant inventing a causal edge from the porosity claim. Both are now `spine: false`. The spine is 16 nodes, one root, connected: need → conflicting-reports gap → confinement hypothesis → glucose spheres + urea/ZnCl2 + temperature sweep → hydrothermal + carbonisation → morphology, porosity, N content → confinement pathway → four-electron identification → activity → durability/methanol tolerance → conclusion.
- **Evidence.** Every spine STR/PRP/PRF claim has an `evidences` edge; n16 is `argued` and n18 `evidenced` (from the MD collision-frequency fits). No orphan claims.
- **Types.** The strongest feature of this graph is that the paper's paradox is modelled explicitly: n17 (`MEC/pathway`, `basis: attributed`, active-site density) is the field's default explanation, brought in by n23 (`KNW/precedent`) and then **ruled out** by n12 and o8 with the `rules_out` rel. That is the correct, rare use of a rel the corpus barely exercises, and it is what licenses n21's conclusion. n14 as `PRP/diagnostic` also satisfies the r04 #10 rule exactly (KNW/model K-L → diagnostic → MEC/identification).
- **mm_ops.** All accurate, including `fit_model` with `form: linearised` on the K-L, Tafel and MD fits, and `cross_check_consistency` on o13 → n26 for the Pt/C slope discrepancy.
- **Audits (2 nodes + 2 image_notes, ≤5).** Correct budget discipline and correctly graded — see below.

## Panel checks

| node | panel_ids | ruling | finding |
|---|---|---|---|
| o8 | `#F3b` | **confirmed** | F3b is the stacked N-species bar chart (pyridinic/pyrrolic/graphitic/oxidised) over NPC-800, NPC-900, NPC-1000, NC-1000. Totals 5.89 / 3.83 / 1.81 at% and pyridinic 2.8 / 1.17 / 0.5 at% are as claimed, and graphitic N does peak at NPC-900. Right panel; the node's `image_note` overstated the case and was corrected. |
| o13 | `#F5b` | **confirmed** | F5b prints all four Tafel slopes beside their lines: NPC-1000 64.9, NPC-900 72.6, NPC-800 105.5, Pt/C **81.5** mV/dec. The Pt/C label against the text's 68.5 is exactly the n26 anomaly, and n15's ranking is what the panel shows. |
| o10 | `#F4b` | **confirmed** | F4b is the five-curve LSV at 1600 rpm. NPC-1000 (red) has the most positive half-wave near 0.86 V and a ~−5.0 mA cm⁻² plateau together with Pt/C; NPC-800/900 stall near −3.4; and the ZnCl2-free NC-1000 control does reach the same plateau at a half-wave roughly 0.07 V lower — the text-silent reading the node records. |

No invented panel ids. o4 (SAED) correctly carries empty `panel_ids`: the insets sit inside F2b and have no id.

## Changes applied

1. `n14` and `n15` → `spine: false` (spine connectivity; 18 → 16 spine nodes). Their diagnostic chain is untouched.
2. `o8.attrs.image_note` corrected against the F3b crop. It said NPC-1000 has the smallest bar on **every** nitrogen type except oxidised N. Reading the segments: graphitic N is ~0.67 at% (NPC-800), ~1.13 (NPC-900), ~0.80 (NPC-1000), so NPC-1000 sits **above** NPC-800 on graphitic N. The node's label (graphitic N peaks at NPC-900) was already right, and the `rules_out` edge into n17 survives the correction — on the corrected reading neither nitrogen type tracks the activity ranking NPC-1000 > NPC-900 > NPC-800, which is the whole argument.

## What the packet got wrong

- **Nothing in the panel section is misassigned** for this paper: every id I opened carried the content its `definition` promised, and the OCR agreed with the detector on all three letters checked.
- The packet's **text** and its own figure disagree on the Pt/C Tafel slope (68.5 vs the 81.5 printed on `#F5b`). This is a paper-level defect of the kind r04 §5 catalogues, not a packet-building error, and the graph handles it the required way: the panel value is used and the conflict becomes n26.
- The **SAED insets in F2b have no panel ids**, so a claim about them cannot be cited. o4 handles this correctly rather than citing F2b for inset-only content. Worth noting for the panel pipeline: insets are a recurring blind spot (three of my eight papers hit it).
- The text describes a **pre-calcination urea XRD trace** that is not in `#F1b`; o1's `image_note` says so.
