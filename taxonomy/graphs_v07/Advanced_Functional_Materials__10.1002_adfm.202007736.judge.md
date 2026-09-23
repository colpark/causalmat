# Judge review: Advanced_Functional_Materials/10.1002_adfm.202007736

**Verdict:** accept with fixes. Structure-only review: no figure or crop was opened, and no panel citation or technique was ruled on. After the fixes the graph has 18 spine nodes, 46 nodes and 54 edges, and passes the v04 checks (types, rels, mm_ops, modalities, OBS fields, mm_op on every figure edge, op attributes) with 0 problems.

The spine is one connected path:
- need -> gap -> hypothesis -> GLC-TEM method + the citrate/no-citrate sweep -> nucleation inside the cell;
- from that act, three arms, which is the allowed two branches plus one control branch:
  - classical: rhombohedral COM (n8) -> classical pathway (n7);
  - non-classical: rectangular 90 degree product (n10) -> dissolution-reprecipitation pathway (n9);
  - citrate control: transient formation (n12) -> chelation pathway (n11) -> buffer overcome (n13) and hydration (n14) -> O:Ca rise (n15) -> COD (n16);
- the citrate arm closes on n20, and n7, n9 and n20 meet at the conclusion n17.

Every spine STR/PRP/PRF/MEC node now has OBS evidence or a KNW premise. Audits are 4 (a1, a2, d1, d2), under the budget of 5, and all fair: a1 notes that only the citrate XRD pattern is plotted, a2 that the EELS 95% intervals overlap while the EDS pair separates, d1 the liquid-cell and MD scale limits, d2 that the non-classical product is named from corner angles with no diffraction. x1 and x2 are ruled-out alternatives, so they sit in the side ring, not the audit ring.

## Changes
- **Split n17 -> n17 + n20.** The conclusion label stated two claims. n17 keeps "the nanoscale nucleation pathway sets the final CaOx polymorph" with its F5 citation; new n20 (DSC/conclusion, spine, source text) carries "citrate buffers CaOx formation and, once the buffer is overcome, the product is COD". The edge n16 -> n17 moved to n16 -> n20, and n20 -> n17 supports was added, so the spine still terminates in a single conclusion.
- **Split o5 -> o5 + o16.** The label read two things off F2 and fed two different claims. o5 keeps the shape reading ("the two residues show 90 degree corners and a rectangular outline at 67-76 s") and its edge to n10; new o16 carries "the two residues merge into a single particle by 85 s" and takes over the o5 -> n9 evidences edge, keeping mm_op track_feature_across_series. The image_note was split with the labels.
- **Added k2 -> n13 premise_for.** n13 is a spine MEC claim (basis = argued) that had neither OBS evidence nor a KNW premise. The stronger tridentate Ca:citrate binding (k2) is the premise its equilibrium argument rests on. Its basis stays argued: no free-calcium measurement is shown.
- Merges: none. No two labels state the same claim. The OBS/claim pairs (o14 with n15, o11/o13 with n16) are a readout and the claim it supports, not duplicates.
- Considered for a split and kept whole: o2 (120 degree corners / hexagonal outline is one reading of one frame), o11 (one indexing act over one SAED pattern; assignment is plural by definition), o13, o14 (one trend on one panel, quantified for the two techniques the panel plots) and d2 (one limitation).
- Left as built, noted rather than edited: on the citrate arm the order runs PRC -> PRP/behavior_class (n12) -> MEC -> STR (n15, n16), so PRP precedes STR on that branch. That is the paper's own order - the transient nucleation behaviour is what the citrate mechanism explains, and the polymorph then follows from the mechanism - so forcing the stage order would misstate the argument.

## Source / read_from changes
- No source change to an existing node, and no read_from change. Every OBS node carries read_from, and the two nodes set to `annotation` (o11 on the F4b COD/graphene index labels, o13 on the F4d Miller labels) are exactly the ones that restate author-drawn strings; o13 correctly records that the packet lists only `(os1)` although about twenty such labels are on the panel. The `pixels` and `axis` nodes restate no string from their panel's annotations list: F1 and F2 offer no annotations at all, F3a lists only `Os`, F4c is annotated false, and on F4e/F4f/F4g the listed strings are condition and peak labels while the readings themselves are axis values (o14, a2) or relative peak heights (o15).
- New nodes: n20 source `text`, with the buffering-and-overcoming statement listed in requires_unseen as F5 linked text; o16 source `figure`, requires_unseen empty.
- requires_unseen elsewhere is already complete and honest: with the packet carrying captions plus linked text only, every with/without-citrate assignment, the 0.1 M level, the scale-bar lengths and the ~20 nm F3 size are listed as text-only facts on the nodes that need them.

## Mode changes
- **n16: mode set to `joint`.** It is the only node with two or more incoming causes edges (n13 excess calcium overcoming the buffer, n14 citrate drawing water into the nucleus). No caption offers a choice between them; the paper needs both, so the mode is joint, not alternative.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
Supports 2, contradicts 0, not covered 1.
- **M1** (Processing -> Structure): in situ liquid-cell TEM plus MD -> rhombohedral COM by a classical pathway, square COM by a non-classical multiphase pathway. **Supports** (n4, n6 -> n8 -> n7 and n6 -> n10 -> n9, meeting at n17; evidence o1, o2, o5, o16). The graph is the more cautious of the two: it does not name the non-classical product COM, and d2 records that the paper's naming rests on corner angles with no diffraction.
- **M2** (Structure -> Performance): rhombohedral and square COM -> formation of kidney stones, via COM binding cell walls more strongly than COD or COT. **Not covered.** n1 states only that CaOx is the main kidney-stone mineral, as the motivation; no node claims a polymorph-to-pathogenesis link or the cell-wall binding, and no panel in the packet bears on it.
- **M3** (Processing -> Property): citrate present during nucleation -> higher hydration state and altered O:Ca ratio. **Supports** (n5 -> n11 -> n14 -> n15 -> n16; evidence o8 from MD, o14 and o15 from EDS/EELS). a2 fairly qualifies it: the EELS 95% intervals overlap, so only the EDS pair separates.
