# Traces v2.6 — tightening the v2.5 merges

Every verdict is model against model.

v2.6 keeps v2.5's 32 papers and its two-step items. It changes only which merges count.

An external review of the Nano Letters page (nanolett.6b04294) found merges that link two items by a shared claim id although the second step never uses what the first concluded. One trace there dropped the XANES result entirely and still reported "every limit survives". Two traces were the same chain under two generator labels. The covariation generator paired series because they had the same length. Each of those is a separate defect and v2.6 addresses each separately.

## Where this run stopped

**The stop rule fired.** The brief said to stop rather than filter if step 5's repeats agree on fewer than two thirds of chains. They agree on 38 of 82 — 46.3%. So steps 1 to 4 are reported as results and step 5 is reported as an instrument that is not yet good enough to filter on. Steps 6 and 7 — counting the merges and rebuilding the pages with a counted/not-counted label — were **not applied**, because both consume step 5 as a gate.

Everything step 5 needs was nevertheless run in full: 492 arm answers and 313 comparisons, all verified byte for byte. The numbers are in `results/v2p6/necessity.json` and the step-5 column of the funnel below is shown for information, not as a result.

The other stop rule did not fire: 34 chains would survive all three gates, above the floor of 10.

## The funnel

| stage | chains | lost here |
|---|---|---|
| chains in v2.5 | 130 |  |
| after dropping covariation | 109 | 21 |
| after collapsing chains that share a tail | 82 | 27 |
| after step 3, no seam ignores the upstream result | 67 | 15 |
| after step 4, every seam passes the scope check | 63 | 4 |
| after step 5, the upstream changes the last answer *(not reliable, see below)* | 34 | 29 |

**Through the checks that hold, 63 of 130 v2.5 chains survive.** 130 became 82 on structure alone: 21 chains used a covariation item and 27 were the same chain under another opener. Of those 82, 15 are lost at step 3 because a seam in them never uses the upstream result, and 4 more at step 4 on scope. Step 5 would remove 29 more, leaving 34, but see the stop rule.

At seam level, on the two gates that hold: 135 seams, 17 flagged upstream-ignored and 12 failing the scope check, leaving 109 that clear both. (51 would also clear step 5, not reported as a result.)

## Chain depth, before and after

| depth | v2.5 | after dropping covariation | after dedup | through steps 3+4 | through step 5 *(not reliable)* |
|---|---|---|---|---|---|
| 2 | 68 | 61 | 51 | 42 | 22 |
| 3 | 31 | 25 | 17 | 11 | 6 |
| 4 | 26 | 21 | 12 | 8 | 4 |
| 5 | 3 | 0 | 0 | 0 | 0 |
| 6 | 2 | 2 | 2 | 2 | 2 |

The two depth-5 chains were both covariation-dependent and are gone. 27 openers were folded into a chain that already existed.

## Step 3 — how many clean seams were empty

17 of 135 seams are flagged. No model call: the v2.5 join audits, re-read. 14 by the structural signal (every upstream limit ruled not_applicable, which is the audit saying no qualification of the upstream result has any object downstream), 6 by the audit stating in words that the derived result is dropped, 2 by both.

**16 of the 17 flagged seams showed "every limit survives" on the v2.5 page.** No limit was ruled dropped because there was nothing downstream for an upstream limit to qualify. The seam looked clean for the same reason it was empty.

## Step 4 — scope

| verdict | seams |
|---|---|
| supports | 104 |
| supports only narrower | 19 |
| incompatible | 12 |

135 of 135 joins ruled, none unparsed.

The agent saw two texts and nothing else: the upstream item's key proposition with its limits, and the premise the next step takes as given. No claim ids, no paper-level claim text, no item or paper names, no panels, no generator label. An id scrub runs over both texts and the build refuses any prompt in which a bare node id survives it.

One limitation to record. `hidden_key_claims` on an item are verbatim graph node labels, so the ban on paper-level claim text rules out the only derived rendering of the join claim. The premise is therefore the downstream item's own join-side observation — and 118 of the 121 v2.5-to-v2.5 joins read the very observation the upstream item already read. The downstream usually does not need a derived result at all; it re-reads the raw measurement. That is why the scope check cannot be the whole test, and why step 5 exists.

| premise source | supports | supports only narrower | incompatible |
|---|---|---|---|
| downstream reads the same observation | 103 | 15 | 0 |
| downstream reads a different observation | 0 | 1 | 2 |
| v5 backbone, previous_output | 1 | 3 | 10 |

## Step 5 — necessity

For each chain the last item was answered twice: arm A with its question and its own evidence, panels included; arm B with exactly that plus the upstream item's key proposition and limits, handed over as a settled earlier result. A second agent read both answers and ruled whether the conclusion or the uncertainty changed. Three repeats, majority of three.

| necessity (majority of 3) | chains |
|---|---|
| yes | 46 |
| no | 36 |

