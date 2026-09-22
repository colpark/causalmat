# Judge review: Materials_Characterization/j.matchar.2020.110200

**Verdict:** accept with fixes. This is a structure-only review. No figures or crops were opened, and panel citations and techniques were not ruled on.

After the fixes the graph has 19 spine nodes, 43 nodes and 63 edges. The spine is one connected, stage-ordered path:
- HYP gap (n1) -> SPT method (n2), IN718 base (n3) and orientation x temperature sweep (n4) -> SLM build (n5).
- n5 -> columnar grains (n7), cube texture (n8), Laves distribution (n9) and argued residual stress/dislocation density (n11).
- It then splits into two branches:
  - RT branch: n7, n11 -> zone II (p2) -> max force (p1); n7 -> fracture mode (p3). Explained by m1 (Schmid factor / grain rotation).
  - 650 C branch: n7, n11, n9 -> side-disc force loss (p4); n7, n9 -> fracture mode (p5). Explained by m2 (dynamic recovery) and m3 (grain-boundary weakening).
- Both branches meet in f1 (the orientation ranking reverses), which leads to c1.

Every spine STR/PRP/PRF/MEC node has OBS evidence or a KNW premise. n11, m1, m2 and m3 are basis=argued, and each has a KNW premise (k3, k2, k5 and k7). There are 2 audits, both fair:
- a1: cube texture makes the punch axis <100> in both discs, which weakens the crystallographic part of m1.
- a2: the 650 C "top better" ranking rests on a ~6% difference with nearly overlapping error bars.

n4 (variable_sweep) realizes p1 and p4 directly. This is kept: the orientation/temperature levels are realized by the SPT measurement itself.

## Changes
- Split m2, k5 and p2 (details below). The spine went from 18 to 19 nodes (m3 added).
- Added k1 premise_for p6. p6 uses the same zone naming as p2.
- Source fixes on p2, p3, p5 and p6. Added a requires_unseen entry to n5. One read_from fix (o5).
- No merges. No mode changes.

## Splits and merges
- **m2 -> m2 + m3.** The old label stated two mechanisms.
  - m2 keeps dynamic recovery of the high SLM-induced dislocation density (n11 supports, k5 premise).
  - New m3 is weakening of the long columnar grain boundaries at 650 C. It is spine. p5 -> m3 and p6 -> m3 supports were moved from m2. New edges: n7 -> m3 supports, k7 -> m3 premise_for, m3 -> p4 explains, m3 -> c1 supports.
- **k5 -> k5 + k7.**
  - k5 keeps "dislocations move under lower force at high T".
  - New k7 is "grain boundaries become weaker than grain interiors at high T" (prior_knowledge).
- **p2 -> p2 + p7.**
  - p2 keeps "RT zone II wider for the side disc", which feeds p1 and is explained by m1. The "(more work hardening)" gloss was dropped because m1 carries it.
  - New off-spine p7 is "RT zone III wider for the top disc" (o13 evidences, k1 premise_for).
- **Kept as one node:**
  - n11 (residual stress and dislocation density): the paper argues them as one chain from layer count, and neither is measured.
  - p3, p4, p5 and f1: each states one side-vs-top contrast.
- **Merges:** none. o11 and o12 read different comparisons of F7 (RT ranking vs temperature change). a2 is the audit reading, not a duplicate.

## Source / read_from changes
- p2: figure -> text. Zone II = plastic bending is a fact from the F1 linked text (carried by k1).
- p6: figure -> text, for the same reason as p2.
- p7 (new): text, for the same reason.
- p3: figure -> text. The graph's own evidence o15 is partial: dimples are not resolved at 2000x. The ductile/dimpled classification comes from the F9 linked text.
- p5: figure -> text. The identification of the top-disc particles as intercellular Nb-rich precipitates comes from the F9 linked text and Table 4 EDS, which is not in the packet.
- n5: stays text. Added "shifting/rotating scan strategy (F3 linked text)" to requires_unseen.
- m2, m3: text, argued.
- read_from, o5: axis -> pixels. The relative peak heights on an arbitrary-unit intensity axis are read from the traces, and no listed annotation string is restated.
- read_from, others: o6, o7 and o8 already have annotation, and they restate listed strings (Max=5.938/5.262, Ta|dx=2.45 / Tex.ldx=2.56, Laves / ChainofLaves). o16 is annotation from in-image strings on F9, which has no panel list; this is acceptable. o11-o14 and a2 are axis readings; o1, o3, o15, o17 and a1 are pixel readings. All of these are correct.

## Mode changes
None. There are three claims with two or more causes edges, and all are "joint". That is correct, because no caption shows a choice between causes:
- p2 (n7, n11): the F10 text gives grain orientation, residual stress and MPBs together.
- p4 (n7, n11, n9): the F7/F10 text lists grain boundaries, dislocation density and Laves chains together.
- p5 (n7, n9): the F9 text says grain boundaries govern the side fracture and intercellular Laves regions govern the top fracture, and together they give the contrast.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 0.
- M1: SLM processing -> columnar <001> grains (side), equiaxed grains + intercellular Laves (top), (100) fibre texture in both. **Supports** (n5 -> n7, n8, n9).
- M2: grain morphology/Laves/texture -> side 54% higher max force at RT, side drop at 650 C, top unchanged. **Supports** (n7, n11 -> p2 -> p1; n7, n11, n9 -> p4; m1, m2, m3).
- M3: microstructure -> fracture modes (side ductile / top brittle at RT; side intergranular / top facets with Nb-rich particles at 650 C). **Supports** (n7 -> p3; n7, n9 -> p5).
- M4: SLM processing -> anisotropic max force at RT and 650 C. **Supports**, through STR (n5 -> n7/n9/n11 -> p1, p4). One inner step of M4 ("top view lacks strong texture") conflicts with n8 (strong cube texture in both views), but the cause->effect pair itself holds.
