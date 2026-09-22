# MatMech content for Journal_of_Advanced_Ceramics/s40145-019-0329-1 (judge only; not shown to staff)
- material: Bi₂V₁₋ₓAlₓ/₂Tiₓ/₂O₅.₅₋δ  elements: ['Bi', 'V', 'Al', 'Ti', 'O']  category: ['Ceramic', 'Crystalline Material']
- MST chain: Processing → Structure → Properties
## Tetrahedron elements
- **Processing**: Solid-state reaction technique with calcination at 650 °C and 750 °C, followed by sintering at 800 °C for 10 h
- **Structure**: Stabilization of tetragonal phase (space group I4/mmm) with dopant concentration x ≥ 0.175; reduction of orthorhombic phase; lattice expansion in c-parameter; increased crystallographic disordering
- **Properties**: Ionic conductivity–electrical property
- **Performance**: Enhanced ionic conductivity in intermediate temperature range (up to 7.28 × 10⁻⁴ S·cm⁻¹ at 300 °C for x = 0.175); suppression of phase transitions enabling room-temperature operational stability
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Solid-state reaction technique with calcination at 650 °C and 750 °C, followed by sintering at 800 °C for 10 h
- effect: Stabilization of tetragonal phase (space group I4/mmm) with dopant concentration x ≥ 0.175; reduction of orthorhombic phase
- experiment: XRD phase analysis | X-ray diffraction | params: 2θ range 10°–80°, Cu Kα radiation, Rietveld refinement using Match-3 and FullProf | result: For x ≥ 0.175, splitted peaks at 32° converge into a singlet (110), indicating tetragonal phase dominance; impurity peaks of BiVO₄ disappear for x ≤ 0.20 after sintering
  - [experimental result] The solid-state reaction involves calcination at 650 °C and 750 °C followed by sintering at 800 °C to promote homogeneity and densification.
  - [experimental result] XRD shows impurity phase BiVO₄ disappears for x ≤ 0.20 after sintering, indicating phase purity is achieved.
  - [experimental result] For x = 0.15, XRD reveals partial splitting at 32° (orthorhombic) which converges to a singlet after sintering, indicating tetragonal phase formation.
  - [experimental result] For x ≥ 0.175, XRD shows a single (110) peak, confirming complete tetragonal phase stabilization.
  - [image description] DSC shows suppression of β→γ phase transition endothermic peaks for x ≥ 0.175, indicating the tetragonal phase is stable at room temperature.
  - [image description] FT-IR shows broadening and disappearance of V–O symmetric stretch for x ≥ 0.175, indicating increased crystallographic disorder consistent with tetragonal phase.
  - [non-referenced_knowledge] Doping with Al³⁺ and Ti⁴⁺ creates oxygen vacancies and induces lattice strain that destabilizes the orthorhombic phase.
  - [deductive reasoning] Combined effect of Al and Ti doping lowers the critical concentration needed for tetragonal stabilization compared to single doping.
  - [deductive reasoning] Thus, the processing protocol enables atomic rearrangement and defect formation that stabilize the tetragonal phase at room temperature.
