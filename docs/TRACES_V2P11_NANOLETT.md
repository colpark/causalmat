# v2.11 pilot — stricter acceptance on one paper

**Every verdict is model against model.** No step of this was reviewed by a person.

Paper: `Nano_Letters__10.1021_acs.nanolett.6b04294`. Scope: the 5 chains v2.10 put on this paper (C19, C20, C45, C46, C85), the 10 units they are built from, grouped into 3 families by shared prefix.

## Step 1 — what each arm actually received

Read out of the prompt files that were sent, not the generator that wrote them (the generator has been edited since those runs, so its source is not evidence).

**Finding: limits were in the handoff to both arm B and arm C; no rerun needed.** All 8 links carried every recorded qualification into both arm B and arm C, so the rerun branch of Step 1 did not fire and no arm was rerun.

What each arm held, per link:

| arm | observation text | cropped panels | whole figures | captions | earlier result | its limits |
| --- | --- | ---: | ---: | --- | --- | --- |
| A | yes | 2 | 0 | yes | no | 0/4 |
| B | yes | 2 | 0 | yes | yes | 4/4 |
| C | no | 0 | 0 | no | yes | 4/4 |
| N | no | 0 | 0 | no | no | 0/4 |

(One link shown; the shape is the same on all eight, and the per-link counts are in `step1.json`.)

**No arm was ever shown a whole figure.** Every panel reached the answerers as a crop plus its printed caption. That matters for Step 3: a judge asked whether the evidence can carry a claim is ruling on crops and captions, which is what the answerers had.

## Steps 2–5 — every seed and link against the six gates

| unit | kind | A | B | C | N | stacked | B−A | B−C | B−stacked | 1 dep | 2 rel | 3 abs | 4 con | 5 cav | 6 val | verdict |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| `nano_letters_com_o16_o19` | seed | 0.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 0.00 | ✓ | **✗** | ✓ | **✗** | ✓ | ✓ | **fail 2_relation** |
| `nano_letters_spi_o16_o13` | seed | 0.00 | 0.67 | 0.00 | 0.00 | 0.33 | 0.67 | 0.67 | 0.33 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | pass |
| `di_nano_letters_com_o16_o19_o13_n16` | link | 0.25 | 0.75 | 0.00 | 0.00 | 0.25 | 0.50 | 0.75 | 0.50 | ✓ | ✓ | ✓ | ✓ | ✓ | **✗** | **fail 6_validity** |
| `nl_di_nano_letters_com_o16_o19_o13_n16_o24_n18` | link | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | pass |
| `d4_nl_di_nano_letters_com_o16_o19_o13_n16_o24_n18_o10_n8` | link | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | pass |
| `d4_nl_di_nano_letters_com_o16_o19_o13_n16_o24_n18_o9_n8` | link | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | ✓ | ✓ | ✓ | ✓ | **✗** | ✓ | **fail 5_caveats** |
| `di_nano_letters_spi_o16_o13_o24_n18` | link | 0.00 | 0.50 | 0.00 | 0.00 | 0.00 | 0.50 | 0.50 | 0.50 | ✓ | ✓ | **✗** | **✗** | ✓ | **✗** | **fail 3_absolute** |
| `nl_di_nano_letters_spi_o16_o13_o24_n18_o10_n8` | link | 0.00 | 0.67 | 0.33 | 0.00 | 0.67 | 0.67 | 0.33 | 0.00 | ✓ | **✗** | ✓ | **✗** | ✓ | **✗** | **fail 2_relation** |
| `nl_di_nano_letters_spi_o16_o13_o24_n18_o9_n8` | link | 0.00 | 1.00 | 0.33 | 0.00 | 0.67 | 1.00 | 0.67 | 0.33 | ✓ | ✓ | ✓ | **✗** | **✗** | ✓ | **fail 4_no_contradictions** |
| `di_nano_letters_com_o16_o19_o13_n18` | link | 0.00 | 0.50 | 0.00 | 0.00 | 0.00 | 0.50 | 0.50 | 0.50 | ✓ | ✓ | **✗** | ✓ | ✓ | **✗** | **fail 3_absolute** |

3 of 10 units clear all six gates.

Which gate does the work:

| first gate failed | units |
| --- | ---: |
| 2_relation | 2 |
| 3_absolute | 2 |
| 6_validity | 1 |
| 5_caveats | 1 |
| 4_no_contradictions | 1 |

## The stacked baseline

Arm B holds everything arm A and arm C hold, so B beating each separately is a low bar: stapling the two answers together clears it. The stacked baseline is that staple — arm A's answer and arm C's, concatenated with nothing added, graded against the same claims by the same grader.

- **8 of 10 units** beat the stacked pile by the required +0.25.
- Mean B−stacked: **+0.517**
- **2 units are additive, not relational**: they pass the dependency gate (B really does beat A and C) yet do not beat the concatenation of A and C. Their answers carry what both sides carry without relating them.

