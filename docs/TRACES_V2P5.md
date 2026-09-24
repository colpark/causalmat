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
| items | 29 | **286** |
| depth | 1–4, and 1 for 22 of 29 | **2 by construction; chains to 6** |
| FM lane | 7 (24%) | **167 (58%)** |
| discriminating items | 3 | **33** |

## The three generators do not behave alike

This is the central result. The generator that produces the most material produces the least
trustworthy conclusions from it.

| generator | items | discriminating | not-identifiable | propositions hold | mixed quantities |
|---|---|---|---|---|---|
| **complementary** | 92 | **22 (24%)** | 53% | 12/24 = 50% | 1/25 = 4% |
| **spine_edge** | 175 | **8 (5%)** | 87% | 10/25 = 40% | 3/25 = 12% |
| **covariation** | 19 | **3 (16%)** | 63% | 12/19 = 63% | 7/19 = 37% |

The last two columns are **sampled, not computed over every item**: the key audit ran on 68
packets and the quantity-kind check on 69, both stratified by generator and then by paper.
The first three columns cover all 286 items.

**Complementarity produces the discriminating items.** Pairing two technique families on one claim
gives 24% discriminating against spine_edge's 5%, and the lowest rate of incomparable quantities.

**A spine edge buys an association and a confound, not a discrimination.** 152 of 175 spine-edge
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
in covariation, which fits a generator whose series proxy the drafter can only partly see. Nothing
was unparsed in this audit.

The **key audit's** proposition split is holds 34, overreaches
29, wrong 5 — unlike the join audit
below, it does rule some propositions outright wrong. Its limits split is holds
240, overreaches 11, wrong 9.
One further packet was audited and then invalidated when its key turned out to belong to another
item, leaving 68.

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

**The result survived every correction.** Across 29 convergence judgements at
two levels of independence, **not once did both routes warrant the conclusion alone.**

Both runs predate the figure-level test, and neither describes the 3 claims
that survive it. They are reported because the finding is what held across the corrections, not
because they describe the final set.

| | node-id run | panel run |
|---|---|---|
| claims judged | 23 | 6 |
| route A warrants alone | partly 18, no 5 | partly 6 |
| route B warrants alone | partly 17, no 5, yes 1 | partly 3, no 3 |
| routes agree | partly 22, yes 1 | partly 6 |
| **both alone** | **0** | **0** |

The 3 figure-level claims were never judged: the independence test was
tightened after the panel run, and no further model call was made. So the strongest statement the
data supports is about the 29 judgements above, whose routes are now known to
overlap — **not** about genuinely independent convergence, which remains unmeasured.

In this corpus a claim reached by two routes is usually **one experiment counted twice** — 20 of the
original 24 shared panels outright, and 4 of the 6 survivors shared a figure.

What cannot be said, and an earlier draft of this section did say: that where the routes really are
separate each still supports the conclusion only partly. The three genuinely independent claims were
never judged, so that sentence extrapolated from overlapping routes to independent ones. Genuine
convergence in this corpus is **3 claims, unmeasured**.

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

Also: only **34 of 175 spine-edge items have a MatMech hop** confirming them. Our graph carries
causal structure MatMech never recorded, and the 141 without one are exactly what v5's link
requirement discarded. By relation they are `causes` 145 and `explains` 30; **`produces` yields zero**
— its upstream is a design or process node that is rarely figure-backed.

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
| **total** | **29** | **286** | **19** | **92** | **175** | **49** | **130** | **6** | **3** |

Five papers yield items but no chain: their pairs do not share a claim in the direction a join
needs — both Biomaterials 2010 papers, Advanced Materials 202005449, JMA 2019.01.003 and Rare
Metals s12598-012-0515-6. Eight papers reach depth 3 or more. Only two reach a convergence claim once independence is
tested on figures.

## The join audit: composing a chain launders limits

All 147 joins audited, 146 parsed.

| | single pairs | **joined** |
|---|---|---|
| propositions hold | 50% | **36/146 = 25%** |

Of the 110 that do not hold, **every one overreaches and none is wrong** — a property of the **join**
audit specifically. The per-item key audit above does rule 5 propositions outright wrong, so this is
not a general feature of the drafters: joining does not introduce false statements, it introduces
unwarranted confidence.

| upstream limits, across the handoff | |
|---|---|
| carried | 165/538 = 31% |
| **dropped** | **123/538 = 23%** |
| not applicable | 250/538 = 46% |

