# Panel detection over MatMech figures

Detects and crops sub-panels in all 425,295 MatMech figures with the MatMMExtract YOLO12-m panel
checkpoint, writing results *beside* the dataset and never modifying it.

- **Checkpoint:** `CMEG-IITR/matmmextract`, `examples/.weights_cache/10garsNWEdgzMGX9nyDE8dMABkU_3BYp9.pt`
  SHA-256 `7a92fbc6571ef025575db6613b78b968c7e340f98a044341bb8581cd11f2605f` (22 classes: A–T, `single`, `common`).
- **Run version:** `matmmextract-yolo12m/7a92fbc6571e/imgsz640/v1` (imgsz 640, conf 0.25, iou 0.5, half precision).
  Upstream's own examples default to imgsz 1024 / conf 0.6; the 1% re-run at 1024 is the side experiment.
- **Hosts:** spark-112b (192.168.100.10) and spark-0b70 (192.168.100.11), one NVIDIA GB10 each,
  driver 580.82.09 / CUDA 13.0, torch 2.14.0+cu130, ultralytics 8.4.156 (see `env_*.txt`).
- **Sharding:** `crc32(doi_folder) % n_hosts == host_idx`, then `// n_hosts % n_gpus == gpu_idx`.
  No coordination between hosts; 30,720 + 31,046 = 61,766 folders.

## Output

`<doi_folder>/panels/panels.json` and `<doi_folder>/panels/crops/<figure stem>_<label>.jpg`
(quality 90, cut from the original at integer pixel coordinates). Corpus-level records merge into
`<root>/panels_run/`: `manifest.jsonl`, `errors.jsonl`, `summary.json`, `review/`.

A folder is skipped when its `panels.json` already carries the same `run_version`, so the job is resumable.

## Rules applied after detection

Rules 1–7 are from the operator plan: broken records to `errors.jsonl`, caption label extraction,
single-figure rule, duplicate-label dedupe, nested-box removal, mismatch flagging, two-level labels.

Two rules were **added after the dry run**, which showed single-panel schematics receiving two or three
stacked whole-frame boxes under different letters (rule 5 does not catch these, since it only removes
nested boxes of the *same* label):

- **3b whole-frame:** every box covers ≥85% of the image and the caption names no panels → `is_single`, no crops.
- **5b cross-label overlap:** drop a box whose IoU with a higher-scoring kept box exceeds 0.7, or that sits
  >90% inside it, whatever its label. Recorded under `duplicates` with `reason: cross_label_overlap`.

## Verification

`verify_untouched.py` checks every original file against the **release zip's own CRC32s**, which is a
stronger baseline than a checksum list taken just before the run.
