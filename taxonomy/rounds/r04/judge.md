# Round r04: judge rulings, merge phase (v03 → v04, final)

**Inputs:** PROTOCOL.md, vocab/v03.json, rounds/r03/judge.md (merge candidates C1, C2, Q1, Q2, K1, P1, P2, O1, O2, F1, S1), proposals_S1–S8.json and metrics.jsonl. r04 covered 32 papers, 1129 nodes and 1418 edges. Coverage by v03 was 100%, with 0 validation problems and 426/426 figure edges carrying an mm_op. Staff proposed **0** new types, rels, mm_ops or modalities.

**Usage base:** all 60 graphs in rounds/r01–r04 (2109 nodes, 2625 edges), after the v01→v03 rename chains. Scripts are in the scratchpad `r04_judge/`:
- `usage_v04.py before` gives the v03 state;
- `usage_v04.py after` gives the state after the v04 renames and conditional renames;
- `build_v04.py` writes vocab/v04.json;
- `hierarchy.py` writes vocab/HIERARCHY.md.

Counts are `[nodes or edges, papers]`.

**Result:** v04 is **final**. It has:
- **81 type entries:** 10 L1 + 7 L2 + **64 leaves** (was 65), max depth 3;
- **22 mm_ops** (was 27) in **5 families** (was 6);
- **14 rels** (1 redefined);
- **13 modalities**.

**Merged away:** 7 entries (1 type and 6 mm_ops), plus the `transform` family. One new op name (`convert_to_quantity`) absorbs three ops. Two ops were narrowed by conditional migration.

Growth has stopped. r04 added 0 leaves per paper (below 0.1) and coverage by v03 was 100% (above 95%).

## 1. Rulings on r04 proposals

