# Judge review: Advanced_Materials/10.1002_adma.202006191

**Verdict:** accept with fixes. This is a structure-only review. No figure or crop was opened, and panel citations and techniques were not ruled on: every cited panel of every evidence node is checked separately by a blind second read.

After the fixes the graph has 50 nodes, 60 edges and 18 spine nodes.

## 1. Spine

The spine is one connected, stage-ordered path rooted at n1:

- **Why:** n1 (soft machines need to change their base shape in situ, not just their gait) -> n2 (hypothesis: one film carrying both magnetic actuation and environment-triggered reconfiguration).
- **Choice and act:** n3 (RM257/ST386 + Disperse Red 1 base matrix), n4 (NdFeB MMPs), n5 (the 0:1 to 2:1 sweep) and n7 (two independent programmed fields) all realize n8 (cast and polymerise 25-40 um films in rubbed polyimide cells).
- **Structure:** n8 produces n12 (where the MMPs sit through the thickness) and n13 (the patterned director field survives up to 1:2).
- **Two property branches that meet in a trade-off:** n12 -> n15 (mass magnetization 15 to 69 emu/g) is the gain arm; n12 and n13 -> n20 (above 1:2 the heated film stops following the programmed cone) is the loss arm. They meet at m2 (MEC/tradeoff).
- **Screen-then-choose:** m2 motivates n6 (adopt 1:2 everywhere), the one DES/down_select, which the `motivates` definition explicitly licenses from a weighed MEC claim. n6 realizes n9 (magnetize at 1.7-1.8 T), n9 feeds_into n10 (environmental heat cue).
- **Performance and conclusion:** n10 -> n19 (temperature sets the base shape, 0 to ~1.6 helical turns) -> n21 (the untethered machine walks, reconfigures and swims) -> n24 (conclusion).

18 spine nodes, inside the 12-20 band; two parallel branches plus the sub-branch n13 that rejoins at n20; no OBS or KNW on the spine.

**Evidence on every spine claim.** n12 has o2, n13 has o1, n15 has o6, n20 has o3, n19 has o5, n21 has o10 and o11. The one gap was **m2**, a spine MEC with no OBS evidence and no KNW premise: its only inputs were in-paper PRP nodes (n15 supports, n20 counteracts, n14 premise_for). **k6** was added for it (see Changes).

**v04 decision rules hold.** n12 is microstructure/distribution (where the constituent lies, aspect=connectivity, per r04 ruling 31) while n13 is microstructure/orientation (molecular/director orientation state). n20 is PRP/behavior_class, not PRP/value: it classifies how the film deforms, not a level. n21-n23 are PRF/service_capability, not qualification, because no external spec or threshold is applied. n9 is PRC/treatment (a permanent modification of an already-made film) while n10 and n11 are PRC/stimulus, each producing an argued state, as r04 ruling 36 requires. n6 is DES/down_select taken after and because of a weighed claim. o10-o12 keep `track_feature_across_series`: these are video frames of one identified object through time, which is what r04 ruling 1 left the op for; the F1b and F2 comparisons across loadings are `compare_across_conditions`.

**Audits: 1, fair.** Only n26 (DSC/limitation: programmed thickness capped near 100 um by the anchoring strength of the rubbed polyimide) qualifies a spine node, n8. No node carries text_silent and no OBS edge is qualifies/contrasts/rules_out. Well inside the budget of 5. o7's image_note explains correctly why the unstated coercivity reading is not flagged text_silent: it supports a claim rather than bounding one.

**Noted, not fixed.** 32 of 50 labels run over the PROTOCOL 20-word cap (o3 is 36 words). That is a batch-wide style drift, not a v04 vocabulary or structure defect (17.9% of all v07 nodes are over), and rewriting 32 labels would risk the claims. Only the labels this review already touched (m2, o14) were shortened.

## 2. Changes

