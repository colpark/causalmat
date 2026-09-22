# Judge review: Journal_of_Materials_Science_&_Technology/j.jmst.2020.05.053

**Verdict:** accept with minor fixes. 18 spine nodes, 49 total, one connected path with two branches (strength/hardening; interphase damage -> fracture mode). 2 audits (a1, n22), fair.

## Checklist

- spine_primary_argument: yes: gap -> Cr-free EHEA + strain sweep -> casting -> L12+B2 lamellar eutectic -> tension -> FCC-first dislocation evolution (0.6%, 1.5%, fracture) -> interface pile-up MEC -> strength; substructure MEC -> three-stage hardening -> hardening capacity -> ductility; interphase damage -> mixed fracture -> conclusion
- spine_nodes: 18
- total_nodes: 49
- connected: True
- spine_evidence: every spine STR/PRP has an evidences edge; MEC n11 basis argued, n15 evidenced by o8 (correlate_across_series)
- v04_rules: types, rels and modalities valid; one mm_op fix (o3->n6); o9 provenance fixed
- mm_ops: name the figure act after the o3 fix
- audits: 2 audit nodes (a1, n22), fair: a1 notes F3a does not resolve the captioned pile-up that n11 leans on; n22 notes deformed TEM images carry no phase labels

## Changes

- e(o3->n6): mm_op register_colocated_views -> inspect_local_feature (o3 reads one TEM panel, F1c; no second view of the same region is registered)
- a1: label reworded so it no longer rests on the caption (caption wording moved to image_note; source 'figure' now holds); image_support shown -> partial (parallel line contrast along the lower interface of F3a may be stacked dislocations or thickness fringes)
- o16 label: 'sparse (F3a)' -> 'unresolved mottled contrast (F3a)'; F3a shows no discrete lines
- o9 provenance measured -> derived (true stress is converted from the engineering curve); added derives edge o6->o9 (replot_derived_series) so derived has its incoming derives edge

## Panel checks (every cited crop opened; 18 crops, 47 node-panel citations)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| n5 | F1a, F1d, F1e | confirmed | - | XRD indexed L12 (superlattice peaks ~25, ~35.5 deg) and B2 (~31, 44.6 deg); SAED FCC[011] and BCC[011] with circled superlattice spots |
| n6 | F1b, F1c | confirmed | - | EBSD red/green lamellar colonies radiating from colony boundaries; TEM parallel lamellae A/B |
| n8 | F3a, F3b | confirmed | - | mottled lamella beside featureless one (a); planar slip traces and circled outcrops (b); phase of each lamella not labelled, partial is right |
| n9 | F4a, F4b, F4c, F4d, F4e | confirmed | - | tangled lines + labelled pile-up (a), slip band (b), pile-up along curved boundary (c), intersecting curved lines (d), labelled networks (e) |
| n10 | F5a, F5b | confirmed | - | walls/Taylor lattice with arrowed pile-up (a); straight parallel dislocations (b); B2 identity of b from caption |
| n12 | F2a, F2b | confirmed | - | UTS ~1000 MPa and failure drop at ~6.5% on F2a (label 6.2%); F2b inset true stress to ~1070 MPa |
| n13 | F2b | confirmed | - | dashed stage lines at ~0.009 and ~0.058; rate ~84 -> ~14 -> ~5 GPa then negative |
| n16 | F2d | confirmed | - | red arrows (holes), red boxes (cracks) and red chevrons at lamella ends; phase on each side not distinguishable |
| n17 | F2c, F2d | confirmed | - | tear ridges and elongated grooves (c); blue-circled facet with faint lines (d) |
| n19 | F1b | confirmed | - | red area visibly dominant (~2/3); text 60/40 |
| o1 | F1a | confirmed | - | indexed markers and reference sticks as stated |
| o2 | F1d, F1e | confirmed | - | zone axes and circled superlattice spots as stated |
| o3 | F1c | confirmed | - | lamellae ~0.8-0.95 um measured against the 0.5 um bar (~70 px) |
| o4 | F1b | confirmed | - | lamellar colonies of two colours, no single-phase regions |
| o5 | F1b | confirmed | - | red area ~2/3 by eye; the stored 69-74% count could not be re-run (no image library in this environment) |
| o6 | F2a | confirmed | - | yield bend near 550-620 MPa, UTS ~1000 MPa, drop at ~6.5% |
| o7 | F2a | confirmed | - | 0.6% marker at ~615 MPa, 1.5% at ~750 MPa |
| o8 | F2b | confirmed | - | rate curve and stage boundaries as stated |
| o9 | F2b | confirmed | - | inset true stress ~410 -> ~1070 MPa to 0.06 |
| o10 | F2c | confirmed | - | tear ridges, grooves, scattered holes |
| o11 | F2d | confirmed | - | arrowed holes and boxed cracks |
| o12 | F2d | confirmed | - | blue circle; lines faint, partial is right |
| o13 | F3a | confirmed | - | featureless upper lamella, mottled lower lamella, parallel lines along lower interface |
| o14 | F3b | confirmed | - | parallel slip traces top-left; two circled outcrops with annotation |
| o15 | F4a, F4c | confirmed | - | 'Dislocations pileup' labels in both; dense band along boundary in c |
| o16 | F3a, F4a, F5a | confirmed | - | increase across the three states is visible; F3a has no resolved lines (label fixed) |
| o17 | F4b | confirmed | - | labelled slip band; featureless lamella at bottom edge |
| o18 | F4d | confirmed | - | curved lines enclosing cells |
| o19 | F4e | confirmed | - | labelled networks, cross-hatched contrast |
| o20 | F5a | confirmed | - | walls, 'Taylor lattice' label, arrow top-left |
| o21 | F5b | confirmed | - | straight parallel lines along one trace direction |
| a1 | F3a | confirmed | - | no resolved pile-up; faint parallel lines along lower interface keep this partial |

