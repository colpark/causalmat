# Judge review: Nature_Materials/10.1038_nmat2372

**Verdict:** accept with fixes. This was a structure-only review. No figures or crops were opened, and panel citations were not ruled on. The graph now has 15 spine nodes and 46 nodes in total. The spine is one connected path: need (n1) -> hypothesis (n2) -> down-select of Li muconate / Li terephthalate (n3) -> synthesis (n4) -> electrode forming (n7) -> galvanostatic cycling (n8). At n8 it splits into two branches:
- **Reduction branch:** n9, the reduced state with altered bonding. n9 leads to the low-voltage plateau (n13, which m0 explains) and to the low heat release with electrolyte (n18). Both meet in the safety claim (n16).
- **Reversibility branch:** n10 -> reversible capacity (n14) -> slow fade (n15).

Both branches end in c1. Every spine STR/PRP/PRF/MEC node has OBS evidence, or a KNW premise when its basis is argued (m0: k8; n16: k3, k4). There are 2 audits, a1 and a3, both text_silent and both fair. a1 qualifies "remains amorphous" (n12). a3 qualifies full reversibility (n10).

## Changes
- **Spine rewire.** The edge n13 -> n18 was a causes edge from plateau voltage to lower heat release. That is not physical causation, so I removed it. I added n9 -> n18 causes: the heat is measured on the reduced state, with no pathway argued. I also added n13 -> n16 supports: the safety claim compares the 0.8 V and 1.4 V electrodes with graphite and LTO.
- Two nodes were narrowed to one claim each. n1 keeps only the need (its graphite-reactivity clause is k3, now k3 -> n1 premise_for). n13 keeps only the plateau potentials (the uptake amounts and the 100-200 mV polarization moved to attrs).
- The spine stays at 15 nodes.

## Splits and merges
- **n9 -> n9 + n9b.**
  - n9 keeps the altered carboxylate/ring bonding, with o7 and o9 as evidence.
  - New n9b (STR/chemistry/composition, off-spine) is "unpaired electrons / radical anions". o13, o14 and k1 moved to n9b.
  - New edges: n8 -> n9b produces, n9b -> n9 supports.
- **k4 -> k4 + k6.**
  - k4 is Li4Ti5O12 at 1.5 V and 150 mA h/g, a premise for n16.
  - k6 is "graphite needs Cu collectors", a premise for d1.
- **n11 narrowed to the conversion on Li uptake.** Its "reverts to pristine" clause restated n10, so it was merged into n10. n10 already has o11 as evidence. I removed o11 -> n11 and n11 -> n10.

## Source / read_from changes
- o1: figure -> text. That the full line is the Rietveld profile (and the dotted line the data) is stated only in the caption.
- o13: figure -> text. The black trace being x = 3 is stated only in the caption.
- o14: figure -> text. That the inset is the echo field-sweep spectrum is stated only in the caption.
- o15: figure -> text. The electrolyte condition comes from the caption and linked text.
- n18: figure -> text. The electrolyte condition and the lithiation levels x = 2.3 and 1.2 come from the F7 linked text.
- New n9b is inferred. It needs the g ~ 2 -> radical lookup (k1).
- read_from: no changes. No OBS node restates a listed panel annotation. o5 and o15 are annotation from on-image labels on F4 and F7, which have no packet annotation list. That is acceptable.

## Mode changes
- None. No claim has two or more causes edges. n13 and n18 each have one, from n9.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 2, contradicts 1, not covered 0.
- M1: acid-base synthesis -> single-phase crystalline salts. **Supports** (n4 -> n5, o1, k5).
- M2: crystalline structure -> reversible capacity ~300 / ~150 mA h/g. **Contradicts.**
  - The graph attributes the capacity to the reversible molecular redox (n10 -> n14).
  - Li muconate loses crystalline order on discharge (n12, m1) yet cycles reversibly.
  - The graph's muconate capacity is ~170-180 mA h/g, not ~150.
- M3: lower thermal reactivity -> safer cells. **Supports** (n18 -> n16, o15, k3).
