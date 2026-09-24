# Traces v3: MatMech's causal hops, stitched to our panel observations

A v2 trace asked whether a set of panels supports one claim, one step per evidence node. v3 asks a
different question. MatMech records a paper's argument as **causal hops** — cause, effect, stage
type, the figures behind it. A v3 trace makes the **hop the step**, and the grading question is
whether the evidence warrants that step.

**Every verdict is model against model.** Nothing here is checked against a human key.

MatMech's cause and effect spans are used to match and to chain, and never enter a prompt. They
stay in `_matmech_span_DO_NOT_PROMPT`. A leak check over all 44 prompts finds zero occurrences.

## What came through

| paper | hops | matched | attachable | chained |
|---|---|---|---|---|
| Acta Materialia | 3 | 3 | 3 | 3 |
| Rare Metals | 2 | 2 | 2 | 2 |
| Advanced Functional Materials | 4 | 4 | 2 | 2 |
| Biomaterials | 4 | 4 | 4 | 4 |
| Nano Letters | 3 | 3 | 3 | 2 |
| **total** | **16** | **16** | **14** | **13** |

The gap between **matched** and **attachable** is the finding and is not folded into one number.
*Matched* means the matcher found a claim of ours stating the hop's fact. *Attachable* means at
least one of those claims is supported — an observation node with panels pointing at it through a
direct `evidences` edge, one step, no paths through intermediate claims. A hop that is matched but
not attachable landed on something the paper asserts in text rather than shows in a figure, and can
carry no trace however good the match.

Two hops are matched but not attachable: adfm M3 and M4, both landing on the thesis pair n2/n19.
One further hop is attachable but not chained: Nano Letters M3, dropped for the reason below.

Support is never read off a claim node's `image_support` field. Three of the five graphs barely set
it — Acta Materialia 0 of 30 claims, Rare Metals 0 of 19, Biomaterials 1 of 31 — while storing the
evidence on observation nodes. Reading the field measures where a graph keeps support, not whether
the paper shows the thing; it would have scored Acta and Rare Metals at zero attachable. `support.py`
is the single place support is derived, and moving to it took attachable from 7/16 to 13/16 before
any other change.

## Validation of the matcher

**4 of 5 clean positives pass.** Six known-positive rows exist, of which one is contaminated: Nano
Letters M1 is the mesopores case, written verbatim into `net-decompose`'s own rules, so its pass is
partly a training case and is excluded from the count. The two Rare Metals rows also pass.

**Nano Letters M3 is a logged structural miss, not a fix.** The row wants n17, "Co3O4 is far less
Na-active than Li-active (~36% vs ~91%)", the hop's fact measured by XAFS. The matcher reaches it
about a third of the time: six runs of the byte-identical prompt returned it twice. Graph completion
cannot rescue it either — n17's only claim-neighbours are n9, n18 and n21, so it sits **two** edges
from the matched set, a sibling of n20 through n18 rather than a neighbour. A two-edge step would
readmit the must-not risks that the unshipped first version of completion produced, so there is no
two-edge step.

The test was corrected twice, both times **before** being frozen, and both corrections are recorded
with reasons in `results/v3/decompose_findings.md`:

1. Two rows were unsatisfiable. `KNOWN` had been every claim our graph reads from the figures a hop
   cites — a figure-level set used as a fact-level expectation. adfm M4 demanded n21, *atmospheric
   ageing*, for a hop about domain size; Biomaterials M4 offered n24, "ALP activity does not
   differ", as proof of "improved osteogenesis", which cuts against it. Both became `must_not`.
2. adfm M3 is underdetermined by its effect text. Widening the row was refused; the ambiguity became
   the attachment-reach measure instead.

From the freeze, rows and pass conditions do not change. Disagreements are logged and still fail.

## Lexical against model

The matcher of record is `net-decompose` plus `complete.py`'s one-edge replace step. The old TF-IDF
matcher is kept beside it, never overwritten.

