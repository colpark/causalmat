# Judge review: Acta_Materialia/10.1016_j.actamat.2020.116609

**Verdict:** accept with fixes. Structure-only review: no figures or crops were opened, and panel citations were not ruled on. After the splits the graph has 17 spine nodes and 47 nodes in total. The spine is one connected path: need -> hypothesis -> 3 nm Al/X architecture + X sweep -> sputtering -> periodic nanolayers. From there it runs in two branches: hardness -> wear rate, and galvanic/DFT MECs -> corrosion ranking. Both branches feed the tribocorrosion loss (n13), which is also explained by the depassivation and worn-track coupling MECs and the damage mode. n13 -> conclusion. Every spine STR/PRP/PRF/MEC node has OBS evidence, and n8 and n9 also have KNW premises. There are 3 audits (o10, o16, o21), all fair.

## Changes
- Split n12 into n12 and n21, and n14 into n14 and n22 (details below). Spine went from 15 to 17 nodes.
- Source/requires_unseen fixes on n6, n10, n12, n18, o21 and o27.
- No merges. No read_from changes. No mode changes.

## Splits and merges
- **n12 -> n12 + n21.** The old label stated two mechanisms, each with its own evidence.
  - n12 keeps "Ti raises the work function -> lower surface activity", with o19 as evidence.
  - New n21 is "weaker Cl adsorption -> less chloride uptake". o20 moved to n21.
  - New edges: n6->n21 supports, n7->n21 premise_for, n21->n11 explains.
- **n14 -> n14 + n22.**
  - n14 keeps depassivation from the OCP drop, with o26 as evidence.
  - New n22 is "worn-track anode coupled to the unworn cathode". o25 and o27 moved to n22.
  - New edges: n14->n22 supports, n22->n13 explains.
- Merges: none. No two labels state the same claim. The OBS/claim pairs such as o7/n8 and o24/n13 are a readout and its claim, not duplicates.

## Source / read_from changes
- n6: figure -> text. The ~5-6 nm period is a Bragg conversion that needs the Cu Kalpha wavelength, which is given only in the linked text. The TEM agreement comes from Table 1.
- n10: figure -> text. Two facts come from the caption and linked text of F8, not from the panels: that F8 shows FE corrosion simulations (dashed line = original surface), and the galvanic sacrificial-anode reading.
- n12: figure -> text. Reading a work-function value as surface activity is stated in the F10 linked text.
- n18: stays inferred. requires_unseen was empty; it now lists the MS slope-sign rule and "the capacitance is the passive film's".
- o21: figure -> text. The axis says only "Defect density". "n-type" and "passive layer" come from the caption and text.
- o27: figure -> text. The FE panels show current during tribocorrosion, and the arrows are current lines with thickness proportional to current density. Both facts come from the caption and linked text.
- New nodes n21 and n22 have source text, with their facts listed.
- read_from: no changes. Every OBS node that restates listed annotation strings already has annotation: o5, o13, o15, o17, o20, o26 and o28. o19 and o30 are annotation from in-image strings that are not in the listed annotations, which is acceptable. The axis/pixel readings (o2, o7, o9, o10, o12, o16, o21-o25, o27, o29) do not restate listed strings.

## Mode changes
- None. Only n13 has two or more causes edges (n9, n11). It is "joint", and that is correct: no caption shows a choice between the two causes, and the F6 linked text attributes the loss to low hardness and high corrosion rate together.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 0.
- M1: sputtering -> periodic, semi-coherent nanolayers. **Supports** (n5 -> n6, n7).
- M2: nanolayers -> hardness 3-5x ROM. **Supports** (n6 -> n8 with k2; the 3-5x value is n20). Interface-mediated strengthening is not a node.
- M3: nanolayering -> reduced surface reactivity. **Supports** (n12, n21, with n7 as premise).
- M4: hardness + reduced reactivity -> tribocorrosion resistance. **Supports** (n9 and n11 joint into n13). The graph adds that Al/Cu beats Al/Ti under the chosen condition (n13, n17).
