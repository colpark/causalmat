# MatMech content for Nano_Letters/10.1021_acs.nanolett.1c00025 (judge only; not shown to staff)
- material: Closable nanotrench metamaterials  elements: ['C', 'H', 'O']  category: ['Nanomaterial', 'Composite Material', 'Metals and Alloys', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Atomic layer lithography and inner bending of flexible substrate
- **Structure**: Nanotrench geometry with predefined width and height, tapered geometry during closing
- **Properties**: Electrical conductance–electrical property, transmission intensity–optical property
- **Performance**: Robust extinction performance enduring over a thousand bending cycles, switching of resonance, chirality, and polarization selectivity
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Atomic layer lithography and inner bending of flexible substrate
- effect: Nanotrench geometry with predefined width and height, tapered geometry during closing
- experiment: Scanning electron microscopy (SEM) and structural simulation | SEM, FEM simulation | params: Trench widths: 20 nm to 300 nm; trench height: 150 nm; curvature analysis via FEM | result: Nanotrench closes from the top with tapered geometry confirmed by SEM images and finite element method simulation
  - [experimental result] Atomic layer lithography was used on a PET substrate to fabricate nanotrenches with defined widths (e.g., 20 nm, 200 nm).
  - [image description] SEM images confirm that nanotrenches close from the top due to differential compression during inner bending.
  - [non-referenced_knowledge] Finite element method simulations reveal pressure distribution causing faster closing at the top, leading to tapered geometry.
  - [deductive reasoning] Therefore, inner bending results in a top-down, tapered nanotrench closure rather than parallel closure.
### M2  Structure → Property
- cause: Nanotrench geometry with predefined width and height, tapered geometry during closing
- effect: Electrical conductance–electrical property, transmission intensity–optical property
- experiment: Electrical transport measurement and terahertz time-domain spectroscopy | Electrical resistance measurement, THz-TDS | params: Nanotrench width: 30 nm; bending cycles up to 300; frequency range: 0.5 THz to microwave | result: Conductance jumps near quantum value $ G_0 = 2e^2/h $ indicate atomic-scale contact formation; extinction reaches ~99.9% with increasing curvature
  - [experimental result] Electrical measurements show exponential resistance decay followed by sharp drops near quantized conductance values, indicating atomic-scale gap closure.
  - [experimental result] THz and microwave transmission data demonstrate nearly complete extinction (>99.9%) under high curvature, indicating effective shielding.
  - [referenced knowledge] Simmons fitting confirms picometer-scale gap narrowing prior to contact formation.
  - [non-referenced_knowledge] Field enhancement in sub-nm gaps reduces transmission through impedance mismatch and plasmonic coupling.
  - [inductive reasoning] Thus, the structural narrowing of the nanotrench leads to abrupt changes in both electrical and optical properties.
### M3  Property → Performance
- cause: Electrical conductance–electrical property, transmission intensity–optical property
- effect: Robust extinction performance enduring over a thousand bending cycles, switching of resonance, chirality, and polarization selectivity
- experiment: Repetition testing and functional modulation experiments | Bending fatigue test, polarization-dependent THz spectroscopy | params: Over 1000 bending cycles; square-shaped nanotrench arrays and split ring resonators (SRRs) | result: Extinction remains >99.9% after 1000 cycles; polarization selectivity and chirality switch with bending
  - [experimental result] After 1000 bending cycles, resistance curves remain consistent and extinction performance is preserved.
  - [image description] Square-shaped nanotrench arrays show resonance doubling and polarization filtering upon bending due to symmetry reduction.
  - [image description] SRR-based metamaterials switch from left to right circular polarization upon trench closure, demonstrating chirality inversion.
  - [non-referenced_knowledge] These effects arise from symmetry-breaking-induced changes in local electromagnetic response.
  - [deductive reasoning] Therefore, the dynamic control of conductance and optical extinction translates into robust, multifunctional performance.
