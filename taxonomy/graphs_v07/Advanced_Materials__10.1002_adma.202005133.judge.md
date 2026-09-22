# Judge review: Advanced_Materials/10.1002_adma.202005133

**Verdict:** accept with fixes. This was a structure-only review: no figures or crops were opened, and panel citations and techniques were not ruled on. The graph now has 46 nodes, 55 edges and 17 spine nodes (was 16).

The spine is one connected path: need (n1) -> hypothesis (n2) -> Au core-satellite base (n3) + TMAPS/TEOS route (n4) -> DNA assembly (n5) feeds silicification (n6) -> conformal ultrathin shell (n7). From n7 it splits in two:
- **Stability branch:** n7 -> acid/neutral stability (n12) -> conclusion.
- **Gap branch:** n7 -> narrower gap spread (n10), explained by the DNA-locking MEC (n11). Then n10 -> reproducible SERS (n17, via MEC n16) -> single-molecule events (n18, via MECs n19 and n24) -> super-resolution hotspot map (n20) -> conclusion (n23).

Every spine STR/PRP/PRF/MEC node has OBS evidence or a KNW premise:
- n7: o1, o2;
- n10: o7;
- n12: o8, o9;
- n17: o13, o14;
- n18: o16 + k2;
- n20: o19 + k5;
- n11: k1; n16: k3 + n14; n19: n21; n24: k4.

There are 3 audits (a1, l1, o18), and they are fair. No v04 violations.

## Changes
- Split n19 and k2 (details below).
- Changed source on six nodes (details below).

## Splits and merges
- **n19 -> n19 + n24.** The old label stated two claims.
  - n19 keeps "the ultrasmall mode volume admits one R6G molecule at a time".
  - New n24 (MEC/pathway, spine) is "diffusion in/out or blinking switches SERS on/off".
  - k4 (the blinking precedent) now premises n24. Edges n19 supports n24 and n24 explains n18 were added.
- **k2 -> k2 + k5.** The two premises serve different claims.
  - k2 is "fluctuation analysis identifies single-molecule events", a premise for n18.
  - New k5 (KNW/model) is "PSF centroid localisation beats the diffraction limit", a premise for n20.
- Merges: none. n9 (mean distance) and n10 (spread) are different claims, and o11/n14 and o12/n21 are each a readout and its claim.

## Source / read_from changes
- n7: figure -> text. TEM contrast does not identify the rim as silica, and coverage in the gaps is not resolved.
- n12: figure -> text. The 2 h exposure is not shown in any panel.
- n13: figure -> text. Aggregation/precipitation is the caption's reading of the colour change, and the spectra are in Fig. S2.
- n17: figure -> text. R6G identity and 0.1 uM are caption facts.
- n20: figure -> text. That F6c and F6d show the same construct, that the spots are hotspots, and that the map comes from a 250-frame localisation all come from the caption and linked text.
- o13: figure -> text. The shading = SD comes only from the caption; the panel annotations name only the traces.
- read_from: no changes. No OBS restates a listed annotation string. The o18/o19 labels name their panels, but what they read (spot size, spot count) comes from pixels.

## Mode changes
- None. No claim has two or more incoming causes edges: n10, n12 and n17 each have one.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 0.
- M1: silicification (TMAPS/TEOS shell) -> controlled nanogaps. **Supports** (n4, n6 -> n7 -> n10; n9, n11; o5, o7).
- M2: controlled nanogaps -> SERS enhancement factor. **Supports** (n10 -> n16 -> n17; n14 and o11 give the gap dependence of EF; o13).
- M3: enhancement factor -> single-molecule sensing at elevated concentration. **Supports** (n16/n17 -> n18, n19, n24, n20; o16, o19). The graph credits single occupancy to the mode volume (n19) rather than to EF magnitude alone, which matches the MatMech non-referenced note.
