# Judge review: Advanced_Composites_and_Hybrid_Materials/s42114-021-00406-x

**Verdict:** accept with fixes. This review checks structure only. No figures or crops were opened, and no panel citations or techniques were ruled on (the blind second read checks those). Splits: 4 (n10, n12, o10, o2). Merges: 0. Source changes: 2 (n19, n10). read_from changes: 0. Mode changes: 0. MatMech: 4 supports / 0 contradicts / 0 not covered.

The graph now has 49 nodes, 54 edges and 16 spine nodes. It passes the v04 validation checks: types, rels, mm_ops, panel ids, cue/technique, modes, spine connectivity and support.

## 1. Spine order

- The spine reads: need n1 -> hypothesis n2 -> base n3, PIL modification n4 and blending-time sweep n5 -> melt blending n6 -> PIL-widened interface n9 -> CNT migration/interfacial localization n7. From n7 there are two branches:
  - mechanical: phase refinement n8 (+ n9, joint) -> elongation n12;
  - electrical: network present n10 -> network most complete at the interface n20 -> conductivity n11 -> EMI SE n13, explained by conduction loss n15.
  Both branches end at conclusion n16. This is one connected path in stage order, with two branches.
- Every spine STR/PRP/PRF/MEC node is backed:
  - n7 by o3, o4, k2 and k3;
  - n8 by o1 and o2;
  - n10 by o5 and k1;
  - n11 by o12 and o13;
  - n12 by o9 and o10;
  - n13 by o16, o17 and o18;
  - n15 by k4.
  Two nodes had no premise before this review, so I added one each:
  - n9 (argued) had neither OBS evidence nor a KNW premise. It now takes k5 (MEPGMA affinity [56]).
  - n20 (argued, new) takes k6 (interfacial localization builds a more effective network [63]).
- The v04 rules hold. n14 is PRP/value with aspect = partition, evidenced by o20 component_partition. n13 is PRF/service_capability.
- Audits: 3, all fair. o14 and o19 find that at 2 min the PIL composite is worse than the PIL-free one in conductivity and SE. o22 (new) finds that PIL-8m is coarser than PIL-6m, so the refinement with PIL is not monotonic.

## 2. Splits and merges

| node | into | why |
|---|---|---|
| n10 | n10, n20 | network present in all blends (G' plateau, o5 + k1) vs network most complete with interfacial CNTs (text only). n20 is on the spine. The edge n10 -> n11 causes became n7 -> n20 causes, n10 -> n20 supports and n20 -> n11 causes |
| n12 | n12, n21 | elongation optimum (spine) vs PIL lowering yield stress and raising ultimate stress (off-spine). o11 moved to n21. n9 causes n21 (linked text F5: plasticizing and compatibilization) |
| o10 | o10, o21 | elongation series vs the ~34 MPa ultimate-stress value. o21 evidences n21 by read_characteristic_point |
| o2 | o2, o22 | a supporting comparison (finer with PIL at 2-6 min) vs a qualifying one (PIL-8m coarser). o22 qualifies n8 |

Other changes:
- o8 label trimmed to the exotherm reading that n18 uses. The melting peaks moved to image_note.
- n10's image_support went from partial to shown after the claim was narrowed. This follows n10's own image_note ("the plateau shows a network in every sample"). It was not re-judged from the image.
- n21 inherits image_support = partial from n12. It was not re-judged.

Merges: none. No two nodes state the same claim. o14 and o19 overlap o12/o13 and o16/o17 in their values, but they state the 2-min comparison, which is the audit.

## 3. Source and read_from changes

| node | source | requires_unseen added |
|---|---|---|
| n19 | figure -> inferred | steepest conductivity rise locates the percolation threshold (prior knowledge) |
| n10 | text -> inferred | G' plateau -> filler network (k1). The text-only "most perfect network" fact moved to n20 |

The new nodes carry their own source:
- text: n20, k5, k6;
- figure: n21, o21, o22.

read_from: no changes. The annotations listed for F3-F7 are sample labels, axis titles and 'Endo'. No OBS label restates one of these strings as its reading. F1, F2, F8 and F9 have no OCR.

One flag for the second read: o12/o13 (F6a) and o20 (F8) quote values to 0.1 (23.0, 28.8 S/m; 36.8 dB). The axis ticks cannot resolve this, so the values may be data labels drawn in the image. The packet does not list them as annotations, so read_from stays axis.

## 4. Mode changes

None. Only n12 has two causes edges (n8, n9). Both are marked joint, which is correct: the F5 caption shows no choice, and the linked text credits both factors. All other claims have at most one causes edge, including n20, n11, n21 and n7.

## 5. MatMech tally (recorded after the graph was final; the graph was not edited)

supports 4, contradicts 0, not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | blending time 2-8 min -> CNT localization at interface/PCL, refined co-continuous phase | supports | n5, n6, n9, n7, n8, k2, k3, k5 | |
| M2 | interfacial PIL-CNT network -> higher conductivity, tensile strength, elongation | supports | n7, n20, n11, n8, n9, n12, n21 | the graph routes mechanics through phase refinement and interface (n8, n9), not the network. MatMech "2.48 S/m" is the 6 wt% value (F6b text). At 8 wt% the graph reads 28.8 S/m (n11). MatMech has G' rising to 6 min; n17 rises through 8 min |
| M3 | conductivity / conduction loss -> EMI SE ~41 dB, absorption dominated | supports | n11, n13, n15, n14, k4, o20 | |
| M4 | 6 min + PIL -> optimum conductivity and elongation | supports | n5, n6, n7, n20, n11, n12, o13, o10 | |