**82 of 146 joins — 56% — launder a limit.** The upstream conclusion was true only within its
limits; the downstream item uses it as if those limits did not apply. Every individual statement
stays true while it happens, which is why a per-item audit cannot see it: that audit rules whether
each *stated* limit is true, and each one is. What changes is that the next item stops carrying
them.

**Laundering is flat per join, near 55% at every depth, so it compounds:**

| chains preserving *every* limit | |
|---|---|
| depth 2 | 32/67 = 48% |
| depth 3 | 8/31 = 26% |
| depth 4 | **1/26 = 4%** |
| depth 5 | 0/3 = 0% |
| depth 6 | 0/2 = 0% |
| **all** | **41/129 = 32%** |

Beyond depth 3 the chains essentially stop preserving their qualifications: one chain in 26 at depth
4, none at all at 5 or 6.

The denominators reach 129 of the 130 chains. One chain is missing —
Journal of Magnesium and Alloys, depth 2 — because one of its joins
is the single reply of 147 that did not parse. An earlier version of this table read 128 of 130;
that was a fault in the counting script, which split join filenames on a double underscore while
four item ids contain one, so two chains looked unaudited whose joins had in fact been audited.

### This corrects how I reported depth

Chains reaching depth 6 was the headline I gave for composition, twice, before this audit existed to
contradict it. If each join is roughly an even chance of shedding a caveat, **a deep chain is not a
stronger item, it is a longer one**, carrying a conclusion whose qualifications were dropped a step
at a time. Depth without limit survival is accumulation, not support.

v2.5's gains over v5 stand on coverage (32 of 32 papers against 16), item count (286 against 29) and
discriminating items (33 against 3). **"Chains to depth 6" should not be counted among them.**

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

All 286 keys are drafted. Three of them failed verification across four dispatches and were left
undrafted for a time; they were redrafted once the relay was told the earlier attempts had been
truncated, and went through the same byte-for-byte transcript verification as every other key. One
key, `rare_metals_com_o2_o3`, was dispatched directly rather than through a relay and carries that
on the item as `key_provenance` — it is the only key in the run that did not come through the
relay-and-harvest path.


## Corrections, 2026-09-24

Every number above was recomputed from the committed data by `trace_kit_v2p5/doc_numbers.py`, which
runs no model call and writes nothing. Verdict spellings are normalised before counting. The
corrections:

| what | was | now | cause |
|---|---|---|---|
| keys undrafted | "three of 286 never produced a verifying reply" | all 286 drafted | stale: written before the final three were redrafted |
| per-paper total items | 283 | 286 | same |
| per-paper generator totals | 19 / 90 / 174 | 19 / 92 / 175 | same |
| generator table, complementary | 89 items, 23 discriminating | 92 items, 22 discriminating | stale count from before the final drafts |
| generator table, spine_edge | 174 items, 7 discriminating | 175 items, 8 discriminating | same |
| spine-edge not-identifiable | 151 of 174 | 152 of 175 | same |
| papers with items but no chain | four | five, named | miscount |
| chain-survival denominators | 128 of 130 chains, depth 2 = 32/66 | 129 of 130, depth 2 = 32/67 | counting-script fault: join filenames split on a double underscore, which four item ids contain |
| key-audit limits | 240/260, unparsed unstated | 240/260, 0 unparsed, split stated | wording |
| "none is wrong" | unscoped | scoped to the join audit; key audit's 5 wrong reported | wording: the sentence was true of one audit and read as true of both |
| generator table, last two columns | denominators unstated | marked as sampled, 68 and 69 packets | wording: sampled columns read as whole-set properties |
| convergence prose | described the 6-claim panel run beside the 3-claim count | both runs tabulated and labelled; the 3 figure-level claims stated as never judged | internal inconsistency: results of a superseded set presented alongside the corrected count |
| spine-edge MatMech hops | 36 of 185 pairs, 149 without, causes 151 / explains 34 | 34 of 175 items, 141 without, causes 145 / explains 30 | stale: counted pairs before the ten self-pairs were removed, not items |
| convergence conclusion | "where the routes really are separate, each supports the conclusion only partly" | withdrawn; genuine convergence is 3 claims, unmeasured | the claim extrapolated from overlapping routes to independent ones that were never judged |

Unchanged and confirmed correct: 286 items, 32 of 32 papers, 167 FM-lane, 33 discriminating, 147
joins, 24 rejected all splits, 130 chains at 68/31/26/3/2, join audit 36/146 holding and 82/146
laundering, 3 convergence claims, key-audit limits 240/260, and the v5 side of the comparison at 29
items over 16 papers with 3 discriminating and 7 FM-lane.
