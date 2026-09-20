# Judge review: Size dependence of microstructure of AlSi10Mg alloy fabricated by selective laser melting

- paper_id: `Materials_Characterization/j.matchar.2017.11.052`  ·  rank 30  ·  batch v05_first100
- vocab: v04 (frozen; no new types accepted, proposals in new_types.jsonl not used)
- **verdict: approved with changes**

## Spine

A sub-millimetre SLM feature must be known to behave like the bulk (h1), and the size dependence is unmeasured (h2) -> thinner plate, different thermal history (h3) -> AlSi10Mg and an 11-level width sweep (h4, h5) -> SLM build (h7) -> melt pools, texture and grain size that do NOT change with width (h8-h10) and low-angle boundary density, Si distribution and Si fraction that DO (h11-h13) -> hardness (h14), explained by in-process ageing (h15) -> conclusion (h16). 15 spine nodes, one root. The paper has no performance stage and the spine correctly stops at the property; the two structure branches - size-independent and size-dependent - are exactly the two the conclusion contrasts.

Evidence or stated basis on every spine STR/PRP/PRF/MEC claim: `h8` evidenced by i1; `h9` evidenced by i2, i3; `h10` evidenced by i4; `h11` evidenced by i5; `h12` evidenced by i6, i7; `h13` evidenced by i8; `h14` evidenced by i10; `h15` basis = argued.

Types were re-checked against the v04 decision rules, every edge whose src is an OBS node with a figure carries an mm_op from the v04 list, and each mm_op names what a reader does to that figure.

## Changes

- i5: panel_ids F7a, F7b, F7c OVERTURNED and emptied. Opening the crops shows that all four offered F7 ids are the SEM panels of paper Fig. 8 (Si particles on a grey matrix), not the EBSD orientation maps that carry the printed Sv(LAB) values. No correct panel id exists: the three EBSD maps of paper Fig. 7 sit in the same image file but the detector offered no id for them. figs = ['F7'] is retained and the image_note now records the figure-level citation.
- h11: the same three panel_ids removed for the same reason, with an image_note added.
- h12: panel_ids corrected from ['F7d'] to all four SEM ids - the wide-plate Si strings the node contrasts against are panel F7a, which IS offered.
- i6: panel_ids corrected from ['F7d'] to ['F7a', 'F7d'], the two panels the node actually reads (wide plate and 0.27 mm plate), and the image_note's statement that 'only the last SEM panel has an offered id' corrected.
- notes: the packet-defect paragraph corrected to the true F7 id mapping.

## Panel checks

Three OBS nodes carrying panel_ids were picked and their crops opened.

### `i5` — OVERTURNED

- panel_ids checked: `10.1016/j.matchar.2017.11.052#F7a`, `10.1016/j.matchar.2017.11.052#F7b`, `10.1016/j.matchar.2017.11.052#F7c`
- correct id: **none exists in this packet**
- all three crops are SEM micrographs of Si particles (paper Fig. 8 a, b, c), not the EBSD maps carrying Sv(LAB) = 0.149, 0.143 and 0.125 um-1. The values are genuinely printed on the composite F7 image, in its upper half, but no panel id addresses those maps, so the node must cite F7 at figure level.

### `i7` — CONFIRMED

- panel_ids checked: `10.1016/j.matchar.2017.11.052#F8a`
- the histogram panel prints 'dm = 10.41 mm' and 'Mean size: 60 nm', peaks at about 26.5% near 50 nm and has a tail out to about 380 nm - exactly the node's reading

### `i11` — CONFIRMED

- panel_ids checked: `10.1016/j.matchar.2017.11.052#F3`
- F3 is offered as a whole-figure id and the plot confirms every element of the node: the 10.4 mm and 0.27 mm error bars overlap, the 0.35 and 0.42 mm points sit near 109.3 Hv above the 0.5-0.66 mm points near 107.5 Hv, and the narrowest sample carries the largest bar

No panel_id anywhere in this graph is invented: every one appears in the packet's panel section (checked mechanically over all nodes, not only the three above).

## What the packet's panel section got wrong

The packet's panel section is wrong about F7 in a way that mattered, and this is the one overturn in the set. Packet F7 is a single image file holding TWO paper figures: paper Fig. 7 (three fine-step EBSD orientation maps, each printing its Sv(LAB) value) above, and paper Fig. 8 (four SEM panels of Si particles) below. The detector offered four ids, F7a-F7d, and the panel definitions attached to them are the caption text of paper Fig. 7 - which is what led the staff to read F7a-c as the EBSD maps. All four crops were opened: every one is an SEM panel of paper Fig. 8, in caption order (a) 10.41 mm, (b) 2.10 mm, (c) 0.66 mm, (d) 0.27 mm. The three EBSD maps have no offered id at all. Two further packet defects the graph already reports survive inspection: the packet holds 9 image files for an 11-figure paper, packet F8 is paper Fig. 9, and paper Fig. 10 (Si number density and area fraction against width) is absent, which is why i8 had to enter as a text-only OBS. The F8 cue lines misread the panel titles 'dm = 10.41 mm' as scale bars - F8a confirms the title is a panel label.

## Audits

2 audits (h18 the 5 Hv effect against 3-4 Hv bars, i11 the overlapping bars and non-monotonic trend). Both bear directly on h14, the terminal property claim of a paper with no performance stage, and both are stated as scatter rather than as refutation, which is the right distinction here. i4's note that every plotted intercept is below the text's 8 um and only about 1.5x the 5 um EBSD step is carried inside the evidence node rather than as a separate audit, which is correct under the audit budget.
