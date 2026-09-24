# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202010426 (judge only; not shown to staff)
- material: H-MAPbI3-xClx  elements: ['H', 'M', 'A', 'Pb', 'I', 'Cl', 'C', 'N', 'O']  category: ['Crystalline Material', 'Ceramic', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Spin coating method using MAI and PbCl2 in DMF solvent, followed by thermal annealing at 100°C for 60 min
- **Structure**: Tetragonal structure of MAPbI3 with residual Cl ions
- **Properties**: tensile strength–mechanical property, conductivity–electrical property
- **Performance**: Reversible transition between transparent and dark reddish-brown states with high solar modulation ability (23.7%), low transition temperature (29.4-51.4°C), and narrow hysteresis width (7.7-13.2°C)
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Spin coating method using MAI and PbCl2 in DMF solvent, followed by thermal annealing at 100°C for 60 min
- effect: Tetragonal structure of MAPbI3 with residual Cl ions
- experiment: XRD measurements on H-MAPbI3-xClx films | X-ray diffraction (XRD) | params: Cold state and hot state conditions, varying molar ratios of MAI:PbCl2 | result: Tetragonal structure confirmed; Cl incorporation shown through peak shift in XRD patterns
  - [experimental result] Samples were spin-coated from MAI and PbCl2 in DMF and thermally annealed at 100°C for 60 minutes.
  - [image description] XRD patterns confirm the tetragonal structure of MAPbI3, with a peak shift indicating Cl ion incorporation.
  - [referenced knowledge] Peak shift from 14.36° to 14.44° correlates with reduced d-spacing due to smaller Cl⁻ compared to I⁻.
  - [non-referenced_knowledge] Annealing temperature and precursor composition influence crystalline phase and anion distribution in hybrid perovskites.
  - [deductive reasoning] Therefore, the combination of spin coating and annealing results in a tetragonal MAPbI3 structure with residual Cl ions.
### M2  Structure → Property
- cause: Tetragonal structure of MAPbI3 with residual Cl ions
- effect: High solar modulation ability (23.7%)
- experiment: Optical transmittance measurements | UV–vis–NIR spectrophotometer | params: Wavelength range from 300–2500 nm, measurement at cold (25°C) and hot (60°C) states | result: τlum = 85.2% (cold), τlum = 30.3% (hot), Δτsol = 23.7%
  - [image description] Transmittance spectra show large difference in visible light transmission between cold and hot states.
  - [experimental result] Δτsol reaches 23.7% due to strong absorption in visible range at hot state.
  - [referenced knowledge] Cl-doping alters band structure and optical absorption in hybrid perovskites.
  - [non-referenced_knowledge] Crystal symmetry and anion composition control optical response in halide perovskites.
  - [deductive reasoning] Thus, the tetragonal MAPbI3 structure with residual Cl enables high solar modulation ability via enhanced optical contrast.
### M3  Property → Performance
- cause: High solar modulation ability (23.7%)
- effect: Reversible transition between transparent and dark reddish-brown states
- experiment: Cycle performance test under ambient conditions | Temperature-controlled heating/cooling cycles | params: 50 heating-cooling cycles, RH ~50%, temp: 25–60°C | result: Stable τlum and Δτsol maintained over 50 cycles
  - [image description] Cycle tests demonstrate consistent optical performance across 50 heating/cooling cycles.
  - [experimental result] Δτsol remains stable at ~23.7% over repeated cycles.
  - [referenced knowledge] Optical contrast stability ensures reliable switching between transparent and tinted states.
  - [non-referenced_knowledge] Smart window materials must maintain reversible optical modulation over many cycles.
  - [inductive reasoning] Hence, high solar modulation ability contributes to the excellent reversible thermochromic performance of H-MAPbI3-xClx TPSW.
### M4  Processing → Performance
- cause: Spin coating method using MAI and PbCl2 in DMF solvent, followed by thermal annealing at 100°C for 60 min
- effect: Low transition temperature (29.4–51.4°C) and narrow hysteresis width (7.7–13.2°C)
- experiment: Transition temperature measurement under variable humidity | Temperature-controlled chamber with humidity regulation | params: RH 25–80%, temp 20–60°C | result: Tc ranges from 29.4 to 51.4°C; ΔTc reduces from 22.9 to 9.6°C
  - [image description] Figure shows tunable Tc and narrower ΔTc in H-MAPbI3-xClx compared to H-MAPbI3.
  - [experimental result] Tc can be adjusted from 29.4 to 51.4°C depending on RH conditions.
  - [referenced knowledge] Humidity affects hydration/dehydration equilibrium and thus controls transition temperature.
  - [non-referenced_knowledge] Processing conditions influence film morphology and phase purity, affecting thermodynamic behavior.
  - [deductive reasoning] Therefore, spin coating and annealing optimize hydration dynamics and Cl incorporation, resulting in improved transition properties.
