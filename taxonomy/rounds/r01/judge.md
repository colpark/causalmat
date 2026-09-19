# Round r01: judge rulings (v00 → v01)

**Inputs:** PROTOCOL.md, vocab/v00.json, proposals_S1.json (JMA Mg-SiCp creep; Acta Ti DTEM), proposals_S2.json (J. Adv. Ceram. thermoelectric sulfide; POC bio-based PU coating), all 4 graphs, 3 packets read in full or in part.

**Result:** 141 staff proposals (99 types, 37 mm_ops, 5 rels) ruled: **ACCEPT 18, MERGE 84, RESTRUCTURE 36, REJECT 3**. I also ruled on 6 cross-cutting or judge-initiated items (image_support, the OBS cut, provenance, `supports`, 2 provisional leaves). v01 has **75 type entries = 10 L1 + 7 L2 groupings + 58 leaves** (depth ≤ 3; only OBS and STR use L3), **13 rels**, **21 mm_ops in 6 families**, and 122 renames. All 135 r01 nodes migrate to a v01 type through `renames`. 56 of the 58 leaves are used by r01 nodes; the 2 unused are the provisional `PRC/treatment` and `STR/chemistry/composition`.

## Spot checks (graphs vs packets, figures opened)

Graphs checked against packets: **JMA** (all nodes vs packet text and MatMech blocks) and **Ceramics** (all nodes). Figures opened: JMA F1, F3, F7; Ceramics F2, F5, F7; Acta F4, F5; POC F7 (9 figures).

| figure | staff label | verdict |
|---|---|---|
| JMA F1 optical micrographs | n7 feature_size, fit=poor; n6 distribution | **Confirmed.** Grain boundaries are visible only in (a). In b–f the particles hide them, so 65→22 µm cannot be read from the figure (`image_support: not_shown`). Particle clustering and streaking are visible in d–f, which the text denies (`n6: partial`). |
| JMA F3 bar chart | n16 xy_curve, contrast_coplotted_quantities | Modality OK under v01's `xy_curve` definition (bar charts count). The UTS decline 188→174 MPa is real but mostly inside the error bars, so `partial` rather than `contradicts`. |
| JMA F7a/b log–log | extract_slope, collapse_by_normalization | **Confirmed.** In (b) the lines bunch together, so the collapse op is correct. In (a) the 5/10 wt% points lie above AZ91 at 120 MPa, as S1 notes. This belongs in a `text_silent` OBS node. |
| Ceramics F2 XRD/XPS | reference_match, peak_shift, diffraction_pattern / spectrum | Modalities correct. The x=0.1 trace is visibly degraded (broad hump near 20–23°). The doped XPS Cr 2p signal is at noise level, so `n11: partial` at best. |
| Ceramics F7 κ | component_partition | **Confirmed an internal inconsistency:** for x=0.1, κ_total ≈1.38 minus κe ≈0.57 gives 0.81, but κl is plotted as ≈1.27. The other three samples close to within 0.02. This is the model case for `image_support: contradicts` + mm_op `cross_check_consistency`. |
| Ceramics F5 (paper Fig. 6) m* vs n | derived m*, compare_with_literature | Correct. **Packet F-ids are not paper figure numbers** (packet F5 = paper Fig. 6, packet F6 = paper Fig. 5). Staff must cite packet ids. n14 (Hall n) reads n only from abscissa positions on this plot → `partial`. |
| Acta F4 SAED + radial profiles | a12 diffraction_pattern, a14 **xy_curve** | a14 is wrong. The radial intensity profile is a 1D diffraction trace, so it should be `diffraction_pattern` (now stated in modality_notes). The unlabelled "Liquid Phase" hump in the difference pattern is visible, so it becomes a `text_silent` node. |
| Acta F5 β-fraction vs log t | read_curve_shape_against_template | Confirmed. Shoulders at ~0.1–0.3 are visible at 1575, 1450, 1200 K (weakly at 1400 K). "Single sigmoid" in the text is `partial`. |
| POC F7 photographs | photograph; inspect_visual_uniformity, compare_panels | Correct. MDI panel streaked, IPDI clear, dipentene panel shows a specular highlight. Both ops map to `compare_across_conditions`. |

Staff figure-reading quality is high. Both staff found real image/text discrepancies, and the new `image_support` field exists to capture them.

Graph-level errors found (rel misuse), all fixed by v01 rel definitions:
- `evidences` from non-OBS sources: Acta a22→a20 (STR→MEC), a25→a26 (PRP→MEC); Ceramics n10→n12 (STR→STR). Use `supports`.
- `causes` used for reasoning rather than physics: Ceramics n32→n34, n22→n34 (claim→conclusion); POC n4→n21 (DES variable_sweep→PRP), n21/n24/n30/n31→n32. Use `supports`. A DES→PRP link must route through PRC/STR or a MEC.
- `motivates` used claim→DSC: JMA n17/n27/n11→n35. Use `supports`.
- JMA n24 (UTS-limiting mechanism) comes from the MatMech extraction block, not from packet text. Keep only with `attrs.source: "matmech"`. It is also a `counteracts` edge to n17, not `explains`.

