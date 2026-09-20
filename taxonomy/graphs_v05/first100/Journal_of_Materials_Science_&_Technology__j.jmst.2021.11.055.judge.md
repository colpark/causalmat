# Judge review — Journal_of_Materials_Science_&_Technology/j.jmst.2021.11.055

**Cd-vacancy-anchored ligand-free Cu clusters on CdS nanorods for sacrificial-agent-free photocatalytic CO2 reduction** (rank 16)

**Verdict: approved with changes.**

## Checklist

- **Spine.** 20 nodes, one root (n2), connected: ligand-blocking gap → vacancy-trapping hypothesis → CdS rods + Cu + protonate/anneal route → rods, edge Cd vacancies, anchored clusters, Cu–S interface → charge-transfer mechanism → carrier descriptor and CO2 binding → CO2⁻ intermediate → CO yield → TON/selectivity → conclusion. Two branches (charge transfer and CO2 binding) meeting at n19, which is the allowance.
- **Evidence.** Every spine STR/PRP/PRF claim has an `evidences` edge; n15 is `argued`, n18 `evidenced`. No orphan claims.
- **Types.** n12 as `STR/defect/point` with `aspect: position` is r04 ruling #25 applied correctly. n13 as `microstructure/distribution` rather than `shape` follows the "where a constituent lies → distribution" rule. n19 (`service_capability`, yield under the stated use condition) vs n20 (`figure_of_merit`, TON and selectivity as the field's ranking convention) is the r04 #11 split, correctly made.
- **mm_ops.** Accurate. `register_colocated_views` on o3 → n13 is the right op — the zoomed region and its line profiles have to be registered onto the rod edge — and `compare_with_reference_value` on the XANES/EXAFS reference curves is correct rather than `match_to_reference`, because the references are plotted alongside as values, not matched as a whole trace.
- **Audits (3 nodes + 2 image_notes, ≤5).** The best-audited graph of the eight. n26 names a genuine internal contradiction in the paper's own evidence and leaves it as an anomaly rather than picking a side. Nothing here dresses a "does not resolve" finding up as a contradiction: o2, o5, o8 and o12 all carry `image_support: partial`, which is where those judgements belong.

## Panel checks

| node | panel_ids | ruling | finding |
|---|---|---|---|
| o3 | `#F1e`, `#F1h` | **confirmed** | F1h holds the two intensity line profiles: upper boxed and annotated **0.36 nm** (Line 1), lower boxed and annotated **0.22 nm** (Line 2). Both spacings are printed on the panel, and the 0.22 nm reading is a resolved periodic lattice — which is what makes the n26 anomaly against the EXAFS real rather than rhetorical. |
| o9 | `#F5h` | **confirmed** | F5h plots Qst vs CO2 uptake for CR and CuCR SCC. CuCR SCC starts at ~25.4 kJ mol⁻¹ against ~8.9 for CR, the curves cross near 0.072 mmol/g, and CuCR SCC bottoms out near 3.0 at 0.105 — every number in the node. It also climbs back above CR at ~0.125, which the node missed; added. |
| o11 | `#F3e` | **confirmed** | F3e prints TON 48.1 (CR-H), 94.4 (CuCR SCC), 54.4 (CR) on the left axis with CO selectivity on a blue right axis at ~72, ~81 and ~72%. Matches the node, and its `image_note` is right that the 0–100% right axis makes the 9-point selectivity gain a small step. |

No invented panel ids.

## Changes applied

1. `n19 -> n20` rel `causes` → `supports`. TON and selectivity are computed from the same run as the CO yield — claim-to-claim reasoning, not physical causation, which is the distinction v04 insists on.
2. `o13.attrs.image_note`: "the dark traces at the bottom of **F3**" → **F4a**. The node reads F4a and F4d; F3 is the photocatalysis figure.
3. `o9.attrs.image_note` extended with the full shape of the F5h curves. n27 said the Cu catalyst's Qst "drops below that of bare CdS" above ~0.075 mmol/g; the panel shows this holds only over a middle window (~0.072 to ~0.125 mmol/g) before the curve climbs back above CR and ends higher. The audit is now bounded to what the panel shows — which makes it less sweeping, not stronger.

## What the packet got wrong

- **Nothing misassigned.** Every id I opened carried the content its `definition` promised, and the F5 definitions track the caption correctly through h panels — notably better than the Figure 4 section of the Advanced Materials packet in this same batch.
- **Split definitions across panels.** `#F5a`'s definition is the fragment "Cd 3d and", `#F5b`'s "S 2p of CuCR SCC and CR", and F5d–f each repeat the whole "Time-resolved transient PL decay curves…" clause. That is the caption's own sentence structure, not an error, but the `definition` field alone is not enough to identify F5a/F5b.
- **Many detector-only letters** (`#F1e`, `#F1h`, `#F3e`, `#F5b`, `#F5c`): the OCR read no label. All four I opened carry their letters in the image and the detector assignment is right each time.
- **A provenance note, not a packet fault:** o9 is marked `computed` because F5h is a *calculated* Qst and the source CO2 isotherms are not in the packet. `derived` would be the better value but would violate the v04 rule that `derived` needs an incoming `derives` edge from the OBS it came from — and that OBS does not exist here. `computed` is the valid choice; it is worth flagging that the isotherms behind the paper's binding claim are not in the record.
