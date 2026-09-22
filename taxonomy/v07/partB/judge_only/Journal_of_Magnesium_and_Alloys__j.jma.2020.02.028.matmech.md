# MatMech content for Journal_of_Magnesium_and_Alloys/j.jma.2020.02.028 (judge only; not shown to staff)
- material: AZ61 Mg alloy  elements: ['Al', 'Mg', 'Zn']  category: ['Metals and Alloys', 'Nanomaterial', 'Crystalline Material']
- MST chain: Processing → Structure → Properties
## Tetrahedron elements
- **Processing**: Equal-channel angular pressing (ECAP) with 160° channel angle at 373 K, 423 K, and 473 K, followed by electropulsing treatment (EPT) with pulse durations of 25–50 μs and processing times of 5–20 min
- **Structure**: Grain size refined from 89 μm to 1.0 μm; homogeneous ultrafine equiaxed grains; high dislocation density; weakened basal texture; increased fraction of high-angle grain boundaries (HAGBs)
- **Properties**: yield strength–mechanical property, ultimate tensile strength–mechanical property, tensile elongation to failure–mechanical property
- **Performance**: Exceptional combination of high strength (YS = 330 MPa, UTS = 448 MPa) and good ductility (TEF = 15%) surpassing conventional AZ61 alloys processed by other methods
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Equal-channel angular pressing (ECAP) with 160° channel angle at 373 K for 4 passes
- effect: High dislocation density and non-equiaxed microstructure with limited dynamic recrystallization
- experiment: ECAP processing at 373 K | Equal-channel angular pressing | params: Channel angle = 160°, temperature = 373 K, 4 passes, Bc route, extrusion rate = 4 mm/s | result: Samples showed high defect density, undeformed areas dominant, no full recrystallization; 5th pass caused fracture
  - [referenced knowledge] ECAP with 160° channel angle generates lower equivalent strain per pass (ε_eq = 0.2) compared to 90° dies.
  - [non-referenced_knowledge] Lower strain per pass reduces thermal activation needed for recrystallization.
  - [experimental result] Processing at 373 K (below typical recrystallization temperature) further inhibits dynamic recrystallization.
  - [image description] Micrographs (Fig. 3) show high defect density and undeformed regions after 4 passes at 373 K.
  - [deductive reasoning] Thus, 160° ECAP at 373 K accumulates high dislocation density without significant recrystallization.
### M2  Processing → Structure
- cause: Variable-temperature ECAP: 8 passes at 423 K followed by 3 passes at 373 K
- effect: Highly deformed, elongated microstructure with high accumulated dislocation density and suppressed dynamic recrystallization
- experiment: Variable-temperature ECAP | Equal-channel angular pressing | params: 8 passes at 423 K, then 3 passes at 373 K | result: Grains refined but elongated; dynamic recrystallization incomplete; high dislocation density retained
  - [image description] 8-pass ECAP at 423 K refines grains but leaves incomplete recrystallization due to sub-optimal temperature.
  - [experimental result] Subsequent 3-pass ECAP at 373 K introduces additional strain without triggering recrystallization.
  - [non-referenced_knowledge] Lower temperature suppresses atomic diffusion and grain boundary migration, inhibiting recrystallization.
  - [deductive reasoning] Thus, the combined process accumulates high dislocation density while maintaining deformed microstructure.
### M3  Processing → Structure
- cause: Electropulsing treatment (EPT) with 25 μs pulse duration and 10 min processing time on variable-temperature ECAPed AZ61
- effect: Ultrafine, homogeneous, equiaxed grains with average size of 1.0 μm and high fraction of high-angle grain boundaries (HAGBs)
- experiment: EPT with 25 μs pulse duration and 10 min processing time | Electropulsing treatment | params: Pulse duration = 25 μs, processing time = 10 min, frequency = 100 Hz, current = 1×10⁴ A | result: Complete recrystallization with average grain size of 1.0 μm; uniform equiaxed microstructure
  - [non-referenced_knowledge] High deformation stored energy (DSE) from variable-temperature ECAP provides thermodynamic driving force for recrystallization.
  - [non-referenced_knowledge] EPT applies high peak current density (jm), generating electron wind force that promotes dislocation motion and nucleation.
  - [image description] EBSD data show high HAGB fraction (65%) and uniform grain size in 25 μs-10 min sample.
  - [experimental result] Shorter pulse duration prevents excessive thermal softening and abnormal grain growth.
  - [deductive reasoning] Thus, optimized EPT parameters induce rapid, uniform static recrystallization into ultrafine grains.
