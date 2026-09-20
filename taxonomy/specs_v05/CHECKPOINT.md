# Part 3 checkpoint: collapse script against the hand-built specs

`collapse_modality.py` run on rank 3 (`10.1002_adma.201404945`, kit `photo_spec.json`) and rank 7
(`s40145-019-0334-4`, kit `ceramic_spec.json`), diffed node by node with `diff_specs.py`
(match key: target state + lane + figure set).

**Agreement on matched nodes: lane 6/6, target state 6/6.** Verdict and necessity agree on 3 of 6, and the
panel sets never agree in string form. Every difference is explained below; nothing is left open.

## Fixed in the script (5 bugs the diff caught)

1. **Lane by modality, not by label mention.** An EDS spectrum whose label mentioned TEM ("The EDS inset
   assigns Pb and S lines…") landed in the microscopy lane. A spectrum, curve or map is now classical
   whatever the label says, and only XAS reaches the `spec` lane.
2. **Classic nodes split per claim**, not one per state, per the written rule "one per (lane, target state,
   claim)".
3. **Merged verdict takes the worst case** (`contradicts` > `not_shown` > `partial` > `shown`) instead of the
   most common value, so merging never upgrades a partial read.
4. **Panel ids deduplicated**, keeping order; a merged node was repeating `#F2a` once per member.
5. **Necessity**: a node with no `shown` member is `redundant` when its claim keeps other shown support, and
   `decorative` only when the claim has no other figure-backed support at all. It was calling the first case
   decorative.

Also added, and reported rather than hidden: **211 of 432 evidence nodes carry no `attrs.technique`** (16 of 32
graphs never set it). The family is then read from the node's own label with the part-1 rule table, and failing
that from the node's `modality` field as the placeholders `MICRO`/`DIFF`. Every lane node records
`tech_source` as `attrs`, `label`, `modality` or `none`.

## Where the hand version is wrong instead

1. **Stale verdicts.** Photo M2 is `partial` in the graph, `shown` by hand; ceramic C1/C6 likewise; photo C2/C6
   is `shown` in the graph, `partial` by hand. The hand specs predate the v05 judge pass, which re-read the
   crops and moved several reads.
2. **A state the graph does not have.** `ceramic_spec.json` carries an S3 performance state, but that graph's
   spine has no PRF node at all (STR 4, DES 3, PRP 3, HYP 2, MEC 2, PRC 1, DSC 1). The script emits four states
   and the hand five, which also shifts every row id after S2.
3. **Optical microscopy placed in the `micro` lane** (photo M3, "Microscopy: SEM, TEM, optical"). The written
   lane definition is micro = SEM, TEM, so the script files optical evidence as classical.
4. **Classic evidence merged by instrument, not by claim** ("I-t curves" folding F2, F3 and F4 across two
   different spine claims). The rule keys on the claim.
5. **Necessity judged within a lane.** Ceramic M2/M7 is `necessary` by hand, but the removal test counts every
   figure-backed `shown` node whatever its lane, and that claim keeps support from r8, r9 and r11.

## Expected, not a fault on either side

**Panel strings never match**: the hand specs name panels in prose ("F1 inset", "F5 zones A, B", "F2, F3a, F3c,
F4c to e") while the script emits canonical ids (`10.1002/adma.201404945#F1a`). The ids are the field the kit
README adds for verification, and they are what part 4 checks against the store.

**Node counts differ** (photo 10 vs 7, ceramic 10 vs 7) as a consequence of the per-claim split above.

## Status

The diff is clean in the sense the checkpoint asks for: every remaining difference is either a rule the script
follows and the hand version does not, or a hand-side error named above. **The other 30 papers have not been
run**, per the instruction to stop here.
