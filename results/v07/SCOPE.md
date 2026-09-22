# v07 fix 3: `asks_for` on every item

Every verdict is model against model.

- **net-writer** now returns `asks_for`, the node ids the question actually asks the solver to produce, under the rule
  "The question must ask for exactly the graded target. If you cannot ask for it plainly, say so in `asks_for: []` and
  leave the key empty." The agent recited the new rules verbatim before any item was written.
- **The scope net** (`validate_traces.py`) fails an item when `asks_for` is empty or is not the same set as
  `graded_targets`. A failing item gets one rewrite with the mismatch shown, then `blocked_by: scope`
  (`v07.py written_stage` feedback, `written2`). Items written before the rule carry no field and are warned, not
  failed, so old verdicts stand until their paper is re-run.
- **Rewritten: 4 of 4 known scope items.** All four now pass the scope net with `asks_for` equal to the graded target.

| item | graded target | before | after |
|---|---|---|---|
| AEM 201501833 T3 | o8 | inspect (writer) | **valid** |
| JMST 2020.05.053 T14 | o12 | inspect (writer) | inspect, cause **cutter**: the circled facet is ~30 px in the supplied crop, so the river pattern the key needs is below its resolution |
| AFM 202005640 T2 | o19 | inspect (writer) | inspect, cause **solver**: the arm ignored the ">0.05" series the key turns on |
| Nano Letters 0c03311 T1 | o6 | inspect (writer) | inspect, cause **writer**: the question asks whether the panel supports -6.5 eV, which the panel prints as a label |

- The three items the prompt lists as having `answer_key_nodes` outside `hidden ∪ graded_target` **did not reproduce**:
  a scan of all written items finds one (JMST 2021.11.026 T4), and that trace is closed, so it is not an item. The
  provenance net already fails that condition, which is why none survives in a gated item.
- **Scope blocked 0 of 119 written items**, far under the quarter that would stop the run, because the net only judges
  items written under the new rule; the four re-written ones all pass.
