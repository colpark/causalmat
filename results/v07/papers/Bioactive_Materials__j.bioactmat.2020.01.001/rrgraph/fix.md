# Second-read flags: Bioactive_Materials__j.bioactmat.2020.01.001

Graph: /home/aid1/Documents/causalmat/taxonomy/graphs_v07/Bioactive_Materials__j.bioactmat.2020.01.001.json

Packet (captions, linked text, panel section with every crop path): /home/aid1/Documents/causalmat/taxonomy/v07/partC/packets/Bioactive_Materials__j.bioactmat.2020.01.001.md

A blind reader described each crop below without the paper; a grader ruled the description contradicts the node. For each: open the whole figure and the crop, decide whether the node cites the wrong panel. If another panel of the same paper shows the observation, set panel_ids (and figs) to it. If no panel shows it, set attrs.source to "text", drop panel_ids, and list the fact in attrs.requires_unseen. If the node and panel are right and the reader or grader erred, leave the node and say so. Edit only the flagged nodes in the graph JSON (keep ids), and write /home/aid1/Documents/causalmat/results/v07/papers/Bioactive_Materials__j.bioactmat.2020.01.001/rrgraph/fix.json: {"<node>": {"action": "repointed|text|kept", "panel_ids": [...], "why": "one sentence"}}. Do not run git.


## o20 cites F7
Node label: Actin/nucleus images at 1 d: few round cells on Ti (~9 per field), more on HA (~17) and most, more spread, on Si-HA (~22)
Crop F7: /home/aid1/Documents/causalmat/matmech/Bioactive_Materials/j.bioactmat.2020.01.001/images/018f3df9a28e817c843c6e6a7538beb2bd0601e0d285205c8c3e5822b672dc7d.jpg
Reader on F7:
Panel description of /home/aid1/Documents/causalmat/.v07work/rr/b8cd2bf1b28961ed.jpg:

This is a 2x3 grid of immunofluorescence/confocal microscopy images comparing cell attachment/spreading on three substrates — Ti, HA, and Si-HA (columns) — at two time points, 1 day and 3 days (rows). Cells are stained with what appears to be a red marker (likely actin/cytoskeleton, e.g., phalloidin or a cell-membrane/cytoskeletal stain) and a blue nuclear counterstain (likely DAPI), imaged in dark-field fluorescence mode. A 50 µm scale bar is present in the bottom-right panel (3 d, Si-HA). Across the top row (1 d), cell density is sparse and roughly similar between the three substrates, with cells appearing small and rounded/spindle-shaped with limited red (cytoskeletal) signal. By 3 days, cell density increases markedly on all three substrates, with cells showing more spread morphology and stronger, more organized red cytoskeletal staining outlining cell borders; the Si-HA panel at 3 d appears to show the highest cell density and most confluent coverage among the three substrates, suggesting enhanced cell proliferation/spreading on the Si-doped HA surface compared to Ti and plain HA.
Grader: WRONG: The key states that at 1 day there is a clear increasing trend — few round cells on Ti (~9), more on HA (~17), most and more spread on Si-HA (~22). The candidate explicitly states the opposite for that timepoint, describing the 1-day row as "sparse and roughly similar between the three substrates," and instead places the differentiation (density/spreading trend) at the 3-day row. This directly contradicts the key's specific claim about what the 1-day panels show, so it is WRONG rather than PARTIAL.


## o24 cites F8f
Node label: Stained discs at 7 d: Ti pale pink, HA and Si-HA dark red-brown, Si-HA marginally darker
Crop F8f: /home/aid1/Documents/causalmat/matmech/Bioactive_Materials/j.bioactmat.2020.01.001/panels/crops/c43b75e543ff4e8913e6d710d525814559de7ebbf6d78e49c7a886c325733e8a_F.jpg
Reader on F8f:
Panel (f) shows a photographic (macroscopic, not microscopy) image of three circular disc-shaped samples, each labeled: "Ti" (top left), "HA" (top right), and "Si-HA" (bottom). No scale bar is present, and no measurement technique markings (e.g., SEM/EDS labels) are visible — this appears to be a plain digital photograph comparing the visual appearance/coloration of the three coated or treated disc samples side by side. All three discs are roughly the same size and shape (circular, coin-like) but differ in surface tone: the Ti disc has a lighter, slightly mottled purplish-grey surface, while the HA and Si-HA discs are darker maroon/reddish-brown, with Si-HA appearing marginally darker/more uniform than HA. No quantitative trend or data plot is shown; the panel simply documents a qualitative color/appearance comparison across the three sample conditions.
Grader: WRONG — The candidate's description of the Ti disc's color ("lighter, slightly mottled purplish-grey") directly contradicts the answer key's description ("Ti pale pink"). The candidate does correctly identify HA and Si-HA as dark red-brown/maroon with Si-HA marginally darker than HA, matching the key on that point, but the contradiction on the Ti disc's color is a direct conflict with a named feature in the key, not merely an omission.


## o26 cites F9
Node label: Marked down-growth zones are longest along the Ti pillar, shorter for HA and short boxes at the Si-HA pillar edge
Crop F9: /home/aid1/Documents/causalmat/matmech/Bioactive_Materials/j.bioactmat.2020.01.001/images/2f2727870903d16eaa183cc06e112d8b2890c882cc9fc70ae49bf90d53770ff7.jpg
Reader on F9:
The image (/home/aid1/Documents/causalmat/.v07work/rr/c58c7fcc0b81c706.jpg) is a 3-row x 2-column composite of hematoxylin-and-eosin (H&E) stained histology sections, each row showing a low-magnification overview (left, scale bar 500 µm) and a corresponding higher-magnification inset (right, scale bar 200 µm) of a boxed region.

Row 1: Overview shows two separate curled/folded tissue flaps with black dashed boxes marking regions of interest; the zoomed panel shows a layered fibrous tissue cross-section with a black double-headed arrow labeling a thickness of 400 µm.

Row 2: Overview shows a larger, more convoluted folded tissue structure (appears skin/wound-like with follicular or glandular structures) with red dashed boxes; the zoomed panel shows fibrous/adipose-like tissue with red arrows marking a much thinner measured gap of 100 µm.

Row 3: Overview shows a folded tissue section containing multiple dark, densely stained round/oval structures (possibly hair follicles, glands, or cellular inclusions) with blue dashed boxes; the zoomed panel shows a magnified view of these round dark-purple structures embedded in fibrous tissue, without an explicit measurement arrow/label visible.

Overall trend across rows: each pair juxtaposes a wide-field tissue overview against a zoomed region highlighting a specific structural layer or gap, with measured thicknesses decreasing from 400 µm (row 1) to 100 µm (row 2); row 3 emphasizes morphological/cellular content (round inclusion bodies) rather than a linear thickness measurement.
Grader: WRONG. The key describes marked "down-growth zones" compared across three pillar types (longest at Ti, shorter at HA, short boxes at Si-HA edge), i.e., a comparison of epithelial/tissue down-growth length by pillar material. The candidate's description instead reports absolute measured gap/thickness values (400 µm, then 100 µm, then no measurement) and emphasizes generic histological features (fibrous tissue, round inclusion bodies) with no mention of Ti, HA, or Si-HA pillars or any comparison of down-growth extent between them. This contradicts/misses the key's central comparative claim rather than merely omitting a detail, so it does not qualify as PARTIAL.
