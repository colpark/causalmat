# Judge review: Advanced_Energy_Materials/aenm.202003412

**Verdict: accept with fixes.**

This review checks structure only. No figures or crops were opened. Panel citations and techniques are left to the blind second read.

## Checklist
- **Spine:** 20 connected nodes in stage order, the upper limit. The path runs:
  - need (n1) -> ternary hypothesis (n2) -> Co host, Fe/Cr co-substitution and the ternary composition sweep (n3, n4, n5) -> urea co-precipitation (n6);
  - n6 then produces three structure claims: low crystallinity (n7), Fe-raised Co valence (n10) and Cr2+ (n10b). The chain continues n10b -> Cr fourfold coordination (n9b) -> Co octahedral occupancy (n9);
  - n7, n9 and n10 are joint causes of the eta10 optimum (n12). Two MECs explain n12: valence-transition energetics (n11) and the lowest theoretical overpotential (n17);
  - n12 -> 7-day alkaline stability (n14) and neutral-electrolyte activity (n15) -> conclusion (n18);
  - control branch: anneal (n16a) -> segregated crystalline phases (n16b) -> worse activity (n16c), which contrasts n12.
- **Evidence:** every spine STR/PRP/PRF/MEC claim now has OBS evidence or a KNW premise:
  - n7: o6a, o6b
  - n9: o8
  - n9b: k4
  - n10: o10, o11, o12, k2
  - n10b: o13
  - n11: o1, o20, o21, k2
  - n12: o15, o16
  - n14: o19a
  - n15: o22
  - n16b: o24 (new, text_only)
  - n16c: o16
  - n17: o3
- **v04 rules:** pass. n7 stays STR/phase/fraction (degree of crystallinity). n16b is a spine STR claim. Before this review it had neither evidence nor a premise. It now carries o24, a text_only OBS for Fig. S19 (XRD/TEM), which is not in the packet.
- **Audits:** 1 (o23, text_silent, qualifies n17). It is fair: F1b and F4g disagree on the site ranking.

## Splits and merges
- **n9 -> n9 + n9b.** Co octahedral occupancy (Co EXAFS, o8) and Cr fourfold coordination (Cr coordination numbers in Table S2, plus k4) are separate claims. The text links them causally, so the old n10 -causes-> n9 edge is now n10b -> n9b -> n9.
- **n10 -> n10 + n10b.** n10 is Fe raising the Co valence. n10b is Cr2+ from electron extraction from Fe. o13 now evidences n10b.
- **n13 -> n13 + n13b.** Tafel slope (o17) and TOF (o18) are separate claims. Both support n12.
- **n14 -> n14 + n14b.** Potential held for 7 days (o19a, spine) and >95% metal retention (o19b, side). n14b supports n18.
- **n17 -> n17 + n17b.** n17 is the lowest eta_theo, 0.49 V, at Co-CoFeCr (o3). n17b is a new DSC/comparison (against model): eta_theo vs onset overpotential, R2 = 0.96 (o4). n17b supports n17.
- **d1 -> d1 + d1b.** d1 is the comparison with IrO2 (baseline, o16). d1b is the comparison with reported Cr-containing trimetallics (prior_work, text only).
- **Label trims (no new node):**
  - n7: the crumpled-nanosheet morphology is evidence, not part of the claim.
  - n16c: R_CT and carrier density moved to attrs.also_in_text.
- **Merges:** none. The OBS/claim pairs that restate each other (o3/n17, o19a/n14) are evidence and claim, not duplicates.

## Source / read_from changes
- o13: read_from pixels -> annotation. The label restates the listed F3d annotation 'E=0.4eV'.
- requires_unseen updated:
  - n3: PDOS, Fig. S1
  - n9: Co coordination numbers
  - n9b: Cr coordination numbers
  - n10 and n10b: split along the claims
  - n14 and n14b: sample identity and ICP-AES retention
  - n16c: eta10 373 mV only
- No source value changed. The text-derived claims were already "text", and the annotated readings (n13, n17, n17b) are "figure".

## Mode changes
None. n12 is the only claim with two or more causes edges (n7, n9, n10). It is correctly "joint": no caption shows a choice between the causes.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 1, not covered 1.
- **M1** (co-precipitation -> low-crystalline, homogeneous nanosheets): supports (n6, n7, n8, o6a, o6b, o7a, o7b).
- **M2** (co-precipitation -> faster Co3+/Co4+ formation -> activity): supports (n6, n10, n11, n12, o20, o21). The graph credits the Fe/Cr composition, not the low-temperature route itself. The Cr6+ vacant-d-orbital argument is not in the graph.
- **M3** (amorphous structure with Cr-promoted octahedral Co -> eta10, TOF, mass activity): supports (n7, n9, n9b, n12, n13b). Mass activity is not a node.
- **M4** (amorphous, homogeneous, octahedral Co -> eta10, kinetics, stability): supports (n7, n9, n12, n13, n14, n14b). Homogeneity (n8) is side, not causal.
- **M5** (Cr promotes octahedral Co -> more Co3+ and a tuned spin state): contradicts (n9, n10, n10b, o10). In the graph and the linked text, the Co3+ rise comes from Fe. Cr alone has a negligible effect, and Cr replacing Fe slightly lowers Co3+. The spin state is not covered.
- **M6** (mass activity, low R_CT -> eta10, TOF, stability): not covered. There are no mass-activity or R_CT nodes (R_CT appears only as an attr on n16c).
