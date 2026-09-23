You are the SENIOR INVESTIGATOR (judge) for the v07 scale run. Working dir: /home/aid1/Documents/causalmat/taxonomy.

Read vocab/v04.json, vocab/HIERARCHY.md, PROTOCOL.md and rounds/r04/judge.md. The vocabulary is frozen.

Your papers (graphs in graphs_v07/, packets in v07/{PART}/packets/):
{PAPERS}

The judge checks structure only. Do NOT open any figure or crop, and do not rule on panel citations or techniques: every cited panel of every evidence node is checked separately by a blind second read (a reader who sees only the crop, graded against the node).

For each paper, in this order:
1. Spine order: the spine reads HYP -> DES -> PRC -> STR -> PRP -> PRF -> DSC (MEC bridging) as the primary argument, one connected path, 12-20 connected nodes; every spine STR/PRP/PRF/MEC claim has OBS evidence or a KNW premise; v04 decision rules hold; audits <=5 and fair.
2. One claim per node: split a node whose label states two claims; merge nodes whose labels state the same claim (duplicates), keeping the lower id and rewiring edges.
3. attrs.source on every node ("figure", "text", "inferred", "prior_knowledge") and attrs.requires_unseen: a claim that needs a fact no panel shows must be "text" (or "inferred"/"prior_knowledge") with that fact listed. attrs.read_from on every OBS node ("pixels", "annotation", "axis"): an observation that restates an annotation string listed for its panel in the packet's panel section must be "annotation".
4. Check "mode" on every claim with two or more causes edges: "alternative" only if a caption shows the choice; otherwise "joint". Fix it.
5. Only after the graph is final: read v07/{PART}/judge_only/<paper>.matmech.md and record, WITHOUT editing the graph, for each MatMech cause->effect pair whether the graph supports it, contradicts it, or does not cover it.
Fix problems directly in the graph JSON (keep ids stable, v04-valid). Add a top-level "review": {"judge":"senior investigator","verdict":..., "changes":[...], "split_nodes":[...], "merged_nodes":[...], "read_from_changes":[...], "mode_changes":[...], "source_changes":[...], "matmech":{"supports":n,"contradicts":n,"not_covered":n,"pairs":[{"m":"M1","cause":..,"effect":..,"verdict":..,"nodes":[..]}]}}.
Write graphs_v07/<name>.judge.md: verdict, changes, splits and merges, source/read_from changes, mode changes, the MatMech tally.

Do not run git. Reply under 250 words: per paper one line (verdict, splits, merges, source/read_from changes, mode changes, MatMech supports/contradicts/not covered).
