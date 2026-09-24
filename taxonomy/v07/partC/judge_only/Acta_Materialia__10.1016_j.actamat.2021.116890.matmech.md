# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116890 (judge only; not shown to staff)
- material: Al-Cr-Fe-Ni-Ti complex concentrated alloys  elements: ['Al', 'Cr', 'Fe', 'Ni', 'Ti']  category: ['Metals and Alloys', 'Nanomaterial']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Homogenization treatment at 1200°C for 6 hours followed by air-cooling
- **Structure**: BCC matrix with L21 nanoprecipitates, transitioning from semicoherent to fully coherent interfaces with increasing Al content
- **Properties**: yield strength–mechanical property, ultimate tensile strength–mechanical property
- **Performance**: High temperature strength and creep resistance
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Homogenization treatment at 1200°C for 6 hours followed by air-cooling
- effect: Formation of BCC matrix with L2₁ nanoprecipitates, transitioning from semicoherent to fully coherent interfaces with increasing Al content
- experiment: Microstructural characterization using SEM and TEM | Scanning Electron Microscopy (SEM), Transmission Electron Microscopy (TEM) | params: Al content varied (8–16 at.%) | result: Precipitate size decreases and number density increases with Al content; misfit dislocations decrease with higher Al, leading to coherent interface in 16Al alloy
  - [experimental result] Homogenization at 1200°C ensures dissolution and uniform distribution of elements prior to precipitation.
  - [image description] BSE-SEM images show precipitate size decreases and number density increases with increasing Al.
  - [image description] Misfit dislocations are visible in low-Al alloys but disappear in 16Al, indicating fully coherent interface.
  - [non-referenced_knowledge] Lattice misfit decreases with increasing Al, promoting coherent interface formation.
  - [deductive reasoning] Therefore, homogenization followed by air-cooling promotes coherent nanoprecipitate formation when Al content is sufficiently high.
### M2  Structure → Property
- cause: Decrease in lattice misfit and increase in coherency between BCC matrix and L2₁ precipitates
- effect: Increase in yield strength and ultimate tensile strength with Al addition
- experiment: Tensile and compressive mechanical testing | Mechanical Testing | params: Room temperature and 700°C testing conditions | result: Yield strength increases from 1070.3 MPa (8Al) to 1427.0 MPa (16Al); UTS reaches 572.9 MPa in 16Al alloy
  - [experimental result] Strain maps from PED-enhanced NBD show increasing coherency strain with Al content.
  - [image description] Dislocations are observed to be blocked at precipitate interfaces in 16Al alloy, indicating strong interaction.
  - [referenced knowledge] Coherency strain fields impede dislocation motion, increasing flow stress.
  - [non-referenced_knowledge] Fully coherent precipitates in 16Al allow for better load transfer compared to semicoherent ones in 8Al.
  - [deductive reasoning] Thus, decreasing lattice misfit and increasing coherency lead to enhanced yield and tensile strengths.
### M3  Property → Performance
- cause: Increased yield strength and ultimate tensile strength at high temperatures
- effect: Enhanced high-temperature performance, particularly creep resistance and structural stability
- experiment: High-temperature tensile tests at 700°C | Tensile Test | params: Testing temperature: 700°C | result: 16Al alloy shows yield strength of 400.8 MPa and UTS of 572.9 MPa at 700°C, significantly higher than other HEAs
  - [experimental result] Tensile tests at 700°C show significant strength retention in 16Al alloy.
  - [image description] Fully coherent precipitates resist dislocation bypass mechanisms like Orowan looping, maintaining strengthening at high temperature.
  - [referenced knowledge] Coherency strengthens the interface and suppresses diffusional relaxation, improving creep resistance.
  - [non-referenced_knowledge] Structural stability of coherent precipitates under thermal stress enhances long-term mechanical reliability.
  - [deductive reasoning] Therefore, the combination of high strength and thermal stability leads to superior high-temperature performance.
### M4  Structure → Property
- cause: Transition from spherical to cuboidal precipitates with increasing Al content
- effect: Improved precipitation hardening via coherency strengthening
- experiment: TEM microstructural analysis | Transmission Electron Microscopy | params: Observation of precipitate shape and interface structure | result: 8Al and 10Al show spherical precipitates with semicoherent interfaces; 16Al shows cuboidal precipitates with fully coherent interfaces
  - [image description] DF-TEM images show transition from spherical to cuboidal precipitates with increasing Al.
  - [image description] SADPs confirm evolution from semicoherent to coherent interface structures with Al addition.
  - [referenced knowledge] Cuboidal precipitates grow along elastically soft <100> directions, minimizing strain energy.
  - [non-referenced_knowledge] Coherent precipitates generate stronger strain fields that interact more effectively with dislocations.
  - [deductive reasoning] Thus, cuboidal and coherent precipitates provide stronger coherency strengthening than spherical, semicoherent ones.
### M5  Processing → Structure
- cause: Air-cooling after homogenization treatment
- effect: Rapid formation of primary and secondary L2₁ nanoprecipitates
- experiment: APT and TEM analysis of precipitate composition and structure | Atom Probe Tomography, Transmission Electron Microscopy | params: Cooling rate after homogenization | result: Primary L2₁ precipitates form during air-cooling; secondary precipitates form at lower temperatures during cooling
  - [experimental result] APT confirms formation of primary and secondary precipitates immediately after air-cooling.
  - [referenced knowledge] DSC shows endothermic peaks corresponding to dissolution of secondary precipitates upon reheating.
  - [non-referenced_knowledge] Cooling rate and thermodynamic driving force dictate the extent and speed of precipitation.
  - [deductive reasoning] Therefore, air-cooling after homogenization enables rapid and extensive precipitation without additional aging.
