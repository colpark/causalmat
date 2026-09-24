# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c04053 (judge only; not shown to staff)
- material: BioZIF-8  elements: ['Zn', 'C', 'H', 'N']  category: ['Crystalline Material', 'Nanomaterial', 'Composite Material', 'Biomaterial']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Microfluidic synthesis with aptamer surface modification
- **Structure**: Cubic morphology with encapsulated biomolecules (BSA, siRNA, DOX)
- **Properties**: pH-responsive drug release–chemical property, encapsulation efficiency–chemical property
- **Performance**: Targeted delivery to lymph nodes and tumor, biocompatibility in vivo
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Microfluidic synthesis using double spiral mixing channels
- effect: BioZIF-8 MOFs exhibit reduced average size with narrower size distribution and cubic morphology
- experiment: Dynamic light scattering (DLS) and SEM analysis of ZIF-8 MOFs | Characterization technique | params: Microfluidic flow rate: 35 μL/min; solution composition: zinc nitrate (23 mg/mL), 2-methylimidazole (220 mg/mL) | result: Hydrodynamic size ~477 ± 54 nm; core size ~373 ± 10 nm; narrow size distribution; cubic morphology confirmed by SEM
  - [non-referenced_knowledge] Double spiral channels provide transverse shearing force that enhances mixing efficiency and reduces mixing time by ~46% compared to straight channels.
  - [deductive reasoning] Enhanced mixing leads to rapid and uniform supersaturation of reactants, promoting simultaneous nucleation across the fluid stream.
  - [experimental result] Uniform nucleation followed by controlled growth results in monodisperse ZIF-8 crystals with narrow size distribution.
  - [image description] SEM images confirm cubic morphology consistent with sodalite-type ZIF-8 structure.
  - [deductive reasoning] Therefore, microfluidic processing enables precise control over ZIF-8 crystal size and morphology through improved mixing dynamics.
### M2  Processing → Structure
- cause: One-step microfluidic encapsulation of biomolecules (BSA, siRNA, DOX)
- effect: BioZIF-8 MOFs maintain cubic morphology with increased hydrodynamic size compared to neat ZIF-8
- experiment: SEM and DLS analysis of BioZIF-8 MOFs | Characterization technique | params: Encapsulated biomolecules: BSA, siRNA, DOX; flow rate: 35 μL/min | result: Hydrodynamic sizes: siRNA@ZIF-8 = 528 nm, DOX@ZIF-8 = 766 nm, BSA@ZIF-8 = 722 nm; cubic morphology preserved as shown by SEM
  - [experimental result] ZIF-8 crystallization proceeds rapidly under microfluidic conditions, trapping biomolecules within the forming framework.
  - [experimental result] Despite biomolecule presence, XRD patterns remain similar to neat ZIF-8, indicating preservation of sodalite structure.
  - [image description] Biomolecules increase hydrodynamic size but do not alter cubic morphology as seen in SEM images.
  - [non-referenced_knowledge] ZIF-8’s flexible pore architecture accommodates large biomolecules during crystallization without structural distortion.
  - [deductive reasoning] Thus, one-step microfluidic synthesis allows biomolecule encapsulation into ZIF-8 while maintaining structural identity.
### M3  Structure → Property
- cause: Cubic ZIF-8 structure with encapsulated biomolecules
- effect: High encapsulation efficiency of biomolecules (e.g., ~59% BSA, ~53.5% siRNA, ~47% DOX)
- experiment: Fluorescent labeling and UV–vis spectroscopy of encapsulation efficiency | Quantitative measurement | params: Cy5-labeled siRNA, FITC-labeled BSA, UV–vis detection of DOX concentration | result: Microfluidic BioZIF-8 shows significantly higher encapsulation efficiency than hydrothermally synthesized samples: BSA (59% vs 43%), DOX (47% vs 34.5%), siRNA (53.5% vs 37.3%)
  - [non-referenced_knowledge] ZIF-8 has a sodalite topology with interconnected cages and 3.4 Å pore apertures that allow entry of biomolecules up to ~5 kDa.
  - [experimental result] Microfluidic synthesis ensures rapid supersaturation and uniform nucleation, maximizing available internal volume for biomolecule capture.
  - [experimental result] Fluorescent and UV–vis measurements confirm significantly higher encapsulation efficiency in microfluidic BioZIF-8 compared to conventional methods.
  - [inductive reasoning] Higher encapsulation efficiency is attributed to both structural porosity and kinetic advantages of microfluidic synthesis.
