# Judge review: Advanced_Energy_Materials/aenm.202003752

**Verdict:** accept with fixes. This is a structure-only review. No figure or crop was opened, and no panel citation or technique was ruled on; every cited panel is checked separately by the blind second read.

**Final graph:** 20 spine nodes, 45 nodes and 55 edges, v04-valid.

## Spine

The spine reads as one connected, stage-ordered path from h1 to c1, with MEC bridging:

- need (h1) -> hypothesis (h2) -> base IL electrolyte (d1) and HFE diluent (d2) -> preparation (p1) -> Li+-FSI- solvation structure (e1) -> FSI- reduced first (m1) -> inorganic SEI (e2) -> strong SEI with uniform Li+ flux (m2) -> flat dense Li (e3) -> low exposed area (m3) -> 99.4% efficiency (v4) -> Li/Li 1000 h (g1) -> LFP 87% at 5 C (g2) -> conclusion (c1);
- transport branch: p1 -> viscosity (v1) -> conductivity (v2), which both motivate the down-select (d4) -> plating (p2), and v2 also `causes` e3;
- safety branch: p1 -> nonflammability (v3) -> c1.

Two parallel branches plus the main line, within budget. Every spine STR/PRP/PRF/MEC claim is evidenced or visibly unevidenced: e1 (o4-o7, k1), e2 (o12, o13), e3 (o11), v1 (o1), v2 (o2), v3 (o3), v4 (o8), g1 (o10), g2 (o16, o17), m1 (o14, k2), m2 (k3, basis=argued), m3 (basis=argued). v04 decision rules hold: bonding vs composition for e1/e2 (coordination vs what the SEI is made of), shape for e3 (topography of the deposit, not void fraction), value vs behavior_class for v1/v2/v4 against v3, service_capability for g1-g3, pathway for m1-m3 (each is built from evidence, not picked from a catalogue), signal vs response for o4-o7 against o1/o2/o8, component_partition for o7 (a decomposition read at one condition), and down_select for d4 (chosen after and because of v1/v2).

**Audits:** 4 (a1-a4), all fair, each bounding the spine claim it is attached to: the commercial electrolyte holding the highest conductivity in F1a (a1 -> v2), the ILE efficiency trace running to about 600 cycles against the text's 250 (a2 -> v4), Li2O resolved only in the LHCE O 1s trace (a3 -> e2), and the commercial cell matching the LHCE for the first about 400 cycles at 5 C (a4 -> g2).

## Changes

1. **o16 split** (below).
2. **v4 label trimmed.** "about 99.4% Coulombic efficiency with low polarization" states two properties. The polarization claim has no OBS node (F2b is not typed and shows the LHCE alone) and nothing downstream reads it; splitting it out would also have pushed the spine past 20. It is now recorded in v4 `attrs.image_note`, and v4 carries the efficiency claim alone.
3. **One source change and three requires_unseen fills** (below).
4. **No merges, no mode changes, no spine, type, rel or mm_op changes.** The graph was v04-valid before and after.

## Splits and merges

Rule applied: split when the clauses are separate propositions that take different evidence or need different node fields. A comparative claim stated against its own controls is one claim.

- **o16 -> o16 + o17.** The label joined the retention value printed on F5b ("87% after 1000 cycles") with the Coulombic-efficiency trace read against the right-hand axis, which forced one `read_from` value to be wrong. o16 keeps the printed retention (`annotation`); new node **o17** (OBS/response/characteristic_value, F5b, xy_curve, measured) carries the efficiency level (`axis`) and evidences g2 with `read_characteristic_point`. g2 already carried that reading in its image_note, so nothing new was asserted.
- **Merges: none.** Every OBS/claim pair here is a readout and the claim it evidences (o1/v1, o2/v2, o3/v3, o8/v4, o11/e3, o12-o13/e2, o15/g3, o16/g2), and a3 is the text-silent tension about the ILE trace, not a duplicate of o13.
- **Not split, with reason:** h1 is one need stated with its two requirements; h2 is one hypothesis whose two consequences are the chain v1 -> v2; e3 and o11 each state one comparative morphology claim against their two controls; o7 is one partition reading, which is what component_partition is for; o10 is one stability reading of F2c with its two insets.

## Source / read_from changes

Rule applied: a claim whose value, sample or test configuration is given only by a caption or the linked text is "text" (or "inferred"/"prior_knowledge") with that fact listed; it stays "figure" when the panel or its own annotations carry it.

- **v2 -> text.** The 3.2 mS cm-1 (LHCE) and 1.1 mS cm-1 (ILE) values, and with them "almost three times", are text numbers. F1a itself reads about 0.7 and about 3.4 (o2), so the claim cannot be taken off the panel. Listed in requires_unseen.
- **v3** (stays inferred), requires_unseen filled: the comparator is a carbonate electrolyte (1.0 M LiPF6 in EC:DMC:EMC) and the nonflammability is attributed to the intrinsic nonflammability of the IL and the HFE.
- **v4** (stays inferred), requires_unseen filled: caption F2a, the efficiency is that of Li plating/stripping in Li/Cu cells.
- **g1** (stays inferred), requires_unseen filled: caption F2c, the cell is a Li/Li symmetric cell.
- **read_from:** the o16/o17 split only. Every other OBS node is right: o12, o13, o14 and o16 restate strings listed for their panels ("LI"/LiF, "LiO"/"L,CO,"/"ROCO.L", "LUMOatFSI", "87%after1000cycles"); o1, o2, o5, o6, o7, o8, o10, o15, o17, a1, a2 and a4 read plotted data against the axes and use the on-panel series labels only to name the traces; o3, o4, o11 and a3 are pixel judgements (a flame, a band position, a deposit morphology, a resolved component).

## Mode changes

None. e3 is the only claim with two or more incoming `causes` edges (e2, the inorganic SEI, and v2, the ionic conductivity). Both already carry `"mode": "joint"` with a basis, which is right: no caption weighs the two against each other, and Figure 4d-f with its linked text puts the robust SEI and the faster Li+ replenishment together as two factors. Every other claim has at most one `causes` edge, `produces` and `explains` aside.

## MatMech tally (recorded after the graph was final; graph not edited)

Supports 3, contradicts 0, not covered 0.

- **M1 Processing -> Structure.** **Supports** (d1, d2, d3 -> p1 -> e1 -> e2, explained by m1; evidence o4-o7, o12-o14 with k1, k2). The graph splits the record's single effect in two and puts the plating act between them: p1 produces the solvation structure, while the SEI is produced by the plating step p2 and caused by e1. The record's Raman numbers (1223 -> 1227 cm-1) and RDF reading match o4 and o5.
- **M2 Structure -> Properties.** **Supports** (e2 -> m2 -> e3 -> m3 -> v4, with k3). The efficiency half of the record's effect is carried in full. Viscosity and conductivity hang off the processing act in the graph (p1 -> v1 -> v2), not off the solvation structure, which is how the paper itself argues them; the Li+ transference number is a Supporting-Information result with no panel and is not in the graph. The record's "nearly triple that of ILE" and ">100 mPa s" are the text values; a1 and o2 record what F1a shows.
- **M3 Properties -> Performance.** **Supports** (v4 -> g1 `causes`, g1 -> g2 `supports`, v4 -> g3 `supports`, and v2 -> e3 `causes` for the conductivity route; evidence o10, o15, o16, o17). The graph places dendrite-free deposition upstream as a structure claim (e3) rather than as an effect of the properties, and a4 bounds g2: F5b shows the commercial cell matching the LHCE for the first about 400 cycles.
