# Round r03: judge rulings (v02 → v03)

**Inputs:** PROTOCOL.md, vocab/v02.json, proposals_S1–S4.json, metrics.jsonl, and the orchestrator's r03 metrics: 16 papers, 519 nodes, 645 edges, coverage by v02 = 98.5%, 0 validation problems, 211/211 figure edges with mm_op, 10–19 spine nodes per paper. I read all 16 graphs for proposed and poor-fit nodes (22 poor, 8 proposed). I checked 4 graphs node by node against their packets: Advanced Materials (photonic-crystal memory), JMST (VTaCrW DFT), Nature Materials (PZT modulus sensor) and Acta Materialia (ice faulting). I opened 4 figures: AdvMat F2, JMST F3, NatMat F3 and Acta F3 (image file).

**Result:** 26 rulings: **ACCEPT 22, MERGE 2, RESTRUCTURE 1, REJECT 1**.

v03 has:
- **82 type entries:** 10 L1 + 7 L2 + 65 leaves (+2 leaves, max depth 3, no type renames);
- **14 rels** (2 redefined);
- **27 mm_ops** (+2; 2 proposed ops merged into existing ones and recorded in `renames`);
- **13 modalities** (notes extended).

New in v03 is a `usage` block with r01–r03 counts after all renames (28 papers), for the merge phase.

## Data issue (not a vocabulary matter)

In **Acta_Materialia__10.1016_j.actamat.2010.05.040** the F3 and F4 image files are swapped relative to their captions in the MatMech record. Packet F3 (`f3ae52…jpg`) carries the caption of paper Fig. 4 (fault angle vs confinement) but shows paper Fig. 3, the SEM of the C- and P-faults. I opened the image and confirmed this. Packet F4 is the reverse. S1's figure ids follow the image files, which is correct. The upstream record should be fixed; `build_packets.py` cannot detect this.

## Spot checks

