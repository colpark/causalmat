# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202009336 (judge only; not shown to staff)
- material: PET fiber  elements: ['C', 'H', 'O', 'Zn', 'Al', 'Mo', 'N', 'Li']  category: ['Polymer', 'Ceramic', 'Metals and Alloys', 'Coatings and Thin Films', 'Nanomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Dip-coating method and thermal deposition
- **Structure**: Inverted structure with ZnO/PEI bilayer and multi-stacked layers
- **Properties**: current efficiency–electrical property, brightness–optical property
- **Performance**: Visualization of letter information on daily clothes
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Dip-coating method and thermal deposition
- effect: Inverted structure with ZnO/PEI bilayer and multi-stacked layers on PET fiber
- experiment: Fiber phOLED fabrication using dip-coating and thermal deposition | Device Fabrication | params: Dip-coating speed: 10 mm/s for ZnO NPs, 50 mm/s for EML; Thermal deposition: TCTA (~40 nm), MoO3 (~10 nm), Al (~100 nm) | result: Uniform concentric multi-layered structure formed on 300 μm diameter PET fiber
  - [image description] Figure shows cross-sectional SEM image of the fiber phOLED with clearly defined multi-stacked layers including ZnO/PEI bilayer, RGB EML, TCTA, MoO3, and Al.
  - [referenced knowledge] ZnO/PEI bilayer has been widely used as solution-processed EIL in OLEDs
  - [non-referenced_knowledge] Inverted structure was found to be more suitable for cylinder-shaped fiber substrates compared to normal structure due to balanced electron injection from uniformly coated EIL
  - [experimental result] Dip-coating enabled uniform concentric coating of solution-processed layers on the curved PET fiber surface
  - [experimental result] Thermal deposition added top layers without damaging underlying layers due to solvent orthogonality in material selection
  - [deductive reasoning] Thus, dip-coating followed by thermal deposition created the inverted structure with ZnO/PEI bilayer and multi-stacked layers on PET fiber
### M2  Structure → Property
- cause: Inverted structure with ZnO/PEI bilayer and multi-stacked layers
- effect: High current efficiency (CE) and brightness
- experiment: Current density–voltage–luminance measurements | Electroluminescence characterization | params: Applied voltage range: <8 V; Current density measurement: source meter; Luminance measurement: spectro-radiometer | result: Red, green, and blue fiber phOLEDs showed CE values of 16.3, 60.7, and 16.9 cd A⁻¹ respectively
  - [image description] Figure shows that red, green, and blue fiber phOLEDs achieved CE values of 16.3, 60.7, and 16.9 cd A⁻¹ respectively
  - [referenced knowledge] Triplet excitons can diffuse to adjacent layers without proper EBL, causing non-radiative decay
  - [non-referenced_knowledge] Efficient charge recombination requires balanced electron-hole charge transport and exciton confinement in EML
  - [experimental result] Host material combinations were selected to balance electron-hole charge flow into EML
  - [experimental result] TCTA layer acted as both HTL and EBL preventing triplet exciton loss
  - [deductive reasoning] Therefore, the inverted structure with optimized charge balance and exciton confinement resulted in high CE and brightness
### M3  Property → Performance
- cause: High current efficiency and brightness
- effect: Visualization of letter information on daily clothes
- experiment: Textile display integration and demonstration | System demonstration | params: Passive matrix addressing scheme with 4 scan lines and 4 data lines; Microcontroller board (Arduino Uno); Encapsulation with 50 nm Al₂O₃ | result: Successfully displayed distinguishable letter information ('KAIST') in both bright and dark environments
  - [image description] Photograph shows the textile display successfully visualizing letter information 'KAIST' in both bright and dark environments
  - [referenced knowledge] Commercial displays like iPhone 11 Pro have max brightness around 800 cd m⁻²
  - [non-referenced_knowledge] Wearable displays need sufficient brightness for readability under various lighting conditions
  - [experimental result] Fiber phOLEDs achieved brightness up to 11,482 cd m⁻², exceeding commercial displays
  - [experimental result] High CE values (up to 60.7 cd A⁻¹) reduced power consumption while maintaining brightness
  - [deductive reasoning] Therefore, the high CE and brightness enabled effective visualization of information on clothing under all lighting conditions
### M4  Structure → Performance
- cause: Inverted structure with ZnO/PEI bilayer and addressable pixel design
- effect: Matrix-addressable operation for displaying complex information
- experiment: Addressable fiber phOLED characterization | Electrical testing | params: Voltage application to specific pixels; Measurement of J–V–L characteristics of single unit vs. addressable device | result: Individual pixels could be independently addressed without affecting neighboring pixels
  - [image description] Figure shows schematic of contact and emission regions with different resistivity enabling selective pixel activation
  - [non-referenced_knowledge] Addressability is necessary for displaying complex information rather than just emitting light
  - [experimental result] Contact region contains Liq layer creating higher resistance compared to emission region
  - [experimental result] Current flows preferentially to lower resistance emission regions when voltage is applied through scan lines
  - [deductive reasoning] This selective current flow enables matrix addressing of individual pixels for complex information display
