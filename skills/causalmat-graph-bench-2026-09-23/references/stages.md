# Stage contract

Every path is relative to the repo root. Per-paper state lives in `results/v07/papers/<P>/`; a paper is
resumable at any stage because each writes a file the next reads.

`<P>` is `<Journal>__<doi with / as _>`, e.g. `Acta_Materialia__10.1016_j.actamat.2015.04.055`.

---

## Phase A — once over the corpus

### A1 Sub-panel detection

```bash
python scripts/panels/detect_panels.py --root ./matmech --out-dir ~/panels/out \
    --host-idx 0 --n-hosts 2 --gpu-idx 0 --n-gpus 1
```

Writes `<doi>/panels/panels.json` and `panels/crops/<figure stem>_<label>.jpg` (quality 90, cut at integer
pixel coordinates from the original). Corpus records merge into `<root>/panels_run/`.

Resumable: a folder whose `panels.json` carries the same `run_version` is skipped.

Nine rules run after detection. Seven are from the operator plan (broken records to `errors.jsonl`,
caption label extraction, single-figure rule, duplicate-label dedupe, nested-box removal, mismatch
flagging, two-level labels). **Two were added after a dry run** and matter:

- **3b whole-frame** — every box covers ≥85% of the image and the caption names no panels → `is_single`,
  no crops. Without it, single-panel schematics get two or three stacked whole-frame boxes under
  different letters.
- **5b cross-label overlap** — drop a box whose IoU with a higher-scoring kept box exceeds 0.7, or that
  sits >90% inside it, whatever its letter. Rule 5 only removes nested boxes of the *same* label.

Reference: 422,869 figures, 1,090,345 crops, 46 GB, ~1 h on two GB10s. 32% of figures are single-panel.

**Gate:** every DOI folder has a `panels.json`, both hosts ran the same checkpoint hash, and
`verify_untouched.py` passes against the release zip's CRC32s.

### A2 Panel↔text matching

```bash
python scripts/panels/match_panels.py --root ./matmech --out-dir ~/panels/match_out --workers 16
```

Ties every detected panel to the caption sentence that *defines* it and the body text that *uses* it, and
assigns a tier per figure. Stages 1–4 and 6 are regex and geometry only; stage 5 is OCR and runs on
flagged figures when `pytesseract` is available.

Tiers decide what a packet may offer. **Tier A** figures give per-panel crops with caption spans.
**Tier B** gives fewer. **Tier C** offers *no panels at all* — the graph may still cite the whole figure
with `figs` and empty `panel_ids`, and the cutter's `no_crop` rule will later close traces that depend on
it. Codes seen in practice: `A_exact`, `C1_count_mismatch`, `C3_caption_swap`, `C4`, `C6_unresolved`.

Reference: 60.6% of figures name panel labels; of those 64.4% match the detected letters exactly.

### A3 Crop OCR

```bash
python scripts/panels/ocr_panels.py --root ./matmech --out-dir ~/panels/ocr_out \
    --host-idx 0 --n-hosts 2 --procs 18
python scripts/panels/merge_ocr.py --root ./matmech --out ./matmech/ocr_run --parts ...
```

RapidOCR over every crop of the selected subset → `<doi>/panels/ocr.json`, holding each token with its
box and confidence. Sharding matches A1.

Everything downstream re-derives cue classes from these stored tokens, so a pattern change never needs an
OCR re-run — `scripts/panels/cue_rules_v2.py` `assign(tokens)` returns the cue list for one crop offline.

**Cue precision matters and is measured.** `docs/CUE_PRECISION.md` judged 295 crops by eye; 7 of 14 cue
classes fell under 90% and are disabled. A cue class that is wrong does real damage: it drives the
technique check in B2 and the R6 block in C1.

### A4 Supply count and selection

```bash
python scripts/panels/fm_supply.py --root ./matmech --out results/fm_supply.json
python3 taxonomy/select_v07.py --n 168 --out results/v07/selection.json
```

Supply pools evidence per paper from three independent sources — panel cues, MatMech's own
`microscopic_image` flag, and the experiment `type`/`name` strings — so a modality counts when any names
it. Reference: 61,766 papers → 26,700 with SEM → **16,487 with SEM plus three or more tool-addressable
modalities**.

Selection is deterministic and excludes every already-graphed paper. Eligibility: SEM confirmed on an
accepted panel; at least two other modalities figure-backed; 4–12 figures; ≥60% of them tier A/B.
Journal quota proportional to the eligible pool by largest remainder, minimum 3 per journal. Within a
journal: year descending, then DOI.

