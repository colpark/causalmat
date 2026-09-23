# MatMech content for Advanced_Energy_Materials/aenm.202003419 (judge only; not shown to staff)
- material: Carbon host with nitrogen zincophilic sites (CnC HS)  elements: ['C', 'H', 'O', 'N', 'Zn']  category: ['Nanomaterial', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Synthesis of carbon hollow-spheres (C HS) from resorcinol–formaldehyde polymer, followed by nitrogen doping via layer-by-layer strategy using polydopamine precursor
- **Structure**: Pyridinic-nitrogen sites on carbon host forming Zn-N bonds; homogeneous zinc nucleation and mesoporous zinc-network formation
- **Properties**: Zn-N bond strength–chemical property, overpotential–electrochemical property, Coulombic efficiency–electrochemical property
- **Performance**: Suppression of zinc-dendrite formation, stable cycling performance over 7000 min in symmetric cells, high capacity retention over 500 cycles in Zn-MnO₂ battery
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Synthesis of carbon hollow-spheres (C HS) from resorcinol–formaldehyde polymer, followed by nitrogen doping via layer-by-layer strategy using polydopamine precursor
- effect: Pyridinic-nitrogen sites on carbon host forming Zn-N bonds; homogeneous zinc nucleation and mesoporous zinc-network formation
- experiment: Synthesis of CnC HS | Layer-by-layer synthesis with polydopamine precursor | params: Resorcinol–formaldehyde polymer template, nitrogen doping via polydopamine, template removal | result: Successful formation of nitrogen-doped carbon hollow spheres (CnC HS) with uniform shell thickness (~20 nm)
  - [experimental result] Nitrogen doping is introduced via polydopamine precursor during synthesis of CnC HS.
  - [experimental result] N1s NEXAFS and XPS confirm the presence of pyridinic-nitrogen in CnC HS.
  - [non-referenced_knowledge] Bader charge analysis shows nitrogen atoms carry significant negative charge (−1.1741 e), while carbon atoms are nearly neutral (0.0036 e).
  - [deductive reasoning] Electronegative nitrogen creates localized charge density gradients that attract Zn²⁺ ions.
  - [experimental result] DFT calculations show stronger binding energies of Zn on N-doped graphene (−0.072 to −0.089 eV) vs. pristine graphene (0.014 to 0.030 eV).
  - [deductive reasoning] This enhanced binding enables uniform initial nucleation, leading to mesoporous zinc-network formation instead of dendrites.
### M2  Structure → Property
- cause: Pyridinic-nitrogen sites on carbon host forming Zn-N bonds; homogeneous zinc nucleation and mesoporous zinc-network formation
- effect: Zn-N bond strength–chemical property, overpotential–electrochemical property, Coulombic efficiency–electrochemical property
- experiment: NEXAFS and Raman spectroscopy | Ex situ NEXAFS and in situ Raman | params: Zinc deposition on CnC HS and C HS; monitoring N1s and C1s spectra; normalization to G-band (1580 cm⁻¹) | result: Reduction in pyridinic-nitrogen peak (398.1 eV in NEXAFS; ~1200 cm⁻¹ in Raman) after plating confirms Zn-N bond formation; G-band remains stable.
  - [experimental result] In situ Raman shows decrease in pyridine peak (~1200 cm⁻¹) during zinc plating, indicating bonding between Zn²⁺ and pyridinic-N.
  - [experimental result] NEXAFS confirms pyridinic-N peak intensity decreases while graphitic-N increases, suggesting chemical state change due to Zn binding.
  - [experimental result] DFT shows higher charge transfer and binding energy between Zn and N-doped graphene than pristine graphene.
  - [deductive reasoning] Stronger Zn-N bonding lowers the activation energy for zinc nucleation.
  - [deductive reasoning] Lower nucleation barrier directly reduces plating overpotential and increases reversibility (Coulombic efficiency).
### M3  Structure → Property
- cause: Homogeneous zinc nucleation and mesoporous zinc-network formation
- effect: Overpotential–electrochemical property, Coulombic efficiency–electrochemical property
- experiment: Galvanostatic plating overpotential measurement | Cyclic voltammetry and charge/discharge profiling | params: Current density: 0.5, 2.0, 4.0 mA cm⁻²; areal capacity: 1 mAh cm⁻² | result: CnC HS shows lower plating overpotential (39 mV) than C HS (43 mV) at 0.5 mA cm⁻²; difference increases at higher currents.
  - [experimental result] Ex situ SEM shows planar zinc morphology on CnC HS, while C HS exhibits dendritic growth.
  - [image description] Figure 3f and 3g illustrate that zincophilic sites enable spacious nucleation, while zincophobic surfaces lead to dense, clustered nucleation.
  - [referenced knowledge] Dense nucleation causes localized high current density (tip effect), accelerating dendrite growth.
  - [non-referenced_knowledge] Spacious nucleation distributes ion flux evenly, reducing peak current density at any point.
  - [deductive reasoning] Lower peak current density reduces energy barrier for deposition, decreasing overpotential.
### M4  Property → Performance
- cause: Zn-N bond strength–chemical property, overpotential–electrochemical property, Coulombic efficiency–electrochemical property
- effect: Suppression of zinc-dendrite formation, stable cycling performance over 7000 min in symmetric cells, high capacity retention over 500 cycles in Zn-MnO₂ battery
- experiment: Symmetric cell cycling and Zn-MnO₂ battery test | Galvanostatic cycling, Coulombic efficiency measurement | params: Current density: 4 mA cm⁻², capacity: 1 mAh cm⁻²; cycling for 7000 min; Zn-MnO₂ battery over 500 cycles | result: CnC HS/Zn symmetric cell cycles >7000 min with stable voltage; C HS fails after 4000 min. CnC HS retains >90% capacity after 500 cycles in Zn-MnO₂ battery.
  - [experimental result] CnC HS exhibits 95% average Coulombic efficiency over 200 cycles, while C HS degrades after 38 cycles.
  - [experimental result] Symmetric cell with CnC HS maintains stable voltage for 7000 min; C HS shows open-circuit failure after 4000 min.
  - [non-referenced_knowledge] Low overpotential indicates minimal energy loss and high reversibility during Zn plating/stripping.
  - [deductive reasoning] High reversibility prevents accumulation of dead zinc and dendritic growth.
  - [referenced knowledge] Suppressed dendrite formation prevents separator penetration and internal short-circuit, enabling long cycle life.
### M5  Processing → Performance
- cause: Synthesis of carbon hollow-spheres (C HS) from resorcinol–formaldehyde polymer, followed by nitrogen doping via layer-by-layer strategy using polydopamine precursor
- effect: Suppression of zinc-dendrite formation, stable cycling performance over 7000 min in symmetric cells, high capacity retention over 500 cycles in Zn-MnO₂ battery
- experiment: Zn-MnO₂ battery performance test | Galvanostatic charge/discharge cycling | params: CnC HS/Zn anode paired with MnO₂ cathode; 500 cycles; 1 mA cm⁻² | result: CnC HS anode retains >90% capacity after 500 cycles; C HS anode shows significant decay after 400 cycles.
  - [experimental result] CnC HS is synthesized via nitrogen doping using polydopamine precursor during processing.
  - [experimental result] This processing step introduces pyridinic-N sites that form Zn-N bonds, as confirmed by NEXAFS and Raman.
  - [non-referenced_knowledge] Zn-N bonds lead to spacious nucleation and homogeneous Zn deposition, preventing dendrites.
  - [deductive reasoning] Dendrite suppression directly enables stable cycling over 7000 min and 500 battery cycles.
