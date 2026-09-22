# MatMech content for Advanced_Materials/10.1002_adma.202004707 (judge only; not shown to staff)
- material: C5N  elements: ['C', 'N', 'H', 'Cl', 'O']  category: ['Crystalline Material', 'Nanomaterial', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Synthesis via double condensation reaction of hexaaminobenzene (HAB) trihydrochloride and pyrene-4,5,9,10-tetraone (PTK) in trifluoromethanesulfonic acid (TFMSA) at 175°C
- **Structure**: 2D fused aromatic network with evenly distributed holes and 12 nitrogen atoms in each hole, ABC stacking model with interlayer distance of 3.40 Å
- **Properties**: electron mobility–electrical property, hole mobility–electrical property, conductivity–electrical property
- **Performance**: High charge carrier mobilities up to 996 cm²V⁻¹s⁻¹ without doping and conductivity of 1038 S cm⁻¹ after doping with HCl at 160°C
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Double condensation reaction of hexaaminobenzene (HAB) trihydrochloride and pyrene-4,5,9,10-tetraone (PTK) in trifluoromethanesulfonic acid (TFMSA) at 175°C
- effect: Formation of a 2D fused aromatic network with evenly distributed holes and 12 nitrogen atoms in each hole, adopting an ABC stacking model with interlayer distance of 3.40 Å
- experiment: Synthesis of C5N | Chemical synthesis via double condensation | params: Reaction between HAB and PTK in TFMSA at 175°C | result: Formation of a 2D fused aromatic network structure confirmed by XRD and TEM
  - [experimental result] The synthesis involved a double condensation reaction between HAB and PTK in TFMSA at elevated temperature.
  - [image description] The schematic shows the resulting ABC-stacked 2D layered structure with uniform pore distribution.
  - [referenced knowledge] Aromatization provides the driving force for the spontaneous formation of pyrazine rings.
  - [non-referenced_knowledge] Pyrazine-based linkages are known to promote planar conjugated systems with high thermal stability.
  - [deductive reasoning] Thus, the synthetic conditions favor the formation of a stable 2D aromatic network with defined stacking.
### M2  Structure → Property
- cause: 2D fused aromatic network with evenly distributed holes and 12 nitrogen atoms in each hole, ABC stacking model with interlayer distance of 3.40 Å
- effect: High electron mobility (996 cm²V⁻¹s⁻¹) and hole mobility (501 cm²V⁻¹s⁻¹)
- experiment: Field-effect transistor (FET) characterization | Electrical transport measurement | params: Gate voltage sweep from -80 to +80 V on thin flakes of varying thicknesses | result: Measured mobilities up to 996 cm²V⁻¹s⁻¹ for electrons and 501 cm²V⁻¹s⁻¹ for holes in 43 nm thick films
  - [experimental result] The synthesized material exhibited a fully π-conjugated 2D structure with minimal structural disorder.
  - [image description] Transfer curves show high mobility values across various film thicknesses, indicating intrinsic transport properties.
  - [referenced knowledge] Increased carbon content in similar 2D structures correlates with higher charge mobility.
  - [non-referenced_knowledge] π-Conjugated systems allow for delocalized electronic states that reduce scattering during charge transport.
  - [deductive reasoning] Therefore, the 2D aromatic structure of C5N enables exceptional electron and hole mobilities.
### M3  Property → Performance
- cause: electron mobility–electrical property, hole mobility–electrical property
- effect: High charge carrier mobilities up to 996 cm²V⁻¹s⁻¹ without doping
- experiment: Mobility measurements in FET configuration | Electrical characterization | params: Channel width: 4 μm, channel length: 500 nm, gate voltage range: -80 to +80 V | result: Highest reported mobilities among pristine organic materials without external doping
  - [experimental result] The measured mobilities were 996 cm²V⁻¹s⁻¹ for electrons and 501 cm²V⁻¹s⁻¹ for holes in 43 nm thick films.
  - [image description] The transfer curves demonstrate strong ambipolar behavior across multiple thicknesses.
  - [referenced knowledge] Doping is often required to boost conductivity in organic materials, but introduces instability.
  - [non-referenced_knowledge] Ambipolar transport ensures balanced contribution from both carriers, enhancing overall conductivity.
  - [deductive reasoning] Therefore, the high intrinsic mobilities enable outstanding performance without the need for doping.
### M4  Processing → Property
- cause: HCl gas doping at 160°C
- effect: Conductivity increased to 1038 S cm⁻¹
- experiment: HCl doping experiment | Gas-phase chemical doping | params: HCl (35 wt%) exposure at temperatures from 20 to 160°C under vacuum | result: Conductivity increased from 7.2 S cm⁻¹ to 1038 S cm⁻¹ at 160°C
  - [experimental result] Initial conductivity was 7.2 S cm⁻¹ at room temperature after doping, rising to 1038 S cm⁻¹ at 160°C.
  - [image description] The conductivity plot shows a clear increase with doping temperature, peaking at 160°C.
  - [referenced knowledge] HCl doping is known to enhance conductivity through physical adsorption and charge transfer.
  - [non-referenced_knowledge] Acidic environments can increase free charge carrier density via protonation or electron transfer.
  - [deductive reasoning] Thus, HCl doping at elevated temperature maximizes charge transfer and enhances conductivity dramatically.
