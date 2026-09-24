# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c04959 (judge only; not shown to staff)
- material: High-concentration polymeric interlayer (PVC-based)  elements: ['C', 'H', 'O', 'Li', 'N', 'S', 'F']  category: ['Polymer', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Thermal cross-linking of PVC solution with LiTFSI salt
- **Structure**: Abundant solvation sites and conductive nanochannels formed by interactions between anions and polymer chains
- **Properties**: Ionic conductivity–electrical property, oxidation resistance–chemical property
- **Performance**: Improved cycle life and high Coulombic efficiency in all-solid-state batteries with high-voltage cathodes
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Thermal cross-linking of PVC solution with LiTFSI salt
- effect: Abundant solvation sites and conductive nanochannels formed by interactions between anions and polymer chains
- experiment: FTIR spectroscopy before and after cross-linking | Fourier-transform infrared (FTIR) spectroscopy | params: PVC solution before and after thermal cross-linking, varying LiTFSI concentrations | result: Changes in functional group peaks indicate successful polymerization and ion dissociation
  - [experimental result] The preparation process involves thermal cross-linking of PVC with LiTFSI to form a polymeric interlayer.
  - [image description] FTIR spectra confirm that functional groups like C=O coordinate with Li⁺ ions, promoting salt dissociation.
  - [non-referenced_knowledge] Salt-polymer interactions create additional solvation sites for Li⁺ conduction.
  - [deductive reasoning] High salt concentration leads to formation of conductive nanochannels due to anion-induced chain separation.
### M2  Structure → Property
- cause: Abundant solvation sites and conductive nanochannels formed by interactions between anions and polymer chains
- effect: Ionic conductivity–electrical property
- experiment: Electrochemical impedance spectroscopy (EIS) | EIS measurements with stainless steel blocking electrodes | params: Temperature range: 25–90°C | result: Conductivity of 1.1 × 10⁻⁴ S cm⁻¹ at 30°C and 4 × 10⁻⁴ S cm⁻¹ at 60°C
  - [experimental result] FTIR analysis shows strong coordination between Li⁺ and carbonyl groups in PVC chains.
  - [image description] EIS data demonstrate low impedance and high conductivity in PVC compared to PEO.
  - [non-referenced_knowledge] Anion-induced chain separation creates nanochannels that allow rapid ion transport.
  - [deductive reasoning] Therefore, the structure of the high-concentration polymeric interlayer directly enables high ionic conductivity.
### M3  Structure → Property
- cause: Abundant solvation sites and conductive nanochannels formed by interactions between anions and polymer chains
- effect: Oxidation resistance–chemical property
- experiment: Linear sweep voltammetry (LSV) | LSV with stainless steel working electrode | params: Voltage sweep from 2.5 V to 5.0 V vs Li/Li⁺ | result: Negligible current density (<2 μA cm⁻²) up to 5.0 V vs Li/Li⁺
  - [image description] LSV experiments show PVC-coated SSE exhibits negligible current up to 5.0 V, indicating high oxidation resistance.
  - [referenced knowledge] TFSI⁻ anions have low HOMO energy levels, reducing susceptibility to oxidation.
  - [non-referenced_knowledge] Carbonyl and ether groups in PVC are inherently resistant to oxidation due to electron stabilization.
  - [deductive reasoning] Thus, the structural design of the polymeric interlayer imparts excellent chemical stability under high voltage conditions.
### M4  Property → Performance
- cause: Ionic conductivity–electrical property
- effect: Improved cycle life and high Coulombic efficiency in all-solid-state batteries with high-voltage cathodes
- experiment: Cycling tests on Li | PVC-NCM battery | Galvanostatic cycling at 60°C | params: Voltage window: 2.5–4.25 V, 100 cycles | result: 75% capacity retention and >99.9% Coulombic efficiency after 100 cycles
  - [image description] EIS measurements show reduced interfacial resistance in PVC-coated NCM cells.
  - [non-referenced_knowledge] Lower interfacial resistance leads to improved charge transport and reduced overpotential.
  - [deductive reasoning] Uniform Li⁺ flux minimizes side reactions and maintains structural integrity of the cathode.
  - [deductive reasoning] As a result, high ionic conductivity directly contributes to improved cycling performance and Coulombic efficiency.
### M5  Property → Performance
- cause: Oxidation resistance–chemical property
- effect: Improved cycle life and high Coulombic efficiency in all-solid-state batteries with high-voltage cathodes
- experiment: Cycling tests on Li | PVC-LCO battery | Galvanostatic cycling at 60°C | params: Voltage window: 2.5–4.2 V, 100 cycles | result: 90% capacity retention and >99.9% Coulombic efficiency after 100 cycles
  - [experimental result] LSV experiments confirm PVC’s stability up to 5.0 V, preventing decomposition during high-voltage operation.
  - [image description] PVC coating eliminates pore-related issues and provides continuous ion pathways in composite cathodes.
  - [non-referenced_knowledge] Stable interface reduces parasitic reactions and maintains active material accessibility.
  - [deductive reasoning] Thus, oxidation resistance ensures durable interface functionality, contributing to improved battery performance.
