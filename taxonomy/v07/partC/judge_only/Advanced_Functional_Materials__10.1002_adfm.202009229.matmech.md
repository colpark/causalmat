# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202009229 (judge only; not shown to staff)
- material: antiGFAP-AuNPs  elements: ['Au', 'Ag', 'Si', 'O', 'C', 'H', 'N']  category: ['Nanomaterial', 'Metals and Alloys', 'Biomaterial']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Conjugation of antiGFAP antibodies with gold nanoparticles (AuNPs)
- **Structure**: Uniform monomers of antiGFAP-AuNPs with a diameter of 80 nm
- **Properties**: LSPR signals–optical property
- **Performance**: Specific binding of GFAP to the surface of PBMCs in TBI diagnosis
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Conjugation of antiGFAP antibodies with gold nanoparticles (AuNPs)
- effect: Uniform monomers of antiGFAP-AuNPs with a diameter of 80 nm
- experiment: Characterization of antiGFAP-AuNPs | Transmission Electron Microscopy (TEM), Dynamic Light Scattering (DLS), UV–vis absorption spectroscopy | params: Size measurement of AuNPs and antiGFAP-AuNPs before and after conjugation, DLS hydrodynamic size analysis, UV–vis spectral shift | result: AntiGFAP-AuNPs showed consistent diameters centered at 80 nm by TEM; DLS confirmed hydrodynamic sizes increased slightly from 90.5 ± 1.1 nm (AuNPs) to 106.5 ± 1.2 nm (antiGFAP-AuNPs); UV–vis spectra showed redshift indicating successful antibody conjugation
  - [experimental result] TEM imaging confirmed that both AuNPs and antiGFAP-AuNPs had diameters centered at 80 nm, with a visible protein layer on the latter.
  - [experimental result] Dynamic light scattering showed hydrodynamic size increased from 90.5 ± 1.1 nm for AuNPs to 106.5 ± 1.2 nm for antiGFAP-AuNPs.
  - [experimental result] UV–vis absorption spectra showed a detectable redshift after conjugation, confirming antibody attachment.
  - [referenced knowledge] Antibody conjugation to nanoparticles typically causes a measurable redshift in UV–vis absorption due to changes in surface plasmon resonance.
  - [deductive reasoning] Therefore, antiGFAP-AuNPs are uniform monomers with stable antibody conjugation, suitable for specific GFAP detection.
### M2  Structure → Performance
- cause: Uniform monomers of antiGFAP-AuNPs with a diameter of 80 nm
- effect: Specific binding of GFAP to the surface of PBMCs in TBI diagnosis
- experiment: Flow cytometry and competitive binding assays | Flow cytometry, SEM imaging, DFM imaging with computational analysis | params: Binding affinity of antiGFAP-AuNPs on PBMCs, blocking experiments using Fc blockers and free antiGFAP antibodies | result: Clone 273807 antiGFAP-Alexa488 showed 43.2 ± 2.4% binding to PBMCs; pre-treatment with same antibody reduced binding to 18.4 ± 6.8%. Blocking with Fc blockers and antiGFAP antibodies nearly eliminated nonspecific binding.
  - [experimental result] AntiGFAP-AuNPs were shown to bind specifically to GFAP antigens in vitro through flow cytometry and DLS-based binding studies.
  - [image description] SEM and DFM imaging revealed distinct antiGFAP-AuNP binding on PBMC surfaces, which was significantly reduced after blocking with Fc blockers and free antiGFAP antibodies.
  - [experimental result] Blocking experiments confirmed that antiGFAP-AuNP binding to PBMCs was primarily due to specific antigen-antibody interactions rather than nonspecific adsorption.
  - [referenced knowledge] Uniform nanoparticle size ensures reproducible binding kinetics and reduces nonspecific interactions in biological environments.
  - [deductive reasoning] Therefore, the structural uniformity of antiGFAP-AuNPs enables reliable and sensitive detection of GFAP on PBMCs for TBI diagnostics.
### M3  Processing → Performance
- cause: Conjugation of antiGFAP antibodies with gold nanoparticles (AuNPs)
- effect: Specific binding of GFAP to the surface of PBMCs in TBI diagnosis
- experiment: Competitive binding and fluorescence colocalization | Fluorescence microscopy combined with DFM imaging | params: Colocalization of antiGFAP-AuNPs with lineage-specific fluorescent markers for B cells, monocytes, NK cells, and T cells | result: 47.4% of B cells and 71.7% of monocytes showed high antiGFAP-AuNP binding (>30 AuNPs per cell), while <10% of NK and T cells showed similar binding.
  - [experimental result] AntiGFAP-AuNPs showed specific binding to GFAP-positive astrocytes but not to GFAP-negative Ovcar5 cells in control experiments.
  - [image description] Fluorescence-DNM colocalization identified high antiGFAP-AuNP binding predominantly on B cells and monocytes.
  - [referenced knowledge] Targeted nanoprobe systems improve disease detection by enhancing signal-to-noise ratios and reducing background interference.
  - [non-referenced_knowledge] Antibody-functionalized nanoprobes allow for selective molecular recognition in complex biological environments such as blood.
  - [deductive reasoning] Thus, antiGFAP-AuNP conjugation enables selective detection of GFAP on immune cell subpopulations relevant to TBI pathogenesis.
