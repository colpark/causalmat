# Judge review: Advanced_Materials/10.1002_adma.202003852

Oriented Perovskite Growth Regulation Enables Sensitive Broadband Detection and Imaging of Polarized Photons Covering 300-1050 nm

**Verdict: accept with minor changes.** After review the graph has 59 nodes and 76 edges, 16 of them spine.

This is a structure-only review. The judge opened no figure or crop. Panel citations and techniques are left to the blind second read.

## Checklist
- **Spine:** 16 connected nodes, with two branches that meet at n13. The path runs need (n1) -> hypothesis (n2) -> Sn-Pb quasi-2D base (n3) + NH4SCN/NH4Cl (n4) -> spin coating (n5). From there:
  - branch (a): out-of-plane orientation (n6) -> absorption dichroism (n9, dipole MEC n10) -> polarization-dependent photocurrent (n11, transport MEC n12);
  - branch (b): uniform Pb-Sn lattice (n7) -> NIR absorption (n8).
  
  The branches meet at broadband polarized responsivity (n13), which leads to D* (n14, joint with noise n21) -> imaging (n15) -> conclusion (n16). This matches the paper's argument.
- **Evidence:** every spine STR/PRP/PRF claim has an OBS evidences edge. MEC n10 has premise k3. MEC n12 had no evidence and no premise, so I added k5 (ref. 42, transport channels).
- **v04 rules:** pass. I checked types, rels and mm_ops against vocab/v04.json.
- **Audits:** 4 (o5, o7, o15, o19). Each audit qualifies the claim it bears on.

## Changes
- n9 split into n9 (absorption dichroism, o10) and n27 (PL anisotropy, o9 and o11). The paper explains the two by different mechanisms: refractive-index anisotropy for absorption, exciton anisotropy for PL. Added n6 -causes-> n27.
- n18 split into n18 (crystallite size, from FWHM via Scherrer) and n28 (STR/phase/fraction, crystallinity).
  - n28 is basis argued and source text: the ~100x intensity rise is in the text only, because the F1f intensities are scaled nonproportionally.
  - Added n5 -produces-> n28 and o7 -qualifies-> n28.
  - Rewired n18 -causes-> n24 (speed) to n28 -causes-> n24. The text credits the faster response to crystallization.
- n19 split into n19 (roughness, Ra 33.9 -> 16.6 nm) and n29 (STR/microstructure/porosity, fewer pinholes; o1 evidences it). Added n29 -causes-> n20 (joint) and n29 -supports-> n22. The n22 label now names all three leakage factors.
- n23 split into n23 (lifetime, 4 vs 14 ns) and n30 (MEC/pathway, Sn-site traps, basis argued). Added n30 -explains-> n23 and n7 -supports-> n30.
- k5 KNW/precedent added as a premise for spine MEC n12.
- requires_unseen filled on n1 (the introduction is not in the packet), k1 and k4.

## Splits and merges
- Splits: n9 -> n9 + n27; n18 -> n18 + n28; n19 -> n19 + n29; n23 -> n23 + n30.
- Merges: none. The OBS/claim pairs o2/n8, o18/n21 and o23/n14 play different roles, so they are not duplicates.

## Source / read_from changes
- Source: n21 and o18 changed figure -> text. That the trace is *dark* noise current appears only in the F4b caption.
- read_from: no changes. o13 is already "annotation". In every other OBS node the listed annotation strings only identify a series or sample, and values are read from the axis or pixels.

## Mode changes
None. n14 (n13 + n21, the D* equation) and n20 (n18 + n19 + n29, leakage) are "joint", which is correct: no caption presents either set of causes as a choice.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 0.
- **M1** (additives -> (202) orientation): supports (n4, n5, n6, o4, o6). The graph qualifies it with o5 (isotropic GIWAXS halo) and o7 (the no-additive XRD already shows the same two reflections).
- **M2** ((202) orientation -> polarization ratio): supports (n6, n9, n27, n10).
- **M3** (polarization ratio -> broadband polarized detection and imaging): supports (n9, n11, n13, n15, n16). In the graph, the broadband reach comes from the Sn-Pb composition branch (n7 -> n8 -> n13). The 0.41 ratio at 900 nm is not in the graph.
