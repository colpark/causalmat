# MatMech content for Journal_of_Materials_Science_&_Technology/j.jmst.2020.05.053 (judge only; not shown to staff)
- material: Al₀.₉CoFeNi₂  elements: ['Al', 'Co', 'Fe', 'Ni']  category: ['Metals and Alloys', 'Crystalline Material', 'Composite Material']
- MST chain: Processing → Structure → Properties
## Tetrahedron elements
- **Processing**: Bulk casting via medium-frequency induction melting under Ar atmosphere
- **Structure**: Dual-phase lamellar eutectic microstructure composed of FCC (L1₂) phase (60%) and B2 phase (40%), with lamellar width of 1–2 μm; dislocation substructures including planar slip, dislocation networks, dislocation walls, and Taylor lattices in FCC phase, and planar dislocations in B2 phase
- **Properties**: ultimate tensile strength–mechanical property, yield strength–mechanical property, ductility–mechanical property, work-hardening rate–mechanical property
- **Performance**: High strength (1005 MPa) and ductility (6.2%) at room temperature; three-stage work hardening; ductile fracture in FCC phase and brittle-like fracture in B2 phase
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Bulk casting via medium-frequency induction melting under Ar atmosphere
- effect: Dual-phase lamellar eutectic microstructure composed of FCC (L1₂) phase (60%) and B2 phase (40%), with lamellar width of 1–2 μm
- experiment: XRD, EBSD, and TEM-SAED analysis | X-ray diffraction, Electron Backscatter Diffraction, Transmission Electron Microscopy with Selected Area Electron Diffraction | params: Used to identify crystal structure and phase distribution in as-cast alloy | result: Confirmed presence of ordered FCC (L1₂) and B2 phases with lamellar morphology and 1–2 μm spacing
  - [experimental result] Bulk Al₀.₉CoFeNi₂ alloy was produced by medium-frequency induction melting under Ar atmosphere.
  - [experimental result] XRD pattern shows peaks corresponding to ordered FCC (L1₂) and B2 phases.
  - [image description] EBSD phase mapping confirms a full eutectic cell morphology with alternating lamellae.
  - [image description] TEM-SAED patterns verify the crystal structures of both phases as ordered FCC (L1₂) and B2.
  - [non-referenced_knowledge] Eutectic solidification typically results in lamellar microstructures when two phases nucleate and grow cooperatively.
  - [deductive reasoning] Thus, the casting process leads to the observed lamellar eutectic structure with 60% FCC (L1₂) and 40% B2.
### M2  Structure → Properties
- cause: Dual-phase lamellar eutectic microstructure with FCC (L1₂) (60%, soft and ductile) and B2 (40%, hard and brittle) phases
- effect: Ultimate tensile strength of 1005 MPa and ductility of 6.2% at room temperature
- experiment: Uniaxial tensile test | Tensile test | params: Strain rate of 10⁻³ s⁻¹, gauge dimensions Φ8 mm × 40 mm | result: Yield strength of 559 MPa, ultimate tensile strength of 1005 MPa, and elongation of 6.2%
  - [experimental result] The alloy has a dual-phase lamellar structure with FCC (L1₂) (60%) and B2 (40%).
  - [non-referenced_knowledge] FCC (L1₂) phase is described as soft and ductile, while B2 phase is hard and brittle.
  - [experimental result] Tensile test results show high strength (1005 MPa) and ductility (6.2%).
  - [non-referenced_knowledge] The soft FCC phase deforms plastically, absorbing energy, while the hard B2 phase impedes dislocation motion, increasing strength.
  - [deductive reasoning] The lamellar arrangement ensures effective load transfer between phases, preventing premature failure.
  - [deductive reasoning] Thus, the microstructure directly enables the observed combination of high strength and ductility.
### M3  Structure → Properties
- cause: Dual-phase lamellar eutectic microstructure with FCC (L1₂) and B2 phases
- effect: Three-stage work hardening behavior
- experiment: True stress-strain and hardening rate analysis | Tensile test with dσ/dε calculation | params: Measured true stress and strain hardening rate (dσ/dε) against true strain | result: Three-stage work hardening: rapid drop (I), slight decrease (II), sharp fall (III)
  - [experimental result] The stress-strain curve exhibits three distinct stages of work hardening.
  - [non-referenced_knowledge] FCC (L1₂) phase deforms first and dominates early deformation.
  - [non-referenced_knowledge] B2 phase remains elastic until higher strains, delaying plastic flow.
  - [non-referenced_knowledge] Stage I: Dislocation motion begins in FCC phase only, causing rapid hardening rate drop.
  - [non-referenced_knowledge] Stage II: FCC phase develops complex dislocation configurations (bands, networks), increasing hardening.
  - [non-referenced_knowledge] Stage III: B2 phase begins to deform, but phase boundaries crack, causing strain localization and rapid hardening rate drop.
  - [deductive reasoning] Thus, the phase-specific deformation sequence and interaction create the three-stage work hardening.