| paper | hop | lexical sub-claims | model (matcher of record) |
|---|---|---|---|
| Acta Materialia | M1 | n8, n15, n4, n2 | n2, n8, n9 |
| Acta Materialia | M2 | n4, n12, n2, n17, n10 | n2, n12 |
| Acta Materialia | M3 | n18, n19, n11 | n18 |
| Rare Metals | M1 | s6, h1, s1, s2, m3 | h1, s1, s2, s5, s6 |
| Rare Metals | M2 | s6, s5, p3, c1 | s6, c1 |
| Advanced Functional Materials | M1 | n7, n13, n4 | n4, n7 |
| Advanced Functional Materials | M2 | n13, n9, n21 | n13 |
| Advanced Functional Materials | M3 | — | n2, n19 |
| Advanced Functional Materials | M4 | n2 | n2, n19 |
| Biomaterials | M1 | n8, n3, n9 | n8, n9 |
| Biomaterials | M2 | n13, n12, n17 | n13, n12, n11, n2 |
| Biomaterials | M3 | n17, n12 | n11, n12, n15, n16, n17 |
| Biomaterials | M4 | — | n12, n13, n16, n17 |
| Nano Letters | M1 | n2, n22 | n2, n5 |
| Nano Letters | M2 | — | n7, n8, n20 |
| Nano Letters | M3 | — | n1, n7, n8, n20 |

38 lexical, 44 model, 22 shared. The lexical matcher returned **nothing** for four hops, three of
them Nano Letters, and the model found claims for every one. Where they disagree most is Nano
Letters, whose effect spans are comparative ("superior lithium storage compared to sodium") and
share almost no vocabulary with claims written as capacities in mAh/g.

## The six hops step 3a called coverage gaps

Step 3a found the coverage-gap label untrustworthy: all six hops the lexical matcher left unattached
cite figures our graph already reads, so they were relabelled `matcher_miss` and the patch run was
correctly not performed. Step 3b re-asks with the matcher of record:

| verdict | count | which |
|---|---|---|
| resolved | 4 | Biomaterials M4, Nano Letters M1, M2, M3 |
| missing_edge | 2 | adfm M3, adfm M4 |
| unrelated | 0 | — |

Nothing here was ever a coverage gap. The two `missing_edge` hops are the adfm pair: our graph does
read F2 and F6, but joins those panels to the specific claims (n9, n17, n21) rather than to the
thesis pair n2/n19 that the hop lands on. The fact and the panels are both in our graph; the edge
between them is not.

## The Biomaterials pairs

Biomaterials is the one paper whose hops do not form a line. Its four hops link M1→M3, M2→M4 and
M3→M4, so **two routes arrive at the same performance hop**:

- M2 (Processing → Properties) → M4, the direct route: Co²⁺ incorporation to VEGF/HIF-1α response.
- M1 (Processing → Structure) → M3 (Structure → Properties) → M4, the route through the mesoporous
  structure and the release it controls.

That is a fork, not a chain, and it is why Biomaterials yields two traces rather than one. It also
makes the paper the natural place to ask whether the two routes are independently warranted, since
they share only their endpoint.

## Nano Letters: the third hop is a restatement

M3 is dropped from the chain as not independently supported. Its effect, "inferior sodium storage
performance compared to lithium storage", is M2's effect inverted, and the claims it lands on (n7,
n8) are evidenced by **F2 panels only — the identical set as M2** — so it adds no evidence. M3 cites
F6, where the XAFS claim n17 lives, but the matcher never reaches n17, so M3 borrows M2's evidence
entirely. Structurally it is a Processing → Performance shortcut spanning M1's cause to M2's effect,
not a third step. The chain is M1 → M2.

The original scope-limit wording is not in the repo; this is my reading of it, stated as such.

## The traces

