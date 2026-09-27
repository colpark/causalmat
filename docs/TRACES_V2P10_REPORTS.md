# v2.10 reports: the chains, paper by paper

One self-contained HTML page per paper. Each page carries the paper's whole argument graph, every passing chain it supports from depth 2 to depth 5, and, under every step, the figure panel the step read, the box it occupies on its figure, its caption and the sentences the paper writes about it.

**Every verdict is model against model.**

## What was built

- **86 chains** across **17 papers**: 40 at depth 2, 26 at depth 3, 15 at depth 4, 5 at depth 5.
- **18 pages** (17 papers + an index), **19.3 MB** in total.
- **146 distinct figure panels** shown, each as a crop, as a box on its whole figure, and as the text the paper writes about it.

### Page sizes

| paper | chains | deepest | panels | size |
| --- | ---: | ---: | ---: | ---: |
| Advanced_Composites_and_Hybrid_Materials / s42114-021-00366-2 | 10 | 3 | 15 | 2.19 MB |
| Advanced_Functional_Materials / 10.1002_adfm.202005093 | 8 | 4 | 11 | 1.98 MB |
| Nano_Letters / 10.1021_acs.nanolett.6b04294 | 5 | 4 | 7 | 1.84 MB |
| Bioactive_Materials / j.bioactmat.2020.02.005 | 9 | 4 | 13 | 1.68 MB |
| Advanced_Energy_Materials / aenm.202003419 | 8 | 5 | 12 | 1.54 MB |
| Journal_of_Magnesium_and_Alloys / j.jma.2020.11.023 | 7 | 5 | 10 | 1.50 MB |
| Journal_of_Materials_Science_&_Technology / j.jmst.2020.05.053 | 8 | 3 | 9 | 1.46 MB |
| Journal_of_Magnesium_and_Alloys / j.jma.2015.01.001 | 4 | 2 | 10 | 1.32 MB |
| Journal_of_Magnesium_and_Alloys / j.jma.2020.09.027 | 5 | 2 | 12 | 1.18 MB |
| Advanced_Energy_Materials / aenm.201601491 | 3 | 3 | 7 | 0.99 MB |
| Journal_of_Magnesium_and_Alloys / j.jma.2020.02.028 | 2 | 3 | 8 | 0.74 MB |
| Biomaterials / j.biomaterials.2011.11.042 | 5 | 3 | 6 | 0.69 MB |
| Journal_of_Advanced_Ceramics / s40145-021-0536-4 | 6 | 3 | 7 | 0.69 MB |
| Journal_of_Advanced_Ceramics / s40145-021-0538-2 | 3 | 4 | 8 | 0.60 MB |
| Bioactive_Materials / j.bioactmat.2020.01.002 | 1 | 2 | 3 | 0.35 MB |
| Nano_Letters / 10.1021_acs.nanolett.0c04053 | 1 | 2 | 5 | 0.30 MB |
| Advanced_Energy_Materials / aenm.202003412 | 1 | 2 | 3 | 0.23 MB |

Largest 2.19 MB, smallest 0.23 MB, median 1.18 MB.

## The written paragraph, and what the check removed

One Sonnet call wrote a paragraph for each chain from the chain's stored texts alone. A second Sonnet call read it sentence by sentence against those same texts and had to quote the text supporting each sentence. A sentence kept its place only when the checker both called it supported **and** produced a quote; "supported" with no quote is the checker asserting a support it could not point to, so those were removed too.

- **443 sentences written**, **399 kept** (90.1%), **44 removed** (9.9%).
- Chains whose paragraph did not survive checking at all: 0.
- Check replies that could not be parsed: 0.

| depth | sentences written | kept | kept % | 95% CI |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 216 | 187 | 86.6% | 81.4&ndash;90.5% |
| 3 | 130 | 118 | 90.8% | 84.6&ndash;94.6% |
| 4 | 68 | 65 | 95.6% | 87.8&ndash;98.5% |
| 5 | 29 | 29 | 100.0% | 88.3&ndash;100.0% |

