# Modality-view pages with the panel data embedded

**Date:** 2026-09-20. Input: the 32 v05 argument graphs ([`V05_BATCH.md`](V05_BATCH.md)) and the panel stores
(`panels.json`, `match.json`, `ocr.json`, crops). Renderer: the modality-graph kit.

Each paper renders as one page: five argument states down the middle, measurement lanes beside them, and every
evidence node showing the crops it was read from with their caption spans and OCR facts.

## What was built

| Step | Script | Result |
|---|---|---|
| Technique normalisation | `taxonomy/normalize_technique.py` | 167 strings → `FAMILY:mode`, 0 unmapped |
| Collapse to the modality view | `taxonomy/collapse_modality.py` | 32 specs, 311 lane nodes, 597 panel-id citations |
| Checkpoint diff | `taxonomy/diff_specs.py` | see [`CHECKPOINT.md`](../taxonomy/specs_v05/CHECKPOINT.md) and [`DISAGREEMENTS.md`](DISAGREEMENTS.md) |
| Embed panels | `taxonomy/embed_panels.py` | 505 crops + whole figures embedded as data URIs |
| Render | kit `build_all.py --specs` | 32 pages, 43 MB total |

**Lanes across the 32 papers:** microscopy 32, classical 32, diffraction 21, atomistic 6, spectroscopy 4.
**Necessity of the 311 lane nodes:** redundant 264, corrective 27, necessary 17, decorative 3.

## The verbatim rule

`definition` and `use` are copied from `match.json` exactly as the caption segmentation produced them, and a
`B1_caption_empty` figure keeps an empty definition. Nothing is paraphrased and no caption is generated: the
point of putting the crop beside the span is that a reader can see whether they agree, and a generated caption
would hide the disagreement the view exists to expose. `letter`, `tier`, `ocr_agrees` and `cues` come from the
stores, and `ocr_agrees` is `null` with `cues` omitted when a paper has no OCR record.

## Checks

1. **Every cited id resolves or is explained.** 505 of 527 distinct cited ids are embedded. The other 22 have
   no crop file, each named in that spec's `assets_note`. **0 unexplained.**
2. **No unused entries.** 0 embedded panels that no node cites.
3. **Browser check on three pages, one node per lane** (headless Firefox, counting `aside img`): 10 of 10 nodes
   matched, where expected = embedded ids cited + whole figures present.

   | page | node | expected | shown |
   |---|---|---|---|
   | adma.201404945 | M1 (micro), C3 (classic) | 2, 2 | 2, 2 |
   | s40145-019-0334-4 | M1 (micro), M3 (diff), C5 (classic) | 4, 1, 1 | 4, 1, 1 |
   | nanolett.6b04294 | M1, M3, C4, M6, M7 (5 lanes) | 2, 5, 2, 2, 4 | 2, 5, 2, 2, 4 |

4. **Five crops checked by eye against their definition span.** All five are the panel the span describes and
   carry the right letter. Two spans are complete sentences; **three are truncated fragments** — "Li/PCO cell
   and", "625, and", "AZ91-20SiCp composite and". This is the caption-span lag already recorded in
   [`V05_BATCH.md`](V05_BATCH.md): the segmentation drops text when the caption puts the letter after its
   description. It is a finding for the matching run, not something to fix by swapping the image.

   One OCR cue is also wrong in the sample: a 100 µm scale bar read as "scale bar 108Mm".

5. **Sizes.** Largest page 2.74 MB, median 1.40 MB, every page under the 16 MB limit. No page needed the
   figure-dropping or 700 px fallback; the 11 `assets_note` entries are all missing-crop explanations.

## Missing rather than wrong

- **22 cited ids have no crop**, because the panel is the whole figure: the detector writes no crop for a
  single-panel figure, so the page shows the figure itself instead.
- **Insets and tier C figures** still carry `panel_ids: []` on their nodes, as in the graphs.
- **Half the graphs never recorded an instrument**, so lane assignment falls back to the node's label and then
  its modality; every lane node records `tech_source`.

## Repo note

Committed specs have the base64 image data stripped (0.79 MB in total instead of 42 MB). Regenerate the full
specs and pages on the host with:

```
python taxonomy/embed_panels.py --root matmech --specs taxonomy/specs_v05
cd modality_kit/kit && python3 build_all.py --specs ../../taxonomy/specs_v05
```

The kit needed three small local fixes to run off-host: a guard around the built-in Ni-Co example's absolute
path, a stub for its metadata, and the template path resolved next to `build_all.py`.

**No human has checked any of this.** Every accuracy number above is one agent's reading against another's.
