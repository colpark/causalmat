# Judge review: Advanced_Functional_Materials/10.1002_adfm.202007255

**Verdict:** accept with fixes. This was a structure-only review: no figures or crops were opened, and panel citations and techniques were not ruled on. The graph now has 56 nodes, 72 edges and 16 spine nodes (spine unchanged).

The spine is one connected path: need (n1) -> hypothesis (n2) -> TMO coating choice (n3) -> coating (n4) -> screen: dendrite-free dual layer for all oxides (n5) -> down-select MnO (n7) -> MnO/PP Li||Cu cells (n8) -> MnO reduced to Mn0 + Li2O (n9) -> Mn0/Li2O SEI (n10) -> self-healing MIEC SEI mechanism (n14) -> dual-layer deposit (n12). From there it splits in two:
- **Li||Cu branch:** CE (n15)
- **Li||Li branch:** symmetric-cell overpotential (n17)

These lead to Li||LFP (n18) and Li@Cu||LFP (n19), then to the conclusion (n21).

Every spine STR/PRP/PRF/MEC node has OBS evidence, and n14 also has KNW premises (k6, k7). There are 2 audits (a1: F3h Mn 2p spacing inconsistent with a doublet; a2: MnO/PP without LiNO3 set against a PP control that contains LiNO3). Both are fair. No v04 violations.

## Changes
- Split n14, n5 and n11 (details below).
- n10 label trimmed to the composition claim. The origin (dissolution-migration-reduction) is n23, which explains n10.
- n20 label trimmed to one claim: bare PP gives dendritic, loose Li. The stripping residue is observation o17.

## Splits and merges
- **n14 -> n14 + n26 + n27.** The old label stated three mechanisms.
  - n14 (spine) keeps the self-healing Mn0/Li2O MIEC SEI, with o17, k6, k7, F6a and its explains edges to n12 and n17.
  - New n26 (side, argued): Mn0 seeds nucleate the bottom sphere layer. n10 supports n26, and n26 explains n12.
  - New n27 (side, argued): Li-on-Li wettability gives the top sheets, and n27 explains n12.
  - o14 evidences both n26 and n27.
- **n5 -> n5 + n25.**
  - n5 (spine) keeps the claim that every oxide gives a dendrite-free dual layer.
  - New n25 (side, STR/microstructure/porosity, aspect=ranking, source text) is the claim that CoO and MnO give the densest sphere layer. n4 produces n25, n25 motivates n7, and o1 evidences n25.
- **n11 -> n11 + n28.**
  - n11 keeps the Mn-free surface with Mn0 ~100 nm beneath.
  - New n28 (STR/chemistry/composition, basis attributed): Mn0 is not re-oxidised on stripping. o10 and o11 evidence n28, a1 qualifies it, and n28 supports n14.
- Merges: none. n5/n12, n9/n10 and n6/n25 each state different claims.

## Source / read_from changes
- o14: figure -> text. The plated capacity per panel comes from the F4 caption, and F4 has no panel annotation list.
- o19: figure -> text. That F7a is MnO/PP/MnO and F7b is PP comes from the F7 caption.
- read_from: no changes. o6, o8, o9 and o10 already use "annotation". The other OBS nodes read morphology or curve positions, not listed annotation strings.

## Mode changes
- None. n15 (n12, n10), n18 (n15, n17) and n19 (n15, n12) are all "joint", which is correct: no caption shows an alternative choice.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 1.
- M1: MnO coating -> dual-layer deposit. **Supports** (n3, n4 -> n8 -> n9 -> n10 -> n14/n26/n27 -> n12; o12, o13, o14).
- M2: dual-layer deposit -> dendrite-free deposition. **Not covered.** The graph puts dendrite-free and dual-layer in one node (n12) and attributes both to the MIEC SEI (n14). It has no edge from dual layer to dendrite-free.
- M3: dual-layer deposit -> cycling stability in Li||Li and Li||Cu. **Supports** (n12 -> n15, n17; o19, o21). The graph reads CE ~99% only at 0.2 mA cm-2, and ~91% at 2.0/2.0.
- M4: dendrite-free deposition -> cycling stability. **Supports** (n12 -> n17, n15, n19; n20 control; o18, o24). The ">98% capacity after 150 cycles with GPE" in the record is not read as such.
