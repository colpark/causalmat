# v06 pilot: eight papers, graphs and traces rebuilt, validated by solving

Branch `v06-pilot/2026-09-21`. The same eight papers run through the v06 prompts (v06: captions only; v06b: linked text restored; v06c: generate generously, validate by solving).

**Every verdict is model against model.** The graphs come from staff and judge subagents. The questions and keys come from net-writer. The solving gate is Sonnet subagents (net-fullarm, net-floor, net-grader). No human has checked any item.

## Funnel per paper (v06c)

| paper | cut | open | written | passed nets | valid | text-sufficient | inspect |
|---|---|---|---|---|---|---|---|
| J Adv Ceram 9-0334-4 | 9 | 8 | 8 | 8 | 2 | 1 | 5 |
| Acta Materialia 4.06.008 | 11 | 9 | 9 | 9 | 6 | 2 | 1 |
| Adv Functional Materials 02005093 | 2 | 1 | 1 | 1 | 0 | 0 | 1 |
| Adv Energy Materials 01501833 | 7 | 0 | 0 | 0 | 0 | 0 | 0 |
| Adv Energy Materials 01301564 | 2 | 1 | 1 | 1 | 0 | 0 | 1 |
| Rare Metals 2-0515-6 | 4 | 3 | 3 | 3 | 2 | 0 | 1 |
| Bioactive Materials 9.01.001 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| Adv Materials 01300071 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **total** | 38 | 23 | 23 | 23 | 11 | 3 | 9 |

Of the valid items, 4 have a partially correct full arm with an abstaining floor (counted valid, flagged `partial` in `results/v06c/solving_gate.jsonl`). On the first four papers, 7 of 18 gate items are inspect, so the stop rule (more than half) does not fire.

## Trace counts across versions (the same eight papers)

| version | traces | open | control | closed |
|---|---|---|---|---|
| v05 (MatMech block in the packet) (5 of 8 papers on file) | 33 | 13 | 13 | 7 |
| v06 (captions only) | 21 | 0 | 6 | 15 |
| v06b (linked text, cutter v2.1) | 38 | 4 | 9 | 25 |
| v06c with --v1-filters | 38 | 5 | 9 | 24 |
| v06c (cutter v2.2) | 38 | 23 | 0 | 15 |

## With and without the v1 filters

The v2.2 cutter keeps three hard rules before the gate: the panel matches its node (R6, now honouring judge `cue_overrides`), the answer is findable from what is given (R3, with condition labels counted as given), and nothing reveals the answer (R4, R5). Switched off behind `--v1-filters`: the bare-infer closure, the floor-reaches closure, and the plot-read and depth-one control strata. Per-paper and per-root counts are in `results/v06c/CUT_v2_2.md`.

**What the gate teaches.** The v1 filters would have removed 18 of the 23 items that reached the gate:

| v1 filter | items at gate | valid | text-sufficient | inspect |
|---|---|---|---|---|
| bare infer (no rejection, budget or stopping rule) | 9 | 3 | 1 | 5 |
| depth one and not an image read (control) | 7 | 5 | 1 | 1 |
| plot read, no domain model (control) | 2 | 1 | 0 | 1 |

- **Depth-one control:** 5 of 7 were valid, mostly Acta diffraction and phase-map reads. This filter was throwing away good items.
- **Bare-infer closure:** 3 of 9 were valid. The 5 inspect items failed on masking or keys, not on bareness, so the filter did not predict the failure.
- **Plot-read control:** 1 of 2 was valid.
- **Text-sufficiency:** the gate catches it by itself (3 items, 2 of them from filtered traces), mostly because a caption states the answer. The floor-reaches closure is not needed before the gate.

## Inspect items by cause

| paper | trace | cause | defect |
|---|---|---|---|
| J Adv Ceram 9-0334-4 | T3 | cutter | the key names phase identities (grey ZrB2, dark SiC, white WSi2) that only the in-image labels carry, and R5 masked them; the full arm read the shapes but could not assign phases |
| J Adv Ceram 9-0334-4 | T4 | graph | the full arm read the ZrB2 grains in F5c/F8d as equiaxed, against the key (elongated, interlocking); the floor half-reached the key from context m1 (liquid transport to fast-growing ZrB2 planes) |
| J Adv Ceram 9-0334-4 | T5 | cutter | the answer is printed in the panel: F6 is handed over as a whole figure with no OCR record, so its "ZrB2 platelets" label was never masked |
| J Adv Ceram 9-0334-4 | T6 | cutter | inconsistent masking: "Submicro-Sized SiC" was masked in F8a but "Nano-sized SiC" stayed in F8b/F8c; the full arm read the labels and inferred the wrong trend |
| J Adv Ceram 9-0334-4 | T7 | cutter | the answer is printed in the panel: the "nano-sized" label in the unmasked whole figure F6; the full arm read it and did not measure the 50-150 nm size |
| Acta Materialia 4.06.008 | T4 | writer | the rewrite paraphrased the key into "banding in one direction, no variation through the depth-wise direction"; the full arm said the z direction is uniform at every step (the answer) and the grader did not match it; the F6c-e captions also state it |
| Adv Energy Materials 01301564 | T1 | graph | the full arm read the insets as sparse thin flakes at 0 mL and coarser flakes at 20 mL, against the key (few large flakes at 0 mL, finest at 10-20 mL); the insets are small and the reading is disputable |
| Adv Functional Materials 02005093 | T1 | cutter | F5i has no crop in the store; the fallback to the whole figure hands over an image with panels a-h and no histology, so nothing can be read |
| Rare Metals 2-0515-6 | T2 | graph | the key gives absolute plate lengths (20-40, 10, 5-10 nm) that the full arm could not measure against the 20 nm bar; it gave only the correct coarse-to-fine order |

