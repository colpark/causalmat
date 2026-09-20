# Panel-crop OCR and the SEM + multimodal subset

**Date:** 2026-09-19/20. Follows the detection and match runs in [`PANELS.md`](PANELS.md).

Two things happened here: a supply count that picked the subset worth spending GPU time on, and an OCR run over that subset's crops.

## 1. Which papers are worth the compute

`scripts/panels/fm_supply.py` counts papers carrying SEM **and** three or more modalities that an
available tool can act on. Evidence per paper is pooled from three independent sources, so a modality
counts when any of them names it:

- **panels** — modality and technique cues on accepted (tier A/B) panel definitions plus caption preambles;
- **flags** — MatMech's own `microscopic_image` flag;
- **methods** — the experiment `type`/`name` strings in MatMech's extracted mechanisms.

| Cut | Papers |
|---|---|
| All | 61,766 |
| With SEM | 26,700 (43%) |
| **SEM + 3 or more tool-addressable modalities** | **16,487 (27%)** |
| …and the material name parses as a formula (MLIPs and generators apply directly) | 2,646 |

SEM was corroborated by two or more sources in 17,343 of the 26,700. The 16,487 papers hold 124,285
figures, 91,589 of them tier A/B, carrying 252,875 accepted panels and 368,310 crops.

**Modality depth among SEM papers:** 3 modalities 7,507 · 4 modalities 5,033 · 5 modalities 2,603 ·
6 or more 1,344 · two or fewer 10,213.

