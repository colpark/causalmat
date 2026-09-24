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

## A scoring bug that corrupted the first reading of these results

The level matcher tested `warrants` before `partly warrants`. Since "warrants" is a substring of
"partly warrants" — and "warranted" of "partly warranted" — **every partial ruling was scored as a
full one**. The arms looked far more confident than they were, and one reported finding (a
difference between the two Biomaterials routes) was an artefact of it and does not survive. The
matcher now tests most-specific-first, `does not address` and `contradicts` and `partly` before any
bare warrant test, and the numbers below are from the corrected pass over the same verified replies.

All 30 arm replies and 14 removal replies were verified byte-for-byte against their prompt files
from the agents' own transcripts, so the replies themselves were never in question; only the
scoring of them was.

## The headline: reordered scores exactly like full

The `reordered` arm gets the full evidence, but the steps are out of the paper's order and the link
sentences ("linked to the previous step by: shared spine claim n5") are removed. If the chain's
sequence carries information, this arm should lose some of it.

It does not. **`reordered` scores +0.00 against `full`**, with identical per-step rulings on 12 of
14 steps. The only chain where they differ is Nano Letters, and there the two rulings swap with the
reversal rather than degrade. This result survived the scoring fix unchanged, which is the one
reassurance available: it is not an artefact of the bug above.

**Said plainly: the sequence carries nothing, and on this evidence v3 adds no information over v2.**
Presenting a paper's argument as an ordered chain of causal hops, rather than as a bag of
claim-and-evidence pairs, did not change a single ruling that v2 could not already have produced.

The limitation belongs beside that conclusion, not after it. `full` rules "partly warrants" on 12
of 14 steps — **86%, a near-constant scale**. With almost every step ruled the same way there is
little room for any arm to differ, so the reordered result rests on a ceiling rather than standing
free of it. A fair reading: the sequence carries nothing *that this grading question can detect*,
and this grading question detects very little.

## Per-hop scores, all four arms and the control

| trace | step | hop | full | floor | oracle_complete | reordered | permute_image |
|---|---|---|---|---|---|---|---|
| acta_materia_M1_M2_M3 | 1 | M1 | partly | partly | partly | partly | does not address |
| acta_materia_M1_M2_M3 | 2 | M2 | partly | partly | partly | partly | partly |
| acta_materia_M1_M2_M3 | 3 | M3 | partly | partly | partly | partly | partly |
| advanced_fun_M1_M2 | 1 | M1 | partly | does not address | **warrants** | **warrants** | does not address |
| advanced_fun_M1_M2 | 2 | M2 | partly | partly | partly | partly | does not address |
| biomaterials_M1_M3_M4 | 1 | M1 | partly | **warrants** | partly | partly | does not address |
| biomaterials_M1_M3_M4 | 2 | M3 | partly | partly | **warrants** | partly | does not address |
| biomaterials_M1_M3_M4 | 3 | M4 | partly | partly | partly | partly | does not address |
| biomaterials_M2_M4 | 1 | M2 | partly | partly | partly | partly | does not address |
| biomaterials_M2_M4 | 2 | M4 | partly | does not address | partly | partly | does not address |
| nano_letters_M1_M2 | 1 | M1 | **warrants** | partly | **warrants** | **contradicts** | warrants |
| nano_letters_M1_M2 | 2 | M2 | **contradicts** | partly | **contradicts** | partly | contradicts |
| rare_metals_M1_M2 | 1 | M1 | partly | partly | **warrants** | partly | does not address |
| rare_metals_M1_M2 | 2 | M2 | partly | partly | partly | partly | does not address |

Majority-class baseline, the share of each arm's rulings taking its single most common level. An arm
that says one thing everywhere scores 100% here and carries no signal:

| arm | majority class | baseline | mean delta vs full |
|---|---|---|---|
| full | partly warrants | 12/14 = **86%** | — |
| floor | partly warrants | 11/14 = 79% | −0.03 |
| oracle_complete | partly warrants | 9/14 = 64% | **+0.22** |
| reordered | partly warrants | 12/14 = **86%** | +0.00 |
| permute_image | does not address | 10/14 = 71% | −0.72 |

