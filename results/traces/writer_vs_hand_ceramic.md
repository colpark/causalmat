# Writer versus hand: ceramic twelve — run 1

Every verdict here is model against model: the writer is a Sonnet subagent (net-writer, no tools), the structural nets are code, and the reference is the hand-written fixture. No human checked any item.

| T | status | hidden target named (hand / writer) | grader node named (hand / writer) | numbers in key (hand / writer) | unsourced (writer) | answer_key_nodes (hand / writer) | verdict (hand / writer) |
|---|---|---|---|---|---|---|---|
| T1 | control | 1/1 / 1/1 | n/a / n/a | - / 2 | - | q18, r2 / r2 | survives (control) / survives (control) |
| T2 | closed | 0/1 / 1/1 | n/a / n/a | 1 / 1, 2, 3, 50, 100 | - | - / - | closed / closed |
| T3 | closed | 1/1 / 1/1 | n/a / n/a | 2 / 2, 50, 100 | - | - / - | closed / closed |
| T4 | open | 0/2 / 2/2 | n/a / n/a | 0, 2 / 0, 2, 20, 25 | - | - / q9, r10 | survives / survives |
| T5 | open | 1/2 / 2/2 | yes / yes | 0, 10, 15, 20, 25, 91.7, 94.9, 96.4, 97.6, 98.5 / 0, 2, 15, 20, 25, 91.8, 96.4, 98.5 | - | r10, r3 / q10, r3 | survives / flagged [leak] |
| T6 | open | 0/2 / 2/2 | n/a / n/a | - / 0, 20, 25 | - | - / q14, r10 | survives / survives |
| T7 | open | 0/1 / 1/1 | n/a / n/a | - / 2 | - | - / q15, s5 | survives / flagged [leak] |
| T8 | control | 1/1 / 1/1 | n/a / n/a | 20, 25 / 7, 20, 25 | 7 | q19, r9 / r9 | survives (control) / flagged (control) [provenance] |
| T9 | open | 2/2 / 2/2 | n/a / n/a | 2, 15, 20 / 1, 2, 15, 20 | - | q11, q15, r3, r8 / q11, q15 | survives / survives |
| T10 | open | 1/2 / 2/2 | n/a / n/a | - / 2 | - | - / q11, q15 | survives / survives |
| T11 | open | 1/1 / 1/1 | no / yes | 1, 2, 6.05, 15, 17.1, 20, 655 / 0, 1, 2, 4.3, 6.0, 6.05, 12.6, 15, 16.0, 17.1, 20, 25, 91.8, 96.4, 98.5, 505, 568, 655 | - | q17, r8 / q10, q17, r8 | survives / survives |
| T12 | closed | 1/1 / 1/1 | n/a / n/a | 30, 40, 1550 / 30, 40, 1550 | - | - / q5 | closed / closed |

Columns. *Hidden target named*: of the nodes the validator treats as the graded target, how many the key cites (by id in the text or in `answer_key_nodes`). *Grader node named*: when the `grader` field names a held-out node (T5 r3, T11 r8), whether the grading note names it. *Numbers*: every number `validate_traces.nums` pulls from the key; it includes formula digits (the 2 in ZrSi2, the 1 and 2 in m^1/2), so treat short digits as noise. *Unsourced*: numbers in the writer's key that appear in no source label (the `provenance` net).

## How this run was done

- 12 dispatches of `net-writer` (Sonnet, no tools; tools check in `subagent_tools_check.txt`, run 2), one per trace. Packets in `results/traces/writer/ceramic_run1/<T>.writer.txt`, replies verbatim in `<T>.writer.out.txt`.
- **Leave-one-out exemplars.** `trace_kit/fixtures/writer_exemplars.json` holds the hand-written ceramic twelve, and all 12 of its answer keys match the fixture exactly. Passing the whole file would give the writer the answer to the trace it is writing, so each ceramic packet drops the exemplar with the same id (`writer_packets.py build --loo`). The other 11 exemplars are still same-paper siblings, so the writer can borrow wording from siblings. That makes this diff an optimistic bound on the writer, not an independent test.
- **Compacted exemplars.** Exemplars are passed without their `linear`/`walk` step lists (question, key, grading, mask, grader, hidden, evidence kept). The writer has no Read tool, so each packet is relayed inline, and the step lists doubled the packet size without bearing on the fields the writer writes.
- **Relay checked.** `trace_kit/harvest.py` takes the reply from each subagent transcript and compares the prompt the subagent received with the packet file byte for byte: 12 of 12 exact. The first harvester took the last handback call; T9's writer called it twice (the second call was refused by the harness), so the harvester now keeps the first. Fixed before the numbers above were produced.

## Reading

**Provenance: 1 of 12 fails (T8). Under the 2-of-12 threshold, so `net-writer.md` is not tightened and there is one run.** The failure is the writer citing the panel by name ("On F7, ..."): the 7 is a figure number, not a quantity, but the net counts it as an unsourced number. The rule treats it as a failure, and here it looks like the net is too literal, not that the writer made up a value.

**What the writer changed, relative to hand:**

1. *Longer, and the question restates the context.* The hand questions are one or two sentences that assume the packet carries the context. The writer's questions repeat the context in prose (T5, T7, T11). That is harmless where the context is already given (T5, T11) and harmful in T7.
2. *Leaks the hand version avoids.* The leak net flags two:
   - **T7** (mechanism) hands over the thermal-mismatch premise (s5) and frames it as a rival ("why isn't the thermal-expansion-mismatch stress by itself enough"). The hand key counts thermal mismatch as part of the answer, so the question gives part of the answer away. Caught (bigrams: thermal expansion, expansion mismatch, crack path).
   - **T5** (rank, graded by the density channel r3) asks for the hidden claim itself: "how does relative density change ... at which composition does it peak". The hand question asks for a porosity rank from the images and holds the density series back as an independent check. The writer's version turns an image-to-rank item into "recall the density curve", and its key uses q10's 91.8 where the channel r3 reads 91.7. Caught (bigram: relative density).
   - **T4** is a miss by the leak net. The writer's question asks "is there a threshold where SiC switches from submicron to nanometre scale?", which gives away the answer's two size classes. It shares no bigram or number with the hidden labels, so the net passes it. This is a false negative, recorded for step 2.
