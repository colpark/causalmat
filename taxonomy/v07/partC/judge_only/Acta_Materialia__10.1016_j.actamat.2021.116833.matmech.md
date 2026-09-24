# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116833 (judge only; not shown to staff)
- material: Potassium Sodium Niobate (KNN)  elements: ['K', 'Na', 'Nb', 'O']  category: ['Ceramic', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Solid-state synthesis using orthorhombic and monoclinic Nb2O5 reactants, ball milling, calcination at 950°C
- **Structure**: Chemical inhomogeneity observed in calcined powder, multiple perovskite phases formed
- **Properties**: Piezoelectric coefficients–electromechanical property
- **Performance**: Poor reproducibility of electromechanical properties in industrial applications
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Use of monoclinic Nb2O5 reactant during solid-state synthesis
- effect: Chemical inhomogeneity and formation of multiple perovskite phases with distinct lattice constants in calcined KNN powder
- experiment: In-situ temperature-dependent XRD | X-ray diffraction | params: Heating from RT to 1100°C at 1°C/min up to 650°C then 2.5°C/min up to 1100°C; continuous measurement | result: KNN-M and BZ6-M show two distinct diffraction peaks at ~32° and ~31.5° 2θ, indicating multiple perovskite phases formed sequentially during heating
  - [experimental result] In-situ XRD shows two distinct perovskite phase formations in KNN-M and BZ6-M at different temperatures (400°C and 450°C).
  - [experimental result] DTG data indicates separated decomposition peaks for Na2CO3 (~470°C) and K2CO3 (~625°C) when monoclinic Nb2O5 is used.
  - [non-referenced_knowledge] Smaller Nb2O5 particles have higher curvature, surface energy, and reduced diffusion distance, favoring faster reaction with Na+ ions.
  - [deductive reasoning] Larger Nb2O5 particles react later at higher temperatures, allowing K+ ions to dominate in those regions.
  - [inductive reasoning] This results in spatially separated Na-rich and K-rich KNN domains, forming multiple perovskite phases with distinct lattice constants.
### M2  Processing → Structure
- cause: Calcination at high temperature (~950°C)
- effect: Partial chemical homogenization of KNN-M and BZ6-M samples
- experiment: In-situ XRD at high temperature | X-ray diffraction | params: Heating up to 1100°C; peak fitting using Lorentzian profiles | result: At ~950–1000°C, separated 110C peaks merge into a single broad peak in KNN-M and BZ6-M, indicating partial homogenization
  - [experimental result] At ~950°C, separated 110C diffraction peaks in KNN-M and BZ6-M merge into a single broader peak.
  - [image description] Statistical fitting of peak profiles confirms reduction in multiple phase contributions.
  - [referenced knowledge] Surface energy provides driving force for diffusion and homogenization in ceramics.
  - [deductive reasoning] Homogenization efficiency is lower in monoclinic Nb2O5-derived samples due to larger initial compositional differences.
  - [inductive reasoning] Therefore, high-temperature calcination partially homogenizes chemically inhomogeneous KNN ceramics, especially those derived from monoclinic Nb2O5.
### M3  Structure → Properties
- cause: Chemical inhomogeneity in A-site composition (K/Na ratio variation)
- effect: Variation in Curie temperature (TC) and piezoelectric performance of sintered KNN ceramics
- experiment: Dielectric and piezoelectric property measurements | Electromechanical testing | params: Measurements on sintered KNN-O and KNN-M ceramics | result: KNN-M exhibits higher TC and greater variability in dielectric and ferroelectric properties compared to KNN-O
  - [experimental result] KNN-M, which has more severe chemical inhomogeneity, shows significantly different dielectric and ferroelectric properties compared to KNN-O.
  - [referenced knowledge] Piezoelectric properties are highly sensitive to composition and structural ordering.
  - [non-referenced_knowledge] Variations in K/Na ratio create local strain fields that interfere with coherent polarization switching.
  - [deductive reasoning] Thus, chemical inhomogeneity directly reduces the reproducibility and quality of piezoelectric performance in KNN ceramics.
### M4  Properties → Performance
- cause: Variability in piezoelectric coefficient (d33)
- effect: Poor reproducibility of electromechanical performance in industrial applications
- experiment: Comparative electrical characterization of sintered ceramics | Piezoelectric and dielectric testing | params: Measurement of d33, TC, and ferroelectric hysteresis loops | result: Significant differences found between KNN-O and KNN-M, while BZ6-O and BZ6-M show more similar properties due to improved homogenization
  - [experimental result] KNN-M samples show significant variability in TC and ferroelectric properties compared to KNN-O.
  - [non-referenced_knowledge] Industrial applications require tight tolerances on electromechanical parameters for consistent performance.
  - [referenced knowledge] Poor reproducibility of piezoelectric properties hinders large-scale manufacturing and reliability assurance.
  - [deductive reasoning] Therefore, chemical inhomogeneity induced by processing leads to inconsistent piezoelectric performance, limiting the practical utility of KNN ceramics.
