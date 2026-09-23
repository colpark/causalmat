# The claim-contribution label, and whether it separates

**Every verdict is model against model.** The four-level ground truth is itself a model label, and
**no item in this pipeline has been checked by a person.** Part 4 below is the one step that requires
one, and it has not been done.

Branch `traces-v2/2026-09-23`. `taxonomy/graphs_*`, `results/v07/` and `trace_kit/` are untouched;
the label is a sidecar in `results/v2/`.

## Why this exists

The v2 run stopped because the step question and the ground truth asked different things: the step
asks what a panel contributes to the claim, while `image_support` records whether the observation is
visible in the panel. 14 of 21 steps disputed, 12 one-directional.

## Part 2. The label reproduces the disputes, so the mismatch was definitional

`net-contrib` saw the claim text, one observation text and the relation. No panel, no question, no
arm answer, no tools. Panel references were scrubbed from the observation first, and every prompt was
machine-checked for a panel, figure, image, question, answer or support level before dispatch.

| `image_support` | `establishes` | `supports_part` | `not_addressed` | `cuts_against` |
|---|---|---|---|---|
| shown (17) | 1 | 15 | 0 | 1 |
| partial (3) | 0 | 3 | 0 | 0 |
| contradicts (1) | 0 | 1 | 0 | 0 |

The two fields agree on 4 of 21 steps. Of the 14 disputes: **13 resolved** (the label lands on what the
full arm said), 1 unchanged, **0 agreeing with neither**. The stop-rule threshold was one third; the
actual figure is 0%. The mismatch was definitional and the field fixes it.

Full cross-table and the resolved list: `results/v2/contrib_vs_image_support.md`.

## Part 3. As an absolute scale the label fails, and the baseline is why

Re-gated with `expected_support` from `contribution`. The new target is 19 of 21 `partial`.

| case | **baseline** (always "partial") | full | oracle_complete | floor | no_image | permute_image |
|---|---|---|---|---|---|---|
| case1_three_techniques | **3/3** | 2/3 | 3/3 | 0/3 | 1/3 | 0/3 |
| case2_annotated | **3/4** | 3/4 | 3/4 | 3/4 | 2/4 | 0/4 |
| case3_contradicts | **4/4** | 3/4 | 3/4 | 3/4 | 3/4 | unparsed |
| case4_oracle | **4/5** | 2/5 | 2/5 | 1/5 | 1/5 | unparsed |
| case5_drop | **5/5** | 4/5 | 4/5 | 0/5 | 4/5 | unparsed |

**No arm number here is readable without the baseline beside it.** A constant "partial" beats the
image-reading arm on 4 of 5 cases. The metric is worse than uninformative.

### Degeneracy or leakage: both, at different scales

`oracle_complete` matches or beats `full` on 4 of 5 cases, so the stop rule fires. Reported by cause,
as the brief requires rather than on the raw match:

**In aggregate it is degeneracy.** The oracle sits at or below the majority-class baseline on every
case and its per-step pattern is mostly the constant answer. It is not beating the baseline; it is
reproducing it, as is everything else.

**On the two steps where the class prior gives no help, it is leakage:**

| step | truth | full | oracle | floor | no_image |
|---|---|---|---|---|---|
| case2 step 2 | `contradicts` | partial | **contradicts** | partial | shown |
| case4 step 5 | `shown` | partial | **shown** | not addressed | not addressed |

The oracle got both discriminating steps right; the full arm got neither. That is the leakage
signature: the text delivery carries the answer exactly where the prior cannot fake it. With n=2 this
is weak evidence, but the direction is the concerning one, and the two causes are not alternatives:
degeneracy hides the leakage by drowning 19 of 21 steps in a constant.

The `permute_image` control was rebuilt twice this run. Its prompts now carry 5 to 12 real cross-case
images each, 0 missing; where it parsed it scored 0, so the items do use their pictures.

## Part 4. The audit pack, unfilled

`results/v2/audit_pack/` - 21 pages, one per step, plus `audit_sheet.csv`.

The brief asks for 30 steps across four contribution values. The five cases carry 21 steps and
3 values (supports_part 19, cuts_against 1, establishes 1), so **every step is included and nothing is padded**,
as the stop rule directs. Each page shows the claim, the observation as the label saw it, the relation,
the graph's `image_support`, the contribution with its reason and what it leaves open, and a box for
agree or disagree with a reason.

**This is the one step in the pipeline a person must do. It has not been done.**

## Part 5. Whether to label the pool: no, not as absolute levels

60 edges from the 589-claim pool, stratified.

| stratum | n | `establishes` | `supports_part` | other |
|---|---|---|---|---|
| single_evidence | 20 | **8 (40%)** | 11 | 1 |
| reference_match | 20 | **1 (5%)** | 18 | 1 |
| random_rest | 20 | **5 (25%)** | 13 | 2 |

**The stop rule does not fire**: `establishes` reaches 40% in the single-evidence stratum, far above
the 10% floor. The label is not degenerate.

But the strata did not measure what they were designed to. `reference_match` came back at 5%, the
opposite of the prediction, because it was drawn from claims with more than one evidence node - so by
construction no single observation could establish them. That is a confound in the stratification, not
a property of reference matches. Controlling for it:

| evidence nodes on the claim | n | `establishes` |
|---|---|---|
| 1 | 21 | **9 (43%)** |
| 2-3 | 29 | 4 (14%) |
| 4+ | 10 | 1 (10%) |

**The label separates, and what it separates on is claim arity.** That is correct behaviour: a claim
resting on one panel can be established by it; a claim resting on five cannot be established by any one
of them. The `establishes` cases read as genuine - a thrombin specific activity, a capacity retention
figure, a nodule count, each directly naming the quantity its claim asserts.

### The decision the evidence supports

**Do not label the pool as absolute levels.** Support chains are seeded by definition on claims with
two or more figure-backed evidence nodes, which is precisely the population where `establishes` is
rare. `supports_part` will dominate any chain the redesign builds, permanently, and a constant answer
will keep beating the image arm however good the labels are. Part 3's degeneracy is structural, not a
labelling fault, and 1,500 to 1,800 more calls would buy a well-founded constant.

### The alternative, described and not built

Within a chain, rank the panels by contribution instead of assigning each an absolute level: ask which
step carries most weight for the claim and which least. An ordering discriminates even when every step
sits at the same level, it needs no new vocabulary, the `unsettled` field already supplies the material
to justify an order, and the majority-class attack disappears because a permutation has no majority
class. The cost is that ranking needs every step in one prompt, which changes the arm contract and the
oracle-delivery question with it.

## What is still open

- The human audit. Nothing here has been checked by a person.
- Whether the leakage signal on the two non-majority steps holds at n larger than 2.
- Whether ranking discriminates, which the paragraph above describes and no code implements.

## Files

- `results/v2/contrib_labels.jsonl`, `contrib_vs_image_support.md` - part 2
- `results/v2/cases/*/*/gate.json` - part 3, each with `majority_class_baseline`
- `results/v2/audit_pack/` - part 4, unfilled
- `results/v2/separability.json` - part 5, 60 labels with their strata
- `trace_kit_v2/` - `contrib`, `separability`, `audit_pack`, `score`, `chain`, `summarize`

Every verdict is model against model.
