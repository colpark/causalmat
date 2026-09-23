# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116763 (judge only; not shown to staff)
- material: Cr7Mn25Co9Ni23Cu36  elements: ['Cr', 'Mn', 'Co', 'Ni', 'Cu']  category: ['Metals and Alloys', 'Crystalline Material']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Heat treatment at various temperatures (200, 400, 600, 800, and 1000°C) for 2 hours
- **Structure**: Formation of sigma phase at 800°C, two FCC solid solution phases at lower temperatures
- **Properties**: yield strength–mechanical property, ultimate tensile strength–mechanical property, elongation to fracture–mechanical property
- **Performance**: Decrease in tensile mechanical properties due to sigma phase formation
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Heat treatment at 800°C for 2 hours
- effect: Formation of Cr- and Co-rich sigma phase with tetragonal structure
- experiment: Microstructural analysis after heat treatment | Scanning Electron Microscopy (SEM) and Transmission Electron Microscopy (TEM) | params: Samples heat treated at 800°C for 2 hours followed by water quenching | result: New phase observed as white spots in SEM images and identified as sigma phase via TEM diffraction patterns and EDS elemental analysis
  - [image description] SEM images show no sigma phase at temperatures below 800°C but observe it at 800°C (Fig. 1d).
  - [image description] TEM confirms the sigma phase has a tetragonal structure rich in Cr and Co (Fig. 2).
  - [experimental result] Thermodynamic calculations indicate sigma phase stability below ~850°C (Fig. 3).
  - [non-referenced_knowledge] The sigma phase has lower Gibbs energy than FCC phases at 800°C due to favorable enthalpy of mixing between Co and Cr.
  - [deductive reasoning] Thus, heat treatment at 800°C enables diffusion-controlled phase transformation favoring sigma phase formation.
### M2  Structure → Performance
- cause: Formation of sigma phase
- effect: Decrease in tensile mechanical properties including yield strength, ultimate tensile strength, and elongation to fracture
- experiment: Tensile testing of heat-treated samples | Tensile test | params: Room temperature tensile tests on samples heat treated at various temperatures (200–1000°C) for 2 hours | result: Yield strength drops from 581 MPa (600°C) to 303 MPa (800°C), UTS from 829 MPa to 530 MPa, and elongation from 22% to 15%
  - [image description] Figure 7b shows significant drop in yield strength and elongation after 800°C heat treatment.
  - [image description] Sigma phase precipitates are not homogeneously distributed and vary in size (up to hundreds of nm), as seen in Fig. 1d.
  - [non-referenced_knowledge] Inhomogeneous second-phase distribution creates weak interfaces and stress concentration sites that initiate fracture.
  - [deductive reasoning] Therefore, sigma phase formation under 800°C heat treatment degrades tensile mechanical performance.
### M3  Processing → Structure
- cause: Heat treatment at 600°C for extended durations (>8h)
- effect: Delayed formation of sigma phase due to sluggish solid-state diffusion kinetics
- experiment: Microstructural evolution with time at 600°C | Scanning Electron Microscopy (SEM) | params: Samples heat treated at 600°C for 4, 6, 8, 10, and 12 hours | result: Sigma phase appears after 8-hour treatment and increases in volume fraction with longer duration
  - [experimental result] CALPHAD predicts sigma phase presence below ~850°C, but experimentally observed only after 8-hour treatment at 600°C (Fig. 5d).
  - [image description] SEM images show gradual increase in sigma phase fraction with increasing treatment time at 600°C (Fig. 5).
  - [non-referenced_knowledge] Diffusion kinetics are slower at lower temperatures, delaying phase transformation.
  - [deductive reasoning] Hence, sigma phase formation at 600°C is kinetically limited and requires sufficient annealing time.
