# Judge review: Progress_in_Organic_Coatings/j.porgcoat.2021.106233

**Verdict:** accept with changes. This review covers structure only. Figures, panel citations and techniques were not ruled on.

## Spine
There are 20 spine nodes, and they form one connected, stage-ordered path:
- HYP h1 -> h2
- DES d1, d2, d3
- PRC p1 -> p2 -> p3 -> p4 (feeds_into)
- STR s2, s3 (from p2); s5a, s5b (from p4)
- MEC m1 (barrier), m2 (passivation), m3 (chelation)
- PRP prp1 (retained Rc/Rct/Cc) and prpr (2.5 wt% optimum)
- PRF prf1
- DSC c1

The three MEC branches converge on prp1. That is more than two parallel branches, but it is the paper's synergy argument itself (barrier + passivation + chelation), so it was accepted. The control branch is s6 -> prpc -contrasts-> prp1.

Evidence for the spine claims:
- s2 from o4, o5 and o6, with k1
- s3 from o8, o9 and o10
- s5a from o13, s5b from o14, both with k2
- m1 from o15 and o18
- m2 from o22 and o20, with k4
- m3 from o23, with k5
- prp1 from o17a, o17b and o18
- prf1 from o17a and o17b
- prpr now has `basis = argued` (see Changes)

There are 3 audits: o21 (qualifies prpr), and o24 and o24b (both qualify m2). Each changes the support of a spine claim, so they are fair.

## Changes
- **o20 relabelled.** Its label named a data set rather than stating a readout. It now states the reading from its image_note: impedance of the 1, 5, 7.5 and 10 wt% coatings falls, then partly recovers at 40-60 d. The 2.5 wt% part (F6d) is o24's content, so F6 was dropped from o20.
- **o20 edge rewired.** o20 -> prpr (evidences) became o20 -> m2 (evidences). The paper reads a recovery like this as passivation, the same inference o22 draws. The reading says nothing about a peak at 2.5 wt%.
- **prpr set to `basis = argued`.** No OBS evidences the 2.5 wt% optimum any more. The claim rests on |Z|0.01Hz values quoted only in the text, and o21 contradicts the day-0 ranking.
- **Removed o16 -> prp1 (evidences).** o16 is the raw EIS data set that feeds the circuit fits: o15, o17a, o17b, o18 and o24b. prp1 keeps its readouts o17a, o17b and o18.

## Splits and merges
Splits:
- **h1 -> h1 + h1b.** The label stated two needs. h1 keeps "GO coatings lack long-term protection" (spine). The new h1b holds "residual Cl- in HCl-doped PANI accelerates corrosion". It is a side HYP that motivates h2 and d2, and it is off the spine to keep the spine at 20.
- **o24 -> o24 + o24b.** The old node read two figures as one claim.
  - o24 keeps the F6 reading: the Nyquist arcs of the 2.5 wt% coating shrink monotonically, with no rise after 40 d.
  - The new o24b holds the F8a reading: Rc rises only from ~0.9e8 to ~1.3e8 after 40 d. It is derived through the o16 circuit fit.
  - Both qualify m2.

Merges: none. No two labels state the same claim.

## Source / read_from changes
- **source figure -> text, because the band assignment comes from the linked text and refs:** o1, o4.
- **source figure -> text, because the sample or row identity appears only in a caption (the panel's annotations do not name it):** o2, o5, o6, o10, o16, o20, o21, o22, o23, o24, o25, o26, s6.
  - o2 also needs F5b for "absent in GO".
- **source figure -> text, because "after 40 d" appears only in the F10 caption:** s5a, s5b.
- Every change adds the unseen fact to `requires_unseen`.
- **read_from:** none changed.
  - o2, o5, o6 and o25 are already "annotation".
  - The EIS nodes read values off the axes. Their only listed annotations are legend sample names, which is not what the observations state.

## Mode changes
None. prp1 is the only claim with two or more causes edges (s2 and s3). It is correctly "joint", because no caption shows a choice between the two causes.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
**Supports 5 · contradicts 0 · not covered 0**

| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | PA-doped in-situ polymerisation on FGO -> sulfonated FGO with dispersed PANI_PA | supports | p1, p2, s1, s2, s3, o8-o10. The graph notes partial clustering (o8) |
| M2 | FGO/PANI_PA + oxide + [FenPA2] -> higher Rc, Rct, lower Cc | supports | s2, s3, s5a, s5b, m1-m3, prp1, o17a, o17b, o18 |
| M3 | same structure -> 60-d protection, \|Z\| ~1.33e8 | supports | prp1, prf1, m1-m3. 1.33e8 is text-only; o24 and o24b qualify m2 |
| M4 | PA instead of HCl + FGO (processing) -> better than FGO/PANI_HCl/WPU | supports | h1b, d2, p1-p3, s6, prpc, o25, o26. "No Cl 2p in PANI_PA" is not a node |
| M5 | p-ABSA functionalisation -> sulfonic FGO, better dispersion | supports | p1, s1, o1, o2, k1. Only the sulfonic half is covered; the dispersion half was dropped by staff |