## Cross-cutting rulings

**(a) `image_support` node field: ACCEPT.** It is required on every node with non-empty `figs`. Values:
- `shown`
- `partial`
- `not_shown`
- `contradicts`

The definitions are in PROTOCOL.md and in `vocab.node_fields`. `attrs.image_note` holds what the figure does show. Figure content the text never mentions becomes its own OBS node with `attrs.text_silent: true`. It is not folded into an existing node. I rejected S1's three-value version ({shown, partly, not_visible}) because it cannot express the most informative case, a figure that contradicts the text (Ceramics F7 x=0.1; POC NMR b/e labels swapped; C=C at ~3010 vs text 3180 cm⁻¹).

**(b) New rels:**
- **`derives`: ACCEPT, absorbing `reduces_to`.** Arithmetic combination (S2) and data reduction (S1) have the same consequence: the dst is not independent evidence.
- **`parameterizes`: MERGE → `premise_for`.** premise_for is broadened to in-paper inputs, because the source type already says whether the premise is KNW or in-paper data.
- **`qualifies`: ACCEPT.**
- **`counteracts`: ACCEPT.**
- **Judge addition: `supports`,** for claim→claim and claim→DSC reasoning. `causes` is now restricted to physical causation and `evidences` to OBS sources. This was the most frequent graph error in r01. Without the split, a causal graph would mix physics with argumentation.

**Provenance (judge restructure).** S1's `OBS/derived/*` and `OBS/computation/*` and S2's `OBS/response/derived_quantity` all encode where the data came from. That axis is orthogonal to what is read, so it is now a required OBS field, `provenance`, with values measured | derived | computed. A computed TTT diagram is `OBS/response/regime_map` with provenance=computed. This removes 6 would-be leaves without losing the distinction.

**OBS cut: S2 wins.** OBS L2 is the feature of the data that is read:
- `signal`: discrete features of spectra and patterns
- `response`: a quantity vs a variable
- `morphology`: spatial or visual content

S1's technique families (imaging, diffraction, mechanical, computation) duplicate `modality` and `attrs.technique`. They would also grow without limit (electrochemical, magnetic, optical…). The deciding test was cross-paper sharing. Under S2's cut, XRD, XPS, FTIR, NMR and electron diffraction share the five `signal` leaves across a ceramic, a polymer and a metal paper. Under S1's cut, the Acta SAED indexing and the POC NMR assignment land in different L2s even though they are the same inferential act.

**Other cuts made in the same spirit.** PRP and MEC were flattened to argumentative roles. Property family and physical mechanism class are required attrs, not types. A family-based PRP (mechanical/thermal/…) would reach 30+ leaves at 64 papers, and after a property claim the next inference (explained by a MEC, leads to a PRF) does not depend on the family.

## Rulings table

