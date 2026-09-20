# Paper → logical graph: node vocabulary by saturation sweep

## Goal

Turn every materials paper into **one directed graph**: "this, so this, so this". It should follow the paper's main line of argument:

**hypothesis → selection/design → processing → structure → property → performance → discussion**

Measurements (images and data) sit in between as evidence. The graph loses detail by design. The shared **node vocabulary** is the product: it must be detailed, but as general as possible.

## Objects

**Node.** One logical unit of the argument: an act, a readout or a claim. It has:

- `type`: a path in the vocabulary, e.g. `OBS/diffraction/peak_shift` or `STR/phase/identity`. Types name the **role in the argument**, never the material or technique-specific content.
- `label`: the paper-specific content, ≤ 20 words.
- `attrs`: specifics that are *not* types, e.g. `{technique: "XRD", quantity: "lattice parameter", value: "4.05 Å", material: "Al-Mg"}`.
- `figs`: figure ids from the packet (F1, F2, …) that carry this node.
- `attrs.technique`: **required on every OBS node that carries `figs`.** It names the instrument or method that
  produced the panel, in the controlled form `FAMILY:mode` used by `normalize_technique.py` (`SEM`, `SEM:BSE`,
  `TEM:HRTEM`, `XRD:synchrotron`, `XAS:EXAFS`, `ATOM:DFT`, `PHYS:density`, …). It names the **instrument, not the
  subject**: write `SEM`, never `SEM of worn surfaces`, and leave the subject in the node label. A node whose
  panel comes from two instruments carries both, as a list. Without it the modality view cannot assign a lane,
  and half of the v05 batch had to be back-filled because the field was optional.
- `modality`: required on OBS nodes. One of the modality list in the vocabulary (see `modality_notes`: 1D diffraction traces are `diffraction_pattern`, bar charts are `xy_curve`; if a node reads two panel kinds, split it).
- `provenance` (from v01): required on OBS nodes. `measured` (recorded by an instrument/test) | `derived` (computed in this paper from other OBS; must have an incoming `derives` edge) | `computed` (simulation, theory or model output). Provenance is not a type: the OBS type still names what feature of the data is read.
- `image_support` (from v01): required on every node with non-empty `figs`; states whether the attached figure actually shows the claim, judged from the image, not the caption:
  - `shown`: the figure visibly shows the claim as stated;
  - `partial`: the figure supports only a weaker, qualified or subset version (some panels or samples, within noise, magnification too low);
  - `not_shown`: the figure does not resolve the claimed feature; the claim rests on text or tables;
  - `contradicts`: the figure shows something inconsistent with the claim (e.g. peak position differs from text, arithmetic between panels does not close).
  Put what the image does show in `attrs.image_note`. Content that a figure shows but the text never states becomes its own OBS node with `attrs.text_silent: true` **only if it bears on a spine claim** (it qualifies, contradicts or would change it); otherwise record it in `attrs.image_note` of the nearest OBS node.
- `spine` (from v02): required boolean on every node. `true` marks the paper's primary line of argument; see **Spine and periphery** below.

**Edge.** `{src, dst, rel, mm_op?}`:

- `rel` comes from the edge vocabulary. Keep three rels apart: `evidences` (OBS -> claim), `causes` (physical causation in the material), `supports` (claim -> claim or claim -> DSC reasoning).
- `mm_op` is required when `src` is an OBS node that has a figure, whatever the rel (`evidences`, `derives`, `premise_for`, `contrasts`, ...). It names the **multimodal reasoning operation** that turns the figure into the claim, e.g. `compare_across_conditions` or `measure_feature_metric`. It comes from the mm_op vocabulary, which also grows.

**Generalisation rule.** A distinction is a **type** only if it changes what reasoning happens next. Otherwise it is an **attribute**.

- *Grain size refined* vs *grain size coarsened*: same type, direction as an attribute.
- *Phase identity* vs *phase fraction*: different types, because different inferences follow.

## Spine and periphery (from v02)

Every graph must read as a short core argument ("this, so this, so this") with evidence and audits hanging off it.

**Spine (`spine: true`).** The nodes a reader needs to restate the paper's argument in one paragraph:

