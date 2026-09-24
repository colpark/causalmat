# Matcher findings against the frozen validation set

The validation set in `trace_kit_v3/validate_decompose.py` is **frozen** as of 2026-09-23, after two
corrections made before the freeze (both recorded in that file's docstring and in `docs/TRACES_V3.md`):

1. Unsatisfiable figure-level rows. `KNOWN` had been `our_claims_from_those_figures` -- every claim
   our graph reads from the figures a hop cites. adfm M4 demanded n21 (*atmospheric ageing*) for a
   hop about domain size; Biomaterials M4 offered n24 ("ALP activity does not differ") as proof of
   "improved osteogenesis", which cuts against it. Both became `must_not`.
2. adfm M3, underdetermined by the effect text. Widening the row was refused as a fix; the
   ambiguity became the attachment-reach measure instead.

From this point the rows, the must-not sets and the pass conditions do not change. Where the
matcher disagrees with a row, the disagreement is logged here and the test still fails.

Every verdict is model against model.

## Findings

_(none yet; post-fix run pending)_