`oracle_complete` does not merely tie `full` — it scores **higher**, +0.22, and is the least
constant arm at 64%. Handing the measurement over in words produces more confident rulings than
handing over the picture it came from. v2 reached the same conclusion on these same five papers,
where its oracle stop rule fired on all five cases; v3 reproduces it and strengthens it. `floor`,
captions with no images and no measurements, is within a rounding error of `full` at −0.03.

`permute_image` is the only arm that clearly separates, at −0.72 and ruling "does not address" on 10
of 14 steps. The scale can detect wrong pictures. It is not detecting anything else.

Nano Letters is the only trace where `full` departs from "partly warrants" at all, ruling step 1
`warrants` and step 2 `contradicts` — the Li-versus-Na comparison whose third hop we dropped as a
restatement. It is the one place in the set where an arm disagrees with the paper.

## Hop-level necessity

Evidence is withheld from one step, the step's own text is kept so the model knows what the paper
concluded there, and the chain is judged again. Necessary means the closing comes back **strictly
weaker**.

| trace | step | hop | technique | panels | full | without | necessary |
|---|---|---|---|---|---|---|---|
| acta_materia_M1_M2_M3 | 1 | M1 | TEM | 5 | partly | partly | no |
| acta_materia_M1_M2_M3 | 2 | M2 | MECH:compression | 3 | partly | partly | no |
| acta_materia_M1_M2_M3 | 3 | M3 | MECH:tensile | 2 | partly | partly | no |
| advanced_fun_M1_M2 | 1 | M1 | SEM | 1 | partly | partly | no |
| advanced_fun_M1_M2 | 2 | M2 | PL | 1 | partly | partly | no |
| biomaterials_M1_M3_M4 | 1 | M1 | XRD:small_angle | **6** | partly | partly | no *(size-limited)* |
| biomaterials_M1_M3_M4 | 2 | M3 | CHEM:ion_concentration | 4 | partly | partly | no |
| biomaterials_M1_M3_M4 | 3 | M4 | BIO:western_blot | 2 | partly | partly | no |
| biomaterials_M2_M4 | 1 | M2 | CHEM:ion_concentration | 2 | partly | partly | no |
| biomaterials_M2_M4 | 2 | M4 | BIO:western_blot | 2 | partly | partly | no |
| nano_letters_M1_M2 | 1 | M1 | PHYS:N2_sorption | 3 | does not address | does not address | no |
| nano_letters_M1_M2 | 2 | M2 | ECHEM:GCD | 4 | does not address | **partly (stronger)** | no |
| rare_metals_M1_M2 | 1 | M1 | SEM | **12** | partly | partly | no *(size-limited)* |
| rare_metals_M1_M2 | 2 | M2 | TEM | 3 | partly | *no answer* | — |

**Not one hop's evidence is necessary.** Thirteen of fourteen removals were answered, and every one
of them left the chain's closing exactly where it was. The chain reads "partly warrants" with the
evidence and "partly warrants" without it.

Two rows carry more than five panels and their results are **size-limited rather than
content-based**: Rare Metals M1 hands over 12 SEM panels and Biomaterials M1 hands over 6
small-angle XRD panels. Withholding that much at once is not a clean test of what those panels
contribute; it changes how much the model is asked to hold at all. Rare Metals is the known case and
behaves as expected.

One removal is **non-monotonic**: Nano Letters M2 comes back *stronger* without its evidence, "does
not address" rising to "partly warrants". That is the mechanism the design cannot escape — the step
text still asserts what the paper concluded, so withholding the evidence leaves an unchallenged
assertion, and the ECHEM data is the thing that was generating the doubt. v2 recorded and struck a
non-monotonicity finding for the same reason; v3 reproduces it once in fourteen.

One job produced **no answer at all**: Rare Metals M2. The agent wrote that it would disregard
"MCP Server Instructions" and "Auto Mode" text that had appeared in its tool output stream, said it
still needed to view the remaining TEM images, and stopped. Environment text leaked into a
subagent's stream and derailed it. That row is a failed job and is not evidence of anything.

