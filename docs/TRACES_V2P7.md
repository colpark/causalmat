# Traces v2.7 — fixing what v2.6 exposed

Every verdict is model against model.

Same 32 papers. v2.7 does not scale to more. It measures how much of v2.6's necessity signal was noise, replaces the instrument that produced it, widens a flag that was too narrow, settles a contradiction between two checks, and builds a generator that makes merges which actually need what came before.

## Part A — the noise floor

| pairing | rulings | "yes" | rate | chains majority yes | unanimous |
|---|---|---|---|---|---|
| arm A vs arm A (identical prompt) | 189 | 55 | **29.1%** | 15/63 | 31 |
| arm A vs arm B (same chains) | 189 | 98 | 51.9% | 34/63 | 29 |

**The floor is 29.1%.** Nothing was added between those two answers — same prompt, same evidence, two samples — and the v2.6 comparer still called them changed 55 times in 189. So of v2.6's 51.9% yes rate, 56% is sampling variation. The genuine lift from handing over the upstream result is **22.8 points**.

The stop rule was 40%. 29.1% is below it, so the run continued.

15 of 63 chains score a majority "yes" against themselves, and 31 are unanimous on a pair whose correct answer is known to be no. That is the answer to the c055 case in the brief: three repeats agreeing is not decisive when a third of single rulings are false positives. Three flips at 29.1% come up all-heads about 2.5% of the time.

The prompts were the v2.6 files byte for byte. A floor measured on different text would not be comparable with the rate it is meant to correct.

## Part B — a graded comparer

The comparer now scores 0 to 3 on how far the substance differs and must quote the specific difference or say "none". And each chain is judged against itself: necessity counts only when the A-vs-B score beats **that chain's own** A-vs-A score by at least a point, in 2 of 3 repeats. A chain whose answers wander on their own has to clear a higher bar, which no single global threshold can do.

| score | A vs B | A vs A |
|---|---|---|
| 0 | 37 | 75 |
| 1 | 87 | 83 |
| 2 | 59 | 29 |
| 3 | 6 | 2 |

Mean score: **1.18 for A vs B against 0.778 for A vs A.** The gap between the two is the same quantity Part A measured, now on a scale that can show its size rather than rounding it to a yes.

| agreement across the 3 repeats | chains | share |
|---|---|---|
| all three give the identical score | 10 | 16% |
| all three within one point | 50 | 79% |
| all three agree on the necessity decision | 18 | 29% |

