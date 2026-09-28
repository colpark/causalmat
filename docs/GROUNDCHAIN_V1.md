# groundchain v1

Turning Matter-to-Mechanism reasoning chains into items where reading a figure panel is a necessary step. Five papers, run end to end through Stage 2.

**Verdict: stop.** The reason is Stage 2, and it is a property of the input, not of the machinery. Numbers below.

## Roles and pinned versions

- answerer `gc-answerer` model `claude-sonnet-5`
- checker `gc-checker` model `claude-sonnet-5`
- detector `matmmextract-yolo12m/7a92fbc6571e/imgsz640/v1`, weights sha256 `7a92fbc6571e`, imgsz 640, conf 0.25, iou 0.5
- matcher `match/v4`

The detector string is the one MatMech's own `panels.json` carries, so the tier comparison below is like for like.

## Stage 1: selection funnel

| step | n |
| --- | ---: |
| csv rows | 2645 |
| passed local filter | 135 |
| crossref resolved | 132 |
| in europe pmc full text | 38 |
| and year ge 2021 and cc | 24 |
| after cap 10 per publisher | 23 |
| picks | 20 |
| reserves | 3 |

Publishers among the 23 kept: Springer 7, American 10, Royal 6.

The brief asked for 2023+, a cap of 6 per publisher and 20 picks + 10 reserves. Those cannot hold together on this corpus: they yield **16** papers, no reserves. Relaxed to 2021+ and a cap of 10 on the user's decision.

## Stage 1: fetch

Every publisher route is shut. ACS and RSC return 403, IOP and ECS redirect to a bot wall, Europe PMC's own `/bin/` images 403, the articles are not in NCBI's OA subset and Unpaywall has no PDF. Only `nature.com` serves images to a plain client. What works is Europe PMC's **`supplementaryFiles` zip**, which holds the figure JPEGs under exactly the filenames the JATS `xlink:href` gives. Captions and body text come from `fullTextXML`, images from the zip. No scraping.

| doi | figures | route |
| --- | ---: | --- |
| `10.1038/s41467-021-27311-7` | 7 | epmc |
| `10.1038/s41598-024-63377-1` | 7 | epmc |
| `10.1021/acsami.2c02118` | 9 | epmc |
| `10.1038/s41598-021-00148-2` | 7 | epmc |
| `10.1038/s41598-021-92671-5` | 9 | epmc |

5 of 5 succeeded, 7-9 figures each. No paper fell below the 4-figure threshold, so no reserve was swapped in.

## Stage 2: panel tiers against MatMech

| | tier A | tier B | tier C | figures |
| --- | ---: | ---: | ---: | ---: |
| this run | **51.3%** | 28.2% | 20.5% | 39 |
| MatMech | 34.5% | 37.4% | 28.0% | 425295 |

86 panels, 72 (83.7%) carrying a body use-sentence.

| paper | figures | tiers | panels | with use |
| --- | ---: | --- | ---: | ---: |
| `10.1021_acsami.2c02118` | 9 | {'A': 2, 'B': 6, 'C': 1} | 19 | 13 |
| `10.1038_s41467-021-27311-7` | 7 | {'A': 4, 'B': 2, 'C': 1} | 26 | 25 |
| `10.1038_s41598-021-00148-2` | 7 | {'B': 3, 'A': 3, 'C': 1} | 13 | 11 |
| `10.1038_s41598-021-92671-5` | 9 | {'C': 5, 'A': 4} | 12 | 10 |
| `10.1038_s41598-024-63377-1` | 7 | {'A': 7} | 16 | 13 |

Four fetch bugs were found by these numbers rather than by reading code, each caught because a tier or use count looked wrong:

1. Nature marks panel labels `<bold>a</bold>`. Stripping tags naively gives "a Long-term cycling...", a bare letter the matcher cannot see. All 7 pilot figures landed in tier C with 0 panels matched; converting to `(a)` first moved 4 to tier A.
2. `image_description` was truncated to 4000 characters of 47055, hiding every figure reference past the opening. `panels_with_use` 0 -> 25 of 26.
3. `strip()` replaced every tag with a **space**, so `<xref>Fig. 1</xref>a` became "Fig. 1 a" and the matcher read the panel letter as a separate token. Use-sentences 36.0% -> 83.7% across the five. This also re-wrote the captions and cost 5 points of tier A (56.4% -> 51.3%); kept anyway, because use-sentences are what Stage 3 masks.
4. The figure regex was `<fig\b`, and `\b` matches the hyphen in `<fig-count/>`, which would swallow the first real figure on any paper carrying that element.

