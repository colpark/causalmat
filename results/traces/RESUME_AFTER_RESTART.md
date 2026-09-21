# Resume after session restart (trace validation, 2026-09-20)

Every verdict here is model against model; no human checked any item.

## Why the stop
`net-writer.md` got three new rules (commit "Writer rules: ..."). A `net-writer` dispatched after the edit, asked to quote
its Rules, returned only the old four: the agent registry is read at session start. The new rules reach the writer only
after a restart. Part C (retroactive rewrite) and the rest of step 2 both need writer dispatches, so both wait.

## Done
- Step 0 (tools check, run 2 passed), step 1 (ceramic writer + diff), Acta_Materialia 2014 writer run 1.
- A: rules + `trace_kit/fixtures/writer_exemplars_negative.json`; `writer_packets.py` passes the negatives, and takes
  `--only T1,T2` and `--feedback <json {T: text}>` for rewrites.
- B: content-word leak test; figure refs and all graph node ids stripped before number extraction (file:line in commit).
- C.1: `results/traces/rewrite_list.json`, 22 traces (ceramic 12, Acta_Materialia 2014 10).

## Open decision (stop rule hit)
The content-word test flags 13/17 non-closed writer traces so far and 2/9 hand traces. That is over the "more than
half" stop rule, so C.4 (block on a second leak failure) must not run on this test as it stands. Causes and evidence
are in `results/traces/writer_vs_hand_ceramic.md`, run-2 section: the crude stemmer, and panel vocabulary that is in no
given node.

## On restart, in order
1. Dispatch `net-writer`: "Quote the Rules section of your instructions verbatim, then stop." It must show 7 rules.
2. C.2: for each paper in rewrite_list.json, rename `<T>.writer.out.txt` to `<T>.writer.out.run1.txt`, rebuild the
   packets (`writer_packets.py build ... [--loo for ceramic]`), dispatch, harvest (`trace_kit/harvest.py` checks the relay
   byte for byte), merge into `results/traces/<paper>.traces.json`, validate. The ceramic packets use `--loo`.
3. Continue step 2 on the remaining 30 papers with the new rules. Commit and push after each paper.
4. C.4/C.5 once the content-word decision is made; then step 3 onward, unchanged.

## Session 2 (after restart): step 0 stopped
Content-word exclusion widened to panel caption spans, OCR cues and tokens, modality and technique, plus figure-level
entries and grader-named nodes (fix 1 and fix 2; see the run-3 section of `writer_vs_hand_ceramic.md`). Hand fixture:
0 flags. Written copy: T4 and T7 as required, plus **T1** (explain/rejection; intensity, threshold, trend), so the pass
condition failed after two fixes. Stopped per the stop rule. Steps 1 onward not started. The open decision: whether the
content-word test exempts explain/rejection traces the way the bigram test does.
