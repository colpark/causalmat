# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116843 (judge only; not shown to staff)
- material: FeNiCoCr high-entropy alloy (HEA)  elements: ['Fe', 'Ni', 'Co', 'Cr']  category: ['Metals and Alloys', 'Nanomaterial', 'Crystalline Material']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Helium ion implantation at 773 K with a fluence of 5.14×10^16 ions/cm²
- **Structure**: Formation of highly pressurized helium nanobubbles (HPHNBs) with mean radius of ~1.2 nm and dislocation loops with mean radius of ~3.3 nm
- **Properties**: yield strength–mechanical property, strain hardening capacity–mechanical property
- **Performance**: Enhanced strength-ductility synergy in micro/nanoscale components
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Helium ion implantation at 773 K with a fluence of 5.14×10^16 ions/cm²
- effect: Formation of highly pressurized helium nanobubbles (HPHNBs) with mean radius of ~1.2 nm and dislocation loops with mean radius of ~3.3 nm
- experiment: Helium ion implantation and microstructural observation | Transmission Electron Microscopy (TEM) | params: Implantation temperature: 773 K; Fluence: 5.14×10¹⁶ ions/cm²; Beam flux: 1.8×10¹² ions/cm²/s | result: Formation of HPHNBs with mean radius ~1.2 nm and dislocation loops with mean radius ~3.3 nm
  - [experimental result] FeNiCoCr HEA was implanted under vacuum with 275 keV He⁺ ions at 773 K to a fluence of 5.14×10¹⁶ ions/cm².
  - [image description] Fresnel-contrast TEM images show high density of HPHNBs and dislocation loops after implantation.
  - [referenced knowledge] Sluggish helium diffusion in fcc HEAs enables stable bubble formation under implantation conditions.
  - [non-referenced_knowledge] Helium atoms are trapped by existing defect sinks like dislocations and grain boundaries, promoting bubble nucleation and growth.
  - [deductive reasoning] Therefore, helium ion implantation under controlled conditions leads to the formation of HPHNBs and dislocation loops within the alloy matrix.
### M2  Structure → Property
- cause: Formation of highly pressurized helium nanobubbles (HPHNBs) with mean radius of ~1.2 nm
- effect: Increased yield strength and enhanced strain hardening capacity
- experiment: In situ TEM tensile and compression tests | Nanomechanical testing inside TEM | params: Tensile/compression tests on nanopillars with thicknesses of ~50–70 nm and diameters ~100 nm | result: Yield strength increased by ~50% in HPHNB-HEA compared to U-HEA with minimal reduction in ductility
  - [experimental result] In situ TEM tensile tests show twinning-mediated deformation in U-HEA and stacking-fault-mediated deformation in HPHNB-HEA.
  - [image description] Compression tests reveal ~50% increase in yield strength in HPHNB-HEA without significant loss of ductility.
  - [referenced knowledge] Stacking faults enhance work hardening in alloys with low stacking fault energy through interaction of slip systems.
  - [non-referenced_knowledge] HPHNBs act as dispersed barriers that increase CRSS via the relation Δτ = αμb(Nd)^½.
  - [deductive reasoning] Thus, HPHNBs improve both yield strength and strain hardening capacity via obstacle hardening and stacking-fault multiplication.
### M3  Property → Performance
- cause: Increased yield strength and enhanced strain hardening capacity
- effect: Enhanced strength-ductility synergy in micro/nanoscale components
- experiment: In situ TEM tensile and compression tests | Nanomechanical testing inside TEM | params: Strain rates ~4×10⁻⁴ s⁻¹ (tension), ~8×10⁻⁴ s⁻¹ (compression); displacement-controlled mode | result: HPHNB-HEA shows moderate tensile ductility (~14.5%) and improved compressive plasticity without early fracture
  - [experimental result] Tensile tests show moderate ductility (~14.5%) in HPHNB-HEA despite increased strength.
  - [image description] Images show no coalescence or fragmentation of HPHNBs during straining, indicating structural stability.
  - [referenced knowledge] Ion implantation usually causes embrittlement, but HPHNB-HEA retains ductility due to unique deformation mechanism.
  - [non-referenced_knowledge] Ductility is maintained when mobile dislocation density compensates for reduced dislocation mean free path.
  - [inductive reasoning] Therefore, the stacking-fault-mediated deformation mechanism preserves ductility while increasing strength, resulting in enhanced strength-ductility synergy.
### M4  Structure → Property
- cause: High internal pressure within HPHNBs (~2.5–4.7 GPa)
- effect: Reduced activation free energy for partial dislocation nucleation
- experiment: NEB simulations | Molecular dynamics simulation using LAMMPS with MEAM potential | params: Models with/without HPHNBs; varying internal pressure from 0 to 6 GPa | result: Activation free energy decreases with increasing internal pressure, enhancing dislocation nucleation rates
  - [experimental result] MD simulations show decreasing activation free energy with increasing internal pressure in HPHNBs.
  - [image description] NEB plots demonstrate that higher internal pressure correlates with lower activation free energy for partial dislocation nucleation.
  - [referenced knowledge] The relationship ΔG(τ) = A(1 − τ/τ_ath)^α describes how external shear stress affects nucleation energy.
  - [non-referenced_knowledge] Internal pressure induces local shear stress that facilitates dislocation emission from the HPHNB surface.
  - [deductive reasoning] Therefore, high internal pressure in HPHNBs reduces the energy required to initiate dislocation activity, enhancing plasticity and work hardening.
