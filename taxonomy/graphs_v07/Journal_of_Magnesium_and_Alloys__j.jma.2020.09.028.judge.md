# Judge review: Journal_of_Magnesium_and_Alloys/j.jma.2020.09.028

**Verdict:** accept with fixes. This review checks structure only. No figures or crops were opened, and panel citations were not ruled on.

The graph has 47 nodes, 65 edges and 17 spine nodes. The spine is one connected path:
- need (h0) -> hypothesis (h1) -> AZ31 base (d1) + twin-then-anneal route (d2, purpose decouple) -> T6 (p1) -> TD compression (p2) -> anneal (p3);
- twinning c-axis rotation (s2) -> prismatic plates (s3). The anneal removes twin boundaries (s6);
- branch 1: s3 -> blocking MEC (m1) -> basal CRSS up (pr1) -> ACA-45 deg CYS +~20 MPa (pr2). s6 supports pr2 as the decoupling control;
- branch 2: s3 -> CRSS ratio down (pr4) -> prismatic-slip MEC (m3) -> fracture strain kept (pr5);
- both branches meet at c1.

There is no PRF stage, because no use condition is tested. This is noted in the graph. Every spine STR/PRP/MEC node has OBS evidence or a KNW premise: s2 (o4, o5, k1), s3 (o8, k1, k6), s6 (o2, o3), m1 (k2), pr1 (o15), pr2 (o10), pr4 (o16), m3 (o12, k4), pr5 (o11).

There are 3 audits (a1, a2, a3), all fair:
- a1: the SF gap 0.43 vs 0.40 qualifies s7, "similar orientation";
- a2: the imaged plate size vs D = 32.5 nm qualifies pr1;
- a3: resolved-shear dtau vs normal-stress CYS qualifies m1.

The AC-45 deg extra-strength branch (s4, m2, pr3) is correctly kept off the spine.

## Changes
- m1: source changed from figure to text (details below).
- o17: read_from changed from axis to annotation.
- o11: the label stated two readouts from F6 (fracture strain, and peak stress). Peak stress is used by no claim, so it was moved to image_note rather than split into an orphan OBS node.
- requires_unseen filled on the inferred nodes a1, a3 and c1. Their source values are unchanged.

## Splits and merges
- Splits: none, apart from the o11 label trim above. pr3 (AC vs A, and AC vs ACA) and pr7 / o13 (mixed fracture mode, and a larger ductile share) each state one comparison set, so they are kept.
- Merges: none. o15/pr1, o16/pr4 and o17/pr8 are readout/claim pairs, not duplicates.

## Source / read_from changes
- m1: figure -> text. Two facts come from text, not from a panel:
  - The "prismatic plates block basal glide more strongly" argument is stated in the linked text of Fig. 8, with refs 4 and 11.
  - The packet F8 has an empty caption, and the Fig. 8 caption sits under F9. So the identity of the slip plane and of the plates is not given with the panel.
- a1, a3, c1: stay inferred. requires_unseen now lists:
  - sample identity from the caption;
  - the Schmid-law conversion;
  - for a3, that A holds basal plates only through k6;
  - for c1, the AZ31 route from the linked text.
- o17: axis -> annotation. The label restates the listed F10g annotation "YS(prism)/YS(basal)".
- The other OBS read_from values were checked against the listed annotations and are correct. o1, o3, o4, o7, o13 and a1 are annotation. The rest are pixels or axis and restate no listed string.

## Mode changes
None.
- s3 (s1 + s2) is joint, and that is correct: the plates must exist and the lattice must twin.
- pr3 (pr1 + s4) is joint, and that is correct: the linked text adds the plate term and the twin-boundary/dislocation terms together.
- No caption offers a choice between causes in either case.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 1.
- **M1:** ageing, then TD compression, then anneal -> basal-to-prismatic plates, twin grain refinement, and twin boundaries removed. **Supports** (p1, p2, p3 -> s1, s2, s3, s4, s6).
- **M2a:** prismatic plates + refined grains -> CYS +~40 MPa. **Supports** (pr1 + s4 jointly -> pr3, with m2). The graph also isolates the plate-only +~20 MPa in pr2.
- **M2b:** the same cause -> compression ratio +22%. **Not covered.** There is no claim node for the AC-45 deg ductility gain. o11 reads 0.28 vs 0.25 (~12%) and flags the 22%.
- **M3:** full route -> strength and ductility both improved. **Supports** (pr2, pr4, m3, pr5, c1), with one difference: the graph claims ductility is *retained* (ACA), not improved.
- MatMech's CYS values (75 / 115 / 96 MPa, from Table 1) differ from the F6 knees read in o10 (~65 / ~70-115 / ~87 MPa). This is recorded only; Table 1 is not in the packet.
