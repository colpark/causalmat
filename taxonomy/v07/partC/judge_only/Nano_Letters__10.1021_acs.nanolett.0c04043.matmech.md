# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c04043 (judge only; not shown to staff)
- material: Metal−molecule−metal junction  elements: ['Au', 'C', 'H', 'S']  category: ['Metals and Alloys', 'Polymer', 'Composite Material', 'Coatings and Thin Films', 'Nanomaterial']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Template-stripping technique for sub-nanometer smooth electrodes, dielectrophoretic trapping of colloidal nanorods
- **Structure**: Uniform sub-5 nm molecular junctions with self-assembled monolayers
- **Properties**: Tunneling conduction–electrical property, Young's modulus–mechanical property
- **Performance**: Electromechanical tuning of the junction, stable performance in reconfigurable devices
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Template-stripping technique for sub-nanometer smooth electrodes and dielectrophoretic trapping of colloidal nanorods
- effect: Uniform sub-5 nm molecular junctions with self-assembled monolayers
- experiment: AFM imaging of electrode arrays before and after planarization | Atomic Force Microscopy (AFM) | params: Gold surface roughness comparison before and after template stripping | result: Surface roughness reduced from ~2 nm to ~0.6 nm
  - [experimental result] Template-stripped gold exhibits ~0.6 nm roughness compared to ~2 nm in as-evaporated gold
  - [image description] AFM images show dramatic improvement in surface topography after template stripping
  - [non-referenced_knowledge] Ultrasmooth surfaces are essential for uniform molecular self-assembly at the nanoscale
  - [experimental result] PEG-thiol molecules self-assemble uniformly on stripped gold surfaces
  - [non-referenced_knowledge] Dielectrophoretic trapping places gold nanorods over the molecular layer without mechanical damage
  - [deductive reasoning] Gap width is defined by the thickness of the self-assembled molecular layer
### M2  Structure → Property
- cause: Uniform sub-5 nm molecular junctions with self-assembled monolayers
- effect: Tunneling conduction (electrical property), Young’s modulus (mechanical property)
- experiment: Current-voltage (I-V) measurements and Simmons model fitting | Electrical characterization | params: Voltage sweeps across PEG-thiol and dodecanethiol molecular junctions | result: Exponential current increase with voltage due to tunneling; fitted Young’s modulus values: ~81 MPa (PEG-thiol), ~0.97 GPa (dodecanethiol)
  - [experimental result] Measured I-V curves exhibit exponential current increase consistent with tunneling
  - [experimental result] Simmons model fits indicate variable tunneling gap depending on applied voltage
  - [experimental result] PEG-thiol layer shows ~37% compression within 2 V, while dodecanethiol remains nearly rigid
  - [referenced knowledge] Fitted Young’s modulus values match expected literature values for these materials
  - [deductive reasoning] Stiffer molecular layers resist compression, leading to less current modulation
### M3  Property → Performance
- cause: Tunneling conduction (electrical property), Young’s modulus (mechanical property)
- effect: Electromechanical tuning of the junction, stable performance in reconfigurable devices
- experiment: Repeated I-V sweeps and stability testing | Electrical cycling test | params: Multiple voltage cycles up to 2 V | result: Stable performance with minimal hysteresis for hexanedithiol junctions; degradation observed at higher voltages
  - [non-referenced_knowledge] Applied voltage generates electrostatic attraction between electrodes
  - [deductive reasoning] Compressible molecular layers allow gap narrowing under force
  - [experimental result] Reduced tunneling gap leads to exponential increase in current
  - [experimental result] Hexanedithiol junctions show stable I-V behavior over 30 cycles
  - [inductive reasoning] Stability depends on molecular layer rigidity and absence of irreversible deformation