- Allowed types: HYP, DES, PRC, STR, PRP, PRF, MEC and DSC/conclusion. OBS and KNW nodes are **never** spine: they are evidence and premises. DSC other than the conclusion is spine only if the paper's headline is that comparison or guidance.
- Size: **10–20 spine nodes per paper**. If you need more, you are putting sub-results on the spine: keep the one claim per stage that the next stage uses, and leave the rest off.
- Connectivity: spine nodes form one connected, stage-ordered path from the first HYP to DSC/conclusion. Each spine node except the first has an incoming edge from another spine node by `motivates`, `realizes`, `feeds_into`, `produces`, `causes`, `explains` or `supports`. At most two parallel branches (e.g. two properties that meet in a trade-off).
- Evidence: every spine STR/PRP/PRF claim has ≥1 incoming `evidences` edge from an OBS node, or `attrs.basis` ≠ `evidenced` (argued | attributed | imposed) so that unsupported links are visible.

**Periphery (`spine: false`).** Rendered around the spine in three derived rings (no extra field needed):

- *evidence*: OBS nodes with an edge into a spine node, plus derives chains feeding them, and the KNW premises they use;
- *audit*: nodes with `attrs.text_silent`, OBS nodes whose edges are `qualifies`/`contrasts`/`rules_out`, and DSC/limitation;
- *side*: other claims (secondary structure, discarded branches, extra property readouts).

**Audit budget.** Audits remain valuable but are secondary. Add an audit node only when it changes the support of a spine claim (qualifies, contradicts, or reveals an alternative the paper ignores). Everything else goes into `attrs.image_note` on the existing OBS node, or into `image_support` of that node. Aim for ≤ 5 audit nodes per paper and 25–40 nodes in total.

## Loop

1. **Round r.** Sample papers stratified over journals. Round sizes run 4, 8, 16, 32, 64, …
2. **Staff (fellow discussants).** Each decomposes its papers with vocabulary v(r−1):
   - opens **at least 3 figures per paper**;
   - writes a graph JSON per paper;
   - writes a proposal file: new types, new rels, new mm_ops, merges/splits of existing entries, each with a definition, justification and example node ids;
   - marks nodes that fit only poorly.
3. **Senior investigator (judge).** Reads v(r−1), every proposal, and spot-checks graphs and figures. For each proposal it rules ACCEPT, MERGE into an existing entry, REJECT (with reason), or RESTRUCTURE the hierarchy. It then writes v(r) and a rulings log.
4. **Metrics.** `metrics.py` computes per round:
   - accepted new leaf types per paper;
   - share of nodes typed with pre-existing entries (coverage);
   - node and edge counts;
   - mm_op growth.
5. **Stop growth** when a round of ≥ 16 papers adds < 0.1 accepted leaves per paper, and coverage by the previous vocabulary is ≥ 95%.
6. **Merge phase.** Staff propose merges to maximise generality. The judge rules, and writes the final hierarchy with definitions and usage counts.
7. **Cases.** Re-decompose 3 papers with the final vocabulary and render them.

## Graph JSON (one file per paper, `rounds/rXX/graphs/<paper_id with / → __>.json`)

```json
{"paper_id": "...", "title": "...", "vocab_version": "v00",
 "nodes": [{"id": "n1", "type": "HYP/...", "label": "...", "attrs": {}, "figs": [], "modality": null, "provenance": null, "image_support": null, "spine": false, "fit": "good|poor", "proposed": false}],
 "edges": [{"src": "n1", "dst": "n2", "rel": "motivates", "mm_op": null}],
 "notes": "information lost; places where the paper's argument branches"}
```

Use `"proposed": true` on a node whose type is a new proposal. Proposed types must also appear in the proposal file.

## Proposal file (`rounds/rXX/proposals_<staff>.json`)

```json
{"staff": "S1", "papers": ["..."],
 "types": [{"path": "STR/phase/fraction", "definition": "...", "why_not_existing": "...", "examples": ["<paper>#n7"]}],
 "rels": [], "mm_ops": [], "modalities": [],
 "merges": [{"merge": ["A", "B"], "into": "C", "why": "..."}],
 "splits": [], "comments": "..."}
```
