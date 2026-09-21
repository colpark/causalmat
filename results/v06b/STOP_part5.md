# v06b stop after part 5 (solving gate)

Every verdict is model against model.

## What reached the gate

The eight v06b graphs cut into 38 traces: 4 open, 9 control and 25 closed.

| paper | open after cut | written | after gates |
|---|---|---|---|
| Journal of Advanced Ceramics | T6, T8 | both | both blocked (T6 leak in question; T8 bigram "crack path" shared with the given observation o15) |
| Acta Materialia | none | | |
| Advanced Functional Materials | none | | |
| AEM 2015 | none (T1-T3 closed by R6: the SEM observations cite F4a/F4b, which are CV plots) | | |
| AEM 2013 | none | | |
| Rare Metals | T1, T3 | both | T1 survives; T3 blocked (bigram "theta precipitates" shared with the given node d1: likely a false positive, left for a decision) |
| Bioactive Materials | none | | |
| Advanced Materials | none | | |

One item reached the solving gate: Rare Metals T1.

## Gate result (results/v06/solving_gate.jsonl)

Rare Metals T1: the fullarm is PARTIAL and the floor ABSTAINs, so the item is classed **inspect**.

The defect is the answer key. It goes past the graded target o1 into the claim s1 ("La more than Sm") and its downstream p3/c1. The fullarm read the panels and put Sm ahead of La in refinement. It was marked down only for that, and o1's own panel descriptions do not settle La against Sm. The floor could not answer, so the item is not text-sufficient.

## Stop

The rule reads: more than half of open items marked inspect on the first four papers. Read literally, it does not fire, because the first four papers yield no open item after the cut. In substance it does fire: the pilot yields one servable item across eight papers, and that item is inspect. There is no valid item to build a sheet for, so part 6 (sheets, docs/V06_PILOT.md, PR) is not run.

## Dominant defects, in order of how many items they remove

1. **Bare-infer and depth-one rules (v1, unchanged).** 14 closed and 9 control. Most infer traces never reach rule 3.
2. **Rule 3 (v2.1).** 6 closed. The drivers are caption-only sample identity and GO volumes that appear only in linked text.
3. **The leak gate after one rewrite.** 3 blocked. Two of these are bigrams shared with a given node, which no rewrite can remove.
4. **The writer includes downstream claim nodes in the key of an infer trace.** This sends the only survivor to inspect.

## Decisions needed

- Whether a bigram shared with a given node, but absent from the question, should block. This affects ceramic T8 and Rare Metals T3.
- Whether the key of an infer trace should be limited to its graded targets (a writer rule or a cutter field).
