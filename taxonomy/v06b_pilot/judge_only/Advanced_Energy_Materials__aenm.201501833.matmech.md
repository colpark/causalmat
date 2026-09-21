# MatMech content for Advanced_Energy_Materials/aenm.201501833 (judge only; not shown to staff)
- material: Ni_xP_γO_z  elements: ['Ni', 'P', 'O']  category: ['Nanomaterial', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Hydrothermal synthesis via ligand substitution of Ni-MOF with sodium phosphate at 150°C for 75 h
- **Structure**: Hollow porous microrod morphology with amorphous-crystalline texture and substitution of BTC ligands by PO_4^{3-} units
- **Properties**: Specific capacitance–electrochemical property, conductivity–electrical property
- **Performance**: Specific capacitance of 1627 F g^{-1} at 1 A g^{-1}, 53.65% capacitance retention after 10,000 cycles, energy density of 7.95 Wh kg^{-1} at 500 W kg^{-1}
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Hydrothermal synthesis via ligand substitution of Ni-MOF with sodium phosphate at 150°C for 75 h
- effect: Hollow porous microrod morphology with amorphous-crystalline texture and substitution of BTC ligands by PO_4^{3-} units
- experiment: FT-IR spectroscopy | Fourier transform-infrared spectroscopy | params: Comparison of Ni-MOF and MOF-derived Ni_xP_γO_z | result: IR bands of BTC ligands disappeared; new bands at 1120–910 cm⁻¹ and 600–530 cm⁻¹ assigned to P–O stretching and O–P–O bending modes
  - [non-referenced_knowledge] Ni-MOF consists of 1D zigzag chains of Ni(II) and BTC ligands connected by hydrogen bonding.
  - [experimental result] Sodium phosphate is introduced under hydrothermal conditions (150°C, 75 h) to substitute BTC ligands.
  - [experimental result] FT-IR shows disappearance of BTC vibrational bands and emergence of P–O and O–P–O bands, confirming ligand substitution.
  - [image description] SEM reveals that the microrod morphology is retained but becomes looser with surface pores and volume expansion.
  - [experimental result] XRD shows Ni_xP_γO_z has amorphous with crystalline textured structure, indicating partial retention of order after substitution.
  - [deductive reasoning] Substitution of bulky BTC with smaller PO_4^{3-} induces structural rearrangement, creating porosity and expanding the framework.
### M2  Structure → Properties
- cause: Hollow porous microrod morphology with amorphous-crystalline texture and substitution of BTC ligands by PO_4^{3-} units
- effect: Specific capacitance–electrochemical property, conductivity–electrical property
- experiment: Four-point probe conductivity measurement | Electrical conductivity measurement | params: Active material mixed with carbon black and PVDF (8:1:1) on glass slide | result: Resistance decreased from 1049.42 Ω sq⁻¹ (Ni-MOF) to 714.13 Ω sq⁻¹ (Ni_xP_γO_z)
  - [experimental result] MOF-derived Ni_xP_γO_z has a hollow porous microrod morphology with increased surface area (142.24 m²/g vs. 2.51 m²/g for Ni-MOF).
  - [image description] SEM images confirm looser structure with surface pores, which reduces ion diffusion length and improves electrolyte access.
  - [experimental result] FT-IR and TGA confirm substitution of insulating BTC ligands with conductive PO_4^{3-} units.
  - [experimental result] Four-point probe measurements show 32% reduction in electrical resistance after substitution.
  - [image description] CV curves show clear redox peaks at 0.4 V/0.2 V, corresponding to Ni²⁺/Ni³⁺ transitions in Ni_xP_γO_z.
  - [referenced knowledge] Phosphate groups stabilize the structure and facilitate electron transfer during redox reactions.
  - [deductive reasoning] Thus, the combined effect of high surface area, porous morphology, and phosphate-enhanced conductivity enables high pseudocapacitance and improved charge transfer.
### M3  Properties → Performance
- cause: Specific capacitance–electrochemical property, conductivity–electrical property
- effect: Specific capacitance of 1627 F g^{-1} at 1 A g^{-1}, 53.65% capacitance retention after 10,000 cycles, energy density of 7.95 Wh kg^{-1} at 500 W kg^{-1}
- experiment: Galvanostatic charge/discharge testing | Electrochemical charge/discharge measurement | params: Three-electrode system in 2 M KOH, current densities from 0.6 to 20 A g⁻¹ | result: Specific capacitance of 1627 F g⁻¹ at 1 A g⁻¹; 1044.4 F g⁻¹ at 20 A g⁻¹; 53.65% retention after 10,000 cycles at 6 A g⁻¹
  - [experimental result] Ni_xP_γO_z exhibits high specific capacitance (1627 F g⁻¹) at 1 A g⁻¹ due to abundant redox-active Ni sites and high surface area.
  - [image description] Conductivity is improved by PO_4^{3-} substitution, reducing charge transfer resistance (smaller semicircle in Nyquist plot).
  - [experimental result] Capacitance retention remains high (1044.4 F g⁻¹) at 20 A g⁻¹, indicating good rate capability from fast ion diffusion in porous structure.
  - [experimental result] After 10,000 cycles, 53.65% capacitance retention is achieved, attributed to structural stability from phosphate reinforcement.
  - [deductive reasoning] Energy density of 7.95 Wh kg⁻¹ at 500 W kg⁻¹ is calculated from capacitance and voltage using E = 0.5CV²/3.6.
  - [deductive reasoning] Thus, enhanced conductivity and pseudocapacitance directly translate to superior performance metrics.
