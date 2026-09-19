# Round r02: judge rulings (v01 → v02)

**Inputs:** PROTOCOL.md, vocab/v01.json, proposals_S1–S4.json, metrics.jsonl (r02: 326 nodes, 8 papers, coverage by v01 = 96.9%, 147/147 figure edges with mm_op). I read all 8 graphs; 4 were checked node by node against their packets: Rare Metals, JMA, JMST and Biomaterials. Figures opened: Rare Metals F2, JMA F11, JMST F8, Biomaterials F3 and F7, AEM F5.

**Result:** 38 rulings: **ACCEPT 28, MERGE 3, RESTRUCTURE 3, REJECT 4**.

v02 has:
- **80 type entries:** 10 L1 + 7 L2 + 63 leaves (+5 leaves, max depth 3);
- **14 rels** (+1);
- **25 mm_ops** in 6 families (+4, 1 renamed);
- **13 modalities** (+3).

It also introduces 5 renames and 1 attr-value rename. v02 also adds the node field `spine` and the claim attribute convention `attrs.basis`, both written into PROTOCOL.md.

## Spot checks

| figure | staff label | verdict |
|---|---|---|
| Rare Metals F2b SAED | r13 diffraction_pattern, assign_features, **contradicts** | **Confirmed.** The inner ring is labelled Fe3O4(311) (d = 2.53 Å) and the outer ring anatase(101) (d = 3.52 Å). The larger d must give the smaller ring, so the labels are swapped. F2a: contrast separation is clear and many particles are elongated, so r14 `partial` is right. |
| JMA F11 pole figures + misorientation histograms | n23 orientation_distribution (poor), n24 xy_curve feature_metric (poor), n25 feature_presence text_silent | **Confirmed.** The (0001) maxima sit at the TD rim, not at ND, and no pre-EPT baseline is shown, so `partial` is right. The <2° bin dominates (b). A ~88° spike is visible in (d). Modality `orientation_distribution` is correct: the pole figure has no spatial axes. Type rulings are in the poor-fit section below. |
| JMST F8 EPMA line scans beside BEI | m16/m17 spatial_map, correlate_colocated_modalities | **Confirmed.** The dashed layer boundaries in both profiles are registered to layers I–IV in the central BEI. The Al trough (~3300 vs ~4200 counts) at the B2/II boundary is real and text-silent. Line scan → `spatial_map` is right (now in modality_notes). |
| Biomaterials F7C (10 µm bar) | b20 feature_metric, **contradicts** | **Confirmed.** The largest voids are ~30–35 µm and most are 5–20 µm, against the 50–100 µm in the text. |
| Biomaterials F3B | b13 spatial_map, proposed volume_render | **Confirmed** as a colour-segmented 3D surface render. It supports the connectivity and penetration-depth reading (PLA fills about one HA pore layer). `volume_render` accepted. |
| AEM F5 FT-EXAFS | a19/a20 spectrum, quantify_from_intensity | Correct reading. Co shell II falls monotonically. Fe shell III rises to match shell II only at 0.49 (a20 `partial` is right). Modality note added: FT-EXAFS/PDF → `spectrum`. |

Figure reading by staff remains strong: every contradicts or partial verdict I checked holds. The errors I found are rel misuse and audit inflation:

- **PRC→PRC typed `realizes`.** AEM a7→a8; Bioactive b6→b7. Migrate to `feeds_into`.
- **DES→DES `realizes`.** Bioactive b14→b5. This should be `motivates`.
- **Inconsistent calcination typing.** Bioactive b7 is a gel calcination typed treatment, while Rare Metals r8 (the same act) is typed synthesis. Migrate b7 → `PRC/synthesis`.
- **Claim nodes carrying `figs`.** a10, a16, a18, b16, b19 and others duplicate the OBS nodes that already hold those figures.

## Rulings table