- **m2 label trimmed.** Its second conjunct, "1:2 is the window where both survive", restated n25 (DSC/design_guidance: "keep the MMP loading at or below about 7 vol% (1:2 mass ratio)") word for word. m2 now states only the trade-off. m2 -> n25 supports and m2 -> n6 motivates are both kept, so the window is not lost.
- **k6 added** (KNW/fact, source=prior_knowledge, premise_for m2): "Hard NdFeB microparticles are rigid and non-actuating: they carry the magnetization but cannot contract with the mesogens." This is the premise that makes the two arms of m2 one trade-off rather than two unrelated readings, and it closes the only spine claim that had neither OBS evidence nor a KNW premise.
- **n21, n22 source figure -> text** (see Source changes).
- **n17, o9 source figure -> inferred** (see Source changes).
- **o14 label trimmed:** "with the light already removed" is a caption fact that no panel shows; it moved to image_note, so o14 stays a pixel reading of the two photographs.
- **o10 annotation_match corrected:** "24s" is not a string listed for F3c ("24smorphing" is, and o11 already claims it); "Reaching" was added, which o10's label does restate.

## 3. Splits and merges

No splits were needed. One label trim (m2 -> n25), described above.

Candidates examined and left alone:

- **n7** ("program two independent fields into one monolithic film: a director field and a magnetization profile") is one architectural decision - the monolithic integration is the paper's point - and the two fields are already realised by two separate acts, n8 and n9.
- **n13** ("survives up to 1:2 and can no longer be read once the MMPs block the light path") is one scoped claim plus its own detection limit. A second node would only restate image_support=partial and the image_note.
- **n16** ("stays hard-magnetic, so a profile programmed once is retained without a holding field") is a claim and its immediate reading; both downstream edges (premise_for n9, supports m3) rest on the retention half, so a split would add a node with no new evidence.
- **n17** states one anisotropy claim from one test series.
- **o9** reads panels e, f and g, but all three are the same panel kind (xy_curve), the same technique and the same quantity, so the modality split rule does not bite.
- The readout/claim pairs (o1/n13, o2/n12, o3/n20, o4/n14, o5/n19, o6/n15, o7/n16, o9/n17, o13/n23) are observations and the claims they evidence, not duplicates. m1 is the mechanism behind n20, not a restatement of it.

## 4. Source and read_from changes

**Source changes (4).**

- **n21 figure -> text.** The label turns on "70 C glycerol", and the node's condition attribute on 8 mT, 1-4 mT and 4 mT at 3 Hz. F3c's annotations are frame labels only ("Initial state", "Standingup", "2sWalking", "12sedge", "Swimming down", "Helical propulsion", "Sinkingbygravity"); neither the temperature nor any field strength is written on F3c, and F3b carries only "Glycerol". Facts now listed in requires_unseen.
- **n22 figure -> text.** The 40 mT rotating field and the ~80 C needle are in the linked text only. The single F4a annotation is "Twiningmotionofvines", and the experimental filament row is in no offered crop at all (which is why o12 cites figs=[F4] with an empty panel_ids).
- **n17 and o9 figure -> inferred.** Attaching 1.35 MPa to 0:1 and 3.2-4.6 MPa to the composites needs the symbol-to-ratio legend, which sits below panel g in the whole figure and is in none of the F2e, F2f or F2g crops - o9's own image_note already recorded this. Which of e, f and g is the parallel, the perpendicular and the perpendicular-splay test comes from the caption spans. The linked text defers all strain data to Figure S4, which is not in the packet, so this is inferred rather than text.

