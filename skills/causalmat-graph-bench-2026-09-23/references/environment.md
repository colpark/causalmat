# Environment

Everything the pipeline needs, with the steps a human must do marked **[MANUAL]**.

## Hardware actually used

| | |
|---|---|
| Hosts | `spark-112b` (192.168.100.10), `spark-0b70` (192.168.100.11) |
| GPU | 1 × NVIDIA GB10 each, driver 580.82.09, CUDA 13.0 |
| Disk | 16 GB zip → ~20 GB extracted, + 46 GB of panel crops, + ~230 MB per 100-paper export |
| Sharding | `crc32(doi_folder) % n_hosts == host_idx`, then `// n_hosts % n_gpus == gpu_idx`. No coordination between hosts. |

One host works. Two halves the wall time of A1 and A3. Nothing later needs a GPU.

## Python

Detection and OCR hosts (`scripts/panels/env_spark-112b.txt`):

```
numpy==2.5.2
pillow==12.3.0
torch==2.14.0+cu130
torchvision==0.29.0+cu130
tqdm==4.70.1
ultralytics==8.4.156
```

Plus, for the later stages on any host:

```
rapidocr-onnxruntime     # A3, PP-OCRv4 models bundled in the wheel
pytesseract              # A2 stage 5 only, optional; without it flagged panels carry ocr_letter=null
reportlab                # C4 export PDFs
pillow                   # C4 export PNGs
scikit-learn scipy numpy # the text-only floor, scripts/text_floor.py
```

System binary: **`pdftotext`** (poppler-utils) for the export's answer-leak check. Without it the check
falls back to `pypdf`; with neither, the leak check silently reports "no extractor" — treat that as a
failed check, not a pass.

Font: `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf` and `-Bold`. The export registers these by
absolute path and will not start without them.

## The dataset

**[MANUAL]** `scripts/fetch_data.sh` downloads MatMech v5 from figshare
(`10.6084/m9.figshare.29815979`, CC BY 4.0), verifies MD5 `e56587094485d19b2595ee38339843e9`, extracts to
`./matmech`, and asserts 61,766 `data.json` records. The download is 16 GB and frequently needs resuming;
the script passes `-C -` and retries, but a human should watch it finish.

Cite: Liu et al., *Scientific Data* 13:269 (2026), https://doi.org/10.1038/s41597-026-06598-5.

**Never modify anything under `matmech/`.** Every stage writes *beside* the data:
`<doi>/panels/`, `<root>/panels_run/`, `<root>/match_run/`, `<root>/ocr_run/`.
`scripts/panels/verify_untouched.py` checks every original against the **release zip's own CRC32s** —
a stronger baseline than a checksum list taken just before the run. Run it after A1 and A3.

## The sub-panel detector

**[MANUAL]** The MatMMExtract YOLO12-m panel checkpoint (the "matscifig" sub-panel algorithm) is not in
this repo and is not downloadable without accepting the upstream terms.

- Source: `CMEG-IITR/matmmextract`, file
  `examples/.weights_cache/10garsNWEdgzMGX9nyDE8dMABkU_3BYp9.pt`
- SHA-256 `7a92fbc6571ef025575db6613b78b968c7e340f98a044341bb8581cd11f2605f`
- 22 classes: `A`–`T`, `single`, `common`
- Place it where `scripts/panels/detect_panels.py` expects it (`WEIGHTS` at the top of the file) or edit
  that constant.

**Verify the hash before running.** The run version string embeds it
(`matmmextract-yolo12m/7a92fbc6571e/imgsz640/v1`) and resumability keys off that string, so a different
checkpoint silently re-runs everything under a new version rather than erroring.

Parameters used: `imgsz 640, conf 0.25, iou 0.5`, half precision. Upstream's own examples default to
`imgsz 1024 / conf 0.6`; that is a different run, not a drop-in substitute.

## Publisher full text

**[MANUAL]** The packet builder uses publisher XML where it can get it. This needs API credentials the
repo does not carry:

```
ELSEVIER_API_KEY        ELSEVIER_INST_TOKEN        SPRINGER_API_KEY
```

Without them the packet header says `text_source: captions_only` and every graph built from it rests on
captions alone. The reference run used `captions_plus_linked_text` — captions plus the paper's own
sentences as linked by the PDF parser — which is what `--linked-text` gives you without any key.
**Wiley and ACS have no fetcher**; those papers are caption-plus-linked-text whatever you set.

## The agent harness

The B and C stages are agentic and assume Claude Code with subagents.

- **Concurrency cap 20.** `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`. Relay children count against it, so a
  relay dispatching 6 at a time plus three other relays will hit the cap and stall. Keep total in-flight
  children under ~16 and let relays retry on refusal.
- **[MANUAL] The subagent registry is cached.** Editing a file in `.claude/agents/` does not take effect
  until Claude Code restarts. After any edit to a `net-*` agent, restart and verify by dispatching one
  job and reading back its rules before trusting a batch.
- The seven agents are in `agents/` beside this file. Copy them to `.claude/agents/`.

## Credentials for publishing

**[MANUAL]** Pushing the branch needs a GitHub token. Pass it per push through a one-shot credential
helper reading an environment variable; never write it to `git config`, `~/.git-credentials` or any file
in the repo:

```bash
GH_TOKEN=... git -c credential.helper= \
  -c credential.helper='!f() { echo username=x-access-token; echo password=$GH_TOKEN; }; f' \
  push origin <branch>
```

An agent running under a permission classifier will usually be **denied** this, because the token appears
in the command string. That is correct behaviour. Have the human run the push.

A prior run of this pipeline wrote a token in plaintext into a helper script and into
`~/.git-credentials` via a global `credential.helper=store`. If you inherit such a repo, rotate the token.

## What has no automated substitute

1. Accepting the MatMMExtract terms and placing the checkpoint.
2. Publisher API keys, if you want real full text.
3. Restarting the harness after editing a subagent definition.
4. The GitHub push.
5. Watching the 16 GB download finish.
6. Deciding whether a closure finding ends the project. The pipeline will happily produce items from a
   corpus that cannot carry a benchmark.