| unit | B | stacked | B−stacked |
| --- | ---: | ---: | ---: |
| `nano_letters_com_o16_o19` | 1.00 | 1.00 | 0.00 |
| `nl_di_nano_letters_spi_o16_o13_o24_n18_o10_n8` | 0.67 | 0.67 | 0.00 |

### The clearest case

`nano_letters_com_o16_o19`: arm A scores 0.00 and arm C 0.00, yet their concatenation scores 1.00 — a gap of +1.00 over either answer alone.

The claim: *“Structural retention (XRD) plus retained oxidized Co (XANES, unlike Co foil) together indicate sodiation reduces PCO only slightly, without producing metallic Co.”*

What the grader quoted from the pile to call it stated:

> there is no conversion to metallic Co0 during discharge, even at OCV or after full discharge ... consistent with a Co-centered redox process (e.g., Co3+/Co2+-like) accompanying Na insertion/extraction ... the host structure's principal reflections survive the full Na insertion/extraction cycle without a phase change detectable by this diffraction window

That quote is a splice. Its parts come from opposite sides of the concatenation boundary — one from the arm that saw only the first measurement, one from the arm that saw only the second — joined by the grader, not by any answerer. The claim was assembled by the reader. This is exactly what gate 2 exists to catch, and no arm-versus-arm comparison can see it, because arm B beats both A and C by a full point here.

## Step 3 — evidence validity

25 combined claims ruled across 10 units.

| ruling | n | share |
| --- | ---: | ---: |
| supported | 11 | 44.0% |
| overreaches | 10 | 40.0% |
| unsupported | 4 | 16.0% |

The 5 rulings that fail gate 6, verbatim:

- **`di_nano_letters_com_o16_o19_o13_n16`** — *unsupported* — “A conversion-type reduction to metallic Co would be expected to generate new particle/void interfaces and hence measurable SAXS contrast changes.”
  - cannot show: The evidence only shows what SAXS looked like for the sample that did NOT undergo metallic-Co conversion (near-invariant profile); it contains no measurement of, or comparison to, a conversion-type/metallic-Co case, so it cannot establish what SAXS contrast changes such a process 'would be expected' to produce.
  - quoting: “Na SAXS contours stay nearly straight; I(q) curves overlap except a small drop at ~0.03-0.1 A-1 at 0.11/0.02 V”
- **`di_nano_letters_spi_o16_o13_o24_n18`** — *unsupported* — “Na capacity fading is attributable to poor sodiation reactivity rather than to volume-change-driven structural failure.”
  - cannot show: any direct measurement of capacity fade or its cause; the evidence never measures capacity, volume change, or mechanical/structural failure modes tied to cycling loss
  - quoting: “B is a computed proxy for reaction extent, not a direct measurement of capacity fade, so the pair does not quantitatively tie a given oxidation-degree value to a specific amount of capacity loss”
- **`nl_di_nano_letters_spi_o16_o13_o24_n18_o10_n8`** — *unsupported* — “The continued fade to the 40th cycle is of the kind n18 predicts rather than the kind a volume-change failure would produce.”
  - cannot show: whether the fade from 470 to 60 mAh/g by cycle 40 is driven by the same limited-conversion mechanism versus structural degradation accumulating beyond cycle 1
  - quoting: “n18's structural-retention evidence was established only for the first cycle, so extending the poor-reactivity attribution to explain the continued fade from ~470 (1st charge) down to ~60 mAh/g by the 40th cycle is not established by this pairing -- the later fade could still involve structural degradation that accumulates past cycle 1, which was never checked”
- **`di_nano_letters_com_o16_o19_o13_n18`** — *overreaches* — “Structural/chemical retention (XRD+XANES) together with the absence of volume change (SAXS) jointly indicate sodiation produces neither appreciable metallic-Co-forming reduction nor appreciable volume/morphology change.”
  - cannot show: The observation does not show an outright 'absence' of volume/morphology change -- it explicitly reports a small SAXS drop at ~0.03-0.1 A^-1 whose magnitude and physical origin are not quantified or explained, so 'absence of volume change' asserts more certainty than the data (which show only near-constancy with one small exception) allow.
  - quoting: “Na SAXS contours stay nearly straight; I(q) curves overlap except a small drop at ~0.03-0.1 A-1 at 0.11/0.02 V ... Does not quantify the magnitude of the small SAXS drop at ~0.03-0.1 A^-1 in terms of actual volume/morphology change, nor its physical origin”
- **`di_nano_letters_com_o16_o19_o13_n18`** — *unsupported* — “The capacity fading is instead consistent with limited/poor sodiation (conversion) activity of the oxide rather than volume-change-induced degradation.”
  - cannot show: None of the XRD, XANES, or SAXS measurements shown here directly measure or attribute capacity fading to a mechanism (limited conversion activity vs. volume-change degradation); the evidence only bears on structural/chemical/morphological persistence, not on the electrochemical fading mechanism itself.
  - quoting: “Does not establish the mechanism by which sodiation activity is limited (why conversion is minor)”

## The chains and families

