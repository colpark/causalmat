# Traces v2.8b — the same-question control

Every verdict is model against model.

In v2.8 only arm B was asked the full combined question. Arms A and C got narrower questions matching what they held, which they needed to be answerable, but it left their near-zero scores on combined claims partly a property of the question. This run asks every arm the same full question, word for word, and blanks the missing section with "not provided" so the document shape never changes either.

It also adds arm N, which gets the question and nothing else. These are published papers. If a model reaches a key's combined claims with no measurement and no earlier result, then that claim was never evidence of composition.

The v2.8 claim lists, and the v2.8 arm A, B and C answers and gradings, are reused unchanged. The grader is the v2.8 grader, unchanged, and never sees the arm label.

## The headline

| arm | what it held | mean combined | mean limit |
|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.067 | 0.129 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 0.774 | 0.565 |
| **C** | earlier result only, narrow question (v2.8) | 0.091 | 0.310 |
| **A_full** | measurement + panels, **full** question | 0.022 | 0.094 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.036 | 0.186 |
| **N** | nothing but the full question | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 0.499 | 0.478 |

**8 of 8 items are strictly compositional**, against 7 of 8 under v2.8's looser rule. Arm B beats A_full on 8, beats C_full on 8, and arm N stays under 0.25 on 8.

**Split halves agree on 7 of 8 items.** The stop rule was 6 of 8: not fired.

The memorisation stop rule did not fire: arm N reaches 0.25 or more on 0 of 8 items, under the threshold of 3.

## What the blanked sections did to the arms

The control removed one artefact and introduced another, and the second one is large enough that the headline above cannot be read at face value. Marking a section "not provided" makes the answerer refuse rather than reason from what it does hold:

| arm | answers that open by refusing the task | of |
|---|---|---|
| **A_full** | 39 | 48 |
| **C_full** | 10 | 48 |
| **N** | 48 | 48 |
| **B_narrow** | 0 | 48 |

Arm N refuses in 48 of 48 samples and A_full in 39 of 48. So A_full's 0.022 and C_full's 0.036 are substantially a measure of abstention, not of what the evidence supports. v2.8's arms A and C, asked a narrower but coherent question with real content in every section, abstained not at all and scored 0.067 and 0.091.

**The two runs bracket the truth rather than one superseding the other.** v2.8 asked each arm a question it could answer but gave arm B an easier one. v2.8b asked every arm the same question but told two of them their evidence was missing, which they mostly took as an instruction to stop. The real single-side capability sits between 0.022 and 0.067 for the measurement side and between 0.036 and 0.091 for the earlier-result side. Neither run settles it, and a third design -- same question, no blanking, each arm simply given less -- would.

The same caveat weakens arm N as a memorisation test. It scores 0.000 on every item, which is a clean result, but with 48 of 48 answers refusing outright it measures whether the model WILL answer with no evidence, not whether it COULD. A sharper test would name the paper and ask for a best guess.

## Arm N on its own

Arm N held the question and nothing else: no measurement, no earlier result, no panels. Whatever it scores is what the wording of the question, plus whatever the model already knows about the paper, is worth.

| item | journal | combined claims | arm N combined | arm N limit | arm N contradictions |
|---|---|---|---|---|---|
| `di_acta_materia_com_o10_o14_o12_n13` | Acta Materialia | 5 | **0.000** | 0.000 | 0.000 |
| `di_advanced_ene_spi_o1_o12b_o20_n10` | Advanced Energy Materials | 1 | **0.000** | 0.000 | 0.000 |
| `di_journal_of_a_spi_o13_o20_o22_n15` | Journal of Advanced Cerami | 2 | **0.000** | 0.000 | 0.000 |
| `di_materials_ch_com_o1_o7_o3_r1` | Materials Characterization | 4 | **0.000** | 0.000 | 0.000 |
| `di_journal_of_m_spi_o15_o17_o16_m2` | Journal of Magnesium and A | 4 | **0.000** | 0.000 | 0.000 |
| `di_bioactive_ma_com_o11_o12_n18_o15_n2` | Bioactive Materials | 3 | **0.000** | 0.000 | 0.000 |
| `di_advanced_fun_spi_o1_o4_o6_n10` | Advanced Functional Materi | 7 | **0.000** | 0.000 | 0.000 |
| `di_journal_of_m_spi_o14_o10_o11_f2` | Journal of Materials Scien | 3 | **0.000** | 0.000 | 0.000 |

