# Judge review: Advanced_Energy_Materials/aenm.201601491

Metal-Organic Framework Cathodes Based on a Vanadium Hexacyanoferrate Prussian Blue Analogue for High-Performance Aqueous Rechargeable Batteries

**Verdict:** accept with minor fixes. 51 nodes, 63 edges, 18 spine nodes. One connected HYP -> DSC/conclusion path: route (p1) -> crystallinity (s3) -> utilization (r1) and cycling (p2) -> V+Fe valence change (s6) -> identified couples (m2) -> multi-electron redox (r2), which meet jointly at the 91 mAh/g capacity (f1); plus the fade branch p2 -> V-site dissolution (s8) -> Rct (r4) -> fade (f3). That is two converging branches plus the fade line off p2, which matches the paper's three-part argument. Every spine STR/PRP/PRF claim has an OBS evidences edge (s3, r1, s6, r2, f1, s8, r4, f3); m1 is basis=argued. Every mm_op names a figure act. Audits are o4, o19 and o21 (3), and all three are fair against the crops. All types, rels, ops and modalities are v04-valid. The node total (51) is above the 25-40 aim, but no node is redundant enough to drop.

## Changes

- o11: panel_ids [] -> [F1g] (TGA is the bottom half of F1g; OCR cue lists only FTIR; recorded in cue_overrides)
- o18 label: Fe edge values ~7124.8->7126.1 corrected to ~7124.3->7125.9 eV as read from F3d
- o19 label and image_note: 'near Fe3+ reference' / '~1.3 of ~5.5 eV' -> '~2/3 toward the Fe3+ line; ~1.6 of ~5.9 eV span'
- s3 source figure -> text; requires_unseen lists the w/ vs w/o HCl sharpness claim (not visible in F1d), the arrow key, and the width/background -> amorphous reading
- s6 source figure -> inferred; requires_unseen lists the linear edge-energy/valence lookup (k4)
- r2 source figure -> text; requires_unseen lists the ~43 mAh/g single-electron capacity
- f1 source figure -> text; requires_unseen lists the earlier-PBA capacities
- h2 requires_unseen added (earlier PBAs Fe-only redox); m3 requires_unseen adds the Fe assignment of the second couple

## Panel checks (every cited crop opened: 15 crops, 23 node citations)

| node | panels | ruling | note |
|---|---|---|---|
| k6 | F5c | confirmed | inset equivalent circuit Re-(CPE1||Rfilm)-(CPE2||Rct-W) printed in crop |
| o2 | F1d | confirmed | all three patterns line up with the V3[Fe(CN)6]2 card bars (200),(220),(400),(420) |
| o3 | F1d | confirmed | simple mixing broad, (200)/(220) merged, raised background; co-precipitated patterns narrower |
| o4 | F1d | confirmed | red (w/ HCl) and blue (w/o HCl) peaks of similar width at ~17.5 and ~24.8 deg; audit holds |
| o5 | F1f | confirmed | HRTEM, 5 nm bar; red arrows on darker patches, white arrows on featureless regions; fringes barely resolved |
| o9 | F1g | confirmed | top half: FTIR bands ~3430 broad, ~2100 strong, ~980 sharp, <650 cm-1 |
| o11 | F1g | confirmed | bottom half: TGA ~100% -> ~75% by ~340 C, step to ~61% at ~360 C; citation restored (was figure-only) |
| o10 | F1h | confirmed | HAADF + Na/V/Fe/C/N/O maps all cover the same particle |
| o6 | F2a | confirmed | initial ~91 / ~81 / ~61 mAh/g; ranking held over 250 cycles |
| o7 | F2a | confirmed | first w/ HCl point ~91 mAh/g |
| o15 | F2a | confirmed | steep drop in first ~20-40 cycles, ~55 mAh/g at 250; CE ~100% |
| o12 | F2c | confirmed | three pairs ~0.55/0.52, ~0.89/0.87, ~1.08/1.07 V; 1.08 V pair current falls over 20 cycles |
| o16 | F3b | confirmed | Fe edge triangles move from ~7123 (0.45 V) to ~7125 eV (1.15 V), between FeO and Fe2O3 |
| o17 | F3c | confirmed | V pre-edge triangles ~5469.7 -> ~5470.5 eV, between V2O3 and V2O5 (VO2 ~5470.3) |
| o18 | F3d | confirmed | monotonic rise for Fe and V; Fe values corrected to ~7124.3 -> ~7125.9 eV |
| o19 | F3d | confirmed | Fe2+ line ~7120.4, Fe3+ ~7126.3 eV; first Fe point ~2/3 toward Fe3+; label numbers corrected |
| o20 | F4a | confirmed | ~98 -> ~54 mAh/g at 3520 mA/g; back to ~78 at 55; first charge ~41 |
| o23 | F4b | confirmed | polarization grows with current; end regions shrink, mid plateau ~0.85 V persists |
| o22 | F5b | confirmed | circle-marked PBA peaks ~17.5, 35, 39.5 deg present from pristine to 250th; asterisk peaks match CFP trace |
| o26 | F5c | confirmed | dotted fits run through the open-circle data for 3rd/60th/150th/250th |
| o21 | F5c | confirmed | lines shift left and steepen with cycling; no semicircle resolvable at 0-80 ohm scale |
| o25 | F5d | confirmed | Rct ~3 -> ~26 ohm at 150, ~24 at 200, ~28 at 250, large error bars; Rfilm ~2-3, Re ~0.5 flat |
| o24 | F5e | confirmed | V ~2.0 (50), ~2.7 (100), ~3.7 (150), ~3.75 (250) mg/L; Fe to ~1.1 |

