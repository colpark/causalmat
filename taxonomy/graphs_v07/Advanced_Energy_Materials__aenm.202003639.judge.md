# Judge review: Advanced_Energy_Materials/aenm.202003639

**Verdict: accept with minor changes.**

This review checks structure only. No figures or crops were opened. Panel citations, techniques and `image_support` are left to the blind second read.

## Checklist

- **Spine:** 20 connected nodes in stage order, one path from the first HYP to the conclusion:

  need (n1) -> hypothesis that co-inserted Zn2+ makes a Zn-hosting framework (n2) -> two design choices, the citrate-complexed KMnHCF base system (n3) and the 30 m KFSI + 1 m Zn(CF3SO3)2 electrolyte (n4) -> precipitation (n5) and galvanostatic cycling (n7) -> pristine monoclinic KMnHCF (n6), Zn2+ dominant (n8a) and Mn lost (n8b) -> site occupancy (n10) -> Jahn-Teller pathway (n11) and the Coulomb / d-pi trade-off (n12) -> conversion to rhombohedral KZnHCF (n9) -> wider channels (n15), solid-solution storage (n16) and the Fe3+/Fe2+ redox centre (n17) -> 100 mAh/g (n18) on a 1.74 V plateau (n25) -> 98% retention to 400 cycles (n19) -> conclusion (n20).

  Two parallel branches at a time: synthesis and electrolyte meet at n8a/n9; the channel/solid-solution branch and the redox-centre branch meet at n18.
- **Evidence:** every spine STR/PRP/PRF/MEC claim has OBS evidence, a KNW premise, or `attrs.basis` != evidenced:
  - n6: o1, o4, o5 | n8a: o6, o12b | n8b: o12 | n9: o7, o10, o11, o16
  - n10: o20 | n11: o20, o21, premise k3 (o19 contrasts) | n12: basis argued, premise k2
  - n15: basis argued | n16: o14, o17 | n17: o18 | n18: o8 | n25: o8 | n19: o8
- **v04 rules:** pass.
  - n7 stays PRC/stimulus: the cycling produces argued states (n8a, n8b, n9), which is the r04 rule for stimulus vs a PRF condition.
  - The new n24 is STR/chemistry/bonding (coordination converted), not site_occupancy: "how atoms are bonded or coordinated" against "who sits where".
  - n12 stays MEC/tradeoff with basis=argued: which interaction favours which phase is asserted in the F7 linked text, not measured.
  - a1 gains `aspect = ranking` (levels of four elements at one cycle, the r04 trend vs characteristic_value rule for categorical groups).
- **Audits:** 2 (a1, a2), both `text_silent`, both fair and both bounding a spine claim: a1 shows Zn is only third largest at the 4th cycle against the text's "remained high"; a2 shows the fade is complete near cycle 50, so the 100-cycle end point of the conversion is an upper bound.

## Splits and merges

- **n10 -> n10 + n24.** The label stated two claims.
  - n10 (spine) keeps the site preference: inserted Zn2+ takes framework lattice sites rather than Fe(CN)6 vacancies. k1 still contrasts it with the earlier reports where Zn2+ switches between cavity and vacant sites.
  - The new n24 (STR/chemistry/bonding, side) holds the coordination change: MnN6 octahedra completely replaced by ZnN4 tetrahedra linked to octahedral FeC6.
  - n11 causes n24, o20 evidences n24, and n24 supports n15, which is the wider-channel mechanism that reads off that linkage.
- **n18 -> n18 + n25.** The label stated two property values.
  - n18 (spine) keeps the capacity: near 100 mAh/g after the first 100 cycles, down from 138 mAh/g.
  - The new n25 (PRP/value, spine) holds the single plateau averaging 1.74 V and the 150 Wh/kg it gives. n17 explains n25, o8 evidences it, and n25 supports n20, so the conclusion's "high voltage" is now carried on the spine instead of resting on the need node alone.
