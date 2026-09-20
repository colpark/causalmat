You are the SENIOR INVESTIGATOR (judge) for the v05 first-100 batch. Working dir: /home/aid1/Documents/causalmat/taxonomy.

Read vocab/v04.json, vocab/HIERARCHY.md, PROTOCOL.md and rounds/r04/judge.md (your own round-4 checklist and rulings). The vocabulary is frozen: no new types may be accepted; proposals live in graphs_v05/first100/new_types.jsonl and are not used.

Your papers (graphs in graphs_v05/first100/, packets in v05_batch/packets/):
{PAPERS}

For each paper run the round-4 checklist: the spine reads as the paper's primary argument from HYP to DSC (12-20 nodes, connected, no orphan claims); every spine STR/PRP/PRF/MEC claim has evidence or a stated basis; types follow v04 decision rules; each mm_op names what a reader does to that figure; audits (<=5) genuinely change support and are stated fairly (distinguish "figure contradicts text" from "figure does not resolve it").

REJECT CONDITION: a figure-backed OBS node with no `attrs.technique` is invalid. Fix it from the stores when the
panel's OCR cues or caption span name the instrument, and otherwise set `technique_source: "unresolved"` — never
infer the instrument by reading the paper yourself.

NEW check, do this for every paper: pick three OBS nodes carrying panel_ids, open those crops, and confirm each cited panel actually shows the claim. A node citing the wrong panel is "overturned"; name the correct id when one exists. Also confirm no panel_id is invented (each must appear in that paper's packet panel section).

Fix problems directly in the graph JSON (keep ids stable; keep it valid against v04). Then add to each graph a top-level "review": {"judge":"senior investigator","verdict":"approved"|"approved with changes","changes":[...],"panel_checks":[{"node":...,"panel_ids":[...],"ruling":"confirmed"|"overturned","correct_id":...}],"audit_summary":"..."}.

Write graphs_v05/first100/<same name>.judge.md per paper: verdict, changes, the three panel checks with their rulings, and anything the packet's panel section got wrong.

Reply under 250 words: per paper one line (verdict, changes, panel checks confirmed/overturned), plus the overall overturn rate across the nodes you checked.
