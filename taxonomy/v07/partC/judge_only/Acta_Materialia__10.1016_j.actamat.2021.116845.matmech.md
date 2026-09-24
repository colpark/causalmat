# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116845 (judge only; not shown to staff)
- material: 4H-SiC  elements: ['Si', 'C']  category: ['Ceramic', 'Crystalline Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property
## Tetrahedron elements
- **Processing**: Selected-area He+ irradiation with constrained lateral expansion
- **Structure**: Anisotropic defect distribution with interstitial defects in the [0004] direction and vacancies/carbon antisite defects in the [1120] and [1010] directions
- **Properties**: Swelling–mechanical property
- **Performance**: Degradation of mechanical properties due to anisotropic swelling
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Selected-area He+ irradiation with constrained lateral expansion
- effect: Anisotropic defect distribution with interstitial defects in the [0004] direction and vacancies/carbon antisite defects in the [1120] and [1010] directions
- experiment: TEM and STEM characterization of defect distribution | Transmission Electron Microscopy (TEM), Scanning Transmission Electron Microscopy (STEM) | params: Observation under different diffraction conditions using g = [0004], [1120], and [1010]; quantification of black spot defect (BSD) size and number density | result: Interstitial-type BSDs preferentially formed in the [0004] orientation, while negative volume defects dominated in [1120] and [1010]. Number density and average size of BSDs were significantly higher in [0004] than in other orientations.
  - [experimental result] He+ irradiation introduces Frenkel pairs (interstitials and vacancies) in SiC.
  - [experimental result] Under constraint, compressive stress develops in lateral directions ([1120] and [1010]) due to restricted swelling.
  - [referenced knowledge] Interstitials are mobile at room temperature (migration energy ~1.5 eV for Si, ~0.7 eV for C), whereas vacancies are not (~3.2–5.2 eV).
  - [non-referenced_knowledge] Compressive stress likely inhibits interstitial loop nucleation in planes perpendicular to the stress axis.
  - [experimental result] Interstitials redistribute to the [0004] direction where expansion is unconstrained, forming larger and denser BSDs.
  - [deductive reasoning] Vacancies and/or C_Si defects dominate in constrained directions due to their negative volume effect and inhibited interstitial accumulation.
### M2  Structure → Property
- cause: Anisotropic defect distribution with interstitial defects in the [0004] direction and vacancies/carbon antisite defects in the [1120] and [1010] directions
- effect: Swelling–mechanical property degradation
- experiment: EBSD stress mapping and defect-induced strain analysis | Electron Backscatter Diffraction (EBSD) | params: Stress measurement in X ([1120]), Y ([1010]), and Z ([0004]) directions; correlation between stress state and defect distribution | result: Large compressive stress (-0.94 GPa in X, -1.15 GPa in Y) observed in constrained directions, with minimal stress in Z. Anisotropic defect distribution correlates with differential strain and swelling.
  - [experimental result] Interstitial-type BSDs in [0004] direction lead to local lattice expansion as seen in HR-TEM.
  - [experimental result] C_Si and/or C–C bond formation in [1120] and [1010] detected by EELS indicates negative-volume defects.
  - [non-referenced_knowledge] Interstitials expand lattice locally; C_Si defects contract it, creating opposing volumetric effects.
  - [deductive reasoning] This anisotropic expansion/contraction results in internal stress and localized deformation.
  - [experimental result] Measured compressive stress in lateral directions supports this mechanism of strain imbalance.
  - [inductive reasoning] Internal stress degrades mechanical properties, particularly under load or thermal cycling.
