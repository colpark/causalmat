# Judge review: Journal_of_Magnesium_and_Alloys/j.jma.2020.09.027

Hydrogen storage in Mg90Ce5Y5 catalysed by carbon-cobalt composites (C@Co). This is a structure-only review. No figures or crops were opened, and no ruling was made on panel citations or techniques.

## Verdict
Accepted with fixes.

The spine runs:
- need n1 -> hypothesis n2 -> base system n3 and modification n4;
- n4 -> C@Co synthesis n5 -> milling n8, with n5 -> carbon defects n6;
- n8 -> inert catalyst n9 (thermodynamic control n19) and carbon/Co distribution n10;
- n10 -> the MECs n11, n12 and n13 -> faster absorption n14;
- n6 and n10 -> JMAK exponent n16 -> rate-step change n17 -> faster desorption n15, with n6 -> activation energy n18 -> n15;
- n10 -> activation n20;
- everything meets at the conclusion n21.

There are 20 spine nodes, all connected from n1, and the graph is stage ordered. Branching:
- The two main branches are absorption and desorption. n19 is the control branch.
- n20 is a one-node activation leaf. It is the only PRF, so it stays on the spine; this goes one past the branch guidance.

After the fixes, every spine STR/PRP/PRF/MEC node has OBS evidence or a KNW premise. The PRP/diagnostic n16 -> KNW/lookup k3 -> MEC/identification n17 chain meets the v04 rule. There is one audit: a1 (patchy carbon coverage) qualifies n10, and it is fair. The graph now has 70 nodes and 94 edges.

## Changes
- **Broke a cycle.** n15 -supports-> n16 closed the loop n15 -> n16 -> n17 -explains-> n15. The JMAK exponent is fitted from the isothermal curves (o24 -derives-> o26), not taken from the desorption claim. I removed that edge and added n6 -causes-> n16 and n10 -causes-> n16, both mode joint. This follows the F8/F9 linked text, which attributes the change to C defects (nucleation) and Co (H recombination) together.
- **Premises for unsupported spine MECs.** n11, n12 and n13 had neither evidence nor a premise. I added:
  - k8 (carbon defects as nucleation sites, ref. [34]) -premise_for-> n11;
  - k9 (two-stage hydrogenation: nucleation-controlled, then diffusion-controlled, ref. [40]) -premise_for-> n12;
  - o20 (the second stage shortens from 66 to 11 min) -evidences-> n12 (compare_across_conditions);
  - k10 (two desorption rate-limiting steps, ref. [42]) -premise_for-> n13.
- **n27 property family.** Changed from ionic_electrochemical to thermodynamic, because this is equilibrium hydrogen uptake, not a redox capacity.

## Splits and merges
- **n7 -> n7, n7b.** n7 is the uniform dispersion of Co (distribution). n7b is Co NPs below 50 nm (feature_size). o7 evidences both: measure_feature_metric -> n7b, and assess_spatial_distribution -> n7. n7 keeps its causes edge to n18.
- **n25 -> n25, n25b.** n25 is particle size (feature_size). n25b is irregular spherical rather than flat particles (shape). o13 evidences both.
- **n27 -> n27, n27b.** n27 is the capacity drop from 5.1 to 4.56 wt% (PRP/value). n27b is a MEC/pathway: C@Co absorbs no hydrogen and so dilutes the absorbing mass (text, attributed). n27b -explains-> n27.
- **Merges: none.** The claim/OBS pairs (n16/o26, n18/o27, n19/o29) have distinct roles. o14 and a1 read different content from F4c.

## Source / read_from changes
- **n6: figure -> text.** It needs the ID/IG -> defect-density mapping (ref. [33]) and the claim that defects are catalytic sites (ref. [34]).
- **n22: figure -> text.** The graphene-like assignment comes from the linked text. The fcc Co structure comes from the PDF card, not from a panel.
- **o10: figure -> text.** That panel a is the ball-milled state is given only in the caption.
- **o15, o17, o18: figure -> text.** The sample states (ball-milled or dehydrogenated C10) are given only in the F5 caption.
- **requires_unseen filled** on the text claims n11, n12, n13, n21, n28 and n30.
- **read_from: o23 axis -> annotation.** Its label restates the R10min values the authors printed on the bars. This matches the treatment of o20's 66/11 min tokens.
- **Kept as they are:**
  - o19, o14 and a1 mention legend or colour-key strings, but their content (curves, spatial arrangement) is read from the axis or pixels.
  - Every other annotation-type node already carries "annotation".

## Mode changes
None. There are three multi-cause claims, and all stay "joint", because no caption shows a choice between the causes:
- n14 (n6, n10);
- n18 (n6, n7);
- n16 (n6, n10), which has new edges.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | carbonization at 800 C -> defective C nanosheets, uniform Co NPs <50 nm, 3.88 nm mesopores | supports | n5, n6, n7, n7b, n22, n24, o2, o4, o7 |
| M2 | ball-milling with 10 wt% C@Co -> refinement, smaller particles, C/Co on alloy surfaces | supports | n8, n10, n25, n25b, o13, o14 |
| M3 | C defects + dispersed Co -> Ea 130.3 -> 81.9 kJ/mol | supports | n6, n7, n11, n18, o27 |
| M4 | mesopores + C nanosheets (diffusion) -> desorption time 150 -> 11 min | not covered | n24, n12, n14, n15, o24 |
| M5 | C defects + Co -> rate-limiting step surface -> nucleation and growth | supports | n6, n10, n13, n16, n17, k3, o26 |
| M6 | carbon layers on particles -> full activation in first cycle | supports | n10, n20, n28, o19 |
| M7 | smaller particles + catalytic sites -> onset 341.0 -> 267.0 C | supports | n6, n18, n15, o25 |

supports 6 / contradicts 0 / not covered 1

Notes on the tally:
- **M2:** the grain refinement and amorphization seen as XRD broadening are only in o10's image_note, not a claim.
- **M4:** the graph ties the diffusion-channel mechanism n12 to absorption, following the paper's F6 text. It ties the desorption speed-up to Ea and the rate-step change. Mesoporosity (n24) has no causal edge.
- **M7:** only the catalytic-site path is in the graph. Particle size has no edge to n15.
