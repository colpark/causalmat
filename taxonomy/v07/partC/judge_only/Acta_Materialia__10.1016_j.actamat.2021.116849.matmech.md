# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116849 (judge only; not shown to staff)
- material: Mn1.95Cr0.05Sb0.95Ga0.05  elements: ['Mn', 'Cr', 'Sb', 'Ga', 'Ti', 'Ni']  category: ['Crystalline Material', 'Composite Material', 'Metals and Alloys']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Composite fabrication with Ti50Ni50 shape memory alloy substrate
- **Structure**: Tetragonal crystal structure (P4/nmm)
- **Properties**: Magnetic entropy change–magnetic property, Transformation temperature–thermal property
- **Performance**: Enhanced magnetocaloric effect under nonvolatile strain, Wide working temperature window of 31 K at 1 T
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Composite fabrication with Ti50Ni50 shape memory alloy substrate providing nonvolatile residual strain
- effect: Mn1.95Cr0.05Sb0.95Ga0.05 ribbon exhibits external lattice distortion εext = 0.14%
- experiment: XRD analysis of MnCrSbGa under different strains | X-ray diffraction | params: 2θ scan of (002) peak with εr,sub = 0%, 1%, and 2% | result: 0.04° decrease in (002) peak angle at 2% strain corresponds to ~0.14% external lattice distortion
  - [experimental result] TiNi substrate provides stable residual strains of 0%, 1%, and 2% after unloading
  - [image description] XRD shows (002) peak shifts by 0.04° when strain increases from 0% to 2%
  - [referenced knowledge] Elastic modulus of Mn2Sb is ~50 GPa at room temperature
  - [non-referenced_knowledge] Stress-strain relationship follows Hooke’s law: σext = k·εext
  - [deductive reasoning] Calculated external stress σext ≈ 70 MPa causes ~0.14% lattice distortion in MnCrSbGa
### M2  Structure → Property
- cause: External lattice distortion εext = 0.14% induced by SMA substrate
- effect: Transformation temperature TM of MnCrSbGa shifts up by ~6 K
- experiment: Temperature-dependent magnetization measurements | SQUID magnetometry | params: M-T curves under 0.1 T magnetic field for M/E/T-0%, -1%, and -2% samples | result: TM increases from ~215.59 K (free state) to ~221.87 K at 2% strain
  - [non-referenced_knowledge] Landau model includes magnetoelastic coupling term λε(m1 + m2)² affecting free energy of magnetic states
  - [image description] Free energy calculations show crossing point between AFM and FRM states shifts to higher temperature with increasing εext
  - [referenced knowledge] Clausius-Clapeyron relation predicts dT/dσc = εtrVs / ΔStr for first-order phase transitions
  - [deductive reasoning] Measured stress sensitivity dT/dσc = 0.085 K/MPa matches theoretical value from material parameters
### M3  Property → Performance
- cause: Shifted transformation temperature TM with enhanced working temperature window
- effect: Wide effective working temperature window ΔETW = 31 K at 1 T magnetic field
- experiment: Magnetocaloric effect characterization | Isothermal magnetization and entropy change calculation | params: ΔSM(T) curves under 1 T field for M/E/T-0%, -1%, and -2% samples | result: Individual ΔETW ≈ 33 K each, combined window extends to 31 K due to strain-gradient tuning
  - [experimental result] Each sample individually has ΔETW ≈ 33 K at 5 T field
  - [image description] Different residual strains shift individual TM values by up to 10 K
  - [referenced knowledge] Constant refrigeration capacity RC despite temperature shifts enables uniform cooling performance
  - [inductive reasoning] Combining samples with 0%, 1%, and 2% strains creates continuous 31 K working window at 1 T field
### M4  Processing → Performance
- cause: Composite fabrication with Ti50Ni50 shape memory alloy substrate providing large nonvolatile strain
- effect: Enhanced magnetocaloric effect with TM shift ~6 K at 2% strain
- experiment: Comparison with PMN-PT composite | Magnetization vs. temperature measurements | params: M-T curves under 0.1 T field for MnCrSbGa/TiNi and MnCrSbGa/PMN-PT composites | result: TiNi substrate achieves 6 K TM shift vs. only 0.8 K for PMN-PT electrostrain
  - [experimental result] TiNi SMA provides residual strains up to 2% after unloading
  - [image description] PMN-PT piezoelectric substrate only achieves 0.047% nonvolatile electrostrain
  - [non-referenced_knowledge] SMA strain translates to ~70 MPa stress in MnCrSbGa via Hooke's law
  - [deductive reasoning] With dT/dσc = 0.085 K/MPa, 70 MPa stress yields ~6 K TM shift