| votes over the 3 repeats | chains | share |
|---|---|---|
| 3 yes / 0 no | 21 | 26% |
| 2 yes / 1 no | 25 | 30% |
| 1 yes / 2 no | 19 | 23% |
| 0 yes / 3 no | 17 | 21% |

**Stability: 38 of 82 chains had all three repeats agree, 46.3%.** The stop rule was two thirds, so **this does not clear it and the run stops rather than filter on a noisy check.**

How noisy: the per-repeat "yes" rate is 0.537, so three independent coin flips at that rate would agree 25.4% of the time. The observed 46.3% is above that, so the check is not pure noise — it carries real signal. It is just nowhere near separable enough to gate on: 44 of 82 chains, 54%, split 2-1, and a majority of three on a coin that lands 54% heads is not a verdict.

Three things to fix before this check is worth running again:

1. **The comparer is asked a yes/no question about a difference of degree.** Two prose answers to an open question differ in wording every time; ruling whether the difference "matters" is the judgement, and it is being forced into a binary. A graded scale, or asking the same agent to rank the two answers on a stated dimension, would be steadier.

2. **Arm A and arm B are separate samples, so they differ for two reasons at once** — the upstream result, and ordinary answer-to-answer variation. Sampling arm A three times and comparing it against itself would measure that floor directly. That control was not run here and should be: without it we cannot say how much of the 54% "yes" rate is the upstream result at all.

3. **Necessity probes only the last hop**, so a chain is judged on one merge (see below).

| depth | necessity yes | necessity no |
|---|---|---|
| 2 | 28 | 23 |
| 3 | 9 | 8 |
| 4 | 7 | 5 |
| 6 | 2 | 0 |

Two limitations of this test, both of them consequences of the brief's design and worth stating plainly. First, **necessity probes only the last hop of a chain.** A depth-4 chain and a depth-3 chain that end with the same merge get a byte-identical pair of arms and so the same verdict: 17 of the 164 arm prompts are duplicates of another chain's for exactly this reason. "Compositional" is therefore a verdict on a chain's final merge, not on every merge along it. Second, arm B hands the upstream result over as settled, so a comparer ruling "no" is saying the last step reaches the same place without it -- not that the upstream result is wrong.

## Per paper

| paper | chains | pass 3 | pass 3+4 | seams | ignored | compositional *(not reliable)* | seams counted *(not reliable)* |
|---|---|---|---|---|---|---|---|
| Advanced Composites and Hybrid · s42114-021-00366-2 | 7 | 7 | 7 | 9 | 0 | 4 | 6 |
| Journal of Magnesium and Alloy · j.jma.2020.09.027 | 6 | 6 | 6 | 6 | 0 | 2 | 2 |
| Nano Letters · 10.1021_acs.nanolett.0c040 | 5 | 5 | 5 | 5 | 0 | 2 | 2 |
| Advanced Functional Materials · 10.1002_adfm.202005093 | 5 | 4 | 4 | 11 | 1 | 3 | 7 |
| Journal of Magnesium and Alloy · j.jma.2015.01.001 | 4 | 4 | 4 | 4 | 0 | 1 | 1 |
| Bioactive Materials · j.bioactmat.2019.12.006 | 7 | 5 | 3 | 17 | 2 | 1 | 1 |
| Journal of Magnesium and Alloy · j.jma.2020.11.023 | 6 | 3 | 3 | 13 | 4 | 0 | 0 |
| Advanced Energy Materials · aenm.201601491 | 4 | 3 | 3 | 5 | 1 | 3 | 4 |
| Bioactive Materials · j.bioactmat.2020.02.005 | 4 | 3 | 3 | 5 | 1 | 3 | 4 |
| Journal of Materials Science & · j.jmst.2021.12.003 | 3 | 3 | 3 | 4 | 0 | 2 | 2 |
| Materials Characterization · j.matchar.2015.10.016 | 3 | 3 | 3 | 3 | 0 | 1 | 1 |
| Advanced Energy Materials · aenm.202003419 | 3 | 3 | 2 | 7 | 0 | 1 | 1 |
| Journal of Advanced Ceramics · s40145-021-0538-2 | 3 | 2 | 2 | 9 | 1 | 2 | 5 |
| Nano Letters · 10.1021_acs.nanolett.6b042 | 3 | 2 | 2 | 3 | 1 | 1 | 1 |
| Advanced Energy Materials · aenm.201301564 | 2 | 2 | 2 | 5 | 0 | 1 | 1 |
| Advanced Energy Materials · aenm.202003639 | 2 | 2 | 2 | 3 | 0 | 2 | 3 |
| Journal of Advanced Ceramics · s40145-021-0536-4 | 2 | 2 | 2 | 2 | 0 | 1 | 1 |
| Journal of Materials Science & · j.jmst.2020.05.053 | 2 | 2 | 2 | 7 | 0 | 2 | 7 |
| Biomaterials · j.biomaterials.2011.11.042 | 4 | 2 | 1 | 8 | 3 | 0 | 0 |
| Advanced Energy Materials · aenm.202003412 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| Advanced Functional Materials · 10.1002_adfm.202008088 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |
| Bioactive Materials · j.bioactmat.2020.01.002 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| Journal of Advanced Ceramics · s40145-021-0537-3 | 1 | 1 | 1 | 2 | 0 | 1 | 1 |
| Acta Materialia · 10.1016_j.actamat.2021.116 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Journal of Advanced Ceramics · s40145-021-0532-8 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Journal of Magnesium and Alloy · j.jma.2020.02.028 | 1 | 0 | 0 | 2 | 1 | 0 | 0 |

