# v07 scale: 100 papers, the first real data bench

**Every verdict is model against model.** No human has checked any item in this set.

100 papers carried end to end: staff graph, structure-only judge, blind second read of every cited panel,
panel judge on every flag, staff citation fix, cutter, writer, structural nets, solving gate, inspector.
Per-paper rows are in `results/v07/batch.csv`; per-item rows in each paper's `results/v07/papers/<P>/gate.jsonl`.

**112 valid items, 1.12 per paper.** 9 more are text-sufficient and 55 went to inspect.

## Funnel

| stage | traces | share of cut |
|---|---|---|
| cut by the cutter | 477 | 100% |
| open after the cutter rules | 181 | 38% |
| written | 180 | 38% |
| passed the structural nets | 173 | 36% |
| **valid** | 112 | 23% |
| text-sufficient | 9 | 2% |
| inspect | 55 | 12% |

41 of the 112 valid items are partial. 100 papers, 1.12 valid per paper.

## Yield by journal

| journal | papers | cut | valid | valid per paper |
|---|---|---|---|---|
| Acta_Materialia | 10 | 49 | 11 | 1.10 |
| Advanced_Composites_and_Hybrid_Materials | 4 | 21 | 6 | 1.50 |
| Advanced_Energy_Materials | 11 | 78 | 22 | 2.00 |
| Advanced_Functional_Materials | 10 | 49 | 6 | 0.60 |
| Advanced_Materials | 11 | 49 | 10 | 0.91 |
| Bioactive_Materials | 6 | 19 | 4 | 0.67 |
| Biomaterials | 3 | 8 | 1 | 0.33 |
| Journal_of_Advanced_Ceramics | 8 | 47 | 15 | 1.88 |
| Journal_of_Magnesium_and_Alloys | 8 | 32 | 7 | 0.88 |
| Journal_of_Materials_Science_&_Technology | 5 | 29 | 9 | 1.80 |
| Materials_Characterization | 5 | 17 | 3 | 0.60 |
| Nano_Letters | 9 | 37 | 10 | 1.11 |
| Nature_Materials | 1 | 1 | 0 | 0.00 |
| Progress_in_Organic_Coatings | 5 | 20 | 7 | 1.40 |
| Rare_Metals | 4 | 21 | 1 | 0.25 |

## Yield by year

| year | papers | cut | valid | valid per paper |
|---|---|---|---|---|
| 2009 | 1 | 1 | 0 | 0.00 |
| 2010 | 2 | 4 | 0 | 0.00 |
| 2011 | 1 | 4 | 1 | 1.00 |
| 2012 | 1 | 4 | 1 | 1.00 |
| 2013 | 2 | 8 | 3 | 1.50 |
| 2014 | 2 | 13 | 5 | 2.50 |
| 2015 | 5 | 15 | 5 | 1.00 |
| 2016 | 4 | 19 | 7 | 1.75 |
| 2017 | 3 | 13 | 4 | 1.33 |
| 2018 | 2 | 7 | 0 | 0.00 |
| 2019 | 5 | 26 | 1 | 0.20 |
| 2020 | 11 | 49 | 9 | 0.82 |
| 2021 | 47 | 244 | 53 | 1.13 |
| 2022 | 14 | 70 | 23 | 1.64 |

## Yield by annotated share of crops

| annotated share of crops | papers | cut | valid | valid per paper |
|---|---|---|---|---|
| 0.00-0.25 | 1 | 10 | 0 | 0.00 |
| 0.25-0.50 | 6 | 23 | 6 | 1.00 |
| 0.50-0.75 | 34 | 150 | 39 | 1.15 |
| 0.75-1.00 | 59 | 294 | 67 | 1.14 |

## Yield by figure-modality family

| figure-modality family | gate items | valid | rate |
|---|---|---|---|
| SEM | 58 | 40 | 69% |
| TEM | 23 | 15 | 65% |
| XRD | 20 | 14 | 70% |
| ECHEM | 17 | 6 | 35% |
| ATOM | 10 | 8 | 80% |
| XAS | 10 | 8 | 80% |
| XPS | 7 | 4 | 57% |
| MECH | 6 | 3 | 50% |
| TRANSPORT | 6 | 3 | 50% |
| RAMAN | 5 | 3 | 60% |
| OPTICAL | 4 | 2 | 50% |
| PL | 4 | 2 | 50% |
| UVVIS | 3 | 1 | 33% |
| PHYS | 2 | 2 | 100% |
| THERMAL | 2 | 0 | 0% |
| FLUORESCENCE | 1 | 0 | 0% |
| EPR | 1 | 0 | 0% |
| EBSD | 1 | 1 | 100% |
| FTIR | 1 | 1 | 100% |
| DERIVED | 1 | 0 | 0% |
| BIO | 1 | 1 | 100% |
| AFM | 1 | 1 | 100% |
| ASSAY | 1 | 0 | 0% |
| CT | 1 | 1 | 100% |

## Inspect causes (55 items)

| cause | items | share |
|---|---|---|
| solver | 26 | 47% |
| writer | 16 | 29% |
| graph | 8 | 15% |
| cutter | 5 | 9% |

## What the cutter closed (296 traces)

| rule | traces closed | share of all closed |
|---|---|---|
| skip | 126 | 43%|
| R3 | 77 | 26%|
| no_crop | 57 | 19%|
| other | 20 | 7%|
| R4 | 16 | 5%|
| R6 | 0 | 0%|

