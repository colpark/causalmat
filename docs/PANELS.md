# Panel extraction, validation and panel-to-text matching

**Date:** 2026-09-19/20. **Corpus:** MatMech, 61,766 papers, 424,621 figures.

Two runs, both writing *beside* the dataset and changing no original file:

1. **Detection** — sub-panels in every figure, with the MatMMExtract YOLO12-m checkpoint on two GB10 hosts.
2. **Match** — every detected panel tied to the caption text that defines it and the body text that uses it, with a tier per figure.

Scripts: [`scripts/panels/`](../scripts/panels). Outputs live at `<dataset>/panels_run/`, `<dataset>/match_run/` and `<doi>/panels/`.

## 1. Detection run

- **Checkpoint:** `CMEG-IITR/matmmextract`, SHA-256 `7a92fbc6571ef025575db6613b78b968c7e340f98a044341bb8581cd11f2605f`, 22 classes (A–T, `single`, `common`).
- **Run version:** `matmmextract-yolo12m/7a92fbc6571e/imgsz640/v1` (imgsz 640, conf 0.25, iou 0.5, half precision).
- **Hosts:** spark-112b (.10) and spark-0b70 (.11), one NVIDIA GB10 each, driver 580.82.09 / CUDA 13.0, torch 2.14.0+cu130, ultralytics 8.4.156.
- **Sharding:** `crc32(doi) % 2`, giving 30,720 + 31,046 = 61,766 folders. No coordination needed.

| | spark-112b | spark-0b70 | total |
|---|---|---|---|
| Figures | 210,075 | 212,794 | **422,869** (+1,752 from dry runs) |
| Crops | 540,096 | 548,850 | **1,090,345** (46 GB) |
| Skipped | 605 | 663 | **1,275** |
| Wall time | 57.7 min | 66.2 min | |
| Throughput | 60.6 fig/s | 53.6 fig/s | |

**Panel counts:** 32% of figures are single-panel; the rest run from 2 to 20 panels, with 2–6 most common.
**Captions:** 60.6% of figures name panel labels; of those, 64.4% match the detected letters exactly.

**Two rules added after the dry run.** A dry run on 100 random folders showed single-panel schematics
receiving two or three stacked whole-frame boxes under *different* letters. The plan's rule 5 only removes
nested boxes of the *same* label, so these survived and produced duplicate crops:

- **whole-frame:** every box covers ≥85% of the image and the caption names no panels → treat as single, no crops.
- **cross-label overlap:** drop a box whose IoU with a higher-scoring kept box exceeds 0.7, or that sits >90%
  inside it, whatever its letter. Recorded under `duplicates` with `reason: cross_label_overlap`.

**Acceptance checks.** Every DOI folder has a `panels.json` (61,766/61,766). Both hosts ran the same
checkpoint hash and parameters. **All 546,552 original files verified identical against the release zip's own
CRC32s** — a stronger baseline than a pre-run checksum list (`verify_untouched.py`).

## 2. Match run (tiered validation)

Run version `match/v4`; the whole corpus tiers in ~21 s on 18 CPU workers.

| Tier | Figures | Share | Codes |
|---|---|---|---|
| **A** accept | 146,836 | 34.6% | `A_exact` — caption, body text and detector letters agree |
| **B** repair | 159,254 | 37.6% | `B3_single` 134,824 · `B4_text_only` 11,734 · `B2_off_by_one` 6,584 · `B1_caption_empty` 6,112 |
| **C** quarantine | 119,205 | 28.1% | `C1_count_mismatch` 39,528 · `C6_unresolved` 34,352 · `C3_caption_swap` 19,602 · `C4_two_level` 12,307 · `C5_broken_record` 9,036 · `C2_order_violation` 4,380 |

- **Panels:** 727,627 accepted (A + B). 96.6% carry a definition span; 59.5% also carry use sentences from the body text.
- **`fetch_captions.txt`:** 6,112 figures whose captions have empty slots, for a publisher caption fetch.
- **Microscopy figures** (the first consumer): 62.6% Tier A, 21.7% B, 15.7% C — better than the corpus average.

**Three bugs the 200-figure sample check caught before scaling:**

1. `Fig. 3 shows` parsed as panel **s**, and `Fig. 12 for…` as panel **f**. These phantom references inflated
   Tier B4 and faked the caption-swap signature. A bare letter now counts only when glued to the number and
   not followed by another letter.
2. Captions using `(A)` for major panels and `(a)` for sub-panels were flattened into one letter set. That is a
   case-based two-level figure and now routes to `C4`.
3. Figures with **no** boxes were landing in Tier A (empty = empty) and produced no panel record at all. They
   now go to `B3_single` and point at the original image. This moved ~115k figures.

Fixing 1 and 2 took Tier A from 41% to 62% of multi-panel figures.

