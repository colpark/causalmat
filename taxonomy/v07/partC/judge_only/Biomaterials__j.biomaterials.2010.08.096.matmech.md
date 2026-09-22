# MatMech content for Biomaterials/j.biomaterials.2010.08.096 (judge only; not shown to staff)
- material: Single-walled carbon nanotubes (SWNTs)  elements: ['C', 'H', 'O']  category: ['Nanomaterial', 'Composite Material', 'Biomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Functionalization with amphiphilic PEG-PMHC18 polymers of varying PEG lengths (2 kDa, 5 kDa) and densities (5% to 100%) via covalent anchoring, followed by sonication, centrifugation, and filtration
- **Structure**: PEG-coated SWNTs with single-tube or small-bundle morphology (average length ~200 nm), stabilized in aqueous and physiological environments
- **Properties**: Blood circulation half-life–biological property, Tumor/Normal organ uptake ratio–biological property, NIR optical absorption–optical property
- **Performance**: In vivo photothermal ablation of 4T1 tumors in mice following intravenous injection and NIR laser irradiation (808 nm, 1 W/cm²)
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Functionalization with amphiphilic PEG-PMHC18 polymers of varying PEG lengths (2 kDa, 5 kDa) and densities (5% to 100%) via covalent anchoring, followed by sonication, centrifugation, and filtration
- effect: PEG-coated SWNTs with single-tube or small-bundle morphology (average length ~200 nm), stabilized in aqueous and physiological environments
- experiment: AFM imaging of PEGylated SWNTs | Atomic Force Microscopy (AFM) | params: SWNTs functionalized with 10%-5kPEG-PMHC18 and other variants; centrifuged at 21,000g for 1 h; filtered through 0.1 μm membranes | result: Functionalized nanotubes appeared as single tubes or small bundles with average length ~200 nm; no aggregation observed in solution
  - [experimental result] PEG-PMHC18 polymers were synthesized with varying molar ratios of PEG to MHC18 monomer (1:10 to 2:1) and different PEG molecular weights (2 kDa, 5 kDa).
  - [experimental result] SWNTs were sonicated in polymer solutions and purified by centrifugation and filtration to remove aggregates and excess polymer.
  - [image description] AFM images show that functionalized SWNTs are predominantly single tubes or small bundles with average length ~200 nm.
  - [non-referenced_knowledge] PEG chains provide steric stabilization by forming a hydrophilic corona that prevents nanotube-nanotube aggregation in aqueous media.
  - [deductive reasoning] Thus, controlled PEGylation density and length directly determine the degree of dispersion and resulting nanotube structure.
### M2  Processing → Properties
- cause: Functionalization with amphiphilic PEG-PMHC18 polymers of varying PEG lengths (2 kDa, 5 kDa) and densities (5% to 100%) via covalent anchoring, followed by sonication, centrifugation, and filtration
- effect: Blood circulation half-life increases with higher PEGylation degree and longer PEG chains; tumor uptake and skin accumulation also increase
- experiment: Blood circulation half-life measurement | Raman spectroscopy | params: Intravenous injection of SWNTs into tumor-bearing mice; blood samples collected at multiple time points; SWNT concentration measured as % ID/g | result: Blood half-life increased from 2.5 h (10%-2kPEG) to 20.8 h (100%-5kPEG); 10%-5kPEG-SWNTs showed 12.8 h half-life
  - [experimental result] PEGylation degree and PEG molecular weight were systematically varied to synthesize ten different polymer coatings.
  - [experimental result] Raman spectroscopy quantified SWNT concentration in blood over time, revealing a direct correlation between PEGylation and half-life (up to 20.8 h for 100%-5kPEG).
  - [referenced knowledge] Longer circulation allows more opportunities for nanotubes to extravasate through leaky tumor vasculature (EPR effect).
  - [non-referenced_knowledge] PEGylated nanomaterials evade RES uptake by reducing opsonization, prolonging systemic exposure.
  - [deductive reasoning] Thus, increased PEGylation leads to longer circulation half-life, which directly enhances both tumor and skin uptake.
### M3  Structure → Properties
- cause: PEG-coated SWNTs with single-tube or small-bundle morphology (average length ~200 nm), stabilized in aqueous and physiological environments
- effect: NIR optical absorption and blood circulation half-life are determined by surface coating density and morphology
- experiment: UV-VIS-NIR spectroscopy and Raman detection | UV-VIS-NIR spectrophotometry and Raman spectroscopy | params: SWNT solutions analyzed for optical density at 808 nm; Raman G-band at ~1590 cm⁻¹ used for quantification in tissues | result: Polymer-coated SWNTs showed strong resonance Raman scattering at ~1590 cm⁻¹ and strong NIR absorption at 808 nm, enabling quantitative in vivo tracking
  - [image description] AFM confirmed that functionalized SWNTs were single tubes or small bundles, not large aggregates.
  - [experimental result] Raman spectroscopy detected a strong G-band peak at ~1590 cm⁻¹, indicating intact nanotube structure and absence of severe defects.
  - [non-referenced_knowledge] Well-dispersed nanotubes exhibit stronger and more consistent NIR absorption than aggregated ones due to uniform electronic structure.
  - [deductive reasoning] Thus, the structural integrity achieved through PEGylation enables reliable optical properties for in vivo detection and photothermal conversion.
### M4  Properties → Performance
- cause: Blood circulation half-life of 12–13 h and high tumor uptake (~15% ID/g) with relatively low skin accumulation (~3% ID/g)
- effect: Successful in vivo photothermal ablation of 4T1 tumors following intravenous injection and 808 nm NIR laser irradiation (1 W/cm²)
- experiment: In vivo photothermal therapy | Laser irradiation and tumor volume measurement | params: 10%-5kPEG-PMHC18-SWNTs injected intravenously; 808 nm laser at 1 W/cm² applied to tumors for 5 min; tumor volume measured every 2 days for 2 weeks | result: 5 out of 7 tumors completely disappeared after treatment; no significant tumor regression in control groups (laser only, SWNT only, untreated)
  - [experimental result] SWNTs with 10%-5kPEG-PMHC18 coating showed blood half-life of 12.8 h and tumor uptake of ~15% ID/g, with low skin accumulation (~3% ID/g).
  - [experimental result] The Raman signal confirmed high tumor localization and minimal off-target accumulation.
  - [referenced knowledge] SWNTs absorb strongly at 808 nm, converting light to heat efficiently.
  - [non-referenced_knowledge] The laser power used (1 W/cm²) was lower than previously required for other nanomaterials due to superior tumor targeting.
  - [deductive reasoning] Thus, the optimized biodistribution property directly enabled effective photothermal performance at low laser power.
### M5  Processing → Performance
- cause: Functionalization with amphiphilic PEG-PMHC18 polymers of varying PEG lengths (2 kDa, 5 kDa) and densities (5% to 100%) via covalent anchoring
- effect: In vivo photothermal ablation of 4T1 tumors with high efficacy using intravenous injection and low-power NIR laser
- experiment: In vivo photothermal therapy | Laser irradiation and tumor volume measurement | params: 10%-5kPEG-PMHC18-SWNTs injected IV; 808 nm laser at 1 W/cm² applied to tumors for 5 min; tumor volume measured every 2 days | result: 5 out of 7 tumors completely disappeared; tumor growth suppressed in remaining 2; no effect in control groups
  - [experimental result] Ten different PEG-PMHC18 polymers were synthesized with varying PEG lengths and densities.
  - [experimental result] Only the 10%-5kPEG-PMHC18-SWNTs achieved the optimal balance of tumor uptake (~15% ID/g) and low skin accumulation (~3% ID/g).
  - [experimental result] This specific formulation enabled effective tumor heating under low-power laser (1 W/cm²), unlike previous studies requiring higher power.
  - [referenced knowledge] Previous attempts at systemic photothermal therapy failed due to insufficient tumor targeting or excessive off-target accumulation.
  - [deductive reasoning] Therefore, the precise control of surface chemistry during processing directly determined the success of in vivo performance.
### M6  Processing → Structure
- cause: Synthesis of 5%-2kPEG-PMHC18 polymer with limited water solubility
- effect: Failure to solubilize SWNTs, resulting in aggregation
- experiment: SWNT solubilization test | Visual observation and centrifugation | params: SWNTs sonicated in 5%-2kPEG-PMHC18 polymer solution; centrifuged at 21,000g | result: 5%-2kPEG-PMHC18 polymer could not suspend SWNTs; solution remained heterogeneous
  - [experimental result] Five different PEGylation densities (5%, 10%, 25%, 50%, 100%) were synthesized using 2kPEG and 5kPEG.
  - [experimental result] Only the 5%-2kPEG-PMHC18 polymer failed to solubilize SWNTs, while all others succeeded.
  - [non-referenced_knowledge] The 5% density corresponds to too few PEG chains per polymer backbone to shield the hydrophobic SWNT surface.
  - [deductive reasoning] Thus, insufficient PEG density during processing results in poor structural stabilization of SWNTs.
### M7  Processing → Properties
- cause: Use of 100%-5kPEG-PMHC18 polymer for SWNT functionalization
- effect: Extremely high skin accumulation (~29% ID/g) despite high tumor uptake (~23% ID/g)
- experiment: Biodistribution and skin Raman imaging | Raman spectroscopy and ex vivo skin imaging | params: Mice sacrificed 2 days post-injection; skin slices imaged with 785 nm laser and 50x objective; SWNT levels measured as % ID/g | result: 100%-5kPEG-SWNTs showed ~29% ID/g in skin, compared to ~3% ID/g for 10%-5kPEG-SWNTs
  - [experimental result] 100%-5kPEG-PMHC18-SWNTs exhibited the longest blood half-life (20.8 h) and highest tumor uptake (23% ID/g).
  - [image description] Raman imaging revealed strong SWNT signals specifically in the dermis layer of the skin.
  - [non-referenced_knowledge] The skin dermis is rich in micro-vessels (~5 μm diameter), which may act as physical traps for nanoparticles with prolonged circulation.
  - [deductive reasoning] This trapping mechanism is not observed with shorter-circulating SWNTs, as they are cleared before repeated dermal exposure.
  - [inductive reasoning] Thus, excessive PEGylation during processing leads to unintended high skin accumulation as a direct property consequence.