No item has arm N at or above 0.25.

## Every item, all seven arms

### `di_acta_materia_com_o10_o14_o12_n13`

Acta Materialia · drafter label **discriminating** · upstream `acta_materia_com_o10_o14` (complementary) · 5 combined claims, 4 limit claims

| arm | what it held | mean combined | mean limit | mean contradictions |
|---|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.133 | 0.042 | 0.167 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 0.600 | 0.792 | 0.333 |
| **C** | earlier result only, narrow question (v2.8) | 0.000 | 0.083 | 0.000 |
| **A_full** | measurement + panels, **full** question | 0.067 | 0.000 | 0.167 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.000 | 0.000 | 0.167 |
| **N** | nothing but the full question | 0.000 | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 0.233 | 0.500 | 0.667 |

B − A_full +0.533 → **True** · B − C_full +0.600 → **True** · arm N below 0.25 → **True**

strictly compositional **True** (v2.8 said True) · reaches it unprompted (B_narrow ≥ 0.5) **False** · halves (True, True) agree **True**

### `di_advanced_ene_spi_o1_o12b_o20_n10`

Advanced Energy Materials · drafter label **discriminating** · upstream `advanced_ene_spi_o1_o12b` (spine_edge) · 1 combined claims, 4 limit claims

| arm | what it held | mean combined | mean limit | mean contradictions |
|---|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.333 | 0.125 | 0.000 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 0.833 | 0.292 | 0.000 |
| **C** | earlier result only, narrow question (v2.8) | 0.000 | 0.833 | 0.667 |
| **A_full** | measurement + panels, **full** question | 0.000 | 0.083 | 0.000 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.000 | 0.500 | 1.167 |
| **N** | nothing but the full question | 0.000 | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 0.667 | 0.292 | 0.000 |

B − A_full +0.833 → **True** · B − C_full +0.833 → **True** · arm N below 0.25 → **True**

strictly compositional **True** (v2.8 said True) · reaches it unprompted (B_narrow ≥ 0.5) **True** · halves (True, True) agree **True**

### `di_journal_of_a_spi_o13_o20_o22_n15`

Journal of Advanced Ceramics · drafter label **discriminating** · upstream `journal_of_a_spi_o13_o20` (spine_edge) · 2 combined claims, 4 limit claims

| arm | what it held | mean combined | mean limit | mean contradictions |
|---|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.000 | 0.000 | 0.000 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 0.583 | 0.458 | 0.667 |
| **C** | earlier result only, narrow question (v2.8) | 0.500 | 0.000 | 0.000 |
| **A_full** | measurement + panels, **full** question | 0.000 | 0.000 | 0.000 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.250 | 0.000 | 0.000 |
| **N** | nothing but the full question | 0.000 | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 0.250 | 0.208 | 0.000 |

B − A_full +0.583 → **True** · B − C_full +0.333 → **True** · arm N below 0.25 → **True**

strictly compositional **True** (v2.8 said False) · reaches it unprompted (B_narrow ≥ 0.5) **False** · halves (True, False) agree **False**

### `di_materials_ch_com_o1_o7_o3_r1`

Materials Characterization · drafter label **discriminating** · upstream `materials_ch_com_o1_o7` (complementary) · 4 combined claims, 3 limit claims

| arm | what it held | mean combined | mean limit | mean contradictions |
|---|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.000 | 0.000 | 0.000 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 1.000 | 0.444 | 0.667 |
| **C** | earlier result only, narrow question (v2.8) | 0.000 | 0.056 | 0.000 |
| **A_full** | measurement + panels, **full** question | 0.000 | 0.000 | 0.667 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.000 | 0.000 | 0.000 |
| **N** | nothing but the full question | 0.000 | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 0.333 | 0.222 | 1.500 |

B − A_full +1.000 → **True** · B − C_full +1.000 → **True** · arm N below 0.25 → **True**

