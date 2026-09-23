# Traces v2: support chains, five cases

**Every verdict is model against model, and the four-level ground truth is itself a model label.**
No item here has been checked by a person.

Branch `traces-v2/2026-09-23`, from `v07-scale/2026-09-21`. Nothing under `results/v07/`,
`trace_kit/` or `taxonomy/graphs_*` was modified; v1 stands for comparison.

## The run stopped. Two stop rules fired, and they share one cause.

- **The oracle-complete arm matched or beat the full arm on steps in three of five cases** (threshold: two).
- **Ground-truth disputes reached 14 of 21 graded steps, 67%** (threshold: one third).

The brief reads the second as "the graph's `image_support` labels are too unreliable to grade against".
That is not what the evidence shows, and the correction matters more than the rest of the run.

### The step question and the ground truth are asking different things

- The step asks: **what does this data contribute to the claim?**
- `image_support` records: **is this observation visible in this panel?**

Case 1 step 3 is the clean example. The DSC panel plainly shows a weak peak at ~605 C and a shoulder
at ~638 C, so `image_support: shown` is correct. The arm answered `partial`, because that panel does
not establish *"La forms a cubic NaZn13-type Al6Cu6La phase at dendrite boundaries; Sm forms none"*.
Both answers are right, to different questions.

The disputes are one-directional, which is what a semantic mismatch looks like and a noisy label does not:

| graph says | arm says | n |
|---|---|---|
| shown | partial | 12 |
| partial | shown | 1 |
| contradicts | partial | 1 |

The same fault explains the oracle result. The oracle hands over the observation text; when the graded
target is effectively the observation's own visibility, the delivery carries the answer. On case 4 the
oracle-complete arm scored **5/5** against the full arm's 2/5 - not because the oracle is generous, but
because the target collapsed onto what the oracle says.

Plan section 1 says ground truth is `image_support` **plus the edge relation**. The edge-relation half
works: the caveat rule added for case 4 (a node arriving by `qualifies`/`contrasts` is a caveat, not
support) produced the `contradicts` and `partial` levels correctly. The `image_support` half does not
carry claim-level sufficiency, because nothing in the graph records it.

**This is a plan-level decision and it is left open:** either add a per-step claim-contribution label
that does not exist today, or narrow the step question to "is this observation visible in this panel?",
which makes a perception item rather than the reasoning chain the redesign is for.

## 1. The five cases

| case | paper | claim | steps | channels | expected levels | closing |
|---|---|---|---|---|---|---|
| case1_three_techniques | Rare_Metals__s12598-012-0515-6 | `s2` | 3 | SEM, THERMAL, XRD | shown, partial, shown | partial |
| case2_annotated | Biomaterials__j.biomaterials.2011. | `n8` | 4 | PHYS, TEM, XRD | shown, partial, shown, shown | partial |
| case3_contradicts | Advanced_Functional_Materials__10. | `n14` | 4 | PL, XRD | shown, shown, partial, contradicts | partial |
| case4_oracle | Nano_Letters__10.1021_acs.nanolett | `n15` | 5 | ECHEM, XAS, XRD | partial, shown, shown, shown, shown | partial |
| case5_drop | Acta_Materialia__10.1016_j.actamat | `n11` | 5 | EBSD, OM, TEM | shown, partial, shown, shown, shown | partial |

Each carries its required feature: case 1 three techniques; case 2 an annotated panel (3 panels hidden
by saturation split); case 3 a `contradicts` step from audit `a3`; case 4 a partial oracle return from
audit `a2`; case 5 a dropped panel (`o15`, whose figure offers no crop) with the chain surviving on five
steps across three channels - the case v1 closed outright.

Oracle steps, dropped panels and necessity:

| case | oracle steps | dropped | necessity (channel-level structural leave-one-out) |
|---|---|---|---|
| case1_three_techniques | o5 | - | SEM=redundant by single loo, THERMAL=redundant by single loo, XRD=necessary |
| case2_annotated | o6 | - | PHYS=redundant by single loo, TEM=redundant by single loo, XRD=necessary |
| case3_contradicts | - | - | PL=necessary, XRD=redundant by single loo |
| case4_oracle | a2 | - | ECHEM=redundant by single loo, XAS=redundant by single loo, XRD=redundant by single loo |
| case5_drop | - | o15 | EBSD=redundant by single loo, OM=redundant by single loo, TEM=redundant by single loo |

