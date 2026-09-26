# Traces v2.9 — the 24 papers outside the pilot

Every verdict is model against model.

The 32 v2.5 papers minus the 8 used in the v2.8 pilot. Every derived_input pair on them, drafted and tested with the method the pilot settled: claims split out of the key, three evidence arms graded against those claims, and an arm that gets nothing but the paper's name. Out of sample in the sense that matters — none of these papers tuned anything.

## Step 0 — the free filters

240 candidate triples on 24 papers, reduced to **88 pairs on 19 papers** without one model call.

| filter | pairs removed |
|---|---|
| v2.7 flagged this upstream as ignored into this claim | 74 |
| same (item, target claim) already taken | 52 |
| new obs is one the upstream used | 14 |
| new obs shares a panel with the upstream | 12 |

The largest is the v2.7 widened "upstream ignored" rule, applied here as: drop a pair when v2.5 already composed a join from this pair's upstream item into an item concluding this pair's target claim, and v2.7 flagged that join as one where the downstream never used the upstream result. If the join that used this exact result for this exact claim came out empty, the pair asks for the same thing again.

5 papers yield nothing:

- Biomaterials · j.biomaterials.2010.02.024 — no two-step item on this paper concludes a claim that points at another claim with an unused, panel-backed observation
- Biomaterials · j.biomaterials.2010.08.096 — no two-step item on this paper concludes a claim that points at another claim with an unused, panel-backed observation
- Progress in Organic Coatings · j.porgcoat.2021.106157 — no two-step item on this paper concludes a claim that points at another claim with an unused, panel-backed observation
- Advanced Materials · 10.1002_adma.202005449 — no two-step item on this paper concludes a claim that points at another claim with an unused, panel-backed observation
- Journal of Advanced Ceramics · s40145-021-0532-8 — no two-step item on this paper concludes a claim that points at another claim with an unused, panel-backed observation

## Step 1 — Haiku calibration

76 tags, 75 check verdicts and 133 gradings rerun on the v2.8 pilot data with the same prompts byte for byte. Only the model differs, and every dispatch was verified as `haiku` from the relay's own transcript.

| role | agreement with Sonnet | bar | verdict |
|---|---|---|---|
| tagging | 29/76 = 38.2% | 85% | **fails** |
| checking | 18/75 = 24.0% | 85% | **fails** |
| grading | 105/133 = 78.9% | 85% | **fails** |
| grading, pilot verdicts | 3/8 | all | **fails** |

On the replies Haiku returned as valid JSON — the unbiased subset, since the salvage drops quotes and a stated without a quote is withdrawn to absent — grading agreement is 100/117 = 85.5%, at the bar rather than over it, and the verdict condition still fails.

| role | how the reply parsed |
|---|---|
| check | prose 1, unparsed 6, json 1 |
| grade | json 117, salvaged 15, unparsed 11, prose 1 |

Schema compliance is the number that decides this at 15,000 papers, and it is not close. Three of my own parser bugs had to be fixed before this was a fair test: Haiku answers the checker in prose, fences its grading JSON, and -- the one that was purely mine -- `obj()` counts braces without respecting string literals, so claims containing Miller indices like {10-12} were unparseable. What survived all three fixes is real: Haiku quotes the answer's words without escaping the quotes inside them.

All roles stay on Sonnet: {"draft": "sonnet (fixed by the brief)", "tag": "sonnet", "check": "sonnet", "grade": "sonnet"}.

## The funnel

| stage | count |
|---|---|
| candidate triples | 240 |
| after the free filters | 88 |
| drafted into a usable key | 88 |
| split into claims | 88 |
| with at least one combined claim | 88 |
| compositional (B beats A and C, N low) | 68 |
| depth 3 candidates | 53 |
| depth 3 links that pass | 40 |

Step 2 dropped nothing: 88 of 88 pairs kept a combined claim. At 15,000 papers that matters — the three production calls per pair are pure cost and all the selection happens in the arm test.

Tag agreement between the two agents was 96.7% (684 of 707), against the pilot's 94.7% on a set four times larger and on papers that tuned nothing.

## Steps 3 and 4 — the arms

| arm | what it held | mean combined | mean limit |
|---|---|---|---|
| A | the measurement with its panels, narrow question | 0.142 | 0.160 |
| B | measurement + earlier result, full question | 0.813 | 0.611 |
| C | the earlier result alone, narrow question | 0.014 | 0.191 |
| N | the paper's title and journal, no evidence | 0.078 | 0.010 |

