# Where the disagreements came from

When the collapse script was checked against the kit's two hand-built specs (part 3 checkpoint, see
[`taxonomy/specs_v05/CHECKPOINT.md`](../taxonomy/specs_v05/CHECKPOINT.md)), the two sides agreed on lane and
target state for every matched node but differed on verdict, necessity, node count and panel strings.

Every difference traces to one of four places. Only the first is the new code.

## 1. The collapse script (new code, part 2)

All five script-side bugs. Each was fixed and the fix is in `taxonomy/collapse_modality.py`:

| Bug | Effect |
|---|---|
| lane chosen from label mentions | a chemical spectrum filed as microscopy because its caption named an electron microscope |
| classic lane keyed per state | evidence for two different claims folded into one node |
| merged verdict took the most common value | merging could upgrade a `partial` read to `shown` |
| panel ids not deduplicated | a merged node repeated the same id once per member |
| necessity called a no-`shown` node decorative | it is `redundant` when the claim keeps other support |

**This is what the checkpoint is for.** It found them before 30 more papers were run on the bad rules.

## 2. Timing: the hand examples predate the judge pass

Three hand-side differences are stale verdicts — `partial` where the graph now says `shown`, and the reverse.
The hand specs were written from the graphs *before* the v05 judge pass re-opened the crops and moved several
reads. Nobody was wrong at the time; the evidence moved underneath the reference.

**Fix for the pipeline:** build hand references after a judge pass, never before, or re-derive them when the
graphs change.

## 3. Definition drift between the kit and the written rules

Two hand-side differences:

- **optical microscopy in the `micro` lane.** The kit example labels that lane "Microscopy: SEM, TEM, optical";
  the written rule says micro = SEM, TEM. The script follows the written rule and files optical as classical.
- **classic evidence grouped by instrument** ("I-t curves" spanning three figures and two different claims)
  where the rule keys on the claim.

**Fix for the pipeline:** when a worked example and the written rule disagree, the later explicit instruction
wins, and the example should be regenerated from it rather than left as a second source of truth.

## 4. The graph-writing step (the v05 staff agents)

Two structural problems, both upstream of anything the collapse does:

- **Half the graphs never recorded the instrument.** 211 of 432 evidence nodes carry no `attrs.technique`, and
  16 of 32 graphs never set it once, because `PROTOCOL.md` does not require the field. The lanes are the whole
  point of the modality view, so the script falls back to the node's label, then to its `modality` field with
  `MICRO`/`DIFF` placeholders, and records `tech_source` on every lane node (`attrs`, `label`, `modality` or
  `none`) so the provenance stays visible.
- **A state the graph does not contain.** `ceramic_spec.json` has a performance column, but that paper's spine
  has no PRF node at all (STR 4, DES 3, PRP 3, HYP 2, MEC 2, PRC 1, DSC 1). The hand picture and the graph
  disagree about what the paper contains, which also shifts every row id after S2.

**Fix for the pipeline:** make `technique` required when a graph is written, and derive every downstream
picture from the graph rather than from a parallel reading of the paper.

## Not an error on either side

The hand specs name panels in prose ("F1 inset", "F5 zones A, B", "F2, F3a, F3c, F4c to e"); the script emits
canonical ids (`10.1002/adma.201404945#F1a`). The ids did not exist when the kit was written — they come from
the panel store, which is newer — and they are what the verification step checks against the store.

## Summary

| Cause | Differences | Where the fix belongs |
|---|---|---|
| new collapse code | 5 | fixed in this pass |
| stale hand reference | 3 | regenerate references after judging |
| kit vs written rule | 2 | one source of truth for the rules |
| graph-writing step | 2 | require `technique`; derive pictures from graphs |
| panel naming convention | all panel strings | expected; ids are the newer field |

The two fixable causes are upstream, not in the code written today.
