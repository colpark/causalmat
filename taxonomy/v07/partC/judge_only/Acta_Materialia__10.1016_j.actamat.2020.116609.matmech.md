# MatMech content for Acta_Materialia/10.1016_j.actamat.2020.116609 (judge only; not shown to staff)
- material: Al/X (X = Ti, Mg, Cu) nanostructured metallic multilayers (NMMs)  elements: ['Al', 'Ti', 'Mg', 'Cu']  category: ['Metals and Alloys', 'Nanomaterial', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: DC magnetron sputtering with individual layer thickness of ~3 nm
- **Structure**: Periodic nanostructured multilayers with semi-coherent interfaces
- **Properties**: tribocorrosion resistance–mechanical property, hardness–mechanical property, elastic modulus–mechanical property
- **Performance**: Ultrahigh tribocorrosion resistance in 0.6 M NaCl aqueous solution
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: DC magnetron sputtering with individual layer thickness of ~3 nm
- effect: Periodic nanostructured multilayers with semi-coherent interfaces
- experiment: TEM analysis of NMM structure | Transmission electron microscopy | params: Cross-sectional imaging of Al/X multilayers | result: Semi-coherent interfaces observed between Al and Ti layers with specific orientation relationships; coherent interfaces in Al/Mg; semi-coherent in Al/Cu
  - [experimental result] Al/X multilayers were deposited using DC magnetron sputtering under controlled conditions
  - [image description] Bright-field TEM images show semi-coherent interfaces between Al and Ti layers with specific orientation relationships
  - [non-referenced_knowledge] Layer thickness governs mechanical properties in multilayer systems
  - [deductive reasoning] Given equal layer thickness across samples, interface coherency differences arise from material combinations
### M2  Structure → Property
- cause: Periodic nanostructured multilayers with semi-coherent interfaces
- effect: Increased hardness (3-5× rule-of-mixture values)
- experiment: Nanoindentation tests | Mechanical testing | params: Berkovich tip, 4-5 mN maximum load | result: Hardness of all NMMs is ~3–5 times greater than corresponding rule-of-mixture hardness
  - [experimental result] Nanoindentation tests showed hardness of all NMMs is ~3–5 times greater than corresponding rule-of-mixture hardness
  - [image description] SEM images of indents showed no surface cracks or apparent pile-up indicating high strain hardening
  - [referenced knowledge] Multilayer architectures enhance mechanical properties through interface-mediated strengthening mechanisms
  - [non-referenced_knowledge] Dislocation pile-up at interfaces contributes to strength enhancement in multilayer materials
  - [deductive reasoning] Therefore, the periodic nanostructured multilayer design with semi-coherent interfaces impedes dislocation motion, leading to significant increases in hardness
### M3  Structure → Property
- cause: Periodic nanostructured multilayers with semi-coherent interfaces
- effect: Reduced surface reactivity and pitting susceptibility
- experiment: DFT calculations of surface properties | Computational modeling | params: Work function, oxygen and chloride adsorption energies on Al(111) and Al/Ti NMM surfaces | result: Al/Ti NMM has higher work function (4.19 eV vs 4.04 eV for pure Al) and reduced Cl adsorption energy (-1.72 eV vs -1.85 eV for pure Al)
  - [experimental result] DFT calculations showed Al/Ti NMM has higher work function (4.19 eV) than pure Al (4.04 eV)
  - [experimental result] Calculated Cl adsorption energy was lower on Al/Ti (-1.72 eV) than on pure Al (-1.85 eV)
  - [non-referenced_knowledge] Higher work function indicates reduced electron availability for corrosion reactions
  - [referenced knowledge] Surface work function correlates with corrosion resistance
  - [deductive reasoning] Thus, the nanolayered structure in Al/Ti multilayers increases the surface work function while reducing chloride ion adsorption, decreasing surface reactivity
### M4  Property → Performance
- cause: Increased hardness and reduced surface reactivity
- effect: Ultrahigh tribocorrosion resistance in 0.6 M NaCl aqueous solution
- experiment: Tribocorrosion tests | Combined mechanical/electrochemical testing | params: Reciprocating sliding against Al2O3 ball under 0.47 GPa contact pressure in 0.6 M NaCl solution | result: Al/Cu NMM showed best wear resistance; Al/Ti NMM showed highest corrosion resistance; overall best tribocorrosion performance from synergistic effects of both properties
  - [experimental result] Tribocorrosion tests showed Al/Cu NMM had best wear resistance while Al/Ti NMM had highest corrosion resistance
  - [experimental result] FE simulations confirmed galvanic corrosion dominates material loss in NMMs
  - [experimental result] DFT calculations showed Al/Ti multilayers have increased work function and reduced Cl adsorption
  - [non-referenced_knowledge] Tribocorrosion involves synergistic effects of mechanical wear and electrochemical degradation
  - [referenced knowledge] Mixed potential theory explains galvanic corrosion behavior in multilayer systems
  - [deductive reasoning] Therefore, the enhanced hardness resists mechanical wear while reduced surface reactivity minimizes corrosion damage, providing ultrahigh tribocorrosion resistance
