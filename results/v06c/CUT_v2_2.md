# Cutter v2.2 on the v06b graphs

Before the gate, three hard rules apply: the panel matches its node (R6), the answer is findable from what is given (R3), and nothing reveals the answer (R4, R5). The v1 filters are off by default: the bare-infer closure, the floor-reaches closure, and the plot-read and depth-one control strata. `--v1-filters` restores them for comparison, and that run reproduces the v06b cut except where the R6 fix below applies. Generate stays closed with no oracle. Rank-needs-three, competing causes and the optimum test change the question type as before.

Every verdict is model against model.

R6 now honours a judge's recorded `cue_overrides`. The Acta judge overrode F6c, a phase map where the scale-bar detector had fired on the colour bar, and without the override Acta T4 and T7 were blocked.

## Per paper

| paper | traces | v2.2 open / closed | with --v1-filters open / control / closed |
|---|---|---|---|
| Acta Materialia .2014.06.008 | 11 | 9 / 2 | 0 / 7 / 4 |
| Advanced Energy Materials nm.201301564 | 2 | 0 / 2 | 0 / 0 / 2 |
| Advanced Energy Materials nm.201501833 | 7 | 0 / 7 | 0 / 0 / 7 |
| Advanced Functional Materials fm.202005093 | 2 | 1 / 1 | 0 / 1 / 1 |
| Advanced Materials ma.201300071 | 2 | 0 / 2 | 0 / 0 / 2 |
| Bioactive Materials .2019.01.001 | 1 | 1 / 0 | 0 / 1 / 0 |
| Journal of Advanced Ceramics 5-019-0334-4 | 9 | 8 / 1 | 2 / 0 / 7 |
| Rare Metals 8-012-0515-6 | 4 | 3 / 1 | 2 / 0 / 2 |
| **total** | 38 | 22 / 16 | 4 / 9 / 25 |

## Per root

| root | v2.2 open / closed | with --v1-filters open / control / closed |
|---|---|---|
| infer | 19 / 5 | 3 / 7 / 14 |
| explain | 3 / 6 | 1 / 2 / 6 |
| intervene | 0 / 2 | 0 / 0 / 2 |
| generate | 0 / 3 | 0 / 0 / 3 |

## What still closes under v2.2

- Acta Materialia T1 (infer/estimate): not derivable from given panels: o4: text, not in given captions: ['b,c are the strain-free calculation from the exact grain shape (caption)
- Acta Materialia T9 (infer/compare): not derivable from given panels: o14: text, not in given captions: ['Lab cycle = average over many (111) grains, Syn cycles = the single gra
- Advanced Energy Materials T1 (infer/rank): not derivable from given panels: o1: text, not in given captions: ['GO volumes 5/10/20 mL (F1 linked text)']
- Advanced Energy Materials T2 (intervene/next condition): decision 10.0 is not the condition directly after the last given (None)
- Advanced Energy Materials T1 (infer/compare): panel_modality: o6 is SEM but F4b reads as electrochemistry
- Advanced Energy Materials T2 (infer/estimate): panel_modality: o7 is SEM but F4b reads as electrochemistry
- Advanced Energy Materials T3 (explain/rejection): panel_modality: o8 is SEM but F4b reads as electrochemistry
- Advanced Energy Materials T4 (explain/rejection): not derivable from given panels: o18: text, not in given captions: ['panel a/c = Ni-MOF, panel b/d = NixPyOz (captions)']
- Advanced Energy Materials T5 (explain/rejection): not derivable from given panels: o17: text, not in given captions: ['sample identity (caption)']
- Advanced Energy Materials T6 (explain/mechanism): mechanism trace with no shown evidence: nothing to observe
- Advanced Energy Materials T7 (generate/design under constraint): no oracle for PROCESS: gate 2 closes the root
- Advanced Functional Materials T2 (generate/design under constraint): no oracle for PROCESS: gate 2 closes the root
- Advanced Materials T1 (explain/mechanism): not derivable from given panels: b10: text, not in given captions: ['Electrons reach the NCs through the conducting graphene, Li+ through mi
- Advanced Materials T2 (generate/design under constraint): no oracle for PROCESS: gate 2 closes the root
- Journal of Advanced Ceramics T9 (intervene/next condition): not derivable from given panels: g1: source inferred
- Rare Metals T4 (explain/mechanism): mechanism trace with no shown evidence: nothing to observe

By rule: {'not derivable from given panels': 7, 'decision 10.0 is not the condition directly after the last given (None)': 1, 'panel_modality': 3, 'mechanism trace with no shown evidence': 2, 'no oracle for PROCESS': 3}

Traces the v1 filters would have removed that are open now: 18. Each carries `v1_filter` with the ruling the filter would have made, for the gate comparison in part 4.
