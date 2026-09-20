# OCR cue precision, and which classes may feed a modality decision

**Date:** 2026-09-20. Sample: the 295 crops in `ocr_run/review/`, each drawn with its OCR token boxes.
Every crop was opened and judged by eye; no code decided any of this. Precision is
correct / (correct + wrong), with unclear cases excluded. Raw scores: `results/cue_scores/`.

The question is not whether the OCR read the text well, but whether the **cue class** is right about what the
panel is. A class at or above 90% may feed the `modality_agrees` link in the verification chain. A class below
it is **disabled** until its pattern is tightened.

| Cue class | Precision | Judged | Feeds `modality_agrees`? |
|---|---|---|---|
| SEM | 1.000 | 13 | yes |
| electrochemistry | 1.000 | 13 | yes |
| thermal | 1.000 | 13 | yes |
| optical_spectroscopy | 1.000 | 13 | yes |
| Raman | 0.929 | 14 | yes |
| micrograph | 0.909 | 33 | yes |
| EDS | 0.909 | 11 | yes, but one miss from failing |
| XPS | 0.857 | 14 | **no** |
| mechanical | 0.833 | 12 | **no** |
| none | 0.833 | 12 | **no** |
| XRD | 0.800 | 15 | **no** |
| FTIR | 0.714 | 14 | **no** |
| XAS | 0.357 | 14 | **no** |
| EDS_line_scan | 0.077 | 13 | **no** |

**Seven of fourteen classes are disabled.** Only SEM, electrochemistry, thermal, optical spectroscopy, Raman,
micrograph and EDS may be used, and EDS sits one miss above the line.

## One failure mode, repeated

Almost every error is the same shape: **the pattern fires on an axis unit that an unrelated technique shares,
with no check on the value range or on the other axis.**

- **XAS (0.357)** matches "Photon energy (eV)" on panels running 1.5–3.5 eV — photoluminescence,
  electroluminescence, UV-vis, transient absorption. Nine of the nineteen errors in that batch are this one case.
  A real X-ray absorption edge is above ~100 eV.
- **EDS_line_scan (0.077)** fires on any "distance" token: nanoscratch depth curves, misorientation profiles,
  modulus-versus-distance, a furnace schematic's dimension arrow, a "Channel Distance = 10.5 µm" annotation.
  Only 1 of 13 was a real line scan. It needs a composition axis (at%, wt%, counts, element names) as well.
- **FTIR (0.714)** claims Raman spectra off a shared "wavenumber (cm⁻¹)" axis.
- **XRD (0.800)** claims angle-resolved optical maps and a circular-dichroism spectrum from a bare "20" tick
  beside "(deg)" — the very pattern added because OCR reads 2θ as "20".
- **XPS (0.857)** claims an EDX spectrum whose axis reads "Binding Energy (keV)" out to 4 keV.
- **mechanical (0.833)** fires on the bare word "Strain": a piezoresistive dR/R₀ curve and a strain colourbar
  on a DIC map. Requiring a stress or load axis alongside strain would take it to 12/12.
- **EDS (0.909)** claimed a Ru K-edge XANES spectrum, since a keV axis alone does not separate EDS from hard
  X-ray absorption.

## Misses rather than false positives

`none` means the pattern assigned no cue. Of 13 such crops, one carried a technique the text could have
identified — a plain engineering stress–strain plot whose axis wording the mechanical pattern does not match,
the same gap as above. One more is a phase/orientation map with no technique tokens at all, so it is not
text-recoverable. Text-recoverable miss rate: about 8%.

## Tightenings to make before re-enabling

1. **XAS**: require the photon-energy axis to exceed ~100 eV, or the tokens `XANES`/`EXAFS`/`K-edge`.
2. **EDS_line_scan**: require a composition axis alongside distance.
3. **FTIR**: require a transmittance or absorbance y-axis, and exclude panels whose bands sit at Raman mode positions.
4. **XRD**: require `2θ`/`2 theta` adjacency rather than a bare "20" tick next to "(deg)".
5. **XPS**: reject binding-energy axes that run into the keV range.
6. **mechanical**: require a stress or load axis alongside strain, and ignore colourbar-only hits.
7. **micrograph**: the scale-bar-only rule holds at 0.909, but all three misses are a unit-bearing number inside
   a plot read as a scale bar. Requiring the token to sit outside any axis or tick box would clear them.

## One definition to settle

A thermal-conductivity-versus-temperature panel was scored correct as `none`, because `thermal` is defined as
TGA, DSC and heat-flow only. If thermal transport belongs in `thermal`, `none` drops to 0.75. That is a
definition choice, not a pattern bug.

## Consequence for the verification chain

`modality_agrees` may only consult the seven enabled classes. For a node whose panel's only cue is disabled,
the link is **not** a failure — it is unknown, so the chain reports `partial` rather than `unverified`, exactly
as a missing OCR record does.
