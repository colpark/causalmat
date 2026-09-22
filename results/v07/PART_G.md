# v07 G: the blind second read is the panel check

**Every verdict is model against model.**

## Result
**40 valid on the 32 papers, up from 31 at checkpoint B.** There are 60 gate items, against 56 before. The other 20 are 4 text-sufficient and 16 inspect.

| | checkpoint B | after G |
|---|---|---|
| gate items | 56 | 60 |
| valid (partial) | 31 | **40** (18) |
| text-sufficient | 4 | 4 |
| inspect | 21 | 16 |
| inspect causes | graph 16 (14 second read), solver 3, writer 1, cutter 1 | solver 6, writer 6, graph 3, cutter 1 |
| inspect by second read | 14 | 0 |

Per-item rows: `results/v07/gate_32_after_G.jsonl`. The 4 pilot traces whose flags were cleared carry their v06c gate verdicts: their trace, writer and gate prompts are unchanged, as A3 established.

## 1. Grader leniency (net-grader.md, second-read case only)
- Added the rule in the prompt's wording. After a restart the grader recited it verbatim.
- The 13 Part F flags were re-graded with their original prompts: **5 of 12 wording flags clear, 0 of 1 real flags clear.** No tightening was needed. Details are in `reread_precision.md`.
- The 7 wording flags that survive are reader misreads, which a text-only grader cannot detect.

## 2. Judge scope (taxonomy/prompts/v07_judge.md)
- The judge now checks structure only:
  - spine order and connectivity;
  - one claim per node (split, merge duplicates);
  - `source` and `requires_unseen` on every node, `read_from` on every observation;
  - `mode` on multi-cause claims;
  - the MatMech tally, which is recorded and does not edit the graph.
- It opens no figure or crop and rules on no panel or technique.
- I edited `v07_judge.md`, not `v06_judge.md`, because v07 dispatches `v07_judge.md`; the v06 file stays as the record of v06.

## 3. The panel check at graph time (trace_kit/v07.py rrgraph / rrggrade / rrgapply)
Order of work:
1. After the judge, net-reread reads every panel cited by any node, blind.
2. net-grader grades each node against the reads of all its cited panels, with the leniency rule.
3. A WRONG node goes to the staff subagent in `rrgraph/fix.md`. Staff re-opens the whole figure and the crop, then either repoints `panel_ids`, sets `source` to `text`, or keeps the node. The action goes in `rrgraph/fix.json`.
4. A repointed node's new panels are read and graded again.
5. A kept node is resolved: staff looked at the image.
6. A CORRECT node is recorded as `cue_overrides` in the graph. The judge used to supply these, and the cutter's R6 rule honours them.
7. Traces inherit only the flags that remain.

## 4. What was real, and what was fixed
**The one Part F `real` flag was a tooling bug.**
- ACHM o16 cites F6b. The packet's F6b is the paper's Fig. 5b, the dielectric loss plot, and it shows what the node says. The reader and the gate had been given the paper's Fig. 6b bar chart.
- Cause: packet ids number figures by their position in `data.json` `image_info`. `panel_record`, `fig_preamble` and `linked_text` in `cut_traces.py`, and the panel store in `validate_traces.py`, looked figures up by `match.json` `figure_number`, which repeats or skips on schemes and unnumbered figures.
- Fixed with `fig_by_number`.
- Affected: 9 of the 32 papers and 51 of the 168 Part C papers.

The bug did most of its damage in the cut, not in the second read: wrong crops trip the image-type and missing-crop rules and close traces. The re-cut reopened 6 traces:
- AEM 1601491 T7
- Bioactive 2020.02.005 T1 and T2
- POC 2016.09.010 T1
- AEM 201501833 (pilot) T1 and T3

It also gave ACHM T1, T3 and T4 their correct crops.

The 5 re-cut papers ran the new pipeline end to end: graph-time second read, staff fix, cut, writer, nets, gate, inspector. The pilot paper's v06b graph was copied to `graphs_v07/`, so its pipeline is v07.

| paper | cited panels | grader units | WRONG | staff: repointed / text / kept | gate after G |
|---|---|---|---|---|---|
| ACHM s42114-021-00366-2 | 22 | 29 (+1 after repointing) | 4 | 1 / 1 / 2 | 3 valid |
| AEM 1601491 | 15 | 23 | 3 | 0 / 0 / 3 | 4 valid, 1 inspect (solver) |
| Bioactive 2020.02.005 | 25 | 25 | 3 | 0 / 0 / 3 | 1 valid, 1 inspect (solver) |
| POC 2016.09.010 | 18 | 14 | 6 | 0 / 0 / 6 | 3 valid |
| AEM 201501833 (pilot) | 14 | 19 | 1 | 0 / 0 / 1 | 1 valid, 1 inspect (writer) |
| **total** | **94** | **110** | **17** | **1 / 1 / 15** | **12 valid, 3 inspect** |

- Graph-time second read on these 5 papers: 17 of 110 units flagged (15%). Staff changed 2, so precision is 2/17 = **12%**, and **2 of 110 panel-citing nodes (1.8%) needed a citation fix**:
  - ACHM s10 repointed from F3e+F3f to F3a, F3c, F3d, F3e, because F3f is only a photo of powder colours;
  - ACHM s14 set to text, because its "<0.026" figure is only in the table.
- For the 32 papers, the 12 Part F `wording` flags count as cleared: the judge ruled them from the image. Their traces went to the gate:
  - Acta 2015 T1: valid.
  - J Adv Ceram 0476-z T3: valid.
  - Adv Mater 702037 T2: inspect, cause solver.
  - Adv Mater 702037 T3: inspect, cause writer.
  - Bioactive 2020.01.002 T2: inspect, cause writer.
  - JMST 2020.05.053 T14: inspect, cause writer.
  - JMA 2013 T4 and JMST T4 fail the leak and provenance nets, so they drop out of the gate set.
  - Pilot traces: Rare Metals T1 is valid and Acta 2014 T5 text-sufficient (v06c verdicts). Acta 2014 T4 and AEM 2013 T1 stay inspect (v06c causes writer and graph).
- None of the 16 inspect items now comes from the second read. Of the 7 new inspect items, the inspector found none to be a graph error: 4 writer, 3 solver.

## Other fixes
- **Stray tool markup:** an arm reply ended in `</message></invoke>`, and relays strip that from prompts. `v07.py grade` now removes it from the candidate before building the grader prompt.
- **Graph file indentation:** staff wrote one graph back with 2-space indentation. It was reformatted to the repo's indent=1.

## Cost of the re-run
- Second read: 94 reads and 111 grader units.
- Re-grade of Part F flags: 13 grader dispatches.
- Staff: 3 dispatches.
- Writer: 15 jobs.
- Arms and graders: 42 arms and 23 graders.
- Inspector: 2 dispatches.
- Relays: 9.

Every verdict is model against model.
