# MatMech content for Advanced_Energy_Materials/aenm.202003412 (judge only; not shown to staff)
- material: Co₅Fe₃Cr₂ (oxy)hydroxide  elements: ['Co', 'Fe', 'Cr', 'O', 'H']  category: ['Nanomaterial', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Coprecipitation method using CoCl₂·6H₂O, FeCl₃·6H₂O, and KCr(SO₄)₂·12H₂O in hot urea solution at 90 °C for 6 h, followed by centrifugation, washing, and drying at 60 °C
- **Structure**: Amorphous nanosheet aggregates with homogeneous elemental distribution; Co atoms predominantly in octahedral sites; Cr promotes Co occupancy in octahedral coordination and induces lattice distortion
- **Properties**: Overpotential–electrochemical property, mass activity–electrochemical property, turnover frequency–electrochemical property, charge transfer resistance–electrochemical property, carrier density–electrochemical property
- **Performance**: High OER activity in alkaline and neutral electrolytes with η₁₀ = 232 mV, Co-based mass activity of 1486.0 A g⁻¹, TOF of 0.23 s⁻¹, and stability over 168 h with minimal Co/Fe leaching
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Coprecipitation method using CoCl₂·6H₂O, FeCl₃·6H₂O, and KCr(SO₄)₂·12H₂O in hot urea solution at 90 °C for 6 h
- effect: Formation of amorphous nanosheet aggregates with homogeneous elemental distribution and low crystallinity
- experiment: Synthesis of Co₅Fe₃Cr₂ (oxy)hydroxide | Coprecipitation | params: CoCl₂·6H₂O, FeCl₃·6H₂O, KCr(SO₄)₂·12H₂O in 0.2 M urea at 90 °C for 6 h; total metal anion concentration = 20 mM | result: Amorphous nanosheet aggregates formed, confirmed by TEM and XRD
  - [experimental result] Co–Fe–Cr (oxy)hydroxides were synthesized via coprecipitation in hot urea solution at 90 °C without high-temperature pyrolysis.
  - [image description] TEM and SAED show crumpled nanosheets with diffusive rings, indicating low crystallinity.
  - [image description] EDX mapping confirms homogeneous distribution of Co, Fe, and Cr.
  - [non-referenced_knowledge] Incorporating Fe and Cr into Co (oxy)hydroxides distorts the crystal lattice due to ionic radius mismatch.
  - [non-referenced_knowledge] Low-temperature synthesis prevents atomic rearrangement into ordered phases.
  - [deductive reasoning] Thus, the processing method yields an amorphous, homogeneously mixed nanostructure.
### M2  Processing → Property
- cause: Coprecipitation method using CoCl₂·6H₂O, FeCl₃·6H₂O, and KCr(SO₄)₂·12H₂O in hot urea solution at 90 °C for 6 h
- effect: Enhanced Co³⁺/Co⁴⁺ redox activity and optimized electronic structure leading to high OER activity
- experiment: Quasi-operando EELS of Co L-edge | Electron Energy Loss Spectroscopy | params: Biasing catalyst on Au TEM grid at 0, 1.4, and 1.5 V_RHE in 0.5 M KHCO₃ for 10 min | result: Co L₃/L₂ ratio in Co₅Fe₃Cr₂ drops fastest (3.64 → 2.69), indicating rapid Co²⁺ → Co³⁺/Co⁴⁺ transition
  - [experimental result] Co–Fe–Cr (oxy)hydroxides were synthesized via low-temperature coprecipitation.
  - [experimental result] Quasi-operando EELS shows Co L₃/L₂ ratio decreases fastest in Co₅Fe₃Cr₂ upon applying potential, indicating rapid Co²⁺ → Co³⁺ transition.
  - [referenced knowledge] Cr⁶⁺ has vacant d-orbitals that accept electrons from Co, facilitating oxidation (analogous to W⁶⁺ in prior studies).
  - [non-referenced_knowledge] Amorphous structure enhances ion accessibility and charge transfer, accelerating redox transitions.
  - [deductive reasoning] Thus, the processing method enables rapid formation of high-valence Co active sites, enhancing OER activity.
### M3  Structure → Property
- cause: Amorphous nanosheet structure with Co predominantly in octahedral sites and Cr promoting Co occupancy in octahedral coordination
- effect: High Co-based mass activity (1486.0 A g⁻¹), low overpotential (232 mV), and high turnover frequency (0.23 s⁻¹)
- experiment: XAS and XPS analysis of Co valence and coordination | X-ray Absorption Spectroscopy and X-ray Photoelectron Spectroscopy | params: Co K-edge EXAFS and Co 2p XPS of Co₅Fe₃Cr₂ (oxy)hydroxide | result: Co coordination number = 5.8 ± 0.4 (octahedral); Co³⁺ abundance = 31.1 at.% (higher than monometallic Co's 9.3 at.%)
  - [experimental result] EXAFS shows Co coordination number of 5.8 in Co₅Fe₃Cr₂, indicating dominant octahedral (Co_Oh) coordination.
  - [experimental result] XPS and EELS confirm increased Co³⁺ abundance (31.1 at.%) and higher Co valence state.
  - [referenced knowledge] Co in octahedral sites with t₂g⁵eg¹ configuration is optimal for binding OER intermediates.
  - [non-referenced_knowledge] Amorphous structure increases the number of accessible active sites.
  - [deductive reasoning] Thus, the structure enables high Co³⁺ concentration and efficient intermediate adsorption, leading to high mass activity and TOF.
### M4  Structure → Performance
- cause: Amorphous nanosheet structure with homogeneous elemental distribution and Co in octahedral sites
- effect: High OER performance: η₁₀ = 232 mV, Co-based mass activity = 1486.0 A g⁻¹, TOF = 0.23 s⁻¹, and stability over 168 h
- experiment: LSV and Tafel analysis in 1 M KOH | Linear Sweep Voltammetry | params: Catalyst loading = 0.2 mg cm⁻² on GCE, scan rate = 5 mV s⁻¹ | result: Co₅Fe₃Cr₂ achieves η₁₀ = 232 mV and Tafel slope = 31 mV dec⁻¹, outperforming IrO₂ (316 mV)
  - [image description] Co₅Fe₃Cr₂ has amorphous nanosheet structure with homogeneous elemental distribution (TEM/EDX).
  - [experimental result] EXAFS confirms Co predominantly in octahedral sites, which are optimal for OER.
  - [experimental result] LSV shows η₁₀ = 232 mV and Tafel slope = 31 mV dec⁻¹, superior to IrO₂ and other compositions.
  - [experimental result] EIS shows lowest charge transfer resistance (5.4 Ω) and highest carrier density (6.2×10¹⁹ cm⁻²).
  - [experimental result] Stability test shows negligible Co/Fe leaching and maintained structure after 168 h.
  - [deductive reasoning] Thus, the structure enables high activity, fast kinetics, and durability, defining superior performance.
### M5  Structure → Property
- cause: Cr promotes Co atoms to occupy octahedral sites and induces lattice distortion
- effect: Increased Co³⁺ abundance and optimized Co spin state (t₂g⁵eg¹) for favorable OER intermediate binding
- experiment: EXAFS fitting of Co coordination | Extended X-ray Absorption Fine Structure | params: Co K-edge FT-EXAFS in Co₅Fe₃Cr₂, Co₅Fe₅, Co₅Cr₅, and Co (oxy)hydroxides | result: Co coordination number increases from ~5.1 in Co₅Fe₅ to 5.8 in Co₅Fe₃Cr₂, indicating Cr promotes octahedral Co occupancy
  - [experimental result] EXAFS shows Co coordination number increases from 5.1 in Co₅Fe₅ to 5.8 in Co₅Fe₃Cr₂.
  - [experimental result] Cr²⁺ prefers tetrahedral coordination, as confirmed by reduced Cr coordination number from 5.6 to 4.4.
  - [referenced knowledge] Cr²⁺ in tetrahedral sites forces Co into octahedral sites to maintain charge and structural balance.
  - [referenced knowledge] Octahedral Co³⁺ has t₂g⁵eg¹ configuration favorable for OER intermediates.
  - [experimental result] XPS and EELS confirm increased Co³⁺ abundance and spin-state tuning in Co₅Fe₃Cr₂.
  - [deductive reasoning] Thus, Cr-induced octahedral Co occupancy creates optimal electronic structure for OER.
### M6  Property → Performance
- cause: High Co-based mass activity (1486.0 A g⁻¹) and low charge transfer resistance (5.4 Ω)
- effect: Superior OER performance: η₁₀ = 232 mV, TOF = 0.23 s⁻¹, and stability over 168 h
- experiment: Mass activity and TOF calculation | Electrochemical activity measurement | params: Current density at η = 300 mV, normalized by Co mass and active site count | result: Mass activity = 1486.0 A g⁻¹ (Co-based); TOF = 0.23 s⁻¹
  - [experimental result] Co₅Fe₃Cr₂ exhibits Co-based mass activity of 1486.0 A g⁻¹ and TOF of 0.23 s⁻¹.
  - [experimental result] EIS shows lowest charge transfer resistance (5.4 Ω) among all catalysts.
  - [non-referenced_knowledge] Mass activity and TOF are proportional to the number and intrinsic activity of active sites.
  - [non-referenced_knowledge] Low charge transfer resistance enables efficient electron supply to active sites during OER.
  - [deductive reasoning] Thus, these properties directly cause low η₁₀ (232 mV) and high stability.
