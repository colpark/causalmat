# Cutter v2.1 on the v06b graphs

Rule 3 now grades the right target and counts the given captions as seen. Seeding is lane-level: a trace is seeded where removing every evidence node of an FM family leaves the claim with no shown support. Node-level necessity is kept only as a recorded field (`node_necessity`).

Every verdict is model against model: the graphs, sources and requires_unseen facts are staff/judge output, and the cutter only applies rules to them.

## Traces per paper

| paper | trace | root / subtype | status | ruling | graded targets |
|---|---|---|---|---|---|
| Acta Materialia | T1 | infer / estimate | closed | not derivable from given panels: o4: text, not in given captions: ['b,c are the strain-free calculation from t | o4 fail |
| Acta Materialia | T2 | infer / estimate | control | depth one and not an image read: negative-control stratum | o5 pass |
| Acta Materialia | T3 | infer / estimate | control | depth one and not an image read: negative-control stratum | o6b pass |
| Acta Materialia | T4 | infer / rank | control | depth one and not an image read: negative-control stratum | o6 pass |
| Acta Materialia | T5 | infer / rank | control | depth one and not an image read: negative-control stratum | o8 pass |
| Acta Materialia | T6 | infer / estimate | control | depth one and not an image read: negative-control stratum | o10 pass |
| Acta Materialia | T7 | infer / rank | control | depth one and not an image read: negative-control stratum | o11 pass |
| Acta Materialia | T8 | infer / estimate | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Acta Materialia | T9 | infer / compare | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Acta Materialia | T10 | infer / estimate | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Acta Materialia | T11 | infer / rank | control | depth one and not an image read: negative-control stratum | o7 pass |
| Advanced Energy Materials | T1 | infer / rank | closed | not derivable from given panels: o1: text, not in given captions: ['GO volumes 5/10/20 mL (F1 linked text)'] | o1 fail |
| Advanced Energy Materials | T2 | intervene / next condition | closed | decision 10.0 is not the condition directly after the last given (None) |  |
| Advanced Energy Materials | T1 | infer / compare | open |  | o6 pass |
| Advanced Energy Materials | T2 | infer / estimate | open |  | o7 pass |
| Advanced Energy Materials | T3 | explain / rejection | open |  | o8 pass |
| Advanced Energy Materials | T4 | explain / rejection | closed | not derivable from given panels: o18: text, not in given captions: ['panel a/c = Ni-MOF, panel b/d = NixPyOz ( | o18 fail |
| Advanced Energy Materials | T5 | explain / rejection | closed | not derivable from given panels: o17: text, not in given captions: ['sample identity (caption)'] | o17 fail |
| Advanced Energy Materials | T6 | explain / mechanism | closed | mechanism trace with no shown evidence: nothing to observe |  |
| Advanced Energy Materials | T7 | generate / design under constraint | closed | no oracle for PROCESS: gate 2 closes the root |  |
| Advanced Functional Materials | T1 | explain / rejection | control | plot read, no domain model: depth-one negative control | o23 pass |
| Advanced Functional Materials | T2 | generate / design under constraint | closed | no oracle for PROCESS: gate 2 closes the root |  |
| Advanced Materials | T1 | explain / mechanism | closed | not derivable from given panels: b10: text, not in given captions: ['Electrons reach the NCs through the condu | b10 fail |
| Advanced Materials | T2 | generate / design under constraint | closed | no oracle for PROCESS: gate 2 closes the root |  |
| Bioactive Materials | T1 | explain / rejection | control | plot read, no domain model: depth-one negative control | b8 pass |
| Journal of Advanced Ceramics | T1 | infer / classify | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Journal of Advanced Ceramics | T2 | infer / compare | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Journal of Advanced Ceramics | T3 | infer / classify | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Journal of Advanced Ceramics | T4 | infer / classify | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Journal of Advanced Ceramics | T5 | infer / classify | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Journal of Advanced Ceramics | T6 | infer / rank | open |  | o9 pass |
| Journal of Advanced Ceramics | T7 | infer / estimate | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Journal of Advanced Ceramics | T8 | explain / mechanism | open |  | m2 pass |
| Journal of Advanced Ceramics | T9 | intervene / next condition | closed | not derivable from given panels: g1: source inferred | g1 fail, o12 pass |
| Rare Metals | T1 | infer / rank | open |  | o1 pass |
| Rare Metals | T2 | infer / estimate | closed | bare infer: no rejection, no budget, no stopping rule |  |
| Rare Metals | T3 | infer / rank | open |  | o8 pass |
| Rare Metals | T4 | explain / mechanism | closed | mechanism trace with no shown evidence: nothing to observe |  |

Totals: {'closed': 22, 'control': 9, 'open': 7}. Traces with a graded target: 22; closed on rule 3: 6 (27%). The stop rule (more than half) does not fire.

Rule firings across all traces: {'R1': 3, 'R3': 24, 'R4': 8, 'R5': 13, 'R6': 7, 'R7': 3, 'seed': 26}. Each firing is recorded per trace in `v2_rules` with its `cut_traces.py` line.

## requires_unseen facts behind the rule 3 closures (results/v06b/knowledge_pile.json)

- Acta Materialia T1: {"o4": ["b,c are the strain-free calculation from the exact grain shape (caption)"]}
- Advanced Energy Materials T1: {"o1": ["panel-to-sample mapping a = Cu2S, b-d = RGO-Cu2S-1/-2/-3 (caption)", "GO volumes 5/10/20 mL (F1 linked text)"]}
- Advanced Energy Materials T4: {"o18": ["panel a/c = Ni-MOF, panel b/d = NixPyOz (captions)"]}
- Advanced Energy Materials T5: {"o17": ["sample identity (caption)"]}
- Advanced Materials T1: {"b10": []}
- Journal of Advanced Ceramics T9: {"g1": ["vol% levels behind sample names RZSZ-x (text)"], "o12": []}

## Changes in this step

- R3 caption match: identifiers (sample names, formulas, numbers with units) must appear in the given panel spans or figure preamble. LaTeX in the OCR spans is compacted first. When the target's own label uses some identifiers, only those count, so a caption mapping that also lists panels not given does not fail the target.
- Intervene levels: these are the sweep label's first number list with its unit. A panel's level is read as number+unit, or through a sample stem only when the label ties the first and last levels to that stem (RZSZ-0 to RZSZ-25). A panel with an unreadable level is withheld. This fixes AEM 2013, where RGO-Cu2S-3 had been read as level 3 and the 10 and 20 mL panels were handed over.
- Explain/mechanism traces with no shown evidence are closed instead of crashing (AEM 2015 T6, Rare Metals T4). An R1 joint-cause mechanism with no support is closed the same way.
- The ceramic v1 regression still reports 0 differences.
