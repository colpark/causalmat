# Judge review: Journal_of_Advanced_Ceramics/s40145-021-0476-z

Enhanced electromagnetic wave absorption property of binary ZnO/NiCo2O4 composites (staff B11, v07).

**Verdict:** accept with fixes. Spine of 17 nodes reads as the paper's argument (NH3.H2O sweep -> co-precipitation/heat treatment -> phases, nano-dot interfaces, argued interface density -> permittivity and small magnetic loss -> attenuation + matching (joint) -> RL -> -10 dB qualification -> conclusion). Every spine STR/PRP/PRF claim has an evidences edge or a stated basis (s3, r2 argued). 5 audit nodes (o9, o15, o27, o28, l1), all fair: each bears on a spine claim. 51 nodes, 86 edges, v04-valid.

Crops checked: 28 (all 25 staff citations plus F8b, F8d, F8f). Overturned: 0. Technique/cue mismatches: 0 (5 cue overrides). Mode changes: 0.

## Changes

- technique strings put in normalize_technique.py controlled form: EM:VNA -> TRANSPORT:VNA (13 nodes), STEM:EDS -> [TEM:STEM, EDS:mapping] (o6), PHYS:N2-sorption -> PHYS:surfacearea (o8), MAG:M-H -> OTHER:magnetometry (o9; no magnetometry family exists). Instrument unchanged; no cue conflict.
- o1 label corrected: markers sit only above the -10 pattern, not on all three; image_note adds the 59 deg text/figure mismatch
- o4 label: dot size ~10-15 nm (5 nm bar), was ~10 nm
- o21 image_note corrected: staff said the -5 minimum is not at 18 GHz/5.0 mm; F8b shows ~-6.3 dB there, so the text value is not contradicted
- o22 citations F8b, F8d, F8f restored (crops opened: RL-vs-frequency curves; micrograph cue is a false scale-bar hit on the '1.00mm' thickness legend); cue_overrides recorded
- o27 adds F8d, F8f (the curves that show RL still falling at 18 GHz); cue override recorded
- r2 attrs.basis set to argued: evidences edges (o13, o17) show low mu' and no eddy current, not small magnetic loss
- requires_unseen filled on text-sourced spine/side nodes p1, p2, m1, r2, r3, r4, f1, b1, m3, s3
- added derives edges o11/o14 -> o19, o21, o22 (Delta and RL use the full complex e and mu)

## Panel checks

| node | panels | ruling | note |
|---|---|---|---|
| o1 | F1a | confirmed | XRD patterns of -5/-7/-10 with star/diamond legend; markers only above -10 (label fixed) |
| o2 | F1a | confirmed | no peak in any pattern lacks a counterpart marked on -10 |
| o3 | F2b | confirmed | HRTEM, 0.26 nm fringes in region labelled ZnO |
| o4 | F2c | confirmed | HRTEM nano-dot labelled NiCo2O4 with 0.23 nm fringes; size ~10-15 nm |
| o5 | F2b | confirmed | dotted boundary between ZnO and circled NiCo2O4 dots |
| o6 | F2d | confirmed | dark-field image + Co/Ni/Zn maps; Ni patchy, Co near-continuous, Zn even |
| o7 | F1b, F1c, F1d | confirmed | SEM: b, c irregular agglomerates; d plates/rods covered with ordered ~30-50 nm particles |
| o8 | F3a | confirmed | N2 isotherms: -5/-10 loop at 0.45-0.9, -7 flat to 0.95 then jump to ~108 |
| o9 | F4a, F4b | confirmed | M-H: knee ~3 kOe at ~0.02 emu/g, 0.026 at 15 kOe; small open loop, Mr ~0.001, Hc ~50-100 Oe |
| o10 | F5a | confirmed | e' 5.6-5.78 / 6.57-6.85 / 6.67-6.96 |
| o11 | F5b | confirmed | e'' -5<-7<-10, 0.39/0.50/0.67 at 18 GHz; -5 above -7 near 12.5-13.5 GHz |
| o13 | F5d | confirmed | mu' ~1.16-1.20 -> ~0.91 |
| o14 | F5e | confirmed | mu'' falls with humps near 6 and 12.5 GHz |
| o15 | F5c, F5f | confirmed | mu''/mu' 0.06-0.15 vs e''/e' 0.01-0.10; crossing ~17-17.5 GHz |
| o17 | F6a | confirmed | C0 0.06 -> 0.005, three samples overlap |
| o18 | F6b | confirmed | Cole-Cole with arcs labelled I, II, III per sample |
| o19 | F7a, F7b, F7c | confirmed | Delta maps; 0.4 contour in b (>=~3.1 mm at 18 GHz) and c (>=~3.7 mm); a min 0.55 |
| o20 | F7d | confirmed | alpha at 18 GHz ~84/~73/~55 for -10/-7/-5 |
| o21 | F8a, F8c, F8e | confirmed | RL maps, colour-bar minima -6.52/-33.50/-27.50; image_note corrected (F8b reaches ~-6.3 at 18 GHz, 5 mm) |
| o22 | F8b, F8d, F8f | confirmed | RESTORED: RL curves at 1.00-5.00 mm; d and f cross -10 dB only above ~16.8 GHz; b stays above -6.5 dB. Staff had dropped them for a false micrograph cue |
| o27 | F8c, F8e | confirmed | maps: deepest colour only at the 18 GHz / 5 mm corner |
| o27 | F8d, F8f | confirmed | ADDED: curves still falling steeply at 18 GHz |
| o28 | F5b, F5e, F7d, F8c, F8e | confirmed | e'' and alpha rank -10 top; mu'' -7 >= -10; RL minima -33.5 (-7) vs -27.5 (-10) |