By cause: {'cutter': 5, 'graph': 3, 'writer': 1}. The dominant cutter defect is labels printed in the image: whole figures handed over without OCR masking (ceramic F6), inconsistent masking across panels of one figure (ceramic F8), and phase labels masked when the key needs them (ceramic F5).

## Text-sufficient items (knowledge pile)

- J Adv Ceram 9-0334-4 T8: the given observation o15 names deflection, bridging, pull-out and branching, and s4 gives interlocking platelets; the mechanism follows from the text
- Acta Materialia 4.06.008 T5: the F5c/F5e captions state that the peak width increases greatly in the qx direction
- Acta Materialia 4.06.008 T10: the caption names a {111} pole figure of the ellipse region; picking one isolated grain peak follows from domain knowledge

## The five old defective items

| item (v05) | defect then | fate in v06c |
|---|---|---|
| ceramic T5 (F8a-e) | annotated-micrograph leak | Still defective. The F8 panels return as ceramic T6 (SiC size, RZSZ-0/10/15). R5 masked "Submicro-Sized SiC" in F8a but OCR missed "Nano-sized SiC" in F8b/c, and the full arm answered from the labels (inspect). The same class recurs in ceramic T5/T7 through the unmasked whole figure F6. |
| Acta T10 (F1b, F4b, F6a-e) | false rivalry; key resting on unseen facts | The rivalry is gone: all causes in the v06b graph are joint, and R1 builds no competing-causes trace from them. The same panels now carry single-read items: T7 (F6 phase jumps) valid, T6 (F4b) valid with a partial full arm, T10 (F1c) text-sufficient, T4 (F6 z-uniformity) inspect because the writer paraphrased the key. |
| AEM 2013 T4 (intervene) | the cut handed over the decision | Fixed but closed. The v06c intervene cut (AEM 2013 T2) hands over only F1a and F1b (0 and 5 mL, levels read from the condition labels), withholds F1c (10 mL, the decision), F1d and the series panels, and then closes on rule 3: the decision node's unseen facts include the PCE values. |
| AEM 2015 T1 (F4a/F4b) | wrong panel citation (CV plots cited as SEM) | Closed by R6 (panel_modality). The cut now catches it. |
| AFM T3 (F2) | hidden mechanism no panel shows | Not generated. The v06b graph gives AFM only one open trace (T1, a rejection on F5i), and that one is inspect: F5i has no crop, and the whole-figure fallback does not contain it. |

## Joint versus alternative causes

Every causes edge in the eight v06b graphs is `mode: joint`. Acta has one `rules_out` edge, but it does not touch a claim with two causes, so no competing-causes trace survives in v06c. R1 turns each joint-cause claim into a mechanism trace seeded at the explaining MEC; those close when the mechanism has no shown evidence (AEM 2015 T6, Rare Metals T4).

## Graph diffs

v06b against v05 (the MatMech influence) and v06b against v06 (the linked-text contribution) are in `results/v06b/graph_diff.md`. With linked text restored, no v06b spine is more than a third smaller than v05. The ceramic spine is 13 nodes and carries the liquid-phase mechanism.

## Files

- `results/v06c/cut`, `cut_v1filters`, `CUT_v2_2.md`, `CONDITION_LABELS.md`: the cut
- `results/v06c/writer/<paper>`: packets, replies (byte-exact relay), `written*.json`, `validation*.json`
- `results/v06c/gate/<paper>`: gate packets, arm answers, grader prompts and replies
- `results/v06c/solving_gate.jsonl`: one line per gate item, with verdict, defect, cause and v1 filter
- `results/v06c/sheets`: question-only and answered PDFs with images for the 11 valid items (`trace_kit/build_sheets_v06c.py`)
