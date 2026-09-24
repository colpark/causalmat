# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116828 (judge only; not shown to staff)
- material: Fe-0.2C binary alloy  elements: ['Fe', 'C']  category: ['Metals and Alloys', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Cold-rolling, austenitization at 900°C, ice-brine quenching, sub-zero cooling in liquid nitrogen, hydrogen charging
- **Structure**: Fully martensitic structure with prior austenite grain boundaries
- **Properties**: tensile strength–mechanical property, hydrogen content–chemical property
- **Performance**: Hydrogen-related fracture behavior, intergranular and quasi-cleavage cracking
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Cold-rolling, austenitization at 900°C, ice-brine quenching, sub-zero cooling in liquid nitrogen
- effect: Fe-0.2C binary alloy exhibits a fully martensitic structure with prior austenite grain boundaries
- experiment: Microstructural characterization | EBSD | params: Mid-thickness section analysis of tensile-tested specimens | result: Martensitic structure confirmed with distinct lath, block, packet, and prior austenite grain boundaries
  - [experimental result] Specimens were cold-rolled, austenitized at 900°C, then quenched and cooled in liquid nitrogen to produce martensite.
  - [image description] EBSD orientation maps reveal hierarchical martensitic microstructure with lath, block, packet, and prior austenite grain boundaries.
  - [non-referenced_knowledge] Martensitic transformation during quenching forms hierarchical microstructures including lath, block, packet, and prior austenite grains.
  - [deductive reasoning] Thus, the combination of thermal and mechanical processing leads to formation of fully martensitic microstructure with characteristic boundaries.
### M2  Structure → Property
- cause: Fully martensitic structure with prior austenite grain boundaries
- effect: High tensile strength but susceptibility to hydrogen embrittlement
- experiment: Tensile testing and fractography | Slow strain rate tensile test | params: Hydrogen charging levels: 0.41 mass ppm and 2.21 mass ppm; stress concentration factors: 2.1 and 3.2 | result: High-strength steel exhibited hydrogen-related intergranular fracture at high hydrogen content (2.21 mass ppm)
  - [non-referenced_knowledge] Fe-0.2C alloy was processed to have a fully martensitic microstructure with defined prior austenite grain boundaries.
  - [image description] Intergranular fracture surfaces were observed along prior austenite grain boundaries in SEM analysis.
  - [referenced knowledge] Prior austenite grain boundaries are known to be susceptible to hydrogen-induced decohesion.
  - [inductive reasoning] Therefore, the martensitic structure contributes to high tensile strength but increases vulnerability to hydrogen embrittlement via intergranular cracking.
### M3  Property → Performance
- cause: High tensile strength and hydrogen content
- effect: Hydrogen-related intergranular fracture behavior
- experiment: Finite element simulation | Stress-strain-hydrogen distribution modeling | params: Measured hydrogen contents (0.41 and 2.21 mass ppm), stress concentration factors (2.1 and 3.2) | result: Crack initiation occurred at regions of high principal stress and elevated local hydrogen content near notch root
  - [experimental result] Hydrogen charging at 1 A m⁻² yielded 2.21 mass ppm hydrogen content associated with brittle fracture behavior.
  - [image description] FE simulations showed high local stress and hydrogen concentration at crack initiation sites ahead of notch root.
  - [referenced knowledge] Hydrogen reduces cohesive energy at grain boundaries leading to intergranular failure.
  - [non-referenced_knowledge] Intergranular fracture is stress-controlled decohesion at prior austenite grain boundaries.
  - [deductive reasoning] Therefore, high hydrogen content and localized stress synergistically induce intergranular fracture via decohesion at prior austenite grain boundaries.
### M4  Property → Performance
- cause: Local plastic strain and moderate hydrogen content
- effect: Quasi-cleavage fracture along {011} planes
- experiment: Digital image correlation (DIC) | Surface strain mapping | params: Plastic strain distribution before and after tensile deformation | result: Enhanced local plastic deformation observed at notch root surface where quasi-cleavage cracks initiated
  - [experimental result] Hydrogen charging at 0.625 A m⁻² yielded 0.41 mass ppm hydrogen content associated with quasi-cleavage fracture.
  - [image description] DIC analysis revealed enhanced plastic strain localized along {011} planes at notch root surface.
  - [referenced knowledge] Hydrogen enhances localized plasticity (HELP effect) promoting cleavage-like fracture.
  - [non-referenced_knowledge] Quasi-cleavage fracture occurs on {011} planes due to localized plastic deformation and hydrogen-assisted void coalescence.
  - [deductive reasoning] Therefore, moderate hydrogen content and localized plastic strain synergistically lead to quasi-cleavage fracture along {011} planes.
