# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c04362 (judge only; not shown to staff)
- material: Prussian blue analogue nanocomposites  elements: ['Fe', 'C', 'N', 'K', 'Na', 'Cl', 'O', 'H']  category: ['Nanomaterial', 'Composite Material', 'Polymer', 'Biomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: UV-polymerized hydrogel embedding nanocomposite electrodes
- **Structure**: Porous electrodes with uniformly distributed active materials
- **Properties**: discharging capacity–electrical property, mechanical stability–mechanical property, biocompatibility–biological property
- **Performance**: operation in artificial tears, compatibility with contact lens cleaning solution, power supply to low-power microprocessor
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: UV-polymerized hydrogel embedding nanocomposite electrodes
- effect: Porous electrodes with uniformly distributed active materials
- experiment: Electrode fabrication and SEM imaging | Scanning Electron Microscopy (SEM) | params: 50 μm thick electrode fabricated via doctor blading and UV polymerization in molds | result: Uniform distribution of active materials confirmed by cross-sectional SEM image
  - [experimental result] Film electrodes of the PBA nanocomposite were prepared by doctor blading and UV polymerization.
  - [image description] Cross-sectional SEM image shows active materials uniformly distributed in the porous matrix.
  - [referenced knowledge] Doctor blading and UV polymerization techniques are commonly used for fabricating porous electrode structures.
  - [non-referenced_knowledge] UV-polymerization allows for precise control over pore structure and material distribution in composite electrodes.
  - [deductive reasoning] Therefore, UV-polymerized hydrogel embedding leads to porous electrodes with uniform distribution of active materials.
### M2  Structure → Property
- cause: Porous electrodes with uniformly distributed active materials
- effect: discharging capacity–electrical property
- experiment: Galvanostatic cycling with potential limitation (GCPL) | Electrochemical testing | params: Current density of 100 μA between 0.2 and 0.9 V vs SHE in artificial tears | result: Battery exhibits 155.4 μAh discharge capacity at 100 μA
  - [non-referenced_knowledge] Porous electrodes allow for good ion permeability and large surface area contact with electrolyte.
  - [image description] GCPL curves show consistent charge-discharge behavior with high capacity retention even after deformation into contact lens shape.
  - [referenced knowledge] Porous electrode structures enhance electrochemical performance by increasing surface area and ion accessibility.
  - [deductive reasoning] Therefore, the uniform porous structure of the electrode enables high discharging capacity through improved ion and electron transport.
### M3  Structure → Property
- cause: Porous electrodes with uniformly distributed active materials
- effect: mechanical stability–mechanical property
- experiment: Mechanical bending test | Cyclic bending test | params: Repeated radial compression exceeding 20,000 cycles | result: Battery retains 63.3% capacity after 100 cycles under repeated bending
  - [experimental result] Battery was bent more than 20,000 times and showed only minor degradation in capacity.
  - [image description] Photos show full structural recovery when compressive displacement is released.
  - [referenced knowledge] Flexible porous structures can accommodate mechanical strain through microstructural rearrangement.
  - [non-referenced_knowledge] Hydrogel matrices provide mechanical compliance while maintaining structural integrity under repeated deformation.
  - [deductive reasoning] Thus, the porous electrode structure embedded in hydrogel provides mechanical stability through compliant deformation mechanisms.
### M4  Structure → Property
- cause: Porous electrodes with uniformly distributed active materials
- effect: biocompatibility–biological property
- experiment: Cytotoxicity test | Cell viability assay | params: MDA-MB-231 cells cultured during battery operation in DMEM medium at 40 μA | result: No significant difference in dead cell amount or total cell density compared to controls
  - [experimental result] Cells grown during battery operation showed no obvious differences in viability compared to controls.
  - [image description] Microscope images confirm similar live/dead cell ratios between battery samples and controls.
  - [referenced knowledge] Prussian blue analogues have been shown to be biocompatible due to their non-toxic redox chemistry.
  - [non-referenced_knowledge] Uniform material distribution minimizes localized toxicity effects from concentration gradients.
  - [deductive reasoning] Therefore, the uniform distribution of biocompatible PBA nanocomposites ensures overall biocompatibility of the device.
### M5  Property → Performance
- cause: discharging capacity–electrical property
- effect: operation in artificial tears
- experiment: Electrochemical characterization in artificial tears | Galvanostatic discharge measurement | params: Artificial tears containing 0.15 M NaCl and 0.02 M KCl at pH 7 | result: Battery delivers 155.4 μAh capacity at 100 μA in artificial tears
  - [experimental result] Battery delivers 155.4 μAh capacity at 100 μA in artificial tears with cutoff voltages of 0.2 and 0.9 V.
  - [image description] GCPL curve shows stable discharge profile with clear voltage plateaus in artificial tears.
  - [referenced knowledge] Tear electrolytes contain primarily sodium and potassium ions that serve as effective charge carriers.
  - [non-referenced_knowledge] Discharge capacity determines the energy available for device operation in physiological environments.
  - [deductive reasoning] Thus, the measured discharge capacity enables reliable operation of the battery in tear electrolyte conditions.
### M6  Property → Performance
- cause: mechanical stability–mechanical property
- effect: compatibility with contact lens cleaning solution
- experiment: Cleaning solution compatibility test | Cycling test in commercial cleaning solution | params: Bausch+Lomb renu fresh solution at 100 μA with 0.2-0.9 V cutoff | result: Battery retains >72% capacity after 50 cycles in cleaning solution
  - [experimental result] Battery presents stable GCPL curve even in commercial cleaning solution containing disinfectants and protein removers.
  - [image description] Photograph confirms battery remains physically intact in cleaning solution.
  - [referenced knowledge] Contact lens cleaning solutions often involve physical agitation that requires mechanical robustness.
  - [non-referenced_knowledge] Mechanical stability prevents structural degradation during handling and cleaning procedures.
  - [deductive reasoning] Therefore, the mechanical stability of the battery enables compatibility with standard contact lens cleaning protocols.
### M7  Property → Performance
- cause: biocompatibility–biological property
- effect: power supply to low-power microprocessor
- experiment: SRAM power demonstration | Integrated circuit operation | params: Low-power static random-access memory powered by battery in artificial tears | result: Successful operation of SRAM with measured waveforms confirming functionality
  - [experimental result] Battery successfully powers a low-power SRAM demonstrating practical utility.
  - [image description] Measured waveforms confirm proper SRAM operation when powered by the battery.
  - [non-referenced_knowledge] Biocompatibility ensures long-term safety for devices operating in proximity to sensitive biological tissues.
  - [referenced knowledge] Biocompatibility is essential for any device intended for prolonged contact with ocular surfaces.
  - [deductive reasoning] Hence, the biocompatibility of the battery enables safe operation while powering integrated microelectronics.
