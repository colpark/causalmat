# Final node vocabulary (v04)

Status: **final** (merge phase closed after r04). Scope of usage counts: 60 papers (r01–r04), 2109 nodes, 2625 edges, after all renames. `[n, p]` = nodes (or edges) and papers. Full definitions, decision rules and examples are in `vocab/v04.json`; rulings are in `rounds/r04/judge.md`.

**Counts:** 81 type entries = 10 L1 stages + 7 L2 groups + 64 leaves (max depth 3) · 22 mm_ops in 5 families · 14 rels · 13 modalities.

## Design principles

1. A distinction is a type only if it changes the next inference; everything else is an attribute (aspect, via, form, proxy, object, property_family).
2. Types name the role in the argument, never the technique or material; figure form (modality), data origin (provenance) and figure fidelity (image_support) are node fields, not types.
3. Keep the argument skeleton fixed (HYP -> DES -> PRC -> STR -> PRP -> PRF -> DSC, with OBS/KNW as evidence and premises and MEC as bridge) and absorb new cases with boundary rules before adding leaves.
4. Siblings are separated by a written decision rule a new annotator can apply; where staff could not apply it, the siblings were merged unless the next inference differs.
5. An entry used in fewer than 2 of 60 papers survives only if clearly general across material classes.
6. mm_ops name the figure act and its failure modes; what follows from the act is carried by the dst node type, not by the op name.

## Types: L1 stage → L2 group → leaf

The spine runs HYP → DES → PRC → STR → PRP → PRF → DSC/conclusion, with MEC as the bridge between stages. OBS (evidence) and KNW (premises) are never spine.

