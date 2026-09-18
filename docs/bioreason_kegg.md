# BioReason on KEGG: how the data is built, and what the FM channel actually adds

Sources: arXiv 2505.23579v2 (https://arxiv.org/html/2505.23579), github.com/bowang-lab/BioReason, HuggingFace `wanglab/kegg`, `wanglab/variant_effect_coding`, `wanglab/variant_effect_non_snv`. Rows marked *(our check)* were computed on the HF parquet files on 2026-09-18. Everything else cites the paper or repo.

## 1. From KEGG to items

| Piece | What it is | Locator |
|---|---|---|
| Graph | KEGG **Network Variants**: 298 networks. Each is a symbolic string, e.g. `(PDE11A*,PDE8B*) // cAMP -> (PRKAR1A+PRKACA) -> ... => (STAR,CYP11B1) -> Cortisol`, where `*` marks the variant gene | Fig. 2A, §4.1.1 |
| Measurement modality | Reference and alternate DNA windows of ±2000 bp from GRCh38 around each variant. Variants are cross-linked to ClinVar, dbSNP, OMIM and COSMIC | `data/KEGG_Data_1..3.ipynb`, `CONFIG['sequence_window']=2000` |
| Question | Chromosome, network definition and gene list, then "what disease does this `<GENE>` allele contribute to?". The nucleotide change is **not** in the text; it is only in the DNA pair | HF `question` field |
| Answer | A disease label from 37 classes, e.g. "cushing syndrome" | §5.1 |
| Reasoning trace | Written by **Claude 3.7 Sonnet** (temperature 0.2), 8 to 12 causal steps. The prompt includes the gene, the ref/alt allele, the network **and the answer label**. No verification step exists | `BioReasoning_DataCuration_KEGG.ipynb::create_variant_prompt`, §4.1.2 |
| Size and splits | 1,449 items: train 1159, val 144, test 146. The paper's "290 test" is test and val combined. No code shows how the split was made | §5.1, `eval_kegg_dna_vllm.py` |

## 2. Model and training

- **Encoder:** a frozen DNA foundation model, either NT-v2-500M or Evo2-1B.
- **Projection:** a single linear layer that maps the DNA embeddings into Qwen3-1.7B or 4B. The ref and alt embeddings sit inside `<dna_start>...<dna_end>`, ahead of the text (`bioreason/models/dna_llm.py:142`).
- **SFT:** LoRA (r32/α64), with loss on the `<think>` trace and the answer.
- **RL:** Dr. GRPO with 8 generations, β=0, 1000 steps, on KEGG train only.
- **Reward:** 2.0 if the label appears as a case-insensitive substring, plus 0.5 for an answer of 10 words or fewer, plus 0.5 for format. The code's default reward functions also add `xmlcount` and `soft_format`, so the maximum reward is 3.75, not the paper's 2.5 (`train_grpo.py:124`).

## 3. Reported results (single runs, no error bars)

| Model | KEGG Acc / F1 |
|---|---|
| Evo2-only (no text) | 88.28 / 72.43 |
| Qwen3-4B (raw DNA pasted as text) | 90.00 / 79.66 |
| Evo2 + Qwen3-4B | 95.17 / 86.14 |
| Evo2 + Qwen3-4B + GRPO | **98.28 / 93.05** |

The variant-effect-prediction sets show larger gaps. On VEP-Coding, Evo2+Qwen4B scores 80.2 accuracy against 49.0 for LLM-only.

## 4. Read through the fm-advantage-benchmark lens

| Skill check | BioReason-KEGG | Consequence |
|---|---|---|
| Shape (`shape.md`) | infer / classify, pick 1 of 37. The role floor sits on the predictor line and no lift is recorded | An agent cannot register value on this task at any accuracy |
| Mechanical floor (P2, I1) | *(our check)* A lookup table giving the majority train label per question string gets **96.9%** eval accuracy. By gene + network it gets 97.2%, and by gene alone 94.8% | The floor already takes about 97% of the ceiling |
| Channel lift (I2) | No arm keeps the text and removes or shuffles the DNA. The LLM-only arm reads about 8k characters of raw nucleotides, which is a weak adjudicator | The DNA channel's lift over the text lookup is at most the 14 ambiguous contexts (39 eval rows). I2 would CLOSE or badly bound it |
| Split integrity (P3) | *(our check)* 289 of 290 eval questions are identical to a train question; there are only 186 distinct questions. All 91 genes appear in train, and 249 of 290 eval reference sequences also occur in train | Near-total leakage between the splits |
| Label source (D4) | The traces are post-hoc rationales written *given the label* (the label appears in 1379 of 1449 traces). They also state ref>alt changes that the model sees only as DNA at SFT time | The traces teach rationalisation, not inference, and they are never graded |
| Grader (Gate 2) | Final-label substring match | This can be gamed by listing several labels. The reasoning is never scored |
| Power (P7, A4) | n=290 at temperature 0; the 95.2→98.3 gain is about 9 items | Below any honest MDE |

**What carries over to MatMech:**
- The architecture: a measurement FM projected into an LLM, then SFT, then GRPO on a verifiable reward.
- The graph-plus-measurement-plus-label recipe.

**What to avoid:**
1. An answer that can be recovered from the text context by lookup.
2. Traces written with the label in hand.
3. Duplicate questions leaking across splits.
4. No ablation that keeps the text and removes only the FM channel.
5. A reward that checks only the final label.

## 5. Not verified

- How the KEGG split was made, and whether val was used for early stopping.
- How the macro-F1 in Table 1 was averaged.
- Which NT embedding layer was used.
- BioReason-Pro (bioRxiv 2026.03.19.712954) covers protein function (ESM3 + GO), not KEGG. Its full text was not read.
