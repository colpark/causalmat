# Second-read flags: Journal_of_Advanced_Ceramics__s40145-021-0536-4

Graph: /home/aid1/Documents/causalmat/taxonomy/graphs_v07/Journal_of_Advanced_Ceramics__s40145-021-0536-4.json

Packet (captions, linked text, panel section with every crop path): /home/aid1/Documents/causalmat/taxonomy/v07/partC/packets/Journal_of_Advanced_Ceramics__s40145-021-0536-4.md

A blind reader described each crop below without the paper; a grader ruled the description contradicts the node. For each: open the whole figure and the crop, decide whether the node cites the wrong panel. If another panel of the same paper shows the observation, set panel_ids (and figs) to it. If no panel shows it, set attrs.source to "text", drop panel_ids, and list the fact in attrs.requires_unseen. If the node and panel are right and the reader or grader erred, leave the node and say so. Edit only the flagged nodes in the graph JSON (keep ids), and write /home/aid1/Documents/causalmat/results/v07/papers/Journal_of_Advanced_Ceramics__s40145-021-0536-4/rrgraph/fix.json: {"<node>": {"action": "repointed|text|kept", "panel_ids": [...], "why": "one sentence"}}. Do not run git.


## n16 cites F9
Node label: S1 keeps K_IC >= 5.1 MPa m^1/2 (8.7% below RT) and flexural strength >= 450 MPa up to 800 C
Crop F9: /home/aid1/Documents/causalmat/matmech/Journal_of_Advanced_Ceramics/s40145-021-0536-4/images/eb8ef4d5ac9c0729d578ced4c2471885d7a738ec0cacc0e3d2652a83552e5980.jpg
Reader on F9:
The image (/home/aid1/Documents/causalmat/.v07work/rr/a6285b660572e877.jpg) is a line/scatter plot with two y-axes plotted against a common x-axis of Temperature (°C), ranging from 0 to 800.

- Left y-axis (black): K_IC (MPa·m^1/2), scale 0–18. Black circular data points connected by a black line, with vertical error bars at each point, at roughly 25°C, 400°C, 600°C, and 800°C. Values start around 9, rise slightly to ~9.5 at 400°C, peak at ~11 at 600°C, then drop back to ~9 at 800°C — a mild non-monotonic trend with a peak near 600°C.
- Right y-axis (red): σ (MPa), scale 0–900. Red square data points connected by a red line, also with error bars, at the same temperature values. Values are roughly flat/slightly declining, starting near 280 MPa at 25°C and gradually decreasing to about 250 MPa at 800°C.

No scale bar is present (this is a data plot, not a micrograph). No other panel labels, legends, or annotations are visible in the image beyond the axis titles and tick marks.
Grader: WRONG - the candidate reports flexural strength values of ~250-280 MPa and K_IC values of ~9-11 MPa·m^1/2, which directly contradict the key's claim that strength stays ≥450 MPa and K_IC stays ≥5.1 MPa·m^1/2 (8.7% below RT). The plot type/axes match (temperature-dependent dual-axis plot), but the specific quantitative values described contradict the key's thresholds, so this is a contradiction rather than a mere omission.