Taken together, necessity by removal does not work in this design. The closing is immovable, the one
row that does move goes the wrong way, and two of the rows that could have moved are too large to
read.

## The Biomaterials fork

Biomaterials' two routes into M4 were judged independently:

| route | chain | full closing |
|---|---|---|
| through the structure | M1 → M3 → M4 | partly warrants |
| direct from processing | M2 → M4 | partly warrants |

**They agree, and both are partial.** An earlier pass reported the structural route as fully
warranted and the direct route as only partly so; that difference was produced by the substring bug
above and does not survive. On the corrected scoring the fork is not doing evaluative work either —
the two routes are indistinguishable. What the fork still shows is structural: the paper's argument
genuinely branches, and M4 is reached twice by evidence that shares no intermediate step.

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
| full arm | 14/21 steps correct | 86% one class |
| text vs picture | oracle 15/21 vs full 14/21; stop rule fired 5 of 5 | oracle **+0.22 above full** |
| control separates | permute_image 0/7, unparsed on 3 of 5 | permute_image −0.72, parsed 6 of 6 |
| necessity | 11 of 14 channels necessary | **0 of 13 hops necessary** |

Two things v3 does better. Its control actually runs: v2's `permute_image` failed to parse on three
of five cases and graded 0/7 where it did, so it never functioned as a control, while v3's parses
everywhere and separates cleanly. And v3 uses more of each paper's argument — 16 hops with 14
attachable, against v2's five hand-picked claims.

One thing v2 did better, and it matters: v2 had a key, however weak. That key was degenerate — every
one of the five expected closings was "partial" — but it at least let an arm be *wrong*. v3's arms
can only be compared with each other, and when they nearly all say "partly warrants", that
comparison has little to say.

The sharpest divergence is necessity. v2 found 11 of 14 channels necessary; v3 finds **0 of 13
hops**. The measures are not the same — v2 removed a whole technique channel from a claim, v3
removes one hop's evidence from a chain — but the direction is unambiguous and the reason is
visible in the prompts: a v3 step still states the paper's conclusion when its evidence is taken
away, so there is nothing left to disagree with.

The conclusion for the design, stated without hedging: **the causal-hop framing did not buy
information.** The sequence is not doing work, the pictures are not doing work over the text, no
hop's evidence is necessary, and the grading question is too easily satisfied to separate the arms.
v3's contribution is structural rather than evaluative — it shows where a paper's argument forks
(Biomaterials), which hops restate rather than advance (Nano Letters M3), and which land on claims
with no figure behind them (adfm M3, M4).

## Where the chain structure lives

The `reordered` result says where it does not live: **not in the sequence, as this design presents
it.** Stripping the paper's order and the link sentences changed nothing. That is a real finding
about the presentation, but it does not establish that the structure is absent from the argument —
only that asking "does this evidence warrant this step?" cannot see it. The chain is handed to the
model as a premise, and a premise is not tested by being reordered; the model re-derives each step
locally from its own evidence either way.

So the structure, if it is anywhere measurable, is in what the chain **excludes** rather than in the
order it presents. Three places this work did find it, none of them in the arms:

- **The graph check.** Seven stage links were candidates; before the matcher of record, five could
  not be confirmed through our graph. Whether hop A's effect claims and hop B's cause claims meet is
  a structural fact, and it is decided outside the solver entirely.
- **The fork.** Biomaterials reaches M4 by two routes sharing no intermediate step. The arms judge
  both identically, but the branching is in the graph whether or not any arm can see it.
- **The restatement.** Nano Letters M3 borrows M2's exact panel set. That is detectable by
  comparing evidence sets, not by asking a model to grade a step.

### The inverted design, and why it is not affordable here

The natural way to make the structure the *answer* rather than the premise is to invert the task:
hand over the evidence unordered and ask the model to reconstruct the chain. Then the ordering is
what is scored, and `reordered` stops being a control and becomes the whole item.

The arithmetic kills it at our chain lengths. Guessing an ordering of `n` steps is right 1/`n`! of
the time:

| chain length | orderings | chance |
|---|---|---|
| 2 | 2 | 50.0% |
| 3 | 6 | 16.7% |
| 4 | 24 | 4.2% |
| 5 | 120 | 0.8% |
| 6 | 720 | 0.1% |

Our six chains are of length 3, 2, 3, 2, 2, 2 — **mean chance accuracy 38.9%**. Four of the six are
two-step chains where a coin does as well as a model. Nothing below four steps separates a solver
from guessing, and **none of the five papers produced a chain of four or more**: 16 hops, nine
confirmed links, longest path three.

So an inverted design needs a corpus filtered for long chains before it can be run at all. From
these five papers the yield of four-plus-hop chains is zero, and that is too small a sample to
extrapolate honestly — the estimate that matters is not in this data and would need a scan across
the hundred-paper bench to produce. What can be said from here is the requirement, not the rate: an
inverted item needs a confirmed chain of at least four hops, and this design's chains are half that
length.

---

# v3b: hide the effect

v3's result stands and is unchanged above. Its cause was the format: every step stated the paper's
conclusion, so the model graded an assertion and the evidence was optional. v3b removes the
conclusion. Each step now gives the evidence and names the **property** it concerns — derived from
the claim's `type`, a controlled vocabulary, because a type cannot leak a result — and asks what the
evidence establishes, what it does not, and with what confidence. The answers are graded against the
hidden effect with the sub-claims as the key: correct, partly correct, wrong, or cannot tell.

Six traces, five arms, three repeats, plus 14 removals x 3. 132 answers and 125 gradings, every one
verified byte-for-byte from the agents' own transcripts.

## The stop rule did not fire, and that is the main validation

> *Stop if the floor arm produces the hidden effect correctly on more than half the hops.*

**Floor is correct on 0 of 41 rulings — 0%, with 39 of 41 "cannot tell".** Adding partly-correct
takes it to 2%. The hidden effect is not readable from captions, so the item is testing evidence
rather than recall. This is the thing v3 could never establish, because v3 handed the conclusion
over in the prompt.

## Arm results

Pooled verdicts, and the paired comparison against `full` on the same case and step, averaged over
repeats on a 0–3 scale (correct 3, partly 2, cannot tell 1, wrong 0):

| arm | n | correct | partly | wrong | cannot tell | hit-rate | paired Δ vs full |
|---|---|---|---|---|---|---|---|
| full | 39 | 17 | 20 | 2 | 0 | **44%** | — |
| floor | 41 | 0 | 1 | 1 | 39 | 0% | **−1.33** (14 of 14 worse) |
| measurement | 42 | 13 | 26 | 3 | 0 | 31% | −0.17 (5 worse, 1 better, 8 same) |
| reordered | 39 | 12 | 24 | 3 | 0 | 31% | −0.18 (6 worse, 2 better, 6 same) |
| permute_image | 28 | 0 | 7 | 19 | 2 | 0% | **−1.72** (10 of 12 worse) |

Nano Letters is excluded from `permute_image`: both its steps are oracle-delivered, so its `full`
arm carries no images and its permuted prompt is byte-identical to `full`. Counting it would score a
non-control as a control passing.

**The design discriminates now, hard, at both extremes.** Captions alone cannot do the task and
wrong pictures actively produce wrong findings — 19 of 28 permute rulings are `wrong`, not `cannot
tell`, so the arm confidently reads the swapped panels and gets the answer wrong. In v3 the widest
gap between any arm and full was 1.44 on a four-level scale that barely moved; here floor and
permute sit 1.3–1.7 below full on a scale full actually uses.

## The three questions

### Does removal now change answers?

**At the step whose evidence was removed, yes, 14 of 14 — but that result is close to tautological
and should not be quoted on its own.** The question asks what *this* evidence establishes; with none
provided, "cannot tell" is the correct answer, and that is exactly what comes back: every one of the
14 drops falls to `cannot tell` in most repeats.

The informative question is whether removing one hop's evidence degrades the **other** hops, which
is what a chain would predict.

