# MatMech content for Journal_of_Magnesium_and_Alloys/j.jma.2020.09.027 (judge only; not shown to staff)
- material: Mg90Ce5Y5  elements: ['Mg', 'Ce', 'Y', 'C', 'Co']  category: ['Metals and Alloys', 'Nanomaterial', 'Composite Material']
- MST chain: Processing → Structure → Property
## Tetrahedron elements
- **Processing**: High-temperature carbonization reaction to synthesize C@Co composites, followed by mechanical ball-milling of Mg90Ce5Y5 alloy with 10 wt.% C@Co composites under argon atmosphere
- **Structure**: C nanosheets with high defect density and uniformly dispersed Co nanoparticles (size <50 nm); grain refinement and amorphization of Mg90Ce5Y5 alloy particles; formation of mesoporous structure (pore diameter ~3.88 nm)
- **Properties**: dehydrogenation activation energy–kinetic property, hydrogen absorption capacity–thermodynamic property, hydrogen desorption time–kinetic property
- **Performance**: Full activation in first hydrogenation cycle; hydrogen desorption time reduced from 150 min to 11 min at 300°C; lowered initial dehydrogenation temperature from 341.0°C to 267.0°C
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: High-temperature carbonization reaction of Co(NO3)3·6H2O and PVP under argon atmosphere at 800°C
- effect: Formation of C nanosheets with high defect density and uniformly dispersed Co nanoparticles (<50 nm) with a mesoporous structure (pore diameter ~3.88 nm)
- experiment: Synthesis of C@Co composites | Thermal carbonization | params: 800°C, 2 hours, argon atmosphere, Co(NO3)3·6H2O and PVP precursors | result: C@Co composites with Co nanoparticles on carbon nanosheets and mesoporous structure
  - [experimental result] Co(NO3)3·6H2O and PVP were dissolved in water and dried, then heated to 800°C under argon.
  - [experimental result] XRD confirms the presence of C and Co phases in the product.
  - [experimental result] Raman spectra show D and G bands with ID/IG = 0.97, indicating high defect density in carbon.
  - [experimental result] Nitrogen adsorption-desorption isotherms reveal a BET surface area of 186.4 m²/g and mesopores of 3.88 nm.
  - [image description] SEM and TEM show Co nanoparticles (<50 nm) uniformly distributed on C nanosheets with graphitic layers.
  - [non-referenced_knowledge] Defects in carbon and nanoparticle dispersion enhance catalytic active sites.
  - [deductive reasoning] Thus, carbonization produces a mesoporous C@Co structure with high defect density and uniform Co distribution.
### M2  Processing → Structure
- cause: Mechanical ball-milling of Mg90Ce5Y5 alloy with 10 wt.% C@Co composites at 300 rpm for 5 h under argon
- effect: Grain refinement and amorphization of Mg90Ce5Y5 alloy particles; reduced particle size; C nanosheets and Co nanoparticles dispersed on alloy surfaces
- experiment: Ball-milling of Mg90Ce5Y5 + C@Co | Mechanical milling | params: 5 h, 300 rpm, ball-to-powder ratio 40:1, argon atmosphere | result: Particle size reduction and amorphization observed; C and Co distributed on alloy surfaces
  - [experimental result] Mg90Ce5Y5 alloy powder was ball-milled with 10 wt.% C@Co composites for 5 h under argon.
  - [experimental result] XRD shows broadened peaks in C10 alloy, indicating grain refinement and amorphization.
  - [image description] SEM reveals C10 particles are smaller and irregular compared to C0 particles.
  - [image description] EDS mapping confirms C and Co are distributed on Mg alloy particles.
  - [non-referenced_knowledge] Ball-milling reduces particle size and increases surface area and defect density.
  - [deductive reasoning] Thus, ball-milling creates a fine-grained, defect-rich microstructure with homogeneous catalyst dispersion.
### M3  Structure → Property
- cause: High defect density in C nanosheets and dispersed Co nanoparticles in C@Co composites
- effect: Reduction of dehydrogenation activation energy from 130.3 to 81.9 kJ mol⁻¹ H₂
- experiment: Dehydrogenation kinetics and activation energy measurement | Arrhenius analysis | params: Dehydrogenation at 280–360°C, fitted using Arrhenius equation | result: Activation energy decreased from 130.3 to 81.9 kJ mol⁻¹ H₂ with C@Co addition
  - [experimental result] C@Co composites contain carbon nanosheets with high defect density (ID/IG = 0.97).
  - [image description] Co nanoparticles are uniformly dispersed and <50 nm in size.
  - [referenced knowledge] Defects in carbon act as active sites for nucleation of Mg/MgH2 phase.
  - [referenced knowledge] Co nanoparticles promote recombination of hydrogen atoms during desorption.
  - [non-referenced_knowledge] The synergistic effect of C and Co reduces the energy barrier for dehydrogenation.
  - [experimental result] Arrhenius analysis confirms activation energy dropped from 130.3 to 81.9 kJ mol⁻¹ H₂.
  - [deductive reasoning] Thus, defect density and Co nanoparticles directly reduce the activation energy.
