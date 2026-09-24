# MatMech content for Advanced_Materials/10.1002_adma.202006689 (judge only; not shown to staff)
- material: Sb2(S,Se)3  elements: ['Sb', 'Se', 'S']  category: ['Crystalline Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Sequential coevaporation of Sb2Se3 and S powders in a vacuum chamber with controlled source-substrate distance and temperature
- **Structure**: Formation of Sb2(S,Se)3 alloy with varying crystal orientations and grain sizes
- **Properties**: bandgap–optical property, power conversion efficiency–electrical property
- **Performance**: Achieved a power conversion efficiency of 8.0% in solar cells
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Sequential coevaporation of Sb2Se3 and S powders in a vacuum chamber with controlled source-substrate distance and temperature
- effect: Formation of Sb2(S,Se)3 alloy with varying crystal orientations and grain sizes
- experiment: X-ray diffraction (XRD) | XRD | params: Analysis of crystallinity and texture coefficient ratios between different crystal planes | result: Texture coefficient ratio (TC(221)/TC(120)) indicates vertical alignment of ribbons in S2 and S3 films compared to S1.
  - [non-referenced_knowledge] Source–substrate distance determines the kinetic energy of vaporized precursor materials, which influences homogeneity and crystal orientation.
  - [experimental result] Increasing the source–substrate distance results in lower kinetic energy of vapor particles due to collisions, favoring specific crystal orientations.
  - [image description] Texture coefficient analysis reveals that S2 and S3 exhibit higher TC(221)/TC(120) ratios, indicating more vertical ribbon alignment compared to S1.
  - [deductive reasoning] Proper deposition conditions (10 cm source–substrate distance, 315°C substrate temperature) yield the most vertical alignment of ribbons.
### M2  Structure → Property
- cause: Vertical alignment of (Sb4Se6)n ribbons
- effect: Improved charge transport and reduced bandgap
- experiment: UV–vis absorption spectroscopy | UV–vis | params: Bandgap estimation from (αhν)² vs hν plots | result: Bandgaps of S1, S2, and S3 are 1.36 eV, 1.26 eV, and 1.19 eV, respectively.
  - [non-referenced_knowledge] Vertical alignment of ribbons reduces resistance along the transport direction, enhancing electrical conductivity.
  - [experimental result] S2 and S3 show higher Jsc values (~30 mA/cm²), indicating improved charge generation and transport due to favorable crystal orientation.
  - [image description] S2 and S3 exhibit lower bandgaps (1.26 eV and 1.19 eV) compared to S1 (1.36 eV), allowing better absorption of low-energy photons.
  - [deductive reasoning] Gradient band structure in S2 and S3 promotes directional carrier movement toward respective charge transport layers.
### M3  Property → Performance
- cause: Reduced bandgap and improved charge transport
- effect: Increased power conversion efficiency (PCE) in solar cells
- experiment: Photovoltaic performance measurement | Current–voltage (J–V) characterization | params: AM 1.5G illumination, device configuration: FTO/CdS/Sb2(S,Se)3/Spiro-OMeTAD/Au | result: Device S2 achieved a PCE of 8.0%, significantly higher than S1 (6.23%) and S3 (6.43%).
  - [experimental result] S2 exhibits the lowest interfacial defect density (3.00 × 10¹⁰ cm⁻²), minimizing non-radiative recombination.
  - [image description] S2 achieves the highest Jsc (30.2 mA/cm²) and FF (57.9%), leading to a PCE of 8.0%.
  - [non-referenced_knowledge] Defect tolerance in 1D Sb2(S,Se)3 structure allows high performance despite slight stoichiometric deviations.
  - [deductive reasoning] Optimized processing conditions enable structural features that maximize light absorption and minimize carrier loss, achieving the highest reported PCE for vapor-deposited Sb2(S,Se)3 solar cells.