**68 of 88 items are compositional, 77.3%** (95% CI 67.5–84.8%). The earlier result is needed on 76, the measurement on 84.

**Arm N reaches 0.25 or more on 11 of 88 items, 12.5%.** The stop rule was 15%, so it did not fire.

Items where the paper name alone reaches the claims:

- `di_advanced_ene_com_o11_o13_n12_o14_n14` — N 0.250, B 1.000 · Advanced Energy Materials
- `di_advanced_ene_com_o3_o5_m8_o15_m14` — N 0.500, B 1.000 · Advanced Energy Materials
- `di_advanced_ene_com_o4_o5_o15_m14` — N 1.000, B 0.000 · Advanced Energy Materials
- `di_advanced_ene_com_o9_o11_o12_r2` — N 0.500, B 1.000 · Advanced Energy Materials
- `di_advanced_fun_spi_o9_o12_o20_a15` — N 0.333, B 1.000 · Advanced Functional Materials
- `di_biomaterials_spi_o1_o10_o17_n12` — N 1.000, B 0.667 · Biomaterials
- `di_journal_of_a_spi_o2_o1_o10_n15` — N 0.333, B 1.000 · Journal of Advanced Ceramics
- `di_journal_of_m_com_o14_o16_n10_o20_n12` — N 0.750, B 1.000 · Journal of Magnesium and Alloys
- `di_journal_of_m_com_o2_o3_o13_n18` — N 0.500, B 1.000 · Journal of Magnesium and Alloys
- `di_journal_of_m_spi_o15_o16_o11_n16` — N 0.500, B 0.500 · Journal of Materials Science & Technology
- `di_nano_letters_spi_o8_o9_o10_n17` — N 1.000, B 1.000 · Nano Letters

11 items fell in the 0.10–0.40 borderline band and got a second sample of A, B and C. **1 flipped.**

- `di_rare_metals_com_o2_o5_o1_s1` — one sample said True, two samples say False

### Per paper

| paper | items | compositional |
|---|---|---|
| Advanced Composites and Hybrid M · s42114-021-00366-2 | 9 | 8 |
| Journal of Materials Science & T · j.jmst.2020.05.053 | 10 | 8 |
| Bioactive Materials · j.bioactmat.2020.02.00 | 7 | 7 |
| Advanced Energy Materials · aenm.202003419 | 6 | 5 |
| Advanced Functional Materials · 10.1002_adfm.202005093 | 8 | 5 |
| Biomaterials · j.biomaterials.2011.11 | 7 | 5 |
| Journal of Magnesium and Alloys · j.jma.2020.09.027 | 6 | 5 |
| Journal of Magnesium and Alloys · j.jma.2020.11.023 | 5 | 5 |
| Journal of Magnesium and Alloys · j.jma.2015.01.001 | 5 | 4 |
| Advanced Energy Materials · aenm.201601491 | 4 | 3 |
| Journal of Advanced Ceramics · s40145-021-0536-4 | 3 | 3 |
| Nano Letters · 10.1021_acs.nanolett.6 | 3 | 3 |
| Journal of Advanced Ceramics · s40145-021-0538-2 | 3 | 2 |
| Journal of Magnesium and Alloys · j.jma.2020.02.028 | 4 | 2 |
| Advanced Energy Materials · aenm.202003412 | 2 | 1 |
| Bioactive Materials · j.bioactmat.2020.01.00 | 1 | 1 |
| Nano Letters · 10.1021_acs.nanolett.0 | 2 | 1 |
| Advanced Energy Materials · aenm.201301564 | 2 | 0 |
| Rare Metals · s12598-012-0515-6 | 1 | 0 |

## Step 5 — depth 3

68 compositional items yielded **53 next-link candidates** across 32 of them, at most 2 each.

| dropped at generation | count |
|---|---|
| over the 2-per-item cap | 12 |
| observation already used in the chain | 8 |
| panel already used in the chain | 4 |

passed: no next link reuses a node or panel from its own chain — checked against every step of the chain, not just the one before, so a link cannot quietly re-read the chain's own first measurement.

**40 of 51 next links pass, 78.4%** (95% CI 65.4–87.5%), against 77.3% at depth 2.

**40 depth 3 chains hold end to end** — both links passing.

### Three worked depth 3 chains

#### `nl_di_journal_of_m_com_o15_o16_o10_n18_o20_n19`

Journal of Magnesium and Alloys

**step 1** — the v2.5 two-step item `journal_of_m_com_o15_o16` (complementary)