### M2  Structure → Properties
- cause: Stabilization of tetragonal phase (space group I4/mmm) with dopant concentration x ≥ 0.175; increased crystallographic disordering; higher concentration of oxygen ion vacancies
- effect: Enhanced ionic conductivity (up to 7.28 × 10⁻⁴ S·cm⁻¹ at 300 °C for x = 0.175); dominance of grain interior conduction; suppression of phase transition-related conductivity discontinuities
- experiment: Electrochemical impedance spectroscopy (EIS) | Electrochemical impedance spectroscopy | params: Frequency range 4 Hz – 8 MHz, temperature range RT–650 °C, gold electrodes | result: Grain resistance (Rg) and grain boundary resistance (Rgb) decrease with temperature; overall resistance dominated by grain interior; highest conductivity at x = 0.175
  - [experimental result] UV–Vis analysis shows the lowest band gap (1.95 eV) for x = 0.175, correlating with the highest concentration of oxygen vacancies.
  - [image description] FT-IR shows disappearance of the V–O symmetric stretch band for x ≥ 0.175, indicating high crystallographic disorder.
  - [experimental result] XRD and DSC confirm complete tetragonal phase stabilization at x = 0.175 with suppressed phase transitions.
  - [experimental result] EIS shows grain interior resistance dominates and decreases with temperature, indicating bulk ionic conduction.
  - [image description] Arrhenius plot for x = 0.175 shows no discontinuity at 420 °C, confirming stabilization of the conducting phase.
  - [non-referenced_knowledge] Oxygen vacancies act as charge carriers, and their concentration is maximized at x = 0.175 due to optimal Al/Ti co-doping.
  - [non-referenced_knowledge] Crystallographic disorder in the tetragonal phase reduces energy barriers for oxygen ion hopping.
  - [deductive reasoning] Thus, the combination of high vacancy concentration and structural disorder in the stabilized tetragonal phase maximizes ionic conductivity.
### M3  Processing → Properties
- cause: Solid-state reaction technique with calcination at 650 °C and 750 °C, followed by sintering at 800 °C for 10 h
- effect: Enhanced ionic conductivity (up to 7.28 × 10⁻⁴ S·cm⁻¹ at 300 °C for x = 0.175)
- experiment: EIS and SEM correlation | Electrochemical impedance spectroscopy and scanning electron microscopy | params: Grain size measurement via SEM; Rg and Rgb from EIS fitting | result: Maximum grain size (10.18 μm) and minimum Rg occur at x = 0.175; conductivity peaks at same composition
  - [experimental result] Sintering at 800 °C for 10 h enables densification and grain growth in the ceramic pellets.
  - [image description] SEM shows maximum average grain size (10.18 μm) at x = 0.175, indicating optimal sintering behavior.
  - [experimental result] EIS shows the lowest grain resistance (Rg) at x = 0.175, correlating with largest grain size.
  - [experimental result] Grain boundary resistance (Rgb) also decreases at x = 0.175, suggesting improved grain connectivity.
  - [non-referenced_knowledge] In polycrystalline ceramics, larger grains reduce the number of high-resistance grain boundaries per unit path length.
  - [deductive reasoning] Thus, processing-induced grain growth at x = 0.175 reduces overall resistivity and enhances ionic conductivity.
### M4  Structure → Properties
- cause: Lattice expansion in c-parameter and increased oxygen vacancy concentration due to Al³⁺/Ti⁴⁺ co-doping
- effect: Lower activation energy for ionic conduction and enhanced conductivity in intermediate temperature range
- experiment: Rietveld refinement and Arrhenius analysis | XRD Rietveld refinement and conductivity temperature dependence | params: Unit cell parameters from FullProf; activation energy from Arrhenius slope | result: c-parameter increases with x; activation energy decreases to minimum at x = 0.175 (0.73 eV)
  - [experimental result] Rietveld refinement shows c-parameter increases with dopant concentration x, due to larger ionic radius of Ti⁴⁺ compared to V⁵⁺.
  - [experimental result] UV–Vis and FT-IR indicate higher oxygen vacancy concentration at x = 0.175, inferred from band gap reduction and V–O band broadening.
  - [image description] Arrhenius plot shows minimum activation energy (0.73 eV) at x = 0.175, corresponding to maximum conductivity.
  - [non-referenced_knowledge] Oxygen vacancies are the charge carriers in Bi₂VO₅.₅₋δ; higher concentration increases carrier density.
  - [non-referenced_knowledge] Lattice expansion reduces the energy barrier for oxygen ion hopping between vacancy sites.
  - [deductive reasoning] Thus, combined effect of increased vacancy concentration and lattice expansion lowers Ea and enhances conductivity.
