# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202010623 (judge only; not shown to staff)
- material: Perovskite/PbS Quantum Dots  elements: ['Pb', 'S', 'Cd', 'Cl', 'Zn', 'O', 'Sn']  category: ['Crystalline Material', 'Nanomaterial', 'Composite Material', 'Ceramic', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Surface passivation of PbS QDs using CdCl2, ZnO nanowires passivated by SnO2 as electron transporting layer
- **Structure**: Periodic surface structures with wavelengths smaller than 0.5 mm, improved crystallinity of perovskite film
- **Properties**: Power conversion efficiency (PCE)–electrical property, open-circuit voltage (VOC)–electrical property, short-circuit current density (JSC)–electrical property, fill factor (FF)–electrical property
- **Performance**: Operational stability over 500 hours under continuous illumination, ambient stability in 65% relative humidity
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Surface passivation of PbS QDs using CdCl2
- effect: Improved crystallinity and reduced surface defects in PbS QDs
- experiment: TRPL spectroscopy of PbS QDs before and after Cd doping | Time-Resolved Photoluminescence (TRPL) | params: Bandgap of QDs: 0.92 eV; measured with and without CdCl2 passivation | result: Longer lifetime observed for Cd-doped PbS QDs
  - [experimental result] PbS QDs were synthesized with bandgaps of 0.92, 1.12, and 1.3 eV by controlling their sizes.
  - [experimental result] XPS spectra confirm presence of Cd (406.4 eV) and Cl (199.6 eV) atoms on the surface of PbS QDs after CdCl2 doping.
  - [experimental result] TRPL results show longer carrier lifetime for Cd-doped QDs compared to undoped ones.
  - [referenced knowledge] CdCl2 with low electron affinity is known to passivate the surface of PbS QDs.
  - [non-referenced_knowledge] Passivation reduces surface defects, which minimizes non-radiative recombination pathways.
  - [deductive reasoning] Thus, CdCl2 passivation leads to structurally improved PbS QDs with fewer surface defects and better charge transport properties.
### M2  Processing → Structure
- cause: ZnO nanowires passivated by SnO2 as electron transporting layer
- effect: Improved crystallinity and morphology of perovskite films deposited on ZnO NWs/SnO2 ETL
- experiment: ALD deposition of SnO2 on ZnO NWs and perovskite film characterization | Atomic Layer Deposition & XRD/SEM Analysis | params: SnO2 thickness: 4 nm; annealing temperature: 150°C | result: Pinhole-free perovskite film with average grain size ~420 nm and improved crystallinity
  - [experimental result] ZnO NWs were grown on ITO glass and conformally coated with 4 nm SnO2 using ALD.
  - [experimental result] TEM images confirm uniform amorphous SnO2 layer around ZnO NWs with d-spacing of 0.26 nm (corresponding to (002) planes).
  - [experimental result] Photoluminescence measurements show enhanced PL peak at 380 nm and quenched green emission for SnO2-coated NWs, indicating reduced surface defects.
  - [experimental result] XPS results indicate that SnO2 passivates surface defects, reducing oxygen vacancies and hydroxyl groups on ZnO NWs.
  - [referenced knowledge] ALD-deposited SnO2 has been shown to reduce surface recombination through defect passivation.
  - [non-referenced_knowledge] Reduced interfacial defects improve charge transfer efficiency and minimize recombination losses.
  - [deductive reasoning] Therefore, SnO2 passivation of ZnO NWs enhances the structural quality of the perovskite film grown on top.
### M3  Structure → Property
- cause: Improved crystallinity and morphology of perovskite films on ZnO NWs/SnO2 ETL
- effect: Higher power conversion efficiency (PCE), open-circuit voltage (VOC), and fill factor (FF) in PSCs
- experiment: Current density–voltage (J–V) measurements of PSCs | Electrical Characterization | params: Measured under standard AM1.5G illumination, reverse scan | result: Champion device shows VOC = 1.16 V, JSC = 24.4 mA/cm², FF = 78%, PCE = 22.15%
  - [experimental result] Perovskite films on ZnO NWs/SnO2 ETL show pinhole-free morphology and larger grain size (~420 nm).
  - [experimental result] XRD patterns reveal excellent crystallinity with minimal PbI₂ phase impurity.
  - [experimental result] Steady-state PL and TRPL measurements indicate faster charge transfer and lower recombination rates.
  - [referenced knowledge] Improved crystallinity enhances charge transport and reduces non-radiative recombination.
  - [non-referenced_knowledge] Fewer defects mean less energy loss and more efficient charge collection.
  - [deductive reasoning] Hence, structural improvements directly translate into higher VOC, JSC, FF, and overall PCE.
### M4  Property → Performance
- cause: Higher power conversion efficiency (PCE), open-circuit voltage (VOC), and fill factor (FF) in PSCs
- effect: Improved operational stability over 500 hours under continuous illumination
- experiment: Operational stability test of tandem solar cells | Stability Measurement Under Illumination | params: Continuous illumination, nitrogen environment | result: Tandem device retains 94% of initial PCE after 500 hours
  - [experimental result] 2T-tandem device achieves stabilized PCE of 17.1% with minimal hysteresis.
  - [experimental result] Operational stability test shows only 6% PCE loss after 500 h under continuous illumination.
  - [experimental result] Device retains >94% of initial PCE even after extended operation.
  - [referenced knowledge] Structural and interfacial improvements are known to enhance stability against light-induced degradation.
  - [non-referenced_knowledge] Lower defect density reduces degradation pathways such as ion migration and phase segregation.
  - [inductive reasoning] Thus, enhanced photovoltaic performance correlates with improved operational stability in tandem devices.
### M5  Processing → Performance
- cause: Use of PbS QDs back cell in tandem configuration
- effect: Excellent ambient stability in 65% relative humidity over 70 days
- experiment: Ambient stability test of single-junction and tandem devices | Environmental Stability Testing | params: 65% relative humidity, no packaging | result: Tandem device shows no PCE loss after 70 days; single-junction PSC loses 37% of initial efficiency
  - [experimental result] Ambient stability tests show tandem device retains full PCE after 70 days at 65% RH, while single-junction PSC degrades significantly.
  - [image description] Water contact angle measurement indicates high hydrophobicity of PbS QDs layer (~97°).
  - [referenced knowledge] PbS QDs are known for excellent air stability and resistance to moisture.
  - [non-referenced_knowledge] Hydrophobic coatings prevent moisture ingress and protect sensitive interfaces.
  - [deductive reasoning] Therefore, incorporation of PbS QDs back cell improves ambient stability by acting as a physical and chemical barrier against humidity.