```

HYP                                         Stage 1, why: the motivation, gap, need or testable expectation the work sets out from.
├─ gap                              [27, 27]  Something is unknown, unmeasured, unexplained or contradictory in the literature
├─ need                             [44, 44]  An application or societal requirement (property level, cost, sustainability, safety) that current material...
├─ hypothesis                       [53, 53]  A testable expectation or proposed strategy: doing X should produce Y

DES                                         Stage 2, choice: a reasoned decision about material, geometry, route, method or comparison axis.
├─ base_system                      [51, 51]  Choice of the host/base material or starting feedstock, with the reason (cost, renewability, known structur...
├─ modification                     [29, 28]  Choice to add or substitute a constituent into a base (dopant, alloying element, reinforcement, filler, co-...
├─ architecture                     [13, 10]  A priori geometric or spatial target to be built: pore/channel lattice, external shape, strut network, laye...
├─ route                            [15, 14]  Choice of processing route, technique, schedule or auxiliary (solvent, catalyst, atmosphere) justified agai...
├─ method                           [16, 14]  Choice of characterization/test method, specimen geometry or sampling protocol because it enables or valida...
├─ variable_sweep                   [46, 45]  The controlled variable(s) and levels that form the comparison axis of the study
├─ down_select                       [10, 9]  A design decision made after, and because of, an observation, screen or weighed claim

PRC                                         Stage 3, act: a processing act or exposure applied to make, shape, modify or probe the material.
├─ synthesis                        [43, 33]  A reaction or assembly step that turns precursors into the target compound, phase, polymer or colloidal obj...
├─ forming                          [30, 25]  Turning feedstock (powder, melt, solution, sol, pellets) into a bulk body or designed shape: casting, sinte...
├─ deposition                        [11, 9]  Applying material onto a substrate as film, coating or layer (PVD, CVD, spin/bar coating, electrodeposition...
├─ joining                            [2, 2]  Joining pre-made bodies into one assembly across a new interface: diffusion bonding, brazing, welding, TLP ...
├─ treatment                        [22, 15]  Modifying the structure of an already-made material of the target compound: annealing, ageing, solution tre...
├─ stimulus                         [15, 15]  An external perturbation or exposure (thermal pulse, load, field, bias or cycling, corrosive/biological env...

OBS                                         Evidence: a readout from a measurement or computation before interpretation; never spine. Subtype names WHAT FEATURE of the data is read; modality, provenance and image_support are node fields.
├─ signal/                                  Discrete features of a trace (peaks, bands, reflections, edges, steps, pole-figure maxima) read individually, or a whole trace judged against a reference or model trace.
│  ├─ reference_match               [23, 16]  A whole measured trace (pattern, spectrum or response curve) judged to coincide or not with a reference tra...
│  ├─ feature_assignment            [48, 30]  Individual features assigned to origins: reflections indexed to phases, bands to groups, NMR signals to sit...
│  ├─ feature_presence              [41, 25]  A feature appears or disappears between samples, stages or times, or a specific expected feature is absent ...
│  ├─ feature_shift                 [18, 14]  A feature's position read relative to a reference: moving across a series (aspect=shift), or offset/overlap...
│  ├─ feature_quantification        [36, 21]  Feature intensity, area or width read as a measure of an amount or degree, qualitatively (grows, fades) or ...
├─ response/                                A quantity read as a function of a variable or condition, over an ensemble, or split into contributions.
│  ├─ trend                        [225, 53]  How a quantity changes with a varied variable or ranks across groups: direction, monotonicity, ranking (att...
│  ├─ characteristic_value         [124, 48]  A defined point or level read from a curve, test or table: onset, peak, step, minimum, crossing that fixes ...
│  ├─ fitted_parameter              [25, 18]  A parameter obtained by fitting a functional form or model to data: exponent, slope, activation energy, rat...
│  ├─ distribution                    [9, 3]  The spread and shape of a non-imaged quantity over an ensemble (computed sites, specimens, DLS classes, ind...
│  ├─ component_partition             [7, 6]  A total response shown with its separated contributions (co-plotted or decomposed, at one condition or acro...
│  ├─ regime_map                      [3, 3]  Boundaries between states or regimes in a condition space, 2-D or 1-D: TTT/CCT, phase or exchange-pathway d...
├─ morphology/                              Spatial/visual content of an image or map (micrograph, photograph, element map, tomogram, fluorescence image).
│  ├─ appearance                   [131, 49]  Qualitative reading of what imaged features look like, or whether a signal is there: shape, surface/fractur...
│  ├─ feature_metric                [60, 37]  A measured metric of imaged features: size or size distribution, number density, thickness, area fraction, ...
│  ├─ distribution                  [39, 27]  Spatial arrangement of features, elements or a labelled species across the field: uniformity, clustering, a...

STR                                         Stage 4, structure: a claim about the material's structure at any scale, inferred from observations (or imposed by model construction).
├─ phase/                                   Crystal/phase-level structure: which phases, how much, cell dimensions, site occupancy.
│  ├─ identity                      [38, 32]  Which phases or crystal structures are present, incl. 'no secondary phase' and mesoscale periodic arrangeme...
│  ├─ fraction                      [14, 13]  How much of a crystalline phase is present, incl. its evolution: phase fraction, degree of transformation, ...
│  ├─ lattice                       [12, 11]  Unit-cell dimensions, interlayer spacing or lattice strain and their change.
│  ├─ site_occupancy                  [5, 5]  Distribution of constituents over the crystallographic sites of a phase: site preference, inversion, antisi...
├─ chemistry/                               Molecular/chemical-level structure: bonds and configuration, elemental composition and valence.
│  ├─ bonding                       [24, 17]  Bonds, functional groups, linkages or coordination present or converted, up to full molecular structure
│  ├─ composition                   [11, 10]  WHAT a phase or region is made of: elemental composition, stoichiometry, valence, solute content, per-layer...
├─ defect/                                  Crystallographic defects: point (0-D) vs line/planar (1-D/2-D).
│  ├─ point                           [8, 5]  Substitutional, interstitial or vacancy species by charge state, compensation, position (aspect=position) o...
│  ├─ extended                        [5, 3]  Line and planar defects (dislocations, stacking faults, twins, APBs) and their density
├─ microstructure/                          Arrangement of grains, particles, pores, phases and cracks at meso/micro scale.
│  ├─ feature_size                  [29, 25]  Size of structural units (grains, particles, crystallites, pores, layers)
│  ├─ distribution                  [23, 21]  Spatial distribution of a constituent: dispersion, agglomeration, segregation, gradient, shell/coating cove...
│  ├─ shape                         [20, 16]  Shape and topography of structural units or of a built architecture (lenticular, equiaxed, lamellar, core-s...
│  ├─ porosity                      [15, 14]  Amount, connectivity and hierarchy of porosity: void fraction, relative density, open vs closed, interconne...
│  ├─ orientation                     [4, 3]  Orientation state: crystallographic texture, molecular/fibre orientation, grain-boundary character (misorie...
│  ├─ damage                          [3, 2]  Loss of continuity induced in a made material by load, thermal cycling or environment: microcracks, gouge, ...
├─ interface                        [11, 10]  State of an interface or boundary between constituents or with a substrate: bonding, reaction layer, cohere...

PRP                                         Stage 5, property: a claim about a property of the material or of an assembly (attrs.object); attrs.property_family required; attrs.basis=argued when unmeasured.
├─ value                           [137, 57]  The level of a property or its change with a design variable or condition, incl. a claim that one contribut...
├─ behavior_class                   [19, 18]  A categorical classification of how the material behaves: failure/wear/decay mode, conduction type, magneti...
├─ descriptor                       [13, 10]  A microscopic descriptor between structure and a measured property as intermediate cause: carrier density, ...
├─ diagnostic                         [7, 7]  A quantity whose role is to identify a mechanism via a known mapping (stress exponent, activation energy, A...

PRF                                         Stage 6, performance: a claim about how the material, device or process performs in a use or test condition.
├─ figure_of_merit                    [6, 6]  A composite application metric combining several properties or normalising a property per mass, volume or c...
├─ service_capability               [55, 39]  The material, device or method performs (or fails) under a stated use condition, or a built prototype or pr...
├─ qualification                      [6, 5]  Performance judged against an external criterion: standard pass/fail, spec, rating compared with a threshol...

MEC                                         Bridge: a mechanistic explanation linking cause to effect across stages; attrs.mechanism_class names the physics.
├─ pathway                         [132, 58]  A causal pathway by which a cause produces an effect
├─ identification                   [17, 14]  The operative mechanism is identified as one member of a known catalogue (rate-controlling step, transforma...
├─ tradeoff                           [7, 7]  A net outcome explained by one contribution outweighing an opposing one

KNW                                         Premise: prior knowledge, literature or theory brought in as an input; never spine.
├─ precedent                        [49, 36]  A specific earlier result (own or others') used as analogy, support or comparator.
├─ model                            [38, 29]  A named model, formalism or governing equation used to compute, fit or predict.
├─ lookup                           [22, 20]  A known mapping from an observable value or feature to its interpretation: diagnostic value -> mechanism, b...
├─ fact                             [24, 21]  A tabulated fact or known structure of a constituent used as a premise (constant, radius, composition, crys...

DSC                                         Stage 7, discussion: conclusion, comparison, guidance, limitation or outlook drawn from the results.
├─ conclusion                       [57, 57]  Summary claim of what was shown and what is new
├─ comparison                       [21, 20]  Results set against prior work, a model prediction or an incumbent
├─ design_guidance                  [21, 21]  A generalised design rule, optimum window or trade-off recommendation drawn from the results.
├─ limitation                       [23, 20]  A stated limit of method or data, or an anomaly attributed to artefact, that bounds a claim (kind = method ...
├─ outlook                          [17, 17]  Proposed application or next experiment (kind = application | research).
```