The decision is what gets used, so the decision agreement is the number that matters: 29%, which **does not clear the two-thirds target**. (v2.6's yes/no comparer agreed on 46.3%.)

| necessity | chains |
|---|---|
| no | 35 |
| yes | 28 |

## Part C — the widened flag

The flag now fires on **any** limit's `why` that says the downstream does not use, invoke or rely on what the upstream brought, not only when every limit is not_applicable. 17 seams becomes **72 of 135**, 55 new.

**c055 is flagged** (it was not in v2.6). Its seam has one carried limit and three not_applicable, so the structural rule never fired, and the sentence naming the problem was discarded by two v2.6 exclusions at once: it is scoped to a single limit, and its object is an evidence leg rather than a conclusion.

> The downstream item (spi_o13_o9) does not use the AIMD data at all -- it pairs SAXS with ECHEM/GCD instead of with AIMD, so this AIMD-specific limit has nothing to attach to in the joined claim.

Three sentences match the rule while saying something else and are excluded by hand, each with its reason in the code: a caveat being what is absent rather than the upstream's contribution; "does not rely on X alone", which says the downstream added evidence and is the opposite of ignoring it; and a validation of the upstream not being invoked rather than the upstream itself.

All 55 new flags with their trigger sentences are in `results/v2p7/partC.json`. A sample:

- `advanced_com_com_o1_o12a__advanced_com_spi_o1_o3`
  > The downstream item does not use TGA at all -- it pairs FTIR with the optical partitioning photograph instead.
- `advanced_com_com_o5_o7__advanced_com_spi_o5_o13`
  > The downstream item does not use the photograph/darkening evidence at all -- it pairs SEM with dielectric constant data instead.
- `advanced_com_spi_o10_o9__advanced_com_spi_o9_o20`
  > since the downstream item never invokes bonding quality (A) at all, this specific limit does not transfer -- there is no A-to-B dose-response claim in the joined claim to be dropped or carried.
- `advanced_ene_com_o3_o4__advanced_ene_spi_o3_o15`
  > since TEM is absent from the downstream evidence, this identification limit is moot rather than violated.
- `advanced_ene_com_o3_o5__advanced_ene_spi_o3_o6`
  > The downstream item does not invoke TEM/HRTEM at all -- it pairs XRD with GCD, not XRD with TEM -- so this particular representativeness limit is simply not in play in the joined claim's own evidentia
- `advanced_ene_spi_o11_o14__advanced_ene_spi_o14_o15`
  > The downstream joined claim does not invoke the XAS/Zn-N-bonding inference at all;

## Part D — the backbone contradiction

14 backbone joins. v2.5 rated 7 sound and 7 as laundering a limit; v2.6 scope passed 4. They already agree on pass/fail for 9 of 14.

**Correction to the brief.** The brief says the v2.5 join audit rated all backbone seams clean. It did not: it rated 7 of 14 as laundering a limit and 7 as sound. The contradiction is real but it is narrower than 'all clean against 10 of 14 failing'.

The disagreement has a mechanical cause, not a difference of opinion. The v2.6 scope check used the downstream backbone item's `previous_output` as its second text. That field holds the result the item was handed by **its own v5 chain** — the item at (same trace, step = previous_step). v2.5's composition joined items into backbone items on a shared claim id and did not consult the v5 chain at all.

In **13 of 14** joins the upstream is not the v5 previous step. The scope check was comparing this join's upstream against a premise belonging to a different item, so its ten "incompatible" verdicts record that mismatch rather than a scope failure of the join.

| which check is right | joins |
|---|---|
| v2.5 join audit | 13 |
| v2.6 scope | 1 |

| join | upstream is the v5 previous step | v2.5 | v2.6 scope | right |
|---|---|---|---|---|
| acta_materia_M1_M2_M3_s2__acta_materia_M1_M2_M3_s3 | yes | sound | incompatible | v2.6 scope |
| advanced_ene_M1_M2_M4_s2_1__advanced_ene_M1_M2_M4_s2_2 | no | sound | supports only narrower | v2.5 join audit |
| advanced_ene_spi_o4_o5__advanced_ene_M1_M2_M4_s2_2 | no | launders a limit | incompatible | v2.5 join audit |
| advanced_ene_spi_o14_o17__advanced_ene_M1_M2_M4_s3 | no | launders a limit | incompatible | v2.5 join audit |
| bioactive_ma_M5_M7_s2_1__bioactive_ma_M5_M7_s2_2 | no | sound | supports | v2.5 join audit |
| bioactive_ma_com_o11_o12_n18__bioactive_ma_M5_M7_s2_2 | no | launders a limit | incompatible | v2.5 join audit |
| bioactive_ma_spi_o9_o11__bioactive_ma_M5_M7_s2_2 | no | sound | supports only narrower | v2.5 join audit |
| bioactive_ma_spi_o10_o11__bioactive_ma_M5_M7_s2_2 | no | launders a limit | incompatible | v2.5 join audit |
| bioactive_ma_spi_o16_o11__bioactive_ma_M5_M7_s2_2 | no | launders a limit | incompatible | v2.5 join audit |
| bioactive_ma_spi_o16_o11_n25-n18__bioactive_ma_M5_M7_s2_2 | no | launders a limit | incompatible | v2.5 join audit |
| biomaterials_M1_M3_M4_s2_1__biomaterials_M1_M3_M4_s2_2 | no | sound | incompatible | v2.5 join audit |
| biomaterials_spi_o1_o10__biomaterials_M1_M3_M4_s2_2 | no | sound | incompatible | v2.5 join audit |
| biomaterials_spi_o3_o20__biomaterials_M1_M3_M4_s2_2 | no | launders a limit | supports only narrower | v2.5 join audit |
| biomaterials_M2_M4_s2_1__biomaterials_M1_M3_M4_s2_3 | no | sound | incompatible | v2.5 join audit |

The single well-posed case is `acta_materia_M1_M2_M3_s2__acta_materia_M1_M2_M3_s3`, and there v2.6 is right — and v2.5 contradicts **itself**: its `note_for_caller` calls that join a "topic mismatch" while its structured verdict says sound.

3 joins link consecutive sub-steps of one step, a genuine sequential relation, but `previous_step` on a sub-2 item points past sub-1, so the premise text is wrong for those too and their scope verdicts are also void.

## Part E — derived_input

311 candidate triples reduce to **188 distinct (item, target claim) pairs** across 28 of 32 papers. Running all of them would cost about 3100 model calls, so a cap of 3 per paper takes **76** forward.

| dropped at generation | count |
|---|---|
| over the per-paper cap | 112 |
| new obs is one the upstream used | 25 |
| new obs shares a panel with the upstream | 15 |

The exclusion is checked mechanically and twice, by node id and by panel id, and asserted again over the finished items: passed: no item shares an observation node or a panel id with its upstream item.

| paper | candidates | items taken |
|---|---|---|
| Bioactive Materials · j.bioactmat.2019.12.00 | 50 | 3 |
| Advanced Functional Materials · 10.1002_adfm.202005093 | 25 | 3 |
| Journal of Materials Science & Tec · j.jmst.2020.05.053 | 22 | 3 |
| Acta Materialia · 10.1016_j.actamat.2021 | 19 | 3 |
| Advanced Energy Materials · aenm.202003419 | 16 | 3 |
| Journal of Magnesium and Alloys · j.jma.2020.09.027 | 15 | 3 |
| Bioactive Materials · j.bioactmat.2020.02.00 | 15 | 3 |
| Advanced Composites and Hybrid Mat · s42114-021-00366-2 | 15 | 3 |
| Journal of Magnesium and Alloys · j.jma.2020.11.023 | 15 | 3 |
| Journal of Advanced Ceramics · s40145-021-0536-4 | 14 | 3 |
| Advanced Energy Materials · aenm.201301564 | 13 | 3 |
| Journal of Advanced Ceramics · s40145-021-0538-2 | 11 | 3 |
| Advanced Energy Materials · aenm.201601491 | 9 | 3 |
| Biomaterials · j.biomaterials.2011.11 | 9 | 3 |
| Advanced Energy Materials · aenm.202003639 | 8 | 3 |
| Nano Letters · 10.1021_acs.nanolett.6 | 8 | 3 |
| Journal of Magnesium and Alloys · j.jma.2020.02.028 | 7 | 3 |
| Nano Letters · 10.1021_acs.nanolett.0 | 7 | 3 |
| Journal of Advanced Ceramics · s40145-021-0537-3 | 6 | 3 |
| Journal of Magnesium and Alloys · j.jma.2015.01.001 | 6 | 3 |
| Advanced Energy Materials · aenm.202003412 | 4 | 2 |
| Journal of Materials Science & Tec · j.jmst.2021.12.003 | 4 | 3 |
| Advanced Functional Materials · 10.1002_adfm.202008088 | 4 | 3 |
| Materials Characterization · j.matchar.2015.10.016 | 3 | 3 |
| Journal of Magnesium and Alloys · j.jma.2019.01.003 | 3 | 2 |
| Bioactive Materials · j.bioactmat.2020.01.00 | 1 | 1 |
| Journal of Advanced Ceramics · s40145-021-0532-8 | 1 | 1 |
| Rare Metals · s12598-012-0515-6 | 1 | 1 |

| stage | items |
|---|---|
| candidate triples | 311 |
| distinct (item, target claim) pairs | 188 |
| after the cap of 3 per paper | 76 |
| drafted | 76 |
| the drafter says the two sides combine | 75 |

**The necessity gate is skipped, per the Part B stop rule.** Part B's decision agreement was 28.6% against a two-thirds target, and the brief says that when Part B fails, the gate is skipped and the items are built and drafted anyway. So there is no necessity column and no claim that these items compose. Part E's own stop rule -- fewer than 10 items passing necessity -- cannot be evaluated, because nothing was measured against it.

76 of 76 drafted, 0 unparsed, 0 keys failing the belongs-check that caught 11 mis-attached keys in v2.5.

| the drafter's own labels | items |
|---|---|
| dependency: real | 75 |
| inference_validity: follows, weakly | 74 |
| causal_strength: associative | 56 |
| causal_strength: conditional mechanism | 15 |
| causal_strength: discriminating | 4 |
| causal_strength: descriptive | 1 |
| dependency: none | 1 |
| inference_validity: does not follow | 1 |
| inference_validity: follows | 1 |

Read these with care. `dependency: real` on 75 of 76 items and `combines` true on 75 are the DRAFTER's judgement of an item it was shown as a pair, not an independent test. The drafter cannot be the necessity check; that is the whole reason the gate exists. What the labels do say is less flattering and more informative: 74 of 76 are only "follows, weakly", 56 are merely associative, and 71 name something not identifiable. The generator produces pairs that are structurally dependent and evidentially weak.

### Five worked examples

The brief asked for both arms and the comparer's reasoning on each. Those do not exist, because the gate was skipped. What is shown instead is the full item: the input result, the new observation, and the key the drafter wrote from the two.

**`di_bioactive_ma_com_o5_o10_o8_n9`** — Bioactive Materials, edge n7 -> n9, upstream `bioactive_ma_com_o5_o10`

- question: What does this measurement, read together with the established earlier result below, settle about PRP/value that neither settles on its own? Say what the combination supports and what it leaves open.
- input result (arm B only): Taken together, the polarization data and the immersion data provide two independent lines of evidence that converge on the same ranking: Mg-Zn-Y-Nd degrades far faster than 317L SS. The electrochemical scan shows a much lower corrosion potential for Mg-Zn-Y-Nd (near -1.5 V) versus 317L SS (about -0
- new observation `o8` (both arms): pH with Mg-Zn-Y-Nd climbs from 7.4 to ~10 by day 22 and plateaus; blank control peaks ~8.4 then falls to ~7.5; 317L SS falls to ~6.1 at day 20
- panels ['F5a'] against the upstream's ['F3', 'F5b'] — disjoint by construction
- drafted proposition: The already-established faster degradation of Mg-Zn-Y-Nd relative to 317L SS (from the converging polarization and immersion evidence) together with the pH data -- Mg-Zn-Y-Nd's solution climbing from 7.4 to ~10 by day 22 and plateauing there, while the blank control peaks near 8.4 then falls to ~7.5 and 317L SS falls to ~6.1 by day 20 -- 
- labels: {'dependency': 'real', 'inference_validity': 'follows, weakly', 'causal_strength': 'associative'}

**`di_bioactive_ma_com_o1_o2_o3_n8`** — Bioactive Materials, edge n5 -> n8, upstream `bioactive_ma_com_o1_o2`

- question: What does this measurement, read together with the established earlier result below, settle about STR/chemistry/bonding that neither settles on its own? Say what the combination supports and what it leaves open.
- input result (arm B only): FTIR (GATR) assigns specific vibrational bands to bond types present in the PPAm film -- N-H (3350/3210 cm-1), aliphatic C-H, -N=C=O/-C=N (2245/2180 cm-1), C=O/C=N (1645 cm-1), C-N (1230 cm-1) -- while ToF-SIMS independently detects N-containing fragment ions (CH4N m/z 30, C3H9N m/z 59, C4H10N m/z 7
- new observation `o3` (both arms): Starred NO vibration, N=N, N-N and N-O stretch bands appear in NO-PPAm and are absent from the PPAm spectrum
- panels ['F2a'] against the upstream's ['F1b', 'F1c'] — disjoint by construction
- drafted proposition: Because A already establishes (via converging FTIR bond assignments and ToF-SIMS fragment ions) that the PPAm film retains nitrogen within its own molecular structure (e.g., amine N-H, C-N, and other N-containing groups), the new starred NO-vibration, N=N, N-N, and N-O stretch bands that B shows appearing in NO-PPAm but absent from plain 
- labels: {'dependency': 'real', 'inference_validity': 'follows, weakly', 'causal_strength': 'associative'}

**`di_bioactive_ma_com_o5_o7_o10_n17`** — Bioactive Materials, edge n14 -> n17, upstream `bioactive_ma_com_o5_o7`

- question: What does this measurement, read together with the established earlier result below, settle about PRP/value that neither settles on its own? Say what the combination supports and what it leaves open.
- input result (arm B only): Together, the FTIR chemical signature (-COOH ~3400 cm-1, -C=O ~1660 cm-1 on BVLD-PPAmF vs PPAmF) and the QCM-D areal mass trace (rise to ~0.78 ug/cm2 after BVLD injection, settling to ~0.71 after PBS rinse, 0.74 +/- 0.05 ug/cm2 annotated) support that BVLD is chemically immobilised on the coating su
- new observation `o10` (both arms): Thrombin specific activity ~0.65e-3 abs/ng/cm2 on BVLD-PPAmF and BVLD/NO-PPAmF vs ~1.3e-3 on 316L SS, PPAmF and NO-PPAmF (***)
- panels ['F4'] against the upstream's ['F3b', 'F3c'] — disjoint by construction
- drafted proposition: Read together, the established immobilisation result (chemically distinct BVLD retained on the coating at ~0.74 ug/cm2 after PBS rinsing) and the thrombin specific-activity measurement (~0.65e-3 abs/ng/cm2 on BVLD-bearing coatings vs ~1.3e-3 on the non-BVLD surfaces) support that the BVLD material shown to survive rinsing and remain on th
- labels: {'dependency': 'real', 'inference_validity': 'follows, weakly', 'causal_strength': 'associative'}

**`di_bioactive_ma_com_o11_o12_n18_o15_n20`** — Bioactive Materials, edge n18 -> n20, upstream `bioactive_ma_com_o11_o12_n18`

- question: What does this measurement, read together with the established earlier result below, settle about PRF/service_capability that neither settles on its own? Say what the combination supports and what it leaves open.
- input result (arm B only): Together, the SEM morphology and the BIO platelet counts show that BVLD/NO-PPAmF has both the fewest adhered platelets (~5x1e2 cells/mm2, lowest of the five surfaces) and a morphology dominated by a few round, unspread platelets, in contrast to 316L SS and PPAmF (32 and 41x1e2 cells/mm2, many spread
- new observation `o15` (both arms): Photographs: 316L SS and PPAmF tubes are filled by dark thrombus; BVLD-PPAmF and NO-PPAmF partly open; BVLD/NO-PPAmF lumen and foil nearly clean
- panels ['F6b', 'F6c'] against the upstream's ['F5a', 'F5b'] — disjoint by construction
- drafted proposition: Read together, the in-vitro platelet data (fewest adhered platelets, least spread/round morphology on BVLD/NO-PPAmF) and the shunt-tube photographs (316L SS and PPAmF lumens filled with dark thrombus, BVLD-PPAmF and NO-PPAmF only partly open, BVLD/NO-PPAmF lumen and foil nearly clean) show the same five-surface ranking holding at two diff
- labels: {'dependency': 'real', 'inference_validity': 'follows, weakly', 'causal_strength': 'associative'}

**`di_journal_of_m_com_o14_o16_o19_n17`** — Journal of Magnesium and Alloys, edge n24 -> n17, upstream `journal_of_m_com_o14_o16`

- question: What does this measurement, read together with the established earlier result below, settle about MEC/pathway that neither settles on its own? Say what the combination supports and what it leaves open.
- input result (arm B only): Together SEM (a: deformed, elongated relief with no clear boundaries; b,c: equiaxed grains ~2-4 um with grooved boundaries) and EBSD (a: equiaxed grains mostly ~0.5-1.5 um; c: equiaxed grains ~1.5-3 um) show that panel (a) is not genuinely undifferentiated/deformed as SEM alone suggests -- EBSD reve
- new observation `o19` (both arms): After full recrystallization grain size ranks F10d (~1 um) < F7c (~5-8 um) < F9c (~15-30 um, with twinned remnants)
- panels ['F7c', 'F9c', 'F10d'] against the upstream's ['F10a', 'F10b', 'F10c', 'F11a', 'F11c'] — disjoint by construction
- drafted proposition: Read together, the earlier SEM/EBSD result (which orders three sampled regions from a fine, only-EBSD-resolved equiaxed population of about 0.5-1.5 um up through an intermediate ~2-4 um SEM-only estimate to a cross-validated ~1.5-4 um coarser population) and the full-recrystallization ranking (F10d ~1 um < F7c ~5-8 um < F9c ~15-30 um with
- labels: {'dependency': 'real', 'inference_validity': 'follows, weakly', 'causal_strength': 'associative'}

## The updated funnel

Two tracks now, because they measure different things. The v2.5/v2.6 chains are merges found by sharing a claim id; the derived_input items are merges built so that something has to travel.

| stage | chains |
|---|---|
| chains in v2.5 | 130 |
| after dropping covariation | 109 |
| after collapsing chains that share a tail | 82 |
| after step 3 (v2.6 flag) | 67 |
| after step 4, every seam passes the scope check | 63 |
| after step 3 widened to the v2.7 rule | 63 of 135 seams survive the flag |
| after Part B necessity, floor-corrected | 28 |

| derived_input | items |
|---|---|
| candidate triples | 311 |
| distinct (item, target claim) pairs | 188 |
| after the cap of 3 per paper | 76 |
| drafted | 76 |
| the drafter says the two sides combine | 75 |

## Cost

Estimated before starting: **2004 calls** (Part A 378, Part B 378, Part E 1248).

| stage | model calls | relays | wall minutes | seconds per call |
|---|---|---|---|---|
| partA_arms | 189 | 4 | 13.1 | 4.16 |
| partA_compare | 189 | 3 | 22.5 | 7.15 |
| partB | 452 | 6 | 37.4 | 4.96 |
| partE_drafts | 76 | 4 | 8.5 | 6.74 |
| partE_drafts_redo | 76 | 4 | 9.2 | 7.26 |

**Actual: 982 calls, 90.7 minutes** at the 20-agent cap, dispatch to last harvest, relay overhead included. Every reply verified byte for byte against its prompt file from the agent's own transcript.

That is 1022 calls under the 2004 estimated, and the whole difference is Part E: the necessity gate was skipped when Part B failed its agreement target, which removed the 702 arm samples and 468 comparisons that gate would have needed. What was spent instead was 76 drafts twice over, because an id collision in the first pass meant two items would have carried a key drafted for a different item; all 76 were re-drafted on corrected ids rather than the four being patched in place.

Parts C and D cost nothing: they re-read audits that already exist.

## Where the data is

- `results/v2p7/partA.json` — the noise floor, every A-vs-A ruling
- `results/v2p7/graded/` — Part B, every graded prompt and reply
- `results/v2p7/partB.json` — scores, per-chain margins, agreement
- `results/v2p7/partC.json` — every flag with the sentence that triggered it
- `results/v2p7/partD.json`, `partD_cases.json` — the 14 backbone joins side by side
- `results/v2p7/derived_input.json` — candidates, drops and the items taken forward
- `results/v2p7/draft/`, `armsE/`, `gradedE/` — Part E drafts, arms and comparisons

Every verdict is model against model.