| trace | paper | chain | steps | panels |
|---|---|---|---|---|
| acta_materia_M1_M2_M3 | Acta Materialia | M1→M2→M3 | 3 | 10 |
| rare_metals_M1_M2 | Rare Metals | M1→M2 | 2 | 15 |
| advanced_fun_M1_M2 | Advanced Functional Materials | M1→M2 | 2 | 2 |
| biomaterials_M1_M3_M4 | Biomaterials | M1→M3→M4 | 3 | 12 |
| biomaterials_M2_M4 | Biomaterials | M2→M4 | 2 | 4 |
| nano_letters_M1_M2 | Nano Letters | M1→M2 | 2 | 7 |

All 50 panels resolve and are handed over whole and unaltered. No one-hop traces: a single hop has
no step to warrant. Biomaterials and Nano Letters qualify only because the graph check confirmed
their links, which were `stage_only` before.

## The headline: reordered scores exactly like full

The `reordered` arm gets the full evidence, but the steps are out of the paper's order and the link
sentences ("linked to the previous step by: shared spine claim n5") are removed. If the chain's
sequence carries information, this arm should lose some of it.

It does not. **`reordered` scores +0.00 against `full`**, with identical per-step rulings on 13 of
14 steps. The one chain that moves is Nano Letters, where the two rulings simply swap places with
the reversal — which is the reversal, not a loss.

**Said plainly: the sequence carries nothing, and on this evidence v3 adds no information over v2.**
Presenting a paper's argument as an ordered chain of causal hops, rather than as a bag of
claim-and-evidence pairs, did not change a single ruling that v2 could not already have produced.

There is a limitation that has to be stated beside that conclusion rather than after it. The `full`
arm says "warrants" on 13 of 14 steps — **93%, a near-constant scale**. With almost every step
ruled the same way, there is very little room for any arm to differ from `full`, so the reordered
result rests on a ceiling rather than standing free of it. The only arm that moves substantially is
the one deliberately given the wrong pictures. A fair reading is: the sequence carries nothing *that
this grading question can detect*, and this grading question detects very little.

## Per-hop scores, all four arms and the control

| trace | step | hop | full | floor | oracle_complete | reordered | permute_image |
|---|---|---|---|---|---|---|---|
| acta_materia_M1_M2_M3 | 1 | M1 | warrants | warrants | warrants | warrants | does not address |
| acta_materia_M1_M2_M3 | 2 | M2 | warrants | warrants | warrants | warrants | warrants |
| acta_materia_M1_M2_M3 | 3 | M3 | warrants | warrants | warrants | warrants | warrants |
| advanced_fun_M1_M2 | 1 | M1 | warrants | does not address | warrants | warrants | does not address |
| advanced_fun_M1_M2 | 2 | M2 | warrants | warrants | warrants | warrants | does not address |
| biomaterials_M1_M3_M4 | 1 | M1 | warrants | warrants | warrants | warrants | does not address |
| biomaterials_M1_M3_M4 | 2 | M3 | warrants | warrants | warrants | warrants | does not address |
| biomaterials_M1_M3_M4 | 3 | M4 | warrants | warrants | warrants | warrants | does not address |
| biomaterials_M2_M4 | 1 | M2 | warrants | warrants | warrants | warrants | does not address |
| biomaterials_M2_M4 | 2 | M4 | warrants | does not address | warrants | warrants | does not address |
| nano_letters_M1_M2 | 1 | M1 | warrants | warrants | warrants | **contradicts** | warrants |
| nano_letters_M1_M2 | 2 | M2 | **contradicts** | warrants | **contradicts** | warrants | contradicts |
| rare_metals_M1_M2 | 1 | M1 | warrants | warrants | warrants | warrants | does not address |
| rare_metals_M1_M2 | 2 | M2 | warrants | warrants | warrants | warrants | does not address |

Majority-class baseline, the share of each arm's rulings taking its single most common level. An arm
that says one thing everywhere scores 100% here and carries no signal:

