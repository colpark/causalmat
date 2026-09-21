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

## Session 2: where it stopped (user limit)
Step 0 passed (run 4, rejection exempt). Step 1 passed (run 3, seven rules). Step 2 (C.2) done for the ceramic paper only.
The user said to process only up to that paper. Acta Materialia 2014 (10 traces in rewrite_list.json) and the 30 remaining
papers were NOT processed; Acta's run-1 files are untouched. Steps 3-5 not started.

## Session 3 (2026-09-20): parts 1-3 done, part 4 stopped after 8 of 31 papers (stop-rule check)
Every verdict here is model against model; no human checked any item.
- Part 1 (cutter premise rule): ceramic re-cut differs from the fixture only in T7; 31-paper re-cut changes 2 of 139 hidden sets.
- Part 2 (content words and coverage as warnings); part 3 (ceramic closed: 0 of 12 fail a gate).
- Part 4: 8 papers written and validated (Acta 2014 through AFM 202005093), pushed per paper. Net fixes on the way,
  all "not a quantity" extraction bugs: 3-D and 1.35e-3 (one number), 'Figure 4a' / 'Fig. 5(c)', and digits glued to
  letters (ZrB2, m2/g). None changed a ceramic verdict.
- Stop-rule check after 8 papers: blocked 6 of 22 non-closed (27%); 1 of 7 status-open (14%); blocks whose leak comes
  from the question the writer wrote: 1 of 22 (5%). The other 5 blocks are given-context overlaps: the leak gate
  compares the hidden labels with the given labels as well as the question, and in 2 rejection traces the hidden
  ruling repeats the given claim's own numbers (the bigram and content-word tests already exempt rejection traces).
  No rewrite can remove those. Stopped for a decision (see the report in chat).
- Remaining: 23 papers, then stage1_summary.json, then step 3 onward.