### M4  Structure → Property
- cause: Mesoporous structure (3.88 nm pores) and carbon nanosheets embedded in Mg alloy
- effect: Improved hydrogen diffusion rate and reduced hydrogen desorption time from 150 min to 11 min at 300°C
- experiment: Isothermal dehydrogenation kinetics | Sieverts-type apparatus | params: 300°C, initial pressure 0.005 MPa, sample mass 0.5 g | result: Desorption time reduced from 150 min (C0) to 11 min (C10)
  - [experimental result] C@Co composites have mesoporous structure with dominant pore size of 3.88 nm.
  - [image description] TEM shows carbon layers adhered to alloy particles.
  - [referenced knowledge] Carbon nanosheets provide channels for hydrogen diffusion in MgH2 matrix.
  - [non-referenced_knowledge] Hydrogen desorption kinetics are limited by diffusion in MgH2.
  - [experimental result] Dehydrogenation time drops from 150 min to 11 min with C@Co addition.
  - [deductive reasoning] Thus, mesopores and carbon sheets enhance hydrogen diffusion, reducing desorption time.
### M5  Structure → Property
- cause: High defect density of C nanosheets and presence of Co nanoparticles
- effect: Change in rate-limiting step of dehydrogenation from surface-controlled to random nucleation and growth
- experiment: Johnson-Mehl-Avrami (JMA) kinetics analysis | JMA fitting of desorption curves | params: Fitting of ln[−ln(1−α)] vs. ln(t) for C0 and C10 at multiple temperatures | result: Avrami index η decreased from 1.59 to 1.32, indicating mechanism shift
  - [experimental result] JMA analysis of dehydrogenation curves yields Avrami index η = 1.59 for C0.
  - [experimental result] η decreases to 1.32 for C10 after adding C@Co.
  - [referenced knowledge] η ~1.5 indicates nucleation and growth mechanism; η ~3–4 indicates surface control.
  - [non-referenced_knowledge] Defects in C nanosheets promote Mg phase nucleation.
  - [non-referenced_knowledge] Co nanoparticles enhance H atom recombination, reducing surface control.
  - [deductive reasoning] Thus, C@Co shifts rate-limiting step from surface-controlled to nucleation-controlled.
### M6  Structure → Performance
- cause: C nanosheets with high defect density and Co nanoparticles in C@Co composites
- effect: Full activation of Mg90Ce5Y5 alloy in first hydrogenation cycle
- experiment: Activation hydrogenation cycles | Sieverts-type hydrogenation cycling | params: 360°C, 3 cycles, monitoring hydrogen uptake | result: C0 requires 3 cycles for full activation; C10 fully activated in 1st cycle
  - [experimental result] C10 alloy achieves full hydrogen absorption capacity in the first cycle.
  - [experimental result] C0 alloy requires three cycles to fully activate.
  - [non-referenced_knowledge] Carbon layers wrap alloy particles and inhibit oxidation and sintering during heating.
  - [deductive reasoning] This protection allows immediate and complete hydrogenation in the first cycle.
### M7  Structure → Performance
- cause: Reduced particle size and enhanced catalytic sites from C@Co composites
- effect: Lowered initial dehydrogenation temperature from 341.0°C to 267.0°C
- experiment: Differential Scanning Calorimetry (DSC) | DSC analysis | params: Heating rate 5°C/min, argon flow 100 mL/min | result: Initial dehydrogenation temperature decreased from 341.0°C to 267.0°C
  - [experimental result] DSC shows initial dehydrogenation temperature for C0 is 341.0°C.
  - [experimental result] For C10, initial dehydrogenation temperature is 267.0°C.
  - [non-referenced_knowledge] C@Co composites provide catalytic sites that lower the energy barrier for MgH2 decomposition.
  - [deductive reasoning] Thus, the onset temperature of dehydrogenation is significantly reduced by catalytic action.
