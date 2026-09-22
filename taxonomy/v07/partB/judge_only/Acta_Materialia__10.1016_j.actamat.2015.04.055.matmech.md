# MatMech content for Acta_Materialia/10.1016_j.actamat.2015.04.055 (judge only; not shown to staff)
- material: γ-TiAl based alloys (TNM and TNM0.75C)  elements: ['Ti', 'Al', 'C', 'Mo']  category: ['Metals and Alloys', 'Crystalline Material']
- MST chain: Processing → Structure → Properties
## Tetrahedron elements
- **Processing**: Vacuum arc remelting (VAR), vacuum induction melting (VIM), hot isostatic pressing (HIP), hot forging, homogenization heat-treatment
- **Structure**: Multi-phase microstructure consisting of γ, α2, and βo phases; C enrichment in α2 phase, depletion in βo phase, and segregation at phase interfaces
- **Properties**: hardness–mechanical property
- **Performance**: Increased high-temperature strength and creep resistance due to C addition
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Hot isostatic pressing (HIP) at 1200°C for 4 h at 200 MPa followed by furnace cooling
- effect: Formation of structurally homogeneous microstructure in TNM and TNM0.75C alloys
- experiment: Microstructural analysis by SEM-BSE | Scanning Electron Microscopy - Backscattered Electron imaging | params: Observation of TNM and TNM0.75C alloys after hot forging and homogenization heat-treatment | result: TNM alloy shows predominantly globular morphologies; TNM0.75C exhibits coarse lamellar features due to C-induced phase transformation changes
  - [experimental result] Ingot processing includes HIP at 1200°C under 200 MPa pressure with subsequent furnace cooling.
  - [image description] SEM-BSE images show globally uniform microstructures in both alloys after HIP and heat-treatment.
  - [referenced knowledge] Homogenization heat-treatment after forging promotes structural homogeneity.
  - [non-referenced_knowledge] Phase transformation behavior during cooling determines final microstructural morphology.
  - [deductive reasoning] Thus, HIP and controlled cooling produce structurally homogeneous γ-TiAl alloys suitable for microstructural analysis.
### M2  Structure → Property
- cause: C enrichment in α₂ phase and segregation at phase interfaces
- effect: Increased hardness of γ and α₂ phases in TNM0.75C alloy
- experiment: Nanoindentation measurements | Instrumented nanoindentation with cube corner indenter | params: Indentation depth ~60 nm, 30–50 indents per phase, fused silica calibration | result: Hardness increased from 7.49 GPa to 8.46 GPa (γ phase), 8.74 GPa to 9.92 GPa (α₂ phase) with C addition
  - [experimental result] APT analysis shows C concentrations of 0.3 at.% in γ phase and 1.2 at.% in α₂ phase in TNM0.75C alloy.
  - [image description] Nanoindentation reveals significant hardness increases in both γ and α₂ phases with C addition.
  - [referenced knowledge] ΔH ∝ √c relation predicts hardness increase proportional to square root of solute concentration.
  - [non-referenced_knowledge] Interstitial C atoms create local stress fields that hinder dislocation glide in ordered L1₀ structures.
  - [deductive reasoning] Therefore, C dissolved in γ and α₂ phases strengthens them via solid solution hardening mechanism.
### M3  Structure → Performance
- cause: Suppression of ωo phase formation in βo matrix
- effect: Softening of βo phase in TNM0.75C alloy despite higher Mo content
- experiment: TEM analysis of βo + ωo microstructure | Transmission electron microscopy with selected area diffraction | params: Observation of TNM and TNM0.75C alloys in ⟨111⟩βo zone axis | result: Fine ωo precipitates observed in TNM alloy; none detected in TNM0.75C alloy
  - [experimental result] APT shows 2 at.% higher Mo in βo phase of TNM0.75C alloy due to reduced βo fraction.
  - [image description] TEM confirms absence of ωo precipitates in TNM0.75C βo phase while present in TNM alloy.
  - [referenced knowledge] ωo precipitates in βo matrix contribute significantly to hardness of βo + ωo mixture.
  - [non-referenced_knowledge] Precipitation hardening depends on dispersion of secondary phase particles within matrix.
  - [inductive reasoning] Therefore, absence of ωo precipitates in TNM0.75C βo phase dominates over Mo-induced solid solution hardening, resulting in net softening.
### M4  Processing → Structure
- cause: Vacuum arc remelting (VAR) for TNM vs. vacuum induction melting (VIM) for TNM0.75C alloy
- effect: Different phase fractions: TNM has 19% βo phase vs. TNM0.75C has only 2% βo phase
- experiment: XRD phase quantification | X-ray diffraction with Rietveld analysis | params: Quantitative phase analysis of forged and heat-treated alloys | result: TNM: 70% γ, 11% α₂, 19% βo; TNM0.75C: 61% γ, 37% α₂, 2% βo
  - [experimental result] TNM alloy was remelted twice by VAR, TNM0.75C once by VIM before casting.
  - [image description] XRD phase quantification shows βo phase reduced from 19% to 2% with C addition.
  - [referenced knowledge] C strongly stabilizes α/α₂ phase in TiAl alloys.
  - [non-referenced_knowledge] Melting route affects solidification mode and thus phase selection during solidification.
  - [deductive reasoning] Therefore, VIM melting combined with C addition suppresses βo phase formation through α/α₂ stabilization.