- **Considered and not split.** n23 ("500-600 nm single-crystalline cubic particles with some surface defects") is one morphological description of the as-made powder, used nowhere downstream, and v04 has no leaf that carries single-crystallinity apart from the phase/identity node n6 that o4 and o5 already evidence. n11 states one pathway and n12 one trade-off, which those leaves are defined to carry.
- **Merges:** none. o12/o12b and n8a/n8b are OBS and STR roles of the same fact, not duplicates; a1 reads the 4th cycle against the text where o12b reads the series; n15 is a mechanism where n24 is a structural state; n13 is one contribution where n12 is the net trade-off.

## Source / read_from changes

- n20: source inferred -> text. The conclusion is the title claim plus the F3 linked-text sentence that the material is a promising ZIB cathode; `requires_unseen` records that the packet has no conclusion section.
- o4: read_from pixels -> annotation. The string `d（220)=0.36nm` is printed on F1e and listed for that panel, so the d-spacing is restated, not measured from the fringes. The packet's `annotated: false` is an OCR artefact (the string was filed under axis labels) and is now recorded in `image_note`.
- o1: read_from axis -> pixels. The reading is the visual coincidence of the calculated and experimental traces and a flat difference curve; no value is read against an axis. Rp/Rwp are text-only, as the node already notes.
- o6: read_from axis -> pixels. The reading is the count of four arrowed redox-peak pairs, not a value read against an axis.
- read_from kept as is elsewhere: o5, o11, o14, o16, o19, o20 each restate a string listed under `annotations` for their panel and are already `annotation`; o7, o8, o10, o12, o12b, o17, o18, a1, a2 read numbers against a plotted axis; o2, o21, o22 are qualitative or scale-bar readings on panels with no annotations.
- n18 `requires_unseen` was rewritten after the split: the 138 and 102 mAh/g values stay text-quoted on n18, the 1.74 V and 150 Wh/kg move to n25.

## Mode changes

None. n9 is the only claim with two or more `causes` edges (n8a and n8b). "joint" is correct: no caption offers Zn insertion and Mn loss as alternatives, and the paper's equations run them together.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)

**Supports 5, contradicts 0, not covered 0.**

- **M1** (cycling in the concentrated KFSI/Zn electrolyte -> monoclinic to rhombohedral with MnN6 replaced by ZnN4): **supports** (n4, n7, n8a, n8b, n9, n24, n11, n12; o10, o11, o12, o12b, o16). The graph routes the pair through the composition change and adds the Jahn-Teller pathway and the Coulomb / d-pi trade-off as the explanation. Audit a2 puts completion near cycle 50 rather than 100, and audit a1 shows the record's "Zn remained high after 4 cycles" is weaker than stated. The Mn3+ disproportionation sub-claim has no node.
- **M2** (rhombohedral KZnHCF with ZnN4 and wider channels -> 100 mAh/g over 400 cycles, 98% retention): **supports** (n9, n24, n15, n16, n18, n19; o8, o14, o17). n15 carries basis=argued: the channel width is stated in the F3 linked text, not measured.
- **M3** (cycling -> single voltage plateau and better redox reversibility): **supports** (n7, n9, n16, n25, n17, n18; o6, o7, o18). The plateau is carried by n16 and n25, reversibility by n17 with the XANES shift o18. The graph makes the plateau a consequence of the conversion n9 rather than of the cycling act directly.
- **M4** (citrate-assisted precipitation -> monoclinic KMnHCF with few vacancies and high crystallinity): **supports** (n3, n5, n6, n23; o1, o4, o5). The low-vacancy half sits in the DES node n3 (label and `attrs.reason`) because its evidence, the ICP/TGA formula, is off-packet and listed in `requires_unseen`.
- **M5** (rhombohedral structure with ZnN4 -> high Fe3+/Fe2+ reversibility and low polarization): **supports** (n9, n17, n16, n25, n11; o18, o21). Reversibility is supported through n9 -> n17 with the reversible XANES shift o18. "Low polarization" has no node, and the graph uses the DOS degeneracy relief (o21, n11) to explain the phase transition rather than the redox reversibility.
