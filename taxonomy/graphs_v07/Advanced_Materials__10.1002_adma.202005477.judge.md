# Judge review: Advanced_Materials/10.1002_adma.202005477

**Verdict:** accept with fixes. This is a structure-only review. No figures or crops were opened, and panel citations and techniques were not ruled on (every cited panel is checked separately by a blind second read).

After the fixes the graph has 51 nodes, 69 edges and 18 spine nodes. The spine is one connected path in stage order: need for an antibiotic-free agent (s1) -> LCK hypothesis (s2) -> Cu(II)-BTC base system + phosphomolybdic-acid modification + spiky-shell architecture (s3, s4, s5) -> ambient assembly and single-channel shell growth (s6, s7) -> spiky surface, 130 nm silica shell, homogeneous Cu/Mo core (s8, s9, s10). From there it runs in two branches that meet at s15:

- **catalysis:** s10 -> s11 (Cu+MoO3 raise .OH output), with s12 (peroxo-complex pathway) explaining it;
- **capture:** s8 -> s13 (spikes pierce and bind the bilayer), with s9 and s13 supporting s14 (localized capture-killing).

Both enter s15 (zero colonies) as joint causes, then s16 (wound closed at day 16) -> s17 (epidermal thickness) -> s18. Every spine STR/PRP/PRF/MEC claim has OBS evidence: s8/o1, s9/o2, s10/o3, s11/o4-o6, s12/o7-o8, s13/o9-o10, s14/o11-o13, s15/o14-o15, s16/o16-o18, s17/o19-o20. The v04 decision rules hold: s8 is shape (geometry of the built unit) against s9 distribution (coverage of the shell); s15 is PRP/value and s16/s17 PRF/service_capability (argued suitability at the use condition), with c1 carrying the vancomycin comparison; s12 and s14 are MEC/pathway, not identification, because both are built from evidence rather than picked from a catalogue; o20 and o22 are provenance `derived` and each carries a derives edge from its image node. There are 5 audits (a1, a2, a3, a4, d1), at budget, and all are fair: each either contradicts a linked-text statement it cites (a1, a2, a4), offers an alternative the text never weighs (a3), or bounds the scope of a spine claim (d1, the missing POD-M+H2O2 arm in Figure 7).

## Changes
- Split s17 into s17 + s19 (see below).
- read_from pixels/axis -> annotation on o6, o7 and o8.
- requires_unseen corrected on s2, s12 and s14.
- No merges, no source-value changes, no mode changes. The spine stays at 18 nodes and the audit count stays at 5.

## Splits and merges
- **s17 -> s17 + s19.** The old label stated two claims ("near-normal epidermal thickness **and** vessel density") with two disjoint evidence sets, so it could not be graded against either.
  - s17 keeps the epidermal-thickness claim, evidenced by o19 (Masson band) and o20 (thickness index 8.0/7.0/4.0/2.0 with vancomycin 2.25), and stays on the spine as the paper's primary histology endpoint.
  - New **s19** (PRF/service_capability, spine=false, attrs.aspect=angiogenesis) carries the CD31 vessel-density claim, evidenced by o21 (CD31 fields) and o22 (expression ratio and vessel count).
  - New edges: s16->s19 causes, s19->s18 supports, s19->c1 supports. o21->s19 and o22->s19 evidences moved off s17. o22->c1 is kept.
- **Merges: none.** Three candidates were considered and rejected.
  - s16 / c1: c1 is the DSC verdict over both endpoints, with its own premise k3 and its own evidence; the vancomycin parity in s16 is the reading of the F7b curves.
  - o11 / o13: different figures and different claims (capture geometry in SEM; live/dead field and clustering in F4). o13 carries the killing dimension o11 does not.
  - o10 and o22 each merge two panels that state one claim (F6c+F6d; F8d+F8e). Two co-plotted quantities carrying one claim is not two claims, so they were not split back.

## Source / read_from changes
- **read_from -> annotation.**
  - **o6** (pixels -> annotation): the node reports the four-line DMPO-OH assignment, which F2g prints ('·DMPO-OH', with 'DMPOX' and '*DMPO-C' on the interleaved lines). The panel has no intensity scale, so the height ranking stays in image_note as the pixel part.
  - **o7** (axis -> annotation): both the species naming ('Peroxo complexintermediate', 'MoO,(O,)formation step', 'Peroxide adsorption process') and the energies 0.06 and -0.78 are drawn on F3b; the axis ticks are 0.4/0.0/-0.4/-0.8, so those numbers are not axis readings.
  - **o8** (axis -> annotation): 'ReactionPath1', 'ReactionPath2' and every level the node quotes are printed on F3e; the barrier heights are differences of printed levels, not axis readings.