| graph / figure | staff reading | verdict |
|---|---|---|
| AdvMat F2a (absorption + fluorescence on a shared λ axis) | a25 spectrum, `shown`, proposed op assess_feature_overlap | **Reading confirmed.** Curve IV (coumarin emission, ~505 nm) overlaps curve II (closed BP-BTE, ~590 nm, 480–700 nm); open form I has no visible band. a26 `partial` is right: F2b shows only one open/closed pair, not repeated cycling. The op is ruled a merge (#5). |
| AdvMat graph | spine of 21 nodes, 2 branches meeting at a18 | Sound. One op error: a31→a32 is a `derives` edge (image → line profile) carrying `register_colocated_views`. Extracting a profile from one image is not registration of two views; use `measure_feature_metric` (or `replot_derived_series`). |
| JMST F3 (histograms of vacancy E_f and E_m by species) | h12/h13 xy_curve, computed, OBS/response/distribution, read_distribution_statistics | **Confirmed.** Formation energies span ~2.4–3.8 eV on the plot, and V_Ta has the lowest migration bins (0–0.4 eV). The claim IS the spread, and no single point is read. Modality xy_curve is right. |
| JMST graph | computation-only, no PRC; h6 site_occupancy reached by `realizes` with imposed SQS | Correct use of the v02 computation rules. h16 `partial` (the "rises with V" claim is not visible) is a good audit. |
| NatMat F3 (dual-axis bars: sensor µV and CMS modulus MPa) | m18 characteristic_value → m19 via convert_via_calibration; m32 text-silent audit | **Confirmed**, with one correction. The modulus axis is a linear rescaling of voltage, so `derives` + convert_via_calibration is the right reading. The plotted moduli span **~1.5–5.8 MPa**, not the 2.8–7 MPa in the m32 label. The 5-min young-skin bars (~1.5–2 MPa) lie at or inside the 1.76 MPa calibration limit, and all other bars lie above it. m32 stands, but its label should state the range correctly. |
| NatMat graph | device paper, thin STR stage | Legitimate paper shape (#26). m4 DES/architecture carrying F1 is allowed, because it is a design drawing. |
| Acta F3 image (SEM of C/P faults) | o22 micrograph appearance; o23 feature_metric `partial` | **Confirmed.** (a) shows an open gouge 0.1–2 mm wide with debris, which supports STR/microstructure/damage (i7). (b)/(c) show pores aligned along a band, with grain boundaries visible only as hand-drawn outlines in (c), so `partial` is right. |
| Acta graph | o29 register_colocated_views on a `qualifies` edge | A strong audit: thermistor distance is confounded with fault type. The op's broadening to probe-position photographs is accepted (#13). |

Figure reading remains strong: every `partial`/`contradicts` verdict I checked holds, and the one numerical slip (m32 range) does not change the audit. Typing errors are now rare and sit at op level on `derives` edges.

## Rulings table

| # | proposal | staff | ruling | reason |
|---|---|---|---|---|
| 1 | STR/microstructure/damage | S1 | **ACCEPT** | A crack, gouge or delamination state is followed by a friction/fracture-mechanics or failure-mode inference, not by a dislocation (defect/extended) or transport (porosity) inference. Without it, fracture papers jump OBS → PRP/behavior_class and lose the STR stage. Only one node is typed with it, but it is clearly general: thermal-shock microcracking, CMC matrix cracking, cracking of battery particles, coating mud-cracking and fatigue damage. A second in-corpus case exists (Bioactive r03 b14: degradation-opened cracks, currently typed distribution). Boundaries are written against defect/extended and porosity. |
| 2 | OBS/response/distribution | S3 | **ACCEPT** (restricted) | When the spread is the result, the next inference changes: local-environment attribution, overlap/recombination arguments, Weibull reliability. A characteristic value cannot license these. There are 7 nodes in one paper, plus S2's DLS node (d23), which migrates here, so 2 papers in 2 classes. Restricted to **non-imaged** ensembles: imaged-feature statistics stay OBS/morphology/feature_metric, orientation-distribution peaks stay OBS/signal, and a single statistic whose spread is not argued stays characteristic_value. OBS/response is redefined to include "over an ensemble". |
| 3 | Broaden OBS/signal/feature_shift to position relative to another species' feature | S2 | **ACCEPT** (name kept) | The feature read is the same (position); only the reference differs. `attrs.aspect = shift | overlap`. I considered renaming it to feature_position but rejected that: the rename would migrate 9 nodes and would count as a new leaf in metrics without changing any inference. |
| 4 | rel `motivates`: claim → DES/down_select | S2 | **ACCEPT** | Screen-then-choose decisions rest on a weighed claim (trade-off, ranking), not on one OBS. Without this the spine breaks. Restricted to dst = DES/down_select. The DES/down_select definition is updated to match. |
| 5 | mm_op assess_feature_overlap | S2 | **MERGE → compare_coplotted_quantities** (`aspect = overlap`) | The figure act is the same one: set two **different** quantities on shared axes against each other. Dominance and overlap lead to different next nodes (PRP/partition vs MEC/pathway), but the dst type already records which follows, so the op does not need to. The compare family is the largest (6) and should not grow on one paper. S2's audit (compare bandwidths, not just peak positions) is written into the merged definition. Renamed in `renames`. |
| 6 | mm_op read_distribution_statistics | S3 | **ACCEPT** (family read) | This is the figure act for #2, and it has its own failure modes: few counts per class, binning, indistinguishable colour classes, intensity- vs number-weighting (the DLS mean 26.9 vs mode ~21 nm). measure_feature_metric stays for image-derived histograms. |
| 7 | mm_op read_orientation_relationship | S3 | **MERGE → assign_features** (`aspect = orientation_relationship`) | One edge in one paper. The act is indexing reflections of two phases in one pattern and reading which ones coincide; this is assignment plus a pairing. Its distinct consequence (STR/interface: coherency, epitaxy, nucleant potency) is carried by the dst type. I will reconsider as a separate op if r04 shows OR readings in ≥3 papers (precipitation, grain refiners, epitaxial films). |
| 8 | mm_op convert_via_calibration | S4 | **ACCEPT** (family **quantify**, not transform) | 5 edges in 2 papers from different classes (e-beam photonics, bio-device). Its audit (target inside the calibrated range, monotone inversion) changed spine support in both papers. quantify_from_intensity/position apply known physical laws, whereas this op inverts an in-paper empirical calibration. It is a quantify act, the same as its siblings. See merge candidate Q1. |
| 9 | Broaden track_feature_across_series to tracking an identified object through frames | S1 | **ACCEPT** | The existing definition already describes following one feature through a series, and the spectral restriction was incidental. Frame tracking adds identity and aliasing failure modes (AEM F3: simultaneous vs sequential hops), which are now in the definition. |
| 10 | Broaden PRC/treatment to powder comminution and classification | S4 | **ACCEPT** | The compound is the same (not synthesis) and no body is made (not forming). The next step is a before/after size check, which is treatment's inference. It recurs in battery, ceramic and catalyst powders. |
| 11 | Broaden PRC/forming to lithographic/subtractive patterning and transfer printing | S4 | **ACCEPT** | Shaping into a designed geometry, followed by match_to_design against DES/architecture, is exactly forming's inference. A PRC/patterning leaf would change nothing. |
| 12 | Broaden PRF/service_capability to demonstrations (prototype function, process/control capability) | S4, S1 | **ACCEPT** | There are 7 nodes in 3 papers (Nano n18/n21/n25, NatMat m20/m22/m24, AFM s14). A "the built object or method does the job" claim is evidenced like any service claim, and a separate leaf would not change the next step. Demonstration conditions go in attrs. |
| 13 | register_colocated_views: include sensor/probe/indent position photographs registered to signals | S1, S3 | **ACCEPT** | Acta o29 and Matchar F8b (indents on the etched section) show the same act: locating what one view records on a feature that another view delineates. |
| 14 | Audit nodes whose label states the discrepancy take image_support = shown | S1 | **ACCEPT** | The node's claim is the discrepancy, and the figure shows it. The conflict is carried by the qualifies/contrasts edge. Written into the image_support note. |
| 15 | Modality note: intensity line profiles across images → spatial_map | S1 | **ACCEPT** | Written into modality_notes. |
| 16 | Spine: allow a control branch (3 strands) | S1 | **ACCEPT** (restricted) | Allowed: at most two parallel branches **plus one control branch** that ends in a PRP/STR linked to the main branch by `contrasts`. More strands mean sub-results are on the spine. |
| 17 | STR/chemistry/conformation leaf (conditional suggestion) | S1 | **REJECT** | It occurs once (azobenzene isomer), and its next inference (bond/network-level change → property) is the same as bonding's. STR/chemistry/bonding is broadened to configuration/conformation, `attrs.aspect = configuration`. |
| 18 | Biological readout rule: host-tissue biomarkers as PRP/value, object = tissue | S2 | **RESTRUCTURE** | The split S2 proposes for in-vitro vs in-vivo is right, but host-tissue markers are not properties of the material. Rule: **in-vitro cell response vs a design variable = PRP (biological). In-vivo endpoints, and tissue markers that measure endpoint quality (closure, histology scores, collagen, re-epithelialisation, bone ingrowth), = PRF/service_capability. Host biomarkers invoked to explain the endpoint (SOD/catalase oxidative stress, cytokines) = MEC/pathway.** This rule is written into PRP, PRF/service_capability and property_family_notes. |
| 19 | Biodegradation → property_family chemical_corrosion | S2 | **ACCEPT** | Hydrolytic, enzymatic and in-body degradation (Mg implants, polyester hydrolysis, chitosan/lysozyme) are all chemical attack on the material. Written into the note, so that biodegradation is not split across biological/kinetic. |
| 20 | Extrusion boundary: forming = feedstock → body; working a made body = treatment | S3 | **ACCEPT** | Written into both definitions. Hot extrusion of a cast billet (JMA j7) is treatment; extrusion of powder, melt or polymer feedstock is forming. |
| 21 | Reactive hot pressing / SPS / SHS: one synthesis node, attrs.concurrent_forming | S3 | **ACCEPT** | Do not split one act into two nodes. The precursor rule (input is not yet the target compound) decides. |
| 22 | Proxy claims name their proxy (attrs.proxy), basis stays evidenced | S3 | **ACCEPT** | Written into the basis note and the STR/phase/fraction definition (KAM/GAM → transformed fraction). |
| 23 | Modality note: property maps (hardness, modulus) → spatial_map | S3 | **ACCEPT** | Written into modality_notes. A trend read along distance still uses read_trend. |
| 24 | No precipitate/second-phase leaf | S3 | **ACCEPT** (no change; closes the r02 judge candidate) | S3 typed three second-phase papers cleanly with identity / fraction / feature_size / distribution / interface. A combined leaf would hide which aspect the argument uses. |
| 25 | DES/method on the spine (method as headline contribution) | S4 | **ACCEPT** (restricted) | Only when the method is a headline contribution (Nano n27: colour as a dosimeter). DES/method then `realizes` the STR/PRP/MEC claim it makes measurable. The realizes definition and the spine note are updated. It is not a route for putting ordinary characterization choices on the spine. |
| 26 | Device papers have a thin STR stage by nature | S4 | **ACCEPT** (no change) | The argument lives in PRP of an assembly (attrs.object) and PRF of a test object. As in r02 #38, this is a legitimate shape, not a missing type. |

Counts: ACCEPT 22 (1–4, 6, 8–16, 19–26) · MERGE 2 (5, 7) · RESTRUCTURE 1 (18) · REJECT 1 (17).

## Poor-fit and proposed-node rulings (graph migrations)

| node | staff type | should be |
|---|---|---|
| Acta i7 | STR/microstructure/damage (proposed) | accepted as is |
| AdvComp c10 (trans/cis azobenzene) | STR/chemistry/bonding, poor | same, good (`aspect = configuration`, #17) |
| AFM s8 (single Si position moved site by site) | STR/defect/point, poor | same, good (`aspect = position`, now in the definition) |
| AFM s14 (atom steering) | PRF/service_capability, poor | same, good (#12) |
| AFM o20→s8, AEM o26→e6 ops | track_feature_across_series | same, good (#9) |
| AdvMat a7 (colloidal self-assembly + infiltration as film) | PRC/deposition, poor | same, good (self-assembly on a substrate = deposition) |
| AdvMat a9 (fcc colloidal crystal) | STR/phase/identity, poor | same, good (`attrs.scale = mesoscale`, in the definition) |
| AdvMat a25, a33 | OBS/signal/feature_shift, poor | same, good (`aspect = overlap`, #3). Ops assess_feature_overlap → **compare_coplotted_quantities** |
| AdvMat a31→a32 op | register_colocated_views on derives | **measure_feature_metric** (the profile is extracted from one image) |
| Biomaterials 2005 c10 (chitosan crystallinity) | STR/phase/fraction, poor | same, good (crystallinity in the definition) |
| Biomaterials 2013 d6 (micelle self-assembly in saline) | PRC/synthesis, poor | same, good (self-assembly in dispersion = synthesis) |
| Biomaterials 2013 d7 (sol gelling in situ on the wound) | PRC/forming, poor | same, good (in-situ gelation in the definition) |
| Biomaterials 2013 d9 (gel network) | STR/microstructure/porosity, poor | same, good (network mesh in the definition) |
| Biomaterials 2013 d13 (tissue SOD ↓, catalase ↑) | PRP/value, poor | **MEC/pathway** (`mechanism_class = antioxidant`), evidenced by the OBS; it explains the healing PRF (#18) |
| Biomaterials 2013 d14 (collagen, epidermal thickness, histology scores) | PRP/value, poor | **PRF/service_capability** (in-vivo endpoint quality, #18) |
| Biomaterials 2013 d23 (DLS size distribution) | OBS/response/characteristic_value, poor | **OBS/response/distribution**; op → read_distribution_statistics |
| Ceramics c6 (reactive hot pressing) | PRC/synthesis, poor | same, good (#21) |
| JMA j7 (hot extrusion of cast billets) | PRC/treatment, poor | same, good (#20) |
| JMA j21 (superposed SAED, OR) | OBS/signal/feature_assignment, poor; op read_orientation_relationship | same type, good (`aspect = orientation_relationship`); op → **assign_features** (#7) |
| JMST h7, h8, h12, h13, h18, h22, h24 | OBS/response/distribution (proposed) | accepted as is; ops read_distribution_statistics accepted |
| Matchar m17 (KAM → degree of transformation) | STR/phase/fraction | same, `attrs.proxy = KAM` (#22) |
| Nano n18, n21, n25 (demonstrations) | PRF/service_capability, poor | same, good (#12) |
| Nano/NatMat calibration edges (n23→n22, n14→n22, n12→n31, m18→m19, m13→m19) | convert_via_calibration (proposed) | accepted |
| NatMat m6 (lithography + etching + transfer) | PRC/forming, poor | same, good (#11) |
| NatMat m32 | label range 2.8–7 MPa | relabel to ~1.5–5.8 MPa (F3). The audit stands for all but the 5-min young-skin bars |
| Rare Metals s7 (wet milling), s8 (centrifugal classification, spray drying) | PRC/treatment, poor | same, good (#10) |
| Bioactive r03 b14 (degradation opens pores and cracks, exposes HAP) | STR/microstructure/distribution | keep: the argued consequence is HAP exposure (distribution). If a paper argues from the cracks themselves, use STR/microstructure/damage |

**Cluster review:** I checked the 22 poor fits for clusters that would justify a type. Three clusters recur:
1. **Demonstrations** (7 nodes, 3 papers). Absorbed by broadening PRF/service_capability; a demonstration leaf would change no inference.
2. **Soft-matter assembly acts** (self-assembly, in-situ gelation, colloidal crystal). Absorbed by the synthesis, deposition and forming boundary text.
3. **Host-tissue readouts** (2 nodes). Resolved by the PRF/MEC rule, not by a new type.

None justifies a type. After migration all r03 nodes are typed with v03 and no poor fit remains unresolved.

## Merge phase: candidates from usage (r01–r03, 28 papers, after renames)

Counts are `[nodes or edges, papers]` from `usage` in v03. They are computed before the r03 poor-fit migrations above, which move only a handful of nodes. Staff should propose merges in r04. I rule on them at r04, not now, except for #5 and #7, which were forced by this round's proposals.

| id | candidate | evidence | judge's prior |
|---|---|---|---|
| C1 | **track_feature_across_series → compare_across_conditions** for the spectral-stack use; keep track_ only for object identity in frame sequences | compare_across_conditions [98, 26] dominates. track_ [17, 9]'s spectral use duplicates what OBS feature_shift/feature_presence already say | **Likely merge**; staff to test whether any r04 edge loses information |
| C2 | compare family overall (6 ops: across_conditions 98, track 17, coplotted 13, correlate 11, register 11, with_reference_value 10) | all except track have distinct failure modes (correlation ≠ intervention; misregistration; reference provenance) | keep correlate, register, with_reference_value; see C1 |
| Q1 | **quantify_from_intensity [8, 6] + quantify_from_position [2, 2] + convert_via_calibration [5, 2] → one op "convert_to_quantity"** with `attrs.via = intensity \| position \| calibration` | same act (feature → number through a relation). The audits differ only in which relation is trusted | **Plausible merge**. Keep separate until r04 shows whether `via` is reliably filled |
| Q2 | **extract_slope [7, 6] → fit_model [4, 3]** | a slope on linearised axes is a one-parameter fit | plausible; keep extract_slope if the diagnostic chain (slope → PRP/diagnostic → KNW/lookup) needs a visible name |
| K1 | check/transform tail: flag_outlier [1, 1], subtract_reference [1, 1], collapse_by_normalization [2, 1] | general but rare | prune any op with < 3 uses after r04 (60 papers). Candidates: flag_outlier → cross_check_consistency, subtract_reference → replot_derived_series |
| P1 | **PRP/partition [2, 2] → PRP/value** (`aspect = partition`) | the partition reading is already carried by OBS/response/component_partition + compare_coplotted_quantities | likely merge |
| P2 | **PRP/diagnostic [3, 3] → PRP/value** (`role = diagnostic`) | the diagnostic chain is recognisable from the KNW/lookup → MEC/identification edges | contested: the leaf makes the diagnostic inference visible. Staff to argue |
| O1 | **OBS/response/regime_map [1, 1] → OBS/response/trend** (`dimension = 2D`) | 1 use in 28 papers | likely merge unless r04 brings TTT/phase-diagram papers |
| O2 | **OBS/response/component_partition [3, 3] → OBS/response/trend** | the op (compare_coplotted_quantities) carries the reading | likely merge, together with P1 |
| F1 | **PRF/figure_of_merit [2, 2] vs PRF/qualification [4, 3]** | both judge a composite or benchmark number | keep for now: FOM combines properties, qualification applies external criteria |
| S1 | STR low-use leaves: defect/extended [2, 2], microstructure/orientation [2, 2], site_occupancy [4, 4], damage [1, 1] | each has a distinct next inference (slip/phonon, anisotropy, site-selective evidence, fracture) | **keep**: low use reflects the corpus mix (few metallurgy papers), not redundancy |

## Where the hierarchy is and is not converging

**Converging.** The argument-role skeleton is stable:
- HYP (3), DES (6), PRC (6), PRP (5), PRF (3), MEC (3), KNW (4) and DSC (5) got no new leaf this round;
- 12 of 16 papers had no proposed type;
- coverage by the previous vocabulary rose from 96.9% to 98.5%;
- it held across a DFT paper, an ice-mechanics paper, three biomedical papers, a device paper, photonics and a Si anode.

Growth is now confined to the two places r02 predicted, both at low volume: STR/microstructure (damage) and OBS/response (distribution). Poor fits have moved from missing types to **boundary text**. Almost every r03 poor fit was resolved by one sentence in a definition: extrusion, reactive consolidation, self-assembly, demonstrations, host tissue. The mm_op set likewise grew through broadenings and merges rather than new verbs.

**Not converging.**
1. **Biomedical in-vivo papers.** The PRF/MEC split for host responses is new and untested beyond one paper.
2. **Method and device papers**, whose "performance" is that of a process or instrument. The spine rules (DES/method on spine, control branch) were patched this round and need r04 evidence.
3. **The low-use tail** of ops and leaves: see the merge table.

**Saturation.** Accepted leaves are 2/16 = **0.125 per paper**, just above the < 0.1 stop threshold. Coverage (98.5%) passes. The stop rule is formally **not met**, narrowly. My judgement: the growth phase is effectively saturated, since both leaves are low-volume and one is argued largely from generality. r04 (32 papers) should be run as the confirmation round with merge proposals in parallel. If r04 adds ≤ 3 leaves, growth stops.

## Guidance to staff for r04

1. **Try boundary text before a leaf.** Most r03 poor fits were solved by existing definitions read literally. Before marking a node poor, re-read the v03 definitions, which now cover extrusion, reactive consolidation, self-assembly, demonstrations, in-vivo endpoints, crystallinity, isomer state and mesoscale lattices.
2. **The op on a `derives` edge must be a transform or quantify act**, never a compare act (AdvMat a31→a32). If one image is reduced to a profile or number, use measure_feature_metric, replot_derived_series or convert_via_calibration.
3. **Numbers in labels must be read from the figure**, not only from the text. NatMat m32 quoted 2.8–7 MPa where the plot shows ~1.5–5.8 MPa. When text and figure differ, the label follows the figure and `image_note` gives the text value.
4. **Biomedical papers:**
   - in-vitro cell data vs a design variable → PRP (biological);
   - in-vivo endpoint and endpoint-quality histology → PRF/service_capability;
   - explanatory host biomarkers → MEC/pathway;
   - degradation → property_family chemical_corrosion.
5. **Distributions:**
   - a histogram of a non-imaged ensemble whose spread is argued → OBS/response/distribution + read_distribution_statistics;
   - a histogram of image-derived sizes → OBS/morphology/feature_metric + measure_feature_metric;
   - a single mean → characteristic_value.
6. **Overlap readings** (emission vs absorption, band vs stopband) are OBS/signal/feature_shift with `aspect = overlap` and op compare_coplotted_quantities. Check bandwidths as well as peak positions.
7. **Spine discipline:**
   - at most two parallel branches plus one control branch closed by `contrasts`;
   - DES/method on the spine only when the method is the headline;
   - DES/down_select is reached by `motivates` from the weighed claim.
8. **Merge phase.** Each staff member submits ≥ 3 merge proposals in `merges`, citing usage counts from the v03 `usage` block and one r04 edge or node per proposal that would lose or keep information. Priorities: C1, Q1, P1/O2, O1, K1.
9. **Packet anomalies** (swapped figures, like Acta F3/F4) go in `notes` and the proposal comments. Figure ids always follow the image file, never the caption.
