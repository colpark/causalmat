# MatMech content for Advanced_Materials/10.1002_adma.202007978 (judge only; not shown to staff)
- material: PdPtAu alloy  elements: ['Pd', 'Pt', 'Au']  category: ['Metals and Alloys', 'Nanomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Synthesis using a modified surfactant-directing strategy, followed by removal of Pluronic F127 surfactant
- **Structure**: Mesoporous structure with pore diameter of ≈2 nm, trimetallic alloy formation confirmed by elemental mapping and line-scan energy-dispersive X-ray analysis
- **Properties**: Photocurrent response–electrical property, localized electromagnetic field–optical property, photothermal conversion–thermal property
- **Performance**: High sensitivity and selectivity for metabolic profiling in early gastric cancer diagnosis
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Synthesis using a modified surfactant-directing strategy, followed by removal of Pluronic F127 surfactant
- effect: Mesoporous structure with pore diameter of ≈2 nm, trimetallic alloy formation confirmed by elemental mapping and line-scan energy-dispersive X-ray analysis
- experiment: Synthesis and structural characterization of PdPtAu alloys | Scanning electron microscopy (SEM), transmission electron microscopy (TEM), elemental mapping, and line-scan energy-dispersive X-ray analysis | params: Synthesis with F127 surfactant, Au precursor concentration (10×10⁻³ M, 1.2 mL) | result: Uniform PdPt spheres formed after surfactant removal; pore diameter decreased to ≈15 nm for PdPtAu-1; elemental mapping showed even distribution of Pd, Pt, and Au; line-scan profile indicated trimetallic alloy formation.
  - [experimental result] PdPt spheres were synthesized using a surfactant-directing strategy, followed by surfactant removal.
  - [image description] SEM and TEM images show uniform mesoporous structure of PdPt and PdPtAu alloys.
  - [image description] Elemental mapping and line-scan EDX confirm homogeneous distribution of Pd, Pt, and Au across the alloy.
  - [non-referenced_knowledge] Surfactant-directed synthesis allows precise control over nanoparticle morphology and composition.
  - [deductive reasoning] Thus, the surfactant-directing synthesis leads to the formation of trimetallic PdPtAu alloys with mesoporous structure.
### M2  Structure → Property
- cause: Mesoporous structure with pore diameter of ≈2 nm
- effect: Localized electromagnetic field enhancement
- experiment: Finite element simulation of electromagnetic field distribution | Computational modeling under 355 nm laser excitation | params: Simulation of electric field amplitude and dissipated power density on PdPtAu-1/2/3/4 | result: PdPtAu-3 exhibited relative EM field enhancements of 23.7, approximately sevenfold higher than other compositions.
  - [experimental result] Finite element simulations reveal strong EM field enhancements in PdPtAu-3.
  - [image description] Contour plots display highest EM field amplitudes localized within mesopores of PdPtAu-3.
  - [referenced knowledge] Mesoporous noble metal structures are known to enhance plasmonic responses through localized field amplification.
  - [non-referenced_knowledge] Smaller pores improve electromagnetic field localization and enhance plasmonic performance.
  - [deductive reasoning] Therefore, the ≈2 nm mesopores in PdPtAu-3 contribute significantly to localized electromagnetic field enhancement.
### M3  Structure → Property
- cause: Trimetallic alloy formation confirmed by elemental mapping and line-scan energy-dispersive X-ray analysis
- effect: Enhanced photocurrent response
- experiment: Photoelectrochemical analysis of PdPtAu alloys | Photocurrent response measurements under UV illumination | params: Variation of Au content in PdPtAu-1/2/3/4 | result: Photocurrent increased from 0.6 mA for PdPtAu-1 to 2.1 mA for PdPtAu-3 with increasing Au content.
  - [experimental result] Photocurrent measurements show increasing response with Au content up to PdPtAu-3.
  - [image description] Photocurrent response plot indicates maximum at PdPtAu-3 composition.
  - [referenced knowledge] Trimetallic alloying enhances charge separation and reduces recombination in plasmonic systems.
  - [non-referenced_knowledge] Multiple metal components create internal potential gradients that drive directional charge flow.
  - [deductive reasoning] Thus, the trimetallic alloy structure in PdPtAu-3 contributes to enhanced photocurrent response.
### M4  Property → Performance
- cause: Localized electromagnetic field enhancement
- effect: High sensitivity and selectivity for metabolic profiling in early gastric cancer diagnosis
- experiment: LDI MS analysis of metabolite detection performance | Mass spectrometry signal intensity measurements | params: Detection of glucose, phenylalanine, and lysine using PdPtAu-1/2/3/4 matrices | result: PdPtAu-3 provided highest signal intensities for small metabolites (p < 0.05) in both standard samples and plasma.
  - [experimental result] PdPtAu-3 showed highest signal intensities for metabolite detection in LDI MS.
  - [image description] Signal intensity plot demonstrates superior performance of PdPtAu-3 over other compositions.
  - [referenced knowledge] Localized EM field enhancements increase desorption and ionization probabilities of analytes.
  - [non-referenced_knowledge] Higher EM field strength lowers detection limits and improves signal-to-noise ratios in MS analysis.
  - [deductive reasoning] Thus, the enhanced EM field from the mesoporous trimetallic structure contributes to high sensitivity and selectivity in metabolic profiling.
### M5  Property → Performance
- cause: Photothermal conversion
- effect: High sensitivity and selectivity for metabolic profiling in early gastric cancer diagnosis
- experiment: Photothermal response analysis of PdPtAu alloys | Finite element simulation of dissipated power density | params: Laser excitation at 355 nm wavelength | result: PdPtAu-3 exhibited dissipated power density of 1.18 × 10⁶, ~50 times greater than other materials.
  - [experimental result] Photothermal simulations show PdPtAu-3 has highest dissipated power density among tested compositions.
  - [image description] Dissipated power density plot confirms superior photothermal performance of PdPtAu-3.
  - [referenced knowledge] Photothermal heating enhances desorption rates of analytes through localized temperature increases.
  - [non-referenced_knowledge] Combined plasmonic and photothermal effects optimize both ionization and desorption processes in LDI MS.
  - [deductive reasoning] Therefore, the strong photothermal conversion in PdPtAu-3 contributes to its high performance in metabolic profiling.