### M4  Structure → Properties
- cause: Ultrafine grain structure with average size of 1.0 μm and high fraction of HAGBs (65–90%)
- effect: Increased yield strength (YS = 330 MPa) and ultimate tensile strength (UTS = 448 MPa)
- experiment: Tensile testing of EPTed samples | Uniaxial tensile test | params: Strain rate = 0.6×10⁻³ s⁻¹, room temperature | result: YS increased from 100 MPa (as-received) to 330 MPa; UTS increased from 260 MPa to 448 MPa
  - [experimental result] Grain size decreased from 89 μm to 1.0 μm after ECAP+EPT.
  - [referenced knowledge] Hall–Petch relation states that yield strength increases as grain size decreases.
  - [image description] EBSD shows HAGB fraction increased to 65% in ultrafine-grained sample.
  - [non-referenced_knowledge] HAGBs act as barriers to dislocation motion, increasing flow stress.
  - [deductive reasoning] Thus, refined grains and high HAGB fraction jointly enhance YS and UTS.
### M5  Structure → Properties
- cause: Presence of fine Mg₁₇Al₁₂ precipitates dispersed at grain boundaries
- effect: Additional precipitation strengthening contributing to increased yield and ultimate tensile strength
- experiment: Microstructural analysis of precipitates | SEM and EBSD | params: Imaging of grain boundaries in ECAP+EPT samples | result: Fine Mg₁₇Al₁₂ precipitates observed at grain boundaries in micrographs (Fig. 10)
  - [non-referenced_knowledge] Mg₁₇Al₁₂ precipitates are known to form in AZ61 alloy during thermal and deformation cycles.
  - [image description] SEM micrographs (Fig. 10) show fine precipitates at grain boundaries after EPT.
  - [non-referenced_knowledge] Precipitates pin dislocations, increasing the stress required for plastic deformation.
  - [deductive reasoning] This contributes to the observed increase in YS and UTS beyond grain refinement alone.
### M6  Structure → Properties
- cause: Weakened basal texture and increased HAGB fraction
- effect: Improved tensile elongation to failure (TEF = 15%) compared to conventional ECAPed samples (TEF ≤ 10%)
- experiment: Tensile elongation measurement | Uniaxial tensile test | params: Strain rate = 0.6×10⁻³ s⁻¹, room temperature | result: TEF increased from 7% (373K-4) to 15% (25 μs-10 min EPT sample)
  - [non-referenced_knowledge] As-received AZ61 has strong basal texture with c-axis aligned to ND.
  - [image description] EBSD pole figures show weakened texture in 25 μs-10 min EPT sample (texture index = 3.85).
  - [image description] High HAGB fraction (65%) enables grain boundary sliding and activation of non-basal slip systems.
  - [non-referenced_knowledge] This allows more homogeneous deformation, delaying necking and increasing elongation.
  - [deductive reasoning] Thus, texture weakening and HAGB increase improve TEF from ≤7% to 15%.
### M7  Processing → Properties
- cause: Combined ECAP (variable temperature) and EPT (25 μs, 10 min)
- effect: Exceptional mechanical performance: YS = 330 MPa, UTS = 448 MPa, TEF = 15%
- experiment: Mechanical testing of final composite-processed sample | Uniaxial tensile test | params: Sample: 423K-8+373K-3+25μs-10min; strain rate = 0.6×10⁻³ s⁻¹ | result: YS = 330 MPa, UTS = 448 MPa, TEF = 15% — highest among all samples
  - [experimental result] Variable-temperature ECAP (8+3 passes) produces high dislocation density and deformed microstructure.
  - [experimental result] EPT with 25 μs-10 min induces rapid, uniform static recrystallization into 1.0 μm grains.
  - [image description] Precipitates and HAGBs further enhance strength and ductility.
  - [experimental result] Tensile tests show this sample achieves highest YS, UTS, and TEF among all processed variants.
  - [inductive reasoning] Thus, the combined processing achieves a unique balance unattainable by either method alone.
