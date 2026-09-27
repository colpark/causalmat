# Traces v2.10 — chains that hold, and how deep they go

Every verdict is model against model.

The same 24 papers as v2.9. Three things: remove anything the model can answer from the paper's name, push the chains one or two steps deeper, and lay the surviving chains out on a page so one can be read end to end.

## Step 1 — the memorisation purge removed nothing

|  | before | flagged | after |
|---|---|---|---|
| depth 2 compositional items | 68 | 11 | 68 |
| depth 3 chains | 40 | 4 | 40 |

**Nothing moved.** 0 of the 11 flagged depth-2 items were passing, and 0 chains died. v2.9's compositional test already required arm N below 0.25 as one of its three gates, so a memorised item could never have been counted in the first place. The brief assumed they were still in the passing set; they were not, and this is verified rather than argued.

The flagged items are kept in full with their arm N answers, because what a corpus gives away for free is a fact about the corpus. Three scored 1.00 — the title alone reached every combined claim — and on one of those the name beat the evidence outright (arm N 1.00 against arm B 0.00).

## The funnel

| stage | count |
|---|---|
| v2.9 depth 2 compositional | 68 |
| after the memorisation purge | 68 |
| v2.9 depth 3 chains | 40 |
| after the purge | 40 |
| depth 4 candidates | 27 |
| depth 4 produced | 27 |
| depth 4 links passing | 19 |
| depth 5 candidates | 7 |
| depth 5 links passing | 5 |

## Pass rate by depth

|  | passing | rate | 95% CI |
|---|---|---|---|
| depth 2 | 68 of 88 | 77.3% | 67.5–84.8% |
| depth 3 | 40 of 51 | 78.4% | 65.4–87.5% |
| depth 4 | 19 of 27 | 70.4% | 51.5–84.2% |
| depth 5 | 5 of 7 | 71.4% | 35.9–91.8% |

The intervals overlap at every depth. On this evidence a fourth step is no harder than a second, which is the opposite of what v2.6 found when chains were discovered by sharing a claim id rather than built so something has to travel.

## Mean combined score per arm, by depth

|  | A measurement | B measurement + result | C result alone | N name only |
|---|---|---|---|---|
| depth 2 | 0.142 | 0.813 | 0.014 | 0.078 |
| depth 3 | 0.082 | 0.845 | 0.090 | 0.040 |
| depth 4 | 0.200 | 0.895 | 0.012 | 0.062 |
| depth 5 | 0.036 | 0.595 | 0.000 | 0.000 |

## Arm N, and what it does not prove

|  | arm N ≥ 0.25 | mean arm N | answers that refuse anyway |
|---|---|---|---|
| depth 2 | 11 of 88 | 0.078 | 19 of 88 |
| depth 3 | 4 of 51 | 0.040 | 9 of 51 |
| depth 4 | 4 of 27 | 0.062 | 10 of 27 |
| depth 5 | 0 of 7 | 0.000 | 4 of 7 |

Arm N is given the paper's real title and journal and told "Give your best guess. Do not refuse." A large share still refuse. So a low arm N score is partly unwillingness to guess rather than inability, the same failure that made v2.8b's version useless, and the instruction only half fixes it. The memorisation figures are therefore a floor on what the model could produce, not a measure of what it knows.

## Depth 4

27 candidates from 15 of 40 surviving depth 3 chains, at most 2 each.

| dropped at generation | count |
|---|---|
| over the 2-per-chain cap | 13 |
| observation already used in the chain | 1 |

passed: no depth 4 link reuses a node or panel from any earlier step of its own chain.

Production: 27 drafted, tag agreement 96.1%, 0 dropped for having no combined claim.

2 links were borderline and resampled; 0 flipped.

## Per paper

| paper | chains | depth 5 | depth 4 | depth 3 | depth 2 | memorised | size |
|---|---|---|---|---|---|---|---|
| Advanced Composites and Hybrid · s42114-021-00366-2 | 10 | 0 | 0 | 6 | 4 | 0 | 835 KB |
| Bioactive Materials · j.bioactmat.2020.02. | 9 | 0 | 2 | 2 | 5 | 1 | 913 KB |
| Advanced Energy Materials · aenm.202003419 | 8 | 4 | 0 | 0 | 4 | 1 | 559 KB |
| Advanced Functional Materials · 10.1002_adfm.2020050 | 8 | 0 | 6 | 1 | 1 | 2 | 835 KB |
| Journal of Materials Science & · j.jmst.2020.05.053 | 8 | 0 | 0 | 2 | 6 | 2 | 657 KB |
| Journal of Magnesium and Alloy · j.jma.2020.11.023 | 7 | 1 | 3 | 1 | 2 | 0 | 717 KB |
| Journal of Advanced Ceramics · s40145-021-0536-4 | 6 | 0 | 0 | 6 | 0 | 0 | 392 KB |
| Biomaterials · j.biomaterials.2011. | 5 | 0 | 0 | 3 | 2 | 1 | 347 KB |
| Journal of Magnesium and Alloy · j.jma.2020.09.027 | 5 | 0 | 0 | 0 | 5 | 1 | 359 KB |
| Nano Letters · 10.1021_acs.nanolett | 5 | 0 | 2 | 2 | 1 | 0 | 493 KB |
| Journal of Magnesium and Alloy · j.jma.2015.01.001 | 4 | 0 | 0 | 0 | 4 | 1 | 255 KB |
| Advanced Energy Materials · aenm.201601491 | 3 | 0 | 0 | 2 | 1 | 2 | 244 KB |
| Journal of Advanced Ceramics · s40145-021-0538-2 | 3 | 0 | 2 | 0 | 1 | 1 | 283 KB |
| Journal of Magnesium and Alloy · j.jma.2020.02.028 | 2 | 0 | 0 | 1 | 1 | 0 | 125 KB |
| Advanced Energy Materials · aenm.202003412 | 1 | 0 | 0 | 0 | 1 | 0 | 47 KB |
| Bioactive Materials · j.bioactmat.2020.01. | 1 | 0 | 0 | 0 | 1 | 0 | 75 KB |
| Nano Letters · 10.1021_acs.nanolett | 1 | 0 | 0 | 0 | 1 | 1 | 76 KB |

17 pages plus an index in `results/v2p10/pages/`, 86 chains in total, largest page 913 KB. Panels are embedded as data URIs; no page makes an external request.

## Cost

| stage | model calls | relays | wall minutes | seconds per call |
|---|---|---|---|---|
| d4_production | 81 | 9 | 21.3 | 15.75 |
| d4_arms | 110 | 5 | 12.0 | 6.53 |
| d4_gradings | 108 | 4 | 20.1 | 11.19 |
| d4_borderline | 12 | 2 | 6.5 | 32.53 |
| d5_all | 78 | 7 | 954.3 | 734.11 |

**389 calls, 1014.2 minutes**, against an estimate of 940. That is 11.4 calls per link tested. Steps 1 and 4 cost nothing: the purge re-reads v2.9 and the pages are built from results already on disk.

## Where the data is

- `results/v2p10/purge.json` — the flagged items and their arm N answers
- `results/v2p10/deeper_d4.json` — depth 4 candidates and every exclusion
- `results/v2p10/arms_d4/`, `grade_d4/` — every answer and every ruling
- `results/v2p10/step4_d4.json` — the decision per link
- `results/v2p10/pages/` — one page per paper plus the index

Every verdict is model against model.
