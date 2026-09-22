# MatMech content for Journal_of_Magnesium_and_Alloys/j.jma.2020.09.028 (judge only; not shown to staff)
- material: AZ31 Mg  elements: ['Mg', 'Al', 'Zn']  category: ['Metals and Alloys', 'Crystalline Material', 'Nanomaterial']
- MST chain: Processing → Structure → Properties
## Tetrahedron elements
- **Processing**: Solution treatment at 410°C for 8 h, aging at 180°C for 14 h, compression along TD at 10⁻³ s⁻¹ (8% and 13% strain), and annealing at 250°C for 30 min
- **Structure**: Precipitate orientation altered from basal plates (parallel to (0002)ₐ) to prismatic plates (parallel to {101̄0}ₐ); grain refinement due to twinning; twin boundaries eliminated after annealing
- **Properties**: Compressive yield strength–mechanical property, compression ratio–mechanical property
- **Performance**: Improved strength and ductility in compression due to enhanced basal slip resistance and activation of non-basal slip systems
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Aging prior to twinning deformation (solution treatment at 410°C for 8 h, aging at 180°C for 14 h, compression along TD at 10⁻³ s⁻¹ with 13% strain, and annealing at 250°C for 30 min)
- effect: Precipitate orientation altered from basal plates (parallel to (0002)ₐ) to prismatic plates (parallel to {101̄0}ₐ), accompanied by grain refinement due to twinning and elimination of twin boundaries after annealing
- experiment: Microstructural characterization via BSEM and TEM | BSEM, TEM | params: Aged at 180°C for 14 h, compressed at 13% strain along TD, annealed at 250°C for 30 min | result: TEM images show plate-shaped Mg₁₇Al₁₂ precipitates with broad faces parallel to {101̄0}ₐ prismatic planes; BSEM shows grain refinement from ~21.7 μm to ~11.85 μm after 13% compression
  - [experimental result] AZ31 alloy was solution treated at 410°C for 8 h and aged at 180°C for 14 h, forming Mg₁₇Al₁₂ precipitates with habit planes parallel to (0002)ₐ basal planes.
  - [experimental result] Compression along TD at 13% strain activated {101̄2} extension twins, reorienting the c-axis of grains from //ND to //TD.
  - [image description] TEM images show precipitates viewed along [101̄0]ₐ appear as plates and along [0001]ₐ as laths, confirming alignment with prismatic planes.
  - [non-referenced_knowledge] During twinning, precipitates undergo only a small rotation (<4°), preserving their orientation relative to the reoriented matrix lattice.
  - [experimental result] Twin boundaries act as barriers to grain growth, refining the average grain size from ~21.7 μm to ~11.85 μm.
  - [deductive reasoning] Thus, aging before twinning deformation alters precipitate orientation from basal to prismatic and refines grain structure.
### M2  Structure → Properties
- cause: Prismatic plates aligned with {101̄0}ₐ planes and refined grain size
- effect: Compressive yield strength (CYS) increased by ~40 MPa and compression ratio increased by 22% compared to basal plates
- experiment: Compression tests at RT with strain rate of 1×10⁻³ s⁻¹ | Compression test | params: Samples A-45°, AC-45°, ACA-45° machined at 45° to ND to eliminate texture effects | result: CYS increased from 75 MPa (A-45°) to 115 MPa (AC-45°); compression ratio rose from 23% to 28%
  - [experimental result] TEM and EBSD confirm prismatic plates are aligned with {101̄0}ₐ planes, while basal plates are aligned with (0002)ₐ.
  - [deductive reasoning] Orowan model calculations show Δτ for basal slip is 59.67 MPa for prismatic plates vs. 40.87 MPa for basal plates.
  - [deductive reasoning] Hall-Petch equation predicts grain refinement from 21.7 μm to 11.85 μm contributes ~12 MPa additional strengthening.
  - [experimental result] Measured CYS of AC-45° is 115 MPa, 40 MPa higher than A-45° (75 MPa), consistent with combined precipitation and grain boundary strengthening.
  - [experimental result] CRSS for prismatic slip is 126.91 MPa with prismatic plates vs. 127.68 MPa with basal plates, reducing τ_prism/τ_basal from 2.78 to 1.96.
  - [referenced knowledge] A τ_prism/τ_basal ratio < 2.5 promotes prismatic slip activation at RT, enhancing ductility.
  - [image description] More microvoids observed in ACA-45° fracture surface confirm enhanced ductility due to non-basal slip activation.
  - [deductive reasoning] Thus, prismatic plates and refined grains increase CYS, while reduced CRSS ratio enables ductility improvement.
### M3  Processing → Properties
- cause: Aging prior to twinning deformation (solution treatment, aging, compression, annealing)
- effect: Simultaneous improvement in compressive yield strength (CYS) and compression ratio (ductility)
- experiment: Compression tests comparing A-45°, AC-45°, and ACA-45° | Compression test | params: All samples tested at 45° to ND to eliminate texture influence; strain rate 1×10⁻³ s⁻¹ | result: AC-45° (prismatic plates + refined grains) shows highest CYS (115 MPa) and highest compression ratio (28%); ACA-45° (prismatic plates, no twins) has lower CYS (96 MPa) but same ductility as A-45° (23%)
  - [experimental result] Processing includes aging to form precipitates, then compression to induce twinning and grain refinement, followed by annealing to remove dislocations but retain precipitate orientation.
  - [deductive reasoning] Prismatic plates increase Δτ for basal slip by ~20 MPa compared to basal plates.
  - [deductive reasoning] Grain refinement from 21.7 μm to 11.85 μm adds ~12 MPa to CYS via Hall-Petch effect.
  - [experimental result] CRSS ratio τ_prism/τ_basal decreases from 2.78 to 1.96 with prismatic plates, promoting prismatic slip activation.
  - [non-referenced_knowledge] Activation of prismatic slip provides additional dislocation mobility, reducing deformation resistance during late-stage plasticity.
  - [deductive reasoning] Thus, the combined effect of enhanced basal slip resistance and activated non-basal slip systems improves both strength and ductility.
