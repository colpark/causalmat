# Measured necessity by removal

**Every verdict is model against model.** Necessity here is not a property of a panel: it is a
measurement relative to **this answerer, this prompt and this model**, and would move with any of them.
**No item in this pipeline has been checked by a person**, and the 21-page audit pack from the previous
run (`results/v2/audit_pack/`) is still unread.

## 1. The answerer and the protocol

| | |
|---|---|
| answerer | `net-claim`, `model: sonnet`, `tools: Read` only |
| input | claim text, the paper's setup context, panel images. No observation text, no contribution label, no step structure; machine-checked before every dispatch |
| verdicts | supported / partly supported / cannot tell / contradicted, with a confidence 0-1 |
| threshold | `drop > 0.15`, **fixed in advance** |
| repeats | 3 per configuration; majority verdict, median confidence |
| necessity | removal **strictly weakens** the verdict from wherever the full run started, or `drop` clears the threshold |
| calls | 168: per case one full run, one per panel, one per channel, one no-panel floor, x3 |

## 2. Per case, both granularities

| case | full run | floor (no panels) | panel-level | channel-level |
|---|---|---|---|---|
| case1_three_techniques | partly supported 0.55 | cannot tell 0.95 | 1/3 **mixed** | 1/3 **mixed** |
| case2_annotated | partly supported 0.5 | cannot tell 0.95 | 1/4 **mixed** | 0/3 **all_redundant** |
| case3_contradicts | supported 0.72 | cannot tell 0.9 | 1/3 **mixed** | 1/2 **mixed** |
| case4_oracle | partly supported 0.45 | cannot tell 0.95 | 0/6 **all_redundant** | 1/3 **mixed** |
| case5_drop | partly supported 0.55 | cannot tell 0.95 | 0/16 **all_redundant** | 0/3 **all_redundant** |

Case 1 has one panel per channel, so its channel column is the same measurement twice, not a second one.

### Channel-level removal, which is what this part existed to test

| case | channel | panels | verdict without it | drop | rank | necessary |
|---|---|---|---|---|---|---|
| case1_three_techniques | XRD | 1 | partly supported | 0.2 | 1 | **yes** |
| case1_three_techniques | SEM | 1 | partly supported | 0.0 | 2 (tie) | no |
| case1_three_techniques | THERMAL | 1 | partly supported | 0.0 | 2 (tie) | no |
| case2_annotated | XRD | 1 | partly supported | 0.05 | 1 (tie) | no |
| case2_annotated | TEM | 2 | partly supported | 0.05 | 1 (tie) | no |
| case2_annotated | PHYS | 1 | partly supported | 0.0 | 3 | no |
| case3_contradicts | XRD | 1 | supported | -0.1 | 1 | no |
| case3_contradicts | PL | 2 | cannot tell | -0.13 | 2 | **yes** |
| case4_oracle | ECHEM | 1 | partly supported | -0.05 | 1 | no |
| case4_oracle | XRD | 1 | partly supported | -0.1 | 2 | no |
| case4_oracle | XAS | 4 | cannot tell | -0.3 | 3 | **yes** |
| case5_drop | OM | 6 | partly supported | 0.0 | 1 (tie) | no |
| case5_drop | EBSD | 4 | partly supported | 0.0 | 1 (tie) | no |
| case5_drop | TEM | 6 | partly supported | 0.0 | 1 (tie) | no |

**Case 4 is the win.** Panel-level read 0 of 6, all-redundant: pull any one XAS panel and the other three
carry it. Pull the whole XAS channel and the verdict falls to `cannot tell`, drop -0.30. Channel-level
turned an all-redundant chain into a mixed one, which is the hypothesis this part was built to test.

**Case 5 did not move.** 16 panels in three channels of 6, 4 and 6; removing any whole channel still
leaves `partly supported` at the same confidence. Per the stop rule this is a property of the chain
rather than a failure of the method: **a chain of roughly five panels or more cannot be discriminated by
removal at any granularity**, because whatever remains still carries the claim.

**Case 2 moved the wrong way**, mixed at panel level and all-redundant at channel level. The reason
matters more than the result; see section 4.

## 3. Discrimination, and the floor

