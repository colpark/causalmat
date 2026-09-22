# Judge review: Nano_Letters/10.1021_acs.nanolett.0c03980

**Verdict:** accept with changes. This review covers structure only. Figures, panel citations and techniques were not ruled on.

## Spine
There are 16 spine nodes, and they form one connected, stage-ordered path:
- HYP n1 -> n2
- DES n3, n4, n5
- PRC n6 and n24 (parallel lithography inputs) -> n7 (slapping, joining)
- STR n9
- PRP n13 (optical resonance) and n14 (mechanical modes), as two branches
- MEC n12 -> PRP n15
- PRF n16 -> n17
- DSC n19

Every spine STR/PRP/PRF/MEC claim has OBS evidence:
- n9 from o1
- n13 from o4
- n14 from o5 and o6
- n12 from o3
- n15 from o7, with KNW k2
- n16 from o7
- n17 from o7, with KNW k3

There are 2 audits (n22, n23). Both qualify a spine claim, n17 and n15. The v04 decision rules hold:
- slapping is PRC/joining (adhesive/vdW bonding of pre-made bodies)
- lithographic patterning is PRC/forming
- placement is STR/microstructure/distribution (aspect=position)

## Changes
- Split **n6**. n6 is now the LN electrode and membrane lithography. The new n24 is the Si nanobeam lithography with the ~50 nm tether. These are two acts on two chips. n24 is spine: n4 and n5 realize it, and it feeds_into n7.
- Split **n14**. n14 keeps the claim that the modes survive with slightly shifted frequencies (o5, o6). The new n25 holds the modest Q decrease. n25 is text-only (dip widths are not resolvable in F5b), has basis argued, is a side claim, and has n9 causes n25.
- Split **n15**. n15 keeps g0/2pi ~10 kHz. The new n26 holds gamma_e/gamma = 0.015, which is text-only with basis argued. n26 causes n16 (joint) and supports n27.
- Split **n18**. n18 keeps "eta on par with homogeneous LN" (from n17). The new n27 holds "combines the strengths of refs 19/20" (from n15, n26 and k4). n27 supports n19. The n15->n18 and k4->n18 edges were rewired to n27.
- Split **k5**. k5 keeps fibre coupling efficiency (refs 46-48). The new k6 holds that fibres have ripped tethered cavities off chips (refs 49-50). Both are premise_for n3.

## Splits and merges
- Splits: n6 -> n6 + n24; n14 -> n14 + n25; n15 -> n15 + n26; n18 -> n18 + n27; k5 -> k5 + k6.
- Merges: none. No two labels state the same claim.

## Source / read_from changes
- source figure -> text:
  - **o1**: naming nanobeam, membrane, IDT and marker needs the false-colour key in caption F3a.
  - **o3**: that the field is the simulated optical mode comes from caption F3c.
  - **o6**: the before/after-slapping status of F4 vs F5b comes from the captions.
  - **o7**: that the blue trace is S21 comes from caption F5b. No S21 axis label is listed for the panel.
- read_from: none changed.
  - o3, o4, o5 and o8 are already "annotation".
  - o6 and o7 read positions off the frequency axis.
  - o2 reads lobe pixels. Its only listed annotation, 'euwy' (Amplitude), is not what the observation states.

## Mode changes
None. n16 is the only claim with two or more causes edges: n13, n14, n15 and the new n26. All four are "joint". No caption shows a choice among them, and transduction needs the optical cavity, the mechanical mode and both couplings together.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)
**Supports 2 · contradicts 0 · not covered 0**

| M | cause -> effect | verdict | nodes |
|---|---|---|---|
| M1 | fibre pick-and-place (slapping) -> Si cavity on suspended LN membrane with IDT | supports | n3, n7, n9, n20, k5, k6, o1. The <100 nm accuracy rests on text / Fig. S4 (n20, argued) |
| M2 | Si-on-LN hybrid -> state-of-the-art transduction (g0 ~10 kHz, eta ~1e-7) | supports | n9, n13, n14, n12, n15, n26, n16, n17, n18, n27, n21. The graph says "on par with", and n22 and n23 bound it |