## mm_ops (multimodal reasoning operations), by family

Required on every edge whose src is an OBS node with a figure. The op names the figure act and its failure modes; what follows is carried by the dst type.

### read: Extract a feature from one figure: a direction, a point, a spread, a local feature or a spatial pattern.

| op | usage [edges, papers] | act |
|---|---|---|
| `read_trend` | [92, 43] | Read the direction, monotonicity, saturation or change of ranking of a quantity across an ordered series or along an axis. |
| `read_characteristic_point` | [60, 35] | Read a defined point from a curve or scan: onset, peak, minimum, inflection/step, threshold or curve crossing, value at a condition; also locating a sample relative to regime boundaries. |
| `read_distribution_statistics` | [9, 3] | Read range, central value, width, tails, per-class offsets or overlap from a distribution of a non-imaged quantity |
| `inspect_local_feature` | [24, 17] | Judge a local feature (interface, defect, grain shape) in one high-magnification view; representativeness is an assumption. |
| `assess_spatial_distribution` | [17, 15] | Judge uniformity, clustering, alignment, segregation or localisation of features, elements or a labelled species across a field or map. |

### compare: Set two or more traces, panels, figures or sources against each other and read the difference, co-variation or coincidence.

| op | usage [edges, papers] | act |
|---|---|---|
| `compare_across_conditions` | [270, 57] | Compare panels, frames, traces or curves that differ in one condition (design variable, stage, time, before/after) and read the difference, incl. following a spectral or diffraction feature through a stack of traces. |
| `track_feature_across_series` | [4, 3] | Follow one identified OBJECT (atom, particle, layer, crack tip, domain wall, ion) through time-lapse, trajectory or loading frames and read its displacement, sequence or appearance |
| `compare_coplotted_quantities` | [21, 15] | Read two or more different quantities, species or components on shared axes (or in separate figures sharing axis quantity and units) and judge dominance or positional overlap (aspect=overlap) |
| `compare_with_reference_value` | [16, 11] | Position this work's data against reference VALUES plotted, tabulated or quoted alongside: prior work, incumbents, constants, an in-paper benchmark system. |
| `correlate_across_series` | [17, 13] | Align the same sample series across two or more figures with different ordinates and judge co-variation; licenses correlational attribution only. |
| `register_colocated_views` | [23, 17] | Register two or more views of the SAME region (image + map, line scan, point analysis, SAED at marked positions, magnifications, probe/indent positions on a photograph) so content read in one is located on a feature in the other; allowed on derives edges when a colocalisation coefficient or channel ratio is computed |