Overturned: 0.

## Technique mismatches

- o11 (THERMAL:TGA) on F1g, cue FTIR only. The crop holds two plots, FTIR on top and TGA on the bottom (axis labels Relative Mass / Temperature). The staff had dropped the citation. I restored it and recorded a cue override, because the cue list is incomplete rather than wrong. This is the same kind of detector misfire as the micrograph case, but here the missing cue is thermal.
- All other cued crops match: F1d XRD ↔ XRD (o2, o3, o4); F1f micrograph ↔ TEM:HRTEM (o5); F1g FTIR ↔ FTIR (o9); F1h micrograph ↔ STEM:EDS (o10); F2a/F2c/F4a/F4b electrochemistry ↔ ECHEM (o6, o7, o15, o12, o20, o23). F3b-d and F5b-e have no cue class, and on manual check they agree with XAS:XANES, XRD, ECHEM:EIS and ICP:OES.
- read_from: o2 is correctly 'annotation' (it restates the card label). No other OBS restates an annotation string as its observation: legend and element labels only identify series, and values are read from the axis or pixels.

## Mode changes

None. f1 is the only claim with two or more causes edges (r1, r2). Its mode is 'joint', which is correct: no caption or figure presents crystallinity and multi-redox as alternatives.

## Source changes

- s3: figure -> text
- s6: figure -> inferred
- r2: figure -> text
- f1: figure -> text
- h2: inferred -> inferred (requires_unseen added)
- m3: text -> text (requires_unseen extended)

## MatMech (read after the graph was final; graph not edited)

supports 3 · contradicts 1 · not covered 2

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | co-precipitation with HCl, constant molar ratio -> high crystallinity, less amorphous content | supports | p1, s3, o3, o5, o4 | o4 qualifies the w/ vs w/o HCl step |
| M2 | cyanide-O substitution, Fe(CN)6 vacancies, H-bond water network -> multi-electron V+Fe redox, low diffusion activation energy | not_covered | s4, r2 | graph uses the composition only to count electrons (s4 supports r2); no structure -> redox/kinetics causation |
| M3 | large lattice parameter, open framework -> high rate capability | not_covered | f2, m3 | graph attributes rate to the kinetically facile Fe couple (m3), not to the lattice |
| M4 | optimised HCl co-precipitation (high crystallinity) -> cycling stability | supports | p1, s3, r1, s7, o22 | 80% at 880 mA/g is in paper Fig. 5, absent from the packet; at 110 mA/g the graph records ~60% (f3) |
| M5 | amorphous regions around crystallites -> Rct rise during cycling, initial fade | contradicts | m1, s8, r4, m5, o25 | graph (and paper text) assign the amorphous region to Rfilm, which stays flat; Rct rise is traced to V-site dissolution |
| M6 | V and Fe multi-electron redox -> 91 mAh/g capacity | supports | s6, m2, r2, f1, o7 |  |