Overturned: 0.

## Technique mismatches

None. F1a XRD/XRD; F2a-b mechanical/MECH:tensile; F1c, F2c-d, F3-F5 micrograph/TEM or SEM; F1b, F1d, F1e carry no cue class (EBSD, TEM:SAED). No cue overrides needed. read_from checked: o1, o2, o14, o15, o17, o19, o20 restate listed annotations and are 'annotation'; the rest read pixels or axes.

## Source / requires_unseen

- a1: label reworded so it no longer needs the caption wording; source 'figure' holds. All text-sourced nodes list their unseen facts.

## Mode changes

None. Only n8 has two causes edges (n5, n6); marked joint, and no caption or figure shows a choice between them.

## MatMech (read after the graph was final; graph not edited)

supports 7 / contradicts 0 / not covered 0

| M | cause | effect | verdict | nodes | note |
|---|---|---|---|---|---|
| M1 | bulk casting (induction melting, Ar) | dual-phase L12+B2 lamellar eutectic, 60/40, 1-2 um lamellae | supports | n4, n5, n6, n19 | n4 produces n5, n6; 60/40 in n19 (EBSD reads ~2/3 FCC); graph measures TEM lamellae ~0.8-0.9 um, not 1-2 um |
| M2 | soft FCC(L12) + hard B2 lamellar structure | UTS 1005 MPa and 6.2% ductility | supports | n5, n6, n8, n11, n14, n12, n18 | via FCC-first slip, interface pile-up (n11) and hardening capacity (n14); F2a failure at ~6.5% vs 6.2% label |
| M3 | dual-phase L12+B2 lamellar structure | three-stage work hardening | supports | n5, n6, n8, n9, n10, n15, n13 | n15 maps stages to phase-specific substructure; explains n13 |
| M4 | bulk casting | FCC dislocation substructures (planar slip -> networks -> walls, Taylor lattices) | supports | n4, n7, n8, n9, n10 | graph routes this through the tensile stimulus n7 (n4 feeds_into n7 produces n8 -> n9 -> n10); casting is upstream, not the proximate cause |
| M5 | FCC dislocation substructure evolution | high work-hardening ability, delayed necking | supports | n9, n10, n15, n13, n14 |  |
| M6 | FCC(L12)/B2 phase interface | ductile FCC / brittle B2 mixed fracture | supports | n16, n17 | interface voids/cracks (n16) cause mixed fracture (n17); B2 location of river pattern is text-only |
| M7 | dislocation pile-up at FCC/B2 boundaries | high yield strength 559 MPa | supports | n8, n11, n12 | n11 basis argued and qualified by a1 (F3a does not resolve the captioned pile-up); pile-ups shown only at 1.5% (o15) |