| # | proposal | staff | ruling | reason |
|---|---|---|---|---|
| 1 | STR/phase/site_occupancy | S1 | **ACCEPT** (absorbs #2) | A which-site / what-order claim leads to site-selective evidence (EXAFS shells, L-edge, superstructure reflections, NMR, Mössbauer) and to site-specific property arguments (active site, crystal field, phonon mass disorder). It recurs in spinels, pyrochlores, perovskites, HEAs, doped oxides and intermetallics. Boundary with STR/defect/point: point keeps charge state, compensation and carrier/diffusion arguments. |
| 2 | STR/phase/ordering | S2 | **MERGE → STR/phase/site_occupancy** (aspect = ordering) | Order vs random occupancy is the same object as #1: the distribution of species over sublattices. Preference vs ordering is `attrs.aspect`. As separate siblings they would not be mutually exclusive: inversion degree is both. |
| 3 | STR/microstructure/porosity | S2 | **ACCEPT** | Two papers (ceramic, scaffold). It is general: sintered ceramics, AM metals, foams, scaffolds, catalyst supports. A fraction or a connectivity claim has its own next step: a transport argument, or a correction or qualification of property values measured on porous bodies. Pore size stays in feature_size. Specific surface area is included. |
| 4 | DES/architecture | S2 | **ACCEPT** | One paper, but clearly general (AM lattices, scaffolds, laminates, core–shell, graded coatings, device stacks). It is the only DES that is followed by a fidelity check (match_to_design) rather than an incorporation or phase check. |
| 5 | PRC/joining | S3 | **ACCEPT** | One paper, but welding, brazing and diffusion or adhesive bonding are a large, cross-class literature. The product is an assembly with a new interface, and interface reaction-layer and joint-strength inferences follow. Forming is redefined to exclude it. |
| 6 | STR/microstructure/orientation | S3 | **ACCEPT** (broadened) | Texture and grain-boundary character lead to anisotropy, slip or twin activation and recrystallisation diagnosis, not to Hall–Petch. Broadened to thin-film preferred orientation and polymer molecular or fibre orientation so it is not metals-only. |
| 7 | rel feeds_into | S2 | **ACCEPT** | Multi-step routes (mold→cast, reaction→sintering, deposition→calcination) had no PRC→PRC rel, and staff were misusing `realizes` for it. |
| 8 | realizes: dst may be STR (in-silico construction) | S4 | **ACCEPT, restricted** | Only in computation-first papers, and the STR node must carry `attrs.basis = imposed`. That keeps imposed structure from looking like inferred structure. |
| 9 | evidences: dst may be DSC/comparison | S4 | **ACCEPT, extended** | Also DSC/limitation (Bioactive b37→b42). An OBS can directly show agreement, disagreement or a limit. Other DSC stays `supports`-only. |
| 10 | mm_op correlate_across_figures | S1 | **ACCEPT, renamed correlate_across_series** | The op aligns two different quantities over the same sample series in different figures or ordinates. It licenses only a correlational attribution, and that weakness should be visible in the graph. It is distinct from compare_coplotted_quantities (shared axes, dominance) and cross_check_consistency (an arithmetic audit of one quantity). |
| 11 | mm_op correlate_colocated_modalities | S3 | **RESTRUCTURE → register_colocated_views** (family compare) | The distinction from #10 is real. #10 is co-variation **across samples** and gives a correlational attribution. This one is co-location **within one region** and puts chemistry or structure onto a delineated feature. Its failure modes are misregistration and probe size. Renamed so that it also covers #12 and multi-channel audits (Ceramics c21: co-located dark patches in Y/O/Zr maps mean topography, not segregation). |
| 12 | mm_op link_across_magnifications | S2 | **MERGE → register_colocated_views** | Relating a low-mag and a high-mag view of the same region is the same act as registering two modalities: locate what one view shows on a feature the other delineates. The failure mode is the same too (the high-mag field is not where it is assumed to be). |
| 13 | mm_op match_to_design | S2 | **ACCEPT** | The reference is a geometric intent, not a pattern, and the conclusion is process fidelity, not identity. It is general to AM, lithography, patterning, templating and target thickness. I did not broaden match_to_reference, because doing so would blur identity vs fidelity. |
| 14 | mm_op quantify_from_position | S2 | **ACCEPT** | Position → lattice parameter, strain or composition (Bragg, Vegard) is the most common reduction in the corpus and had no op. It closes the r01 gap on derives edges to lattice spacing. |
| 15 | assign_features: include image contrast levels | S4 | **ACCEPT** (broadening) | Z-contrast or mass-thickness → phase via a known mapping is the same match act as indexing. When a co-registered map, rather than a known mapping, assigns the contrast, use register_colocated_views. |
| 16 | compare_with_literature → compare_with_reference_value | S4 | **ACCEPT** (rename) | Covers in-paper benchmark systems (the PLY dimer) and experimental constants (graphite spacing, Nano n9→n11). |
| 17 | modality volume_render | S2 | **ACCEPT** | A 3D experimental reconstruction is the only form that supports connectivity and penetration judgements, and it has its own artefacts. simulation_render stays for simulated output. |
| 18 | modality orientation_distribution | S3 | **ACCEPT** | Intensity over orientation space (pole figure, ODF, IPF density) matches no existing figure form. An IPF-coloured EBSD map stays `spatial_map`. |
| 19 | modality dispersion_diagram | S4 | **ACCEPT** | E vs k along a path (bands, phonons) is read for crossings, gaps and widths, not as a response trend. It recurs in every DFT or phonon paper. Note added: DOS/pDOS/COOP → `spectrum`. |
| 20 | property_family += catalytic | S1, S4 | **ACCEPT** | Needed in 3 of 8 papers (OER, photocatalysis ×2). Electro- and photocatalytic activity is `catalytic`; ionic_electrochemical keeps ion conduction, redox capacity and battery behaviour. AEM a33/a37 and Rare Metals r30 migrate. |
| 21 | property_family += energetic | S4 | **MERGE → thermodynamic** (new value) | "Energetic" collides with energetic materials. Binding, cohesive, formation and surface energies and phase stability are `thermodynamic`. |
| 22 | Broaden OBS/signal/feature_quantification to qualitative width/intensity readings | S1 | **ACCEPT** | a13 (broadening read qualitatively) is the same readout without the conversion step. Whether a number is produced goes in attrs. |
| 23 | Widen quantify_from_intensity to histogram bins | S3 | **REJECT** | Summing bins of a histogram of image-derived values is a metric of imaged features. measure_feature_metric is broadened instead, and JMA n24 migrates. |
| 24 | PRP applies to "material or assembly" (attrs.object) | S3 | **ACCEPT** | A joint, a coating–substrate system or an electrode has properties argued like a material's. A separate assembly type would change no inference. |
| 25 | attrs.basis = argued on PRP | S2 | **ACCEPT, generalised** | One convention for all claim nodes, STR/PRP/PRF/MEC: evidenced \| argued \| attributed \| imposed. It also absorbs S3's "inferred" (JMA n14, stored dislocation density), which becomes `argued`. |
| 26 | Line scans → spatial_map (modality note) | S3 | **ACCEPT** | A quantity over sample distance is a 1D map. Coding it as xy_curve would invite trend reading. |
| 27 | PRP/value vs PRF/qualification rule (community benchmark → PRF) | S1 | **ACCEPT** | Written into the PRF/qualification definition. AEM a46 is now a good fit. |
| 28 | Boundary rule synthesis vs treatment ("converts precursor = synthesis; re-phases as-made solid = treatment") | S1 | **RESTRUCTURE** (merged with #29) | S1 applied the rule to a gel calcination (b7) and called it treatment. S4 applied its own rule to the identical act (r8) and called it synthesis. Unified rule: **if the input is not yet the target compound (precursor, gel, hydroxide, salt, mixed oxides) the step is synthesis, even when thermal. A step on the made compound that changes phase, crystallinity or microstructure is treatment.** b7 migrates to PRC/synthesis. |
| 29 | Boundary rule "new phase = synthesis" | S4 | **RESTRUCTURE** (merged into #28) | "New phase" alone would make every ageing precipitation and every martensitic quench synthesis. The test is the compound, not the phase. |
| 30 | Treatment vs stimulus: "treatment makes the material to be used; stimulus probes it" | S2 | **ACCEPT** | Written into both definitions. Ceramics c10 (1300 °C/24 h ageing as a service test) is correctly a stimulus. |
| 31 | Treatment vs stimulus: "during observation vs judged afterwards" | S3 | **REJECT** (criterion) | Post-mortem service tests (ageing, immersion, irradiation, fatigue) are judged afterwards and are still stimuli. Purpose decides. S3's typing of EPT as treatment is correct under #30. |
| 32 | Composition (what) vs distribution (where / homogeneity) | S2 | **ACCEPT** | Written into the STR/chemistry/composition definition. "Chemically homogeneous" is distribution; "layer II is Co/Ni-rich" is composition. |
| 33 | Provisional PRC/treatment | S1, S3 | **ACCEPT** (confirmed; flag removed) | ECAP and electropulsing (JMA) are clean cases. Bioactive b7 moves to synthesis (#28), so the evidence is one paper, but the category is clearly general. |
| 34 | Provisional STR/chemistry/composition | S1, S3 | **ACCEPT** (confirmed; flag removed) | Co valence (AEM a24), Ce3+/Ce4+ (Bioactive b21), per-layer compositions (JMST m19): three papers, three classes. |
| 35 | Audit-only ops are not mm_ops (S2 used compare_coplotted_quantities for c21) | S2 | **REJECT** (the workaround) | compare_coplotted_quantities needs shared axes. c21 → register_colocated_views, which is a genuine general op that audits also use. The r01 rule stands: do not invent ops that only an audit would use. |
| 36 | No operando/in-situ leaf (PRC/stimulus + OBS trend) | S1 | **ACCEPT** (no change) | In-situ vs ex-situ is an attr (`attrs.in_situ: true`). |
| 37 | No SPD stored-energy leaf | S3 | **ACCEPT** (no change) | STR/defect/extended + attrs.basis = argued. |
| 38 | "Method papers with no property test end at STR" treated as a gap | S2 | **REJECT** (as a vocabulary issue) | It is a legitimate paper shape, not a missing type; the spine may end at STR plus DSC. |

Counts: ACCEPT 28 (1, 3–10, 13–20, 22, 24–27, 30, 32–34, 36, 37) · MERGE 3 (2, 12, 21) · RESTRUCTURE 3 (11, 28, 29) · REJECT 4 (23, 31, 35, 38).

## Poor-fit and proposed-node rulings (graph migrations)

| node | staff type | should be |
|---|---|---|
| AEM a13 (broadening read qualitatively) | OBS/signal/feature_quantification, poor | same type, good (broadened definition) |
| AEM a23 | STR/phase/site_occupancy (proposed) | accepted as is |
| AEM a46 (overpotential at 10 mA/cm²) | PRF/qualification, poor | same, good (benchmark rule). a33/a37 property_family → catalytic |
| Bioactive b33 (photocatalytic activity) | PRP/value, poor | PRP/value, property_family = catalytic |
| Bioactive b7 (gel calcination) | PRC/treatment | **PRC/synthesis** (fed by b6 via feeds_into) |
| Biomaterials b5–b7 | DES/architecture (proposed) | accepted. b7 (discrete composite zoning) is architecture, not modification |
| Biomaterials b28, b30 | STR/microstructure/porosity (proposed) | accepted |
| Biomaterials b29 (mold ridges on pore walls) | STR/microstructure/shape, poor | same, good (shape now includes surface topography) |
| Biomaterials b35 (region-wise stiffness, never measured) | PRP/value, poor | PRP/value + attrs.basis = argued, good |
| Biomaterials b13, b18 | spatial_map + proposed_modality | modality → volume_render |
| Biomaterials b21 op | link_across_magnifications | register_colocated_views |
| Ceramics c28 | STR/phase/ordering (proposed) | STR/phase/site_occupancy, aspect = ordering, basis = argued (image_support not_shown stays) |
| Ceramics c33 | STR/microstructure/porosity (proposed) | accepted |
| Ceramics c21 op | compare_coplotted_quantities | register_colocated_views |
| JMA n14 (stored dislocation density, unmeasured) | STR/defect/extended, poor | same, attrs.basis = argued, good |
| JMA n23 (pole-figure maxima) | OBS/morphology/distribution, poor | **OBS/signal/feature_quantification** (texture strength from maxima), modality orientation_distribution. The op on n23→n26 is read_characteristic_point (unchanged). A pole figure is not spatial content, so morphology was wrong |
| JMA n24 (LAGB/HAGB fractions) | OBS/morphology/feature_metric, poor | same, good. Op quantify_from_intensity → **measure_feature_metric** |
| JMA n25 (~30° and ~88° histogram peaks) | OBS/signal/feature_presence, poor | same, good (signal now covers peaks of non-spatial distributions) |
| JMA n26 | STR/microstructure/orientation (proposed) | accepted |
| JMST m9 | PRC/joining (proposed) | accepted |
| JMST m34 (joint shear strength) | PRP/value, poor | PRP/value, attrs.object = joint, good |
| JMST m15/m16/m18/m22 ops | correlate_colocated_modalities | register_colocated_views |
| Nano n8 (substitutional N imposed by the model) | STR/defect/point, poor | same, attrs.basis = imposed, reached by `realizes`, good. Not site_occupancy: the next inference is electron count (carriers) |
| Nano n19 | PRP/value family mechanical | property_family = thermodynamic |
| Nano F5/F7 band panels (n21, n30, n32) | xy_curve + modality_proposed | dispersion_diagram |
| Nano n9/n27 ops | compare_with_literature | compare_with_reference_value |
| Rare Metals r8 (gel calcination) | PRC/synthesis, poor | same, good (#28) |
| Rare Metals r30 | PRP/value, chemical_corrosion | property_family = catalytic |
| AEM a21→a38, Bioactive b32/b35→b39 | correlate_across_figures | correlate_across_series |
| AEM a7→a8, Bioactive b6→b7, Biomaterials b8→b9→b10/11, Ceramics c8→c9 | realizes / feeds_into | feeds_into |

After migration all r02 nodes are typed with v02 and no poor fit remains unresolved.

## Where the hierarchy is and is not converging

It is converging on the **argument-role skeleton**. The same shapes recurred in electrocatalysis, photocatalysis, biomedical scaffolds, high-entropy ceramics, SPD Mg, dissimilar joining and a pure-DFT paper:

- flat PRP (value / behavior_class / descriptor / diagnostic / partition);
- flat MEC (pathway / identification / tradeoff);
- the KNW use cut;
- the OBS read-feature cut (signal / response / morphology).

None of these needed a new leaf; property family, mechanism class and technique stayed attrs. S4's DFT paper went through with 0 proposed types. That is the strongest sign that provenance = computed plus the OBS read-feature cut generalises.

Growth is now confined to two places. The first is **STR/microstructure and STR/phase**. Porosity, orientation and site occupancy were all predictable gaps that r01 flagged, and I expect one or two more here: candidates are precipitate/second-phase state (currently spread over phase/identity + distribution + feature_size) and molecular-weight/crosslink state for polymers (currently chemistry/bonding). The second is **the PRC/DES boundary for geometry and assembly** (architecture, joining).

It is **not** converging on three fronts:

1. **Boundary rules.** Synthesis/treatment/stimulus had two conflicting staff rules in one round. This round's rules are now written into the definitions and need testing.
2. **mm_ops.** Four new ops in 8 papers. The two correlation/registration ops were real gaps rather than synonyms, but the compare family now has 7 members, and I will look for merges at r03.
3. **Graph size.** 40.8 nodes/paper and rising, driven by audit nodes. The new spine/periphery rule addresses this.

Leaf growth this round is 5/8 = 0.63 leaves per paper (r01: 14.5), and coverage by the previous vocabulary is 96.9%. **Not saturated yet**: the stop rule requires < 0.1 per paper at ≥ 16 papers. On current trends I expect r03 (16 papers) to add 2–4 leaves (≈0.2/paper). r04 is the first realistic stopping round.

## Guidance to staff for r03

1. **Mark the spine first.** Before typing evidence, write the 10–20 node spine (HYP → DES → PRC → STR → PRP → PRF → DSC/conclusion, plus bridging MEC) and set `spine: true`. OBS and KNW are never spine. Check that the spine is connected and that every spine claim has an OBS `evidences` edge or a non-default `attrs.basis`.
2. **Audit budget ≤ 5 nodes per paper.** A `text_silent` or audit OBS node is created only if it changes support for a spine claim. Minor image observations go in `attrs.image_note`. Target 25–40 nodes per paper.
3. **Do not attach `figs` to claim nodes** (STR/PRP/PRF/MEC) when an OBS node already carries that figure. Claim nodes carry figs only for schematics of the claim itself (structure model, mechanism diagram), and DES/PRC only for design or route drawings.
4. **PRC→PRC is `feeds_into`**, never `realizes` or `premise_for`. `realizes` is DES→PRC/measurement (or DES→STR with basis = imposed in computation papers). DES→DES is `motivates`.
5. **Apply the boundary rules literally:**
   - *Gel/precursor calcination* is synthesis.
   - *Treatment* is for the made compound.
   - *Stimulus* is for probing or service tests.
   - *Composition* = what; *distribution* = where.
   - *site_occupancy* = which site / order; *defect/point* = charge, compensation, carriers.
   - *PRF/qualification* = value at a community benchmark condition.
6. **Choose the correlation op carefully:**
   - *correlate_across_series*: same samples, different figures, different quantities.
   - *register_colocated_views*: same region, different modality, channel or magnification.
   - *compare_coplotted_quantities*: shared axes only.
   - *cross_check_consistency*: an arithmetic audit of one quantity.
7. **Use `attrs.basis`** (argued / attributed / imposed) on any claim with no incoming evidence instead of marking it fit = poor.
8. **Before proposing a new leaf, try the attrs and the v02 boundary rules.** Propose only if the next inference differs, and give ≥2 example nodes from ≥2 materials classes where possible.
