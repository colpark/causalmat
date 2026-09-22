# Judge review: Nano_Letters__10.1021_acs.nanolett.5b03976

**Verdict:** accept with minor fixes

## Changes
- o4 modality spatial_map -> xy_curve (a line-scan profile is an xy trace)
- o19 label: valence-band loss reaches ~2.5e3 cm-1 at 2e20 cm-3 (was ~2e3)
- edge n20 -> n19 rel counteracts -> supports: the valence-band loss partition is the loss term that wins the trade-off, a premise for n19, not an effect opposing it
- source/requires_unseen corrections on n1, n13, n17, n18, n22, o3, o4, o19 (see source_changes)

## Panel checks (13 crops opened: 12 cited + F3c withheld)

| node | panel | ruling | correct id | note |
|---|---|---|---|---|
| o1 | F1a | confirmed |  | SEM of device; nanowire, pads, curved ~10-line gratings; 'Nanowire','Pads' annotations restated -> read_from annotation correct |
| o3 | F2b | confirmed |  | interferometric height map; device and surrounding band darker/lower; colour bar not in this crop (source -> text) |
| o4 | F2c | confirmed |  | line scan: ~20-25 nm step at about +/-17 um, trenches at +/-10 um; profile is an xy trace (modality -> xy_curve); no unit label (source -> text) |
| o5 | F3a | confirmed |  | FDTD Ey field confined along wire, fanning to curved mirrors; shows mode confinement, not Q, so partial support of n15 is correct |
| o6 | F3b | confirmed |  | FEM strain ~2.4% (colour-bar top) uniform along wire, ~0 in pads; cue 'mechanical' compatible with MECH:FEM |
| o7 | (none; F3c opened) | confirmed | F3c | F3c crop opened (fig_ref F3c): Raman-derived map ~2-2.4% along wire; correct panel is F3c but citation stays withheld: cue 'mechanical' incompatible with RAMAN and the misfire exemption covers only 'micrograph' |
| o8 | (none; F3c opened) | confirmed | F3c | F3c crop opened: pads read ~0.7-1.0% (red) vs ~0 in FEM F3b; text_silent audit is fair; citation withheld as for o7 |
| o9 | F4a | confirmed |  | 0% max ~1570 nm; strained maxima ~1950-1980 nm; 2.37% not resolved from 1.95% |
| o10 | F4a | confirmed |  | 0% ~270 counts vs strained envelopes ~1000-1100, 1.95% resonance spikes to ~2700 |
| o11 | F4a | confirmed |  | 2.37% envelope ~1100, no brighter than 1.95%, rolls off in grey band >2000 nm |
| o12 | F4b | confirmed |  | Lorentzian peak ~1996 nm, FWHM ~1 nm -> Q ~2000; OCR '(q)' is the (b) label |
| o13 | F4c | confirmed |  | 1/10/45 mW legend restated -> annotation correct; peaks grow, broaden slightly, ~12 nm spacing |
| o14 | F4d | confirmed |  | row-normalised map: every resonance blue-shifts ~5 nm from 5 to 45 mW and broadens |
| o15 | F5a | confirmed |  | net gain -350/-500 at 5 mW to -1250/-1975 at 22.5 mW, all negative |
| o16 | F5a | confirmed |  | 2.37% above 1.95% at every power; gap ~150 -> ~700 cm-1; error bars touch at 5-7.5 mW |
| o17 | F5b | confirmed |  | data below model by ~120-210 cm-1 at 1.7-4.7e19, on model above ~5.5e19; OCR '(q)' is (b) |
| o19 | F5c | confirmed |  | VB crosses CB near 6.5e18, reaches ~2.5e3 at 2e20 (label corrected from ~2e3); pads flat ~70 cm-1 |

Overturned: 0.

## Technique mismatches
- o7 F3c: RAMAN vs cue 'mechanical': citation kept dropped (figs F3, panel_ids [], fig_ref F3c); crop is plainly the right panel; the cue comes from the 'Strain (%)' colour-bar label. Not overridden because the misfire exemption is limited to 'micrograph'; recommend the orchestrator extend it to 'mechanical' on strain maps
- o8 F3c: RAMAN vs cue 'mechanical': same as o7

Cue overrides: none.

## Mode changes
- none (no claim has two or more causes edges)

## Source changes
- n17: text -> figure (F5a shows 2.37% above 1.95% at every power with legend strain labels)
- n18: text -> figure (F5a shows net gain negative and falling with pump)
- o3: figure -> text (colour-to-height mapping is not in the F2b crop; caption states devices sit lower)
- o4: figure -> text (ordinate unit (nm, height) comes from the caption only)
- o19: figure -> text (that the curves are the modelled loss terms of F5b is caption-only)
- n1: inferred [] -> inferred + fact listed (introduction not in packet)
- n13: inferred [] -> inferred + fact listed (Gamma-valley lowering is band-structure knowledge no panel shows)
- n22: inferred [] -> inferred + facts listed (direct-gap assignment, no-lasing statement and VB attribution are text)

## MatMech tally
supports 3 · contradicts 0 · not covered 0

- M1: e-beam lithography, HBr/Cl2 dry etch, KOH wet etch, ALD -> highly strained Ge nanowire with pseudo-heterostructure and high-Q cavity: **supports** (n6, n7, n10, n16, n15, n20). ALD step and pseudo-heterostructure only in text/attrs; o8 audit weakens the confinement contrast
- M2: strained Ge nanowire in high-Q cavity -> direct-bandgap light emission (red-shift, bandgap narrowing): **supports** (n10, n12, n13, n14, n17). VB-splitting-raises-gain step of MatMech not modelled as a node
- M3: direct-gap emission, high strain -> enhanced PL with Q up to ~2000 and >400 nm tunability: **supports** (n12, n14, n15, n17, n22). MatMech's 'further strain could enable RT lasing' outlook absent; graph records no lasing (n21)