A removed sentence is not a wrong sentence; it is a sentence the stored texts do not carry. The commonest kind adds a mechanism or a motive that reads as obvious and is nowhere in the record. Examples, verbatim:

- `C26` — Together these establish that grafting MPTMS onto BST-SH corresponds to a switch from hydrophilic to lipophilic surface behavior, since the chemical signature and the phase-partitioning behavior appear together only in the modified sample.
- `C26` — Step 2 needed that conclusion because the new measurement -- a film micrograph showing BST@Ag1% particles covered by matrix with blurred outlines and no interfacial gaps -- is purely morphological and says nothing about chemistry on its own.
- `C47` — On its own, this is just a declining series with Ag content.
- `C49` — Step 2 needed that conclusion as its baseline because it supplies the only established composition-dependent result (the four Tg values) against which a new measurement can be judged.
- `C53` — Step 2 needed that established association before it could use its new measurement, a capacity-fade curve (steep drop over roughly cycles 20-50, then slow decline to ~55 mAh/g by cycle 250, with CE near 100%): on its own the capacity curve shows only fade, not a cause.
- `C54` — Alone, this carbon result shows only a selective carbon change; paired with the nitrogen result, it shows the same zinc-deposition step selectively removes one nitrogen environment (398 eV) and one carbon environment (290.1 eV) together, leaving the other nitrogen and carbon features intact.
- `C56` — That alone only shows the hosts differ in overpotential, so the chain adds Coulombic efficiency data, which needed the overpotential result to become a claim about durability: CnC HS holds roughly 93-100% CE out to about 205 cycles, while C HS collapses to zero CE by 40-48 cycles and its data end near 50 cycles.
- `C56` — Step 2 then hands in a full-cell capacity trace, needed because the prior step only established a host-level link and left open whether that advantage carries into an actual working cell;

## New finding 1: the caveat ledger

Each step of a chain attached qualifications to its own result. Nothing in the benchmark ever checked whether the chain's **final** claim still respected the qualifications its **earlier** steps had attached. This asked that question directly: every qualification, in the order it was attached, ruled against the final conclusion.

Across 86 chains, **1007 qualifications** were ruled.

| ruling | n | share |
| --- | ---: | ---: |
| respects | 865 | 85.9% |
| ignores | 140 | 13.9% |
| contradicts | 2 | 0.2% |

By depth — the interesting axis, because a longer chain has more to forget:

| depth | chains | qualifications | respects | ignores | contradicts | respected % | 95% CI |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 40 | 306 | 244 | 60 | 2 | 79.7% | 74.9&ndash;83.9% |
| 3 | 26 | 332 | 279 | 53 | 0 | 84.0% | 79.7&ndash;87.6% |
| 4 | 15 | 259 | 236 | 23 | 0 | 91.1% | 87.0&ndash;94.0% |
| 5 | 5 | 110 | 106 | 4 | 0 | 96.4% | 91.0&ndash;98.6% |

The respected share rises at every step of depth, and the share of the written paragraph that survives checking rises with it. **This is almost certainly selection, not care.** A chain reaches depth 5 only by passing the arm test at four consecutive links; a depth-2 chain passed it once. The deeper chains are the survivors of more filtering, and the same property that gets a link past the arm test — a conclusion that stays close to what the two measurements jointly license — is the property the ledger rewards. Read this as a statement about the chains that survive, not about what depth does to reasoning.

Two further reasons not to lean on the interval: the qualifications inside one chain are not independent of each other, since later steps inherit and restate earlier limits, so the interval above is narrower than the truth; and depth 5 is 5 chains.

53 of 86 chains end on a claim that ignores or contradicts at least one qualification they collected on the way.