**Source kept elsewhere.** 19 nodes are text and each lists the fact no panel shows (the "always remained as a sheet" sentence, the NdFeB chemistry, the mass-to-volume conversion, the cell and polymerisation schedule, the 1.7-1.8 T field and glass-rod rolling, the 1 min UV and the 40 mT magnet, the F2b sample geometry, the 100 um anchoring cap, the two dropped equations' consequences). 7 are inferred (n2, m1, m2, m4, n25 plus the two moved here). 4 are prior_knowledge (k2, k3, k5, k6). The remaining 20 are figure, each read off a cited panel whose own labels carry the conditions it names, each with an empty requires_unseen.

**read_from: no changes.**

- **pixels kept** on o1, o2, o3, o12, o14. Rule applied: a panel-identity label that only says which row or column is being read - "Polarizedlight", "SEM", "Deformation at70degC", "NdFeB1:2(wt)LCE", "Mode1", "Mode2(afterUV lighttriggering)" - does not turn a pixel reading into an annotation reading; the claim itself must restate the string. o1 reads the four-brush texture, o2 where the magenta particles sit, o3 cone versus polygon, o14 flat sheet versus closed curl. None of those words is in the image. o12 cites no panel, so no annotation string is listed for it.
- **axis kept** on o4, o5, o6, o7, o8, o9, o13: values read against plotted axes. For o4 the "Increasingtemperature" and "Decreasing temperature" strings are legend entries naming which series is read, not the claim (T_NI stays flat).
- **annotation kept** on o10 and o11: both restate the F3c frame labels and both carry annotation_match. o10's list was corrected as described above.

## 5. Mode changes

None. Only one node takes two or more causes edges.

- **n20** is caused by n12 and n13, and both edges already carry mode "joint" with a mode_basis. Kept joint: no caption shows a choice between the two causes, and F1b fails in both rows at the same two columns - the polarized-light texture and the cone shape are lost together at 1:1 and 2:1 - so the paper never weighs loss of alignment against particle constraint. "alternative" would invent a choice the figure does not offer.
- n15, n17, n19, n21, n22 and n23 each take a single causes edge and correctly carry no mode field.

## 6. MatMech tally (recorded after the graph was final; the graph was not edited for it)

**Supports 3, contradicts 0, not covered 0.**

- **M1 (Processing -> Structure): embedding MMPs and photopolymerization -> director field maintained where there are no MMPs, elastic repulsion concentrating MMPs mid-thickness. Supports.** Nodes n8 -> n12 and n8 -> n13, evidenced by o2 (SEM cross-sections) and o1 (POM). Two qualifications the graph adds. (i) "Near the middle of the film thickness" holds only at 1:4 and 1:2: n12 and o2 read a dense wall-to-wall network at 1:1 and 2:1, so the unqualified record claim is true of the low-loading half only. (ii) The elastic-repulsion explanation is not in the graph at all - no packet panel bears on it and the packet text never states it.
- **M2 (Structure -> Property): maintained director field with mid-thickness MMPs -> shape-morphing and magnetic responsiveness both retained. Supports.** Magnetic arm: n12 -> n15 (15 to 69 emu/g, from o6) and n16 (open loops, coercive field ~7 kOe, from o7). Shape-morphing arm: n14 (T_NI flat over 0-24 vol%, from o4) and n19 (turns versus temperature, from o5); the light-responsive half is n11 -> n23 with m5. The graph is stricter than the record on "retained": n20 (from o3) says that above 1:2 the heated film stops following the programmed cone, and m2 makes that the counter-arm of an explicit trade-off, which fixes the 1:2 window (n6, n25). MatMech states the same reservation only as a parenthetical.
- **M3 (Property -> Performance): shape-morphing plus magnetic responsiveness -> multi-modal locomotion and environmental adaptability. Supports.** n19 -> n21 causes is this pair exactly, evidenced by o10 and o11 and explained by m3 (torque distribution bends the sheet, with k2) and m4 (anisotropic contraction across the splay field, with k4), with n16 supplying the retained magnetization. n22 and n23 carry the other two adaptability demonstrations, and all three support n24. **Record defect noted, not fixed in the graph:** M3's params quote "rotating magnetic field (40 mT)" for the locomotion test, but 40 mT is the filament experiment of F4a; the swimmer uses 4 mT at 3 Hz, with 8 mT for shaping and 1-4 mT for walking (n21 attrs.condition).