Single leave-one-out marks most channels redundant, exactly as the plan warned it would: with every
panel present the evidence is dense and each channel individually looks removable. Only case 1's XRD
and case 3's PL come out necessary, both because they are the sole channel carrying the comparison the
claim needs. Greedy backward elimination on a calibration sample is the plan's answer and has not run.

## 2. Gate, per arm

| arm | steps correct | closings correct | parsed |
|---|---|---|---|
| full | 7/21 | 5/5 | 5/5 |
| floor | 2/21 | 3/5 | 5/5 |
| oracle_complete | 8/21 | 4/5 | 5/5 |
| no_image | 5/21 | 5/5 | 5/5 |
| permute_answer | 6/20 | 5/5 | 5/5 |
| permute_image | 0/11 | 0/5 | 3/5 |

Per case, steps then closing:

| case | full | floor | oracle_complete | no_image | permute_answer | permute_image |
|---|---|---|---|---|---|---|
| case1_three_techniques | 1/3 OK | 0/3 x | 1/3 OK | 1/3 OK | 1/3 OK | 0/3 x |
| case2_annotated | 1/4 OK | 1/4 OK | 0/4 OK | 1/4 OK | 1/4 OK | 0/4 x |
| case3_contradicts | 0/4 OK | 1/4 OK | 0/4 OK | 1/4 OK | 2/4 OK | 0/4 x |
| case4_oracle | 2/5 OK | 0/5 OK | 5/5 x | 1/5 OK | 2/5 OK | unparsed |
| case5_drop | 3/5 OK | 0/5 x | 2/5 OK | 1/5 OK | 0/4 OK | unparsed |

**`item_valid` under rule A (full beats floor on steps, and lands the closing): 2 of 5** -
cases 1 and 5. The floor behaves: 2 of 21 steps, and it misses the closing in 3 of 5.

**Rule A is vindicated.** `closing_alone_discriminates` is False on all five. Every text-only arm landed
the closing 4 or 5 times out of 5 while scoring 5/21 or worse on steps, because "partial" is one of four
levels and the prior favours it. A bench graded on the closing profile alone would have reported that the
images do not matter.

## 3. Alignment controls

| control | steps correct | closings correct | reading |
|---|---|---|---|
| permute_image | **0/11** | 0/5 | total collapse; two more arms answered CANNOT DETERMINE, which is the correct response to a swapped panel |
| permute_answer | 6/20 | 5/5 | near chance on steps; the closing survives, again showing the closing is not a discriminator |
| no_image | 5/21 | 5/5 | below the full arm's 7/21, above the floor's 2/21 |

**The controls degrade step scores to zero on the image permutation**, so that stop rule does not fire:
the items do use their pictures. The pattern the brief predicted - collapse on steps, closing
comparatively stable - is exactly what appeared, and is further evidence for rule A.

Per modality, `permute_image` scored 0 on every channel it parsed (XRD, SEM, THERMAL, PL, TEM, PHYS).
With three parsed controls there is no modality-level signal to separate yet.

## 4. Ground-truth disputes

**14 disputes over 21 graded steps (67%).**
Each is scored as the graph says and queued in `results/v2/gt_disputes.jsonl`. The three clearest:

**case1_three_techniques step 3 (`o5`, THERMAL:DSC) - graph `shown`, arm `partial`**

- graph observation: La alloy shows weak peak A (~605 C) and shoulder B (~638 C), assigned to Al2Cu and Al6Cu6La dissolution
- arm's reason: The reported DSC result (weak peak A ~605C and shoulder B ~638C in the La alloy) indicates an extra thermal event consistent with melting/transformation of an additional phase not present in a simpler eutectic system, supporting the existence of a distinct La-

**case1_three_techniques step 1 (`o2`, XRD) - graph `shown`, arm `partial`**

- graph observation: Extra reflections (stars, ~21-37, 50, 67 deg) appear only in the Al-Cu-Mn-La pattern; Sm pattern matches the RE-free one
- arm's reason: The XRD panel (F2) shows a star-marked peak set labeled 'Al5Cu6La' (note: figure legend gives Al5Cu6La, not Al6Cu6La as stated in the claim) present only in the Al-Cu-Mn-La trace and absent in both the Al-Cu-Mn-Sm and base Al-Cu-Mn traces, which supports 'La f