## Knowledge pile

73 text-only facts recorded across 45 papers.

## The panel check

1632 node-panel units checked, 214 flagged, 48 ruled a real citation error by the panel judge.
Panel-judge precision on the flags: 22%.

## Cost

4458 subagent dispatches, 44.6 per paper. Median wall time per paper 188 min.

At 44.6 dispatches per paper, the 16,487-paper corpus projects to 735k dispatches and 18,465 valid items.

## Where the yield goes

45 of the 100 papers produced no valid item, and 25 produced no gate item at all. The cutter, not the
gate, is what decides this: 296 of the 477 cut traces are closed before anything is written, and the
skip rule (the given panels carry the answer as text) accounts for 126 of them, R3 (the graded target is
not readable from the figure) for 77, and a missing crop for 57. R6, the panel-modality block, fired zero
times across the whole set now that the second read supplies `cue_overrides`.

## What fails at the gate, and whose fault it is

| cause | items | share | what it means |
|---|---|---|---|
| solver | 26 | 47% | the item is fair and the image arm misread it — the benchmark working |
| writer | 16 | 29% | the question or key is at fault |
| graph | 8 | 15% | the evidence node misreads the panel |
| cutter | 5 | 9% | the item withholds what the key needs |

**The writer is the largest fixable defect.** Sixteen items failed because the question and the key do not
ask the same thing. One shape dominates: the question puts a claim under test while the key answers a
caveat carried by an *audit* node that the claim never asserted, so an arm that reads the panel correctly
is scored wrong. Two more rest on criteria never given to the arm — an unstated severity threshold for
"far faster", and a peak-separation-versus-peak-width test the inspector judged unsound on its own terms.
One asked about a "20th versus 27th cycle" comparison where the panel is labelled 20th and 21st.

Fixing that class is the single highest-value change available before the next scale run.

## The panel check

1632 node-panel units were read blind and graded; 214 were flagged; the panel judge ruled 48 of those a
real citation error; the staff subagent, opening the whole figure, confirmed **4**.

So the flag-to-fix rate is 4 in 214, and even the judge-confirmed rate is 4 in 48. The screen is doing
real work — it caught the four genuine errors — but it is expensive per fix, and the false positives fall
into five reproducible classes that the staff agents documented:

1. **Caption-borne identity.** The panel's sample or phase assignment lives in the caption, not on the
   image, so a blind single-crop reader cannot recover it. Nodes that already declare this in
   `attrs.requires_unseen` are the ones most likely to be flagged spuriously.
2. **Composite panels.** Where a "panel" is a whole row (SEM plus four EDX maps), the reader describes
   mostly the EDX tiles, so any SEM-only node citing that row is graded wrong by construction.
3. **Similarly-named materials.** A node correctly noting that a figure lacks a POD-M arm was flagged
   because the reader found the V-POD-M arm.
4. **Legend misreads at crop resolution.** The reader read the curves right and the species labels wrong.
5. **The judge itself.** On one paper the panel judge claimed a panel was a different sample when its
   caption says it is the same specimen.

Class 2 has a concrete fix: split composite rows into per-tile crops, or name the tile in the reader's
prompt. Class 1 argues for passing `requires_unseen` to the reader.

## Cost and projection

4447 subagent dispatches, 44.5 per paper, median 188 minutes of wall time per paper. At that rate the
16,487-paper corpus projects to roughly 733k dispatches and about 18,300 valid items — but that projection
assumes the current 1.11 items per paper holds, and the writer defect above puts perhaps a tenth of the
gate items in question either way.

## Caveats on this bench

- **No human check anywhere.** Every graph, question, key, answer and verdict was produced and judged by
  models. Every verdict is model against model.
- **An MCP server's instructions leaked into subagent tool-result streams.** 202 of 3689 replies on disk
  carry a note from the agent saying it saw an injected "create a document" instruction and ignored it.
  It hit the agents with `Read` in their tool set — 13.2% of second reads, 4.7% of gate arms, 3.6% of
  panel judges — and spared the text-only graders and writers entirely. In every reply inspected the agent
  refused the instruction and answered the real question, so no verdict is known to be wrong because of
  it, but the note lands in the reply text that a grader then reads. The second read, the channel with the
  most contamination, is also the one already known to be imprecise. This is unresolved.
- **Two `null_result` items** (the compared conditions show no visible difference) are in the set and
  reported separately, per `results/v07/NULL_RESULT.md`.
- **The scope net never fired** on these 100 papers as a `blocked: scope` verdict, though the writer did
  decline one item by returning an empty `asks_for` when the audit node it was given had no recorded
  ruling.
- **Four papers were dropped at the cap.** C69-C72 have graphs and judge reviews on the branch but no
  downstream run; the corpus is exactly 100 papers.

## Files

- `results/v07/batch.csv` — one row per paper, 26 columns.
- `results/v07/papers/<P>/gate.jsonl` — one row per gate item.
- `trace_kit/v07_scale_report.py` — regenerates every table above.
- `export/v07_items/` — the items as a standalone dataset (not committed; publisher figures).
- `results/v07/PART_G.md`, `reread_precision.md`, `PANEL_JUDGE.md`, `NUMBERING.md`, `SCOPE.md`,
  `NULL_RESULT.md`, `fix_effect.md` — the method changes that produced this run.

Every verdict is model against model.
