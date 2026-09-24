# MatMech content for Advanced_Materials/10.1002_adma.202006801 (judge only; not shown to staff)
- material: Organic and Perovskite LEDs (PeLEDs)  elements: ['C', 'H', 'O', 'Al', 'I', 'T', 'O']  category: ['Nanomaterial', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Thermal evaporation and solution processing for planarization of the device stack
- **Structure**: Nanostructured LED with planarized cathode to suppress TM waveguide and SPP modes
- **Properties**: TE to TM polarization extinction ratio of 13–optical property
- **Performance**: Highly directional light emission with a divergence angle less than 3° and enhanced current efficiency in PeLEDs
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Thermal evaporation and solution processing for planarization of the device stack
- effect: Nanostructured LED with planarized cathode to suppress TM waveguide and SPP modes
- experiment: Cross-section SEM of OLED on 1D grating | Scanning Electron Microscopy (SEM) | params: Observation of cathode surface morphology after thermal evaporation of thick organic layers | result: Top cathode is nearly planarized due to thick ETL layer
  - [experimental result] A thick ETL is thermally evaporated, resulting in a nearly planar Al cathode surface as observed in cross-section SEM.
  - [image description] The planarized cathode reduces corrugation depth below the threshold required to efficiently extract TM waveguide and SPP modes.
  - [non-referenced_knowledge] TM waveguide and SPP modes are highly sensitive to interface roughness and are only efficiently extracted by deep corrugation at the metal interface.
  - [deductive reasoning] Thus, thermal evaporation of a thick organic stack enables selective extraction of TE waveguide mode while suppressing TM and SPP modes.
### M2  Structure → Property
- cause: Nanostructured LED with planarized cathode to suppress TM waveguide and SPP modes
- effect: TE to TM polarization extinction ratio of 13 – optical property
- experiment: Angle-resolved EL spectra measurements | Spectroscopic characterization | params: Polarization-resolved measurement of emission intensity in TE and TM directions | result: TE to TM extinction ratio of 13 observed in waveguide emission OLED
  - [experimental result] Waveguide emission OLEDs show negligible TM waveguide or SPP features in measured mode dispersion.
  - [image description] Figure shows strong directional TE waveguide emission peak with FWHM divergence angle between 3.5° and 4.1°.
  - [non-referenced_knowledge] Selective diffraction of TE waveguide mode while suppressing TM and SPP modes enhances polarization contrast.
  - [deductive reasoning] Therefore, suppression of non-TE modes results in a TE-to-TM extinction ratio of 13.
### M3  Property → Performance
- cause: TE to TM polarization extinction ratio of 13 – optical property
- effect: Highly directional light emission with a divergence angle less than 3° and enhanced current efficiency in PeLEDs
- experiment: Current efficiency measurement | Electrical and optical characterization | params: Comparison of normal direction current efficiency between reference and waveguide emission PeLEDs | result: Waveguide emission PeLED shows 2.6× enhancement in current efficiency
  - [experimental result] Perovskite LEDs demonstrate directional emission with divergence angle less than 3° and TE-to-TM extinction ratio of 13.
  - [image description] Figure shows spatial pattern and current efficiency enhancement of 2.6× in waveguide emission PeLED compared to reference.
  - [non-referenced_knowledge] Directional light emission with reduced divergence improves outcoupling efficiency and perceived brightness.
  - [inductive reasoning] Thus, high polarization selectivity and narrow divergence lead to enhanced current efficiency and directional light emission.
### M4  Processing → Property
- cause: Thermal evaporation and solution processing for planarization of the device stack
- effect: TE to TM polarization extinction ratio of 13 – optical property
- experiment: Simulation of angular emission profile | Optical simulation | params: Finite-difference time-domain (FDTD) modeling of electric field distribution in OLED with 140 nm ETL | result: TE waveguide mode confined near ITO anode with narrow dispersion peak
  - [experimental result] FDTD simulations confirm TE waveguide mode localization near ITO anode, enabling effective diffraction by grating.
  - [image description] Cross-section SEM confirms planarized cathode suppresses TM and SPP mode diffraction.
  - [non-referenced_knowledge] Effective diffraction of TE waveguide mode requires precise alignment with grating periodicity and planarized electrode surfaces.
  - [deductive reasoning] Therefore, planarization during processing leads to selective extraction of TE mode and high polarization contrast.
### M5  Structure → Performance
- cause: Nanostructured LED with planarized cathode to suppress TM waveguide and SPP modes
- effect: Highly directional light emission with a divergence angle less than 3° and enhanced current efficiency in PeLEDs
- experiment: Angle-resolved emission spectroscopy | Optical characterization | params: Measurement of full-angle emission profiles from 20° to 90° with fine angular resolution | result: Waveguide emission OLED demonstrates divergence angle between 3.5° and 4.1°
  - [experimental result] Waveguide emission OLEDs exhibit divergence angle between 3.5° and 4.1° due to narrow TE waveguide mode dispersion.
  - [image description] Figure compares spatial patterns and current efficiency, showing significant enhancement in waveguide emission PeLED.
  - [non-referenced_knowledge] Narrow divergence angles improve display efficiency by reducing light loss in collimation optics.
  - [deductive reasoning] Therefore, nanostructuring and cathode planarization enable both directional emission and efficiency improvement.