**case3_contradicts step 2 (`o12`, PL) - graph `shown`, arm `partial`**

- graph observation: PL at 80 K: one ~790 nm band for D_d of 20-50 nm, two bands (~750 and ~785 nm) for 50-200 um, one ~750 nm band above 300 um
- arm's reason: F5a shows PL spectra at a fixed temperature (80K) for a range of domain sizes (Dd=10um vs Dd>500um), where larger domains show a single sharp peak and smaller domains show more complex/split emission, suggesting domain size affects phase character, but this si

## 5. Annotation layer

- Panels split across the five cases: **30 of 32 (94%)**. Both failures are whole-figure images with no OCR record.
- Layer decisions taken: **12 hidden**, **22 as_is**, 0 exemplar.
- Labels harvested into `results/v2/labels/`: **750**, kept whether or not the item used them.

A finding the plan did not anticipate: **an `ocr_boxes` split cannot support hiding.** It catches text
only, and the plan forbids hiding words while arrows or marks remain. 14 of the 30 successful splits are
OCR-box splits, so they can support "exemplar" or "the author's label is the claim" but never a layer
hide. Only the 16 saturation splits can hide, which is why 22 panels ended `as_is`. Greyscale micrographs
with white or black arrows - the dominant annotation style in this corpus - are the hard case.

No panel was inpainted. Hidden regions are flat median grey, visible, with their boxes declared in
`panels.csv`, and no mask overlaps a graded feature.

## 6. Against v1, on the same papers

| | v1 (v07 cutter) | v2 |
|---|---|---|
| steps per trace | 3 or 5, nothing else | 3 to 5, mean 4.2 |
| evidence nodes per trace | 1, always | 3 to 5 |
| channels per trace | 1, always | mean 2.8 |
| depth | 1, always | 1 (single hop to the claim) with 2 to 5 parallel channels |
| items per claim | 1 | 1, but grading 3 to 5 steps instead of one yes/no |
| a panel with no crop | closed the trace (35 closures) | dropped, chain survives (case 5) |
| an annotated panel | closed the trace (89 closures) | layer decision, chain survives (cases 2, 3, 5) |

The structural goal of the redesign is met: chains, multiple channels, four-level per-step grading, and
survival of the two conditions that killed v1 traces. What is not yet met is a ground truth those chains
can be graded against.

## 7. What broke, and which rule caused it

| what | rule | outcome |
|---|---|---|
| Captions handed over the answer: F1c's span read "arrow B: Al6Cu6La phase" | plan 1, "nothing from after the answer may appear on the sheet" | `leakguard.py`: captions trimmed clause by clause against the claim's and the step's own distinctive terms, falling back to the figure preamble |
| The oracle returned an interpretation: "assigned to Al2Cu and Al6Cu6La dissolution" | plan 4, "measurements, never interpretations" | oracle returns cut at the first interpretive hinge; the answer sheet shows what was withheld |
| The closing was computed mechanically (two `shown` steps meant shown) | plan 1, the closing is the claim's own support profile | a claim carrying `requires_unseen` cannot close `shown`; `closing_why` records the reason |
| A `qualifies` audit entered as `shown` support | plan 1, ground truth is `image_support` **plus the edge relation** | a node arriving by `qualifies`/`contrasts` is a caveat: `contradicts` if its support is contradicts, else `partial`. This is what gave case 4 its partial oracle return |
| `permute_image` pointed one case's panel names at another case's folder; every path 404'd | my bug, no plan rule | fixed; `permute_answer` became a scoring-side permutation needing no dispatch |
| Step question vs `image_support` measure different things | plan 1 | **unresolved, and the reason this run stopped** |

## Files

- `results/v2/case_selection.json` - the five cases and why each was chosen, from 589 candidate claims
- `results/v2/cases/<paper>/<claim>/` - `case.json`, `question.pdf`, `answer.pdf`, `images/`, `images/layer/`, `panels.csv`, `gate/`, `gate.json`
- `results/v2/labels/<paper>.jsonl` - the harvested localization set
- `results/v2/gt_disputes.jsonl` - the review queue
- `results/v2/v2_summary.json` - every table above, regenerable with `trace_kit_v2/summarize.py`
- `trace_kit_v2/` - `survey`, `annotate`, `chain`, `materialize`, `leakguard`, `sheets`, `gate_v2`, `score`, `summarize`

Every verdict is model against model.
