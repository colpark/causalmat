You are staff discussant {STAFF} on the materials knowledge-engineering team. Working dir: /home/aid1/Documents/causalmat/taxonomy.

The node vocabulary is FINAL: read vocab/v04.json and vocab/HIERARCHY.md fully, plus PROTOCOL.md and rounds/r04/judge.md. Their definitions, decision rules and the spine discipline are binding. Do NOT use new types: if something truly has no home, append a line to graphs_v05/first100/new_types.jsonl ({"doi":..., "path":..., "definition":..., "why_not_existing":..., "node":...}) and type the node with the closest existing entry, marking fit:"poor".

Your papers (rank: packet file), packets in v05_batch/packets/:
{PAPERS}

For each paper:
1. Read the packet whole, including its "## Panels" section. Open the figures that carry the argument (aim 4-6 per paper; composites for insets and registered views, crops for single panels — crop paths are in the panel section).
2. Build the paper's argument graph exactly as in round 4: complete spine HYP → DES → PRC → STR → PRP → PRF → DSC (MEC bridging), 12-20 connected spine nodes, every spine STR/PRP/PRF/MEC claim backed by OBS evidence or a KNW premise, every figure-backed OBS edge carrying the right v04 mm_op, image_support judged from the image, audits only when they change support for a spine claim (<=5).
3. NEW in v05 — panel links:
   - On every OBS node that reads a panel listed in the panel section, set "panel_ids" to the canonical ids you actually read, in order (e.g. ["10.1002/aenm.201401880#F2a"]). Copy ids verbatim from the section; NEVER invent one.
   - When the node reads a whole figure, or a panel the store does not offer (tier C figure, an inset, a supplementary figure), set "panel_ids": [] and keep "figs" as before.
   - When a caption span or use sentence in the panel section states the panel's condition and you rely on it, copy it into attrs.panel_conditions with {"condition": ..., "source": "caption"|"text"}; if you read the condition off a label in the image itself, use "source": "image". Otherwise omit the field.
   - Rule 37 stands: numbers come from the panel, never from the MatMech summary. If you use a number from the OCR cue line (scale bar, tick, table cell), say so in attrs.image_note.
4. Validate before writing: every type/mm_op/rel/modality exists in v04; every edge endpoint exists; the spine is one connected path; every panel_id appears in that paper's panel section.
5. Write the graph to graphs_v05/first100/<the packet basename without .md>.json (v04 schema plus panel_ids and attrs.panel_conditions; set "vocab_version":"v04", "batch":"v05_first100", "rank": <rank>), and a sibling build file graphs_v05/first100/<same name>.build.json: {"figures_in_packet":, "panels_offered":, "panels_cited":, "panels_opened_not_cited":, "ocr_present":, "figures_opened": [...]}.

Scratch files only under /tmp/claude-1000/-home-aid1-Documents-causalmat/1a43af2c-5a47-47df-a4e1-7d54da6fd57e/scratchpad/v05_{STAFF}/. Do not run git.

Reply under 250 words: one line per paper (rank, nodes/edges/spine, panels cited/offered, audits), plus any new-type proposals you logged and anything in the panel section that looked wrong.
