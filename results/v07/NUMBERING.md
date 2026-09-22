# v07 fix 1: the figure-numbering lookup

Every verdict is model against model.

`fig_by_number` (cut_traces.py, validate_traces.py) resolves a packet id `F<n>` by the figure's position in
`data.json` `image_info`, the way the packet numbers them. The old code used `match.json` `figure_number`, which
repeats or skips when a paper has a scheme or an unnumbered figure.

`results/v07/numbering_affected.json` lists every paper whose two lookups differ, the figure numbers that shift, and
every open trace whose given panel ids change under the fix.

- **22 papers shift** among the 79 with a cut. For each, the file records `figures_shifted` and `traces_changed`.
- **17 open traces** would take different crops. **All 17 are in papers cut after the fix**, so their cuts already used
  the corrected lookup and their crops are right.
- **Papers cut before the fix: 9.** Five were re-cut in part G (ACHM s42114-021-00366-2, AEM 1601491,
  Bioactive 2020.02.005, POC 2016.09.010, AEM 201501833), which re-ran 3 traces on corrected crops (ACHM T1, T3, T4)
  and reopened 6 traces the wrong crops had closed. The other four (MatChar 2015.10.016, MatChar 2017.11.052,
  AFM 202005093, Bioactive 2019.01.001) have **no open trace citing a shifted figure**.
- **Nets:** re-running `validate_traces.py` on the two of those four that have written items changes no net result.

**Nothing was left to re-run: 0 traces, 0 verdict changes.** The part G re-run already covered the bug's reach, and the
stop rule (verdicts changing on more than a third of re-run traces) does not apply.
