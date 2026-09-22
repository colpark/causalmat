# v07 checkpoint after Part B (32 papers)

**Every verdict is model against model.** The graphs come from staff and judge subagents, the items from net-writer, the second read from net-reread plus net-grader, and the gate from net-fullarm, net-floor and net-grader. No human has checked any item.

- **Yield:** 31 valid items over 32 papers, mean 0.97 (floor 0.5). The pilot gives 7 on 8 papers; Part B gives 24 on 24.
- **Gate items:** 56 in all: 31 valid, 4 text-sufficient, 21 inspect (37.5%, below the 50% stop line).
- **Inspect causes:**
  - graph: 16. Of these, 15 were second-read flags.
  - solver: 3
  - writer: 1
  - cutter: 1
- **Zero-trace papers:** 9 of the 24 Part B papers produced no open trace. The trace was closed by R3 (not derivable from the given panels), by the skip rule, by no crop, or by no oracle.

## Stop rule triggered: judge passes, second read flags
The second read flagged at least one panel on 10 of 32 papers (31%). Every one of those papers had **0 judge overturns** (8 to 42 panel checks each). The rule says to stop above a quarter.

| paper | second-read flags | judge panel checks | overturns |
|---|---|---|---|
| Acta 2014.06.008 (pilot) | 2 | 16 | 0 |
| AEM 201301564 (pilot) | 1 | 19 | 0 |
| Rare Metals 0515-6 (pilot) | 1 | 8 | 0 |
| Acta 2015.04.055 | 1 | 22 | 0 |
| Bioactive 2020.01.002 | 1 | 15 | 0 |
| ACHM 00366-2 | 2 | 37 | 0 |
| Adv Mater 201702037 | 2 | 42 | 0 |
| JMA 2013.12.002 | 1 | 20 | 0 |
| J Adv Ceram 0476-z | 1 | 23 | 0 |
| JMST 2020.05.053 | 2 | 32 | 0 |

Across all 32 papers the judges overturned none of their panel checks.

What the flags look like, from the ones read so far:
- **Genuine defects the judge missed.** For example:
  - ACHM F6b: the crop the id resolves to shows elongation bars, but the node describes a dielectric-loss curve.
  - Rare Metals F1c: the node says "broken strings" where the read sees a continuous network.
- **Grader over-flagging.** For example:
  - Bioactive F6a–F9a: the read describes "cell grid images" and the key says AO/EB images.
  - Acta 2014 o6: the grader reads the y–x maps against a key about the x–z maps.

The flags have not been sampled for a precision estimate.
