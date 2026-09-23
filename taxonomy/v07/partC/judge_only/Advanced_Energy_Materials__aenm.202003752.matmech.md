# MatMech content for Advanced_Energy_Materials/aenm.202003752 (judge only; not shown to staff)
- material: Ionic liquid-based localized highly concentrated electrolyte (LHCE) composed of LiFSI, [PP₁₃][FSI], and HFE  elements: ['C', 'H', 'F', 'Li', 'N', 'O', 'S']  category: ['Ionic Liquid', 'Nanomaterial', 'Ceramic', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Dissolution of LiFSI in [PP₁₃][FSI] ionic liquid followed by addition of HFE diluent at 1:2 molar ratio
- **Structure**: Localized highly concentrated Li⁺–FSI⁻ solvation structure with minimal HFE/PP₁₃⁺ participation; dense inorganic SEI layer rich in LiF, Li₂O, and S=O compounds
- **Properties**: Ionic conductivity–electrical property, Coulombic efficiency–electrochemical property, viscosity–physical property, Li⁺ transference number–electrochemical property
- **Performance**: Dendrite-free Li deposition over 800 cycles in Li/Cu cells; stable cycling over 5000 cycles in Li/Li symmetric cells at 10 mA cm⁻²; high capacity retention (87%) in LFP/Li batteries after 1000 cycles at 5C
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Dissolution of LiFSI in [PP₁₃][FSI] ionic liquid followed by addition of HFE diluent at 1:2 molar ratio
- effect: Localized highly concentrated Li⁺–FSI⁻ solvation structure with minimal HFE/PP₁₃⁺ participation; dense inorganic SEI layer rich in LiF, Li₂O, and S=O compounds
- experiment: Raman spectroscopy and MD simulation of Li⁺ solvation structure | Raman spectroscopy, Molecular Dynamics (MD) simulation | params: IL/HFE molar ratio of 1:2; comparison with ILE and commercial electrolyte | result: Raman peak shift of FSI⁻ S=O stretch from 1223 cm⁻¹ (ILE) to 1227 cm⁻¹ (LHCE); RDF peak at 1.95 Å for Li–O_FSI increases in LHCE; no Li–O_HFE or Li–N_PP13 peaks detected
  - [experimental result] HFE is added to ILE at a 1:2 molar ratio to form LHCE, reducing viscosity and improving wettability.
  - [experimental result] Raman and FTIR show no shift in HFE peaks, indicating weak Li⁺–HFE interaction.
  - [experimental result] MD simulations show increased Li–O_FSI RDF peak at 1.95 Å and higher AGG proportion in LHCE vs ILE.
  - [referenced knowledge] DFT calculations reveal LUMO localized on FSI⁻ anions, making them preferentially reduced.
  - [experimental result] XPS confirms SEI in LHCE contains abundant LiF, Li₂O, and S=O compounds from FSI⁻ decomposition.
  - [non-referenced_knowledge] Inorganic SEI components have higher mechanical strength and suppress dendrite penetration.
  - [deductive reasoning] Thus, HFE enhances Li⁺–FSI⁻ coordination without solvating Li⁺, promoting inorganic SEI formation and localized high concentration structure.
### M2  Structure → Properties
- cause: Localized highly concentrated Li⁺–FSI⁻ solvation structure with minimal HFE/PP₁₃⁺ participation; dense inorganic SEI layer rich in LiF, Li₂O, and S=O compounds
- effect: Ionic conductivity–electrical property, Coulombic efficiency–electrochemical property, viscosity–physical property, Li⁺ transference number–electrochemical property
- experiment: Viscosity and ionic conductivity measurements; Li⁺ transference number calculation | Viscometer, conductivity meter, Bruce–Vincent method | params: Measurements at 25°C; IL/HFE ratio 1:2; comparison with ILE and commercial electrolyte | result: LHCE viscosity = 6.8 mPa·s (vs 5.9 mPa·s for commercial); ionic conductivity = 3.2 mS cm⁻¹ (vs 1.1 mS cm⁻¹ for ILE); Li⁺ transference number t_Li⁺ = 0.313 (vs 0.165 for ILE)
  - [experimental result] HFE diluent reduces electrolyte viscosity from >100 mPa·s (ILE) to 6.8 mPa·s (LHCE).
  - [experimental result] Lower viscosity increases ionic conductivity to 3.2 mS cm⁻¹, nearly triple that of ILE.
  - [experimental result] MD simulations show uniform Li⁺ flux due to localized high concentration and reduced concentration gradients.
  - [experimental result] Bruce–Vincent method confirms t_Li⁺ = 0.313 for LHCE vs 0.165 for ILE.
  - [non-referenced_knowledge] Dense inorganic SEI (LiF, Li₂O) suppresses parasitic reactions between Li and electrolyte.
  - [deductive reasoning] Reduced side reactions directly increase Coulombic efficiency.
### M3  Properties → Performance
- cause: Ionic conductivity–electrical property, Coulombic efficiency–electrochemical property, viscosity–physical property, Li⁺ transference number–electrochemical property
- effect: Dendrite-free Li deposition over 800 cycles in Li/Cu cells; stable cycling over 5000 cycles in Li/Li symmetric cells at 10 mA cm⁻²; high capacity retention (87%) in LFP/Li batteries after 1000 cycles at 5C
- experiment: Li/Cu and Li/Li symmetric cell cycling; LFP/Li battery rate and cycle testing | Battery cycling test system (Neware CT-4000) | params: Li/Cu: 0.5 mA cm⁻², 0.5 mAh cm⁻²; Li/Li: 10 mA cm⁻², 1 mAh cm⁻²; LFP/Li: 5C rate, 0.5C rate | result: Li/Cu CE ≈ 99.4% over 800 cycles; Li/Li stable for 5000 cycles at 10 mA cm⁻²; LFP/Li retains 87% capacity after 1000 cycles at 5C; LFP/Li@Cu CE >99.5% over 100 cycles
  - [experimental result] LHCE achieves 99.4% CE over 800 cycles in Li/Cu cells.
  - [non-referenced_knowledge] High CE indicates minimal Li loss and dendrite formation.
  - [experimental result] LHCE exhibits 3.2 mS cm⁻¹ ionic conductivity and t_Li⁺ = 0.313, enabling efficient ion transport.
  - [experimental result] Li/Li symmetric cell cycles stably for 5000 cycles at 10 mA cm⁻² with low polarization.
  - [non-referenced_knowledge] High ionic conductivity and transference number reduce concentration gradients and polarization at high current density.
  - [experimental result] LFP/Li cell retains 87% capacity after 1000 cycles at 5C, demonstrating compatibility with high-power cathodes.
  - [deductive reasoning] Thus, the combined properties of high conductivity, transference number, and CE directly enable exceptional battery performance.
