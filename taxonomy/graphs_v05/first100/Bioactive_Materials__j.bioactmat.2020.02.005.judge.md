# Judge review — Bioactive_Materials/j.bioactmat.2020.02.005 (rank 1)

**Verdict: approved with changes.**

Ce–Er co-doped TiO2 for visible-light disinfection. The spine reads as the paper's own argument: need → co-doping hypothesis → host/dopant/sweep choices → sol-gel synthesis → an Er-only optical screen that fixes Er at 0.5 mol% (PRP → DES/down_select) → mixed-phase and composition claims → band gap and carrier-recombination properties → the Ce/Er electronic mechanism → photocatalysis → 20-min kill → conclusion. 17 spine nodes, one connected path from b1 to b18, two parallel structure/property branches plus the dark-killing control branch, and every spine STR/PRP/PRF node has either an `evidences` edge or `basis` ≠ evidenced. Every OBS-with-figure edge carries an mm_op that names a real act on the cited panel. Total 45 nodes is above the 25–40 target; the excess is evidence OBS, not spine, so it was left alone.

## Changes

1. **o13** — `image_note` extended after opening F9a: neither Nyquist arc closes inside the plotted window, so the TiO2 arc diameter is a lower bound only and the node reads arc size rather than a fitted charge-transfer resistance. Type, panel ids and `image_support` unchanged.

Nothing else was altered. Types follow the v04 decision rules throughout (o12 feature_quantification for a band height read as a degree; o13 trend with `aspect=ranking`; bar charts typed `xy_curve`).

## Panel checks

| node | panel_ids | ruling |
|---|---|---|
| o4 | `#F4c` | **confirmed** |
| o11 | `#F6c`, `#F6d` | **confirmed** |
| o13 | `#F9a` | **confirmed** |
| o1 / o2 (extra) | `#F4a` | **confirmed** |

- **o4 → F4c.** The Tauc panel prints 2.90, 2.46, 2.20 and 2.32 eV beside the four extrapolation lines, exactly the values and ordering in the node. The MatMech block's "3.2 → 2.4 eV" matches neither, as the node says.
- **o11 → F6c/F6d.** F6c is the Er 4d window: an unsmoothed noise trace under a drawn smooth envelope, with the 168.8 eV label pointing at a single noise spike. The audit is fairly stated — the figure does not resolve the valence assignment the text reads from it.
- **o13 → F9a.** F9a is the EIS Nyquist panel. TiO2 rises near-vertically past −Z″ 1.1e4 Ω while the co-doped trace turns over below Z′ ~1.5e3 Ω into a sloping line, as claimed.
- **o1/o2 → F4a** (extra check, because audit b21 rests on it). A labels sit on the Er0.5Ce0.3Ti-O trace and R labels on the Er0.5Ce0.1Ti-O trace; the three traces differ only in Ce content. b21's "the annealing-temperature control is not shown" is therefore correct, and correctly framed as *not resolved* rather than *contradicted*.

No panel_id in this graph is invented: all 21 appear in the packet's panel section.

## Audits

Five audit nodes, at budget, each changing the support of a spine claim: b20 with o18 (dark killing ranks Ce0.3 above Ce0.2, the reverse of the light ranking) opens the control branch; b21 with o2 bounds the phase claim b9; b22 with o11 bounds the composition claim b10, which is what carries the Ce-trap mechanism b14. Both b21 and b22 are stated as "the figure does not resolve it", which the crops bear out.

## What the packet got wrong

- The panel **`definition` strings are offset by one** wherever the caption places the panel letter *after* its description (F3, F6, F9, F10): F6a is Ti 2p but is given the "O 1s" span, F9a is the EIS plot but is given the "photocurrent spectra" span, F10a is S. aureus but is given the "and E. coli" span. The correct content is the phrase *before* the letter. The staff read the panels from their image labels and were right to; the judge confirmed this against the images. Captions of the "(a) XRD, (b) UV–vis" form (F4, F5) are correct.
- F10d: OCR read the letter as `(p)` against the detector's `d`.
- The OCR `cues` lines call the d-spacing labels 0.233 nm and 0.360 nm "scale bars" and type the SAED panel F5e as a micrograph.
