# Second-read flags: Bioactive_Materials__j.bioactmat.2019.01.001

Graph: /home/aid1/Documents/causalmat/taxonomy/graphs_v07/Bioactive_Materials__j.bioactmat.2019.01.001.json

Packet (captions, linked text, panel section with every crop path): /home/aid1/Documents/causalmat/taxonomy/v06_pilot/packets/Bioactive_Materials__j.bioactmat.2019.01.001.md

A blind reader described each crop below without the paper; a grader ruled the description contradicts the node. For each: open the whole figure and the crop, decide whether the node cites the wrong panel. If another panel of the same paper shows the observation, set panel_ids (and figs) to it. If no panel shows it, set attrs.source to "text", drop panel_ids, and list the fact in attrs.requires_unseen. If the node and panel are right and the reader or grader erred, leave the node and say so. Edit only the flagged nodes in the graph JSON (keep ids), and write /home/aid1/Documents/causalmat/results/v07/fix_effect/Bioactive_Materials__j.bioactmat.2019.01.001/rrgraph/fix.json: {"<node>": {"action": "repointed|text|kept", "panel_ids": [...], "why": "one sentence"}}. Do not run git.


## b7 cites F3c
Node label: 28 d rates: HP-Mg 0.78 (GS) vs 2.0 mm/y (SBF); HP-Zn about 0.03 vs 0.10; P-Fe about 0.10 vs 0.13
Crop F3c: /home/aid1/Documents/causalmat/matmech/Bioactive_Materials/j.bioactmat.2019.01.001/panels/crops/8874df6ae34b97a9f4f47c1dbeafa8320c7f7bf45608a4033bec6d62fdc2f495_C.jpg
Reader on F3c:
Panel (c) is a bar chart, not a microscopy image — it shows corrosion rate (Pw, mm/y) on the y-axis (0 to 4.0) plotted for three metal groups — HP-Mg (gray bars), HP-Zn (red bars), and P-Fe (blue bars) — under two immersion conditions, GS and SBF, at four time points: 7d, 14d, 21d, and 28d. Error bars (SD) are shown on each bar, and asterisks with connecting brackets mark statistically significant differences between GS and SBF (or between groups) at each time point. HP-Mg consistently shows the highest corrosion rate, especially under SBF conditions, peaking near 3.4 mm/y at 7 days and declining to about 2.0 mm/y by 28 days; HP-Zn and P-Fe remain low throughout (mostly under 0.5-0.6 mm/y) with only modest GS vs SBF differences. There is no scale bar since this is a quantitative bar graph rather than an imaging panel.
Grader: WRONG: the candidate correctly identifies the bar-chart format, GS vs SBF conditions, and that HP-Mg has the highest rate declining toward 2.0 mm/y by 28d (matching the key's HP-Mg SBF ~2.0), but it substantially misstates the HP-Zn and P-Fe values as "mostly under 0.5-0.6 mm/y," whereas the key specifies much smaller values (~0.03-0.10 for HP-Zn, ~0.10-0.13 for P-Fe) — an order-of-magnitude contradiction rather than a minor omission.


## b13 cites F6b
Node label: CCK-8: P-Fe-IC stays about 0.4-0.5 at days 3 and 5 vs negative control 1.9 and 2.6; by day 5 HP-Mg-IC, HP-Zn-IC and HP-Mg-EC reach or exceed the control, other Mg/Zn groups 1.8-2.3
Crop F6b: /home/aid1/Documents/causalmat/matmech/Bioactive_Materials/j.bioactmat.2019.01.001/panels/crops/f6c03e3af07d2df819e8bb416eb277474319b34d0483dda219e68cba1eb026c1_B.jpg
Reader on F6b:
Panel (b) is a grouped bar chart, not a microscopy image, so there is no scale bar or imaging technique involved. Y-axis: "Absorbance at 450 nm" (0 to 4.5), consistent with a colorimetric assay (e.g., LDH or similar cytotoxicity/hemolysis-type absorbance readout at 450 nm). X-axis groups data into three time points: Day 1, Day 3, and Day 5. Each time point contains up to 11 colored bars with error bars, representing conditions: HP-Mg-DC, HP-Zn-DC, P-Fe-DC, HP-Mg-IC, HP-Zn-IC, P-Fe-IC, HP-Mg-EC, HP-Zn-EC, P-Fe-EC, Negative, and Positive (legend in upper left, color-coded).

Trend: absorbance values are low and fairly uniform (~0.4-0.8) across all sample groups at Day 1, then rise substantially and diverge by Day 3 (most sample bars ~1-2.8, with P-Fe-EC and HP-Mg-EC among the highest), and increase further by Day 5 (several bars reaching ~2.3-3.3, notably HP-Mg-IC and HP-Zn-DC). The Positive control bar is near zero/very low at all time points, while the Negative control bar is present at Day 1 (~0.45) but appears absent (zero or omitted) at Day 3 and Day 5.
Grader: WRONG

The candidate's description of the negative control trend directly contradicts the answer key. The key states the negative control has values of 1.9 (day 3) and 2.6 (day 5) — i.e., relatively high and clearly present. The candidate instead states the negative control bar is present at Day 1 (~0.45) but "appears absent (zero or omitted) at Day 3 and Day 5." This is a direct contradiction of a specific, load-bearing feature in the key.

Additionally, the candidate does not identify P-Fe-IC as the group that stays low (~0.4-0.5) at days 3 and 5 while other groups rise — instead it describes a general uniform rise across essentially all sample groups by day 3/5, which conflicts with the key's central contrast (P-Fe-IC staying low vs. negative control and other Mg/Zn groups being much higher).

Given the reversal of the negative-control trend and the missed/contradicted P-Fe-IC vs. control contrast, this should be graded WRONG rather than PARTIAL.
