# Judge review: Advanced_Materials/10.1002_adma.202005864

**Verdict:** accept with fixes. This is a structure-only review. No figure or crop was opened, and panel citations and techniques were not ruled on (every cited panel is checked separately by a blind second read).

After the fixes the graph has 42 nodes, 58 edges and 19 spine nodes.

## Spine

One connected, stage-ordered path with two parallel branches that meet at the conclusion:

- n1 (HYP/need: one fixed metasurface, independent holograms as the medium changes) -> n2 (HYP/hypothesis: phase matrix transformation P1 -> P2).
- **Single-wavelength branch:** n3 (MIM platform) + n4 (two-bar composite cell) + n5 (L1/L2 sweep) -> n6 (e-beam lithography) -> n7 (STR: per-pixel paired nanobars); n6 -> n8 (PRC/stimulus: cedar-oil immersion) -> n9 (PRP: both LSPRs red-shift) -> n10 (MEC: coupled mode -> single-bar dipole, phases 0 and pi) -> n11 (PRP: P1 in air, P2 in oil) -> n12 (PRF: bird in air, fish in oil) -> n17 (FOM: 17.6 / 15.5 %).
- **Dual-wavelength branch:** n13 (three-bar cell, 500 x 500 nm) -> n14 (lithography) -> n15 (STR: three-bar pixel lattice) -> n16 (PRF: DC in air, IU in oil at 710 / 890 nm), with n8 as the joint cause and n10 explaining it -> n19 (FOM: 11.5-13.5 %).
- Both reach n18 (DSC/conclusion).

n8 causes n9 directly, skipping STR, because nothing in the solid changes: only the surroundings do. That is the paper's own argument and the staff note records it.

Every spine STR/PRP/PRF/MEC claim now has OBS evidence or a KNW premise: n7 (o3, o4), n9 (o1), n10 (o2), n11 (o5 + k2), n12 (o6 + k6), n15 (o7, o8), n16 (o10), and n17/n19 (new k7). Before this review n17 had neither; its numbers live in Figure S3, which is not in the packet, so it stays `basis: argued` and is now anchored by the efficiency definition instead of by an invented readout.

