# Judge review: Biomaterials/j.biomaterials.2010.02.024

Controlling silk fibroin particle features for drug delivery. This is a structure-only review. No figures or crops were opened, and no ruling was made on panel citations or techniques.

## Verdict
Accepted with fixes. The spine runs:
- need s1 -> hypothesis s2 -> base system s3, route s4 and variable sweep s5 -> salting out s6.
- s6 then splits into three lines:
  - size s8 -> conclusion s17;
  - secondary structure s9 -> CV release by pH s15;
  - pH/charge pathway MEC s10 -> zeta s11 -> loading s12 and charge-binding MEC s13 -> burst ranking s14.
- s14 and s15 join at the PRF s16 -> conclusion s17.

There are 16 spine nodes, all connected, and every spine STR/PRP/PRF/MEC node has OBS evidence. The pH line splits at s10 into a structure branch and a charge branch that rejoin at s16. Counted that way, the graph stays within the limit of two branches. There are two audits: a1 (RhB efficiency never near 100%, which bounds s12) and o12 (rules out x6). Both are fair. The graph has 47 nodes in total, above the aim of 40, because of the two splits.

## Changes
- Removed s9 -causes-> s11. The paper (F4) presents secondary structure and zeta potential as parallel outcomes of production pH; it never says structure sets charge. s11 stays on the spine through s10 -explains-> s11.
- Added s13 -explains-> s14. The release ranking by drug charge is explained by charge-charge binding.
- Changed o19 -> s10 from premise_for to evidences. The computed domain charge/pI table is the evidence for the argued pathway.
- Trimmed the s8 label to the size claim and moved the distribution broadening to attrs.
- Trimmed the o1 label to the gelation/particle boundary and moved the efficiency trend to image_note.

## Splits and merges
- **x3 -> x3, x3b.** x3 is silk I stability in ethanol and methanol (evidence o5). x3b is sonication stable up to 40 s, converting at 60 s (evidence o6, premise k3). s9 supports both.
- **x4 -> x4, x4b.** x4 is ethanol sterilisation (text). x4b is the guidance to keep sonication under ~40 s (inferred, supported by x3b).
- Merges: none. No two nodes state the same claim; the claim/OBS pairs (s11/o12, s14/o17, s15/o18) play distinct roles.

## Source / read_from changes
- s12: figure -> text. It needs the facts that the drugs are positively charged and that the efficiency drop means matrix saturation (F6 linked text).
- o9: figure -> text. Its requires_unseen already listed the panel concentrations (caption only).
- o11: figure -> text. The meanings of the FSD peak letters (B = beta sheet, A = helix) and the pH 6 / pH 8 identity of the panels come from the F4 caption.
- requires_unseen filled on s5 and x4. o19 requires_unseen cleared: the ProtParam tool name is metadata, not part of the label, and now sits in attrs.tool_note.
- read_from: no changes. o1 and o19 already restate listed annotations and are "annotation". The other OBS nodes read values off axes or band positions and morphology from pixels.

## Mode changes
None. s16 is the only claim with two causes edges (s14, s15). It stays "joint", because no caption shows a choice between drug charge and secondary structure. The removal of s9 -> s11 left s11 with no causes edge.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | salting out at pH 6 -> silk II structure | supports | s6, s9, s10, o10, o11 |
| M2 | salting out at pH 9 -> silk I structure | supports | s6, s9, s10, o10 |
| M3 | more silk II (pH 7) -> larger CV burst | supports | s9, s15, o18, o10 |
| M4 | more silk I (pH 9) -> slower, sustained CV release | supports | s9, s15, o18 |
| M5 | higher production pH -> more negative zeta | supports | s6, s10, s11, o12 |
| M6 | negative zeta -> high cationic drug loading | supports | s11, s12, s13, o13, o15 |
| M7 | ionic strength < ~0.75 M -> no particles | supports | x1, o1, o2 |

supports 7 / contradicts 0 / not covered 0

Notes on the tally:
- M4's permeability mechanism is not in the graph.
- M6's higher-pH comparison is not tested: loading was measured only on pH 8 particles. The graph carries the negative-charge -> loading link.
