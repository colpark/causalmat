# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116827 (judge only; not shown to staff)
- material: Ti-6Al-4V  elements: ['Ti', 'Al', 'V']  category: ['Metals and Alloys', 'Crystalline Material']
- MST chain: Processing → Structure → Property
## Tetrahedron elements
- **Processing**: Isothermal compression at 750°C with varying strain rates
- **Structure**: Evolution of lamellar (α+β) colonies and grain boundary α phase
- **Properties**: Deformation behavior–mechanical property
- **Performance**: None
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Isothermal compression at 750°C with varying strain rates
- effect: Lamellar (α+β) colonies straighten along hoop tensile stress direction and grain boundary α phase kinks or bends depending on orientation relative to compression axis
- experiment: Microstructural characterization via SEM (BSE) | Scanning Electron Microscopy - Backscattered Electron Imaging | params: Compression specimens sectioned along diameter, equatorial plane observations after polishing and etching with Kroll’s reagent | result: Straightening of (α+β) colonies perpendicular to compression axis and kinked/bent morphology in originally parallel colonies
  - [experimental result] Isothermal compression tests were performed at 750°C with various strain rates up to 50% height reduction.
  - [image description] SEM (BSE) images show straightening of (α+β) colonies perpendicular to compression axis and kinking in initially parallel colonies.
  - [referenced knowledge] Taylor factor determines ease of slip initiation: high-Taylor-factor orientations allow multiple slip systems to activate and accommodate deformation.
  - [non-referenced_knowledge] Orientation of lamellar colonies relative to compression axis affects slip system activation and resulting microstructural evolution.
  - [deductive reasoning] Thus, isothermal compression leads to alignment of lamellar (α+β) colonies along hoop stress direction and localized bending/kinking in less favorably oriented regions.
### M2  Structure → Property
- cause: Evolved microstructure with aligned and kinked lamellar (α+β) colonies
- effect: Anisotropic deformation behavior and localized hardening/softening during hot compression
- experiment: Two-point statistical modeling of deformed microstructures | Statistical continuum modeling using two-point correlation functions | params: Vector magnitude and angle resolved two-point statistics from SEM (BSE) montages, strain rate tensor input | result: Simulated two-point statistics match experimental observations for most strain rates, showing central peak deformation consistent with grain shape changes
  - [non-referenced_knowledge] Two-point statistics calculated from SEM (BSE) images capture grain morphology, size, and spatial correlations in the microstructure.
  - [image description] Simulated two-point statistics reproduce experimental observations for most strain rates, indicating accurate modeling of deformation-induced microstructural changes.
  - [referenced knowledge] Lin et al. showed that two-point statistics can evolve under strain to predict microstructural deformation patterns.
  - [experimental result] Deformation alters vector length distributions in two-point statistics, reflecting grain elongation and rotation consistent with observed microstructural features.
  - [inductive reasoning] Therefore, the evolved microstructure with aligned and kinked lamellae directly influences the anisotropic mechanical properties by controlling localized strain accommodation and hardening behavior.
### M3  Processing → Property
- cause: Isothermal compression at 750°C with varying strain rates
- effect: Strain rate dependent deformation behavior characterized by overestimation in simulated two-point statistics at high strain rates
- experiment: Error analysis of simulated vs. experimental two-point statistics | Quantitative comparison using point-by-point error metrics | params: Average error calculated over 20×20 grid centered on central peak; comparisons between individual SEM (BSE) images and large-area montages | result: Average error decreases with increasing strain rate (except at 10 s⁻¹), suggesting better model performance at moderate strain rates
  - [experimental result] Isothermal compression was conducted at strain rates ranging from 10⁻³ to 10 s⁻¹ at 750°C.
  - [image description] Error plots show overestimation of deformation in simulated two-point statistics, particularly at high |r| values and in high strain rate cases.
  - [referenced knowledge] Corson described volume fraction-based limits for two-point statistics which are used to validate model accuracy.
  - [non-referenced_knowledge] Artificial lengthening of vectors during renormalization can mimic tension under compression, introducing error in statistical modeling.
  - [deductive reasoning] Therefore, higher strain rates introduce greater complexity and error in statistical modeling, implying a strain rate-dependent deviation from idealized mechanical behavior predictions.
