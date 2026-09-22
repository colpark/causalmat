# Second-read flags: Progress_in_Organic_Coatings__j.porgcoat.2021.106672

Graph: /home/aid1/Documents/causalmat/taxonomy/graphs_v07/Progress_in_Organic_Coatings__j.porgcoat.2021.106672.json

Packet (captions, linked text, panel section with every crop path): /home/aid1/Documents/causalmat/taxonomy/v07/partC/packets/Progress_in_Organic_Coatings__j.porgcoat.2021.106672.md

A blind reader described each crop below without the paper; a grader ruled the description contradicts the node. For each: open the whole figure and the crop, decide whether the node cites the wrong panel. If another panel of the same paper shows the observation, set panel_ids (and figs) to it. If no panel shows it, set attrs.source to "text", drop panel_ids, and list the fact in attrs.requires_unseen. If the node and panel are right and the reader or grader erred, leave the node and say so. Edit only the flagged nodes in the graph JSON (keep ids), and write /home/aid1/Documents/causalmat/results/v07/papers/Progress_in_Organic_Coatings__j.porgcoat.2021.106672/rrgraph/fix.json: {"<node>": {"action": "repointed|text|kept", "panel_ids": [...], "why": "one sentence"}}. Do not run git.


## n8 cites F2a
Node label: Filler furan groups react with mPU maleimide ends by Diels-Alder, crosslinking fillers into the PU network
Crop F2a: /home/aid1/Documents/causalmat/matmech/Progress_in_Organic_Coatings/j.porgcoat.2021.106672/panels/crops/fccb622e04e05cfbb59041f90e42ec893ad3341d2bb54b41b7816e69594d13e8_A.jpg
Reader on F2a:
Panel description (image: /home/aid1/Documents/causalmat/.v07work/rr/7d9ebe5cd2d4997e.jpg, labeled "a"):

This is an FTIR (Fourier-transform infrared) spectroscopy panel showing three stacked absorbance/transmittance spectra plotted against wavenumber (500–4000 cm⁻¹, x-axis) with no y-axis scale values shown (curves are vertically offset for comparison) and no scale bar (not applicable to spectral data). The three traces, labeled and color-coded, are: "PCM" (blue, top), "F-d@MX" (red, middle), and "F-d@Ce" (black, bottom). The PCM trace shows several sharp, well-resolved absorption bands in the 1000–1500 cm⁻¹ fingerprint region and a distinct dip near 2900 cm⁻¹ (typical C-H stretching). The F-d@MX and F-d@Ce traces are broader and less sharply featured, with F-d@Ce showing a prominent broad absorption band centered around 3200–3600 cm⁻¹ (consistent with O-H/N-H stretching) and a labeled peak at 732 cm⁻¹ (marked with a dashed vertical guideline). The overall trend across the three spectra suggests progressive broadening/loss of sharp fingerprint features and emergence of broad bands upon going from PCM to the F-d@MX and F-d@Ce composite/coated materials, consistent with encapsulation, surface functionalization, or coating of the PCM by MX or Ce-based shell material.

No other information (paper source, full caption, or panel b/c) was visible in the cropped image; only panel "a" is shown.
Grader: WRONG

The candidate describes an FTIR spectroscopy panel showing three stacked spectra (PCM, F-d@MX, F-d@Ce) with peak broadening consistent with encapsulation/coating of a phase-change material (PCM) by MX or Ce-based shells. The answer key states this panel shows filler furan groups reacting with mPU maleimide ends via Diels-Alder chemistry, crosslinking fillers into the polyurethane network. These describe entirely different materials systems (PCM encapsulation vs. PU/filler crosslinking) and different chemistries, so the candidate contradicts the key rather than merely omitting a detail.


## n10 cites F2d
Node label: F-d@MX fillers are thin lamellar sheets
Crop F2d: /home/aid1/Documents/causalmat/matmech/Progress_in_Organic_Coatings/j.porgcoat.2021.106672/panels/crops/fccb622e04e05cfbb59041f90e42ec893ad3341d2bb54b41b7816e69594d13e8_D.jpg
Reader on F2d:
Panel "d" is a scanning electron microscopy (SEM) image at high magnification (scale bar = 100 nm) showing a cross-sectional or side view of an array of elongated, rod- or fiber-like structures oriented roughly vertically (top to bottom) across the frame. The rods have smooth, slightly curved/undulating surfaces and appear closely packed side by side with narrow gaps between them, some gaps showing V-shaped or wedge-shaped openings where adjacent rods diverge. In the background, visible through and between the gaps, are several rounded, bead- or grain-like particles (spherical to ovoid, roughly tens of nanometers in size) partially occluded by the foreground rods. The image is grayscale with typical SEM contrast (bright edges/highlights on rod surfaces, darker shadowed recesses), and there is no visible compositional or trend data (e.g., no EDS mapping or quantitative overlay) — it is a purely morphological/structural micrograph. No other labels or annotations besides the panel letter "d" and the scale bar are present.
Grader: WRONG - the key states the panel shows thin lamellar sheets, but the candidate describes elongated rod/fiber-like structures with rounded bead-like particles, which contradicts the sheet-like morphology stated in the key.