## Technique checks

No cited panel's OCR cue classes conflict with the node's instrument. Form fixes (controlled vocabulary of normalize_technique.py):

- o10,o11,o13,o14,o15,o17,o18,o19,o20,o21,o22,o27,o28: EM:VNA -> TRANSPORT:VNA
- o6: STEM:EDS -> [TEM:STEM, EDS:mapping]
- o8: PHYS:N2-sorption -> PHYS:surfacearea
- o9: MAG:M-H -> OTHER:magnetometry

Cue overrides (false 'micrograph' from the scale-bar detector on the thickness legend of RL-curve panels):

- o22 F8b: crop is an RL-vs-frequency plot; scale-bar detector fired on the thickness legend ('1.00mm' ... '5.00mm'); panel is the right one for the node
- o22 F8d: crop is an RL-vs-frequency plot; scale-bar detector fired on the thickness legend ('1.00mm' ... '5.00mm'); panel is the right one for the node
- o22 F8f: crop is an RL-vs-frequency plot; scale-bar detector fired on the thickness legend ('1.00mm' ... '5.00mm'); panel is the right one for the node
- o27 F8d: same false scale-bar hit on the thickness legend; the curves are the evidence that RL is still falling at 18 GHz
- o27 F8f: same false scale-bar hit on the thickness legend; the curves are the evidence that RL is still falling at 18 GHz

read_from: all annotation-restating nodes (o1, o3, o4, o5, o6, o18) already read_from=annotation; axis/pixels nodes do not restate listed annotation strings.

## Source / requires_unseen

- p1 (text): nucleation of NiCo2(OH)6 around Zn(OH)2 particles (Eqs. 1-3, linked text only)
- p2 (text): hydroxide-to-oxide conversion during heat treatment (Eqs. 4-5, linked text); temperature and time not given
- m1 (text): charge redistribution between ZnO particles and NiCo2O4 nano-dots under the AC field (asserted in linked text; no panel shows it)
- r2 (text): comparison of mu' with 'other magnetic materials' (Refs. 14,15,20; text only); C0 criterion for eddy current (text); single-domain NiCo2O4 argument (Ref. 42, text) [set basis=argued]
- r3 (text): sample suffix 5/7/10 = NH3.H2O amount (text)
- r4 (text): panel a/b/c = -5/-7/-10 (caption)
- f1 (text): panel c/e (and d/f) = -7/-10 (caption)
- b1 (text): ZnO and NiCo2O4 nonmagnetic at room temperature (literature premise, k6)
- m3 (text): exchange resonance at high frequency (Ref. 38, text); eddy-current exclusion via C0 criterion (text)
- s3 (text): number of ZnO and NiCo2O4 nanoparticles rises with NH3.H2O (asserted in linked text; no count shown)

## Mode

No changes. only f1 has two causes edges (r3, r4); joint kept: no caption or figure presents alpha and Delta as alternatives.

## MatMech (read after the graph was final; graph not edited)

Tally: supports 5, contradicts 3, not covered 1.

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | hydrothermal + calcination route with NH3.H2O varied | binary ZnO/NiCo2O4 phases formed via hydroxide intermediates, no impurities | supports | d2, p1, p2, s1, o1, o2 |  |
| M1 | NH3.H2O amount | morphology irregular (-5) -> well-regulated (-7) -> aggregated (-10) | contradicts | s4, o7 | graph (and paper text, F1b-d) has -5 and -7 irregular, -10 well-regulated |
| M2 | ZnO/NiCo2O4 heterojunction structure | enhanced complex permittivity / dielectric loss via interfacial polarization | supports | s2, m1, r1, o18 |  |
| M2 | nonmagnetic ZnO and NiCo2O4 phases | negligible magnetic loss | supports | s1, b1, r2, k6 | graph carries the claim but qualifies it (o9 weak ferromagnetic loop, o15 mu''/mu' > e''/e'); r2 basis argued |
| M2 | mesoporous structure | dielectric loss via mesoporous scattering | not_covered | s5 | porosity is a side node with no edge to any property |
| M3 | attenuation constant plus impedance matching at Ku band, thick layers | RLmin -33.49 dB at 18 GHz, 4.99 mm for -7 | supports | r3, r4, m2, f1, o19, o20, o21 |  |
| M3 | -7 has the highest e''/e' and alpha of the three | -7 gives the deepest RL | contradicts | o11, o20, o28 | F5c and F7d rank -10 highest in both; o28 records that the RL ranking does not follow dielectric loss |
| M3 | high loss + matching | -10 dB threshold met over a broad Ku-band range | contradicts | f2, o22, l1 | graph: RL < -10 dB only ~16.8-18 GHz at >= ~4.7 mm |
| M4 | increasing NH3.H2O | e', e'' and e''/e' rise through more interfaces and interfacial polarization | supports | d2, s3, m1, r1, o10, o11 | interface increase is argued (s3 basis argued) |

MatMech record defects: M1 swaps the -7/-10 morphologies; M2/M3 state -7 has the highest e''/e' and alpha (F5c, F7d rank -10 highest); M3 claims a broad Ku-band -10 dB range (figure: ~16.8-18 GHz only).
