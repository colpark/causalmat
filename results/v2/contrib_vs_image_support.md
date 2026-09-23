# The claim-contribution label against `image_support`

**Every verdict is model against model.** `net-contrib` saw only the claim text, one observation
text and the relation between them: no panel, no question, no arm answer, no `gt_disputes.jsonl`,
and no tools. Panel references were scrubbed from the observation text before dispatch, because
naming a panel would itself tell the label it is looking at figure evidence.

21 steps across the five cases. 21 labelled.

## Cross-table: `image_support` (rows) against `contribution` (columns)

| image_support | `establishes` | `supports_part` | `not_addressed` | `cuts_against` | total |
|---|---|---|---|---|---|
| **shown** | 1 | 15 | 0 | 1 | 17 |
| **partial** | 0 | 3 | 0 | 0 | 3 |
| **contradicts** | 0 | 1 | 0 | 0 | 1 |
| **total** | 1 | 19 | 0 | 1 | 21 |

The two fields agree on **4 of 21** steps when `establishes`/`supports_part`/
`not_addressed`/`cuts_against` are read as shown/partial/not addressed/contradicts.

## What it does to the 14 disputes

- **13 resolved**: the new label agrees with what the full arm said.
- **1 unchanged**: the new label agrees with the graph, against the arm.
- **0 agree with neither**.

### Resolved

| case | step | node | claim needs | graph | arm | contribution |
|---|---|---|---|---|---|---|
| case5_drop | 1 | `o10` | quantitative crystal rotation angle of wavy bands; confirmation of fix | shown | partial | `supports_part` |
| case5_drop | 4 | `o16` | quantitative upper bound near 55 deg; continuity of the angle distribu | shown | partial | `supports_part` |
| case3_contradicts | 1 | `o5` | comparison of transition temperature across different domain sizes; co | shown | partial | `supports_part` |
| case3_contradicts | 2 | `o12` | quantitative transition temperature values across domain sizes; direct | shown | partial | `supports_part` |
| case3_contradicts | 4 | `a3` | transition temperature rising with domain size; precise onset point of | contradicts | partial | `supports_part` |
| case2_annotated | 1 | `o3` | actual pore size (~4-5 nm) determination; channel/hexagonal pore geome | shown | partial | `supports_part` |
| case2_annotated | 3 | `o5` | explicit identification of panel a and b as 2Co-MBG and 5Co-MBG specif | shown | partial | `supports_part` |
| case2_annotated | 4 | `o6` | exact pore size ~4-5 nm; long-range ordering of the channel structure; | shown | partial | `supports_part` |
| case4_oracle | 2 | `o16` | absence of metallic Co reflections/new phase formation; quantitative e | shown | partial | `supports_part` |
| case4_oracle | 3 | `o19` | retention of crystalline (long-range) structure of PCO; quantitative d | shown | partial | `supports_part` |
| case4_oracle | 4 | `o20` | retention of crystalline (long-range ordered) oxide structure; quantit | shown | partial | `supports_part` |
| case1_three_techniques | 1 | `o2` | specific phase composition Al6Cu6La; cubic NaZn13 crystal structure id | shown | partial | `supports_part` |
| case1_three_techniques | 3 | `o5` | Sm forms no new phase; cubic NaZn13 crystal structure identification;  | shown | partial | `supports_part` |

### Unchanged (label sides with the graph)

- **case3_contradicts step 3 (`o13`)** graph `partial`, arm `shown`, contribution `supports_part`
  - why: The map directly shows the dual-band transition window widening toward small domains (equivalently narrowing as domains grow), but it only implies rather than directly quantifies that the transition temperature itself shifts upward with increasing domain size.

## Stop rule

Agrees with neither on **0 of 21 steps = 0%**; the threshold is one third.
**Not fired.**

Every verdict is model against model.
