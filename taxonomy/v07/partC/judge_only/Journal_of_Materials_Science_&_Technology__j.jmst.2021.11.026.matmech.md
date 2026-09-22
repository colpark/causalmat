# MatMech content for Journal_of_Materials_Science_&_Technology/j.jmst.2021.11.026 (judge only; not shown to staff)
- material: Ti₃C₂Tₓ @ MoS₂  elements: ['Ti', 'C', 'Mo', 'S', 'H', 'O', 'F']  category: ['Nanomaterial', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: One-step hydrothermal method at 210 °C for 18 h to synthesize Ti₃C₂Tₓ @ MoS₂ heterostructure composites; followed by dispersion in water and incorporation into waterborne epoxy resin via spraying to form composite coatings
- **Structure**: Hierarchical 2D structure with MoS₂ nanosheets vertically anchored on Ti₃C₂Tₓ nanosheets; suppression of Ti₃C₂Tₓ restacking; van der Waals-dominated interface with optimized stacking configurations (e.g., Configuration VI)
- **Properties**: Low-frequency impedance modulus–electrical property, coating resistance–electrical property, wear rate–mechanical property, binding energy–thermodynamic property, work function–electronic property
- **Performance**: Enhanced corrosion protection and antiwear performance of epoxy coating with 0.1 wt.% Ti₃C₂Tₓ @ MoS₂; 50% reduction in wear rate compared to pure epoxy; largest |Z|₀.₀₁ Hz and R_c values during 9-day saltwater immersion
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: One-step hydrothermal method at 210 °C for 18 h with Na₂MoO₄·2H₂O, thiourea, and citric acid in the presence of few-layer Ti₃C₂Tₓ nanosheets
- effect: Hierarchical 2D structure formed with MoS₂ nanosheets vertically anchored on Ti₃C₂Tₓ nanosheets, preventing restacking of MXene
- experiment: Hydrothermal synthesis of Ti₃C₂Tₓ @ MoS₂ | Hydrothermal synthesis | params: 210 °C for 18 h, 0.12 g Ti₃C₂Tₓ, 0.7 g Na₂MoO₄·2H₂O, 1.5 g thiourea, 0.09 g citric acid in 22 mL water | result: Formation of hierarchical 2D heterostructure with MoS₂ anchored on Ti₃C₂Tₓ
  - [non-referenced_knowledge] Ti₃C₂Tₓ nanosheets are negatively charged and act as hosts for Mo⁶⁺ ions.
  - [experimental result] Na₂MoO₄ and thiourea under hydrothermal conditions react to form MoS₂ via nucleation and growth.
  - [image description] SEM images show MoS₂ nanosheets uniformly anchored on Ti₃C₂Tₓ surfaces, forming a hierarchical 2D structure.
  - [deductive reasoning] The hierarchical structure prevents Ti₃C₂Tₓ nanosheets from restacking by spatial separation.
### M2  Structure → Property
- cause: Van der Waals-dominated interface between Ti₃C₂Tₓ and MoS₂ with Configuration VI stacking (S above Ti(1), Mo above T and C(1))
- effect: High binding energy (E_B < -1.0 eV) and favorable charge redistribution at the interface, enhancing thermodynamic stability and electronic modulation
- experiment: DFT binding energy calculation | First-principles DFT with DFT-D correction | params: GGA-PBE, Grimme DFT-D, 4×4×1 Monkhorst-Pack grid, 400 eV plane-wave cutoff, vacuum 15 Å | result: Configuration VI of Ti₃C₂(OH)₂ @ MoS₂ has E_B = -1.2 eV, the most stable among all configurations
  - [experimental result] DFT calculations with dispersion correction show Ti₃C₂(OH)₂ @ MoS₂ (VI) has the most negative binding energy (E_B = -1.2 eV).
  - [image description] Charge density difference reveals electron accumulation near H atoms and depletion near S atoms at the interface, indicating interfacial polarization.
  - [referenced knowledge] Van der Waals forces dominate the interface, and standard GGA functionals fail to capture this without dispersion correction.
  - [image description] Work function shift from 1.62 eV (Ti₃C₂(OH)₂) to 2.61 eV (heterostructure) confirms electronic coupling at the interface.
  - [deductive reasoning] Thus, Configuration VI enhances interfacial stability through optimized vdW interactions and charge redistribution.
### M3  Structure → Property
- cause: Hierarchical 2D structure with vertically anchored MoS₂ on Ti₃C₂Tₓ nanosheets
- effect: Enhanced barrier effect against corrosive media (Cl⁻, H₂O, Na⁺) and improved self-lubricating properties due to preserved 2D lamellar morphology
- experiment: EIS measurements and coating resistance (R_c) analysis | Electrochemical Impedance Spectroscopy | params: 3.5 wt.% NaCl solution, frequency range 10⁻²–10⁵ Hz, 20 mV perturbation | result: Ti₃C₂Tₓ @ MoS₂-0.1 shows largest |Z|₀.₀₁ Hz (1.15×10⁶ Ω cm² after 9 days) and highest R_c (1.12×10⁶ Ω cm²)
  - [image description] SEM and XRD confirm the hierarchical 2D structure with MoS₂ anchored on Ti₃C₂Tₓ, preserving lamellar morphology.
  - [non-referenced_knowledge] The tortuous path formed by the structure impedes diffusion of Cl⁻ and H₂O into the coating.
  - [experimental result] EIS results show Ti₃C₂Tₓ @ MoS₂-0.1 has the highest |Z|₀.₀₁ Hz and R_c values after 9 days immersion.
  - [referenced knowledge] MoS₂ and Ti₃C₂Tₓ both have low interlayer shear strength due to van der Waals interactions.
  - [image description] Wear tracks show smooth fish-scale patterns without furrow pits, indicating reduced adhesive wear.
  - [deductive reasoning] Thus, the hierarchical structure enhances both barrier effect (corrosion) and lubrication (wear).
### M4  Structure → Performance
- cause: Hierarchical 2D structure with optimal MoS₂ anchoring and suppressed Ti₃C₂Tₓ restacking
- effect: Superior corrosion protection and antiwear performance of epoxy coating with 0.1 wt.% Ti₃C₂Tₓ @ MoS₂
- experiment: Wear rate measurement and EIS performance evaluation | Reciprocating ball-on-disk tribometer and electrochemical workstation | params: 10 N load, 4 mm stroke, 2 Hz, 1800 s; 3.5 wt.% NaCl, EIS frequency 10⁻²–10⁵ Hz | result: Wear rate of Ti₃C₂Tₓ @ MoS₂-0.1 = 0.09 μm³/(N·mm); |Z|₀.₀₁ Hz = 1.15×10⁶ Ω cm² after 9 days
  - [experimental result] Ti₃C₂Tₓ @ MoS₂-0.1 exhibits the highest |Z|₀.₀₁ Hz and R_c values during 9-day immersion, indicating superior barrier performance.
  - [experimental result] Wear rate of Ti₃C₂Tₓ @ MoS₂-0.1 is 0.09 μm³/(N·mm), 50% lower than pure epoxy.
  - [experimental result] Higher loadings (0.3 and 0.5 wt.%) show increased wear rate due to agglomeration and reduced coating compactness.
  - [non-referenced_knowledge] The hierarchical structure prevents restacking and maintains dispersion, maximizing exposure of lubricating and barrier surfaces.
  - [deductive reasoning] Thus, 0.1 wt.% loading achieves the ideal balance of dispersion and functionality, yielding peak performance.
### M5  Processing → Property
- cause: One-step hydrothermal synthesis followed by dispersion and spray coating into epoxy
- effect: Formation of Ti₃C₂Tₓ @ MoS₂ heterostructure with high binding energy and low wear rate, directly influencing electrical and mechanical properties
- experiment: DFT binding energy and tribological testing | DFT calculation and reciprocating friction test | params: DFT-D correction, 4×4×1 grid; 10 N load, 1800 s duration | result: Binding energy of Ti₃C₂(OH)₂ @ MoS₂ (VI) = -1.2 eV; wear rate = 0.09 μm³/(N·mm)
  - [experimental result] Hydrothermal synthesis at 210 °C for 18 h enables direct growth of MoS₂ on Ti₃C₂Tₓ.
  - [experimental result] DFT calculations show this structure has the highest binding energy among configurations.
  - [experimental result] The resulting heterostructure exhibits the lowest wear rate in tribological tests.
  - [non-referenced_knowledge] Strong interfacial binding reduces delamination under stress, enhancing mechanical durability.
  - [deductive reasoning] Thus, processing directly determines interfacial structure, which governs key properties.