### match: Map figure content to a reference, a design, a label or a known class.

| op | usage [edges, papers] | act |
|---|---|---|
| `match_to_reference` | [11, 7] | Judge a whole trace or image against an EMPIRICAL reference (parent sample, standard, database card). |
| `match_to_design` | [9, 6] | Compare an image of a fabricated object with its intended geometry (CAD/STL, mold, template, target dimension) and judge fidelity. |
| `assign_features` | [42, 23] | Assign individual peaks, bands, signals, steps or contrast levels to phases, groups, sites or processes via a known mapping; incl. orientation relationship in superposed patterns (aspect=orientation_relationship). |
| `recognize_signature` | [19, 14] | Match a visible morphology or a curve shape to a known class that implies a mechanism (dimples -> ductile; lenticular -> martensitic; sigmoid, C-curve). |

### quantify: Turn figure content into numbers, parameters or a new derived series (the ops allowed on derives edges, plus register_colocated_views for two-channel ratios).

| op | usage [edges, papers] | act |
|---|---|---|
| `measure_feature_metric` | [43, 26] | Measure sizes, counts, densities, thicknesses, area or boundary fractions of imaged features, or extract a line profile from one image. |
| `convert_to_quantity` | [24, 17] | Convert a feature or readout into a physical quantity through a stated relation; attrs.via = intensity (peak/ROI integrals -> amount; audit background, saturation) \| position (Bragg, Vegard; audit reference and calibration of axis) \| calibration (in-paper calibration; audit target inside calibrated range, comparable state, monotone inversion) \| known_relation (C = I dt/dV, Arrhenius from two points) \| model (Rothwarf-Taylor inversion). |
| `fit_model` | [31, 20] | Fit a functional form to data to obtain parameters: slope/intercept on linearised axes, power law, Arrhenius, Tauc, equivalent circuit, deconvolution; attrs.form = linearised \| power_law \| nonlinear \| circuit \| decomposition |
| `replot_derived_series` | [46, 18] | Build a new series or diagram from other readouts: arithmetic combination, subtraction of a background/reference trace, aggregation, resampling at iso-levels, re-plot against another variable. |

### check: Test agreement or consistency: model against data, curves under normalisation, figures against each other or against the text.

| op | usage [edges, papers] | act |
|---|---|---|
| `overlay_model_on_data` | [33, 13] | Judge agreement region by region between model/fit/simulation output and data, overlaid, side by side or in matched panels |
| `collapse_by_normalization` | [5, 3] | Re-plot against a normalised or corrected variable and check whether curves or points from different conditions merge; the merge is the evidence |
| `cross_check_consistency` | [28, 19] | Verify that quantities read from different figures, panels or the text agree arithmetically or in trend; incl. flagging a point or series that deviates and setting it aside (aspect=outlier). |

Attributes on ops: `convert_to_quantity` → `attrs.via` = intensity | position | calibration | known_relation | model; `fit_model` → `attrs.form` = linearised | power_law | nonlinear | circuit | decomposition; `compare_coplotted_quantities` → `aspect=overlap`; `assign_features` → `aspect=orientation_relationship`; `cross_check_consistency` → `aspect=outlier`.

