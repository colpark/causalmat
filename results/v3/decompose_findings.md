# Matcher findings against the frozen validation set

The validation set in `trace_kit_v3/validate_decompose.py` is **frozen** as of 2026-09-23, after two
corrections made before the freeze (recorded in that file's docstring and in `docs/TRACES_V3.md`):

1. **Unsatisfiable figure-level rows.** `KNOWN` had been `our_claims_from_those_figures` -- every
   claim our graph reads from the figures a hop cites. adfm M4 demanded n21 (*atmospheric ageing*)
   for a hop about domain size; Biomaterials M4 offered n24 ("ALP activity does not differ") as
   proof of "improved osteogenesis", which cuts against it. Both became `must_not`.
2. **adfm M3, underdetermined by the effect text.** Widening the row was refused as a fix; the
   ambiguity became the attachment-reach measure instead.

From this point the rows, the `must_not` sets and the pass conditions do not change. Where the
matcher disagrees with a row, the disagreement is logged here and the test still fails.

Every verdict is model against model.

## Honest positive count

Six known-positive rows, of which **one is contaminated**: Nano Letters M1 is the mesopores case,
which appears verbatim as the worked example inside `net-decompose.md`. Its pass is partly a
training case and is reported separately.

- **Five clean positives**: adfm M3, adfm M4, Biomaterials M4, Nano Letters M2, Nano Letters M3.
  Plus the two Rare Metals rows (M1 -> s6, M1 -> s1), also clean.
- **Post-fix: 4 of the 5 clean pass, 6 of 7 counting Rare Metals.** Nano Letters M3 fails.
- Nano Letters M1 (contaminated) passes; it is not counted in the above.

## Finding 1 -- Nano Letters M3 is nondeterministic, and fails

The row requires n17, "Co3O4 is far less Na-active than Li-active (degree of oxidation ~36% vs
~91% at 2 ps)", the same fact as the hop's effect measured spectroscopically.

The completeness rule was meant to fix exactly this, and it does -- **about a third of the time.**
Six runs of the byte-identical prompt against the fixed agent:

| run | returned n17 | claims |
|---|---|---|
| probe 1 | yes | n7, n8, n17, n20 |
| batch run (harvested) | no | n1, n7, n8, n20 |
| probe A | no | n1, n8 |
| probe B | yes | n1, n7, n8, n17, n20 |
| probe C | no | n7, n8, n20 |
| probe D | no | n7, n8, n20 |

**2 of 6.** The prompts were verified byte-for-byte against the job files by transcript harvest, so
this is run-to-run variance in the matcher, not a stale agent definition or a relay fault. The runs
that miss n17 still reason explicitly about a "general/thesis-level" claim and the "specific cycling
data" (n7/n8) -- they apply the completeness rule, but to the electrochemical pair only, and never
consider the XAFS statement as a third expression of the same fact.

The row stands. The matcher fails it.

## Finding 2 -- three hops land on claims with no evidence, and two had somewhere better to go

Unreachable hops, by name: **Rare Metals M2**, **adfm M3**, **adfm M4**. All three are matched but
not attachable. Two of the three are also completeness misses -- a supported claim sits one edge
away and the matcher did not return it:

| hop | landed on | nearer attachable claim (d=1) |
|---|---|---|
| Rare Metals M2 | p3, c1 | s2: La forms a new Al6Cu6La phase at dendrite boundaries |
| adfm M3 | n2, n19 | n13: emission below 150 K ranks with crystalline state; n14: transition temperature rises as domain size grows |
| adfm M4 | n2, n19 | n13, n14 as above |

adfm M3/M4 are the same pair of abstract claims (n2 = HYP, n19 = DSC) reached by both hops, which
is the thesis-level landing the completeness rule was written to prevent. It is prevented
inconsistently.

## Finding 3 -- discrimination now fails

3.06 claims per hop against a frozen limit of 3 (49 matches over 16 hops). Pre-fix it was 2.94.
The completeness rule bought recall and spent the discrimination budget: the pair rate is still
comfortable at 49/288 = 17.0% against a 50% limit, but the per-hop mean is over.

This is a real tension, not a threshold to nudge: the same rule that adds the specific measured
claim beside the general one necessarily raises claims per hop. The limit is frozen, so the run
fails.

## Where support is read from (instruction 2)

`support.py` is now the single place claim-level support is derived, from a **direct `evidences`
edge out of an observation node carrying panels -- one step, no paths through intermediate claims**,
and never from a claim node's own `image_support` field.

v3 sites that had read support off claims, and their recomputed values:

| site | before | after |
|---|---|---|
| `reach.py` attachable | 7/16 (claim `image_support`) | **13/16** |
| `validate_decompose.py` attachment reach | 7 reach / 9 text-only | **13 reach / 3 text-only** |

`stitch.py` already read `image_support` from OBS nodes, which is correct, so it was not rewired.
It does however count `qualifies` / `contrasts` / `rules_out` edges as evidence alongside
`evidences`: 42 evidence entries across the five papers, of which **36** are `evidences`. The other
6 are caveats. That metric is left as it is -- the v2 caveat rule depends on it -- but it is not the
same definition reach uses, and the two should not be quoted against each other.
