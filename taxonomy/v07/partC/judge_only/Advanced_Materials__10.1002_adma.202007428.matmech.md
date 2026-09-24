# MatMech content for Advanced_Materials/10.1002_adma.202007428 (judge only; not shown to staff)
- material: Li metal anode  elements: ['Li', 'C', 'H', 'N', 'F', 'O', 'S']  category: ['Polymer', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Tape-casting method to fabricate a polycationic polymer protective layer
- **Structure**: Formation of a stable solid electrolyte interphase (SEI) layer and homogeneous Li deposition
- **Properties**: Li+ flux uniformity–electrical property, moisture stability–chemical property
- **Performance**: Dendrite-free Li plating/stripping in carbonate electrolyte, air-stable and water-resistant behavior
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Tape-casting method to fabricate a polycationic polymer protective layer
- effect: Formation of a stable solid electrolyte interphase (SEI) layer and homogeneous Li deposition
- experiment: XPS analysis of SEI layers | X-ray photoelectron spectroscopy (XPS) | params: SEI formed on bare Cu and PIL-coated Cu electrodes using 1 M LiPF6 in EC/DEC with 5 wt% FEC electrolyte | result: PIL-induced SEI shows presence of Li3N and LiF, indicating stable SEI formation due to TFSI anion reduction
  - [non-referenced_knowledge] PDDA–TFSI layer contains positively charged nitrogen and TFSI anions that accumulate at the Li interface.
  - [experimental result] COMSOL simulations show that the polycationic layer evens out electric field distribution during Li plating.
  - [experimental result] XPS confirms presence of Li3N and LiF in SEI formed under PIL coating, indicating TFSI-driven SEI stabilization.
  - [image description] Homogeneous Li deposition observed in SEM images supports the role of uniform Li+ flux in suppressing dendrites.
  - [deductive reasoning] Therefore, the polycationic layer enables stable SEI formation and dendrite-free Li deposition through electrostatic shielding and ion-selective interfacial chemistry.
### M2  Structure → Property
- cause: Formation of a stable solid electrolyte interphase (SEI) layer and homogeneous Li deposition
- effect: Li+ flux uniformity – electrical property
- experiment: Electrochemical impedance spectroscopy (EIS) | EIS analysis | params: Before and after cycling at 1 mA cm⁻² with 1 mAh cm⁻² for 100 h | result: Lower values of Rsf (surface film resistance) and Rct (charge transfer resistance) observed for PDDA–TFSI@Li cell
  - [experimental result] EIS results show reduced surface film resistance (Rsf) and charge transfer resistance (Rct) in PDDA–TFSI@Li cells.
  - [experimental result] XPS confirms high ionic conductivity components like Li3N in the SEI, facilitating fast Li+ transport.
  - [experimental result] Reduced overpotentials during Li plating/stripping indicate uniform Li+ flux at the electrode interface.
  - [deductive reasoning] Thus, the stable and conductive SEI ensures uniform Li+ flux by minimizing transport barriers across the interface.
### M3  Structure → Property
- cause: Formation of a stable solid electrolyte interphase (SEI) layer and homogeneous Li deposition
- effect: Moisture stability – chemical property
- experiment: Water exposure test | Visual observation and contact angle measurement | params: Droplet placed on bare Cu and PDDA–TFSI@Cu electrodes; humidity ≈60% RH | result: PDDA–TFSI@Li remains shiny and shows no color change after 1 h in ambient air; water droplet remains steady on surface for 2 min
  - [experimental result] Contact angle measurements show increased hydrophobicity of PDDA–TFSI@Cu (72°) vs bare Cu (32°).
  - [image description] Visual tests confirm delayed water penetration and absence of violent reaction on PDDA–TFSI@Li.
  - [non-referenced_knowledge] Domain knowledge states that hydrophobic coatings reduce water interaction and protect reactive surfaces.
  - [deductive reasoning] Hence, the hydrophobic TFSI-enriched layer acts as a moisture barrier, preserving Li integrity in humid environments.
### M4  Property → Performance
- cause: Li+ flux uniformity – electrical property
- effect: Dendrite-free Li plating/stripping in carbonate electrolyte
- experiment: In situ optical microscopy of Li deposition | Optical microscopy | params: Li plating at 1 mA cm⁻² on bare Cu vs PDDA–TFSI@Cu | result: Bare Cu shows inhomogeneous nucleation and Li whisker growth; PDDA–TFSI@Cu shows dense, dendrite-free Li layer
  - [experimental result] In situ optical microscopy reveals dendrite-free Li deposition on PDDA–TFSI@Cu electrode.
  - [experimental result] COMSOL simulations show that the polycationic layer flattens the current density profile across the electrode surface.
  - [non-referenced_knowledge] Domain knowledge links uniform Li+ flux to suppression of dendritic morphologies.
  - [deductive reasoning] Therefore, the PDDA–TFSI layer enables dendrite-free Li plating by enforcing uniform Li+ distribution and preventing current density localization.
### M5  Property → Performance
- cause: Moisture stability – chemical property
- effect: Air-stable and water-resistant behavior
- experiment: Air exposure and water immersion test | Environmental exposure testing | params: Exposure to ~60% RH ambient air for 1 h; water droplet placement on Li foil | result: PDDA–TFSI@Li retains metallic luster and structural integrity; bare Li turns black within 1 h and reacts violently with water
  - [experimental result] After 1 h in ambient air (~60% RH), PDDA–TFSI@Li remains shiny with no volume change.
  - [image description] Water droplets remain stable on PDDA–TFSI@Li for 2 min before slow percolation, unlike rapid reaction on bare Li.
  - [non-referenced_knowledge] Hydrophobic surfaces reduce wettability and delay water diffusion to reactive surfaces.
  - [deductive reasoning] Thus, the PDDA–TFSI coating protects Li metal from moisture attack by forming a physical and chemical barrier against water ingress.