3. *Keys are fuller and cite nodes.* The writer fills `answer_key_nodes` on every trace. The hand fixture leaves it null on 7. Target coverage rises from 7/14 to 14/14 cited target nodes on non-closed traces, mostly because the writer cites what the hand key only paraphrases.
4. *Keys go beyond the graded item.* T11's key adds the 25 vol% outcome and the whole q10 density series, and T9's cites no held-out channel. The hand key for T9 cites r3/r8 so that the 15-versus-20 mismatch is the required reason. The writer puts that reason in the key text but leaves r3/r8 out of `answer_key_nodes`.
5. *Grading notes name the grader node where one exists* (T5 r3, T11 r8). Hand T11's note says "from F7" rather than r8. On this column the writer is more complete than hand.
6. *Closed traces (T2, T3, T12)* keep the hand ruling. The writer repeats the label content more fully, including numbers (50-100 nm, 1550 C / 30 min / 40 MPa), all of them sourced.
7. *Controls (T1, T8)* keep the hand ruling ("not resolvable"). The writer drops q18/q19, which are not in its packet, since the cut trace does not reference them. The hand keys cite nodes outside the trace record.

**Carried into step 2.** The writer is used unchanged. Provenance failures get the one rewrite the plan specifies. Leak flags are counted in `stage1_summary.json` but, per the plan, are not rewritten, so they will show up as structural flags. The T4-type leak (the answer's categories given away in the question) gets past the leak net and will reach the nets in step 4 unflagged.

## Run 2 of the nets (same writer outputs, changed `validate_traces.py`)

The questions and keys are the run-1 outputs, unchanged; only the nets changed.
- **Content-word leak test** (`validate_traces.py:31-36`): the stemmed 5+ letter words of the graded targets that appear in no given node label, intersected with the stemmed words of the question. Fails if the intersection is non-empty.
- **Number extraction** (`validate_traces.py:9-10, 73-74`): figure refs (`F7`, `F8a-e`, `F6a-F6e`) are stripped before numbers are extracted. The node-id strip used to cover only `q/r/s` ids and now covers every id in the graph, so `o7` or `a15` in another paper's key is no longer an unsourced 7 or 15. `grader_nodes` (`:70`) is widened the same way.

| T | content words, hand | content words, writer run 1 | writer provenance | writer verdict |
|---|---|---|---|---|
| T1 | - | composition, intensity, threshold, trend | pass (missing -, coverage 0.79) | flagged (control) [leak] |
| T4 | - | fracture, nanometre, particl, submicron | pass (missing -, coverage 0.69) | flagged [leak] |
| T5 | fracture | density, fracture, relative | pass (missing -, coverage 0.57) | flagged [leak] |
| T6 | fracture | fracture | pass (missing -, coverage 0.77) | flagged [leak] |
| T7 | - | expansion, mismatch, thermal | pass (missing -, coverage 0.57) | flagged [leak] |
| T8 | - | - | fail (missing -, coverage 0.41) | flagged (control) [provenance] |
| T9 | - | - | pass (missing -, coverage 0.74) | survives |
| T10 | - | - | pass (missing -, coverage 0.54) | survives |
| T11 | - | - | pass (missing -, coverage 0.41) | survives |

**As expected:** T4's writer question now fails `leak` on `submicron` and `nanometre` (plus `particl` and `fracture`). The bigram test missed it.

**Not as expected:** T8's provenance still fails. The figure ref is gone (`missing_numbers` is empty), but the net also requires word coverage ≥ 0.5 or at least three sourced numbers, and the key's coverage is 0.41 with two sourced numbers. The rule is left as it is. T8 is a control, and the step-2 rewrite gives it one more pass.

**The content-word test also fires on the hand fixture:** hand T5 and T6 on `fracture`. The hand questions say "fracture-surface SEM panels", which describes the panels, and no given node carries the word, so it counts as hidden-only. That is a false positive of the rule as specified.

**Stop rule check, content-word test on all writer traces so far** (ceramic run 1 plus Acta_Materialia 2014 run 1, both written before the new rules): 13 of 17 non-closed traces are flagged by the content-word test alone. The hand twelve: 2 of 9. That is more than half, so the stop rule applies: nothing is blocked on this test until the given-node exclusion is checked. Two causes are visible in the flagged words:
1. The stemmer (`(ing|ed|es|s)$`) splits word families: `cycle`/`cycling`, `retrieved`/`retrieval`, `measure`/`measured` get different stems, so a word the given nodes use still counts as hidden-only.
2. Panel vocabulary is not in any given node. The packet's `read` step names the panels, but their content words (`fracture`, `phase maps`, `lattice strain`) live only in the hidden observation, so any question that names what the panel shows gets flagged.

Some flags are real, and the run-1 writer did restate hidden content: Acta T3 names the hysteresis loop and the ideal thermo-elastic line, Acta T5 gives the 50 and 240 C breakpoints (also caught by the number test), ceramic T7 names the thermal mismatch. So the test finds things the bigram test misses, but as it stands it cannot tell those from the paper's own vocabulary.

Every verdict here is model against model; no human checked any item.