| # | proposal | staff | ruling | reason |
|---|---|---|---|---|
| 1 | **C1** track_feature_across_series (stacked-trace use) → compare_across_conditions; keep track_ for object identity in frames | S1–S8 (unanimous) | **ACCEPT** (narrowing + conditional migration) | Every stacked-trace edge put forward (Acta p10, AFM r12, JAC s1/s3/s6, JMA b11, nl201541y a19, s41563-024 d21/d23, POC p8/q9) already has a src OBS/signal type that says one feature moved or appeared. The op adds nothing, and S7 could not separate d11 from d21. Object tracking keeps its identity/aliasing audit (AdvMat 201706311 o22: order of layer locking). Rule: src OBS/signal/* → compare_across_conditions (25 edges). The two r03 frame-tracking edges that ruling #9 meant for track_ were never migrated (AFM 201901327 o20→s8, AEM 201902373 o26→e6); they now move to track_. Result [4, 3] across STEM frames, AIMD snapshots and loading photographs, which justifies the op as general. |
| 2 | **Q1** quantify_from_intensity + quantify_from_position + convert_via_calibration → convert_to_quantity (`via`) | S1, S2, S4, S7, S8 | **MERGE** | `via` was filled without judgement on every r04 edge (POC p8→p9 position; RM c15 intensity; Bioactive o3→o4 ROI intensity; JAC s4→s5). The three-way split also left gaps: C = I·dt/dV (s42114-021 k20→k17, AEM m26o→m27), two-point Arrhenius (s42114-020 j20→j24) and a Rothwarf–Taylor inversion (s41563-023 c24→c25). These are covered by via = known_relation \| model. Each via's audit sentence stays in the definition. The calibration audit changed spine support in r03 and is kept verbatim. |
| 3 | **Q2** extract_slope → fit_model (`form`) | S1, S3, S4, S5, S6, S7, S8 | **MERGE** | Staff split identical acts across two labels: AdvMat o13→o14, RM r28 vs r27, POC Tafel p17→p18. The failure mode is the same (fitted window, constraints, number of points). The diagnostic chain stays visible through PRP/diagnostic → KNW/lookup → MEC/identification (rs r29→r30→r34, nl a32→a33→a36, JAC j14→j21→j15). It does not need the op name. |
| 4 | **P1** PRP/partition → PRP/value (`aspect = partition`) | S1, S2, S3, S5, S6, S7, S8; S4 against | **MERGE** | [4, 4]. In r04, partition claims were either the same fact as a MEC/identification (RM r35 = r34), carried by MEC/pathway (Acta 2012 load partitioning; AdvMat o18), or carried by the OBS leaf (#5). S4's case (JAC j16 undercuts the grain-growth branch) is carried by j16's `qualifies` edge to j12, not by its type, so `aspect = partition` loses nothing. |
| 5 | **O2** OBS/response/component_partition → OBS/response/trend | S1–S6; S7, S8 against | **REJECT** (keep) | [7, 6]. S7 (s41563-023 c34/c35: Drude term + residual at fixed T) and S8 (RM r32: capacitive share of one CV at one sweep rate) show decompositions **with no varied variable**, so "trend" would mistype them. Next inference: which term dominates → PRP/value (aspect=partition) or MEC. After #4 this leaf is the only visible carrier of the partition reading. The definition now says "at one condition or across conditions". |
| 6 | **O1** OBS/response/regime_map → trend | S1, S2, S4, S5, S6, S8; S3, S7 against (S3 split) | **REJECT merge; ACCEPT S3 split** | Now [3, 3]: r01 TTT, s41563-024 d38 (exchange-pathway ternary map), AdvMat o31 (bistability window). The reading is "which state exists at this condition", which licenses a bistability or exchange-pathway claim that a trend cannot. Split rule: contours of ONE response over two variables → trend (`dimension = 2D`, AdvMat o6). Boundaries between states, including 1-D windows → regime_map. S7's `read_regime_boundaries` op is not created: locating a sample relative to a boundary is added to read_characteristic_point. |
| 7 | **K1** flag_outlier → cross_check_consistency | S1–S8 | **MERGE** (`aspect = outlier`) | [2, 2]. The second use (nl a35) is a set-aside discrepancy, which cross_check already does. S7's own bar was ≥3 uses, and it was not met. |
| 8 | **K1** subtract_reference → replot_derived_series | S1–S4, S7, S8 | **MERGE** | [1, 1]. Subtraction was a step inside another act in r04 (T#t25 background, RM c26→c27 κ_L = κ − LσT, s41563-023 c34 residual). On `derives` edges it is replot_derived_series. When the residual is read against a model, it is overlay_model_on_data. |
| 9 | **K1** prune collapse_by_normalization | S1, S3 prune; S5 keep | **REJECT** prune (keep) | Now [5, 3] (r01 creep effective-stress collapse, JMA 2019 b21 grain-size collapse with adj. R² 0.974, s41563-023 c25). The paper's inference rests on the merge of the curves, and the op has its own audit (high-leverage point). read_trend would hide that. |
| 10 | **P2** keep PRP/diagnostic | S2, S4, S7, S8 keep; S5 abstain | **ACCEPT** (keep) | [7, 7]. Four r04 papers run the full diagnostic → lookup → identification chain. The leaf is the only thing that marks the role difference. S2's Tafel slope used as a ranking went to PRP/value, which shows the rule can be applied. Rule written: diagnostic only if KNW/lookup or KNW/model → MEC/identification follows. |
| 11 | **F1** PRF/figure_of_merit vs PRF/qualification; S1 broaden FOM; S8 rating rule | S1, S2, S8 | **ACCEPT** (keep both, sharpen) | [6, 6] and [6, 5]. S2 separated them cleanly (AEM m35 vs AFM n22). FOM also covers per-mass/volume/cost normalisations used as the field's ranking convention (S1 k18 specific capacitance). Qualification applies only when a threshold, spec or benchmark condition is applied (S8). A normalised efficiency used as a step toward another claim (S8 PEF) is a derived OBS. The next inferences differ: FOM → decompose into constituent properties or trade-off; qualification → application claim. |
| 12 | match_to_reference with a model reference → overlay_model_on_data | S7 | **RESTRUCTURE** (boundary + migration) | S7 got the same reading under two ops (nl a12 overlay vs a21 match). The split now follows reference provenance: empirical reference → match_to_reference; model, fit or simulation output (Rietveld, theory curve, constructed tiling) → overlay_model_on_data. Staff fill this reliably. 3 edges migrated (nmat2713 b23, nl a21, s41563-024 d12). Result: match_to_reference [14, 10] → [11, 7], overlay [30, 12] → [33, 13]. |
| 13 | overlay_model_on_data covers paired side-by-side panels; circularity audit | S6 | **ACCEPT** | All 6 of S6's model-vs-data edges read paired panels. The circularity audit (a parameter tuned on the same data) changed spine support in Nano nl101246z (l1 qualifies n8). |
| 14 | `qualifies` may carry outright contradiction | S1 | **ACCEPT** (redefine) | There are three r04 refutations (s42114-021 k23→k24, k16→k19; s42114-020 j34→j33). The conflict strength sits on the target's image_support. A `contradicts` rel would duplicate it. |
| 15 | Unopened figures: figs=[] + attrs.fig_ref; image_support never from captions | S1, S2, S3, S5, S6 | **ACCEPT** (node-field rule) | S5's `attrs.image_checked=false` nodes are to be normalised to `figs=[]` + `attrs.fig_ref`. Their image_support was judged from the caption and must be dropped. |
| 16 | STR/chemistry/bonding + intermolecular packing | S2 | **ACCEPT** (broaden) | Packing → exciton/CT coupling → optical shift is bonding's own next step (AFM r14, r15). |
| 17 | MEC/pathway + in-vivo biodistribution (mechanism_class = pharmacokinetic) | S2 | **ACCEPT** | Extends r03 #18. Where the material goes is neither an endpoint nor a material property (AFM r24). |
| 18 | compare_coplotted_quantities across figures sharing an axis; non-overlap is a result | S2 | **ACCEPT** | AFM t13→t14. The audit adds same medium/state and same scale. |
| 19 | Review papers: attrs.reproduced_from | S2 | **ACCEPT** (provenance note) | No new provenance value. |
| 20 | PRC/deposition + conversion coatings (aspect = conversion) | S3 | **ACCEPT** | Bioactive s7, s8. |
| 21 | Metamaterial "self-locking" as PRP/behavior_class (object = cell) | S3 | **ACCEPT** (no change) | Written into the behavior_class definition as "kinematic behaviour of an architected cell". |
| 22 | quantify_from_intensity + image-ROI intensity | S4 | **ACCEPT** as convert_to_quantity via = intensity | Absorbed by #2. |
| 23 | register_colocated_views allowed on derives (colocalisation coefficient, channel ratio) | S4 | **ACCEPT** | This is the one exception to the r03 rule "derives ops are quantify acts". The act that can fail is registration (Bioactive o9→o10, PVA r2). |
| 24 | property_family photochemical | S4 | **ACCEPT** (attr value) | Light-triggered generation or release (Bioactive b10). It recurs in PDT, NO release and photo-uncaging. |
| 25 | Defect concentration: PRP/descriptor → STR/defect/point (aspect = concentration) | S4 | **ACCEPT** | JAC j11 matched both definitions word for word. The next inference is point-defect reasoning. |
| 26 | MEC/identification + decoupling experiments | S5 | **ACCEPT** (broaden) | JMA b20. A candidate isolated by experiment has the same consequence (alternatives ruled out) as one found by lookup. |
| 27 | DES/route: schedule designed to isolate a process (purpose = decouple) | S5 | **ACCEPT** | JMA b7. |
| 28 | In-silico pressure: to find the kept phase = treatment; to read a property = stimulus | S5 | **ACCEPT** | JAC a9, a18. |
| 29 | read_trend vs read_characteristic_point: crossings | S5 | **ACCEPT** | A crossing that yields a value → characteristic point. read_trend keeps only direction and change of ranking. |
| 30 | STR/microstructure/damage + binder dissolution | S6 | **ACCEPT** | Matchar 2007 w9. The next step is grain detachment / failure mode, which is damage's inference. |
| 31 | STR/microstructure/distribution + coverage and filler connectivity | S6 | **ACCEPT** | JMST j8, j9. It gives filler connectivity a home, so it does not drift into porosity. |
| 32 | Tribology → property_family surface; wear mode → behavior_class | S6 | **ACCEPT** | Matchar 2018 t12, t13. |
| 33 | Spine: PRP of tool/assembly upstream of STR in tool papers | S6 | **ACCEPT** (restricted) | Only with attrs.object = assembly and when the process acts through that property (Nano nl101246z). |
| 34 | OBS/signal/reference_match + response curves vs model/reference trace | S7 | **ACCEPT** (broaden) | nl a12/a21 and s41563-023 c20/c33 were poor fits under trend. The whole-trace coincidence reading is the same act for any trace. |
| 35 | Withheld: Burgers-circuit op, pairing-symmetry leaf, read_regime_boundaries | S7 | **REJECT** (one use each) | Existing entries cover them: replot_derived_series + measure_feature_metric (nmat2713 b12→b18); PRP/behavior_class (c21); read_characteristic_point (#6). |
| 36 | PRC/stimulus only when the exposure produces an argued state; a service test goes in PRF attrs.condition | S8 | **ACCEPT** (usage note) | POC p32, q30, q33; RM r38. |
| 37 | Do not seed labels from the MatMech summary block | S8, S3, S4 | **ACCEPT** (process rule) | See §5. |

Counts: ACCEPT 28 (1, 6, 10, 11, 13–34, 36, 37; #1 as narrowing, #6 as split) · MERGE 5 (2, 3, 4, 7, 8) · RESTRUCTURE 1 (12) · REJECT 3 (5, 9, 35).

## 2. Staff "indistinguishable" pairs: resolution

Each pair was either merged, or given a decision rule on both sides (the rules are in `rule` of each leaf or op in v04.json).

| pair | reported by (node refs) | resolution | decision rule |
|---|---|---|---|
| track_feature_across_series / compare_across_conditions | S7 (nl a19, s41563-024 d11/d21/d23), S1–S8 via C1 | **merged** for stacked traces | track only when object identity through frames licenses the inference |
| extract_slope / fit_model | S3 (AdvMat o14), S8 (RM r27/r28, POC p17) | **merged** | — |
| overlay_model_on_data / match_to_reference | S7 (nl a12/a21, d12/d14, b23) | **rule + migration** | model/fit/simulation reference → overlay; empirical reference → match |
| OBS/signal/reference_match / OBS/response/trend | S7 (a12, a21, c20, c33) | **rule** | a whole trace judged against a reference or model trace → reference_match, whatever the trace kind |
| OBS/response/trend / characteristic_value | S1 (n35, j34), S3 (z17, z18, s15, s16, s18), S6 (o7, o9) | **rule** (not merged: trend licenses attribution to the varied variable; a value feeds comparison, derivation or qualification) | direction or ranking across ≥2 conditions argued → trend (aspect=ranking for categorical groups); named level read → characteristic_value |
| feature_presence / feature_quantification | S2 (t9, t15, t21, t25, m7), S8 (q9) | **rule** | complete appear/disappear or a yes/no reading → presence; partial change, or a residual/degree argued → quantification |
| feature_presence / feature_assignment | S6 (o2, o10), S7 (d11, d28) | **rule** | indexing a set of features → assignment; one specific expected feature appears or is absent → presence |
| OBS/signal/feature_quantification / OBS/response/trend | S5 (b12, b14, b15, b41) | **rule** | read from the raw pattern or pole figure → signal; read from a plotted quantity vs variable → response, with a derives edge from the pattern node |
| read_trend / read_characteristic_point | S5 (a10→a11, a10→a12) | **rule** | a crossing that yields a value → characteristic point |
| OBS/morphology/appearance / distribution | S4 (o3, o5, o9) | **rule** | what it looks like, or whether a labelled signal is there → appearance; where it is → distribution |
| PRP/value / PRF/figure_of_merit / PRF/qualification | S1 (k18, n34), S8 (q20, p30, p31) | **rule** | external threshold/spec/benchmark → qualification; composite or ranking-convention normalised metric used to rank → FOM; argued from structure as a level or trend → value |
| STR/chemistry/composition / STR/phase/fraction | S1 (k14, j13) | **rule** | amount of a crystalline phase → fraction; loss or gain of an amorphous or organic constituent, or element content → composition (attrs.scope) |
| STR/chemistry/composition / STR/phase/identity | S3 (s11, s12, z24) | **rule** | a phase named only from stoichiometry → composition (attrs.phase_named_from=stoichiometry); identity needs structure-sensitive evidence |
| STR/microstructure/distribution / shape | S1 (j15, k10) | **rule** | coverage, or where a constituent lies → distribution; geometry of a built unit (core-shell, sheath) → shape |
| STR/microstructure/shape / porosity | S2 (n15, m17, m19) | **rule** | a single designed cavity or shell → shape; void fraction, SSA or connectivity → porosity |
| STR/microstructure/porosity / distribution | S4 (p6, p7) | **rule** | type what the next node uses: void amount → porosity; location of the constituent → distribution |
| STR/microstructure/distribution / STR/interface | S8 (r13, r14) | **rule** | contact state (bonding, charge transfer) → interface; dispersion over the support → distribution |
| PRP/descriptor / STR/defect/point | S4 (j11) | **rule** (definition moved) | defect concentration → defect/point |
| MEC/identification / MEC/pathway | S5 (b20, b23) | **rule** (identification broadened) | a member picked from a known catalogue, by lookup or by isolation experiment → identification; a pathway built from evidence → pathway |
| MEC/pathway / PRF/service_capability | S2 (r24) | **rule** | biodistribution or host biomarkers that explain an endpoint → pathway |
| PRP/value (kinetic) / PRF/service_capability | S4 (p10, p15) | **rule** (existing) | a measured rate vs design variable → value; argued suitability at the use condition → service_capability |
| PRP/behavior_class / PRF/service_capability | S6 (w15, w17) | **rule** | how it fails → behavior_class; ranking or passing under a (simulated) service condition → service_capability |
| DES/base_system / DES/modification | S4 (b3, b4, h3, h4) | **rule** | modification only when added to or substituted into a named base; whole-molecule designs → base_system |
| DES/route / method / variable_sweep | S5 (b7) | **rule** | a processing schedule that isolates a process → route (purpose=decouple) |
| PRC/treatment / PRC/stimulus | S5 (a9, a18) | **rule** | in silico: find the kept phase → treatment; read a property → stimulus |
| PRC/stimulus / PRF attrs.condition | S8 (p32, q30, q33, r38) | **rule** | a stimulus node only if the exposure produces an argued state |

## 3. Merge table: before → after (60 papers)

"Before" means after the v01–v03 renames. "After" means after the v04 renames and conditional renames.

| kind | before | after | change |
|---|---|---|---|
| type | PRP/partition [4, 4] + PRP/value [133, 56] | PRP/value [137, 57] | merged (aspect=partition) |
| op | quantify_from_intensity [15, 11] + quantify_from_position [4, 4] + convert_via_calibration [5, 2] | convert_to_quantity [24, 17] | merged (via) |
| op | extract_slope [16, 13] + fit_model [15, 10] | fit_model [31, 20] | merged (form) |
| op | flag_outlier [2, 2] + cross_check_consistency [26, 17] | cross_check_consistency [28, 19] | merged (aspect=outlier) |
| op | subtract_reference [1, 1] + replot_derived_series [45, 18] | replot_derived_series [46, 18] | merged |
| op | track_feature_across_series [27, 15] | [4, 3] | narrowed: 25 edges → compare_across_conditions, 2 r03 edges ← compare |
| op | compare_across_conditions [247, 56] | [270, 57] | +25 −2 |
| op | match_to_reference [14, 10] | [11, 7] | 3 model-reference edges → overlay |
| op | overlay_model_on_data [30, 12] | [33, 13] | +3 |
| family | transform (replot_derived_series, subtract_reference) | folded into quantify | family count 6 → 5 |
| kept | OBS/response/component_partition [7, 6], OBS/response/regime_map [3, 3], PRP/diagnostic [7, 7], PRF/figure_of_merit [6, 6], PRF/qualification [6, 5], collapse_by_normalization [5, 3] | unchanged | merge rejected: the next inference differs |

**Low-use entries kept as clearly general** (fewer than 5 papers):
- PRC/joining [2, 2]: every joint paper;
- STR/microstructure/damage [3, 2]: fracture, thermal shock, battery cracking, weathering;
- STR/microstructure/orientation [4, 3]: texture;
- STR/defect/extended [5, 3]: dislocations and faults;
- read_distribution_statistics [9, 3];
- track_feature_across_series [4, 3];
- modality dispersion_diagram [1, 1]: band and phonon dispersions are standard in computational papers;
- modality volume_render [2, 2].

Their low counts reflect the corpus mix, with few metallurgy and fracture papers, not redundancy. No two staff confused any of them.

**Graph migration (pending, for the orchestrator).** The graphs themselves were not rewritten. To bring them to v04, apply:
1. `renames` together with `rename_attrs`;
2. the three `conditional_renames`;
3. the r03 node migrations that were never applied: Biomaterials 2013 d13 → MEC/pathway, d14 → PRF/service_capability, d23 → OBS/response/distribution; AdvMat 200903105 a31→a32 op → measure_feature_metric;
4. the r01 legacy node porgcoat.2015.05.014 n20 (MEC/feature_attribution → OBS/signal/feature_assignment), which has no modality and needs `spectrum` or `xy_curve`.

## 4. Final design principles

1. **A type exists only if it changes the next inference.** Everything else is an attribute: aspect, via, form, proxy, object, property_family. This rule decided every merge above. PRP/partition went to an aspect because nothing downstream reads it. component_partition and regime_map stayed because their consequences (dominant term; which state exists) cannot be read from a trend.
2. **Types name argument roles, ops name figure acts.** Technique and material never become types. Figure form, data origin and figure fidelity are node fields (modality, provenance, image_support). An op carries the failure modes of reading the figure; what follows is carried by the dst type, not repeated in the op name. That is why extract_slope, the spectral use of track_ and the Q1 triple could merge.
3. **A fixed skeleton, grown by boundary rules.** HYP → DES → PRC → STR → PRP → PRF → DSC, with OBS/KNW as evidence and premises and MEC as the bridge. This held for 60 papers across 15 journals without a new L1 or L2 after r01. From r03 onward, every poor fit was solved by a boundary sentence or a decision rule between siblings, not by a leaf. A new annotator gets one rule per sibling pair.

Also applied: an entry used in fewer than 2 of 60 papers must be clearly general; image_support is judged only from opened images; spine discipline is 10–20 nodes with at most 2 branches plus 1 control branch.

## 5. Data defects in the MatMech records (found by staff, r03–r04)

These are upstream record problems, not vocabulary matters. In every case, figure ids in our graphs follow the image file, not the caption.

| paper | defect | found by |
|---|---|---|
| Acta_Materialia 10.1016/j.actamat.2010.05.040 | F3 and F4 image files swapped relative to their captions: packet F3 shows paper Fig. 3 (SEM of C/P faults) under the Fig. 4 caption, and vice versa | judge r03, S1 |
| Bioactive_Materials j.bioactmat.2021.03.045 | paper Fig. 5 (micro-CT) missing from the record; packet F5–F7 are paper Figs 6–8 | S3 |
| Journal_of_Materials_Science_&_Technology j.jmst.2019.08.010 | packet F2 carries the XRD caption (paper Fig. 1) on the SEM/TEM image of paper Fig. 2; F1 is a caption page. The Scherrer reading had to become text_only | S5 |
| Nature_Materials 10.1038/nmat2713 | F1 image file contains paper Figs 1 and 2 side by side; F2 path is a bare directory; an unlisted near-duplicate composite sits in images/ | S7 |
| Nature_Materials 10.1038/s41563-023-01766-z | F4 path is a bare directory; F5 image is paper Fig. 4 (a–j), and the F5 caption is the tail of the Fig. 4 caption | S7 |
| S8 papers (3 of 4) | MatMech summary numbers disagree with the figures: POC j.porgcoat.2013.10.008 \|Z\| 1e6 Ω cm² at 0.1 Hz vs F6 ≤1.5e4 Ω; Rare Metals s12598-020-01527-w "200 mAh/g after 1900 cycles" vs F4 ~105; Rare Metals s12598-020-01698-6 "κ_L reduced" vs F5e κ_L higher below 700 K | S8 |
| other summary/figure conflicts | bioactmat.2020.11.026 Ca-P in-vivo CR 0.032 mm/y vs F7B ~0.35; adma.201706311 F4c computed but recorded as experiment; Biomaterials (00)00178-2 burst ~20% vs >50%; Biomaterials (02)00177-1 F3 caption concatenates Figs 3 and 4; JAC s40145-021-0458-1 packet F5 is paper Fig. 6 and Fig. 5 is absent; AEM aenm.201501833 F-ids offset by one | S3, S4, S5, S2 |
| **corpus-wide (orchestrator count)** | **1525 of 425,295 image records point to a directory, not a file; 1 file is missing; 1265 papers are affected** | orchestrator |

**Consequences:**
- Staff must not seed labels from the MatMech summary block. Numbers come from the figure, and the text value goes in `image_note`.
- `build_packets.py` should reject directory paths and flag any caption whose figure number differs from the image. It cannot detect swapped images, so these must be found by reading the images.
