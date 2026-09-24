# MatMech content for Advanced_Materials/10.1002_adma.202007154 (judge only; not shown to staff)
- material: Polymeric microparticles (PMPs)  elements: ['C', 'H', 'O', 'Fe', 'Na']  category: ['Polymer', 'Composite Material', 'Nanomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Confinement-free fluid instability induced by superamphiphobic surface (SAPS) at ambient temperature
- **Structure**: Spherical particles, core–shell particles, microcapsules, and necklace-like microfibers
- **Properties**: Fluorescence–optical property, magnetic behavior–magnetic property
- **Performance**: Potential applications in optoelectronic devices, antigen detection, and sustained-release medicine
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Confinement-free fluid instability induced by superamphiphobic surface (SAPS) at ambient temperature
- effect: Polymeric solution columns break up into uniform droplets then form spherical particles spontaneously in seconds
- experiment: PRI-induced droplet formation | Optical microscopy and SEM imaging | params: PEO aqueous solution, 2 wt%, drawn filament length varied, SAPS with ultralow surface energy (~0.41 mN/m) | result: Uniform spherical droplets formed within seconds; particle size ranged from ~1 μm to 1 mm depending on initial column diameter
  - [non-referenced_knowledge] Superamphiphobic surfaces have ultralow surface energy (~0.41 mN/m), minimizing γSV according to the Good-Girifalco equation
  - [deductive reasoning] Maximizing γLS favors the growth of PRI instabilities as shown by theoretical calculations
  - [image description] Figure shows spontaneous breakup of PEO solution columns on SAPS into uniform droplets without external heating or confinement
  - [experimental result] Droplets were nearly spherical because their radius was much smaller than the capillary length (~2.7 mm)
  - [experimental result] As solvent evaporates, the spherical shape becomes more precise rendering spherical PMPs
### M2  Structure → Property
- cause: Spherical particles formed via PRI
- effect: Narrow size distributions indicating excellent size controllability (CV < 10%)
- experiment: Size distribution analysis | SEM and optical microscopy | params: Various rotation speeds of microfluidic spinning instrument, different polymer concentrations | result: Coefficient of variation (CV) < 10% for all tested conditions, demonstrating excellent size control
  - [non-referenced_knowledge] Droplet size depends on wavelength of fastest unstable mode (λ*), which is determined by solution viscosity and column diameter
  - [experimental result] By adjusting drawing speed and rotation rate, column diameter can be precisely controlled
  - [image description] SEM images confirm generation of particles with diameters ranging from 1 μm to 1 mm with narrow size distributions
  - [experimental result] Coefficient of variation (CV) measurements show <10% variation across produced particles
### M3  Structure → Property
- cause: Core–shell structure fabricated using coaxial needle feeding
- effect: Fluorescent and magnetic properties through material compartmentalization
- experiment: Core-shell particle fabrication | Fluorescence microscopy and VSM measurement | params: Coaxial needle setup with PAAS (core) and PEO (shell); QDs and Fe3O4 nanoparticles incorporated into respective phases | result: Successful formation of compartmentalized core-shell particles with distinct fluorescent and magnetic characteristics
  - [experimental result] Coaxial needle setup enables independent control over core and shell material feed rates
  - [image description] Fluorescence images confirm successful compartmentalization of Rhodamine B-labeled shell and FITC-labeled core materials
  - [image description] EDS spectral imaging confirms presence of sodium in core and carbon/oxygen in shell, validating structural separation
  - [experimental result] VSM measurements show linear magnetic response without significant hysteresis due to uniform Fe3O4 nanoparticle distribution
### M4  Property → Performance
- cause: Fluorescence and magnetic properties
- effect: Potential applications in optoelectronic devices, antigen detection, and sustained-release medicine
- experiment: Functional particle characterization | Photoluminescence spectroscopy and magnetic hysteresis measurement | params: QD concentration in precursor solution, Fe3O4 nanoparticle loading level | result: Strong photoluminescence under 450 nm excitation; linear magnetic response with negligible coercivity
  - [non-referenced_knowledge] Fluorescence provides optical contrast for tracking and sensing applications
  - [non-referenced_knowledge] Magnetic behavior allows for external field-controlled movement and localization
  - [experimental result] Photoluminescence spectra confirm strong emission from embedded QDs after encapsulation
  - [experimental result] VSM measurements demonstrate near-linear magnetic response ideal for biomedical applications
  - [inductive reasoning] Therefore, these multifunctional particles are promising for optoelectronics, antigen detection, and sustained-release medicine
