# Judge review: Advanced_Composites_and_Hybrid_Materials/s42114-021-00414-x

**Verdict:** accept with fixes. This review checks structure only. No figures or crops were opened, and no panel citations or techniques were ruled on (the blind second read checks those). Splits: 8 (s11, o9, s12, o12, s13, s17, s24, o27). Merges: 0. Source changes: 2 (s6, s11). read_from changes: 3 (o4, o6, o7). Mode changes: 0. MatMech: 4 supports / 0 contradicts / 0 not covered.

The graph now has 55 nodes, 71 edges and 20 spine nodes. It passes the structural checks: v04 leaf types, rels and mm_ops, an mm_op on every figure-OBS edge, source/requires_unseen on every node, read_from on every OBS node, spine connectivity and spine support. Pre-judge copy: `.v07work/Advanced_Composites_and_Hybrid_Materials__s42114-021-00414-x.pre_judge.json`.

## 1. Spine order

- The spine reads: need s1 -> hypothesis s2 -> PDMS/SCF base s3, GB@rGO modification s4, content/thickness sweep s5 and SCFNA route s6 -> GB@rGO synthesis s7 -> composite forming and compression s8. From there two branches:
  - thickness: in-plane SCF orientation s11 + network compaction s25 (joint) -> lambda vs thickness s14;
  - content: rGO coating s9, gap filling at 1 wt% s12 and matrix dispersion at 2-6 wt% s26 (joint) -> lambda optimum at 1 wt% s15, explained by volume exclusion s13 and the shell/core heat-loss pathway s27.
  The branches meet in the heater-plate test s17 and the CPU TIM test s28, which end at conclusion s20.
- Every spine STR/PRP/PRF/MEC node is backed: s9 by o2 and o4; s11 by o9 and o10; s25 by o30; s12 by o12; s26 by o31; s14 by o13; s15 by o14; s17 by o19; s28 by o20; s13 by k5 (new); s27 by k4.
- The v04 decision rules hold. s25 and s26 are STR/microstructure/distribution (connectivity; dispersion). s27 is MEC/pathway (argued). s17 and s28 are PRF/service_capability.
- Audits: 4, all fair. o3 shows detached flakes against "no rGO separation". o5 shows C=O/O-H still labelled against "disappear". o15 shows that the 1-wt% optimum is absent at 0.4 mm. o25 shows that sigma and lambda do not co-vary at 2-4 wt%, which qualifies s22.

## 2. Splits and merges

| node | into | why |
|---|---|---|
| s11 | s11, s25 | in-plane orientation vs network compaction as thickness falls; s25 now drives s14, with s11 as a joint cause |
| o9 | o9, o30 | fibre orientation in the sections vs packing density against thickness |
| s12 | s12, s26 | gap filling at 1 wt% vs dispersion in the matrix loosening the network at 2-6 wt%; s26 joins the causes of s15 |
| o12 | o12, o31 | 1-wt% bubbles between fibres vs 4-6 wt% bubbles in matrix regions; the "loosening not evident" note goes with o31. o12's op became inspect_local_feature because only one condition remains |
| s13 | s13, s27 | volume exclusion of PDMS vs the conducting-shell/insulating-core heat-loss pathway; s9, s10 and k4 moved to s27 |
| s17 | s17, s28 | heater-plate ranking by content vs CPU core 5 C below commercial grease |
| s24 | s24, s29 | foldable into shapes vs bending durability over 10000 cycles |
| o27 | o27, o29 | the same split for the photograph readings |

Other changes:
- k5 added (KNW/fact, text): PDMS lambda is 0.27 W/m K. It is the premise for s13, which had no OBS or KNW support after the split.
- s12 -> s23 causes became s26 -> s23. Placing 1 wt% in the gaps does not cause strength loss; more bubbles acting as weak points does.
- s23 -> s24 changed from causes to supports.
- s14 was relabelled to thickness only, and s14 and s15 were trimmed to 20 words or fewer. Some OBS labels are still over 20 words (o4, o14, o19, o25, o26); I left them unchanged.

Merges: none. No two nodes state the same claim.

## 3. Source and read_from changes

| node | change | fact listed |
|---|---|---|
| s6 | source figure -> text | SCFNA name and the reason for forced assembly (linked text) |
| s11 | source figure -> text | which view is in-plane vs out-of-plane, and the compression axis (F5/F6 captions) |
| o4 | read_from axis -> annotation | band positions '1347em', "1582cm'" are written on F4a |
| o6 | read_from axis -> annotation | 'Si-O-Si' label on F4b |
| o7 | read_from axis -> annotation | 'C1s', 'Ols' labels on F4c |

The new nodes carry their own source:
- text: s26, s27, k5, o31;
- figure: s25, s28, s29, o29, o30.

o22 stays annotation. Its bar values (1330/651/480) are drawn in the image, although the packet lists only the axis titles as annotations. o28 also stays annotation ('Thiswork').

## 4. Mode changes

None. The multi-cause claims are:
- s15 (s9, s12, s26);
- s17 (s14, s15);
- s14 (s25, s11, new);
- s28 (s14, s15, new).

All are joint. No caption shows a choice between the causes.

## 5. MatMech tally (recorded after the graph was final; the graph was not edited)

supports 4, contradicts 0, not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | SCFNA compression and curing -> compact aligned SCF network, GB@rGO in gaps | supports | s6, s8, s11, s25, s12 | the graph limits gap placement to 1 wt%; at 2-6 wt% GB@rGO disperses (s26) |
| M2 | compact network + core-shell GB@rGO in gaps -> lambda 23.4, sigma 1330, elongation 86.75% | supports | s25, s12, s9, s13, s27, s15, s16, s22, s23 | lambda and sigma are supported. In the graph elongation falls with GB@rGO (s26 -> s23). Electron-dominated conduction is qualified by o25 |
| M3 | high lambda -> TIM heat transfer (CPU -5 C), stable over 5 cycles | supports | s14, s15, s17, s28, s18, s24, s29 | s18 holds as reversibility only (lambda is ~17% lower at 100 C) |
| M4 | compression to 0.1 mm -> lambda 23.4 and sigma 1330 | supports | s8, s25, s14, s15, s12, s16 | lambda vs thickness is supported. The sigma rise is a content effect in the graph (s12 -> s16), not compression. 0.367 (2 mm) is the 0-wt% value |
