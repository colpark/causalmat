# MatMech content for Advanced_Materials/10.1002_adma.202006910 (judge only; not shown to staff)
- material: [6,6]-phenyl-C61-butyric acid methyl ester (PCBM)  elements: ['C', 'H', 'O', 'N']  category: ['Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Introduction of bathophenanthroline (Bphen) into PCBM to form a stable interlayer
- **Structure**: Formation of thermodynamically stable charge-transfer complexes between PCBM and Bphen
- **Properties**: Power conversion efficiency (PCE)–electrical property, Stability under UV light–environmental property
- **Performance**: Retention of over 95% initial efficiency after 1100h UV irradiation and 92% after 1000h continuous illumination under full spectrum
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Introduction of bathophenanthroline (Bphen) into [6,6]-phenyl-C61-butyric acid methyl ester (PCBM)
- effect: Formation of thermodynamically stable charge-transfer complexes between PCBM and Bphen
- experiment: Raman spectroscopy and XPS analysis | Spectroscopic characterization | params: Measurement of vibrational modes and core-level binding energies in PCBM and PCBM:Bphen films | result: Shifts in Raman peaks and N 1s XPS binding energy indicate charge transfer between PCBM and Bphen
  - [non-referenced_knowledge] Bphen contains pyridine rings with lone electron pairs at nitrogen atoms, enabling strong electron donation.
  - [experimental result] XPS measurements show a 0.15 eV shift toward lower binding energy in N 1s peak when Bphen is added to PCBM or C60.
  - [referenced knowledge] The standard enthalpy of formation of C60n− is more negative than neutral C60, suggesting higher stability with charge accumulation.
  - [image description] Raman spectra show a 4 cm⁻¹ upshift in the Ag(2) mode and reduced intensity, indicating weakened electron-accepting tendency of the C60 cage.
  - [deductive reasoning] Thus, Bphen donates electrons to PCBM, forming thermodynamically stable charge-transfer complexes that enhance structural resilience under UV exposure.
### M2  Structure → Performance
- cause: Formation of thermodynamically stable charge-transfer complexes between PCBM and Bphen
- effect: Retention of over 95% initial efficiency after 1100h UV irradiation and 92% after 1000h continuous illumination under full spectrum
- experiment: UV aging and HPLC/MALDI TOF MS analysis | Degradation testing and molecular analysis | params: Exposure to high-intensity UV light (100 mW/cm²) for 1 week; detection of decomposition products via chromatography and mass spectrometry | result: PCBM film with Bphen additive showed minimal spectral change and no detectable decomposition products post-UV exposure
  - [experimental result] HPLC and MALDI TOF MS analyses confirm that PCBM:Bphen films do not produce degradation or dimerization products after UV exposure, unlike pure PCBM films.
  - [image description] UV-vis absorption of PCBM:Bphen films remains stable after UV aging, showing no enhancement or blue shift typically associated with fullerene degradation.
  - [referenced knowledge] Photoinduced degradation of fullerene derivatives like PCBM is known to cause burn-in effects in solar cells.
  - [non-referenced_knowledge] Bphen forms stable charge-transfer complexes that redistribute electronic density on the fullerene cage, reducing reactivity and susceptibility to UV damage.
  - [deductive reasoning] Therefore, the stabilized PCBM:Bphen interlayer prevents UV-induced degradation, leading to superior long-term device performance with >95% efficiency retention after 1100 h UV irradiation.