### M4  Structure → Property
- cause: Positive zeta potential of BSA@ZIF-8 MOFs
- effect: Electrostatic aptamer surface functionalization with DNA/RNA aptamers
- experiment: Zeta potential and EDS mapping of aptamer-modified BioZIF-8 | Surface characterization | params: Aptamer concentration: 0–140 nM; surface charge before/after modification measured | result: Zeta potential shifts from +23.5 mV (BSA@ZIF-8) to −15.7 mV (anti-CCL21 DNA aptamer) and −13.8 mV (A10 RNA aptamer); phosphorus signal detected by EDS confirms aptamer presence
  - [experimental result] ZIF-8 MOFs possess a net positive zeta potential (+23.5 mV) in aqueous suspension due to surface-exposed Zn²+ ions.
  - [non-referenced_knowledge] DNA and RNA aptamers carry negative charges due to phosphate backbone, enabling electrostatic attraction to positively charged ZIF-8 surface.
  - [experimental result] After aptamer modification, zeta potential becomes negative (−15.7 mV and −13.8 mV), confirming successful surface functionalization.
  - [image description] EDS mapping detects phosphorus signal, verifying presence of nucleic acid aptamers on MOF surface.
  - [deductive reasoning] Therefore, the inherent surface charge of ZIF-8 enables simple and effective aptamer conjugation via electrostatic interactions.
### M5  Property → Performance
- cause: pH-responsive degradation of ZIF-8 MOFs
- effect: Controlled drug release at acidic pH (e.g., tumor microenvironment)
- experiment: pH-dependent DOX release study | Drug release assay | params: Release medium: PBS at pH 5.5, 6.5, and 7.4; time points: 0–24 h | result: DOX release accelerates at lower pH; complete release achieved at pH 5.5 within 24 h; SEM shows structural degradation at acidic pH
  - [referenced knowledge] ZIF-8 MOFs degrade at acidic pH due to protonation of imidazolate ligands and disruption of Zn–N coordination bonds.
  - [non-referenced_knowledge] Tumor microenvironment is slightly acidic (pH ~6.5–6.9), below the stability threshold of ZIF-8.
  - [experimental result] In vitro release studies show accelerated DOX release at pH 5.5 compared to neutral pH 7.4.
  - [image description] SEM images confirm structural disintegration of MOFs upon acidic exposure, consistent with enhanced drug release.
  - [deductive reasoning] Thus, the pH-responsive nature of ZIF-8 enables triggered drug release specifically in acidic tumor environments.
### M6  Processing → Performance
- cause: Two-stage microfluidic chip for integrated BioZIF-8 synthesis and aptamer functionalization
- effect: Improved targeting efficiency to lymph nodes and tumors
- experiment: In vivo fluorescence imaging of lymph node and tumor accumulation | Biological performance test | params: FITC-BSA@ZIF-8 MOFs with or without anti-CCL21 DNA aptamer (lymph node targeting) or A10 RNA aptamer (tumor targeting); administered subcutaneously or via footpad | result: Aptamer-functionalized MOFs showed significantly higher fluorescence intensity in lymph nodes and tumors; ICP-MS confirmed elevated Zn levels in target tissues
  - [experimental result] Microfluidic chip design includes two stages: first for BioZIF-8 synthesis, second for aptamer conjugation.
  - [experimental result] Zeta potential changes confirm successful aptamer attachment via electrostatic interaction.
  - [referenced knowledge] Anti-CCL21 DNA aptamer binds specifically to CCL21 in lymph node T-cell zones, enhancing lymphatic accumulation.
  - [referenced knowledge] A10 RNA aptamer recognizes PSMA on prostate cancer cells, increasing tumor-specific internalization.
  - [experimental result] In vivo imaging and ICP-MS data show significantly higher accumulation of aptamer-functionalized MOFs in target tissues.
  - [deductive reasoning] Therefore, integrated microfluidic synthesis of aptamer-BioZIF-8 MOFs enhances targeting performance through precise ligand presentation.
