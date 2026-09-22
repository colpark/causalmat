# Judge review: Journal_of_Advanced_Ceramics/s40145-021-0537-3

**Verdict:** accept with fixes. This is a structure-only review: no figure or crop was opened, and panel citations were not ruled on. The graph has 17 spine nodes, 47 nodes and 65 edges. The spine is one connected path: need -> hypothesis -> PZT modification + sweeps + porous multilayer architecture -> electrospinning -> lamination. It then splits into two branches:
- **Branch A:** PZT-raised beta fraction (n9) -> voltage rises with PZT content (n13).
- **Branch B:** dense-skin/porous-core film (n10) -> surface charge (n11), voltage rises with thickness (n14), and the cast-film control (n18).

Both branches jointly cause the 136.9 uW power (n15). n15 leads to human-motion harvesting (n16) and then to the conclusion (n17). MEC n12 (dipole rotation, basis argued) bridges the branches. Every spine STR/PRP/PRF/MEC node has OBS evidence. n12 also has the KNW premises k5 and k6. There are 3 audits (o18, o24, o30), and they are fair. All types, rels and ops are v04-valid.

## Changes
- **n9 split.** The label stated two claims: electrospinning converts PVDF to beta, and PZT raises beta content to a 4 wt% maximum.
  - n9 keeps the PZT claim. It stays on the spine, with evidence o13 and premise k2.
  - New n9b (STR/phase/identity, side) takes the electrospinning claim: "fibers beta-dominated where cast film shows alpha/gamma". It is produced by n6. o10 and o12 now evidence n9b (moved from n9). k1 (moved from n9) and k2 are its premises. n9b supports n12.
  - The weak 76.1% -> 76.3% FTIR change is recorded in n9b's image_note, not as an audit, because n9b is off-spine.
- **n10 split.** "No visible interlayer interface" is an interface claim. It is separate from the dense-skin/porous-core porosity claim.
  - n10 keeps the porosity claim, with evidence o7 and o16.
  - New n10b (STR/interface, side) is produced by n7. o6 now evidences n10b (moved from n10). n10b supports n14, following the text's claim that lamination raises stress transfer.
- **Notes corrected.** The builder's notes listed an audit "o5" that does not exist. The Pb/Ti EDS discrepancy sits in o2's image_note.

## Splits and merges
- Splits: n9 -> n9, n9b; n10 -> n10, n10b.
- Merges: none. Each readout/claim pair (o19/n14, o20/n13, o21/n18, o22/n15, o29/n16) is a readout paired with its claim, not a duplicate.

## Source / read_from changes
- **o21:** axis -> annotation. The label restates the listed F7c annotations '100um,cast film' and '100μm,fiber film'.
- **o19 and o20:** axis -> annotation. The voltages are the value labels written in F7a/F7b (OCR tokens 6.75V...62.0.V and 7.5V...62.0.V), not axis readings. Those panels list no annotations, so this is the judge's call and follows precedent.
- **k6:** prior_knowledge -> text. PZT ferroelectricity and its piezoelectric constant are stated in the F4/F7 linked text.
- **New nodes:** n9b is "inferred" because it requires the k1/k2 assignments. n10b is "figure".
- **Checked and unchanged:** n1-n4 and n7 are text, with their unseen facts listed. n11 is text (potential ∝ charge is a text premise). n16 is text (which device was used is ambiguous). n17 is inferred. o13, o22, o25, o26 and o29 stay annotation. o23, o24 and o30 stay axis.

## Mode changes
None. n15 is the only claim with two or more causes edges (from n13 and n14). Its mode stays joint: no caption shows PZT content and thickness as alternatives, and the F7e device is the top level of both sweeps.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 0, not covered 2.
- **M1** (electrospinning + lamination -> porous multilayer of oriented fibers, dense surface, separated interior): **supports** (n6, n7, n8, n10, n10b).
- **M2** (electrospinning with PZT -> enhanced beta): **supports** (n6, n9, n9b). o30 still qualifies the beta -> voltage link.
- **M3** (porous oriented structure + beta -> 62 V, 136.9 uW, sensitivity): **supports** (n9, n10, n13, n14, n15, n12). Sensitivity is not in the graph.
- **M4** (porous structure -> flexibility): **not covered.** The graph has the effect (n23), but it is caused by fiber orientation (n8), not porosity.
- **M5** (output -> 21 LEDs lit, 1 uF charged to 6.4 V): **not covered.** LEDs and capacitor charging appear only in n15's image_note. n15 -> n16 covers human-motion harvesting instead.
- **M6** (lamination -> higher sensitivity and power than cast film): **supports** (n7, n10, n18, n14, n15). o18 qualifies the surface-charge route.