**Gate:** if the eligible pool is smaller than your cohort, stop and report the count. That is a closure
finding and it costs nothing to produce.

---

## Phase B — per paper, building the graph

### B1 Packet build

```bash
python taxonomy/build_packets_v06.py <papers.txt> taxonomy/v07/<part> --linked-text
```

The packet is the **only** thing the graph-building subagent may read. It carries: the title and metadata,
every figure's caption, each figure's linked body text, and a panel section listing per crop its absolute
path, caption span, OCR cue classes, every OCR token with its box, and `annotated: true` when a token is a
word or phrase written inside the image (not a panel letter, tick, unit, scale bar or axis label), with
those annotation strings listed.

Deliberately **excluded**: MatMech's own extracted mechanisms, the tetrahedron summary, the MST chain and
the material summary. Those move to `judge_only/<P>.matmech.md`. A graph built from MatMech's own
mechanism text would be reproducing the dataset, not reading the paper.

### B2 Graph extraction — `net-staff` (a general-purpose subagent given `taxonomy/prompts/v07_staff.md`)

Builds an argument graph in the frozen v04 vocabulary: spine
`HYP → DES → PRC → STR → PRP → PRF → DSC` with `MEC` bridging, 12–20 connected spine nodes, each spine
`STR/PRP/PRF/MEC` claim backed by `OBS` evidence or a `KNW` premise.

Non-negotiables, all checked later:

- `panel_ids` copied **verbatim** from the packet, never invented. `[]` with `figs` when reading a whole
  figure or a panel the packet does not offer.
- Every node carries `attrs.source` ∈ `figure | text | inferred | prior_knowledge`. A claim depending on a
  fact visible only in text lists that fact in `attrs.requires_unseen`.
- Every `OBS` carries `attrs.read_from` ∈ `pixels | annotation | axis`. Content matching a listed
  annotation string is `annotation`, with the string in `attrs.annotation_match`.
- Every figure-backed `OBS` carries `attrs.technique` as `FAMILY:mode`, agreeing with the cited panel's
  cue classes via `trace_kit/cue_technique.json`. **A disagreement means the wrong panel was cited.**
  Find the right panel or drop the citation; never change the technique to fit the panel.
- Two or more `causes` edges into one claim each carry `mode: joint | alternative`, `alternative` only
  when a caption or figure shows the choice, with `mode_basis`.

Writes `taxonomy/graphs_v07/<P>.json` and `<P>.build.json` (figures opened, crops opened, panels offered
and cited, cue conflicts resolved, merged nodes).

### B3 Structure-only judge — `net-judge`

`taxonomy/prompts/v07_judge.md`. Checks **structure only**: spine order and connectivity, one claim per
node, `source`/`requires_unseen` on every node, `read_from` on every observation, `mode` on multi-cause
claims, and the MatMech tally (recorded, does not edit the graph).

**It opens no figure and no crop, and rules on no panel or technique.** That job moved to B4 in v07. A
judge that opens images duplicates the second read and disagrees with it.

Writes a `review` block into the graph and a `<P>.judge.md` note.

### B4 Graph-time panel check

This is the expensive stage and the one whose value you should keep measuring.

```bash
python3 trace_kit/v07.py rrgraph  <P>   # net-reread on every panel any node cites, blind
python3 trace_kit/v07.py rrggrade <P>   # net-grader: each node against the reads of its cited panels
python3 trace_kit/v07.py rrgapply <P>   # verdicts; WRONG units -> a flag
python3 trace_kit/v07.py pjudge   <P>   # net-panel-judge opens the crop and rules real|ok
python3 trace_kit/v07.py pjapply  <P>   # only "real" reaches staff, in rrgraph/fix.md
#   staff subagent reads fix.md, opens the whole figure and the crop, writes rrgraph/fix.json
#   {"<node>": {"action": "repointed|text|kept", "panel_ids": [...], "why": "..."}}
```

`net-reread` sees **one image and nothing else** — no caption, no node, no paper. That blindness is the
point and also the source of most false positives.

A `CORRECT` unit records a `cue_overrides` entry in the graph: the second read confirms the panel, so an
OCR cue conflict was a misfire and the cutter's R6 rule honours the override. **C1 depends on this**, so
B4 must finish before C1.

Resolution: `repointed` re-reads and re-grades the new panels; `text` drops `panel_ids` and lists the fact
in `requires_unseen`; `kept` means staff looked at the image and the node stands. **A kept node is
resolved and its flag must clear** — see `failure-modes.md`, this was a bug.

Reference: 1,632 units checked, 214 flagged, 48 ruled real, **4 actual citation fixes**.

