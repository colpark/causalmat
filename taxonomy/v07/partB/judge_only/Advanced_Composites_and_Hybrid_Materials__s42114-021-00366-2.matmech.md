# MatMech content for Advanced_Composites_and_Hybrid_Materials/s42114-021-00366-2 (judge only; not shown to staff)
- material: BST@Ag/PAEN  elements: ['Ba', 'Sr', 'Ti', 'Ag', 'C', 'H', 'O', 'Si', 'N']  category: ['Composite Material', 'Nanomaterial', 'Polymer', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Surface grafting modification of BST nanoparticles with MPTMS followed by in situ reduction of Ag⁺ to form BST@Ag hybrid particles, then solution casting with ultrasonic dispersion into PAEN matrix
- **Structure**: Core-shell hybrid particles with BST core and Ag nanoparticles on surface; improved interfacial compatibility and homogeneous dispersion in PAEN matrix
- **Properties**: Dielectric permittivity–dielectric property, dielectric loss–dielectric property, tensile strength–mechanical property, glass transition temperature–thermal property
- **Performance**: High-temperature-resistant dielectric material with good permittivity-temperature stability below 140 °C and high mechanical strength (>73 MPa)
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Surface grafting modification of BST nanoparticles with MPTMS followed by in situ reduction of Ag⁺ to form BST@Ag hybrid particles
- effect: Core-shell hybrid particles with BST core and Ag nanoparticles on surface; improved interfacial compatibility and homogeneous dispersion in PAEN matrix
- experiment: FTIR spectroscopy and SEM imaging | FTIR, SEM | params: BST-OH and BST-SH particles analyzed via FTIR; BST, BST-SH, and BST@Ag particles imaged via SEM | result: FTIR shows new peaks at 2930 and 2864 cm⁻¹ (–CH₂) and 1122 cm⁻¹ (Si–O); SEM confirms surface coating and size increase from 70 nm (BST) to 100 nm (BST@Ag)
  - [experimental result] BST nanoparticles are hydroxylated via H₂O₂ reflux to create BST-OH surfaces.
  - [experimental result] MPTMS is grafted onto BST-OH via silane coupling, confirmed by new FTIR peaks at 2930, 2864, and 1122 cm⁻¹.
  - [image description] FTIR and visual dispersion tests show surface change from hydrophilic to lipophilic.
  - [experimental result] Ag⁺ ions are reduced in ethylene glycol at 160°C, depositing Ag nanoparticles on BST-SH surfaces via –SH coordination.
  - [image description] SEM images show increased particle size and surface roughness after Ag deposition, confirming core-shell structure.
  - [non-referenced_knowledge] MPTMS’s organic chains and polar –SH groups improve miscibility with PAEN’s –CN groups via dipole–dipole interactions.
  - [image description] Cross-sectional SEM shows absence of agglomeration in BST@Ag/PAEN, indicating homogeneous dispersion.
  - [deductive reasoning] Thus, processing via MPTMS grafting and in situ Ag reduction creates a core-shell structure with enhanced interfacial compatibility and dispersion.
### M2  Structure → Property
- cause: Core-shell hybrid particles with BST core and Ag nanoparticles on surface; homogeneous dispersion in PAEN matrix
- effect: Enhanced dielectric permittivity, low dielectric loss (<0.026), and good permittivity-temperature stability below 140 °C
- experiment: Dielectric property measurement | LCR meter with temperature control | params: Frequency range: 100 Hz – 1 MHz; Temperature range: 25–180 °C; BST@Ag content: 0–5 wt% Ag | result: Dielectric permittivity increased by 78% with 5 wt% Ag; dielectric loss remained <0.026; permittivity stable below 140 °C
  - [image description] BST@Ag hybrid particles are homogeneously dispersed in PAEN matrix, as shown by SEM.
  - [experimental result] Dielectric permittivity increases with Ag content, indicating enhanced polarization.
  - [experimental result] Dielectric loss remains low (<0.026) despite high Ag content, contrary to typical percolation behavior.
  - [non-referenced_knowledge] MPTMS shell on BST prevents direct Ag–Ag contact, inhibiting conductive percolation.
  - [referenced knowledge] Ag nanoparticles induce Coulomb blockade, restricting electron movement and suppressing interfacial polarization loss.
  - [deductive reasoning] Thus, the hybrid structure enables high permittivity without high loss due to controlled interfacial effects.
### M3  Structure → Property
- cause: Core-shell hybrid particles with BST core and Ag nanoparticles on surface; homogeneous dispersion in PAEN matrix
- effect: High tensile strength (>73 MPa) and retained mechanical integrity despite 30 wt% filler loading
- experiment: Tensile testing | Electronic Universal Testing Machine | params: Tensile strength and elongation at break measured for pure PAEN and BST@Ag/PAEN composites with 0–5 wt% Ag | result: Tensile strength decreased only 7.3% (79.3 MPa → 73.5 MPa) with 5 wt% Ag; elongation decreased from 6.9% to 4.4%
  - [image description] SEM images show no agglomeration and indistinguishable interfaces between BST@Ag particles and PAEN matrix.
  - [experimental result] Tensile strength remains above 73 MPa even with 5 wt% Ag (30 wt% total filler).
  - [non-referenced_knowledge] Poor compatibility typically causes filler agglomeration and strength loss in polymer composites.
  - [non-referenced_knowledge] MPTMS grafting enhances polymer-filler adhesion via dipole–dipole interactions between –SH and –CN groups.
  - [deductive reasoning] Thus, the improved structure enables mechanical performance retention despite high ceramic loading.
### M4  Structure → Property
- cause: Core-shell hybrid particles with BST core and Ag nanoparticles on surface; homogeneous dispersion in PAEN matrix
- effect: Glass transition temperature (Tg) reduced from 176°C (pure PAEN) to 146–157°C, and thermal stability maintained (T₅% > 520°C)
- experiment: DSC and TGA analysis | Differential Scanning Calorimetry, Thermogravimetric Analysis | params: Heating rate: 10°C/min (DSC), 20°C/min (TGA); nitrogen atmosphere | result: Tg of composites: 146–157°C (vs. 176°C for pure PAEN); T₅% > 520°C for all composites; char yield increases with filler content
  - [experimental result] DSC shows Tg of composites is lower than pure PAEN (176°C → 146–157°C).
  - [non-referenced_knowledge] MPTMS contains flexible –CH₂–CH₂–CH₂– chains, which can increase free volume and chain mobility in PAEN.
  - [experimental result] TGA shows T₅% > 520°C for all composites, similar to pure PAEN.
  - [non-referenced_knowledge] BST and Ag nanoparticles are thermally stable and inhibit polymer chain mobility during decomposition.
  - [experimental result] A small mass loss at 180–250°C corresponds to MPTMS decomposition, confirming its presence.
  - [deductive reasoning] Thus, the hybrid structure balances plasticization (lower Tg) with thermal stability (high T₅%).
### M5  Processing → Performance
- cause: Surface grafting modification of BST with MPTMS and in situ Ag reduction followed by solution casting
- effect: High-temperature-resistant dielectric material with good permittivity-temperature stability below 140 °C and high mechanical strength (>73 MPa)
- experiment: Comprehensive property evaluation | Dielectric, TGA, DSC, Tensile testing | params: All tests performed on BST@Ag/PAEN composites with 30 wt% filler and 0–5 wt% Ag | result: Composites exhibit permittivity increase >78%, loss <0.026, Tg 146–157°C, T₅% >520°C, tensile strength >73 MPa
  - [experimental result] Processing involves MPTMS grafting and in situ Ag reduction to form BST@Ag hybrid particles.
  - [image description] These particles exhibit homogeneous dispersion and strong interfacial bonding in PAEN, as shown by SEM.
  - [non-referenced_knowledge] The structure enables high permittivity and low loss via interfacial polarization and Coulomb blockade.
  - [experimental result] The structure maintains high thermal stability (T₅% > 520°C) and acceptable Tg (146–157°C).
  - [experimental result] Tensile strength remains >73 MPa due to good dispersion and compatibility.
  - [deductive reasoning] Thus, the processing method directly enables a composite with multi-functional performance suitable for high-temperature electronics.