| arm | majority class | baseline | mean delta vs full |
|---|---|---|---|
| full | warrants | 13/14 = **93%** | — |
| floor | warrants | 12/14 = 86% | −0.08 |
| oracle_complete | warrants | 13/14 = **93%** | +0.00 |
| reordered | warrants | 13/14 = **93%** | +0.00 |
| permute_image | does not address | 10/14 = 71% | **−1.44** |

Three readings follow. `oracle_complete` ties `full`, so the measurement written out in words does
everything the picture does — the same result v2 reached on these five papers, where its oracle stop
rule fired on all five cases. `floor` is within a rounding error of `full`, so the captions alone
carry nearly the whole ruling. And `permute_image` is clearly separated, so the arms can tell wrong
pictures from right ones; the scale is not broken, it is simply not being exercised.

Nano Letters is the only trace where `full` rules anything other than "warrants": step 2 comes back
`contradicts`. That is the Li-versus-Na comparison, the chain whose third hop we dropped as a
restatement, and it is the one place in the set where an arm disagrees with the paper.

## The Biomaterials fork

The two routes into M4 were judged independently, and they do not agree:

| route | chain | full closing |
|---|---|---|
| through the structure | M1 → M3 → M4 | **warrants** |
| direct from processing | M2 → M4 | **partly warrants** |

The longer route, which goes through the mesoporous structure and the release it controls, is
judged warranted. The direct processing-to-properties route is only partly warranted. Both reach
the same performance hop, so the paper's conclusion is better supported through its structural
argument than through the shortcut — which is an argument for keeping the fork rather than
collapsing it to one path.

## v3 against v2, same five papers

| paper | v2 case | v2 steps | v3 traces | v3 steps |
|---|---|---|---|---|
| Acta Materialia | case5_drop | 5 | 1 | 3 |
| Advanced Functional Materials | case3_contradicts | 4 | 1 | 2 |
| Biomaterials | case2_annotated | 4 | 2 | 5 |
| Nano Letters | case4_oracle | 5 | 1 | 2 |
| Rare Metals | case1_three_techniques | 3 | 1 | 2 |
| **total** | **5** | **21** | **6** | **14** |

The two designs do not share a scale and this does not pretend they do. v2 graded each step against
an expected support level taken from the graph, so it could report "steps correct"; v3 has no key,
because "does this evidence warrant this step?" has no stored answer, so its arms are compared with
each other and with the majority-class baseline.

| | v2 | v3 |
|---|---|---|
| a step is | one evidence node under one claim | one MatMech causal hop |
| the step asks | is that observation visible? | does the evidence warrant this move? |
| steps | 21 over 5 cases | 14 over 6 traces |
| key | expected support from the graph | none |
| full arm | 14/21 steps correct | 93% one class |
| text beats or ties picture | oracle 15/21 vs full 14/21, stop rule fired 5 of 5 | oracle +0.00 |
| control separates | permute_image 0/7, unparsed on 3 of 5 | permute_image −1.44, parsed 6 of 6 |

Two things v3 does better. Its control actually runs: v2's `permute_image` failed to parse on three
of five cases and graded 0/7 where it did, so it never functioned as a control, while v3's parses
everywhere and separates cleanly. And v3 uses more of each paper's argument — 16 hops with 14
attachable, against v2's five hand-picked claims.

One thing v2 did better, and it matters: v2 had a key, however weak. That key was degenerate —
every one of the five expected closings was "partial" — but it at least let an arm be *wrong*. v3's
arms can only be compared with each other, and when they nearly all say "warrants", that comparison
has little to say.

The conclusion for the design, stated without hedging: **the causal-hop framing did not buy
information.** The sequence is not doing work, the pictures are not doing work over the text, and
the grading question is too easily satisfied to separate the arms. v3's contribution is structural
rather than evaluative — it shows where a paper's argument actually forks (Biomaterials), which of
its hops restate rather than advance (Nano Letters M3), and which land on claims with no figure
behind them (adfm M3, M4).
