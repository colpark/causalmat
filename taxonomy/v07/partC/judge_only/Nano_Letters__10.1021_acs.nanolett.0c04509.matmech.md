# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c04509 (judge only; not shown to staff)
- material: CdSe nanoplatelets  elements: ['Cd', 'Se']  category: ['Nanomaterial', 'Crystalline Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Synthesis of CdSe nanoplatelets with oleate ligands and drop-casting on gold surfaces
- **Structure**: Rectangular shape with finite length and width, thickness of 5.5 ML (1.65 nm) and 7.5 ML (2.25 nm), edge facets with trap states
- **Properties**: Conduction band density of states–electronic property, trap states–electronic property
- **Performance**: Electron confinement and behavior in quasi-2D systems, potential for optoelectronic applications
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Synthesis of CdSe nanoplatelets with oleate ligands and drop-casting on gold surfaces
- effect: CdSe nanoplatelets have rectangular shape with finite length and width, thickness of 5.5 ML (1.65 nm) and 7.5 ML (2.25 nm), and edge facets that host trap states
- experiment: Transmission electron microscopy (TEM) | Structural characterization | params: Room temperature measurements, NPLs with different thicknesses (5.5 ML and 7.5 ML) | result: Rectangular shapes of NPLs with lateral sizes of (21±2)×(7±1) nm² for 5.5-ML-thick NPLs and (45±10)×(9±1) nm² for 7.5-ML-thick NPLs; thickness confirmed by optical properties
  - [experimental result] CdSe NPLs are synthesized with a discrete number of monolayers, yielding quantized thicknesses of 5.5 or 7.5 ML.
  - [image description] Figure shows rectangular shapes and thickness-dependent exciton energies in optical spectra.
  - [referenced knowledge] Optical absorption features correspond to 1S electron and heavy/light hole transitions dependent on quantum confinement.
  - [non-referenced_knowledge] Monolayer-controlled synthesis results in well-defined 2D structures with predictable electronic behavior.
  - [deductive reasoning] Therefore, processing controls both vertical and lateral confinement through layer-by-layer growth and ligand-mediated self-assembly.
### M2  Structure → Property
- cause: CdSe nanoplatelets have rectangular shape with finite length and width, thickness of 5.5 ML (1.65 nm) and 7.5 ML (2.25 nm), and edge facets that host trap states
- effect: Conduction band density of states exhibits Van Hove singularities instead of typical 2D quantum well behavior
- experiment: Scanning tunneling spectroscopy (STS) | Electronic structure probing | params: Low-temperature measurements (5 K), flat-lying and stacked NPL configurations | result: Distinct peaks in conduction band instead of stepwise function; peak spacing consistent with tight-binding calculations of finite-length NPLs
  - [experimental result] Flat-lying NPLs show distinct conduction band peaks inconsistent with free 2D electron motion.
  - [image description] Figure compares theoretical DOS of finite-length NPLs with experimental STS data, showing matching Van Hove singularity patterns.
  - [referenced knowledge] Tight-binding models predict that reduced lateral dimensionality transforms quantum well DOS into oscillating Van Hove features.
  - [non-referenced_knowledge] Electron wave function is confined laterally by NPL edges acting as potential barriers, modifying the expected 2D behavior.
  - [inductive reasoning] Hence, finite length and width of NPLs cause deviation from ideal 2D DOS toward quasi-1D-like Van Hove singularities.
### M3  Property → Performance
- cause: Conduction band density of states exhibits Van Hove singularities instead of typical 2D quantum well behavior
- effect: Electron confinement and behavior in quasi-2D systems deviate from ideal 2D model, affecting optoelectronic performance
- experiment: Differential conductance measurements under varying set-point currents | Charge state analysis | params: Current-induced shifts in conduction band onset, cryogenic conditions (5 K) | result: Stepwise current changes attributed to charging/discharging of deep trap states; electrostatic shifts exceeding 500 meV alter DOS features
  - [experimental result] Stacked NPLs exhibit sudden current shifts at positive bias, indicating charging of deep trap states.
  - [image description] Figure shows spectral diffusion and electrostatic shifts in differential conductance upon trap-state occupation.
  - [referenced knowledge] Surface trap states limit carrier mobility and introduce non-radiative recombination pathways in colloidal nanostructures.
  - [non-referenced_knowledge] Coulomb blockade from trapped charges modifies local electrostatic environment and alters observed DOS features.
  - [deductive reasoning] Thus, non-ideal DOS combined with trap-state effects reduces performance in optoelectronic applications unless mitigated via passivation or heterostructuring.
