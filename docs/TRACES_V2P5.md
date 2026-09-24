# Traces v2.5: pairwise items from the graph

Generation and audit only. **Every verdict is model against model.**

v5 took its unit from MatMech's causal hops and required a confirmed link between two of them. That
cost 16 of 32 papers — their hops attached to evidence and then nothing joined them. v2.5 takes the
unit from **our own graph**: a pair of observations the graph already links, asked so that neither
observation answers the question alone. Depth 2 by construction.

## Yield, against v5 on the same 32 papers

| | v5 | **v2.5** |
|---|---|---|
| papers yielding items | 16 / 32 | **32 / 32** |
| items | 29 | **283** |
| depth | 1–4, and 1 for 22 of 29 | **2 by construction; chains to 6** |
| FM lane | 7 (24%) | **167 (58%)** |
| discriminating items | 3 | **31** |

## The three generators do not behave alike

This is the central result. The generator that produces the most material produces the least
trustworthy conclusions from it.

| generator | items | discriminating | not-identifiable | propositions hold | mixed quantities |
|---|---|---|---|---|---|
| **complementary** | 89 | **23 (26%)** | 53% | 12/24 = 50% | **4%** |
| **spine_edge** | 174 | 7 (4%) | **87%** | 10/25 = **40%** | 12% |
| **covariation** | 19 | 3 | 63% | 12/19 = **63%** | **37%** |

**Complementarity produces the discriminating items.** Pairing two technique families on one claim
gives 26% discriminating against spine_edge's 4%, and the lowest rate of incomparable quantities.

**A spine edge buys an association and a confound, not a discrimination.** 151 of 174 spine-edge
keys name something as not identifiable — 87%. A `causes` or `explains` edge between two
figure-backed claims almost always comes with a candidate the pair cannot separate. That is an
honest result about how much a causal edge can carry on its own.

**Covariation is the weakest generator and should be rebuilt or dropped.** Two independent lines of
evidence against it: it yields only 19 items, and 37% of its propositions set quantities of
different kinds against each other. The cause is in its construction — there is no
`panel_conditions` field in these graphs, so a sample series is detected from the observation text
(three or more numbers in one sweep) and two series pair when they are the **same length**. Series
length is not comparability, so it will pair a voltage against a current, or a normalized
percentage against an absolute mass.

## The key audit

68 valid packets, stratified by generator and then by paper.

| | v5 | **v2.5** |
|---|---|---|
| propositions hold | 9/23 = 39% | **34/68 = 50%** |
| limits hold | 86/89 = 97% | 240/260 = 92% |

Propositions hold better here than in v5; limits slightly worse, and the 9 wrong limits sit mostly
in covariation, which fits a generator whose series proxy the drafter can only partly see.

The v5 pattern holds across both runs and 91 audited keys: **drafters write reliable caveats and
overstated conclusions.**

## Quantity kinds

11 mixed of 69 = 16%, against v5b's raw 54%. The prompt now names the distinction that checker kept
getting wrong — a proposition that *relates* two different quantities, which is what a covariation
is for, against two quantities *set against each other as if the same kind*.

| | mixed | genuine | borderline | category errors |
|---|---|---|---|---|
| v5b | 14 | 7 | 2 | **5** |
| **v2.5** | **11** | 7 | 4 | **0** |

Every ruling is recorded on its item and none is applied to a key, because in v5b auto-applying
this checker overwrote two hand-calibrated keys.

## Convergence: a claim reached twice is not a claim supported twice

The independence test failed three times, and an auditor caught each one before I did.

| independence tested on | convergence claims |
|---|---|
| disjoint **node ids** | 24 |
| disjoint **panels** | 6 |
| disjoint **figures** | **3** |

A judge first wrote that the routes *"share the same core charge-transfer figures rather than being
fully disjoint measurements"* — 20 of 24 shared panels outright. After that fix, another wrote that
the routes *"draw on the same underlying experiment and same five surfaces"* — 4 of the 6 survivors
used different panels of one figure.

**The result survived every correction.** Across 29 convergence judgements at two levels of
independence, **not once did both routes warrant the conclusion alone.** In the corrected run: route
A partly warrants in all 6, route B partly in 3 and outright no in 3, all 6 agree only partly,
combined strength associative in 5.

In this corpus a claim reached by two routes is usually **one experiment counted twice**, and where
the routes really are separate, each supports the conclusion only partly.

## Structure

147 joins kept, 24 rejected — **all splits, not one loop.** Over `causes` and `explains` between
figure-backed claims these graphs are acyclic.

| depth | chains |
|---|---|
| 2 | 68 |
| 3 | 31 |
| 4 | 26 |
| 5 | 3 |
| 6 | 2 |

Also: only **36 of 185 spine-edge pairs have a MatMech hop** confirming them. Our graph carries
causal structure MatMech never recorded, and the 149 without one are exactly what v5's link
requirement discarded. `produces` yields zero pairs — its upstream is a design or process node that
is rarely figure-backed.

## Per paper

Paper names are truncated; several journals contribute more than one paper.

