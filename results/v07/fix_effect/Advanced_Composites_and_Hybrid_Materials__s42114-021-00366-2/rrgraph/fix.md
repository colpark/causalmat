# Second-read flags: Advanced_Composites_and_Hybrid_Materials__s42114-021-00366-2

Graph: /home/aid1/Documents/causalmat/taxonomy/graphs_v07/Advanced_Composites_and_Hybrid_Materials__s42114-021-00366-2.json

Packet (captions, linked text, panel section with every crop path): /home/aid1/Documents/causalmat/taxonomy/v07/partB/packets/Advanced_Composites_and_Hybrid_Materials__s42114-021-00366-2.md

A blind reader described each crop below without the paper; a grader ruled the description contradicts the node. For each: open the whole figure and the crop, decide whether the node cites the wrong panel. If another panel of the same paper shows the observation, set panel_ids (and figs) to it. If no panel shows it, set attrs.source to "text", drop panel_ids, and list the fact in attrs.requires_unseen. If the node and panel are right and the reader or grader erred, leave the node and say so. Edit only the flagged nodes in the graph JSON (keep ids), and write /home/aid1/Documents/causalmat/results/v07/fix_effect/Advanced_Composites_and_Hybrid_Materials__s42114-021-00366-2/rrgraph/fix.json: {"<node>": {"action": "repointed|text|kept", "panel_ids": [...], "why": "one sentence"}}. Do not run git.


## o12a cites F5b
Node label: Composites show a small (~1%) weight-loss step at 180-250 C that pure PAEN lacks
Crop F5b: /home/aid1/Documents/causalmat/matmech/Advanced_Composites_and_Hybrid_Materials/s42114-021-00366-2/panels/crops/6e2a3cede77ab3ffbf9ef8f73d37794466b913932e86ebb5627b5aa7a627d45f_B.jpg
Reader on F5b:
Panel (b) shows thermogravimetric analysis (TGA) curves: weight (%) on the y-axis (30-110%) versus temperature (°C) on the x-axis (0-800°C). Four curves are plotted, each labeled with an arrow pointing to its final plateau: Pure PAEN (gray), BST@Ag1% (blue), BST@Ag3% (orange), and BST@Ag5% (red). All curves start near 100% weight, show a small step/shoulder around 150-250°C, remain relatively flat until roughly 450-500°C, then undergo a sharp major decomposition step between about 500-600°C. Pure PAEN shows the steepest, deepest drop, leveling off around 37-38% residual weight by 700-800°C, while the three BST@Ag composite curves show progressively less mass loss with increasing Ag content, plateauing at higher residual weights in the order BST@Ag5% (~63-64%) > BST@Ag3% (~63%) > BST@Ag1% (~60%), indicating increased thermal stability/residual char with higher Ag loading. No scale bar is present (this is a graph/plot, not a micrograph); axes are linear with gridline-free white background.
Grader: WRONG. The key states composites show a small (~1%) weight-loss step at 180-250 C that pure PAEN lacks, but the candidate explicitly states "All curves start near 100% weight, show a small step/shoulder around 150-250°C," which includes Pure PAEN among the curves exhibiting this feature — directly contradicting the key's claim that PAEN lacks it.


## o15 cites F6b
Node label: At 100 Hz loss ranks PAEN 0.024 < 1% 0.032 < 3%~5% 0.038; curves converge near 0.015 above 10 kHz
Crop F6b: /home/aid1/Documents/causalmat/matmech/Advanced_Composites_and_Hybrid_Materials/s42114-021-00366-2/panels/crops/6e372eb24982a1a98b08255b7808330b4932ff44f22fa63f080358da39e07534_B.jpg
Reader on F6b:
Panel (b) is a line plot of dielectric loss versus frequency, not a microscopy image. X-axis: Frequency (Hz), log scale from 100 to 1,000,000 Hz. Y-axis: Dielectric Loss, linear scale from 0.00 to 0.12. Four curves are plotted for different composite compositions: Pure PAEN (gray), BST@Ag 1% (teal/blue), BST@Ag 3% (orange), and BST@Ag 5% (red). All curves start around 0.02–0.04 at 100 Hz and decrease with increasing frequency to a minimum near 0.01–0.015 around 10,000–100,000 Hz (typical dielectric relaxation behavior). At higher frequencies (~100,000–1,000,000 Hz) the BST@Ag 1% curve rises sharply back up to about 0.065, while the other three curves (Pure PAEN, BST@Ag 3%, BST@Ag 5%) remain low and roughly flat near 0.01–0.015 across the full frequency range. No scale bar is present, as this is a graph/plot, not a micrograph.
Grader: WRONG: the key states all curves converge near 0.015 above 10 kHz, but the candidate explicitly describes one curve (BST@Ag 1%) diverging sharply upward to ~0.065 at high frequency (~100,000–1,000,000 Hz) instead of converging with the others, which directly contradicts the key's stated high-frequency convergence trend. The candidate also fails to state the specific 100 Hz ranking (PAEN 0.024 < 1% 0.032 < 3%~5% 0.038) that the key specifies, instead giving only a vague combined range.