- **Mixed splits: 3 of 5 at panel level, 3 of 5 at channel level, but not the same three.** Either
  granularity alone gives 3/5; counting a chain as discriminated when *either* separates it gives
  **4 of 5**, with only case 5 constant under both.
- **Repeat instability: 0 of 56 configurations** disagreed across three repeats; the stop rule was one
  third. The measurement is deterministic here, which is why a 0.05 drop is signal rather than noise,
  and also why the confidences are visibly quantised.
- **The confidence floor says `cannot tell` on all five, never `supported`.** The claims are not
  self-persuasive from text and setup alone. This is the first of the three metrics tried in this run to
  clear that bar, and it is the precondition for any evidence metric meaning anything.

## 4. What the numbers say about the metric itself

**`drop` is conditional on the verdict, so most drops are not comparable.** The answerer reports
confidence *in the verdict it gave*. A full run at `partly supported` 0.45 against a removal run at
`cannot tell` 0.95 differs by -0.50, but that is not a gain in support: it is high confidence in a
weaker answer. 4 of 46 drops span a changed verdict and are meaningless; every negative drop in the
tables above is that artefact. Only the **42 drops where the verdict held** are interpretable.

**Removal is non-monotonic in one case.** In case 2, removing panel F4b alone gives `cannot tell`, while
removing the whole TEM channel, F4a **and** F4b, gives `partly supported`. Removing strictly more
evidence produced a strictly stronger verdict. With 0% repeat variance that is not noise; it is the
answerer reacting to what remains rather than to what was taken. It bounds how much weight one removal
can carry, and it is why case 2 flips split between granularities.

**The ordering is real but shallow.** Repeat spread is 0.0, so any non-zero drop clears it and every
case reports `ordering_outside_noise = true`. But the drops sit at 0.0 and +/-0.05 with two exceptions:
case 1 XRD at 0.20 and case 4 XAS at -0.30. Case 5's three channels tie at exactly 0.0, so it has no
ordering and the table says rank 1 (tie) three times rather than inventing 1, 2, 3.

## 5. Against the labels we already had

34 panel rows across the five cases.

| comparison | agreement |
|---|---|
| measured (panel) vs **structural leave-one-out, free from the graph** | **5/34 = 15%** |
| measured (panel) vs measured (channel) | 27/34 = 79% |

**The free structural version is not a usable proxy, and the reason disqualifies it outright.** It calls
32 of 34 panels `necessary` where the measurement calls 31 `redundant`. Worse, it is an artefact of
whichever label feeds it: computed over `image_support` it called most channels
`redundant_by_single_loo`; recomputed, rule unchanged, over `contribution`, where nearly every step is
`partial`, it calls almost everything `necessary`. Only the upstream label moved. A proxy that inverts
when you swap the label beneath it is measuring the label, not the evidence.

So the expensive measurement is **not** merely calibration for a free one. There is no free one.

## 6. Recommendation

**Measured necessity is usable for support chains, under three conditions.**

1. **Use the verdict flip, not the drop.** The flip carried every genuine result here: case 3's PL
   channel, case 4's XAS channel, case 1's XRD panel. The drop is quantised, conditional on the verdict,
   and uninterpretable exactly when the verdict moves, which is when it matters.
2. **Remove at channel level**, keeping panel level as a cross-check. Channel removal rescued case 4;
   panel removal inside a four-panel channel measures redundancy and nothing else.
3. **Cap chains at about five panels.** Case 5, at 16, is constant under both granularities. Above that
   size no removal discriminates, so the chain is cut down or it is not gradeable this way.

Against the two metrics this run discarded, that is a real improvement: `image_support` answered a
different question than the chain asked, `contribution` was a sound label that came back 90% constant on
multi-evidence claims, and this one has a working floor, deterministic repeats, and separates 4 of 5
chains under one granularity or the other. It is also the only one of the three whose ground truth is an
experiment rather than another model's opinion, though the experiment is still run by a model.

**What would settle it:** the audit pack. 21 pages, one per step, unread. Everything above is models
checking models.

## Files

- `results/v2/necessity/<case>.json` - full run, per-panel and per-channel rows, floor, ranks, splits
- `results/v2/necessity/agreement.json` - the 34-row comparison behind section 5
- `.claude/agents/net-claim.md` - the answerer
- `trace_kit_v2/necessity.py` - configurations, guard, collection

Every verdict is model against model.