- new observation `o15, o16`: (d) fine uniform features ~0.3-0.8 um, far finer than (b),(c) at the same 2 um scale  +  IPF maps: (a) equiaxed grains mostly ~0.5-1.5 um; (c) equiaxed grains ~1.5-3 um
- key: The EBSD IPF maps establish that the equiaxed features visible in panels (a) and (c) are genuine crystallographic grains, sized about 0.5-1.5 um in (a) and about 1.5-3 um in (c). The SEM image separately shows that panel (d) contains much finer, uniform equiaxed features (about 0.3-0.8 um) than pane

**step 2** — link 1, `di_journal_of_m_com_o15_o16_o10_n18` — its key became the next earlier result

- earlier result: The EBSD IPF maps establish that the equiaxed features visible in panels (a) and (c) are genuine crystallographic grains, sized about 0.5-1.5 um in (a) and about 1.5-3 um in (c). The SEM image separately shows that panel (d) contains much finer, uniform equiaxed features (about 0.3-0.8 um) than pane
- new observation `o10`: 423K-8+373K-3+25us-10min curve is highest of the three EPT curves: max ~447 MPa vs ~370 and ~356 MPa
- key: Read together, A's morphological trend (equiaxed feature/grain size decreasing from the EBSD-confirmed ~1.5-3 um grains in (c) down to the ~0.3-0.8 um SEM features in (d)) and B's finding that the 423K-8+373K-3+25us-10min EPT curve is the highest of the three EPT curves (max ~447 MPa vs ~370 and ~35
- arms: A 0.000, B 1.000, C 0.000, N 0.000

**step 3** — link 2, `nl_di_journal_of_m_com_o15_o16_o10_n18_o20_n19`

- earlier result: Read together, A's morphological trend (equiaxed feature/grain size decreasing from the EBSD-confirmed ~1.5-3 um grains in (c) down to the ~0.3-0.8 um SEM features in (d)) and B's finding that the 423K-8+373K-3+25us-10min EPT curve is the highest of the three EPT curves (max ~447 MPa vs ~370 and ~35
- new observation `o20`: 'This study' points (~275/380, ~295/355, ~335/448 MPa) all above every literature point (max ~240 YS, ~318 UTS)
- key: Read together, the earlier result (finest equiaxed features in (d) linked to the highest of the three internal EPT curves, ~447 MPa) and the new comparison (all three 'this study' points, ~275/380, ~295/355, ~335/448 MPa, sit above every literature AZ61 point, max ~240 YS/~318 UTS) support that the 
- arms: A 0.000, B 1.000, C 0.000, N 0.000

#### `nl_di_journal_of_m_spi_o1_o13_o15_n9_o21_n10`

Journal of Materials Science & Technology

**step 1** — the v2.5 two-step item `journal_of_m_spi_o1_o13` (spine_edge)

- new observation `o1, o13`: XRD reflections indexed to L12 (incl. weak superlattice peaks near 25 and 35 deg) and B2 (near 31, 44.6 deg)  +  At first strain step one lamella is featureless while the neighbour shows mottled contrast and line contras
- key: The as-cast alloy is confirmed (by XRD) to contain two ordered phases (L12 and B2), and at the first strain step the TEM pair shows one lamella remaining featureless while its neighbor develops mottled contrast plus line contrast along the interface -- together indicating that the two-phase system r

**step 2** — link 1, `di_journal_of_m_spi_o1_o13_o15_n9` — its key became the next earlier result

- earlier result: The as-cast alloy is confirmed (by XRD) to contain two ordered phases (L12 and B2), and at the first strain step the TEM pair shows one lamella remaining featureless while its neighbor develops mottled contrast plus line contrast along the interface -- together indicating that the two-phase system r
- new observation `o15`: Dense dislocation band labelled as pile-up along a lamella boundary
- key: Read together, the earlier TEM contrast asymmetry (one lamella featureless, its neighbor developing mottled contrast plus line contrast along the interface) and the dense dislocation pile-up band at a lamella boundary (F4a, F4c) support that the mottled/line contrast seen in the responding lamella c
- arms: A 0.500, B 1.000, C 0.000, N 0.000

**step 3** — link 2, `nl_di_journal_of_m_spi_o1_o13_o15_n9_o21_n10`

- earlier result: Read together, the earlier TEM contrast asymmetry (one lamella featureless, its neighbor developing mottled contrast plus line contrast along the interface) and the dense dislocation pile-up band at a lamella boundary (F4a, F4c) support that the mottled/line contrast seen in the responding lamella c
- new observation `o21`: Many straight parallel dislocation lines on one slip trace across the field
- key: Read together, the pile-up band at the lamella boundary (Observation A) and the field of many straight, parallel dislocation lines along a single slip trace (Observation B, F5b) show that the microstructure contains at least two qualitatively distinct dislocation morphologies -- a tangled/pile-up ar
- arms: A 0.000, B 1.000, C 0.500, N 0.000

#### `nl_di_journal_of_m_spi_o3_o13_o15_n11_o9_n12`

Journal of Materials Science & Technology

**step 1** — the v2.5 two-step item `journal_of_m_spi_o3_o13` (spine_edge)

- new observation `o3, o13`: TEM bright-field: parallel alternating straight lamellae A and B with sharp interfaces  +  At first strain step one lamella is featureless while the neighbour shows mottled contrast and line contrast along the interface
- key: Taken together, the baseline two-phase lamellar architecture with sharp A/B interfaces (Observation A) and the asymmetric contrast that appears at the first strain step (Observation B) support that the alternating lamellar structure is the substrate on which strain is partitioned unequally between t

**step 2** — link 1, `di_journal_of_m_spi_o3_o13_o15_n11` — its key became the next earlier result

- earlier result: Taken together, the baseline two-phase lamellar architecture with sharp A/B interfaces (Observation A) and the asymmetric contrast that appears at the first strain step (Observation B) support that the alternating lamellar structure is the substrate on which strain is partitioned unequally between t
- new observation `o15`: Dense dislocation band labelled as pile-up along a lamella boundary
- key: Read together with the earlier phase-selective, interface-localized onset of plasticity (mottled contrast and line contrast along one lamella's interface, versus a featureless neighbour), the dense dislocation band identified as a pile-up along a lamella boundary gives a concrete microstructural rea
- arms: A 0.200, B 1.000, C 0.000, N 0.000

**step 3** — link 2, `nl_di_journal_of_m_spi_o3_o13_o15_n11_o9_n12`

- earlier result: Read together with the earlier phase-selective, interface-localized onset of plasticity (mottled contrast and line contrast along one lamella's interface, versus a featureless neighbour), the dense dislocation band identified as a pile-up along a lamella boundary gives a concrete microstructural rea
- new observation `o9`: Inset true stress rises from ~410 to ~1070 MPa up to 0.06 true strain
- key: Taken together, the interface-localized dislocation pile-up seen at the first strain step (A) and the macroscopic stress-strain response (B, true stress rising from ~410 to ~1070 MPa up to 0.06 true strain) support that the microstructural dislocation accumulation at the lamella boundary is occurrin
- arms: A 0.000, B 1.000, C 0.000, N 0.000

## Cost

| stage | model calls | relays | wall minutes | seconds per call |
|---|---|---|---|---|
| step1_calibration_actual | 161 | 5 | 31.6 | 11.79 |
| step2_draft | 88 | 4 | 10.2 | 6.98 |
| step2_tagcheck | 176 | 8 | 26.5 | 9.05 |
| step3_answers | 352 | 4 | 23.9 | 4.07 |
| step4_gradings | 352 | 5 | 34.3 | 5.84 |
| step4_borderline | 66 | 2 | 22.3 | 20.29 |
| step5_production | 159 | 9 | 30.4 | 11.46 |
| step5_arms | 204 | 4 | 15.9 | 4.67 |
| step5_gradings | 240 | 9 | 456.3 | 114.07 |
| step5_borderline | 30 | 2 | 12.5 | 25.01 |

**1828 calls, 663.9 minutes** at the 20-agent cap, dispatch to last harvest. Every reply verified byte for byte against its prompt file, and every model verified from the transcript.

|  | calls | per item | per paper |
|---|---|---|---|
| production (draft, tag, check) | 264 | 3.0 | 13.9 |
| testing (4 arms + gradings + borderline) | 770 | 8.75 | 40.5 |
| all stages | 1828 | 20.77 | 76.2 |

Production is 3.0 calls per pair, as designed. Testing every item costs 8.75 more, which is the number that would have to come down to run a pool of 15,000.

## Where the data is

- `results/v2p9/pairs.json` — Step 0, every pair and every filter
- `results/v2p9/calib.json` — Step 1, Haiku against Sonnet
- `results/v2p9/draft/`, `split/`, `check/`, `step2.json` — Step 2
- `results/v2p9/arms/`, `grade/` — Steps 3 and 4, every answer and ruling
- `results/v2p9/step4.json` — the decision per item
- `results/v2p9/nextlink.json`, `step5.json` — depth 3

Every verdict is model against model.
