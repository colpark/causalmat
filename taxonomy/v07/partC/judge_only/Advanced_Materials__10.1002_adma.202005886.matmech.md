# MatMech content for Advanced_Materials/10.1002_adma.202005886 (judge only; not shown to staff)
- material: Erbium-doped silicon  elements: ['Er', 'Si']  category: ['Crystalline Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Femtosecond laser irradiation for selective doping and crystallization of erbium in silicon matrix
- **Structure**: Formation of optically active erbium centers in crystalline silicon phase
- **Properties**: Photoluminescence at 1530 nm–optical property
- **Performance**: Stable and enhanced photoluminescence for anti-counterfeit label applications
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Femtosecond laser irradiation of double-layered Er/Si thin film
- effect: Formation of optically active erbium centers in silicon matrix with crystalline phase
- experiment: Raman spectroscopy analysis | Raman spectroscopy | params: Laser fluence variation, 518 cm⁻¹ peak detection | result: Appearance of peak at ≈518 cm⁻¹ indicates crystalline silicon phase formation
  - [non-referenced_knowledge] Laser radiation heats material selectively, leading to localized melting.
  - [experimental result] Raman spectra show emergence of 518 cm⁻¹ peak corresponding to crystalline silicon TO mode.
  - [deductive reasoning] Crystallization allows erbium atoms to occupy regular lattice positions, forming optically active centers.
### M2  Structure → Property
- cause: Formation of optically active erbium centers in crystalline silicon phase
- effect: Photoluminescence at 1530 nm wavelength
- experiment: Photoluminescence (PL) measurements | Confocal microscopy with excitation at 525 nm | params: Excitation wavelength 525 nm, detection range 1.4-1.7 μm | result: Strong PL signal observed at 1530 nm from laser-irradiated areas
  - [experimental result] PL spectrum shows multiple peaks near 1530 nm due to sublevel transitions in Er³⁺ ions.
  - [non-referenced_knowledge] These features correspond to fine structure of optical transitions between ^4I₁₃/₂ and ^4I₁₅/₂ levels in erbium.
  - [deductive reasoning] Uniform erbium environment in crystalline matrix leads to narrow spectral features.
### M3  Property → Performance
- cause: Photoluminescence at 1530 nm wavelength
- effect: Stable and enhanced photoluminescence for anti-counterfeit label applications
- experiment: PL stability testing under repeated excitation | Point-by-point PL scanning | params: Accumulation time 2 s per spot over 42×42 pixel array | result: No thermal degradation observed during multiple reading cycles
  - [experimental result] PL signal remains unchanged after multiple read cycles demonstrating stability.
  - [referenced knowledge] 1530 nm emission aligns with telecom industry standards for optical communication.
  - [non-referenced_knowledge] Integration with Si matrix provides mechanical protection against chemical/environmental degradation.
  - [inductive reasoning] Thus, the system offers both technical compatibility and operational robustness for security applications.
### M4  Processing → Performance
- cause: Femtosecond laser irradiation creating luminescent and non-luminescent holes
- effect: Two types of anti-counterfeiting labels with different security levels
- experiment: Label fabrication and testing | Optical microscopy and PL mapping | params: Laser fluences of 6.6 mJ/cm², spacing of 2.5 μm between spots | result: QR code successfully created and read using PL mapping technique
  - [experimental result] Single-step direct writing creates simple luminescent image patterns.
  - [experimental result] Adding chemical etching step followed by secondary laser writing creates complex indistinguishable hole arrays.
  - [non-referenced_knowledge] Only pre-recorded luminescent spots provide 1530 nm emission, forming hidden data pattern.
  - [inductive reasoning] This multi-step approach significantly enhances counterfeiting difficulty while maintaining readability.
