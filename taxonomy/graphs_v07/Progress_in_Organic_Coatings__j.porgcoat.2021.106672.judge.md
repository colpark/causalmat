# Judge review: Progress_in_Organic_Coatings/j.porgcoat.2021.106672

**Verdict:** accept with fixes. The spine has 20 nodes and 46 nodes in total, forming one connected path HYP -> DES -> PRC -> STR -> MEC -> PRP -> PRF -> DSC with two branches: barrier/inhibition corrosion (n13, n14 -> n15, n15b -> n17) and sunlight self-healing (n19 -> n20 -> n22 -> n24). There is 1 audit (a1, text_silent, qualifies n8 and n9), and it is fair. Every spine STR/PRP/PRF/MEC claim has OBS evidence or a KNW premise: n8 o1; n10 o4; n10b o3; n13 k5; n14 k4; n15 o9, o10; n15b o11; n17 o13; n20 k2; n22 o15, o16; n24 o17. Figures and crops were not opened, as instructed.

## Changes
- **n10 split.** n10 is now "F-d@MX are thin lamellar sheets" (F2d). It feeds the barrier claim n13. The new n10b is "F-d@Ce are rough spheres ~200-250 nm" (F2b). It supports the Ce inhibition claim n14. o3 now evidences n10b, and n6 produces n10b.
- **n15 split.** n15 is now "filled coatings >> mPU" (o9, o10). The new n15b is "mixed-filler PCM1/PCM2 keep the highest impedance at 60 days, above the single-filler controls" (o11). This is the synergy claim the hypothesis rests on. n13 and n14 explain both.
- **n11 split.** n11 is now the tensile strength rise then fall. The new n11b is "elongation at break falls". Its image_support is partial because PCM0.5 and PCM2(Mx) exceed mPU. n8 causes n11b and n12 explains it.
- **o8 split.** o8 is now the stress readings. The new o8b holds the elongation readings, moved from o8's image_note, and evidences n11b.
- **n12 split.** n12 is now the crosslink/reinforcement mechanism and explains n11 and n11b. The new n12b says aggregation at 5 wt% lowers strength and explains n11.
- **Thermal cause rewired.** The edge n10->n16 (causes) is replaced by n8->n16 (causes). The text credits the thermal gain to rigid fillers in the network, not to filler shape.
- **n18 off the spine.** n18 (down_select PCM2) is now spine=false, which keeps the spine at 20 after the splits. The edge n17->n19 (motivates) was added so the spine stays connected. The path n17->n18->n19 is kept as a side path.

## Splits and merges
- Splits: n10 -> n10, n10b; n15 -> n15, n15b; n11 -> n11, n11b; o8 -> o8, o8b; n12 -> n12, n12b.
- Merges: none. k4 and n14, and k5 and n13, were considered. Each pair is a general premise plus the paper's applied claim, so they are not duplicates.

## Source / read_from changes
- source: all new nodes are "text" and list what they need from the caption or linked text. requires_unseen was narrowed on n10, n15 and n12 to match their new labels. No other source changes: nodes that depend on a table, the caption or ref 24 are already text and list those facts, and the figure-sourced nodes (n3, n6, n13, n14, o1, o2, a1, o6, o8, o9) rest on scheme or axis content.
- read_from: no changes. No OBS node restates a listed annotation string: F2a lists PCM, F-d@MX and F-d@Ce, and the readings are band flatness or axis values. Every OBS node carries read_from.

## Mode changes
- n17 now has two causes edges (n15 and n15b), both set to **joint**. The linked text credits the fillers-vs-mPU effect and the mixed-filler synergy together, and no caption shows a choice between them. No other claim has two or more causes edges.

## MatMech (read after the graph was final; graph not edited)

Supports 4 · contradicts 0 · not covered 0

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | PDA + furan modification + grafting -> F-d@Ce/F-d@MX DA-bonded to PU | supports | n6, n9, n7, n8, o1, o2, o3, a1 | a1 qualifies the furan-band disappearance |
| M2 | lamellar MXene + dispersed CeO2 -> strength, modulus, thermal stability, impedance | supports | n10, n10b, n13, n14, n15, n15b, n8, n11, n16 | graph carries strength and thermal stability through the network n8, not shape; modulus absent |
| M3 | DA network + barrier/inhibitor synergy -> long-term corrosion resistance + self-healing | supports | n13, n14, n15b, n17, n8, n20, n22, n24 | graph stops at 60 days; the 100-day value is text-only |
| M4 | 60 C curing + sunlight DA re-formation -> corrosion resistance + fast healing | supports | n7, n8, n19, n20, n22, n24 | healing half carried; no direct curing -> corrosion path; >98% mechanical recovery (Fig S2) absent |
