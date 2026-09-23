# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c04014 (judge only; not shown to staff)
- material: Gold nanorod array and organic molecules (hexanal and 4-butylbenzonitrile)  elements: ['Au', 'C', 'H', 'N', 'O']  category: ['Nanomaterial', 'Metals and Alloys', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Incorporation of a gold nanorod array into a Fabry-Perot cavity filled with organic molecules
- **Structure**: Formation of hybrid polaritonic states due to coupling between the cavity, plasmonic array, and molecular vibrations
- **Properties**: Rabi splitting–optical property, coupling strength–optical property
- **Performance**: Increased coupling strength and narrowed plasmon line width for potential use in plasmon-based biosensors
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Incorporation of a gold nanorod array into a Fabry-Perot cavity filled with organic molecules
- effect: Formation of hybrid polaritonic states due to coupling between the cavity, plasmonic array, and molecular vibrations
- experiment: FT-IR microscopy and numerical modeling | FT-IR spectroscopy and FDTD simulations | params: Gold nanorods deposited on SiO2 spacer; cavity thicknesses ranging from 11–16 μm; hexanal and 4-butylbenzonitrile as organic molecules | result: Observation of normal mode splitting and hybrid cavity-plasmon-molecule polaritonic modes
  - [experimental result] Gold nanorod arrays were deposited on a SiO2 spacer inside a Fabry-Perot cavity coated with gold mirrors.
  - [image description] Figure shows transmission maps with new polaritonic states emerging when molecules and plasmons are simultaneously present in the cavity.
  - [referenced knowledge] Plasmonic arrays can ultrastrongly couple with FP cavities in the visible to mid-IR range.
  - [non-referenced_knowledge] Coupling strength increases with effective oscillator density in the cavity volume.
  - [deductive reasoning] Thus, the presence of plasmonic meta-atoms enhances coupling beyond what molecular concentration alone allows.
### M2  Structure → Property
- cause: Formation of hybrid polaritonic states due to coupling between the cavity, plasmonic array, and molecular vibrations
- effect: Rabi splitting–optical property, coupling strength–optical property
- experiment: Hamiltonian analysis of experimental data | Multimode coupled harmonic oscillator model fitting | params: Fitting eigenvalues of Hamiltonian to measured transmission peaks using Jaynes-Cummings model | result: Extracted zero-detuning coupling strengths of ~220 cm⁻¹ (hexanal) and ~202 cm⁻¹ (4-butylbenzonitrile)
  - [experimental result] Measured Rabi splittings of 101 cm⁻¹ (hexanal) and 46 cm⁻¹ (4-butylbenzonitrile) indicate strong coupling regime.
  - [image description] Hamiltonian fit confirms emergence of new polaritonic modes with enhanced coupling strength (~220 cm⁻¹ and ~202 cm⁻¹).
  - [referenced knowledge] Rabi splitting scales with √C where C is molecular concentration.
  - [non-referenced_knowledge] Plasmonic arrays act as artificial molecules with large oscillator strength, contributing to total coupling.
  - [deductive reasoning] Therefore, plasmonic meta-atoms increase effective coupling strength beyond bulk molecular limit.
### M3  Property → Performance
- cause: Rabi splitting–optical property, coupling strength–optical property
- effect: Increased coupling strength and narrowed plasmon line width for potential use in plasmon-based biosensors
- experiment: Line width analysis of polaritonic modes | Transmission spectroscopy with polarization control | params: Polarization-resolved measurements along and perpendicular to nanorod axis | result: Observed plasmon linewidth narrowing from ~621–1120 cm⁻¹ to ~70 cm⁻¹ inside cavity
  - [experimental result] Measured Rabi splittings exceed molecular absorption linewidths, confirming strong coupling regime.
  - [image description] Polaritonic line widths are reduced by cavity mirrors, showing FP cavity mode limits linewidth.
  - [referenced knowledge] Strong coupling modifies chemical reactivity and enzyme activity.
  - [non-referenced_knowledge] Narrower linewidth improves spectral selectivity for sensing applications.
  - [deductive reasoning] Therefore, this hybrid system provides enhanced sensitivity and selectivity for mid-IR molecular sensing.
