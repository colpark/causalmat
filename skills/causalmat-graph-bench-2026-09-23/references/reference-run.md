# The reference run: v07, 100 papers, 2026-09-23

Numbers to compare a new run against. Every one is model-produced; no human checked any item.

## Funnel

| stage | traces | share of cut |
|---|---|---|
| cut | 477 | 100% |
| open after the cutter rules | 181 | 38% |
| written | 180 | 38% |
| passed the structural nets | 173 | 36% |
| **valid** | **112** (41 partial) | 23% |
| text-sufficient | 9 | 2% |
| inspect | 55 | 12% |

**1.12 valid items per paper.** 45 of 100 papers produced no valid item; 25 produced no gate item at all.

## Yield by journal (top and bottom)

| journal | papers | valid/paper |
|---|---|---|
| Advanced Energy Materials | 11 | 1.91 |
| Journal of Advanced Ceramics | 8 | 1.88 |
| J. Materials Science & Technology | 5 | 1.80 |
| … | | |
| Advanced Functional Materials | 10 | 0.60 |
| Biomaterials | 3 | 0.33 |
| Rare Metals | 4 | 0.25 |

An 8× spread. Journal is the strongest predictor of yield in the set — stronger than year or annotated
share, both of which are close to flat.

## Yield by figure-modality family

| family | gate items | valid | rate |
|---|---|---|---|
| ATOM | 10 | 8 | 80% |
| XAS | 10 | 8 | 80% |
| XRD | 20 | 14 | 70% |
| SEM | 58 | 39 | 67% |
| TEM | 23 | 15 | 65% |
| XPS | 7 | 4 | 57% |
| ECHEM | 17 | 6 | 35% |

Electrochemistry is the hard case: many panels, many curves, and keys that turn on a comparison across
cycles the arm has to track.

## Inspect causes

| cause | items | share | meaning |
|---|---|---|---|
| solver | 26 | 47% | the item is fair and the image arm misread it — **the benchmark working** |
| writer | 16 | 29% | the question and key do not ask the same thing |
| graph | 8 | 15% | the evidence node misreads the panel |
| cutter | 5 | 9% | the item withholds what the key needs |

## What the cutter closed

296 traces. `skip` 126, `R3` 77, `no_crop` 57, other 20, `R4` 16, `R6` 0.

## The panel check

1,632 node-panel units read blind, 214 flagged (13%), 48 ruled `real` by the panel judge (22% of flags),
**4 confirmed as citation errors** by the staff round (1.9% of flags, 8% of judge-confirmed).

## Cost

4,447 subagent dispatches, 44.5 per paper, median 188 min wall per paper at 20-way concurrency.

## Export

175 items across three roots: 112 valid, 9 text-sufficient, 54 inspect (one item has no gate packet
because its writer output is absent). 447 PNGs, 232 MB. All five checks pass.

## Other counts

- knowledge pile: 73 text-only facts across 45 papers
- `null_result` items (the compared conditions show no visible difference): 2
- scope-net blocks: 0, though the writer declined one item by returning an empty `asks_for`

## Provenance of the corpus

61,766 papers → 26,700 with SEM → 16,487 with SEM plus three or more tool-addressable modalities →
424,621 figures → 1,090,345 panel crops. The 100 papers are a deterministic journal-quota draw from the
16,487.

Projecting 1.12 items per paper and 44.5 dispatches per paper across the full supply gives ~18,300 items
for ~733k dispatches — arithmetic, not a plan, and it assumes the writer defect above is not first fixed
(which would change both terms).