strictly compositional **True** (v2.8 said True) · reaches it unprompted (B_narrow ≥ 0.5) **False** · halves (True, True) agree **True**

### `di_journal_of_m_spi_o15_o17_o16_m2`

Journal of Magnesium and Alloys · drafter label **conditional mechanism** · upstream `journal_of_m_spi_o15_o17` (spine_edge) · 4 combined claims, 5 limit claims

| arm | what it held | mean combined | mean limit | mean contradictions |
|---|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.042 | 0.200 | 0.000 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 0.917 | 0.533 | 1.167 |
| **C** | earlier result only, narrow question (v2.8) | 0.208 | 0.800 | 0.167 |
| **A_full** | measurement + panels, **full** question | 0.083 | 0.000 | 1.167 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.042 | 0.533 | 0.167 |
| **N** | nothing but the full question | 0.000 | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 0.750 | 0.767 | 0.000 |

B − A_full +0.833 → **True** · B − C_full +0.875 → **True** · arm N below 0.25 → **True**

strictly compositional **True** (v2.8 said True) · reaches it unprompted (B_narrow ≥ 0.5) **True** · halves (True, True) agree **True**

### `di_bioactive_ma_com_o11_o12_n18_o15_n20`

Bioactive Materials · drafter label **associative** · upstream `bioactive_ma_com_o11_o12_n18` (complementary) · 3 combined claims, 4 limit claims

| arm | what it held | mean combined | mean limit | mean contradictions |
|---|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.000 | 0.375 | 0.000 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 1.000 | 0.667 | 0.000 |
| **C** | earlier result only, narrow question (v2.8) | 0.000 | 0.167 | 0.000 |
| **A_full** | measurement + panels, **full** question | 0.000 | 0.292 | 0.000 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.000 | 0.000 | 0.833 |
| **N** | nothing but the full question | 0.000 | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 1.000 | 0.708 | 0.000 |

B − A_full +1.000 → **True** · B − C_full +1.000 → **True** · arm N below 0.25 → **True**

strictly compositional **True** (v2.8 said True) · reaches it unprompted (B_narrow ≥ 0.5) **True** · halves (True, True) agree **True**

### `di_advanced_fun_spi_o1_o4_o6_n10`

Advanced Functional Materials · drafter label **associative** · upstream `advanced_fun_spi_o1_o4` (spine_edge) · 7 combined claims, 4 limit claims

| arm | what it held | mean combined | mean limit | mean contradictions |
|---|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.024 | 0.000 | 0.333 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 0.595 | 0.792 | 0.167 |
| **C** | earlier result only, narrow question (v2.8) | 0.024 | 0.375 | 0.167 |
| **A_full** | measurement + panels, **full** question | 0.024 | 0.000 | 0.333 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.000 | 0.167 | 0.167 |
| **N** | nothing but the full question | 0.000 | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 0.595 | 0.667 | 0.667 |

B − A_full +0.571 → **True** · B − C_full +0.595 → **True** · arm N below 0.25 → **True**

strictly compositional **True** (v2.8 said True) · reaches it unprompted (B_narrow ≥ 0.5) **True** · halves (True, True) agree **True**

### `di_journal_of_m_spi_o14_o10_o11_f2`

Journal of Materials Science & Technology · drafter label **conditional mechanism** · upstream `journal_of_m_spi_o14_o10` (spine_edge) · 3 combined claims, 4 limit claims

| arm | what it held | mean combined | mean limit | mean contradictions |
|---|---|---|---|---|
| **A** | measurement + panels, narrow question (v2.8) | 0.000 | 0.292 | 0.000 |
| **B** | measurement + panels + earlier result, full question (v2.8) | 0.667 | 0.542 | 0.000 |
| **C** | earlier result only, narrow question (v2.8) | 0.000 | 0.167 | 0.000 |
| **A_full** | measurement + panels, **full** question | 0.000 | 0.375 | 0.000 |
| **C_full** | earlier result + its upstream panels, **full** question | 0.000 | 0.292 | 0.000 |
| **N** | nothing but the full question | 0.000 | 0.000 | 0.000 |
| **B_narrow** | arm B's evidence, arm A's **narrow** question | 0.167 | 0.458 | 0.333 |