## Stage 2: chain steps

| paper | step kinds |
| --- | --- |
| `10.1038/s41467-021-27311-7` | 1 conclusion, 2 mechanism, 2 observation, 1 system, 1 variable |
| `10.1038/s41598-024-63377-1` | 1 conclusion, 1 mechanism, 3 system, 1 variable |
| `10.1021/acsami.2c02118` | 1 conclusion, 1 mechanism, 2 observation, 1 system, 2 variable |
| `10.1038/s41598-021-00148-2` | 1 conclusion, 2 mechanism, 1 observation, 1 system, 1 variable |
| `10.1038/s41598-021-92671-5` | 1 conclusion, 1 mechanism, 1 observation, 2 system, 1 variable |

**6 observation steps across 5 papers.** One paper (`10.1038/s41598-024-63377-1`) has none at all: its chain is system, variable, mechanism and conclusion only, so it can yield no data step and no item.

## Stage 2: linking, and why the run stops here

A link is kept only when the **authors** state that observation in their own text. Panel level first, then figure level.

| granularity | states | related | absent | kept |
| --- | ---: | ---: | ---: | ---: |
| panel | 0 | 5 | 7 | 0 |
| figure | 2 | 6 | 4 | 2 |

### Unsupported M2M claims

All 12 panel-level candidates were rejected. Logged in `links.json`. Three reasons, and all of them are the chain being written at the wrong granularity for a figure:

- **Aggregated across techniques.** One step reads "FT-IR, DSC, XRD, DMA, SEM, conductivity, and transference-number results *collectively* indicate..." — seven techniques. No single caption states that.
- **Methodology, not observation.** "Interleaving EIS with each potential step *allows extraction of* interphase resistance..." describes what a method enables. The labeller still called it an observation.
- **Different granularity.** One step claims capacity collapse and short circuit at ~900 cycles; all four author sentences attached to that panel say the cell *maintained stable* cycling to 890 cycles and that the performance *excludes* Li2S formation. Checked by hand expecting a false negative; the checker was right.

Figure level recovers 2 of 12. Both point at the **same figure of the same paper** and cite the **same quote**, and one of the two is weak: its step claims capacity collapse while the quote it was given describes SEM morphology. So the usable yield is one figure, one technique, from five papers — which fails the brief's own rule that a data step should draw on two different techniques on one claim.

## Stages 3, 4

Not run. Stage 3 builds data steps from linked observations and there are not enough to build one that meets the brief's own constraints. Running the arms on a single item from a single figure would produce a number, not a measurement.

| measure | value |
| --- | --- |
| items built | |
| items kept | |
| arm A / B / C / D | |
| repeat agreement, arm A | |
| free baselines | |
| audit findings | |

## Calls

- **29** model calls: 5 labelling (answerer), 12 panel-level link and 12 figure-level link (checker).
- Every reply was matched to its prompt byte for byte in the dispatching agent's own transcript before it was written to disk. One relay pasted 60 kB of payloads into its hand-back; none of it was used.

- Estimated for all 20 papers, before the pilot: ~1,020 calls, 88% of them Stage 4 arms and grading.

## Verdict: stop

Not because the machinery failed. Selection, fetch and panel extraction all work, and the panel tiers (51.3% A) are better than MatMech's own corpus. The input is the problem, exactly where the brief warned it would be: "almost no step cites a figure". Measured, that is **0 of 12 panel-level links** and **2 of 12 at figure level, both on one figure**.

M2M observation steps are summaries written across several techniques and several figures. They are not panel-scale statements, and no amount of Stage 3 masking or Stage 4 arm design turns a step that aggregates seven techniques into a question one panel answers.

What would be worth trying instead, as a different task: invert the direction. Start from a panel whose finding the authors state plainly, build the closed question and the answer key from that span, and use the M2M chain only for the frame. The answer key has to come from the authors' text anyway — the brief already says so — so the chain is doing less work than the design assumes.