| # | proposal | staff | kind | ruling | reason |
|---|---|---|---|---|---|
| 1 | `HYP/need/performance_requirement` | S1 | type | RESTRUCTURE -> `HYP/need` | Accepted as concept, flattened to L2; need vs gap changes the next check (is performance achieved? vs is knowledge produced?) |
| 2 | `HYP/gap/unobserved_regime` | S1 | type | MERGE -> `HYP/gap` | 'Unobserved regime' is one kind of gap; attrs.gap_kind |
| 3 | `HYP/strategy` | S1 | type | MERGE -> `HYP/hypothesis` | A strategy stated as an expectation is a testable hypothesis |
| 4 | `DES/material/system_choice` | S1 | type | MERGE -> `DES/base_system` | Same role as S2 feedstock/selection: choosing the host/base |
| 5 | `DES/experiment/parametric_sweep` | S1 | type | MERGE -> `DES/variable_sweep` | Proposed independently by both staff; one entry |
| 6 | `DES/method/characterization_approach` | S1 | type | MERGE -> `DES/method` | Method, specimen and sampling choices share one role (enable/validate a measurement); aspect in attrs |
| 7 | `DES/method/sampling_protocol` | S1 | type | MERGE -> `DES/method` | Rarely stated as a separate argumentative step; attrs.aspect=sampling, link to claims via qualifies |
| 8 | `DES/specimen/form_factor` | S1 | type | MERGE -> `DES/method` | Specimen geometry chosen for a measurement is a method choice; attrs.aspect=specimen |
| 9 | `PRC/fabrication` | S1 | type | RESTRUCTURE -> `PRC/forming` | Too broad: split into synthesis / forming / deposition / treatment (they lead to different structural checks). JMA stir casting -> forming; Acta flash evaporation -> PRC/deposition |
| 10 | `PRC/stimulus/transient` | S1 | type | RESTRUCTURE -> `PRC/stimulus` | Accepted, flattened; 'transient' is an attribute. General: in-situ heating, loading, cycling, exposure studies |
| 11 | `OBS/imaging/feature_distribution` | S1 | type | RESTRUCTURE -> `OBS/morphology/distribution` | Readout kind kept; L2 'imaging' repeats modality and is replaced by readout family 'morphology' |
| 12 | `OBS/imaging/feature_size` | S1 | type | MERGE -> `OBS/morphology/feature_metric` | Size, count and density are one quantitative image readout; metric in attrs |
| 13 | `OBS/imaging/interface_appearance` | S1 | type | MERGE -> `OBS/morphology/appearance` | Interface is the imaged object (attrs.object), the readout is qualitative appearance; STR/interface carries the distinction |
| 14 | `OBS/imaging/fracture_surface` | S1 | type | MERGE -> `OBS/morphology/appearance` | Fracture surface is the object; failure-mode inference is carried by mm_op recognize_signature and PRP/behavior_class |
| 15 | `OBS/imaging/morphology_change` | S1 | type | MERGE -> `OBS/morphology/appearance` | Change across time/state is a comparison (mm_op compare_across_conditions + attrs.direction), not a readout kind; metric changes go to feature_metric |
| 16 | `OBS/diffraction/phase_reflections` | S1 | type | MERGE -> `OBS/signal/feature_assignment` | Indexing reflections to phases = assigning features to origins, technique-agnostic. Whole-pattern matches (Acta a6) -> OBS/signal/reference_match |
| 17 | `OBS/diffraction/phase_quantification` | S1 | type | RESTRUCTURE -> `OBS/signal/feature_quantification` | Kept, generalised beyond diffraction (conversion from IR, crystallite size from broadening) |
| 18 | `OBS/mechanical/strength_values` | S1 | type | MERGE -> `OBS/response/trend` | Technique-family cut rejected; strength vs design variable is a trend (single test ratings -> characteristic_value) |
| 19 | `OBS/mechanical/time_dependent_deformation` | S1 | type | MERGE -> `OBS/response/trend` | Strain vs time is a trend along time; creep is attrs |
| 20 | `OBS/mechanical/rate_vs_stress` | S1 | type | MERGE -> `OBS/response/fitted_parameter` | As S1 suspected: the argumentative content is the exponent |
| 21 | `OBS/derived/fitted_parameter` | S1 | type | RESTRUCTURE -> `OBS/response/fitted_parameter` | Kept as readout kind; 'derived' moves to the new provenance field |
| 22 | `OBS/derived/kinetic_curve` | S1 | type | MERGE -> `OBS/response/trend` | Fraction vs time is a trend; provenance=derived and derives edges record that it is assembled |
| 23 | `OBS/derived/constructed_diagram` | S1 | type | RESTRUCTURE -> `OBS/response/regime_map` | Kept as regime/boundary map (TTT, phase diagram, processing map) - clearly general across classes |
| 24 | `OBS/computation/condition_estimate` | S1 | type | MERGE -> `OBS/response/trend` | Provenance=computed; its input role is carried by the premise_for edge, not the type |
| 25 | `OBS/computation/model_prediction` | S1 | type | MERGE -> `OBS/response/trend` | Provenance=computed; validation role carried by contrasts edge + DSC/comparison. Computed TTT (Acta a29) -> regime_map |
| 26 | `OBS/computation/thermodynamic_function` | S1 | type | MERGE -> `OBS/response/trend` | Provenance=computed; if taken unmodified from a database use KNW/fact |
| 27 | `STR/phase/identity` | S1 | type | ACCEPT | Both staff |
| 28 | `STR/phase/fraction` | S1 | type | ACCEPT | Identity vs amount lead to different inferences |
| 29 | `STR/microstructure/grain_size` | S1 | type | RESTRUCTURE -> `STR/microstructure/feature_size` | Generalised: grain, particle, crystallite, pore, layer size; feature in attrs |
| 30 | `STR/microstructure/dispersion` | S1 | type | RESTRUCTURE -> `STR/microstructure/distribution` | Renamed to cover agglomeration, segregation, gradients |
| 31 | `STR/microstructure/morphology` | S1 | type | RESTRUCTURE -> `STR/microstructure/shape` | Renamed to avoid clash with OBS/morphology |
| 32 | `STR/interface/quality` | S1 | type | RESTRUCTURE -> `STR/interface` | Single leaf at L2; 'quality' is attrs |
| 33 | `PRP/mechanical/strength` | S1 | type | MERGE -> `PRP/value` | Property-family cut rejected (would explode across classes; inference after a property claim does not depend on family). attrs.property_family required |
| 34 | `PRP/mechanical/creep_rate` | S1 | type | MERGE -> `PRP/value` | As above; quantity=minimum creep rate |
| 35 | `PRP/mechanical/threshold_stress` | S1 | type | MERGE -> `PRP/value` | Critical values are property levels; attrs.quantity |
| 36 | `PRP/mechanical/failure_mode` | S1 | type | RESTRUCTURE -> `PRP/behavior_class` | Kept as categorical behaviour class (failure mode, conduction type, magnetic order) - different inference from a magnitude |
| 37 | `PRP/kinetic/transformation_rate` | S1 | type | MERGE -> `PRP/value` | property_family=kinetic |
| 38 | `PRP/mechanism_diagnostic` | S1 | type | RESTRUCTURE -> `PRP/diagnostic` | Strongly accepted: diagnostic -> lookup -> mechanism is a core, general inference pattern |
| 39 | `PRF/use_condition_capability` | S1 | type | RESTRUCTURE -> `PRF/service_capability` | Renamed |
| 40 | `MEC/process_structure_link` | S1 | type | MERGE -> `MEC/pathway` | Which spine link a MEC bridges is already given by its edge endpoints |
| 41 | `MEC/structure_property_link` | S1 | type | MERGE -> `MEC/pathway` | As above; sign becomes counteracts edge or attrs |
| 42 | `MEC/rate_controlling_step` | S1 | type | MERGE -> `MEC/identification` | Identifying the operative member of a known catalogue; same inferential shape as transformation_mode |
| 43 | `MEC/transformation_mode` | S1 | type | MERGE -> `MEC/identification` | Categorical identification against a catalogue; mode in attrs |
| 44 | `KNW/literature_precedent` | S1 | type | MERGE -> `KNW/precedent` | Same as S2 prior_result |
| 45 | `KNW/theory_model` | S1 | type | MERGE -> `KNW/model` | Model and governing equation are both computational premises |
| 46 | `KNW/diagnostic_lookup` | S1 | type | MERGE -> `KNW/lookup` | Same act as S2 reference_assignment: a known value/feature -> meaning table |
| 47 | `KNW/material_constant` | S1 | type | MERGE -> `KNW/fact` | Same as S2 material_fact |
| 48 | `DSC/trade_off` | S1 | type | RESTRUCTURE -> `DSC/design_guidance` | Renamed: the discussion-level output is a design rule/optimum; the mechanistic trade-off is MEC/tradeoff |
| 49 | `DSC/comparison_prior_work` | S1 | type | RESTRUCTURE -> `DSC/comparison` | Broadened: against prior work, model or baseline (attrs.against) |
| 50 | `DSC/model_validation` | S1 | type | MERGE -> `DSC/comparison` | Comparison with attrs.against=model and a verdict; avoids a sibling that overlaps |
| 51 | `DSC/anomaly_attribution` | S1 | type | MERGE -> `DSC/limitation` | An anomaly blamed on artefact bounds a claim (qualifies); attrs.kind=anomaly |
| 52 | `DSC/limitation` | S1 | type | ACCEPT | General |
| 53 | `DSC/outlook` | S1 | type | ACCEPT | Absorbs S2 application_outlook |
| 54 | `HYP/gap` | S2 | type | ACCEPT | Accepted, but narrowed to knowledge gaps; S2's two examples (low ZT; petroleum dependence) are HYP/need |
| 55 | `KNW/prior_result` | S2 | type | MERGE -> `KNW/precedent` | Merged with S1 literature_precedent |
| 56 | `KNW/structure_model` | S2 | type | MERGE -> `KNW/fact` | A known structure of the host is a fact used as premise; schematic figure recorded via figs |
| 57 | `KNW/governing_equation` | S2 | type | MERGE -> `KNW/model` | Equation vs named model does not change the next step (compute/fit) |
| 58 | `KNW/material_fact` | S2 | type | MERGE -> `KNW/fact` | Merged with S1 material_constant |
| 59 | `KNW/reference_assignment` | S2 | type | MERGE -> `KNW/lookup` | Merged with S1 diagnostic_lookup |
| 60 | `DES/composition/substitution` | S2 | type | RESTRUCTURE -> `DES/modification` | Broadened to any addition/substitution into a base (dopant, alloying, reinforcement, filler, co-monomer) |
| 61 | `DES/feedstock/selection` | S2 | type | MERGE -> `DES/base_system` | Merged with S1 system_choice |
| 62 | `DES/route/selection` | S2 | type | RESTRUCTURE -> `DES/route` | Flattened |
| 63 | `DES/series/variable_sweep` | S2 | type | MERGE -> `DES/variable_sweep` | Proposed by both staff |
| 64 | `DES/down_select` | S2 | type | ACCEPT | Records the OBS -> DES feedback; general to screening papers |
| 65 | `PRC/consolidation` | S2 | type | RESTRUCTURE -> `PRC/forming` | Broadened to all bulk forming (casting, sintering, AM, extrusion) |
| 66 | `PRC/synthesis` | S2 | type | ACCEPT |  |
| 67 | `PRC/deposition` | S2 | type | ACCEPT |  |
| 68 | `OBS/signal/reference_match` | S2 | type | ACCEPT | Technique-agnostic readout kind |
| 69 | `OBS/signal/peak_shift` | S2 | type | RESTRUCTURE -> `OBS/signal/feature_shift` | Renamed: edges, steps, bands also shift |
| 70 | `OBS/signal/peak_presence` | S2 | type | RESTRUCTURE -> `OBS/signal/feature_presence` | Renamed |
| 71 | `OBS/signal/peak_assignment` | S2 | type | MERGE -> `OBS/signal/feature_assignment` | Merged with S1 phase_reflections and S2 MEC/feature_attribution |
| 72 | `OBS/response/trend_with_variable` | S2 | type | RESTRUCTURE -> `OBS/response/trend` | Renamed; the workhorse |
| 73 | `OBS/response/functional_dependence` | S2 | type | MERGE -> `OBS/response/fitted_parameter` | Merged with S1 fitted_parameter/rate_vs_stress |
| 74 | `OBS/response/derived_quantity` | S2 | type | REJECT (migrate -> `OBS/response/trend`) | Provenance is orthogonal to readout kind: new OBS field provenance=derived + rel derives. Migrate to the readout kind actually read (usually trend) |
| 75 | `OBS/response/component_partition` | S2 | type | ACCEPT | General (thermal/electrical conductivity, strengthening contributions, impedance, capacity) |
| 76 | `OBS/response/event_temperatures` | S2 | type | MERGE -> `OBS/response/characteristic_value` | A special case of reading a defined point |
| 77 | `OBS/response/standard_test_values` | S2 | type | MERGE -> `OBS/response/characteristic_value` | The PRF route follows from the claim node, not the readout |
| 78 | `OBS/appearance/visual_quality` | S2 | type | MERGE -> `OBS/morphology/appearance` | Photograph vs micrograph is modality; the readout is qualitative appearance |
| 79 | `STR/phase/identity` | S2 | type | ACCEPT |  |
| 80 | `STR/lattice/parameter_change` | S2 | type | RESTRUCTURE -> `STR/phase/lattice` | Moved under phase; 'change' is attrs.direction |
| 81 | `STR/defect/point_defect` | S2 | type | RESTRUCTURE -> `STR/defect/point` | Renamed; point vs extended split accepted (carrier/diffusion vs mechanical/phonon arguments) |
| 82 | `STR/defect/extended_defect` | S2 | type | RESTRUCTURE -> `STR/defect/extended` | Renamed |
| 83 | `STR/chemical/group_conversion` | S2 | type | MERGE -> `STR/chemistry/bonding` | Conversion vs full structure is scope (attrs.scope), same next inference |
| 84 | `STR/chemical/molecular_structure` | S2 | type | MERGE -> `STR/chemistry/bonding` | As above |
| 85 | `PRP/carrier_parameter` | S2 | type | RESTRUCTURE -> `PRP/descriptor` | Generalised to any intermediate microscopic descriptor, as S2 suggested |
| 86 | `PRP/component_partition` | S2 | type | RESTRUCTURE -> `PRP/partition` | Renamed |
| 87 | `PRP/thermal_stability` | S2 | type | MERGE -> `PRP/value` | property_family=thermal; stability vs transition is attrs.quantity |
| 88 | `PRP/thermal_transition` | S2 | type | MERGE -> `PRP/value` | As above |
| 89 | `PRF/figure_of_merit` | S2 | type | ACCEPT |  |
| 90 | `PRF/qualification_test` | S2 | type | RESTRUCTURE -> `PRF/qualification` | Renamed |
| 91 | `PRF/baseline_equivalence` | S2 | type | REJECT (migrate -> `PRF/qualification`) | Outcome vs incumbent is an attribute (attrs.baseline, attrs.outcome=equivalent) + contrasts edge; the follow-up comes from HYP/need, not from the type |
| 92 | `MEC/defect_chemistry` | S2 | type | MERGE -> `MEC/pathway` | Physical mechanism class is content: attrs.mechanism_class |
| 93 | `MEC/scattering` | S2 | type | MERGE -> `MEC/pathway` | As above. Scattering-regime identification from an exponent (Ceramics n18) -> MEC/identification |
| 94 | `MEC/electronic_structure` | S2 | type | MERGE -> `MEC/pathway` | As above |
| 95 | `MEC/tradeoff_balance` | S2 | type | RESTRUCTURE -> `MEC/tradeoff` | Accepted, renamed; general (strength-ductility, PF-kappa, capacity-rate) |
| 96 | `MEC/composition_attribution` | S2 | type | REJECT (migrate -> `MEC/pathway`) | Right instinct, wrong device: weakness of an explanation is attrs.basis=attributed on MEC/pathway, so it can be filtered without a parallel type |
| 97 | `MEC/feature_attribution` | S2 | type | MERGE -> `OBS/signal/feature_assignment` | As S2 suggested: assigning a DTG step is the same act as assigning a peak (with KNW/lookup premise) |
| 98 | `DSC/conclusion` | S2 | type | ACCEPT |  |
| 99 | `DSC/application_outlook` | S2 | type | MERGE -> `DSC/outlook` | attrs.kind=application |
| 100 | `reduces_to` | S1 | rel | MERGE -> `derives` | Same relation as S2 'derives': dst OBS is computed from src OBS and is not independent evidence |
| 101 | `parameterizes` | S1 | rel | MERGE -> `premise_for` | premise_for broadened to in-paper inputs; source type already tells KNW from in-paper data |
| 102 | `qualifies` | S1 | rel | ACCEPT | Needed for limitations/anomalies; rules_out too strong, contrasts symmetric |
| 103 | `derives` | S2 | rel | ACCEPT | Broadened to all data reduction; key for evidential honesty |
| 104 | `counteracts` | S2 | rel | ACCEPT | Negative-sign contribution needed for trade-off graphs |
| 105 | `compare_panels_across_conditions` | S1 | mm_op | MERGE -> `compare_across_conditions` | Panels, frames and curves differing in one condition: one op |
| 106 | `assess_spatial_distribution` | S1 | mm_op | ACCEPT | General (micrographs, element maps) |
| 107 | `zoom_into_local_feature` | S1 | mm_op | RESTRUCTURE -> `inspect_local_feature` | Renamed |
| 108 | `measure_feature_size_distribution` | S1 | mm_op | MERGE -> `measure_feature_metric` | Size, count, density one op |
| 109 | `recognize_morphological_signature` | S1 | mm_op | MERGE -> `recognize_signature` | Merged with curve-shape template matching, as S1 suggested |
| 110 | `compare_frames_across_time` | S1 | mm_op | MERGE -> `compare_across_conditions` | Time/state is the varied condition; same-specimen is attrs |
| 111 | `count_features_per_area` | S1 | mm_op | MERGE -> `measure_feature_metric` |  |
| 112 | `read_trend_across_series` | S1 | mm_op | MERGE -> `read_trend` |  |
| 113 | `contrast_coplotted_quantities` | S1 | mm_op | MERGE -> `compare_coplotted_quantities` | Merged with partition_total_into_components |
| 114 | `compare_curves_across_conditions` | S1 | mm_op | MERGE -> `compare_across_conditions` | Use read_trend when the series is ordered and a single quantity is read |
| 115 | `extract_characteristic_point_from_curve` | S1 | mm_op | MERGE -> `read_characteristic_point` |  |
| 116 | `extract_slope_from_linearized_plot` | S1 | mm_op | MERGE -> `extract_slope` |  |
| 117 | `collapse_curves_by_normalization` | S1 | mm_op | RESTRUCTURE -> `collapse_by_normalization` | Accepted, renamed; the merge of curves is itself the evidence |
| 118 | `read_threshold_crossing` | S1 | mm_op | MERGE -> `read_characteristic_point` |  |
| 119 | `index_peaks_to_phase` | S1 | mm_op | MERGE -> `assign_features` |  |
| 120 | `match_pattern_to_simulated_reference` | S1 | mm_op | MERGE -> `match_to_reference` | Reference origin (simulated/measured/database) is attrs |
| 121 | `subtract_reference_pattern` | S1 | mm_op | RESTRUCTURE -> `subtract_reference` | Renamed; includes background/baseline subtraction |
| 122 | `integrate_peak_areas_to_fraction` | S1 | mm_op | RESTRUCTURE -> `quantify_from_intensity` | Generalised to widths and other amounts |
| 123 | `resample_curves_at_isolevels` | S1 | mm_op | MERGE -> `replot_derived_series` |  |
| 124 | `read_curve_shape_against_template` | S1 | mm_op | MERGE -> `recognize_signature` |  |
| 125 | `overlay_model_on_data` | S1 | mm_op | ACCEPT | Use fit_model when the overlay is used to extract parameters |
| 126 | `aggregate_snapshots_into_series` | S1 | mm_op | MERGE -> `replot_derived_series` |  |
| 127 | `fit_analytic_expression_to_curve` | S1 | mm_op | RESTRUCTURE -> `fit_model` | Renamed |
| 128 | `flag_outlier_against_trend` | S1 | mm_op | RESTRUCTURE -> `flag_outlier` | Renamed |
| 129 | `match_pattern_to_reference` | S2 | mm_op | MERGE -> `match_to_reference` |  |
| 130 | `track_peak_shift_across_series` | S2 | mm_op | MERGE -> `track_feature_across_series` | Shift vs presence is carried by the node type |
| 131 | `track_peak_across_stages` | S2 | mm_op | MERGE -> `track_feature_across_series` |  |
| 132 | `assign_peaks_to_structure_sites` | S2 | mm_op | MERGE -> `assign_features` |  |
| 133 | `rank_curves_across_series` | S2 | mm_op | MERGE -> `read_trend` |  |
| 134 | `extract_scaling_exponent` | S2 | mm_op | MERGE -> `extract_slope` |  |
| 135 | `compare_against_literature_points` | S2 | mm_op | RESTRUCTURE -> `compare_with_literature` | Renamed, includes tabulated incumbents |
| 136 | `partition_total_into_components` | S2 | mm_op | MERGE -> `compare_coplotted_quantities` |  |
| 137 | `read_value_at_condition` | S2 | mm_op | MERGE -> `read_characteristic_point` |  |
| 138 | `segment_steps_via_derivative` | S2 | mm_op | MERGE -> `read_characteristic_point` | Derivative-assisted reading is attrs |
| 139 | `locate_transition_step` | S2 | mm_op | MERGE -> `read_characteristic_point` |  |
| 140 | `inspect_visual_uniformity` | S2 | mm_op | MERGE -> `compare_across_conditions` | Judging panels of samples that differ in one variable; single-sample uniformity -> assess_spatial_distribution |
| 141 | `compare_panels_across_conditions` | S2 | mm_op | MERGE -> `compare_across_conditions` | Same as S1 |
| 142 | `cross_check_figures (comment)` | S2 | mm_op | RESTRUCTURE -> `cross_check_consistency` | Admitted as check-family op for when the PAPER cross-checks; staff audit findings go to image_support, not to mm_ops |
| 143 | `image_support node field (S1 comment; S2 image_note attrs)` | S1+S2 | field | ACCEPT | Values shown | partial | not_shown | contradicts; see PROTOCOL.md |
| 144 | `OBS L2 = technique family (S1) vs readout feature (S2)` | S1 vs S2 | restructure | RESTRUCTURE -> `OBS/{signal,response,morphology}` | S2 cut adopted; technique families repeat modality/attrs. S1's image readouts folded into OBS/morphology |
| 145 | `(judge) provenance field on OBS` | judge | field | RESTRUCTURE -> `provenance` | measured | derived | computed; replaces OBS/derived/* and OBS/computation/* |
| 146 | `(judge) rel supports` | judge | rel | RESTRUCTURE -> `supports` | Staff used causes/evidences/motivates for claim->claim and claim->DSC reasoning (Acta a22->a20, a25->a26; Ceramics n10->n12, n32->n34; JMA n17->n35) |
| 147 | `(judge) PRC/treatment, STR/chemistry/composition` | judge | type | RESTRUCTURE -> `provisional` | Added provisionally to close sibling sets; must be confirmed by r02 evidence or removed |

## Poor-fit rulings

| node | staff type | ruling |
|---|---|---|
| JMA n7 grain size from F1 | OBS/imaging/feature_size (poor) | The type is right: `OBS/morphology/feature_metric`. The poor fit is evidential, not taxonomic, so record `image_support: not_shown`. |
| JMA n24 agglomeration/porosity/residual stress limit UTS | MEC/structure_property_link (poor) | `MEC/pathway`, attrs.basis=attributed, attrs.source=matmech. Edge n24 →`counteracts`→ n17. |
| Acta a21 single-shot BF frames, lens-shaped grains, nuclei per grain | OBS/imaging/morphology_change (poor) | Split into two nodes. (1) `OBS/morphology/appearance` (lens shape; mm_op recognize_signature; image_support partial). (2) `OBS/morphology/feature_metric` (nuclei per grain; →premise_for→ a24 with measure_feature_metric). |
| Ceramics n29 stacking faults eliminated | STR/defect/extended_defect (poor) | Type correct: `STR/defect/extended`. No direct observation, so attrs.basis=inferred (via κl + ref [10]). Its incoming edge from n28 should be `supports`, not `evidences`, because κl does not show defects. |
| POC n20 TGA steps assigned to urethane cleavage etc. | MEC/feature_attribution (poor) | `OBS/signal/feature_assignment` with KNW/lookup (ref [38]) as premise_for. mm_op on n19→n20: `assign_features` (the derivative-based step reading is attrs on read_characteristic_point). |

## Where the hierarchy is and is not converging

**Converging:**
- **OBS by readout feature.** Both staff independently produced readout-level leaves once technique was removed. The 13 OBS leaves cover all 43 r01 OBS nodes across four materials classes.
- **KNW by use.** The merges were clean: diagnostic lookup = spectral reference table.
- **DES** (base vs modification vs route vs method, plus sweep and down-select) and **HYP** (gap / need / hypothesis) cut cleanly.
- **mm_ops.** 37 names collapsed to 21 with no leftover distinctions. The families (read / compare / match / quantify / transform / check) held for every r01 edge.

**Not converging:**
- **STR** is the least tested. Texture/orientation, porosity/density, composition/valence and ordering/crystallinity (polymers) appear only as attrs or provisional leaves. Four papers cannot tell whether they deserve leaves.
- **PRC** has a thin evidence base. Treatment is unobserved, and the synthesis/forming boundary for reactive consolidation (reactive sintering, in-situ composites) is untested.
- **PRP/PRF boundary.** ZT and coating ratings sit on either side of it by convention rather than by a crisp test.
- **MEC/identification vs MEC/pathway** needs cases where a pathway is argued against named alternatives without a diagnostic.
- **Saturation:** not reached. Coverage of r01 nodes by v00 was ~0 (v00 had only L1 types), and v01 adds 14.5 leaves per paper. The stopping criterion (<0.1 leaf per paper, ≥95% coverage) cannot be approached before r03–r04. r02 is the first real test: if coverage by v01 is <85%, the role-based PRP/MEC flattening or the OBS families are wrong.

## Guidance to staff for r02

1. **Use v01 types even when imperfect; mark `fit: poor`.** Propose a new leaf only if you can name the different inference that follows and show it in two papers or two materials classes. Before proposing, first check whether the distinction is technique, material, property family, mechanism class, direction or provenance. All of these are attrs or fields.
2. **OBS nodes need `modality` + `provenance` + (if figs) `image_support`.** Set modality from the panel actually read: 1D XRD/radial profiles are `diffraction_pattern`, bar charts are `xy_curve`. Split nodes that read two panel kinds. Give derived OBS an incoming `derives` edge from their inputs.
3. **Keep three rels apart.** `evidences` is OBS→claim only. `causes` is physics in the material only (processing→structure→property→performance). `supports` covers claim→claim and claim→DSC reasoning. Never link DES directly to PRP with `causes`.
4. **Every edge whose source is an OBS with figs carries an mm_op** (r01: 54/60 did; the 6 gaps were 5 `derives` edges and 1 `counteracts` edge in the Ceramics graph — arithmetic combination of plotted series is `replot_derived_series`, reading the sign of a counteracting term is `compare_coplotted_quantities`), including `derives`, `premise_for` and `contrasts` edges. Pick ops from the 21. A missing op is a proposal only if none of the six families fits.
5. **Image audit is part of the job.** When the figure disagrees with the text, keep the paper's claim as the node, set `image_support: contradicts` or `partial`, and describe it in `attrs.image_note`. When the figure shows something the text omits (liquid hump, crossing creep lines, curve shoulders), add a `text_silent` OBS node. Do not silently "correct" the paper.
6. **Cite packet figure ids (F1…), not paper figure numbers.** They differ in at least one packet.
7. **Stay on packet text.** MatMech-extraction content not present in the packet text gets `attrs.source: "matmech"`.
8. **Targeted evidence requested:** heat-treatment/ageing papers (PRC/treatment); oxidation-state or segregation claims (STR/chemistry/composition); texture and porosity (still attrs); computation-first papers (DFT/MD) to stress-test `provenance: computed`; electrochemical, biomedical and optical-property papers to stress-test the flat PRP.

## Open questions (top 3)

1. **Flat PRP and MEC.** Is a role-based PRP (value / behavior_class / descriptor / diagnostic / partition) plus a required property_family attr enough for functional, electrochemical and biological papers? Is a role-based MEC (pathway / identification / tradeoff) plus mechanism_class enough? Or do those papers need family-level leaves?
2. **OBS families under computation-heavy and in-situ papers.** Do signal / response / morphology plus `provenance` carry DFT band structures, MD snapshots and operando series? Or does "computed" need its own readout kinds (e.g. energy landscape, simulated field)?
3. **STR resolution.** Should texture/orientation, porosity/density and composition/valence become leaves? Will the provisional `PRC/treatment` and `STR/chemistry/composition` be confirmed?
