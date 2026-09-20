# causalmat

This repo asks whether the MatMech multimodal causal-mechanism dataset can carry a benchmark of **foundation-model (FM) advantage**. That means tasks where an agent holding domain FM tools makes measurably better decisions than:
- the same agent holding only classical tools, and
- a fixed mechanical pipeline with no agent at all.

The reasoning must be grounded on measurements. The analysis follows the `fm-advantage-benchmark` skill (rev 2) and uses BioReason-on-KEGG as the reference construction.

- **Dataset:** MatMech, Liu et al., *Scientific Data* 13:269 (2026), https://doi.org/10.1038/s41597-026-06598-5
  - Data: https://doi.org/10.6084/m9.figshare.29815979 (v5, CC BY 4.0)
  - Code: https://github.com/61peng/matmech
- **Prior materials run of the skill:** https://github.com/colpark/19C_materials

## Contents

| Path | What |
|---|---|
| [docs/ANALYSIS.md](docs/ANALYSIS.md) | **Main result.** The KEGG ↔ MatMech mapping, corpus counts, the text-only floor, measurement-grounding routes, five candidate tasks with FM-in-the-loop workflows and rulings, and the SFT/RL recipe |
| [docs/TAXONOMY.md](docs/TAXONOMY.md) | **Papers as logical graphs.** A saturation sweep over 60 papers built the final node vocabulary v04 (64 leaves, 22 multimodal operations); it includes 3 reviewed showcase graphs and the MatMech data defects found |
| `taxonomy/` | Protocol, vocabularies v00–v04, per-round graphs/proposals/judge rulings, `graphs_v04/` (60 migrated graphs), `cases/` (showcases), scripts |
| `site/argument_graphs.html` | Interactive page: vocabulary tree, saturation curve, the 3 case graphs with their figures |
| [docs/bioreason_kegg.md](docs/bioreason_kegg.md) | How BioReason builds SFT/RL data on KEGG, with our leakage and lookup checks on its HF data |
| [docs/PANELS.md](docs/PANELS.md) | **Panel extraction and matching.** 424,621 figures run through the MatMMExtract YOLO12 detector on 2 GPUs (1.09 M panel crops), then tiered validation matching every panel to the caption text that defines it and the body text that uses it, plus modality statistics |
| [docs/OCR.md](docs/OCR.md) | **Which papers are worth the compute, and OCR over their crops.** 16,487 papers carry SEM plus 3+ modalities an available tool can act on; RapidOCR reads every crop in that subset on two GPUs |
| `scripts/panels/` | Detector worker, merge, CRC verification, tiered matcher, modality stats, review-packet builder, run summaries |
| `results/fm_supply.json` | Papers carrying SEM plus 3+ modalities that an available FM/encoder/generator can act on, with the tool-availability map |
| `results/panel_modalities.json` | Form and technique breakdown of the 727,627 accepted panels |
| `results/corpus_stats.json` | Corpus counts over all 61,766 records |
| `results/text_floor.json` | TF-IDF mechanical floor for the mechanism-selection and effect-prediction templates |
| `scripts/fetch_data.sh` | Downloads the 16 GB zip, checks its MD5, extracts it to `./matmech` |
| `scripts/corpus_stats.py` | Zero-cost counts (links, evidence depth, modalities, conflicts, candidate supply, years) |
| `scripts/text_floor.py` | Text-only floor with no model (the BioReason-style lookup check) |
| `data/` | Figshare README and dataset summary |

## Headline findings

1. **MatMech is to materials what KEGG is to BioReason.** It is a causal graph, and each of its 207,200 mechanisms carries a reasoning chain taken from the authors' own text, with each step labelled by evidence type. KEGG has no equivalent.
2. **The text-only floor closes the naive task.**
   - Given cause + effect, TF-IDF picks the true mechanism among 5 random rivals **98.5%** of the time. With rivals the retriever itself would choose, it drops to **73%**.
   - This mirrors BioReason-KEGG, where a text lookup reaches about 97%.
   - **98.9% of papers are from 2021 or earlier**, so contamination binds any task whose answer is the paper's own text.
3. **FM advantage has to come from measurements the agent must read or compute.** The dataset holds 425k figure images, including about 19.7k XRD figures and 74.6k mechanisms with a microscopy image, plus 94k mechanisms whose result states a number with a unit. It holds no raw spectra or structures.
4. **The candidates recommended for the next stage (D5) are C3 and C1:**
   - **C3:** diffraction plus microscopy structure consistency, with an MLIP acting on agent-built structures and a forward-model residual as grader.
   - **C1:** mechanism discrimination by evidence acquisition, in a replayable in-paper environment.
   - **Controls:** effect prediction (C4, the direct BioReason analogue) is kept only as SFT warm-up data and a negative control.

## Reproduce

```bash
scripts/fetch_data.sh
python3 scripts/corpus_stats.py matmech results/corpus_stats.json
uv venv .venv && uv pip install --python .venv/bin/python numpy scikit-learn scipy
.venv/bin/python scripts/text_floor.py matmech results/text_floor.json
```