## Rels (edge vocabulary)

| rel | usage [edges, papers] | meaning |
|---|---|---|
| `motivates` | [243, 60] | HYP/DSC/OBS gives reason for a DES/PRC choice or a test; a weighed claim (PRP/PRF/MEC, e.g. a trade-off or ranking) may motivate a DES/down_select (screen-then-choose) |
| `realizes` | [163, 60] | a DES choice is carried out by a PRC act or a measurement; in computation-first papers also by constructing an in-silico structure, in which case dst may be a STR node with attrs.basis=imposed; a spine DES/method whose measurement is a headline contribution may realize the STR/PRP/MEC claim it makes measurable |
| `feeds_into` | [42, 32] | src PRC act's product is the workpiece, precursor, mold or template of dst PRC act (ordered multi-step route). PRC->PRC only; replaces realizes/premise_for between PRC nodes |
| `produces` | [171, 58] | a PRC act or condition yields a structural state |
| `evidences` | [755, 60] | an OBS supports a claim (STR/PRP/PRF/MEC) or a DSC/comparison or DSC/limitation verdict. Source must be OBS |
| `causes` | [290, 59] | physical causation in the material: one state leads to another (processing -> structure -> property -> performance). Not for claim-to-conclusion reasoning |
| `explains` | [150, 60] | a MEC accounts for a claim |
| `premise_for` | [177, 57] | a KNW node, or an in-paper node used as an input, supplies an assumption, equation, parameter or condition value for another inference or derivation (absorbs proposed 'parameterizes') |
| `contrasts` | [20, 16] | a claim or OBS is compared against a control, baseline, model or alternative |
| `rules_out` | [6, 6] | evidence or reasoning rejects an alternative explanation |
| `derives` | [108, 37] | dst OBS is computed from src OBS by arithmetic, data reduction, fitting or re-plotting; dst is NOT independent evidence (absorbs proposed 'reduces_to'). Carries an mm_op when src has a figure |
| `qualifies` | [104, 53] | a limitation, caveat, anomaly or contradicting readout bounds the scope or confidence of a claim, or contradicts it outright; the strength of the conflict is carried by the target's image_support (partial \| contradicts) and the audit node's label |
| `counteracts` | [8, 8] | src effect opposes the outcome dst stands for (the loss term of a trade-off) |
| `supports` | [388, 56] | a claim is used as a premise for another claim or conclusion (claim -> claim or claim -> DSC reasoning), as opposed to physical causation (causes) or direct measurement (evidences) |

Keep three apart: `evidences` (OBS → claim), `causes` (physical causation in the material), `supports` (claim → claim or → DSC).

## Node fields

| field | applies to | values | rule |
|---|---|---|---|
| `modality` | OBS (required) | micrograph [146], diffraction_pattern [56], spectrum [75], xy_curve [336], spatial_map [35], table [13], schematic [3], photograph [22], simulation_render [10], text_only [82], volume_render [2], orientation_distribution [7], dispersion_diagram [1] | the panel actually read; split a node that reads two panel kinds. 1-D diffraction traces are diffraction_pattern, bar charts xy_curve |
| `provenance` | OBS (required) | measured [588], derived [83], computed [74] | derived needs an incoming `derives` edge; review papers add `attrs.reproduced_from` |
| `image_support` | any node with figs (required) | shown [547], partial [155], not_shown [4], contradicts [10] | judged from the opened image, not the caption; unopened figure → `figs=[]` + `attrs.fig_ref`; what the image shows goes in `attrs.image_note` |
| `spine` | every node (required) | true / false | 10–20 spine nodes, one connected stage-ordered path HYP → DSC/conclusion, ≤2 parallel branches + 1 control branch; OBS/KNW never spine |
| `attrs.text_silent` | OBS (optional) | true | figure shows content the text never states AND it bears on a spine claim; otherwise `attrs.image_note` |
| `attrs.basis` | STR/PRP/PRF/MEC (optional) | evidenced (default), argued, attributed, imposed | evidence through a proxy stays evidenced, name it in `attrs.proxy` |

`attrs.property_family` (required on PRP): mechanical, thermal, thermodynamic, electrical, ionic_electrochemical, catalytic, magnetic, optical, chemical_corrosion, kinetic, biological, surface, photochemical.

