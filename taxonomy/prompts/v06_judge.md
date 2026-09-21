You are the SENIOR INVESTIGATOR (judge) for the v06 pilot. Working dir: /home/aid1/Documents/causalmat/taxonomy.

Read vocab/v04.json, vocab/HIERARCHY.md, PROTOCOL.md and rounds/r04/judge.md. The vocabulary is frozen.

Your papers (graphs in graphs_v06/, packets in v06_pilot/packets/):
{PAPERS}

For each paper, in this order:
1. Run the round-4 checklist (spine reads as the primary argument, 12-20 connected nodes, every spine claim has evidence or a stated basis, v04 decision rules, mm_op names what a reader does, audits <=5 and fair).
2. Open EVERY crop cited in the graph (every panel_id on every node), not a sample. Rule each cited panel "confirmed" or "overturned" for the node that cites it; when overturned, name the correct id if one exists in the panel section, and fix the graph.
3. For every OBS evidence node, check attrs.technique against the crop you opened and against the panel's OCR cue classes (map: /home/aid1/Documents/causalmat/trace_kit/cue_technique.json). Flag every mismatch and fix it (right panel, or drop the citation). Known misfire: the OCR scale-bar detector gives the "micrograph" cue to some plots and maps; when the crop you opened plainly is the right panel for the node and the only conflict is such a false "micrograph" cue, keep or restore the citation and record it under review.cue_overrides [{"node","panel","cue","why"}] (staff dropped several such citations in this batch). Also check attrs.read_from: an observation that restates an annotation string listed for its panel must be "annotation".
4. Check attrs.source and attrs.requires_unseen on every node: a claim that needs a fact no panel shows must be "text" (or "inferred"/"prior_knowledge") with that fact listed.
5. Check "mode" on every claim with two or more causes edges: "alternative" only if a caption or figure shows the choice; otherwise "joint". Fix it.
6. Only after the graph is final: read v06_pilot/judge_only/<paper>.matmech.md and record, WITHOUT editing the graph, for each MatMech cause->effect pair whether the graph supports it, contradicts it, or does not cover it.
Fix problems directly in the graph JSON (keep ids stable, v04-valid). Add a top-level "review": {"judge":"senior investigator","verdict":..., "changes":[...], "panel_checks":[{"node","panel_ids","ruling","correct_id","note"}], "technique_mismatches":[...], "mode_changes":[...], "source_changes":[...], "matmech":{"supports":n,"contradicts":n,"not_covered":n,"pairs":[{"m":"M1","cause":..,"effect":..,"verdict":..,"nodes":[..]}]}}.
Write graphs_v06/<name>.judge.md: verdict, changes, every panel check, technique mismatches, mode changes, the MatMech tally.

Do not run git. Reply under 250 words: per paper one line (verdict, crops checked, overturned, technique mismatches, mode changes, MatMech supports/contradicts/not covered).
