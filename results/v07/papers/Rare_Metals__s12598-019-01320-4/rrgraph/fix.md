# Second-read flags: Rare_Metals__s12598-019-01320-4

Graph: /home/aid1/Documents/causalmat/taxonomy/graphs_v07/Rare_Metals__s12598-019-01320-4.json

Packet (captions, linked text, panel section with every crop path): /home/aid1/Documents/causalmat/taxonomy/v07/partC/packets/Rare_Metals__s12598-019-01320-4.md

A blind reader described each crop below without the paper; a grader ruled the description contradicts the node. For each: open the whole figure and the crop, decide whether the node cites the wrong panel. If another panel of the same paper shows the observation, set panel_ids (and figs) to it. If no panel shows it, set attrs.source to "text", drop panel_ids, and list the fact in attrs.requires_unseen. If the node and panel are right and the reader or grader erred, leave the node and say so. Edit only the flagged nodes in the graph JSON (keep ids), and write /home/aid1/Documents/causalmat/results/v07/papers/Rare_Metals__s12598-019-01320-4/rrgraph/fix.json: {"<node>": {"action": "repointed|text|kept", "panel_ids": [...], "why": "one sentence"}}. Do not run git.


## o16 cites F1
Node label: A separate bcc reflection is marked only on the 16 h annealed trace, not on shorter anneals
Crop F1: /home/aid1/Documents/causalmat/matmech/Rare_Metals/s12598-019-01320-4/images/e81c9af127cc3a2471e52f6aecdd251c0baa65bf64489a92fc5d019d58a58a07.jpg
Reader on F1:
The image (/home/aid1/Documents/causalmat/.v07work/rr/1e24c52cbdd8fec7.jpg) shows two X-ray diffraction (XRD) pattern panels (a and b), plotting Intensity (a.u., y-axis) versus 2θ/° (x-axis, 30–110°), with fcc peaks marked by diamond symbols and bcc peaks marked by circle symbols.

Panel a compares two states: "As-cast" (black curve, bottom) showing strong, sharp fcc peaks near 2θ ≈ 44°, 51°, 75°, 90° plus a weaker peak near 96°, and "Cold-rolling-80%" (red curve, top, vertically offset) showing broadened/reduced-intensity fcc peaks at similar positions along with a small bcc peak near 2θ ≈ 46-47°, indicating peak broadening and phase change (fcc plus emerging bcc) after severe cold deformation.

Panel b shows a stacked series of six curves (bottom to top: 75 min, 90 min, 2 h, 4 h, 8 h, 16 h, each vertically offset for clarity) tracking evolution with increasing time/duration, all dominated by fcc peaks at the same 2θ positions as in panel a, with a small bcc peak visible near 2θ ≈ 46-47° that appears in the shorter/earlier time curves and is also marked in the topmost (16 h) trace, suggesting a fcc-to-bcc or related phase transformation being monitored over time. No scale bar is present (not applicable to XRD plots); axes are labeled and gridlines/tick marks are standard line-plot style.
Grader: WRONG: the candidate claims the bcc peak is visible in the shorter/earlier time curves as well as the 16 h trace, directly contradicting the key's statement that the bcc reflection is marked only on the 16 h annealed trace and not on shorter anneals.


## o14 cites F5
Node label: F5 grain sizes (d = 30.0, 21.6, 19.2, 9.0, 7.0, 5.3 um) equal the F4 model series, not the measured sizes
Crop F5: /home/aid1/Documents/causalmat/matmech/Rare_Metals/s12598-019-01320-4/images/62b7c18722beacc15579d4d47c5da0c876f5765260972933cb0426e9d373eb79.jpg
Reader on F5:
The image (cfb146f4845580e8.jpg) is a line/scatter plot, not a micrograph. It shows "Average microhardness (HV)" on the y-axis (range ~160–320) plotted against d^(-1/2) (in μm^(-1/2), range 0.15–0.45) on the x-axis, i.e., a Hall-Petch type relationship. Six data points are shown as filled black squares, each with visible vertical error bars, generally increasing from about HV 210 at d^(-1/2) ≈ 0.18 to about HV 290 at d^(-1/2) ≈ 0.43. A single straight best-fit line is drawn through the points with the equation "HV = 145.94 + 336.28 d^(-1/2)" annotated in the upper left, along with "K_HV = 336.28 HV·μm^(1/2)" (the Hall-Petch slope/strengthening coefficient). There is no scale bar since this is a data plot, not a micrograph; the overall trend is a clear positive linear correlation between hardness and inverse square root of grain size, consistent with Hall-Petch grain-boundary strengthening.
Grader: WRONG — the key states this panel shows F5 grain sizes (d = 30.0, 21.6, 19.2, 9.0, 7.0, 5.3 μm) equal the F4 model series values, not the measured sizes. The candidate instead describes a Hall-Petch type plot (average microhardness HV vs. d^-1/2, with a linear fit equation "HV = 145.94 + 336.28 d^-1/2"). This is a different kind of data/content than what the key describes, contradicting rather than agreeing with or merely omitting the key's feature, so this is WRONG.


## s3 cites F2
Node label: Interdendritic regions consist of alternating fine A2 (disordered) and B2 (ordered) phases from spinodal decomposition
Crop F2: /home/aid1/Documents/causalmat/matmech/Rare_Metals/s12598-019-01320-4/images/fb498e218290345b3bbdb5699a140af243d1c07af1ed7ab8b7d33a204e01ac3b.jpg
Reader on F2:
Image at /home/aid1/Documents/causalmat/.v07work/rr/6ac68b4aaa1fe43f.jpg shows an optical (or possibly SEM) micrograph of a rolled metal alloy microstructure, oriented with the rolling direction indicated by an arrow pointing to the upper right. The field shows a light gray matrix containing several dark, elongated, feather/arrowhead-shaped second-phase particles or intermetallic/eutectic features aligned along the rolling direction, each with an internal fine striped/cross-hatched (basket-weave-like) texture. Two features are labeled with arrows: "ID" (pointing to a boundary/interface region between two adjacent dark particles) and "DC" (pointing to the interior/core of one of the larger dark particles). A scale bar of 50 µm is given in the lower right corner, indicating the dark particles range roughly from a few microns up to ~30–40 µm in size. The particles appear stretched and fragmented along the rolling direction, consistent with deformation/elongation of second-phase constituents during rolling processing.
Grader: WRONG — The candidate describes a rolled metal alloy microstructure with elongated, feather-shaped intermetallic/eutectic particles aligned along a rolling direction, each with an internal striped texture, labeled ID (interface) and DC (particle core). The answer key states the panel shows interdendritic regions with alternating fine A2 (disordered) and B2 (ordered) phases from spinodal decomposition. While the candidate's "internal fine striped/cross-hatched texture" loosely echoes the alternating-phase idea, the overall framing (rolled alloy, rolling-direction arrow, elongated/fragmented second-phase particles from deformation) contradicts the key's context of dendritic solidification structure and spinodal decomposition, and the candidate never identifies the phases as A2/B2 or attributes the fine texture to spinodal decomposition. This is a contradiction in feature/technique interpretation, not merely a missing detail, so it grades WRONG.