**Modalities present in the 16,487, and the tool that takes that input** (availability tiers from the
operator's own list: *immediate* = open licence, pip or git, no registration):

| Modality | Papers | Tool, immediate tier | Also exists, not counted on |
|---|---|---|---|
| electron micrograph | 16,482 | SAM, DINOv2; abTEM/Prismatic, CASINO | DINOv3 (gated), EM-DINO/EMCF (licence unclear) |
| vibrational/optical spectrum | 7,917 | Quantum ESPRESSO + Phonopy | |
| diffraction pattern | 7,765 | pymatgen XRD, GSAS-II | TOPAS (procurement); XtalNet, deCIFer, DiffractGPT (unclear) |
| electrochemical response | 4,861 | PyBaMM | |
| elemental map | 4,287 | DTSA-II, CASINO | PENELOPE (gated) |
| mechanical response | 3,967 | LAMMPS + MLIP | Abaqus (procurement) |
| core-level spectrum | 3,628 | SESSA (XPS) | FEFF10 (gated); OmniXAS (unclear) |
| optical/fluorescence micrograph | 3,459 | SAM, DINOv2 | |
| atomistic simulation | 3,291 | LAMMPS + MLIP, Quantum ESPRESSO | VASP (procurement) |
| scanned-probe micrograph | 2,719 | SAM, DINOv2 | |
| composition/structure | 2,646 | MACE, MatterSim, Orb-v3, SevenNet; MatterGen, DiffCSP | UMA (gated); MACE-OMAT/MH/POLAR, GRACE (academic) |
| thermal/phase response | 1,976 | Phonopy | Thermo-Calc (procurement) |
| orientation map | 1,130 | EMsoft | |

Every count rests on immediate-tier tools only.

**Most common combinations:** XRD + SEM/TEM + spectrum 636 · SEM/TEM + optical microscopy + spectrum 519 ·
XRD + electrochemistry + SEM/TEM 399 · simulation + SEM/TEM + spectrum 386 · SEM/TEM + AFM/STM + spectrum 332 ·
XPS + XRD + electrochemistry + SEM/TEM + spectrum 268 (five modalities, all with tools).

**Where they sit:** Adv. Funct. Mater. 4,309 · Adv. Mater. 3,718 · Acta Mater. 2,786 · Nano Lett. 2,688 ·
Adv. Energy Mater. 896, the rest thin. By year they peak in 2020 (1,841) and fall away after 2021, so
contamination-clean supply stays tiny: 161 papers from 2022 on.

**Caveats.** Modalities are inferred from text, never from pixels. "A tool takes this input" is not "the tool
measures the scored quantity" — that is the construct-validity check, and the earlier materials run closed two
FM channels at exactly that step. `composition/structure` is undercounted because it needs the material name
to parse as a formula, which drops "Mg alloy" and "cotton fabric".

## 2. OCR over the subset's crops

`scripts/panels/ocr_panels.py`, RapidOCR with the PP-OCRv4 models bundled in the wheel (no runtime downloads).
Run version `rapidocr-ppocrv4/cuda-cap900/v1`. Scope: the 16,487-paper subset, 368,310 crops, sharded
`crc32(doi) % 2` — the same rule as detection, so each host already holds exactly the crops it processes.

Per crop it records every token with its box and score, plus: `letter` (a top-left token matching a panel
label, compared against the detector's label as `letter_agrees`), `cues` (technique votes from axis labels and
instrument banners), `n_tokens`, `n_numeric_tokens` and `has_scale_bar`. Output goes to `<doi>/panels/ocr.json`;
`panels.json` is not modified.

### Getting it onto the GPU

The first configuration ran on the CPU without saying so. onnxruntime listed `CUDAExecutionProvider` but fell
back, because CUDA needs cuDNN and these ARM hosts have no system cuDNN. Pointing `LD_LIBRARY_PATH` at the
copy bundled inside the torch install fixed it. A second problem was thread oversubscription: 18 worker
processes each spawning ~20 ONNX threads on 20 cores.

| Configuration | Throughput |
|---|---|
| CPU, 18 procs, default threads | 1.4 crops/s |
| CPU, threads capped to 1 per process | 10.6 crops/s |
| GPU, single process | 12.3 crops/s (CPU single process: 2.6) |
| **GPU, 6 procs per host** | **~30 crops/s per host** |
| GPU, 8 procs per host | 20 crops/s — contention, so 6 is the setting |

Also applied: long side capped to 900 px and `det_limit_side_len=640`, which was ~20% faster on a 60-crop
benchmark with the same token count; crops with a short side under 300 px are upscaled 2× instead.

### Result

The run finished in about 102 minutes per host (29.6 and 30.1 crops/s), reading every crop in the subset.

| | |
|---|---|
| Crops processed | 368,310 across 16,360 papers |
| Crops with no text at all | 2,631 |
| Crops where a panel letter was read | 259,813 (71%) |
| **Letter agrees with the detector** | **93.5%** |
| Letter disagreements | 16,909 |
| Crops carrying a scale bar | 101,413 |
| Errors | 0 |

**What the crops say they are**, from axis labels and instrument banners: micrograph 97,241, electrochemistry 18,388,
XPS 8,882, optical spectroscopy 7,483, XRD 7,138, Raman 2,793, mechanical 2,480, FTIR 2,149, SEM banner 1,630, then EDS, XAS,
thermal and EDS line scan in the hundreds.

The disagreements are the output, not a defect: they are the second reader for the 6,584
`B2_detector_off_by_one` figures the match run could not resolve. Every disagreement checked by eye so far was
the OCR misreading, clustered on `d` read as `p` or `q`, with the detector right.

Merged into `<dataset>/ocr_run/` by `scripts/panels/merge_ocr.py`: `manifest.jsonl`, `errors.jsonl`,
`summary.json`, and `review/` with 296 crops drawn with their OCR boxes, spread over cue classes and including
letter disagreements.

**Acceptance checks.** Crop coverage: every crop in the subset has a record and `errors.jsonl` is empty.
Letter agreement is reported above, overall; the per-tier split for B2 figures is computed in the match run's
own records. Cue precision per class has **not** been checked by eye yet — the review sample is built and
waiting, and no class should feed the modality pass until it is.

The letter disagreements are the point of this run, not a defect to repair here: they are the second reader
for the 6,584 `B2_detector_off_by_one` figures the match run could not resolve.
