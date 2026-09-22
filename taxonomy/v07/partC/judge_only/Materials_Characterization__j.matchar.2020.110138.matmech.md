# MatMech content for Materials_Characterization/j.matchar.2020.110138 (judge only; not shown to staff)
- material: AISI 420 martensitic stainless steel  elements: ['Fe', 'C', 'Cr', 'Mn', 'Si', 'P', 'S']  category: ['Metals and Alloys', 'Crystalline Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Laser cladding using a 2.5 kW fiber-connected diode laser with powder feed rate of 20 g/min and laser speed of 10 mm/s
- **Structure**: Columnar and equiaxed prior austenite grains (PAGs); martensite lath and plate substructures; no retained austenite detected; grain size and aspect ratio vary across bead zone, dilution zone, and interface zone
- **Properties**: Grain Orientation Spread (GOS)–microstructural deformation metric, Image Quality (IQ)–crystallographic imperfection metric
- **Performance**: Inverse correlation between IQ and residual stress (RS) enables IQ to serve as an alternative method for RS distribution mapping in laser-cladded coatings
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Laser cladding using a 2.5 kW fiber-connected diode laser with powder feed rate of 20 g/min and laser speed of 10 mm/s
- effect: Columnar and equiaxed prior austenite grains (PAGs); martensite lath and plate substructures; grain size and aspect ratio vary across bead zone, dilution zone, and interface zone
- experiment: EBSD analysis of prior austenite grain (PAG) maps and inverse pole figure (IPF) | Electron Backscatter Diffraction (EBSD) | params: Step size of 0.1 μm, three scan areas (BZ center, DZ center, DZ interface), Kurdjumov–Sachs orientation relationship with tolerances of 5°, 2°, and 6° | result: PAGs in BZ are equiaxed (avg. size ~23.7 μm, aspect ratio 3); DZ center shows mixed equiaxed/columnar (avg. size ~26.1 μm, aspect ratio 4); DZ interface shows long columnar grains (avg. size ~35.1 μm, aspect ratio 6)
  - [experimental result] Laser cladding uses a 2.5 kW laser at 10 mm/s speed with 20 g/min powder feed rate, creating a molten pool with high cooling rates (~14,580 °C/s).
  - [non-referenced_knowledge] The high cooling rate promotes rapid solidification and martensitic transformation without retained austenite.
  - [image description] EBSD PAG maps show equiaxed grains in BZ, mixed grains in DZ center, and long columnar grains in DZ interface.
  - [referenced knowledge] Columnar grains nucleate epitaxially from the HAZ interface and grow with the thermal gradient, while equiaxed grains form in the center due to lower G/R ratio.
  - [experimental result] The aspect ratio of PAGs (3 in BZ, 4 in DZ-C, 6 in DZ-I) confirms directional solidification and thermal gradient effects.
  - [deductive reasoning] Thus, processing parameters (laser power, speed, feed rate) determine thermal gradients, which control PAG morphology, which in turn dictates martensitic substructure.
### M2  Structure → Properties
- cause: Columnar and equiaxed prior austenite grains; martensite lath and plate substructures; varying grain size and aspect ratio across bead zone, dilution zone, and interface zone
- effect: Grain Orientation Spread (GOS) – microstructural deformation metric; Image Quality (IQ) – crystallographic imperfection metric
- experiment: EBSD Grain Orientation Spread (GOS) and Image Quality (IQ) measurements | Electron Backscatter Diffraction (EBSD) | params: GOS calculated as mean misorientation within grains; IQ measured as pattern sharpness; step size 0.1 μm; confidence index >0.1; minimum grain size 2 pixels | result: BZ and HAZ show high GOS (26–59% grains with 3°–5° misorientation); DZ shows low GOS (65–78% grains with 0°–3° misorientation); IQ inversely correlates with residual stress (IQ range: 142–485)
  - [non-referenced_knowledge] Martensitic transformation in laser-cladded AISI 420 MSS involves volume changes and high dislocation densities.
  - [image description] EBSD GOS maps reveal higher misorientation (3°–5°) in BZ and HAZ (26–59% of grains) compared to DZ (low GOS in 65–78% of grains).
  - [referenced knowledge] High GOS indicates high intragranular lattice distortion from rapid cooling and phase transformation.
  - [image description] EBSD IQ maps show low values (dark blue) at top of BZ and HAZ, indicating high strain; high values (light yellow/red) in DZ center, indicating low strain.
  - [referenced knowledge] IQ decreases with increasing dislocation density and lattice distortion due to degraded Kikuchi pattern sharpness.
  - [deductive reasoning] Thus, the structural heterogeneity (grain morphology, substructure type, size) directly determines the measured properties: GOS and IQ.
### M3  Properties → Performance
- cause: Grain Orientation Spread (GOS) – microstructural deformation metric; Image Quality (IQ) – crystallographic imperfection metric
- effect: Inverse correlation between IQ and residual stress (RS) enables IQ to serve as an alternative method for RS distribution mapping in laser-cladded coatings
- experiment: Correlation of EBSD IQ with XRD-measured residual stress | X-ray Diffraction (XRD) and EBSD | params: Residual stress measured by XRD in earlier study [6,19]; IQ values extracted from EBSD scans at same locations | result: IQ is inversely proportional to RS: low IQ corresponds to high tensile stress (BZ top, HAZ); high IQ corresponds to compressive stress (DZ center); strong correlation observed in spatial profiles.
  - [referenced knowledge] Residual stress was experimentally measured by XRD in earlier studies, showing tensile stress in BZ and HAZ, compressive stress in DZ.
  - [image description] EBSD IQ maps show low values (blue) at BZ top and HAZ (high stress), and high values (yellow/red) in DZ center (low stress).
  - [referenced knowledge] IQ decreases with increasing lattice distortion caused by residual stress.
  - [experimental result] The spatial trend of IQ variation across BZ, DZ, and HAZ mirrors the RS profile from XRD.
  - [deductive reasoning] Therefore, IQ can be used as an alternative, high-resolution method to map residual stress distribution without XRD.