---

## Phase C — per paper, making and grading items

### C1 Trace cutting

```bash
python3 trace_kit/v07.py prep <P> <part>
```

Cuts every candidate reasoning trace out of the graph, then closes the ones that cannot make a fair item.
Roots: `infer` (compare, estimate, classify, rank), `explain` (mechanism, rejection, competing causes),
`intervene` (next condition). The closing rules, by cost in the reference run:

| rule | closed | what it catches |
|---|---|---|
| `skip` | 126 | the given panels carry the answer as text or as an author's annotation |
| `R3` | 77 | the graded target is not readable from the figure handed over |
| `no_crop` | 57 | the evidence is cited by figure only, with no crop to hand over |
| other | 20 | |
| `R4` | 16 | a context node shares a claim with a hidden node, or the sweep decision is withheld |
| `R6` | 0 | panel-modality block — fires only without a `cue_override` from B4 |

Also: `R1` closes joint-cause traces with no shown mechanism evidence; `R7` demotes a multi-panel rank to
compare; `R9` drops a walk step that restates an earlier claim; `R5` masks an answer token in a crop
(unused in v07 — no masking occurred).

296 of 477 traces close here. **That is the pipeline working.** The skip rule alone is what stops the
bench measuring OCR.

### C2 Writing and the structural nets

```bash
python3 trace_kit/v07.py written  <P>   # net-writer merged, nets run, pass-2 packets for fixable hits
python3 trace_kit/v07.py written2 <P>   # pass 2 merged, nets run again
```

`net-writer` sees the whole trace including hidden nodes — it is the author, not the answerer — and
returns `question`, `answer_key`, `answer_scope`, `grading`, `answer_key_nodes`, `asks_for`.

Seven nets, all in `trace_kit/validate_traces.py`:

| net | fails when |
|---|---|
| `leak` | the question shares a bigram, a number or a content word with the hidden answer |
| `disjoint` | a hidden node is also given |
| `grader_withheld` | a node the grading channel needs is handed over |
| `derivable` | the observation has no panels, or does not evidence the claim |
| `panels` | a panel id is malformed, or an `infer` item has no panels |
| `linear` | the walk's step numbering or dependencies are broken |
| `provenance` | the answer key contains a number no cited node label carries |
| `scope` | `asks_for` is empty or differs from `graded_targets` |

A leak or provenance hit the writer can fix goes back for one rewrite, then the item is `blocked: scope`.
**The writer may decline**: `asks_for: []` when it cannot ask for the graded target plainly. That is a
correct outcome, not a failure.

### C3 Solving gate and inspector

```bash
python3 trace_kit/v07.py gate    <P>   # net-fullarm (sees panels) and net-floor (text only)
python3 trace_kit/v07.py grade   <P>   # net-grader on each arm's answer; CANNOT DETERMINE is ABSTAIN
python3 trace_kit/v07.py verdict <P>   # gate.jsonl rows; failures -> inspect.md
python3 trace_kit/v07.py cause   <P>   # inspector causes merged into gate.jsonl
```

Verdicts:

- **valid** — the image arm is CORRECT and the floor is not. The item.
- **text-sufficient** — the floor is also CORRECT. Recorded, not part of the bench.
- **inspect** — the image arm failed. An inspector opens the images and assigns a cause:
  `graph | cutter | writer | grader | solver`.

`solver` means the item is fair and the model misread it — the benchmark working. Every other cause is a
defect in the pipeline. Track the mix; it is the health metric.

### C4 Rows, report, export

```bash
python3 trace_kit/v07.py row <P>              # one row of results/v07/batch.csv, 26 columns
python3 trace_kit/v07_scale_report.py          # every table in docs/V07_SCALE.md
python3 trace_kit/export_items.py --include text_sufficient,inspect
```

The export writes a standalone dataset: per item a `question.pdf` (exactly what the solving arm received,
panels inline), an `answer.pdf` (walk, key, grading, nets, both arms and their graders), `images/` with a
PNG per given panel plus `images/figures/` and `images/withheld/`, an `item.json` and a `panels.csv`;
plus `index.csv`, `items.jsonl` and a `README.md` per root.

Five checks, all of which must pass: both PDFs and an `item.json` per item; **no answer-key sentence or
hidden node id in any `question.pdf`** (verify the check is not vacuous by confirming it *does* find the
key in `answer.pdf`); counts agreeing across `index.csv`, `items.jsonl` and folders; every PNG larger
than 80×80; and a count of items missing a panel.

The export tree is **not committed** — the PNGs are copies of publisher figures. Gitignore it.
