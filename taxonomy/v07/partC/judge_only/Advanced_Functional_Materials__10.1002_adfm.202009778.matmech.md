# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202009778 (judge only; not shown to staff)
- material: sodium-ether cointercalated graphite  elements: ['Na', 'C', 'H', 'O']  category: ['Crystalline Material', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Cointercalation of [Na-DEGDME]+ into graphite during discharge process
- **Structure**: Uniform Na deposition on graphite surface with low lattice mismatch
- **Properties**: Na deposition efficiency–electrochemical property
- **Performance**: High Coulombic efficiency and long cycling stability in sodium metal batteries
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Cointercalation of [Na-DEGDME]+ into graphite during discharge process
- effect: Uniform Na deposition on graphite surface with low lattice mismatch
- experiment: DFT calculations for Na plating behavior | Density Functional Theory (DFT) simulations | params: Double stacked [Na-DEGDME]+ intercalated into graphite lattice; adsorption energy calculations for Na atoms | result: Adsorption energy of -1.67 eV indicates energetically favored Na atom adsorption on graphite surface; low lattice mismatch (~4.76%) promotes epitaxial Na growth
  - [experimental result] [Na-DEGDME]+ molecules are intercalated into the graphite lattice during discharge above 0 V vs Na/Na+.
  - [image description] Figure shows SEM images of graphite transitioning from cointercalated to Na-plated states without dendritic growth.
  - [experimental result] DFT calculations reveal a strong adsorption energy (-1.67 eV) of Na atoms on the cointercalated graphite surface.
  - [non-referenced_knowledge] Low lattice mismatch (~4.76%) between Na and cointercalated graphite supports epitaxial growth.
  - [deductive reasoning] Therefore, [Na-DEGDME]+ cointercalation enables uniform Na deposition via strong sodiophilic interactions and reduced lattice strain.
### M2  Structure → Performance
- cause: Uniform Na deposition on graphite surface with low lattice mismatch
- effect: High Coulombic efficiency and long cycling stability in sodium metal batteries
- experiment: Galvanostatic plating-stripping tests | Electrochemical cycling measurements | params: Current densities: 1–5 mA cm⁻²; Area capacity: 1–5 mAh cm⁻² | result: Graphite electrode exhibits 99.86% average Na deposition efficiency over 900 cycles; stable voltage profiles with low overpotential (<25 mV)
  - [image description] Graphite electrodes exhibit dendrite-free Na deposition under varying current densities, as shown by SEM.
  - [experimental result] XPS analysis confirms stable SEI rich in NaF and RCH₂ONa components on graphite, contributing to high CE.
  - [non-referenced_knowledge] A uniform Na deposition morphology reduces local current density hotspots and prevents dendritic failure modes.
  - [deductive reasoning] Thus, the combination of uniform Na growth and stable SEI ensures high Coulombic efficiency (>99.86%) and 900-cycle stability.
### M3  Processing → Performance
- cause: Cointercalation of [Na-DEGDME]+ into graphite during discharge process
- effect: High Coulombic efficiency and long cycling stability in sodium metal batteries
- experiment: Full cell performance testing | Galvanostatic cycling of full cells | params: Graphite anode predeposited with 0.5 mAh cm⁻² Na paired with Na₄Fe₃(PO₄)₂(P₂O₇) cathode | result: Full cell retains 91% of initial capacity after 300 cycles at 0.75 mA cm⁻²; delivers 95 mAh g⁻¹ based on cathode mass
  - [experimental result] Cointercalation occurs prior to Na deposition and establishes favorable nucleation sites on graphite.
  - [image description] Full cell tests demonstrate 91% capacity retention after 300 cycles using predeposited Na-graphite anodes.
  - [non-referenced_knowledge] Controlled cointercalation improves reversibility by minimizing side reactions and dendrite formation.
  - [inductive reasoning] Hence, the cointercalation step during processing is essential for achieving high-performance full cells with long-term stability.