### M4  Processing → Structure
- cause: Bulk casting via medium-frequency induction melting under Ar atmosphere
- effect: Formation of dislocation substructures including planar slip, dislocation networks, walls, and Taylor lattices in FCC (L1₂) phase
- experiment: Interrupted tensile tests with TEM | Transmission Electron Microscopy | params: Samples interrupted at 0.6%, 1.5%, and fracture strain; analyzed for dislocation structures | result: FCC phase evolves from planar dislocations → bending dislocations → high-density dislocations → networks → walls → Taylor lattices
  - [experimental result] Alloy was cast via induction melting under Ar atmosphere.
  - [image description] TEM analysis of deformed samples reveals dislocation evolution in FCC (L1₂) phase.
  - [non-referenced_knowledge] Planar slip dominates in FCC phase due to its ordered L1₂ structure and low cross-slip tendency.
  - [non-referenced_knowledge] Dislocation networks and Taylor lattices form as dislocations interact and rearrange under increasing strain.
  - [deductive reasoning] The initial casting process creates the microstructure enabling this dislocation evolution path under load.
### M5  Structure → Properties
- cause: Dislocation substructure evolution in FCC (L1₂) phase (planar slip → networks → Taylor lattices)
- effect: High work-hardening ability and delayed necking
- experiment: Work-hardening rate analysis | Tensile test with dσ/dε measurement | params: True stress and strain hardening rate calculated from stress-strain data | result: High work-hardening rate (446 MPa difference between UTS and yield strength)
  - [image description] FCC (L1₂) phase exhibits dislocation evolution from planar slip to networks and Taylor lattices.
  - [non-referenced_knowledge] Taylor lattices and dislocation walls are known to strongly impede dislocation motion.
  - [experimental result] The work-hardening rate remains high until stage III due to these structures.
  - [non-referenced_knowledge] High work-hardening rate delays necking and increases uniform elongation.
  - [deductive reasoning] Thus, the dislocation substructure evolution directly enables the high work-hardening ability.
### M6  Structure → Performance
- cause: Phase interface between FCC (L1₂) and B2 phases
- effect: Ductile fracture in FCC phase and brittle-like fracture in B2 phase
- experiment: Fracture surface analysis via SEM | Scanning Electron Microscopy | params: Examined fracture surface at low and high magnification after tensile failure | result: Ductile tear ridges in FCC phase; river pattern and cleavage features in B2 phase; voids at phase boundaries
  - [image description] Fracture surface shows elongated grooves and ductile tear edges in FCC phase.
  - [image description] River patterns and micro-cracks are observed in B2 phase, indicating brittle fracture.
  - [image description] Voids nucleate at FCC/B2 phase boundaries due to plasticity mismatch.
  - [non-referenced_knowledge] FCC phase has high dislocation density and mobility, enabling ductile failure.
  - [non-referenced_knowledge] B2 phase has limited dislocation motion, leading to brittle cleavage.
  - [deductive reasoning] Thus, the phase interface controls the fracture mode, resulting in mixed ductile-brittle failure.
### M7  Structure → Properties
- cause: Dislocation pileup at FCC (L1₂)/B2 phase boundaries
- effect: High yield strength of 559 MPa
- experiment: TEM analysis of early deformation | Transmission Electron Microscopy | params: Samples deformed to 0.6% strain analyzed for dislocation behavior | result: Dislocation pileups observed at FCC/B2 interfaces; no dislocations in B2 phase
  - [image description] At 0.6% strain, dislocations are observed in FCC phase but not in B2 phase.
  - [image description] Dislocations pile up at the FCC/B2 interface due to lattice mismatch and B2 phase resistance.
  - [non-referenced_knowledge] Dislocation pileups generate high local back stresses that oppose further slip.
  - [non-referenced_knowledge] Yield strength is determined by the stress required to move dislocations past these barriers.
  - [deductive reasoning] Thus, the dislocation pileups at the phase boundaries are responsible for the high yield strength of 559 MPa.