| paper | v5 items | v2.5 items | cov | comp | edge | attached | chains | max depth | conv |
|---|---|---|---|---|---|---|---|---|---|
| Bioactive Materials | 0 | 5 | 1 | 2 | 2 | 0 | 2 | 2 | 0 |
| Bioactive Materials | 2 | 26 | 5 | 6 | 15 | 16 | 18 | 4 | 0 |
| Biomaterials | 0 | 5 | 0 | 3 | 2 | 0 | 0 | - | 0 |
| Biomaterials | 0 | 2 | 0 | 1 | 1 | 0 | 0 | - | 0 |
| Journal of Magnesium and Alloys | 0 | 5 | 0 | 2 | 3 | 0 | 2 | 2 | 0 |
| Journal of Magnesium and Alloys | 0 | 14 | 1 | 6 | 7 | 0 | 8 | 2 | 0 |
| Journal of Materials Science & Tec | 0 | 9 | 0 | 2 | 7 | 0 | 2 | 6 | 0 |
| Advanced Energy Materials | 1 | 13 | 0 | 5 | 8 | 1 | 4 | 3 | 0 |
| Advanced Energy Materials | 0 | 3 | 0 | 2 | 1 | 0 | 1 | 2 | 0 |
| Bioactive Materials | 2 | 13 | 1 | 6 | 6 | 1 | 4 | 3 | 0 |
| Journal of Advanced Ceramics | 0 | 5 | 0 | 1 | 4 | 0 | 2 | 2 | 0 |
| Journal of Advanced Ceramics | 0 | 10 | 0 | 1 | 9 | 0 | 5 | 4 | 0 |
| Journal of Materials Science & Tec | 1 | 7 | 0 | 3 | 4 | 2 | 3 | 3 | 0 |
| Materials Characterization | 0 | 10 | 0 | 7 | 3 | 0 | 3 | 2 | 0 |
| Nano Letters | 0 | 7 | 0 | 1 | 6 | 0 | 5 | 2 | 0 |
| Progress in Organic Coatings | 1 | 4 | 1 | 0 | 3 | 0 | 1 | 2 | 0 |
| Advanced Composites and Hybrid Mat | 0 | 13 | 1 | 3 | 9 | 0 | 7 | 4 | 0 |
| Advanced Energy Materials | 1 | 12 | 1 | 7 | 4 | 3 | 4 | 3 | 0 |
| Advanced Energy Materials | 4 | 9 | 0 | 3 | 6 | 4 | 6 | 4 | 0 |
| Advanced Energy Materials | 0 | 8 | 0 | 2 | 6 | 0 | 2 | 3 | 0 |
| Advanced Functional Materials | 0 | 16 | 1 | 6 | 9 | 0 | 14 | 4 | 0 |
| Advanced Materials | 0 | 1 | 0 | 0 | 1 | 0 | 0 | - | 0 |
| Journal of Advanced Ceramics | 0 | 4 | 0 | 0 | 4 | 0 | 1 | 2 | 0 |
| Journal of Advanced Ceramics | 3 | 10 | 0 | 1 | 9 | 0 | 2 | 2 | 0 |
| Journal of Magnesium and Alloys | 1 | 7 | 0 | 1 | 6 | 4 | 4 | 2 | 2 |
| Journal of Magnesium and Alloys | 2 | 6 | 1 | 2 | 3 | 1 | 0 | - | 0 |
| Journal of Magnesium and Alloys | 1 | 16 | 1 | 0 | 15 | 4 | 16 | 5 | 0 |
| Biomaterials | 5 | 13 | 1 | 3 | 9 | 6 | 8 | 3 | 0 |
| Advanced Functional Materials | 1 | 7 | 0 | 2 | 5 | 1 | 1 | 2 | 0 |
| Acta Materialia | 2 | 12 | 2 | 7 | 3 | 3 | 1 | 2 | 1 |
| Nano Letters | 1 | 10 | 2 | 4 | 4 | 3 | 4 | 2 | 0 |
| Rare Metals | 1 | 1 | 0 | 1 | 0 | 0 | 0 | - | 0 |
| **total** | **29** | **283** | **19** | **90** | **174** | **49** | **130** | **6** | **3** |

Four papers yield items but no chain: their pairs do not share a claim in the direction a join
needs. Eight papers reach depth 3 or more. Only two reach a convergence claim once independence is
tested on figures.

## What went wrong in the build, and what caught it

Four defects, **none found by the checks I had written**:

1. **A relay reported 74 dispatches it never made.** Transcript verification found 7 dispatches and
   0 ok. A relay's self-report is never the record.
2. **The `net-writer` definition's own output schema won ~30% of drafts.** The same hazard was
   checked and clear in v5 (0 of 59); at v2.5's prompt length it wins three times in ten. Forbidding
   it explicitly fixed it: 53 of 53 after the change.
3. **Eleven keys were attached to the wrong items** — a magnesium grain-size item carried a
   photocatalysis key. Correcting colliding ids had not removed the reply files the collision
   already wrote. **A subagent reading its own input flagged it.** Byte-for-byte prompt verification
   catches a relay that never dispatched; it cannot catch a correct reply filed against the wrong
   question.
4. **The convergence independence test was too weak, three times over.**

The check I then added to catch (3) had a false positive of its own: it excluded numbers from the
vocabulary comparison, so a key agreeing with its observations entirely through quoted measurements
— 130.3 to 81.9 kJ/mol, 150 min to 11 min — scored near zero and was quarantined. For an item built
on two measurements that is the common case.

Three keys of 286 never produced a verifying reply after four dispatches and are recorded as
undrafted rather than filled in. One key, `rare_metals_com_o2_o3`, was dispatched directly rather
than through a relay and carries that on the item.
