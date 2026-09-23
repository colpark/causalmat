# Judge review: Nano_Letters/10.1021_acs.nanolett.0c04014

**Verdict: accept with fixes.**

This review checks structure only. No figure or crop was opened, and panel citations and techniques are left to the blind second read.

After the fixes the graph has 46 nodes, 62 edges, 19 spine nodes and 3 audits.

## Checklist

- **Spine (19, one connected path).** need n1 -> hypothesis n2 -> FP cavity n3 + nanorod array n4 -> five rod lengths n5 -> deposition n6 -> cavity assembly n7 -> fill with neat liquid n8; n6 produces the array n9 -> plasmon tuning n10; n7 and n10 jointly give the 2+1 = 3 cavity-plasmon polaritons n13; n8 gives the cavity-molecule Rabi splitting n11 -> strong-coupling regime n12 (control branch); n13 -> linewidth narrowing n14 with MEC n15 (second branch); n13 and n11 jointly give the three-component coupling 220 / 202 cm-1 n16, bridged by MEC n17 -> beyond the concentration limit n18 -> conclusion n19. Stage order holds (HYP -> DES -> PRC -> STR -> PRP -> PRF -> DSC), with two parallel branches plus the cavity-only control.
- **Evidence.** n9 (o1, o2); n10 (o6); n11 (o5, s2); n12 (basis=argued, k4, s1); n13 (o8, o9, o10); n14 (o12, basis=argued, k3, s3 contrasts); n15 (basis=argued, k3, s3); n16 (o11, k5); n17 (basis=argued, s5); n18 (basis=argued, s4 contrasts, s6). Every spine STR/PRP/PRF/MEC claim has OBS evidence or a KNW premise, or is flagged basis != evidenced.
- **v04 rules.** Pass. Types, rels, mm_ops, modalities and provenance all validate; every OBS with figs carries an mm_op on its outgoing edges, no OBS or KNW node is spine, and every node with figs has image_support.
- **Audits: 3, all fair.** a1 the paper's own "several rather crude assumptions" (qualifies n16, n17); a2 the non-dispersing artifact bands in F5, as bright as the polariton branches (qualifies n13); a3 the cavity thicknesses used for the F5 simulations (10.8 / 8.5 / 10.4 um) differ from those of the F6 fits (9.7 / 8.0 / 10.1 um) for the same three systems (qualifies n16). a3 is checked against the packet and is real.
- **Node count.** 46 is above the 25-40 guide, but the 12 OBS nodes each read a different panel and the 6 side claims are the control and comparison values the spine leans on; nothing was pruned.

## Splits and merges

- **n8 -> n8 + s7.** The label stated two acts. n8 keeps the fill ("Fill the cavity with neat hexanal or 4-butylbenzonitrile through the two inlets"), which is the exposure whose effect is studied. The new s7 (DES/method, attrs.aspect = technique, spine=false) holds the polarization-resolved probe along the rod long axis, with the anisotropy reason from the F5 linked text; s7 is premise_for o8, o10 and o11. The spine count is unchanged.
- **Merges: none.** n1 and k1 were near-duplicates (both stated the sqrt(C) scaling law), but they play different roles: k1 is the prior-knowledge premise, n1 the shortfall it creates. Instead of merging across HYP and KNW, n1 was relabelled to state the shortfall only. o10 and o11 are not duplicates (F6a is the rod-cavity system, F6b,c the two three-component systems); s4 and s5 are different systems.
- **Two-claim labels trimmed, not split.** n11 dropped "above both bare linewidths" (that criterion is n12 with k4) into attrs.note; n14 dropped "set by the cavity mode" (FP mode fwhm 84 +/- 7.3 cm-1, Table S2) into attrs.floor_note.
- **One corrected edge.** n8 -> n13 causes became n7 -> n13. n13 is the air-filled rod-cavity system (F5a, F6a), so filling with molecules cannot cause it; the FP-mode half of the 2+1 hybridisation comes from the assembled cavity.

## Source / read_from changes

- **n13: figure -> text.** The node's own image_note admits the branch count cannot be read from F5a (the caption's blue dash-dot guides are not discernible), and F6a shows three fitted branches, not the "exactly 2+1 = 3 polaritonic states" decomposition or the "almost linear dispersive behavior" wording, both of which are F5 linked text. requires_unseen filled.
- **s2: figure -> text.** F4b and F4c annotate only C=O and C=N, and F3c carries no annotations at all. Which drawn structure is hexanal and which 4-butylbenzonitrile, and the band centres 1724 and 2225 cm-1, are caption facts. requires_unseen filled.
- **Kept:** n4 and n5 stay figure (450 nm SiO2, the nanorods and L=1100..1500 nm are listed F3b/F3d annotations); n9, n10 and s1 stay figure; all 12 OBS nodes stay figure.
- **read_from: no changes.** o2, o3 and o4 are already annotation and each restates strings listed for its panel (L=1100nm..L=1500nm; FSR=496cm-1, Q=28, d=10.19um, v1520~50cm-1; C=O and C=N). o6 stays axis (band position in cm-1 against the F4d axes). o1, o5, o7, o8, o9, o10, o11, o12 and a2 stay pixels: their content is visual, and the annotations of those panels only name the band or the sample. F5 offers no panels and no OCR, so o8, o9 and a2 cannot be annotation readings.

## Mode changes

None. Two claims take two or more causes edges.
- **n13** (from n10 and n7): "joint" kept. No caption shows a choice, and the F5 linked text says the two FP modes couple to the plasmonic array mode forming exactly 2+1 = 3 states, i.e. both act at once. The src of the second edge was corrected from n8 to n7.
- **n16** (from n13 and n11): "joint" kept. The F6 linked text models the plasmon-molecule hybrid as a single collective oscillator, so both components act together.

## MatMech tally (recorded after the graph was final; the graph was not edited afterwards)

Supports 3, contradicts 0, not covered 0.

- **M1 (rod array in an FP cavity filled with molecules -> hybrid polaritonic states): supports.** n4, n5 -> n6 -> n7 -> n8, with n9 and the polariton claims n13 and n16 and the hybridisation MEC n17; o8 and o11 are the readouts. The graph adds the array geometry and the cavity-only control that MatMech leaves out.
- **M2 (hybrid polaritonic states -> Rabi splitting and coupling strength): supports.** n13 and n11 jointly cause n16 (220 / 202 cm-1) via the JC model k5, evidenced by o10 and o11; n11 (101 / 46 cm-1) carries the Rabi splitting itself, and s4, s5, s6 carry the cavity-only and rod-only comparators. MatMech's "referenced knowledge" that Rabi splitting scales with sqrt(C) is k1 and n1.
- **M3 (Rabi splitting and coupling strength -> increased coupling and narrowed linewidth, for biosensing): supports, partially.** n16 causes n18 and n18 supports n19 carry the coupling-strength leg. The linewidth leg is in the graph (n14, ~70 cm-1, against the bare plasmon s3), but the graph routes it from n13 via n15 (radiation recycled between the mirrors suppresses radiative damping), not from the Rabi splitting, which is a different parent, not a contradiction. The biosensing application has no node: the packet carries no abstract, introduction or outlook text.