- **read_from checked and unchanged.** o4, o5, o10, o16, o20, o22, a1, a2 and a4 stay "axis": their listed annotations are legend strings and axis titles that only name traces, groups or bars. o9, o17, o18, o19, o21 and o3 stay "pixels": their listed annotations are group or frame identifiers ('Flatsurface', '0ns'-'24ns', 'Control', 'Vancomycin', 'CD31/DAPI', element tile labels). o11, o12 and a3 are already "annotation" and match listed F5b/F5c strings. F1 (tier C2) and F4 (tier C3) offer no panel crops, so the packet lists no annotation strings for them and the rule cannot fire there; o2, o14 and o15 keep "annotation" for in-image strings read in the whole-figure pass ('130 nm', the printed CFU counts, the MIC arrows), and o1 and o13 keep "pixels" because their content is morphology and field colour.
- **source: no value changed.** Checked:
  - s15 and s16 stay "figure": the claims are read from the F4a plate counts and the F7b curves, and the text-only 16 ug/mL + 0.1 mM H2O2 dose and the 1e8 CFU/mL inoculum are experimental-context attributes already marked as linked-text values in attrs.condition.
  - s8, s9 and s10 stay "figure": their content is carried by strings drawn in F1 ('Smooth surface', 'mesoporous spike', 'Spiky silica shell', '130 nm') and by the EDX tiles; only the POD-M/V-POD-M naming is a caption fact, and that names the samples rather than making the claim.
- **requires_unseen corrected** (no source change):
  - s12: the Path 1 / Path 2 names and the MoO3+H2O2 -> MoO2(O2)+H2O reaction are drawn on F3a,c,d, so they are not text-only. What is unseen is that the computed Path 1 is the route the real catalyst takes, and that the DFT slab stands for the phosphomolybdate-loaded MOF.
  - s14: the 'LCK action' name and the DNA-damage step appear in the F5a schematic drawing, which is not a measurement; no panel in the packet measures bacterial DNA, and no panel time-resolves the simultaneity of capture and radical release. Both are now listed.
  - s2: same correction for the LCK name, which is drawn on F5a as well as stated in the linked text.

## Mode changes
None. s15 is the only claim with two or more incoming causes edges (s11 and s13). Both stay "joint": no caption offers a choice between the two routes, the paper's LCK argument is that capture and the .OH burst act together, and F4 has no arm that isolates either. New node s19 has a single cause (s16).

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 0.
- **M1: single-channel oriented-assembly coating -> virus-like spiky structure with Cu(II)/MoO3 preserved in the core. Supports.** Nodes s7 -> s8, s9 and s6 -> s10, evidenced by o1, o2, o3. s10 (Cu and Mo homogeneous in both samples) is the "preserved" half.
- **M2: Cu(II) + MoO3 centres -> peroxidase-mimetic .OH generation. Supports.** Nodes s10 -> s11, explained by s12, evidenced by o4-o8. Two audits bound the size of the effect, not its direction: a1 (F2c shows MoO3 alone oxidizing TMB well above the blank, against the linked text) and a2 (all four TA groups give 185-380 a.u., so the gain is about twofold, not on/off).
- **M3: .OH generation -> nearly 100% killing at 16 ug/mL. Supports.** Nodes s11 -> s15 (joint with s13), evidenced by o13, o14, o15. The 16 ug/mL condition is text-only, and o15's image_note records that the F4f MIC arrow sits well above it. a3 offers an alternative reading of the POD-M arm (the flat particles collapse after H2O2) that MatMech does not weigh.
- **M4: virus-like spiky shell -> enhanced capture and localized sterilization. Supports.** Nodes s8 -> s13, s13 and s9 -> s14, s13 -> s15, evidenced by o9-o12. Two of MatMech's stated grounds are weaker in the graph: o12 is image_support partial because the TEM sections do not resolve spikes inside the cytomembrane, and o9's image_note records that the MD penetration is force-driven and the two rows are rendered differently.
