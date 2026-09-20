# v05 batch: 32 argument graphs with panel links

**Date:** 2026-09-20. Protocol unchanged from the 60-paper sweep ([`TAXONOMY.md`](TAXONOMY.md)): vocabulary
`v04`, round-4 judge rules, same staff-and-judge pattern. One addition — when the panel store holds a panel
for a figure the agent reads, the evidence node cites it.

Stopped at 32 papers by request; ranks 33–100 were selected but not run.

## Selection

`taxonomy/select_first100.py`, run over the SEM + multimodal supply list (see [`OCR.md`](OCR.md)).

- **Ranks 1–8:** papers already graphed in the 60-paper sweep that meet the SEM + 3-modality rule (8 of 26
  candidates). Their old graphs are the A/B comparison.
- **Ranks 9–32:** new, journal-stratified, requiring SEM confirmed **on an accepted panel** (not merely in the
  methods text), two or more further figure-backed modalities, 4–12 figures with at least 60% in tier A or B,
  and year 2012 or later.

The 32 span 13 journals; median 7 figures. All 100 selected papers were OCR'd first as a side job (2,177 crops,
~5 minutes, 94% letter agreement) so every packet carries OCR cues.

## Packets

Built by the original builder, then one panel section appended per figure by
`taxonomy/add_panel_sections.py`: tier A/B panels only, each with a canonical id (`<doi>#F<figure><panel>`),
crop path, OCR letter with agreement flag, definition span, use-sentence count, OCR cues and image labels; a
tier C figure gets one line saying no panels are offered. **724 panels offered across the 32 papers.**

## Results

| | |
|---|---|
| Graphs | 32, all valid against v04 |
| Nodes | 1,244; 432 observation nodes |
| **Observation nodes carrying panel ids** | **407 of 432 (94.2%)** |
| Panel ids cited | 630; 534 of 724 offered panels cited (73.8%) |
| Judge verdicts | 30 approved with changes, 2 approved |
| **New leaf-type proposals** | **0** — v04 absorbed every node in 13 journals |
| **Panel checks** | 108 nodes opened and verified; **5 overturned (4.6%)** |

Both stop rules pass: proposals ≤ 3, overturn rate < 10%.

**The five overturns, all "right panel, misread", never a wrong or invented citation:**
one EDS map read as Al-dominated where it is Zr-dominated; phase markers attributed to the wrong trace;
an element comparison that holds for the plant stem, not the leaf; a claim that reflections sharpen where they
do not; and one genuine store fault (rank 30), where a single image file holds two paper figures, so the
offered ids pointed into the other figure. No invented ids anywhere: every id traced back to its packet.

## A/B against the prior graphs (ranks 1–8)

| rank | paper | nodes | spine | evidence nodes now linked |
|---|---|---|---|---|
| 1 | bioactmat.2020.02.005 | 44→45 | 0→17 | 18 |
| 2 | j.jma.2013.12.002 | 27→32 | 13→15 | 9 |
| 3 | adma.201404945 | 37→38 | 16→18 | 13 |
| 4 | aenm.201501833 | 39→36 | 14→16 | 10 |
| 5 | s40145-019-0329-1 | 38→40 | 13→18 | 13 |
| 6 | j.jma.2020.02.028 | 41→45 | 0→20 | 11 |
| 7 | s40145-019-0334-4 | 30→35 | 12→16 | 9 |
| 8 | j.jma.2015.01.001 | 36→41 | 0→19 | 11 |

Graphs grew slightly and spines became explicit (the zeros are round-1/2 graphs written before the spine field
existed). The substantive change is the last column: evidence now points at named panels instead of whole
figures. Counts of `shown` fall in several papers because the judges re-read the crops and demoted claims to
`partial` — the same direction the 60-paper sweep found whenever figures were opened more carefully.

## What the batch says about the upstream stores

Every staff and judge report converged on the same defect classes, all in the record or the earlier passes,
none in the vocabulary:

1. **Caption spans lag by one panel** whenever the caption puts the letter *after* its description. This
   produced the one missing-id case the judges had to repair by hand.
2. **Figure-id offsets**: a scheme or a missing figure shifts packet F-numbers against paper figure numbers
   (confirmed in at least six papers), and in one case a single image file holds two paper figures.
3. **OCR cue lines invent scale bars** out of d-spacings, tick labels and panel titles ("scale bar 0.26 nm"
   where the bar is 10 nm), and mistype modality on plotted panels.
4. **OCR letter misreads cluster on `d` → `p`/`q`/`g`.** In every case staff and judges checked, the detector's
   letter was right and the OCR was wrong — useful, since these are the second reader for the match run's
   `B2_detector_off_by_one` figures.
5. **Insets carry no ids** (SAED, EDS insets), so nodes reading them cite the figure with `panel_ids: []`.
6. **Tier C figures offer nothing**, which is correct but leaves evidence nodes unlinked on those figures.

One judge also found 11 nodes marked `provenance: derived` with no `derives` edge, none of which occurred in
the 60-paper sweep, and ruled them back to `measured`.

## Files

- `taxonomy/graphs_v05/first100/` — 32 graphs, each with `.build.json` and `.judge.md`, plus `batch.csv`,
  `ab.json`, `summary.json`.
- `taxonomy/first100.jsonl` — the selection, ranks 1–100 (only 1–32 were run).
- `taxonomy/{select_first100,add_panel_sections,aggregate_v05}.py`, `taxonomy/prompts/v05_*.md`.

Packets are not committed: `taxonomy/build_packets.py --papers-file` plus `add_panel_sections.py` regenerate
them from the dataset.