Totals: 82 chains, 67 past step 3, 63 past steps 3 and 4, 135 seams, 17 ignored. (34 compositional and 51 seams counted under step 5, not reported as results.)

## Worked example — Nano Letters, nanolett.6b04294

The page the review read. v2.5 showed 4 chains here; v2.6 shows 3 after the covariation drop and the tail collapse — the review's "traces 3 and 4 are the same chain under two generator labels" is the pair that collapsed. Of the 3, 2 clear steps 3 and 4.

| trace | depth | ways in | items | upstream used | scope | necessity | compositional |
|---|---|---|---|---|---|---|---|
| c015 | 2 | 1 | nano_letters_com_o15_o18 → nano_letters_spi_o15_o11 | no | ok | yes (yes/no/yes) | no |
| c038 | 2 | 1 | nano_letters_com_o16_o19 → nano_letters_spi_o16_o13 | yes | ok | no (no/no/no) | no |
| c055 | 2 | 1 | nano_letters_com_o13_o24 → nano_letters_spi_o13_o9 | yes | ok | yes (yes/yes/yes) | yes |

| seam | upstream ignored | scope | counted |
|---|---|---|---|
| nano_letters_com_o13_o24 → nano_letters_spi_o13_o9 | no | supports | yes |
| nano_letters_com_o15_o18 → nano_letters_spi_o15_o11 | yes | supports | no |
| nano_letters_com_o16_o19 → nano_letters_spi_o16_o13 | no | supports | no |

The seam the review named, the one that dropped the XANES result and still reported "every limit survives":

- `nano_letters_com_o15_o18__nano_letters_spi_o15_o11` — flagged by: prose: never-invoked
  > the XANES-dependent metallic-Co-state claim is not invoked here at all.

## One contamination, found and removed

A relay flagged that some arm replies carried text that was not part of the answer. Two kinds, both checked directly rather than taken on the relay's word: a trailing output-framing fragment (`</message>`, `</invoke>`) on 27 replies, and a leading note on 21 replies where the answerer had seen this session's MCP server instruction block in its tool list, correctly judged it was not from the user, ignored it and said so. Neither changed what the answer said.

But both landed asymmetrically — in one arm of a pair and not the other, 25 and 21 pairs respectively — and the comparer is asked whether the two answers differ. So the artifacts were stripped (`clean.py`, leaving the raw replies untouched) and every comparison whose prompt changed was re-run: 39 of 246.

**7 of those 39 flipped, every one of them from "no" to "yes".** The contamination was suppressing the finding that the upstream result mattered. All numbers in this document are from the cleaned re-run.

Two comparison replies quoted the answers inside their `why` field without escaping the quotes and so would not parse as JSON. Their verdict token was unambiguous in the raw text and was read from it; 2 rulings were salvaged this way and are counted here.

## What the calls cost

| stage | model calls | relays | wall minutes | seconds per call |
|---|---|---|---|---|
| scope | 135 | 5 | 8.3 | 3.68 |
| necessity_arms | 492 | 4 | 48.2 | 5.88 |
| necessity_compare | 313 | 6 | 31.3 | 6.01 |

**940 model calls, 87.8 minutes of wall time on 32 papers.** Wall time is measured at a 20-agent concurrency cap, from dispatch to the last harvest, so it includes relay overhead; it is not a per-call cost. Scaling linearly by paper, 99 papers would be about 2908 calls and about 4.5 hours at this cap.

Step 3 costs nothing: it re-reads audits that already exist.

## Stop rules

- repeats agree on fewer than two thirds of chains: 46% agreed, **rule triggered.**
- fewer than 10 chains survive: 34 survive, rule not triggered.

## Where the data is

- `results/v2p6/pruned.json` — steps 1 and 2, with every dropped id
- `results/v2p6/ignored.json` — step 3, the flag and the audit sentence behind it
- `results/v2p6/scope/` — step 4, one prompt and one reply per join
- `results/v2p6/arms/`, `results/v2p6/compare/` — step 5, every arm and comparison
- `results/v2p6/counted.json` — the three gates per seam and per chain, computed for the record; step 5 is present in it but is not reported as a result

- `results/v2p6/pages/` — not built. See "Where this run stopped".

Every verdict is model against model.
