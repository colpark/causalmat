# MatMech content for Journal_of_Magnesium_and_Alloys/j.jma.2020.11.023 (judge only; not shown to staff)
- material: Mg₃Bi₂-based material with Se doping  elements: ['Mg', 'Bi', 'Sb', 'Se']  category: ['Crystalline Material', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Ball milling followed by direct current (DC) hot-pressing at 1053 K under 45 MPa
- **Structure**: Single-phase Zintl compound with coarse grains and uniform distribution of Mg, Bi, Sb, and Se; enhanced valley degeneracy in conduction bands
- **Properties**: Seebeck coefficient–thermoelectric property, electrical conductivity–thermoelectric property, thermal conductivity–thermoelectric property, Hall mobility–electrical property, power factor–thermoelectric property
- **Performance**: Thermoelectric figure-of-merit (ZT) of 0.82 at 300 K and peak ZT of 1.24 at 498 K; high engineering ZT and engineering power factor for low-temperature applications
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Ball milling followed by direct current (DC) hot-pressing at 1053 K under 45 MPa
- effect: Formation of coarse grains and single-phase Zintl compound with uniform distribution of Mg, Bi, Sb, and Se
- experiment: DC hot-pressing and ball milling | Hot pressing | params: 1053 K, 45 MPa, 2 min | result: Dense, single-phase samples with coarse grains and no impurities detected by XRD
  - [experimental result] Samples were prepared by ball milling for 10 h followed by DC hot-pressing at 1053 K and 45 MPa for 2 min.
  - [experimental result] XRD patterns show only the Mg₃Sb₂-type phase with no impurity peaks, indicating single-phase formation.
  - [image description] SEM and EDS mappings confirm dense, layered microstructure with uniform distribution of Mg, Bi, Sb, and Se.
  - [non-referenced_knowledge] Coarse grains reduce grain boundary density, which is known to decrease carrier scattering and improve mobility.
  - [deductive reasoning] Thus, the processing route of ball milling and hot pressing leads to a microstructure with coarse grains and phase homogeneity.
### M2  Structure → Properties
- cause: Enhanced valley degeneracy in conduction bands due to Mg₃Bi₂ alloying and Se doping
- effect: High electron concentration (3 × 10¹⁹ cm⁻³) and ultrahigh Hall mobility (150 cm² V⁻¹ s⁻¹) at 300 K
- experiment: Hall effect measurement | Hall coefficient measurement | params: Magnetic field: 1.5 T; temperature range: 300–623 K | result: Hall carrier concentration up to 3.4 × 10¹⁹ cm⁻³ and mobility up to 150 cm² V⁻¹ s⁻¹ at 300 K for x=0.01 Se doping
  - [image description] DFT calculations show that Mg₃Bi₁.₃₇₅Sb₀.₆₂₅ and Mg₃Bi₁.₃₇₅Sb₀.₅Se₀.₁₂₅ exhibit multiple conduction band minima at M, K, Γ, and L points.
  - [image description] Se doping shifts the Fermi level toward the conduction band minimum, confirming n-type behavior.
  - [experimental result] Hall measurements show Se-doped samples achieve carrier concentrations up to 3.4 × 10¹⁹ cm⁻³ and mobility of 150 cm² V⁻¹ s⁻¹ at 300 K.
  - [non-referenced_knowledge] High valley degeneracy increases the density of states, enabling higher carrier concentration without sacrificing mobility.
  - [non-referenced_knowledge] Coarse grains from hot pressing reduce grain boundary scattering, further enhancing mobility.
  - [deductive reasoning] Thus, the combined effect of band structure engineering and microstructural control leads to high carrier concentration and mobility.
### M3  Structure → Properties
- cause: Alloying of Mg₃Bi₂ with Mg₃Sb₂ and Se doping
- effect: Reduction in lattice thermal conductivity (κ_L) to 0.6–0.7 W m⁻¹ K⁻¹ at low temperatures
- experiment: Thermal conductivity measurement | Laser flash analysis and DSC | params: Thermal diffusivity (D) and specific heat (Cp) measured from 300–623 K | result: Lattice thermal conductivity reduced to 0.6–0.7 W m⁻¹ K⁻¹ at low temperatures for Se-doped samples
  - [experimental result] The material is a solid solution of Mg₃Bi₂ and Mg₃Sb₂ with Se doping, creating atomic-scale compositional fluctuations.
  - [experimental result] Lattice thermal conductivity (κ_L) is measured to be 0.6–0.7 W m⁻¹ K⁻¹ at low temperatures, much lower than pure Mg₃Sb₂.
  - [referenced knowledge] Alloy scattering from mass and strain differences between Bi, Sb, and Se atoms is a known mechanism to suppress κ_L.
  - [non-referenced_knowledge] Reduced κ_L occurs without degradation in electrical transport, indicating decoupling of electronic and thermal transport.
  - [deductive reasoning] Thus, the alloyed structure with Se doping effectively scatters phonons, leading to ultralow lattice thermal conductivity.
### M4  Properties → Performance
- cause: High power factor (29 μW cm⁻¹ K⁻² at 300 K) and low lattice thermal conductivity (0.6–0.7 W m⁻¹ K⁻¹)
- effect: High thermoelectric figure-of-merit ZT of 0.82 at 300 K and peak ZT of 1.24 at 498 K
- experiment: ZT calculation | Thermoelectric property measurement | params: S, σ, κ measured from 300–623 K; ZT = S²σT / (κ_e + κ_L) | result: ZT = 0.82 at 300 K and peak ZT = 1.24 at 498 K for Mg₃.₂Bi₁.₄Sb₀.₅₉Se₀.₀₁
  - [experimental result] Power factor reaches 29 μW cm⁻¹ K⁻² at 300 K due to high carrier concentration and mobility.
  - [experimental result] Lattice thermal conductivity is reduced to 0.6–0.7 W m⁻¹ K⁻¹ due to alloy scattering.
  - [experimental result] ZT is calculated using ZT = S²σT / (κ_e + κ_L), and values exceed 0.8 at 300 K and peak at 1.24 at 498 K.
  - [non-referenced_knowledge] The thermoelectric figure of merit ZT depends directly on the ratio of power factor to thermal conductivity.
  - [deductive reasoning] Thus, the optimized balance of high power factor and low κ_L leads to high ZT performance.
### M5  Processing → Performance
- cause: DC hot-pressing at 1053 K to form coarse grains and minimize grain boundary scattering
- effect: High engineering ZT (ZT_eng) of ~0.9 and engineering power factor (PF_eng) of ~12% efficiency for low-temperature applications
- experiment: Engineering ZT and PF calculation | Integrated thermoelectric performance evaluation | params: Temperature range: 300–623 K; cold side fixed at 300 K | result: ZT_eng ≈ 0.9 and PF_eng ≈ 12% for Mg₃.₂Bi₁.₄Sb₀.₅₉Se₀.₀₁
  - [experimental result] DC hot-pressing at 1053 K produces coarse grains with low grain boundary density.
  - [experimental result] Low grain boundary density reduces resistivity and increases Hall mobility, as confirmed in Fig. 4b.
  - [referenced knowledge] Engineering power factor (PF_eng) and ZT_eng are calculated by integrating S²σ/κ over the operating temperature range.
  - [non-referenced_knowledge] High PF_eng and ZT_eng are achieved because the material maintains high mobility and low κ_L across the temperature range.
  - [deductive reasoning] Thus, the processing method directly enables high engineering performance by optimizing microstructure for real-world thermoelectric operation.