| chain | depth | qualifications | ignored | contradicted |
| --- | ---: | ---: | ---: | ---: |
| C17 | 4 | 20 | 9 | 0 |
| C41 | 3 | 13 | 7 | 0 |
| C54 | 2 | 8 | 6 | 0 |
| C42 | 3 | 13 | 6 | 0 |
| C48 | 2 | 6 | 5 | 0 |
| C62 | 2 | 7 | 3 | 2 |
| C36 | 3 | 12 | 5 | 0 |
| C21 | 3 | 14 | 4 | 0 |
| C55 | 2 | 7 | 4 | 0 |
| C57 | 2 | 8 | 4 | 0 |
| C35 | 3 | 12 | 4 | 0 |
| C37 | 3 | 12 | 4 | 0 |

## New finding 2: the chain against the paper's own wording

The chain's final conclusion was set beside the label the paper's own argument graph gives that claim, and ruled: the same claim, a narrower one, a broader one, or a conflicting one.

| ruling | n | share |
| --- | ---: | ---: |
| agrees | 4 | 4.7% |
| narrower | 41 | 47.7% |
| broader | 40 | 46.5% |
| conflicts | 1 | 1.2% |

| depth | chains | agrees | narrower | broader | conflicts |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 40 | 4 | 21 | 15 | 0 |
| 3 | 26 | 0 | 11 | 15 | 0 |
| 4 | 15 | 0 | 5 | 9 | 1 |
| 5 | 5 | 0 | 4 | 1 | 0 |

A `broader` ruling is the one that matters: it says the chain claimed more than the paper's own wording of that claim supports. `narrower` is the benign direction — the chain hedged where the paper did not.

`agrees` is rare (4 of 86), and that is expected rather than alarming: the chain writes a proposition built from two measurements, while the paper's graph node is a one-line label for the claim. The two almost never match in scope, so the ruling is nearly always a direction rather than an identity.

## The checks

- **Every chain rendered once, in full.** 86 of 86 chains appear on exactly one page; 0 missing, 0 duplicated, 0 with a step id absent from their page.
- **Every cited panel shown.** 146 of 146 panel ids cited by any step appear on their paper's page with an anchor; 0 missing. 0 lettered panels lacked a recorded box on their figure. Whole-figure citations (`#F3`, no panel letter) carry no box because the crop already is the whole figure.
- **Every surviving sentence carries a quote.** 0 of 399 kept sentences have an empty quote.
- **Nothing reaches the network.** 0 external references across all pages: no stylesheet, script, font or image is fetched, and every image is an inline `data:` URI.
- **Rendered and looked at.** Both the deepest-chain paper and a depth-2-only paper were screenshotted in a headless browser — header, argument graph with a chain selected, chain index, trajectory strip, step block with panels, seam band, caveat ledger and the written paragraph, at 1400 px and at 390 px — and inspected for overlap and clipping.

### On the images

A crop at or under 1400 px on its long side is embedded as the file's own bytes: no resample, no re-encode, no annotation. 23 images exceeded the cap and were downscaled once with LANCZOS. The red box is drawn on the **whole figure** as an SVG overlay, never on the crop, so no pixel of the evidence is painted over.

## Cost

- **366 Sonnet calls** against 344 estimated: 86 paragraphs, 86 checks, 86 caveat ledgers and 86 paper comparisons, plus 1 + 21 re-runs.
- The re-runs are the whole reason the byte-check exists, so they are itemised rather than averaged away. One round-A paragraph prompt was delivered 28 bytes short, the phrase "&nbsp;co-occurrence" silently dropped from two places in the middle; the relay counted it as delivered and the paragraph would have read fine. Twenty-one round-B check prompts embedded a paragraph that still carried the writer's own output framing; the prompts were regenerated, which made the byte-check reject those sends on its own, and the checks were re-run.
- Every reply was matched to its prompt byte for byte in the dispatching agent's own transcript before it was written to disk. The relay's own report is not evidence.

