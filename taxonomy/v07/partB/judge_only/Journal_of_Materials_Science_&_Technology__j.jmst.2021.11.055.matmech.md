# MatMech content for Journal_of_Materials_Science_&_Technology/j.jmst.2021.11.055 (judge only; not shown to staff)
- material: Cu clusters/CdS nanorods (CuCR SCC)  elements: ['Cu', 'Cd', 'S', 'C', 'H', 'O']  category: ['Nanomaterial', 'Composite Material', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Ethylenediamine-assisted solvothermal synthesis of CdS nanorods, followed by hydrochloric acid protonation and thermal-induced annealing at 600 °C in a sulfur-containing atmosphere with copper chloride addition
- **Structure**: Cu clusters (1.6–3.2 nm) immobilized on Cd vacancies at the edges of CdS nanorods, with interfacial Cu–S coordination and cationic Cu^δ+ (1 < δ < 2) states
- **Properties**: CO production rate–photocatalytic property, turnover number (TON)–photocatalytic property, charge carrier mobility–electronic property, CO₂ adsorption capacity–adsorption property
- **Performance**: Photocatalytic CO₂-to-CO conversion with TON of 94.4 and average CO production rate of 7.7 μmol g⁻¹ h⁻¹ without sacrificial agents, enhanced photostability over 3 cycles
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Ethylenediamine-assisted solvothermal synthesis of CdS nanorods, followed by hydrochloric acid protonation and thermal-induced annealing at 600 °C in a sulfur-containing atmosphere with copper chloride addition
- effect: Cu clusters (1.6–3.2 nm) immobilized on Cd vacancies at the edges of CdS nanorods, with interfacial Cu–S coordination and cationic Cu^δ+ (1 < δ < 2) states
- experiment: Synthesis of CuCR SCC | Thermal-induced method with acid treatment and annealing | params: Protonation in 0.5 mol L⁻¹ HCl for 12 h, annealing at 600 °C for 2 h in sulfur atmosphere with CuCl₂ addition | result: Formation of Cu clusters on Cd vacancies with no ligand protection and cationic Cu^δ+ state
  - [experimental result] CdS nanorods are synthesized via ethylenediamine-assisted solvothermal method.
  - [experimental result] Protonation with HCl weakens Cd–S bonds, leading to Cd vacancy formation (CR-H).
  - [experimental result] Annealing at 600 °C in sulfur atmosphere with CuCl₂ introduces Cu species into vacancy sites.
  - [image description] AC HAADF-STEM shows Cu clusters (1.6–3.2 nm) localized at nanorod edges, with no Cu-Cu bonding.
  - [experimental result] EXAFS reveals Cu–S coordination at 1.54 Å and absence of Cu–Cu bonds, confirming atomic dispersion.
  - [non-referenced_knowledge] Cd vacancies act as trapping hubs for Cu due to coordination unsaturation and charge imbalance.
  - [non-referenced_knowledge] Thermal treatment in sulfur atmosphere prevents oxidation and stabilizes Cu–S interfacial bonds.
  - [deductive reasoning] Thus, the processing sequence enables direct, ligand-free immobilization of Cu clusters on Cd vacancies.
### M2  Structure → Properties
- cause: Cu clusters (1.6–3.2 nm) immobilized on Cd vacancies at the edges of CdS nanorods, with interfacial Cu–S coordination and cationic Cu^δ+ (1 < δ < 2) states
- effect: Enhanced CO₂ adsorption capacity, increased charge carrier mobility, and improved photocatalytic activity
- experiment: CO₂ adsorption isotherms and isosteric heat (Qst) measurement | Adsorption isotherm analysis | params: Measured at 273 K and 298 K using Quantachrome IQ2 system | result: CuCR SCC exhibits higher CO₂ uptake and Qst of 25.4 kJ mol⁻¹ vs. CR (8.9 kJ mol⁻¹)
  - [experimental result] Cu clusters exhibit cationic Cu^δ+ state (1 < δ < 2) confirmed by XANES and XPS.
  - [experimental result] EXAFS shows Cu–S coordination at 1.54 Å, indicating direct interfacial bonding.
  - [experimental result] XPS binding energy shifts in Cd 3d and S 2p indicate electron depletion from CdS and transfer to Cu.
  - [image description] PDOS shows overlap between Cu 3d and CO₂ 2p orbitals at Fermi level, confirming p-d hybridization.
  - [experimental result] Qst of 25.4 kJ mol⁻¹ for CuCR SCC indicates chemisorption, unlike physisorption in CR (8.9 kJ mol⁻¹).
  - [experimental result] DFT shows E_ads for CO₂ on Cu is −1.73 eV (C atom) vs. +0.53 eV on CR, confirming stronger adsorption.
  - [non-referenced_knowledge] Interfacial electronic modification creates a local electric field favoring electron transfer from CdS to Cu.
  - [deductive reasoning] Thus, the structure enables enhanced CO₂ adsorption and improved charge carrier mobility.
### M3  Structure → Properties
- cause: Cu clusters (1.6–3.2 nm) immobilized on Cd vacancies at the edges of CdS nanorods, with interfacial Cu–S coordination and cationic Cu^δ+ (1 < δ < 2) states
- effect: Enhanced photostability and prolonged carrier lifetime
- experiment: Time-resolved photoluminescence (PL) decay | Transient PL measurement | params: Excitation at 370 nm, decay time constants τ₁ and τ₂ measured | result: CuCR SCC shows τ₁ = 1.14 ns, longer than CR (1.00 ns) and CR-H (1.07 ns)
  - [experimental result] EPR signal at g=2.08 decreases upon photoactivation, indicating reduction of Cu²⁺ to Cu^δ+ via electron transfer.
  - [experimental result] XPS of Cu 2p shows no change after 5 h irradiation, confirming structural stability.
  - [experimental result] PL decay lifetime increases from 1.00 ns (CR) to 1.14 ns (CuCR SCC), indicating suppressed recombination.
  - [non-referenced_knowledge] Strong interfacial coupling prevents Cu cluster migration and agglomeration.
  - [deductive reasoning] Electron transfer from CdS to Cu clusters creates a sink for photogenerated electrons, reducing e⁻–h⁺ recombination.
  - [deductive reasoning] Thus, the structure enhances photostability by stabilizing clusters and accelerating charge separation.
### M4  Properties → Performance
- cause: Enhanced CO₂ adsorption capacity, increased charge carrier mobility, and improved photocatalytic activity
- effect: Photocatalytic CO₂-to-CO conversion with TON of 94.4 and average CO production rate of 7.7 μmol g⁻¹ h⁻¹ without sacrificial agents
- experiment: Photocatalytic CO₂ reduction test | Photoreactor with Xenon lamp irradiation | params: 25 mg catalyst, 5 h irradiation, no sacrificial agent, CO₂ pressure 70–80 kPa | result: CO yield: 38.3 μmol g⁻¹; average rate: 7.7 μmol g⁻¹ h⁻¹; TON: 94.4
  - [experimental result] CuCR SCC achieves CO production rate of 7.7 μmol g⁻¹ h⁻¹, 2× higher than CR and CR-H.
  - [experimental result] TON of 94.4 for CuCR SCC is significantly higher than CR (54.4) and CR-H (48.1).
  - [image description] In situ DRIFTS shows strong formation of CO₂⁻ and HCOO⁻ intermediates on CuCR SCC.
  - [image description] HCOO⁻ signal weakens on CuCR SCC, indicating rapid conversion to CO, while it remains on CR-H.
  - [experimental result] EIS and TPR show lowest impedance and highest photocurrent for CuCR SCC, confirming superior charge separation.
  - [non-referenced_knowledge] Strong CO₂ adsorption (Qst = 25.4 kJ mol⁻¹) and long carrier lifetime (τ₁ = 1.14 ns) are prerequisites for high performance.
  - [deductive reasoning] Thus, the enhanced properties directly enable superior photocatalytic performance.
