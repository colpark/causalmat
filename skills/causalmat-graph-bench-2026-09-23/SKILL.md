---
name: causalmat-graph-bench
description: Build a figure-grounded reasoning benchmark from a corpus of materials-science papers, starting from the raw MatMech release and the MatMMExtract sub-panel detector. Use this when the user wants to turn papers with figures into solvable, graded reasoning items; wants argument graphs extracted from papers with every claim tied to a figure panel; wants to cut reasoning traces out of those graphs and validate them by having one model answer and another grade; or wants to reproduce, extend or audit the v07 causalmat run. Covers sub-panel detection, panel-to-caption matching, crop OCR, paper selection, packet building, graph extraction by subagent, structure-only judging, a blind second read of every cited panel, trace cutting, question writing, structural nets, a solving gate with an image arm against a text-only floor, cause inspection, per-paper rows and a standalone item export.
---

# causalmat: papers to a figure-grounded reasoning bench

**Every verdict is model against model.** Write that sentence into every summary this pipeline produces.
No human checks any item. That is a property of the product, not an omission, and it must be stated
wherever the numbers are.

## What this returns

A set of **items**. One item is a question a model can only answer by reading figure panels, an answer key
taken verbatim from a node of the paper's own argument graph, a grading note, and a recorded verdict from
two arms: one that sees the panels and one that sees only the text. An item is **valid** when the image arm
answers correctly and the text-only floor cannot.

The reference run: **100 papers → 477 traces cut → 181 open → 112 valid items** (1.12 per paper),
9 text-sufficient, 55 inspect. 4,447 subagent dispatches, ~44.5 per paper.

Two things count as success. A bench, or a **closure finding** — a measured reason this corpus cannot carry
one. Both are products. Report whichever you get.

## Load before you start

- `references/environment.md` — every tool, weight, key and GPU, and the **six steps that need a human**.
  Read this first. Four of the six cannot be worked around by an agent.
- `references/stages.md` — the stage contract: inputs, outputs, gates, and what to do when a stage fails.
- `references/agents.md` — the seven `net-*` subagents, what each may see, and the relay discipline that
  keeps a prompt honest. **The relay is not trusted.** Read this before dispatching anything.
- `references/failure-modes.md` — what went wrong in the reference run and how it was caught. Load this
  before interpreting any number the pipeline produces; several defects are invisible in the output.

## The pipeline

Eleven stages in three phases. Phase A runs once over the whole corpus. Phase B and C run per paper and
are resumable at every stage.

| # | Stage | Scope | Compute | Output |
|---|---|---|---|---|
| **A1** | Sub-panel detection | corpus | 2 GPUs, ~1 h | `<doi>/panels/panels.json`, `crops/*.jpg` |
| **A2** | Panel↔text matching | corpus | CPU | `<doi>/panels/match.json`, tier per figure |
| **A3** | Crop OCR | subset | 2 GPUs | `<doi>/panels/ocr.json` |
| **A4** | Supply count and selection | corpus | CPU | the paper list worth spending on |
| **B1** | Packet build | paper | CPU | `taxonomy/v07/<part>/packets/<P>.md` |
| **B2** | Graph extraction (staff) | paper | 1 subagent | `taxonomy/graphs_v07/<P>.json` |
| **B3** | Structure-only judge | paper | 1 subagent | `review` block in the graph |
| **B4** | Graph-time panel check | paper | many subagents | `second_read` block, citation fixes |
| **C1** | Trace cutting | paper | CPU | `cut.traces.json` |
| **C2** | Writing and nets | paper | subagents | `written.json`, `validation.json` |
| **C3** | Solving gate and inspector | paper | subagents | `gate.jsonl`, per-item verdicts |
| **C4** | Rows, report, export | corpus | CPU | `batch.csv`, `docs/`, `export/` |

Stage detail is in `references/stages.md`. Do not improvise a stage order: B4 must complete before C1,
because the cutter reads `cue_overrides` that only the panel check writes.

## The three rules that decide whether the product is real

**1. The floor must fail.** An item where a text-only arm answers correctly is *text-sufficient*, not valid.
It is recorded, not discarded, and it is not part of the bench. Without this arm you are measuring recall of
the paper's own prose. In the reference corpus a TF-IDF lookup answers the naive task 98.5% of the time, and
98.9% of papers predate 2022, so contamination binds anything the text alone settles.

**2. The answer must not be handed over.** The cutter's skip rule closes any trace whose given panels carry
the answer as printed text or as an annotation the authors wrote on the image. This closed 126 of 296 closed
traces in the reference run — the single largest cost in the pipeline, and the one worth paying.

**3. Every verdict is model against model.** One model writes, another answers, a third grades, a fourth
rules on disputes. No step is checked by a person. Say so in every artifact.

## Gates

Stop and report rather than continuing when:

- **A1** leaves any DOI folder without a `panels.json`, or any original file fails its CRC check.
  The run writes *beside* the dataset and must change nothing in it.
- **A4** yields fewer papers than the cohort you need. That is a closure finding: report the count.
- **B4**'s panel judge rules `real` on fewer than 3 of the first 60 flags. Keep the screen, but stop paying
  for the staff round — in the reference run 78 flags produced 4 citation fixes.
- **C2**'s scope net blocks more than a quarter of written items. The writer prompt is wrong, not the items.
- **C3** shows `writer` as the largest inspect cause. Fix the writer prompt before running more papers; in
  the reference run it was 16 of 55 and is the top open defect.
- Any `net-*` subagent lacks its expected rules or tools after a restart. The agent registry is cached;
  see `references/agents.md`.

## Cost

44.5 subagent dispatches per paper, median 188 min wall time per paper at 20-way concurrency.
A 100-paper run is ~4,400 dispatches. Project linearly; the reference run's 16,487-paper supply would be
~733k dispatches for ~18k items, which is a budget question, not a research one.

## Reproducing the reference run exactly

```bash
scripts/fetch_data.sh                       # 16 GB, MD5-checked, extracts to ./matmech
# A1-A3: see references/environment.md, needs 2 GPUs and a human for the checkpoint
python3 taxonomy/select_v07.py --n 168      # deterministic paper list
python3 taxonomy/build_packets_v06.py <papers.txt> <outdir> --linked-text
# B2-C4: per paper, driven by trace_kit/v07.py; see references/stages.md
python3 trace_kit/v07_scale_report.py       # every table in docs/V07_SCALE.md
python3 trace_kit/export_items.py --include text_sufficient,inspect
```

The selection, the cut and every net are deterministic. The subagent stages are not: graphs, questions,
answers and verdicts vary between runs. Record dispatch ids (`v07.py log`) so a number can be traced to the
transcript that produced it.
