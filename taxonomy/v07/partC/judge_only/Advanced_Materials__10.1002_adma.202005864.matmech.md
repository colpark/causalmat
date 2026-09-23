# MatMech content for Advanced_Materials/10.1002_adma.202005864 (judge only; not shown to staff)
- material: Metasurface (gold nanobars on SiO2 substrate)  elements: ['Au', 'Si', 'O']  category: ['Nanomaterial', 'Metals and Alloys', 'Ceramic', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Fabrication by standard e-beam lithography
- **Structure**: Coupled metal–insulator–metal structure with gold nanobars
- **Properties**: Phase modulation–optical property, Reflectance–optical property
- **Performance**: Holographic mimicry in different environments (air and oil), dual-wavelength operation
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Fabrication by standard e-beam lithography
- effect: Coupled metal–insulator–metal structure with gold nanobars of varying geometric parameters (L1, L2, W1, W2, g)
- experiment: Electron beam lithography fabrication | Nanofabrication | params: Gold substrate thickness: 100 nm; SiO₂ spacing layer: 50 nm; Gold nanoantenna thickness: 40 nm; Periodicity: 500 × 250 nm² | result: Unit cells with two coupled gold nanobars exhibiting tunable resonances depending on geometry
  - [experimental result] The holographic mimicry metasurface was fabricated using standard e-beam lithography.
  - [image description] SEM image shows variation in nanobar geometry across pixels, confirming successful lithographic patterning.
  - [non-referenced_knowledge] E-beam lithography allows for sub-100 nm resolution, enabling precise control over nanoscale features.
  - [deductive reasoning] This precision ensures that the designed unit cells with specific lengths and gaps can be realized as intended.
### M2  Structure → Property
- cause: Coupled metal–insulator–metal structure with gold nanobars of varying geometric parameters (L1, L2, W1, W2, g)
- effect: Phase modulation and reflectance properties sensitive to surrounding medium
- experiment: FDTD simulations of reflection spectra | Computational modeling | params: Surrounding media: air (n=1), oil (n=1.515); Working wavelength: 800 nm | result: Resonant peaks shift to longer wavelengths when immersed in oil; phase difference of ~π between air and oil at working wavelength
  - [experimental result] Simulated reflection spectra show resonant mode redshift and phase change when switching from air to oil.
  - [image description] Figure illustrates how the electric field distribution changes between air and oil, altering the effective phase response.
  - [non-referenced_knowledge] Plasmonic resonances are sensitive to the dielectric environment, leading to spectral and phase shifts.
  - [deductive reasoning] Therefore, the same structure exhibits different phase responses depending on whether it is in air or oil.
### M3  Property → Performance
- cause: Phase modulation and reflectance properties sensitive to surrounding medium
- effect: Holographic mimicry in different environments (air and oil), dual-wavelength operation
- experiment: Optical characterization of holographic mimicry | Imaging under different media | params: Incident wavelength: 800 nm; Media: air and cedar oil (n=1.515) | result: Projected hologram transitions from 'bird' in air to 'fish' in oil
  - [experimental result] Each unit cell's phase response differs between air and oil, allowing for two distinct phase matrices.
  - [image description] Measured holograms show distinct bird and fish images in air and oil respectively.
  - [non-referenced_knowledge] Metasurfaces support independent phase control, enabling encoding of multiple holographic functions.
  - [deductive reasoning] Thus, changing the surrounding medium effectively switches between pre-designed holographic outputs.
### M4  Structure → Performance
- cause: Coupled metal–insulator–metal structure with gold nanobars of varying geometric parameters (L1, L2, W1, W2, g)
- effect: Dual-wavelength operation for colorful holographic mimicry
- experiment: Design and testing of three-bar unit cell | Computational simulation and experimental validation | params: Three nanobars with variable lengths (L1, L2, L3); Fixed widths and gap; Simulated at 710 nm and 890 nm | result: Achieved independent phase modulation at both wavelengths in air and oil
  - [experimental result] Design of a three-nanobar unit cell allows tuning of five resonant modes across visible to near-infrared wavelengths.
  - [image description] Image shows four distinct holographic outputs depending on wavelength and surrounding medium.
  - [non-referenced_knowledge] Multiple resonators in a single unit cell enable multiwavelength operation through independent phase modulation.
  - [deductive reasoning] Thus, by independently controlling phase at two wavelengths, a color-like effect is achieved through spectral multiplexing.
