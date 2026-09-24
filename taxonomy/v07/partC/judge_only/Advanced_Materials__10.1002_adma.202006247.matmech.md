# MatMech content for Advanced_Materials/10.1002_adma.202006247 (judge only; not shown to staff)
- material: 3D g-C3N4/Graphene/g-C3N4  elements: ['C', 'N', 'H', 'O']  category: ['Nanomaterial', 'Composite Material', 'Ceramic', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: In situ calcination of dicyandiamide-coated graphene oxide to form 3D g-C3N4/Graphene/g-C3N4 sandwiched nanosheets
- **Structure**: Insulator–metal–insulator layered heterostructure with van der Waals gap between graphene and g-C3N4
- **Properties**: Coulombic efficiency–electrochemical property, structural stability–mechanical property
- **Performance**: Stable cycling of Li metal anodes with high Coulombic efficiency and dendrite-free Li deposition
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: In situ calcination of dicyandiamide-coated graphene oxide to form 3D g-C3N4/Graphene/g-C3N4 sandwiched nanosheets
- effect: Formation of insulator–metal–insulator layered heterostructure with van der Waals gap between graphene and g-C3N4
- experiment: Synthesis and structural characterization of 3D g-C3N4/Graphene/g-C3N4 | XRD, SEM, TEM | params: Dicyandiamide coating on graphene oxide followed by in situ calcination | result: Characteristic XRD peak at 12° (g-C3N4 (100) plane), fluffy porous structure with multi-layer nanosheets observed via SEM/TEM
  - [experimental result] Zeta potential changes indicate successful adsorption of dicyandiamide molecules onto GO sheets during self-assembly.
  - [image description] SEM/EDS confirm uniform coating of dicyandiamide on 3D GO before calcination.
  - [referenced knowledge] Oxygen-containing functional groups on GO interact favorably with amine groups in dicyandiamide.
  - [non-referenced_knowledge] During calcination, dicyandiamide decomposes to form g-C3N4 while maintaining structural integrity on reduced GO.
  - [deductive reasoning] The resulting 3D architecture consists of g-C3N4/graphene/g-C3N4 layers separated by van der Waals gaps.
### M2  Structure → Property
- cause: Insulator–metal–insulator layered heterostructure with van der Waals gap between graphene and g-C3N4
- effect: High Coulombic efficiency and structural stability of Li metal anodes
- experiment: Li plating/stripping performance evaluation | Cycling test, EIS | params: Current density: 1.0 mA cm⁻², Capacity: 1.0 mAh cm⁻² | result: Average CE of 99.1% over 500 cycles, stable SEI resistance and charge transfer resistance
  - [experimental result] AES depth profiling shows N content increases from 8.91 to 17.10 at.% after Li deposition, confirming SEI composition.
  - [image description] Cryo-TEM images demonstrate conformal Li deposition beneath g-C3N4 without dendritic structures.
  - [referenced knowledge] Nitrogen atoms in g-C3N4 exhibit strong Li adsorption and facilitate small amounts of Li₃N formation.
  - [non-referenced_knowledge] Uniform nanopore channels in g-C3N4 regulate Li⁺ flux and prevent localized current hotspots.
  - [deductive reasoning] Thus, the heterostructure guides homogeneous Li deposition and maintains structural integrity during repeated cycling.
### M3  Property → Performance
- cause: Coulombic efficiency–electrochemical property, structural stability–mechanical property
- effect: Stable cycling of Li metal anodes with high Coulombic efficiency and dendrite-free Li deposition
- experiment: Full-cell testing under practical conditions | Galvanostatic cycling | params: Cathode loading: 3.5 mAh cm⁻², Electrolyte: 6.4 μL mAh⁻¹, N/P ratio: 0.43 | result: Stable cycling over 180 cycles with 99.89% average CE and 92.2% capacity retention
  - [experimental result] EIS measurements show stable Rsei and Rct values for 3D g-C3N4 electrodes during cycling.
  - [image description] Voltage polarization remains low throughout prolonged cycling, as shown in full-cell voltage profiles.
  - [referenced knowledge] Suppressed SEI decomposition leads to higher Coulombic efficiency and longer cycle life.
  - [non-referenced_knowledge] 3D porous architecture accommodates volume expansion and reduces local current density.
  - [deductive reasoning] Therefore, the combination of high efficiency and structural adaptability enables stable full-cell operation under lean electrolyte and limited Li conditions.
