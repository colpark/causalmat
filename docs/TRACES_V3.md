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
