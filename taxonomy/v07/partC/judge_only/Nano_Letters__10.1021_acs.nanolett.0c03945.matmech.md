# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c03945 (judge only; not shown to staff)
- material: Au-Al2O3-Si tunnel junction  elements: ['Au', 'Al', 'O', 'Si', 'Ti']  category: ['Metals and Alloys', 'Ceramic', 'Coatings and Thin Films', 'Nanomaterial']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Atomic layer deposition (ALD) of Al2O3, thermal evaporation of gold, electron-beam lithography for patterning
- **Structure**: Periodic array of gold bars on a p-type silicon substrate with a thin Al2O3 barrier
- **Properties**: Light emission spectrum–optical property, electron temperature–thermal property
- **Performance**: Above-threshold light emission (ATLE) in metal-insulator-semiconductor tunnel junctions
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Atomic layer deposition (ALD) of Al2O3, thermal evaporation of gold, electron-beam lithography for patterning
- effect: Periodic array of gold bars on a p-type silicon substrate with a thin Al2O3 barrier
- experiment: Device fabrication characterization | Ellipsometry & AFM thickness measurement | params: 3 nm Al2O3 barrier, 10 nm Au electrode, 1 nm Ti adhesion layer | result: Uniform oxide thickness across wafer; titanium layer shown to damp plasmonic field
  - [experimental result] Al2O3 barrier deposited using atomic layer deposition ensures uniform thickness
  - [experimental result] Thermal evaporation used to deposit 10 nm gold electrode over the oxide layer
  - [image description] Electron-beam lithography creates periodic gold bar arrays with defined dimensions
  - [non-referenced_knowledge] Thin titanium layer (~1 nm) used for adhesion damps plasmonic field
  - [deductive reasoning] Therefore, the combination of these processing steps yields a structured plasmonic tunnel junction
### M2  Structure → Property
- cause: Periodic array of gold bars on a p-type silicon substrate with a thin Al2O3 barrier
- effect: Light emission spectrum–optical property, electron temperature–thermal property
- experiment: Optical emission spectroscopy | Voltage-dependent spectral analysis | params: Applied voltage range: 1.4–3.0 V, step size: 0.2 V | result: Spectral cutoff energy blueshifts with increasing voltage; Fermi-Dirac distribution observed
  - [non-referenced_knowledge] Gold bars form localized plasmon resonators due to their subwavelength dimensions
  - [referenced knowledge] Tunneling electrons from gold to silicon valence band lose energy via plasmon excitation
  - [image description] Measured spectra show clear voltage-dependent blueshift of emission cutoff
  - [experimental result] Fermi-Dirac fits to spectra indicate thermalized electron distributions at elevated temperatures
  - [inductive reasoning] Thus, the nanostructured junction geometry directly controls both optical and thermal properties through plasmon-mediated electron interactions
### M3  Property → Performance
- cause: Light emission spectrum–optical property, electron temperature–thermal property
- effect: Above-threshold light emission (ATLE) in metal-insulator-semiconductor tunnel junctions
- experiment: Temperature extraction from spectral fitting | Fermi-Dirac distribution fitting | params: Voltage range: 1.4–3.0 V, fitting parameter: Te(V) | result: Te increases linearly with voltage below ~2.0 V, then plateaus; ATLE fraction increases with voltage
  - [image description] Spectra show significant emission above ℏω > eV threshold
  - [experimental result] Fermi-Dirac fitting reveals electron temperatures exceeding lattice temperature
  - [referenced knowledge] Electron heating mechanism attributed to nonradiative plasmon decay
  - [non-referenced_knowledge] Temperature-voltage dependence correlates strongly with plasmon resonance energy
  - [deductive reasoning] Therefore, plasmon-mediated electron heating is responsible for the observed above-threshold light emission performance
