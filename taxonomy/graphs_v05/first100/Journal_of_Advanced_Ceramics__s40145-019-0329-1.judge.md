# Judge review — Journal_of_Advanced_Ceramics/s40145-019-0329-1 (rank 5)

**Verdict: approved.** No changes.

Al–Ti co-doped BIVOX oxide-ion electrolyte. The spine is a doping sweep whose structure claim j8 is carried by four independent readouts (XRD peak merging, Rietveld, FTIR band loss, DSC endotherm loss), all turning at x = 0.175, and whose property branch runs band gap → vacancy concentration → conductivity, closed by the PRP/diagnostic → MEC/identification chain for the γ′→γ order–disorder slope change. 18 spine nodes, one connected path j1 → j19, no orphan claims; k13 is a derived OBS with the required `derives` edge from k12.

Two typing points checked against v04 and left as they are:

- **j15 PRP/diagnostic** survives the r04 #10 rule because the diagnostic → identification chain is actually built (j15 → j16, with m4 supplying the mapping). m4 is typed `KNW/precedent` rather than `KNW/lookup`; it is a specific earlier result *used as* the slope-change → order-disorder mapping, so both leaves fit and the chain's substance is present. Not changed.
- **j11** (`STR/defect/point`, `aspect: concentration`) is the r04 #25 ruling applied correctly; its `basis: argued` with `proxy: optical band gap` is honest, since no OBS evidences it directly.

## Panel checks

| node | panel_ids | ruling |
|---|---|---|
| k9 | `#F5` | **confirmed** |
| k10 | `#F5` | **confirmed** |
| k11 | `#F8` | **confirmed** |

- **k9 → F5.** The panel plots (hν·F(R∞))² against hν with one extrapolation line per composition. The x = 0 line crosses at ~2.18 eV and the x = 0.175 line at ~1.95 eV, the lowest of the six — exactly the node.
- **k10 → F5** (audit claim, checked separately on the same panel). Every doped extrapolation crosses at or below the parent's intercept. The text's "blue shift" is contradicted by the panel it cites, so j21 is correctly typed `kind: anomaly` rather than a scope limit.
- **k11 → F8.** An arrow labelled 420 °C sits at 1000/T = 1.44, which is 1000/693 K — the panel and the label agree. The x = 0.10 series breaks sharply there, x = 0.15 only subtly, and x ≥ 0.175 run continuously. k12's ranking also holds: x = 0.175 is highest between 1000/T 1.7 and 1.9, and x = 0.10 becomes highest above the break.

All 12 panel_ids used appear in the packet. F3–F8 are tier-B whole-figure records and are cited as single ids, which is correct.

## Audits

Three, all changing support. j21 with OBS k10 contradicts the text's blue-shift reading and bounds the band-gap claim j13, which is the premise for the vacancy node j11 — so this audit reaches the mechanism, not just a side remark. j22 bounds the conductivity claim j14 by showing that x = 0.175 leads only in the intermediate range, while x = 0.10 wins above the transition. Both were verified on the images. Budget respected (3 ≤ 5).

## What the packet got wrong

- Nothing that misled the graph. Panel letters for F1 and F2 are correct and the tier-A crops match their captions.
- F1's `definition` spans are caption fragments ("calcination at 650 °C", "the maximum intensity peak at ~28.5°") that only make sense read together with the caption; F1c and F1e were detector-only with no OCR letter, and the staff correctly identified them from content.
- k2 reads the 31.5–32.5° inset of F1c and k4 the Rietveld overlays of F1e; neither inset nor sub-panel is offered separately by the panel store, which the nodes record.
