# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202008088 (judge only; not shown to staff)
- material: MAPbI3  elements: ['C', 'H', 'N', 'Pb', 'I']  category: ['Ceramic', 'Coatings and Thin Films', 'Crystalline Material', 'Nanomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Spin-coating, temperature-gradient-assisted solidification, inverse temperature crystallization
- **Structure**: Polycrystalline (PC), highly oriented crystalline (HOC), single-crystalline (SC) structures with varying domain sizes
- **Properties**: Photoluminescence (PL) behavior–optical property
- **Performance**: Phase-transition behavior and photoluminescence in optoelectronic applications
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Spin-coating, temperature-gradient-assisted solidification, and inverse temperature crystallization
- effect: Polycrystalline (PC), highly oriented crystalline (HOC), and single-crystalline (SC) structures with varying domain sizes are formed
- experiment: Sample Preparation Using Different Processing Techniques | Materials Processing | params: Spin-coating at 4000 rpm for PC films; temperature gradient annealing at 85°C for HOC films; inverse temperature crystallization at 110°C for SC crystals | result: Distinct domain sizes: <200 nm (PC), ~70 µm (HOC), >1000 µm (SC)
  - [experimental result] Spin-coated PC films form rapidly under solvent evaporation, limiting grain growth to <200 nm
  - [experimental result] Temperature-gradient-assisted solidification allows directional crystal growth, producing larger (~70 µm) HOC domains
  - [experimental result] Inverse temperature crystallization enables slow, controlled cooling that supports millimeter-scale SC formation
  - [image description] Figure shows SEM images and domain size histograms confirming structural differences among PC, HOC, and SC samples
  - [referenced knowledge] Literature confirms that growth kinetics and thermodynamics govern final crystallinity and domain size
  - [deductive reasoning] Therefore, processing directly determines the structural configuration through control over nucleation and growth mechanisms
### M2  Structure → Property
- cause: Polycrystalline (PC), highly oriented crystalline (HOC), and single-crystalline (SC) structures with varying domain sizes
- effect: Distinct photoluminescence (PL) behavior including dual peaks in PC and single peak in SC
- experiment: TDPL and PDPL Spectroscopy | Optical Characterization | params: Temperature range from 80 K to 300 K, excitation wavelengths of 325, 473, and 633 nm | result: PC exhibits dual PL peaks below 150 K, while SC shows a single peak; grinding reduces spectral differences
  - [experimental result] PC films exhibit dual PL peaks at low temperatures, indicating phase coexistence
  - [experimental result] SC samples display a single PL peak corresponding to orthorhombic phase below 150 K
  - [experimental result] Grinding releases inter-domain stress, aligning all samples to tetragonal phase PL characteristics
  - [image description] Contour maps confirm structural dependence of PL emission patterns
  - [non-referenced_knowledge] Volume expansion during phase transition generates residual stress affecting band structure
  - [inductive reasoning] Thus, domain size dictates residual stress magnitude, which modulates phase stability and optical response
### M3  Property → Performance
- cause: Photoluminescence (PL) behavior–optical property
- effect: Phase-transition characteristics influencing optoelectronic device performance
- experiment: Temperature-dependent XRD and Raman spectroscopy | Structural and Vibrational Analysis | params: XRD from 80–300 K, Raman spectra from 80–300 cm⁻¹ | result: Phase transitions correlate with PL behavior; SC shows abrupt transition, PC shows gradual transformation
  - [experimental result] XRD shows SC undergoes sharp phase transition at ~150 K, consistent with abrupt PL shift
  - [experimental result] PC films exhibit broad phase transitions across temperature range, correlating with dual PL peaks
  - [experimental result] Raman spectra confirm lattice rearrangements during phase transition
  - [image description] XRD peak shifts and FWHM changes indicate residual strain evolution during phase transition
  - [non-referenced_knowledge] Residual stress modifies electronic structure and carrier lifetime, affecting device performance
  - [deductive reasoning] Therefore, PL behavior serves as an indicator of phase stability and stress state, which are critical for optoelectronic performance
### M4  Structure → Performance
- cause: Polycrystalline (PC), highly oriented crystalline (HOC), and single-crystalline (SC) structures with varying domain sizes
- effect: Phase-transition behavior and photoluminescence in optoelectronic applications
- experiment: Thermal Cycling and Aging Studies | Stability Testing | params: Atmospheric exposure duration from fresh to 3-month aged samples | result: Surface degradation and increased dual PL emission in aged SC samples
  - [experimental result] SC samples exhibit abrupt phase transition with high residual stress, leading to macroscopic cracks
  - [experimental result] Aged SC samples show surface degradation and emergence of dual PL emission similar to PC films
  - [image description] Contour maps reveal surface-core PL differences in aged SC samples
  - [non-referenced_knowledge] Volume expansion during phase transition causes residual stress proportional to domain size
  - [inductive reasoning] Higher residual stress in large domains accelerates degradation and alters optoelectronic performance
