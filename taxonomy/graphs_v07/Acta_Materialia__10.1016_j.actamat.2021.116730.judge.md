# Judge review: Acta_Materialia/10.1016_j.actamat.2021.116730

**Verdict:** accept with fixes. This is a structure-only review. No figure or crop was opened, and panel citations and techniques were not ruled on.

After the fixes the graph has 50 nodes, 73 edges and 19 spine nodes. The spine is one connected, stage-ordered path: need -> gap -> Li foil base system + laser-cut-in-argon method + five-geometry sweep -> laser cutting -> loading to fracture -> slip structure (with the cross-slip MEC) and grains thinning to zero -> perfectly ductile fracture, stress level, through-thickness anisotropy and rate strengthening -> the localisation/rate-hardening trade-off -> the calibrated Hill48 model -> conclusion. A second branch runs n7 -> n18 (fracture displacement falls with triaxiality) -> n19 and rejoins at n21. The air-exposure chain n25 -> n26 -> n27 -> n28 is the control branch (spine=false), tied to the main line by n26 contrasts n14.

Every spine STR/PRP/PRF/MEC claim now has OBS evidence or a KNW premise; n17 and n19 had neither before this review, both being MEC nodes with basis=argued. The v04 decision rules hold: n11 runs the k3 lookup -> MEC/identification chain, n15/n16 carry property_family and, for n16, attrs.proxy for the simulation ablation, and o15 stays OBS/response/regime_map (a yield locus is a boundary between states, not a trend). There are 3 audits (n9 heat-affected zone, n22 the 1.2 vs 0.8 MPa literature gap, n23 the thickness-to-zero the simulation cannot reproduce), all fair and within budget. The node count (50) is above the 25-40 aim, which the staff note justifies by the 12 opened figures; I did not prune, because no node is a duplicate and the audit count is low.

## Changes
- Split o11 into o11 + o17 (see below).
- Added **k4** KNW/precedent, the specimen set of refs 46-47 whose notch radii and central hole impose defined triaxial stress states, as premise_for **n19**; and added **k1** premise_for **n17**, since the 3x-10x local strain rate that the trade-off rests on comes from the simulations run with that constitutive model. Both spine MEC nodes were otherwise unsupported.
- Retyped **o13** and **o14** from OBS/response/trend to OBS/signal/reference_match.
- read_from changes on o13, o14, o15. Source changes on n8, n10, n11, n20, o5, o6, o8 and o12.
- No merges and no mode changes. The spine stays at 19 nodes and the audit count at 3.

## Splits and merges
- **o11 -> o11 + o17.** The old label stated two readings, taken at two magnifications of the same panel and used for two different claims with two different mm_ops.
  - o11 keeps the 500 um side profile: the section tapers to a knife edge with the fracture line at mid-thickness (inspect_local_feature -> n12).
  - New o17 is the 100 um inset: smooth sliding relief with no dimples (recognize_signature -> n13). The recognize_signature edge moved from o11 to o17; all other fields are unchanged, so the two nodes carry the same panel, technique, modality and provenance.
- **Merges:** none. The readout/claim pairs (o5-o6/n14-n18, o7/n15, o9/n10, o10/n11, o12/n20) are distinct readings and claims, and the three PRP/value nodes n14, n15 and n18 state three different properties. n14 and n26 are not duplicates: n26 is the air-exposed control.
- Not split: **n8** ("grains of order 100 um, so a gauge section holds only 10-30 grains"). The second clause is an arithmetic restatement of the first given the gauge length, and nothing downstream reads it separately; the missing gauge-length fact is recorded in requires_unseen instead.

## Source / read_from changes
- **read_from -> annotation** on the three F10 panels. Each node identifies its curves from strings listed for the panel; only the numbers come off the axis. Each now also records `annotation_match`.
  - o13: "Simulation with rate-dependent isotropic model", "Experimental", "Notched R10";
  - o14: "Simulation with rate-independent anisotropic model", "Experimental";
  - o15: "Transverse isotropic Hill48 (this study)", "Isotropic (von Mises)".
  - o2 was already annotation ("Heat affected zone") and keeps it. o1, o4, o9, o10, o11, o16 and new o17 stay pixels; o3, o5, o6, o7, o8 and o12 stay axis (F4b's only listed annotations are the OCR fragments "IPa" and "tres", which no node restates, and F5, F9 and F12 carry no OCR at all).
- **source figure -> inferred**, each with the unseen fact listed:
  - n8: no panel shows how many grains a gauge section holds; the 1.5-5 mm characteristic length is Fig. 9 text.
  - n10: the cited panel is a 5 um view inside one grain, so "stopping at the boundaries" is a text fact.
  - n11: the wavy traces are on the panel, but the homologous-temperature argument is text and prior knowledge (k3).
  - n20: F9 shows five curves agreeing, not which four were used for the inverse calibration.
  - o5, o6: that the last plotted point is the fracture initiation is a Fig. 5 text convention, not readable from the curve.
  - o8: that the shear curve ends at complete separation, with no fracture initiation observed, is text-only.
  - o12: the "held back for validation" clause cannot be read from F9.
- Unchanged: n5 (F3 shows the five dimensioned geometries), n9, n13, n14, n15, n16, n18, n24, n25, n26 stay figure; n1 stays prior_knowledge; n21 stays inferred; the text nodes keep their requires_unseen lists, which are complete.

## Mode changes
None.
- **n13** is the only node with two or more causes edges (from n12 and n29). It stays "joint": no caption shows a choice, and the Fig. 6d linked text gives both contributions at once, necking to zero thickness for the line fracture and the high purity for the absence of dimples.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 1, contradicts 1, not covered 1.
- **M1: laser cutting in argon -> periodic surface structures with wavelengths < 0.5 mm. Contradicts.** In the graph the only structure laser cutting produces is a shallow heat-affected layer 50-100 um deep (n6 produces n9, read from the F1b "Heat affected zone" annotation by o2), neither 150 um wide nor periodic. The periodic surface striations the graph does record are the rolling grooves already present on the as-received foil before any cutting (o1).
- **M2: periodic surface structures -> tensile strength. Not covered.** The cause has no node. The graph's strength chain runs slip (n10) -> small hardening and stress level (n14), with anisotropy (n15) and rate strengthening (n16), and it attributes the falling fracture displacement to stress triaxiality (n18 -> n19), not to surface features. The only surface term in the graph is the heat-affected zone n9, and it merely qualifies n14.
- **M3: ductility -> fracture behavior under various stress states. Supports.** n12 (thinning to zero, fracture surface a line) and n29 (no second-phase particles) jointly cause n13 (perfectly ductile fracture, no dimples, no crack initiation in shear), n17 explains the level of ductility, and n13 and n18 carry it into the conclusion n21 across all five stress states. Evidence: o11, o17, o16.
