# MatMech content for Advanced_Composites_and_Hybrid_Materials/s42114-021-00398-8 (judge only; not shown to staff)
- material: FL-Ti3C2/BiOCl/SnO2 ternary composite  elements: ['Ti', 'C', 'Bi', 'O', 'Sn']  category: ['Nanomaterial', 'Composite Material', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Mechanical mixing of FL-Ti3C2, BiOCl, and SnO2 followed by hydrothermal treatment at 120°C for 12 h, and deposition on melamine sponge via multiple dipping-drying cycles
- **Structure**: 2D/2D heterojunction with SnO2 nanoparticles embedded between FL-Ti3C2 and BiOCl sheets; p-n junction formed between BiOCl and SnO2; super-hydrophilic surface due to FL-Ti3C2
- **Properties**: Band gap–optical property, Photoluminescence intensity–electronic property, Hydrophilicity–surface property
- **Performance**: 90.3% formaldehyde degradation rate under UV irradiation; 85.2% retention after 5 recycling cycles
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Mechanical mixing of FL-Ti3C2, BiOCl, and SnO2 followed by hydrothermal treatment at 120°C for 12 h, and deposition on melamine sponge via multiple dipping-drying cycles
- effect: 2D/2D heterojunction with SnO2 nanoparticles embedded between FL-Ti3C2 and BiOCl sheets; p-n junction formed between BiOCl and SnO2; super-hydrophilic surface due to FL-Ti3C2
- experiment: Preparation of FL-Ti3C2/BiOCl/SnO2 ternary nanocomposite | Hydrothermal synthesis | params: 0.15 g SnO2, 0.26 g BiOCl, 0.17 g FL-Ti3C2 in 10 mL water, 120°C for 12 h | result: Formation of ternary nanocomposite with confirmed component integration
  - [experimental result] FL-Ti3C2, BiOCl, and SnO2 were mechanically mixed and subjected to hydrothermal treatment at 120°C for 12 h.
  - [image description] SEM images show FL-Ti3C2 sheets loaded with BiOCl flakes and SnO2 nanoparticles, indicating structural integration.
  - [experimental result] XRD confirms the presence of characteristic peaks for all three components in the composite, proving structural coexistence.
  - [referenced knowledge] BiOCl and SnO2 can form a p-n heterojunction due to their respective band alignments [32].
  - [non-referenced_knowledge] FL-Ti3C2 has a 2D layered structure that facilitates intercalation and interfacial bonding with other 2D materials.
  - [deductive reasoning] Thus, the processing method leads to a 2D/2D heterojunction with embedded SnO2 nanoparticles, a p-n junction between BiOCl and SnO2, and a super-hydrophilic surface due to FL-Ti3C2.
### M2  Structure → Properties
- cause: 2D/2D heterojunction with SnO2 nanoparticles embedded between FL-Ti3C2 and BiOCl sheets; p-n junction formed between BiOCl and SnO2; super-hydrophilic surface due to FL-Ti3C2
- effect: Reduced photoluminescence intensity, lowered band gap (3.33 eV), and enhanced hydrophilicity (contact angle 16°)
- experiment: Photoluminescence (PL) spectroscopy | Photoluminescence analysis | params: Excitation wavelength: 300 nm | result: FBS shows weaker PL peak than individual components, indicating suppressed electron-hole recombination
  - [experimental result] FBS exhibits a significantly weaker PL peak than individual components, indicating reduced electron-hole recombination.
  - [experimental result] UV-Vis DRS shows FBS has a band gap of 3.33 eV, lower than SnO2 (3.80 eV) and BiOCl (3.40 eV), due to composite formation.
  - [image description] The contact angle of FBS is 16°, indicating super-hydrophilicity inherited from FL-Ti3C2.
  - [non-referenced_knowledge] A p-n junction between BiOCl and SnO2 creates an internal electric field that promotes charge separation [60].
  - [non-referenced_knowledge] FL-Ti3C2's super-hydrophilicity enhances adsorption of polar formaldehyde molecules.
  - [deductive reasoning] Therefore, the heterojunction structure leads to reduced PL intensity (better charge separation), lower band gap (better light absorption), and higher hydrophilicity (better adsorption).
### M3  Structure → Performance
- cause: 2D/2D heterojunction with SnO2 nanoparticles embedded between FL-Ti3C2 and BiOCl sheets; p-n junction formed between BiOCl and SnO2; super-hydrophilic surface due to FL-Ti3C2
- effect: 90.3% formaldehyde degradation rate under UV irradiation; 85.2% retention after 5 recycling cycles
- experiment: Photocatalytic degradation of HCHO under UV | Photocatalytic performance test | params: UV lamp (365 nm, 15 W), initial HCHO concentration 1–1.2 mg/m³, 70 min irradiation | result: 3SFBS achieves 90.3% degradation rate, outperforming single components and other composites
  - [experimental result] FBS composite shows reduced PL intensity, indicating suppressed electron-hole recombination.
  - [experimental result] UV-Vis DRS confirms a reduced band gap (3.33 eV) for FBS, enabling better visible light utilization.
  - [image description] The p-n junction between BiOCl and SnO2 creates an internal electric field that drives electron transfer to SnO2 and then to FL-Ti3C2 [60].
  - [non-referenced_knowledge] FL-Ti3C2’s super-hydrophilicity enhances adsorption of polar formaldehyde molecules on the catalyst surface.
  - [non-referenced_knowledge] Melamine sponge’s porous structure provides high surface area and efficient gas diffusion to catalytic sites.
  - [deductive reasoning] Thus, the combined structural advantages lead to 90.3% formaldehyde degradation and 85.2% retention after 5 cycles.
### M4  Processing → Performance
- cause: Deposition on melamine sponge via multiple dipping-drying cycles (nSFBS, n=1 to 5)
- effect: Degradation rate first increases to 90.3% at 3SFBS, then decreases at higher immersion numbers
- experiment: Photocatalytic degradation with varying immersion cycles | Photocatalytic performance test | params: 1SFBS to 5SFBS, UV irradiation for 70 min | result: Degradation rates: 71.2% (1SFBS), 79.1% (2SFBS), 90.3% (3SFBS), 86.8% (4SFBS), 61.9% (5SFBS)
  - [experimental result] The degradation rate increases from 1SFBS (71.2%) to 3SFBS (90.3%) with increasing immersion cycles.
  - [experimental result] Beyond 3 cycles, degradation rate decreases (4SFBS: 86.8%, 5SFBS: 61.9%).
  - [non-referenced_knowledge] The sponge’s porous structure allows gas transport; excess catalyst blocks these channels.
  - [inductive reasoning] Thus, the processing method (dipping cycles) directly influences performance by controlling catalyst loading and gas diffusion efficiency.