**Acceptance checks.** *Coverage passes:* all 423,756 detected figures carry a tier and a reason code, and all
1,272 broken figures carry `C5_broken_record`. *Tier accuracy (checks 2–4) is pending human annotation:* the
packet is built at `match_run/review/` — 400 figures (200 A / 120 B / 80 C, stratified by reason code, journal
and panel count), 710 panel rows in `annotation.csv`, 80 figures double-annotated, plus an instruction sheet.
Each image shows the boxes with letters and prints each panel's assigned definition and its source beneath.

**Not run: OCR (Stage 5).** Tesseract is not installed and this host has no passwordless sudo, so the 6,584
`B2_off_by_one` figures carry `ocr_letter: null` and were accepted on reading-order grounds alone.

**Recommended for `match/v5`.** Of the 34,352 `C6_unresolved` figures, a recurring pattern is: the caption
names no panels, while the body text and the detector agree exactly. That is recoverable as a Tier B code
taking definitions from the text, but the operator plan's tier list does not define it, so they stay quarantined.

## 3. Modalities of the accepted panels

Classified from each panel's own definition span plus the caption preamble (the technique is usually named
once in the preamble, while the panel span names only its condition). `panel_modalities.py`, results in
`results/panel_modalities.json`. Two independent axes; a panel may carry several technique cues.

| Form | Overall | Tier A | Tier B |
|---|---|---|---|
| micrograph | 148,314 (20.4%) | 21.4% | 18.0% |
| xy curve | 122,286 (16.8%) | 17.2% | 15.9% |
| spectrum | 63,204 (8.7%) | 9.7% | 6.5% |
| schematic | 61,709 (8.5%) | 8.5% | 8.6% |
| diffraction pattern | 23,988 (3.3%) | 3.2% | 3.5% |
| simulation render | 21,965 (3.0%) | 3.0% | 2.9% |
| spatial map | 12,242 (1.7%) | 1.7% | 1.6% |
| orientation distribution | 8,260 (1.1%) | 1.0% | 1.4% |
| photograph | 8,193 (1.1%) | 1.3% | 0.7% |
| table | 3,821 (0.5%) | 0.5% | 0.6% |
| *unclassified* | 253,645 (34.9%) | 32.4% | 40.5% |

| Technique | Overall | Tier A | Tier B |
|---|---|---|---|
| TEM | 75,945 (10.4%) | 10.8% | 9.6% |
| SEM | 58,751 (8.1%) | 8.5% | 7.1% |
| electrochemistry | 21,686 (3.0%) | 3.7% | 1.4% |
| XRD | 21,544 (3.0%) | 2.9% | 3.2% |
| mechanical test | 20,168 (2.8%) | 2.3% | 3.7% |
| UV-vis / PL | 18,579 (2.5%) | 2.8% | 1.9% |
| AFM / STM | 16,479 (2.3%) | 2.5% | 1.7% |
| optical microscopy | 15,703 (2.2%) | 2.4% | 1.7% |
| simulation / DFT | 12,040 (1.7%) | 1.7% | 1.5% |
| biological assay | 11,891 (1.6%) | 1.9% | 0.9% |
| EBSD | 10,530 (1.5%) | 1.3% | 1.8% |
| XPS | 10,477 (1.4%) | 1.7% | 0.8% |
| EDS / EDX | 8,930 (1.2%) | 1.2% | 1.3% |
| Raman | 7,719 (1.1%) | 1.2% | 0.7% |
| particle size/porosity … NMR | 7,622 … 1,455 | | |
| *no cue found* | 419,407 (57.6%) | 55.4% | 62.8% |

**Top technique-form pairs:** TEM micrograph 34.4k · SEM micrograph 24.0k · XRD diffraction pattern 12.3k ·
UV-vis/PL spectrum 11.5k · electrochemistry curve 8.7k · AFM/STM micrograph 7.7k · Raman spectrum 4.7k ·
XPS spectrum 4.3k · TEM diffraction pattern 4.1k.

**The cross-modal count that matters for reasoning work:** **42,599 Tier A and 5,552 Tier B figures hold panels
of two or more different forms** — a micrograph beside a spectrum, a diffraction pattern beside a curve. Those
~48k figures are where one claim is built from several modalities inside a single figure, which is the
convergence pattern [`TAXONOMY.md`](TAXONOMY.md) found by hand in the 60-paper sweep.

**Caveats.**
- Tier differences are mild and mostly compositional: Tier B holds more single-panel figures, hence its higher
  unclassified share and its lean toward mechanical tests; Tier A holds more spectroscopy and electrochemistry,
  which use lettered multi-panel layouts.
- The unclassified share is not a regex gap. These panels name only a condition ("0.05 wt% ND", "after 5 cycles")
  with the technique stated nowhere in the caption. Classifying them needs the image, which is a vision-model job.
- Technique and form come from text, never from the pixels. Nothing here has been checked against the images
  beyond the review overlays.
