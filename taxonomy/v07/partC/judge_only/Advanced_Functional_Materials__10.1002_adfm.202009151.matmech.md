# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202009151 (judge only; not shown to staff)
- material: Mo-PTA@CNT  elements: ['Mo', 'P', 'W', 'O', 'C']  category: ['Composite Material', 'Nanomaterial']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Anchoring Mo species on the fourfold hollow sites of phosphotungstic acid (PTA) and embedding in multi-walled carbon nanotubes (CNT)
- **Structure**: Mo species anchored on the fourfold hollow sites of PTA, embedded in CNT
- **Properties**: ammonia yield rate–electrochemical property, Faradaic efficiency–electrochemical property
- **Performance**: High ammonia yield rate and Faradaic efficiency in electrochemical nitrogen reduction reaction (eNRR)
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Anchoring Mo species on the fourfold hollow sites of phosphotungstic acid (PTA) and embedding in multi-walled carbon nanotubes (CNT)
- effect: Mo species anchored on the fourfold hollow sites of PTA, embedded in CNT
- experiment: DRIFT and XPS analysis | Spectroscopic characterization | params: Mo-PTA samples with varying Mo content under vacuum conditions | result: Redshift observed in W–O–W bands with increasing Mo content; Mo 3d peaks indicate charge transfer from W/O to Mo species
  - [experimental result] Mo-PTA is synthesized by wet impregnation where Mo species are anchored on the fourfold hollow sites of PTA.
  - [image description] DRIFT spectra show a redshift in W–O–W bands upon Mo loading, indicating interaction between Mo and PTA framework.
  - [experimental result] XPS data reveal that Mo 3d binding energies decrease relative to bulk Mo compounds, suggesting electron enrichment from W and O atoms.
  - [referenced knowledge] Keggin-structured PTA provides defined coordination sites for anchoring transition metals like Mo.
  - [non-referenced_knowledge] The presence of CNT improves electron transport and physically stabilizes the anchored Mo-PTA structure.
  - [deductive reasoning] Thus, Mo is successfully anchored at the 4-H site of PTA and embedded in CNT, forming a stable and conductive electrocatalytic structure.
### M2  Structure → Property
- cause: Mo species anchored on the fourfold hollow sites of PTA, embedded in CNT
- effect: High ammonia yield rate and Faradaic efficiency in electrochemical nitrogen reduction reaction (eNRR)
- experiment: Electrocatalytic performance testing | Chronoamperometry, LSV, UV-Vis, ion chromatography | params: Applied potential range -0.1 V to -0.8 V vs RHE, 0.1 M K₂SO₄ electrolyte, pH 4 | result: Ammonia yield rate of 51 ± 1 μg h⁻¹ mg_cat⁻¹ and Faradaic efficiency of 83 ± 1% at -0.1 V vs RHE
  - [experimental result] Mo species anchored on PTA exhibit low oxidation states (Mo⁴⁺), as shown by XPS, enabling electron donation to inert N₂.
  - [experimental result] N₂-TPD shows strong chemical adsorption energy (50.46 kJ mol⁻¹) and low activation barrier (21.36 kJ mol⁻¹), confirming facile N₂ activation.
  - [experimental result] CNT reduces H₂O concentration at the electrode interface while enriching N₂, as confirmed by molecular dynamics simulations.
  - [non-referenced_knowledge] Hydrophobic CNT layers reduce HER side reactions by limiting proton availability, enhancing Faradaic efficiency.
  - [inductive reasoning] Thus, the unique structure of Mo-PTA@CNT enables efficient N₂ adsorption/activation and selective ammonia production.
### M3  Property → Performance
- cause: High ammonia yield rate and Faradaic efficiency in electrochemical nitrogen reduction reaction (eNRR)
- effect: High-performance electrocatalyst for ammonia synthesis under ambient conditions
- experiment: Isotope labeling and control experiments | NMR, ion chromatography, isotopic labeling | params: Use of ¹⁵N₂ gas and detection of ¹⁵NH₄⁺ by ¹H NMR and ion chromatography | result: Produced ammonia originates from N₂, not oxynitride contaminants or background sources
  - [experimental result] Mo-PTA@CNT exhibits an ammonia yield rate of 51 ± 1 μg h⁻¹ mg_cat⁻¹ and Faradaic efficiency of 83 ± 1% at -0.1 V vs RHE.
  - [experimental result] Isotope labeling confirms that all produced NH₃ originates from supplied N₂, ruling out contamination.
  - [referenced knowledge] This Faradaic efficiency surpasses many aqueous-based eNRR catalysts including bismuth nanocrystals (66%) and Au nanocages (30.2%).
  - [experimental result] Catalyst retains structure and performance after eNRR, as verified by post-reaction XRD, XPS, and SEM.
  - [deductive reasoning] Therefore, Mo-PTA@CNT demonstrates high-performance electrocatalytic ammonia synthesis under ambient conditions.
### M4  Processing → Performance
- cause: Anchoring Mo species on the fourfold hollow sites of phosphotungstic acid (PTA) and embedding in multi-walled carbon nanotubes (CNT)
- effect: High ammonia yield rate and Faradaic efficiency in electrochemical nitrogen reduction reaction (eNRR)
- experiment: Comparative eNRR tests | Chronoamperometry, DRIFT, TPD | params: Testing Mo-PTA@CNT against PTA@CNT and bare CNT electrodes under identical conditions | result: Mo-PTA@CNT shows significantly higher NH₃ yield and FE than controls; DRIFT confirms NH₃ desorption
  - [experimental result] Mo-PTA@CNT shows a fourfold increase in N₂ content at the interface compared to PTA@CNT due to CNT’s hydrophobicity.
  - [image description] Molecular dynamics simulations confirm higher interfacial N₂ density and lower H₂O concentration in Mo-PTA@CNT systems.
  - [experimental result] Optimal Mo loading (0.7%) yields highest activity; excess Mo causes aggregation and deactivation.
  - [non-referenced_knowledge] Hydrophobic CNT layer enhances gas diffusion and suppresses HER, improving overall eNRR efficiency.
  - [deductive reasoning] Thus, the combined processing steps directly lead to the observed high-performance eNRR characteristics.