v04 decision rules hold. n17/n19 are `PRF/figure_of_merit`, not `qualification`: no external threshold or spec is applied, and the efficiency is a normalised ranking metric used against prior work (r04 ruling #11). n7 and n15 are `STR/microstructure/shape` (geometry of a built unit), not `distribution`. n8 is `PRC/stimulus` and not a bare `PRF attrs.condition`, because the exposure produces an argued state (n9) - r04 ruling #36. n6/n14 stay `PRC/forming`: the act writes a designed two-dimensional geometry, which is forming's inference, while `deposition` names film/coating application. n9 is `PRP/value` (level and its change with a condition) while n10 carries the mode-switch mechanism.

Audits are 4 plus one contrast, at the budget of 5, and each bounds a spine claim: a1 (blurred, broken measured bird and fish) qualifies n12; a2 (text-silent: diffuse background on oil/710 nm, fragmented C at air/890 nm) qualifies n16; a3 (text-silent: ~0.8 reflection in air against ~0.2 in oil at the 800 nm line) qualifies n17 and explains why the oil efficiency is the lower of the single-wavelength pair; d2 (DSC/limitation) qualifies n12; o9 contrasts n16 (simulation against experiment). None is decorative.

Node count is 42, two above the 25-40 aim. This is a two-device paper (single-wavelength bird/fish and dual-wavelength DC/IU), and both devices need their own DES -> PRC -> STR -> PRF chain; no further merge was available.

## Changes

- Split n17 into n17 + n19 (see below) and rewired d1, n16 and n18 accordingly.
- Added k7 (KNW/model) as premise_for n17 and n19.
- Ten source / requires_unseen inconsistencies fixed (see below).
- No merges, no read_from changes, no mode changes.

## Splits and merges

**n17 -> n17 + n19.** The label stated two claims: "17.6 % (air) and 15.5 % (oil) at 800 nm" is the single-wavelength bird/fish device, and "11.5-13.5 % for the four dual-wavelength channels" is the three-bar DC/IU device. Two samples, two measurement sets, and the paper uses only the second when it compares itself with off-axis and interleaved multiwavelength holograms.

- **n17** keeps the single-wavelength claim. Incoming: n12 supports, k7 premise_for, a3 qualifies. Outgoing: n17 -> n18 supports.
- **n19** (new, `PRF/figure_of_merit`, spine, source text, basis argued) carries the four dual-wavelength channel efficiencies. Incoming: n16 supports (moved off n17), k7 premise_for. Outgoing: n19 -> d1 supports (moved off n17) and n19 -> n18 supports.
- a3 stays on n17: it reads the air/oil reflection imbalance at 800 nm, which is the single-wavelength pair.

**No merges.** The pairs that look alike are not duplicates: n7/n15, n4/n13, n6/n14, o4/o8 and o5/o9 are the corresponding nodes of the two different devices, and the OBS/claim pairs (o1/n9, o2/n10, o6/n12, o10/n16) are a readout and the claim it evidences. The staff's own merges recorded in the build file (n9 over the two resonances, n16 over DC and IU, n13 over Fig. 4a and 4b, n7 over the SEM and the optical image) are each one claim and were kept.

**Not split:** a2 reads two per-channel defects on the same panel. Splitting it would put a sixth audit node on a graph already at the audit budget, and both readings are the same act on the same crop, so it stays one audit node. o1 likewise reads dips A and B as one shift.

## Source / read_from changes

Ten nodes carried `source: "figure"` together with a non-empty `requires_unseen`, which the field rule forbids: a figure claim whose reading needs nothing beyond the pixels has `requires_unseen: []`. Corpus-wide this combination occurs 15 times in 4415 v07 nodes, and 10 of those were in this graph. Each was resolved by asking whether the label, as written, can be asserted from the panels alone.

Source changed (the label does need a text-only fact, which stays listed in requires_unseen):

- **n7 figure -> inferred.** "as designed" is a fidelity judgement; the designed per-pixel L1/L2 are text only, so the claim is inferred from o3/o4 together with n4 and n5. The `match_to_design` op on o3 -> n7 is kept.
- **n9 figure -> text.** The label names the index step 1 -> 1.515, which appears only in the F2 caption and linked text. The red-shift itself is read from F2c/F2d by o1, and k4 carries the index as a premise to n8.
- **n12 figure -> text.** "At the working wavelength" is a text-defined condition; 800 nm is nowhere on F3c. The bird/fish switch itself is read from the panel by o6.
- **o7 figure -> text.** "the narrowest bars only tens of nanometres wide" cannot be asserted without the 2 um scale-bar value from the caption; the packet records `scale bar: False` for the F5b crop.

requires_unseen cleared, source kept as figure (the listed fact is panel context, not something the label needs; it was moved into image_note where the node carries figures):

- **n15** - the label states only what the SEM shows; the designed L1-L3 are already carried by n13.attrs.geometry.
- **o2, o5, o6** - none of the three labels names the 800 nm working wavelength.
- **o4, o8** - neither label states a length, so the caption scale-bar values are not needed.

**read_from: no changes.** Every OBS node carries the field. The ruling applied is the standing one: a panel-identity label that only says which panel or which half of a composite panel is being read does not turn a pixel reading into an annotation reading; the claim itself must restate the string.

- kept **pixels** on o5, o6, a1 (F3c, annotations air / oil / Simulation / Experiment) and on o9, o10, a2 (F5c, annotations Simulation / air,710nm / air,890nm / oil,710nm / oil,890nm / Experiment). In every case the content read is the shape in the image - a bird, a fish, the letters D, C, I, U, the blur and the diffuse background - and the annotation strings only select the row and column. Each node's image_note already records that the medium, wavelength and simulation/experiment split come from those strings.
- kept **pixels** on o3 (F3b annotations are the OCR fragments "BD" and "OC", which the label does not use), o2 (near-field maps) and o4, o7, o8 (F3a, F5a, F5b are `annotated: false`).
- kept **axis** on o1 and a3, both read off the wavelength and reflection axes of F2c/F2d.

## Mode changes

None. Two claims take two or more `causes` edges and both are already `joint` with a mode_basis, correctly:

- **n11** <- n7 and n9. The per-pixel bar geometry and the index-driven resonance shift act together to give P1 and P2; no caption offers a choice between them.
- **n16** <- n15 and n8. The fabricated three-bar pixels and the medium change are both needed for DC -> IU; F5c shows air and oil panels of the same sample, which is co-occurrence, not an alternative.

n9, n12 and the other causes edges are single and correctly carry no mode. The new n16 -> n19 and n19 -> d1 edges are `supports`, not `causes`, so mode does not apply.

## MatMech tally (recorded after the graph was final; the graph was not edited for it)

**Supports 4, contradicts 0, not covered 0.**

- **M1 Processing -> Structure (e-beam lithography -> coupled MIM structure with nanobars of varying geometry). Supports.** n6 -> n7 produces, evidenced by o3 (SEM: paired bars differing pixel to pixel) and o4 (unbroken patterned square); the same link is repeated for the colorful device as n14 -> n15 with o7 and o8. One qualification the graph makes that MatMech does not: the 100 / 50 / 40 nm MIM stack is a design choice (n3, n4), not something the lithography is shown to produce, and every layer thickness is text only.
- **M2 Structure -> Property (nanobar geometry -> phase modulation and reflectance sensitive to the medium). Supports.** n7 -> n11 causes, joint with n9 -> n11; n8 -> n9 causes carries the medium sensitivity, o1 reads the red-shift of dips A and B and o2 reads the mode change, with k3 (FDTD + Drude) as the premise behind both and k4 supplying n = 1.515. The graph is more specific than MatMech: the medium sensitivity is attributed to the stimulus n8 acting on the structure, not to the structure alone, and n10 names the mechanism (two-bar coupled mode -> right-bar dipole).
- **M3 Property -> Performance (medium-sensitive phase modulation -> holographic mimicry, dual-wavelength operation). Supports.** n11 -> n12 causes, evidenced by o6 with k6 as premise, for the bird/fish switch; the dual-wavelength half of the effect is n16, explained by n10 and evidenced by o10. Audits a1 and a2 bound both, and d2 attributes the distortion to the four-level phase and to fabrication imperfection.
- **M4 Structure -> Performance (nanobar geometry -> dual-wavelength colorful mimicry). Supports.** n13 -> n14 -> n15 -> n16 causes, joint with n8, evidenced by o10 and contrasted against the simulated o9; n19 carries the efficiency. Two mismatches worth recording, neither of which contradicts the graph: MatMech's cause text lists the two-bar parameters (L1, L2, W1, W2, g) while the dual-wavelength device is the three-bar cell (L1-L3), which the graph keeps separate as n13/n15; and MatMech's "five resonant modes across visible to near-infrared" appears nowhere in the packet, so the graph has no node for it.
