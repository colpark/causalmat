# Judge review: Bioactive_Materials/j.bioactmat.2019.12.001

**Verdict:** accept with minor changes. The graph has 16 spine nodes (14 before the splits) and 50 nodes in total. The spine is one connected path: AZ31 corrodes fast -> MAO leaves open pores -> ALD Ta2O5 sealing hypothesis -> base, modification and route choices -> MAO then ALD for 500 cycles -> Ta-O film covering the MAO -> pores closed -> barrier (MEC, argued) -> icorr/|Z| ranking -> low steady HER and an intact surface (two parallel PRF branches) -> conclusion. Evidence for each spine claim: n8 (o6, k1), n10 (o2, o5, o8), n11 (o1), n12 (o9, o11, k4), n15 (o12), n15b (o14, o15, o18). n16 is argued (o15, k2). There are 2 audits and both are fair. o13 is text_silent: early HER is barely below MAO despite the ~2.7-decade icorr gap. n21 is the stated nano-gap pitting limitation. Structure only: no figure or crop was opened.

## Changes
- n1 split. n1 keeps "AZ31 corrodes fast in physiological solution". The new node n1b (HYP/need, spine) carries "MAO pores and cracks let aggressive ions reach the substrate". Edges: n1 -> n1b -> n2, motivates.
- n9 split. n9 keeps "Ta2O5 film X-ray amorphous", evidenced by o4. The new node n9b (STR/phase/identity, side) carries "crystalline phases alpha-Mg + MgO". o3 now evidences n9b, and n6 produces n9b.
- n15 split. n15 keeps "low steady HER over 294 h", evidenced by o12. The new node n15b (PRF/service_capability, spine, parallel branch) carries "surface largely intact after 294 h". o14, o15 and o18 now evidence n15b. New edges n12 causes n15b and n15b supports n20. n21 now qualifies n15b.
- n17 split. n17 keeps "local pitting", evidenced by o16 and o17. The new node n17b (STR/chemistry/composition, side) carries "Ca-P corrosion products fill the Mg-depleted pit". o17 also evidences n17b, and n17 causes n17b.
- No merges: no two labels state the same claim.

## Source / read_from changes
- nthk: source changed from figure to text. No panel shows that the film thickens with cycle number (0.1 nm/cycle; 50 vs 100 nm), and the curve I/II mapping comes from the caption. Both facts are listed in requires_unseen.
- n1b, n17b (new nodes): source is text, with requires_unseen filled.
- o8: read_from changed from pixels to annotation. The element lines it restates (Ols, Ta4d, Ta4f, C1s, Nls, OKLL) are the annotation strings listed for F3a.
- Checked and unchanged: o3 (the F2 legend has no annotation list) and o19 (the printed icorr values are OCR tokens, not listed annotations).

## Mode changes
None. The only claim with two or more causes edges is n12 (n11 sealing, n8 Ta2O5 chemistry). It is joint, and no caption shows a choice between the two causes.

## MatMech (judge only, graph not edited): supports 4, contradicts 0, not covered 0

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | MAO then ALD Ta2O5 (500 cycles) | amorphous sealing Ta2O5 film; MgO in MAO | supports | n6, n7, n10, n11, n9, n9b, nald | amorphousness is a side node resting only on XRD absence |
| M2 | sealing Ta2O5 film | icorr ~3 orders down, \|Z\| 2-3 orders up | supports | n11, n8, n16, n12, o9, o11 | graph reads ~2.7 and ~2.4 decades vs MAO; Ta2O5 chemistry is a joint cause; amorphousness is not a cause in the graph |
| M3 | low icorr, high \|Z\| | long-term resistance, low HER, pitting suppressed | supports | n12, n15, n15b, n17, n21, o13 | pitting is reduced, not suppressed (n21); early HER is barely below MAO (o13) |
| M4 | MAO + ALD processing | superior long-term performance | supports | n6, n7, n11, n12, n15, n15b, n19 | via the spine chain; organic-sealer comparison in n19 |
