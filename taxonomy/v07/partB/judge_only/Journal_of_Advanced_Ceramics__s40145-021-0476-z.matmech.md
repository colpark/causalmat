# MatMech content for Journal_of_Advanced_Ceramics/s40145-021-0476-z (judge only; not shown to staff)
- material: ZnO/NiCo₂O₄  elements: ['Zn', 'O', 'Ni', 'Co']  category: ['Nanomaterial', 'Composite Material', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Hydrothermal reaction at 200°C for 18 h followed by calcination at 300°C for 2 h in air
- **Structure**: Binary hybrid nanoparticles with ZnO and NiCo₂O₄ phases; interfacial heterojunctions; mesoporous structure; particle morphology controlled by NH₃·H₂O concentration
- **Properties**: Complex permittivity–electrical property, dielectric loss tangent–electrical property, attenuation constant–electromagnetic property
- **Performance**: Minimum reflection loss of -33.49 dB at 18.0 GHz with 4.99 mm thickness
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Hydrothermal reaction at 200°C for 18 h followed by calcination at 300°C for 2 h in air with varying amounts of NH₃·H₂O (0.5, 0.7, and 1.0 mL)
- effect: Formation of binary ZnO/NiCo₂O₄ hybrid nanoparticles with morphology controlled by alkalinity: irregular particles at low NH₃·H₂O (ZnO/NiCo₂O₄-5), well-regulated structure at medium NH₃·H₂O (ZnO/NiCo₂O₄-7), and aggregated structure at high NH₃·H₂O (ZnO/NiCo₂O₄-10); simultaneous formation of ZnO and NiCo₂O₄ phases via hydroxide intermediate conversion
- experiment: Hydrothermal synthesis with varied NH₃·H₂O addition | Hydrothermal reaction and calcination | params: NH₃·H₂O volumes: 0.5 mL (ZnO/NiCo₂O₄-5), 0.7 mL (ZnO/NiCo₂O₄-7), 1.0 mL (ZnO/NiCo₂O₄-10); 200°C for 18 h, then 300°C for 2 h in air | result: Morphology transitions from irregular to well-regulated to aggregated particles; XRD confirms pure ZnO and NiCo₂O₄ phases without impurities
  - [experimental result] Different volumes of NH₃·H₂O (0.5, 0.7, 1.0 mL) were added to the precursor solution, altering the OH⁻ concentration.
  - [non-referenced_knowledge] NH₃ + H₂O → NH₄⁺ + OH⁻ (Eq. 1) and Zn²⁺ + 2OH⁻ → Zn(OH)₂ (Eq. 2) generate hydroxide intermediates.
  - [non-referenced_knowledge] Ni²⁺ and Co²⁺ form NiCo₂(OH)₆ nuclei around Zn(OH)₂ particles for surface energy minimization (Eq. 3).
  - [referenced knowledge] Calcination at 300°C converts Zn(OH)₂ to ZnO and NiCo₂(OH)₆ to NiCo₂O₄ (Eqs. 4 and 5).
  - [image description] SEM images (Fig. 1b–d) show morphology transitions: irregular → well-regulated → aggregated, attributed to alkalinity-induced growth kinetics.
  - [deductive reasoning] Thus, processing via hydrothermal reaction with controlled NH₃·H₂O directly determines the hybrid nanoparticle structure and interfacial arrangement.
### M2  Structure → Properties
- cause: Binary hybrid nanoparticle structure with ZnO/NiCo₂O₄ heterojunctions, mesopores, and controlled morphology (especially ZnO/NiCo₂O₄-7)
- effect: Enhanced complex permittivity (ε' = 6.85, ε'' = 0.50 at 18 GHz), high dielectric loss tangent (ε''/ε' = 0.074), and high attenuation constant (α = 73.64), with negligible magnetic loss due to nonmagnetic nature of both phases
- experiment: Vector network analyzer measurement of complex permittivity and permeability | Vector network analyzer (Agilent N5230A) | params: Frequency range: 2.0–18.0 GHz; sample: ZnO/NiCo₂O₄-paraffin composite (1:1 mass ratio); thickness: 2.5 mm | result: ε' and ε'' increase with NH₃·H₂O content; ε''/ε' peaks at ZnO/NiCo₂O₄-7 (0.074); μ' and μ'' are low and decrease with frequency; no significant magnetic loss observed
  - [image description] TEM and EDS mapping show ZnO and NiCo₂O₄ phases are intimately mixed with interfacial boundaries.
  - [image description] Nitrogen adsorption confirms mesoporous structure (Type IV isotherm, BJH pore size 0–40 nm).
  - [image description] Cole-Cole plots exhibit three semicircles, indicating multiple relaxation processes from ZnO, NiCo₂O₄, and interfacial regions.
  - [referenced knowledge] According to Debye theory, interfacial polarization between dissimilar dielectrics enhances ε'' and ε''/ε'.
  - [experimental result] VSM shows negligible magnetization (Ms = 0.0007 emu/g), confirming nonmagnetic behavior.
  - [deductive reasoning] Thus, the hybrid structure promotes dielectric loss via interfacial polarization and mesoporous scattering, while magnetic loss is absent.
### M3  Properties → Performance
- cause: High dielectric loss tangent (ε''/ε' = 0.074) and high attenuation constant (α = 73.64) in ZnO/NiCo₂O₄-7, coupled with improved impedance matching at high frequencies
- effect: Minimum reflection loss of -33.49 dB at 18.0 GHz with 4.99 mm thickness, meeting the -10 dB absorption threshold over a broad frequency range in Ku-band
- experiment: Reflection loss (RL) calculation using transmission line theory | Vector network analyzer + transmission line model | params: RL calculated from ε_r and μ_r using Eqs. (7) and (8); thickness varied from 1.5 to 5.0 mm | result: ZnO/NiCo₂O₄-7 achieves RL_min = -33.49 dB at 18.0 GHz with d = 4.99 mm; ZnO/NiCo₂O₄-5 and -10 show weaker RL (-6.52 dB and -27.46 dB, respectively)
  - [experimental result] ZnO/NiCo₂O₄-7 exhibits the highest dielectric loss tangent (ε''/ε' = 0.074) and attenuation constant (α = 73.64) among the samples.
  - [image description] Impedance matching parameter Δ is poor at low frequencies but improves at Ku-band (>12 GHz) when thickness exceeds 3.0 mm.
  - [referenced knowledge] According to transmission line theory, RL depends on both α and Δ; high α alone is insufficient without good matching.
  - [experimental result] RL calculation (Eq. 7) using measured ε_r and μ_r confirms ZnO/NiCo₂O₄-7 achieves RL_min = -33.49 dB at 18.0 GHz with d = 4.99 mm.
  - [deductive reasoning] Thus, the combination of high dielectric loss and optimized impedance matching at high frequencies enables exceptional absorption performance.
### M4  Processing → Properties
- cause: Increasing NH₃·H₂O content during hydrothermal synthesis
- effect: Progressive increase in complex permittivity (ε' and ε'') and dielectric loss tangent (ε''/ε') due to enhanced interfacial polarization and particle morphology
- experiment: Dielectric property measurement via vector network analyzer | Vector network analyzer (Agilent N5230A) | params: Frequency: 2.0–18.0 GHz; samples: ZnO/NiCo₂O₄-5, -7, -10; paraffin composite (1:1 mass ratio) | result: ε' increases from 5.78 to 6.96; ε'' increases from 0.39 to 0.67; ε''/ε' increases from 0.068 to 0.097 with increasing NH₃·H₂O
  - [experimental result] NH₃·H₂O concentration was varied (0.5, 0.7, 1.0 mL) in hydrothermal synthesis.
  - [image description] Higher NH₃·H₂O leads to better-regulated morphology (Fig. 1d) and more interfacial boundaries (Fig. 2d).
  - [non-referenced_knowledge] More interfaces increase interfacial polarization, a major contributor to dielectric loss (ε'').
  - [experimental result] Measured ε' and ε'' increase monotonically with NH₃·H₂O (Fig. 5a–b), confirming enhanced dielectric response.
  - [deductive reasoning] Thus, processing via NH₃·H₂O concentration directly tunes dielectric properties by modulating interfacial structure.