B − A_full +0.667 → **True** · B − C_full +0.667 → **True** · arm N below 0.25 → **True**

strictly compositional **True** (v2.8 said True) · reaches it unprompted (B_narrow ≥ 0.5) **False** · halves (True, True) agree **True**

## The item v2.8 failed, which this run appears to rescue

v2.8 failed `di_journal_of_a_spi_o13_o20_o22_n15` because arm C -- the earlier result alone, asked a coherent narrow question -- reached 0.500 of its combined claims, identically across all 6 samples. Under this run's strict rule it passes, because C_full reaches only 0.250.

**I do not read that as a rescue.** The difference between arm C and arm C_full is not more evidence, it is the "not provided" marker telling the same answerer to stop. The v2.8 finding stands: the earlier result alone reaches half this item's combined claims, so one of its two combined tags is wrong.

It is also the one item whose split halves disagree (True then False), with C_full moving 0.167 to 0.333 between them. On every reading it is the weakest of the 8 and should not be counted as compositional without a human looking at its two combined claims.

## Items that dropped out

None. Every item v2.8 called compositional survives the strict rule.

## Reaching it unprompted

Arm B_narrow holds arm B's full evidence but is asked arm A's narrower question, so it is never pointed at the combination. It reaches the combined claims (mean ≥ 0.5) on **4 of 8** items. This does not gate anything; it is the difference between an item whose combination a reader would find and one that has to be asked for.

| item | B (full question) | B_narrow (narrow question) | reaches unprompted |
|---|---|---|---|
| `di_acta_materia_com_o10_o14_o12_n13` | 0.600 | 0.233 | no |
| `di_advanced_ene_spi_o1_o12b_o20_n10` | 0.833 | 0.667 | yes |
| `di_journal_of_a_spi_o13_o20_o22_n15` | 0.583 | 0.250 | no |
| `di_materials_ch_com_o1_o7_o3_r1` | 1.000 | 0.333 | no |
| `di_journal_of_m_spi_o15_o17_o16_m2` | 0.917 | 0.750 | yes |
| `di_bioactive_ma_com_o11_o12_n18_o15_n2` | 1.000 | 1.000 | yes |
| `di_advanced_fun_spi_o1_o4_o6_n10` | 0.595 | 0.595 | yes |
| `di_journal_of_m_spi_o14_o10_o11_f2` | 0.667 | 0.167 | no |

## Split halves

| item | samples 1-3 | samples 4-6 | agree |
|---|---|---|---|
| `di_acta_materia_com_o10_o14_o12_n13` | True | True | yes |
| `di_advanced_ene_spi_o1_o12b_o20_n10` | True | True | yes |
| `di_journal_of_a_spi_o13_o20_o22_n15` | True | False | no |
| `di_materials_ch_com_o1_o7_o3_r1` | True | True | yes |
| `di_journal_of_m_spi_o15_o17_o16_m2` | True | True | yes |
| `di_bioactive_ma_com_o11_o12_n18_o15_n2` | True | True | yes |
| `di_advanced_fun_spi_o1_o4_o6_n10` | True | True | yes |
| `di_journal_of_m_spi_o14_o10_o11_f2` | True | True | yes |

## Cost

Estimated before starting: **384 calls** (192 answers, 192 gradings).

| stage | model calls | relays | wall minutes | seconds per call |
|---|---|---|---|---|
| answers | 192 | 4 | 10.1 | 3.14 |
| gradings | 202 | 5 | 31.3 | 9.31 |

**Actual: 394 calls, 41.4 minutes** at the 20-agent cap. Every reply verified byte for byte against its prompt file from the agent's own transcript.

## Where the data is

- `results/v2p8/control/arms/` — the 4 new arms, 6 samples each
- `results/v2p8/control/grade/` — every grading with its quotes
- `results/v2p8/control/control.json` — arm means, the strict decision, split halves
- the v2.8 arm A, B, C answers and gradings are reused unchanged from `results/v2p8/arms/` and `results/v2p8/partC.json`

Every verdict is model against model.