**It does not. Mean spillover +0.04 over 20 step-pairs — 5 degraded, 7 improved, 8 unchanged.**
Removing step 1's evidence leaves step 2 exactly where it was. The one large movement, Rare Metals
drop1 → step2 at −1.00, is offset by three positive moves of comparable size.

So v3b changes the removal result at the removed step and leaves it unchanged everywhere else. The
chain still does not propagate.

### Does reordered still equal full?

**Effectively yes, and the apparent difference does not survive the noise.** The pooled hit-rate
looks like a drop, 44% to 31%, but paired on the same case and step the difference is **−0.18 on a
0–3 scale**, with 6 steps worse, 2 better and 6 identical.

Two things make that uninterpretable as an ordering effect. The `measurement` arm — which changes
the evidence, not the order — differs from full by **−0.17**, the same magnitude. And `full`'s own
three repeats are unanimous on only **6 of 11 steps (55%)**, so run-to-run variation on this scale
is as large as the difference being claimed.

| arm | repeats unanimous |
|---|---|
| full | 6/11 = 55% |
| floor | 11/13 = 85% |
| measurement | 11/14 = 79% |
| reordered | 10/11 = 91% |
| permute_image | 4/7 = 57% |

**The sequence still carries nothing this design can detect.** v3b fixed the item without rescuing
that claim.

### Does measurement-only text still match images?

**Yes, essentially. −0.17, with 8 of 14 step-pairs identical.**

This needs the caveat stated in the build: **nothing was stripped.** Zero interpretive terms matched
across all 14 steps, because the graph's observation labels are already written as measurements
("Yield stress in [11-20] at RT: 167 MPa as-grown, 113 MPa after the 520 C anneal"). So the
measurement arm and a plain text arm are the same thing on this data, and this comparison is text
against images, not stripped-text against images. An earlier version of the stripper made it worse
by deleting "reflection" — a diffraction peak — from an XRD measurement.

The direction did flip: in v3 the text arm scored **above** full (+0.22); in v3b it scores slightly
below (−0.17). Both are small. The fair statement is that text and images remain interchangeable on
these fourteen steps, with images perhaps marginally ahead once the conclusion is hidden.

## v3 and v3b side by side

| | v3 | v3b |
|---|---|---|
| the step asks | does this evidence warrant this stated conclusion? | what does this evidence establish about this property? |
| conclusion in the prompt | yes | no |
| graded against | nothing (arms compared to each other) | the hidden effect, sub-claims as key |
| full arm | 86% one class | 44% correct, 51% partly, 5% wrong |
| floor | −0.03 vs full | **−1.33**, 0% correct |
| permute_image | −0.72 | **−1.72**, 19 of 28 `wrong` |
| text vs images | text **above** full, +0.22 | text −0.17 |
| reordered | +0.00 | −0.18, inside the noise |
| removal, dropped step | 0 of 13 necessary | 14 of 14, near-tautologically |
| removal, other steps | — | **+0.04, no spillover** |
| stop rule | — | floor 0% correct, did not fire |

**What hiding the effect fixed.** The item. v3's arms sat on a near-constant scale where nothing
separated except deliberately wrong images; v3b's arms span the full range, captions fail
completely, wrong pictures produce confidently wrong answers, and the evidence is doing the work.
That is a real benchmark item where v3 had one that graded an assertion.

**What it did not fix.** Both structural claims survive unchanged. The sequence still carries
nothing detectable — reordered is within run-to-run noise of full. Text still matches images. And
the chain still does not propagate: removing one hop's evidence leaves the others where they were.

The honest summary is that v3's negative findings were **not** artefacts of the format, even though
the format was genuinely broken. Fixing it changed how well the item measures and left what it
measures saying the same thing.

## Completeness

Grader replies occasionally omitted a step, so the per-arm denominators differ (39 to 42 of a
possible 42, and 28 of 36 for permute after the Nano Letters exclusion). Repeat-stability
denominators vary for the same reason: a step counts only where all three repeats returned a
verdict. No reply was discarded for disagreeing; the gaps are missing rows, not filtered ones.