v2.10 accepted all 5 chains on this paper. v2.11 accepts **0**, across **0** of **3** families.

| chain | family | depth | v2.10 | v2.11 | first gate failed | on which unit |
| --- | --- | ---: | --- | --- | --- | --- |
| C19 | F1 | 4 | accepted | rejected | 2_relation | `nano_letters_com_o16_o19` |
| C20 | F1 | 4 | accepted | rejected | 2_relation | `nano_letters_com_o16_o19` |
| C45 | F2 | 3 | accepted | rejected | 3_absolute | `di_nano_letters_spi_o16_o13_o24_n18` |
| C46 | F2 | 3 | accepted | rejected | 3_absolute | `di_nano_letters_spi_o16_o13_o24_n18` |
| C85 | F3 | 2 | accepted | rejected | 2_relation | `nano_letters_com_o16_o19` |

**3 of 5 chains die at the seed** — the unit v2.10 never put to the arms at all. A chain can only be as good as the thing it starts from, and on this paper the starting point was never checked.

**The old rule was not binding here.** Gate 1 is the whole v2.10 test, and all 10 of 10 units pass it. Every rejection in this pilot comes from a gate v2.10 did not have: 7 units clear the dependency test and fail something else.

| family | seed | chains | shared steps | accepted |
| --- | --- | --- | ---: | ---: |
| F1 | `nano_letters_com_o16_o19` | C19, C20 | 3 | 0 |
| F2 | `nano_letters_spi_o16_o13` | C45, C46 | 2 | 0 |
| F3 | `nano_letters_com_o16_o19` | C85 | 2 | 0 |

### The caveat ledger on accepted chains

- **C19**: 17 qualifications, 17 respects
- **C20**: 19 qualifications, 2 ignores, 17 respects — **rejects the chain**
- **C45**: 14 qualifications, 3 ignores, 11 respects — **rejects the chain**
- **C46**: 15 qualifications, 1 ignores, 14 respects — **rejects the chain**
- **C85**: 9 qualifications, 9 respects

## The seeds, which v2.10 never tested

- `nano_letters_com_o16_o19`: 8 claims kept, **1 tagged combined**, 4 limits. 0 dropped by the second tagger.
- `nano_letters_spi_o16_o13`: 10 claims kept, **3 tagged combined**, 4 limits. 0 dropped by the second tagger.

A seed with one combined claim has a combined score that can only be 0.00 or 1.00. That is a coarse instrument, and gate 3 (B ≥ 0.60) on such a seed is an all-or-nothing test rather than a measurement. Stated here rather than left for the reader to infer from the table.

## A defect in the grader itself, found during this run

The `net-grader` agent definition (`.claude/agents/net-grader.md`, and 2 byte-identical copies elsewhere in the repo) carries instructions left over from an older task:

```
Reply with one word first: CORRECT, PARTIAL, WRONG, or ABSTAIN (if the candidate says CANNOT DETERMINE), then one sentence why.

## Rules

Second-read case (the question asks what a figure panel shows and the candidate is an independent description of the panel written without the paper): Grade whether the description and the observation name the same features of the same image. Different names for the same thing (stain names, map axes written in another order, instrument synonyms) are CORRECT. WRONG only when the image shows a different kind of data or contradicts the observation.
```

The body tells the grader to reply with one word (CORRECT/PARTIAL/WRONG/ABSTAIN) and describes a panel-second-read task. Every grading prompt in v2.8 through v2.11 instead asks for per-claim JSON rulings.

Observed effect in this run: **1 of 18 grading replies** opened with the stray verdict word, and **0** failed to return a rulings block. The graders overwhelmingly followed the prompt file and ignored their own system prompt, so the practical damage here is small. The second rule is the worse of the two, though: it tells the grader that "different names for the same thing" are CORRECT, a leniency instruction written for panel descriptions that has no business in claim grading.

**Scope: Affects every grading call in v2.8, v2.9, v2.10 and v2.11, since all used this same net-grader definition.**

Left untouched for this pilot on purpose: changing the grader would make v2.11 incomparable with the v2.10 numbers it is being measured against. It is the first thing to fix before this rule is applied to any other paper.

## The report

`results/v2p11/nanolett.6b04294/report.html` — 2.08 MB, self-contained, 7 panels shown, 0 panel misses, 2 images over the 1400 px cap and downscaled once.

## Cost

- Estimated before any call: **45** (57 with the borderline reserve), against the brief's estimate of 150 to 250. The gap is Step 1: it found the limits were already in the handoff, so the rerun branch never fired.
- Actual: **46 calls**, 21 minutes wall time

  - seedsplit: 2
  - seedsplitcheck: 2
  - seedarms: 8
  - validity: 10
  - ledger: 5
  - seedgrade: 8
  - stacked: 10
  - stacked_redispatch_after_a_slow_reply_was_misread_as_dead: 1

- Every reply was matched to its prompt byte for byte in the dispatching agent's own transcript before it was written to disk. The relay's own report is not evidence.

