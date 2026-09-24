# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c05013 (judge only; not shown to staff)
- material: zigzag graphene nanoribbons (zz-GNRs)  elements: ['C', 'Si']  category: ['Nanomaterial', 'Crystalline Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Epitaxial growth on mesa-structured SiC(0001) by sublimation epitaxy
- **Structure**: Suspended monolayer zz-GNRs with lower edge merging into the SiC substrate
- **Properties**: ballistic transport–electrical property
- **Performance**: Robust and spin-polarized 1D transport channel without external magnetic fields
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Epitaxial growth on mesa-structured SiC(0001) by sublimation epitaxy
- effect: zz-GNRs are suspended across SiC facets with the lower edge merging into the SiC substrate
- experiment: Growth and structural characterization of zz-GNRs | SEM, STM, TEM | params: Mesa-structured SiC(0001), sublimation epitaxy at >1800°C under Ar atmosphere | result: GNRs exhibit ~27° facet angle, 30–40 nm width, and bonding at the lower edge confirmed by cross-sectional TEM
  - [experimental result] GNRs were grown via sublimation epitaxy at temperatures above 1800 °C under Ar atmosphere.
  - [image description] Figure 1a and inset show SEM and STM images of GNRs aligned along the zz direction on mesa structures.
  - [image description] Cross-sectional TEM confirms bonding of the lower edge to the SiC surface.
  - [referenced knowledge] Previous studies confirm edge bonding to the SiC substrate after growth.
  - [non-referenced_knowledge] Facet geometry and thermal expansion differences during cooling influence ribbon morphology and edge bonding.
  - [deductive reasoning] Therefore, epitaxial growth on structured SiC results in suspended GNRs with one edge bonded to the substrate.
### M2  Structure → Performance
- cause: Suspended monolayer zz-GNRs with lower edge merging into the SiC substrate
- effect: Robust and spin-polarized 1D transport channel without external magnetic fields
- experiment: Scanning tunneling spectroscopy and transport measurements | STS, ARPES, ballistic transport | params: Low-temperature measurements, lock-in technique (20 meV, 1500 Hz) | result: STS reveals a peak at Fermi energy localized at the lower edge, indicating a topological 1D surface state; transport shows $G = e^2/h$ over micrometer lengths
  - [experimental result] STS spectra reveal a peak at the Fermi energy localized at the lower edge of the GNR.
  - [image description] Figure 3d shows nonlinear increase in energy splitting near the edge, indicating a dispersive edge state.
  - [image description] Tight binding calculations incorporating a Haldane term reproduce the observed edge state dispersion.
  - [non-referenced_knowledge] Time-reversal symmetry breaking is necessary to explain the observed $e^2/h$ conduction and absence of backscattering.
  - [non-referenced_knowledge] Strain from thermal mismatch and Coulomb interactions may lead to spontaneous symmetry breaking without an external magnetic field.
  - [deductive reasoning] Thus, the edge-substrate interaction enables a chiral, topologically protected state that supports robust ballistic transport.
