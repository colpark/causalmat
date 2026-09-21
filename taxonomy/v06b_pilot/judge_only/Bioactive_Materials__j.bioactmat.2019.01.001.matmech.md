# MatMech content for Bioactive_Materials/j.bioactmat.2019.01.001 (judge only; not shown to staff)
- material: High purity magnesium (HP-Mg), High purity zinc (HP-Zn), Pure iron (P-Fe)  elements: ['Mg', 'Zn', 'Fe']  category: ['Metals and Alloys', 'Biomaterial', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Cut into disks (Ø10 × 2 mm), polished by SiC abrasive paper up to 2000 grit
- **Structure**: Corrosion products formed include carbonate and phosphate layers; surface morphology changes observed via SEM; protective film formation influenced by protein (porcine stomach mucin) and bicarbonate
- **Properties**: Corrosion rate–chemical property, Corrosion potential–electrochemical property, Corrosion current density–electrochemical property, Cytocompatibility–biological property
- **Performance**: Suitability as tracheobronchial stent material due to controlled degradation in respiratory fluid (Gamble's solution) and favorable cell adhesion/proliferation of A549 cells for HP-Mg and HP-Zn
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Cut into disks (Ø10 × 2 mm), polished by SiC abrasive paper up to 2000 grit
- effect: Surface morphology changes observed via SEM; corrosion products formed include carbonate and phosphate layers; protective film formation influenced by protein (porcine stomach mucin) and bicarbonate
- experiment: Static immersion test and surface characterization | SEM, EDS, FTIR | params: Immersion in Gamble's solution (GS) and SBF for 7, 14, 21, and 28 days at 37°C; solution-to-sample ratio of 20 mL/cm² | result: SEM revealed localized corrosion initiation on HP-Mg in GS; EDS and FTIR confirmed carbonate and phosphate corrosion products; protein presence reduced phosphate precipitation
  - [experimental result] High purity magnesium, zinc, and iron were cut into disks and polished with SiC abrasive paper up to 2000 grit.
  - [image description] SEM images show distinct corrosion morphologies after immersion in GS and SBF, with HP-Mg exhibiting widespread pitting and HP-Zn/P-Fe showing localized attack.
  - [experimental result] EDS and FTIR confirm corrosion products are primarily carbonate and phosphate.
  - [referenced knowledge] Protein (porcine stomach mucin) in GS interferes with phosphate precipitation, reducing protective film formation [16].
  - [non-referenced_knowledge] Smooth, polished surfaces provide fewer nucleation sites for corrosion, promoting uniform film growth.
  - [deductive reasoning] Thus, the polishing process enables consistent corrosion product layer formation influenced by solution composition.
### M2  Structure → Properties
- cause: Corrosion products formed include carbonate and phosphate layers; surface morphology changes observed via SEM; protective film formation influenced by protein (porcine stomach mucin) and bicarbonate
- effect: Corrosion rate–chemical property, Corrosion potential–electrochemical property, Corrosion current density–electrochemical property, Cytocompatibility–biological property
- experiment: Potentiodynamic polarization (PDP) and corrosion rate measurement | Electrochemical testing, Weight loss method | params: PDP in GS and SBF; corrosion rate calculated after 28-day immersion after removing corrosion products with CrO₃ solution | result: HP-Mg showed lower corrosion current density and more noble corrosion potential in GS than SBF; corrosion rates in GS were 0.78 mm/y (Mg), 0.034 mm/y (Zn), 0.102 mm/y (Fe), lower than in SBF.
  - [experimental result] Corrosion products detected by FTIR and EDS are carbonate and phosphate, forming a protective layer [19].
  - [referenced knowledge] Protein in GS reduces phosphate precipitation, leading to a less stable film [16].
  - [referenced knowledge] Lower chloride and higher bicarbonate in GS reduce pitting and promote passivation [13,14,17].
  - [experimental result] PDP results show HP-Mg has higher corrosion potential and lower current density in GS than SBF, indicating slower corrosion [17].
  - [experimental result] Corrosion rates measured after 28 days confirm slower degradation in GS (0.78 mm/y for Mg) compared to SBF (2.01 mm/y).
  - [non-referenced_knowledge] Slower corrosion reduces metal ion release, improving cytocompatibility.
  - [deductive reasoning] Thus, the structure of the corrosion layer governs the electrochemical properties and biological response.
### M3  Properties → Performance
- cause: Corrosion rate–chemical property, Corrosion potential–electrochemical property, Corrosion current density–electrochemical property, Cytocompatibility–biological property
- effect: Suitability as tracheobronchial stent material due to controlled degradation in respiratory fluid (Gamble's solution) and favorable cell adhesion/proliferation of A549 cells for HP-Mg and HP-Zn
- experiment: Cytocompatibility assessment via CCK-8, SEM, LSCM, and ICP-OES | Cell viability assay, Cell morphology imaging, Ion concentration measurement | params: A549 cells cultured under DC, IC, EC methods for 1, 3, 5 days; CCK-8 at 450 nm; SEM/LSCM for morphology; ICP-OES for ion release in EC medium | result: HP-Mg and HP-Zn showed no significant cytotoxicity and good cell adhesion in DC and EC; P-Fe showed cytotoxicity at 48h and reduced cell density at 96h; Zn²⁺ (0.23 mM) and Mg²⁺ (6.03 mM) were non-toxic; Fe²⁺/Fe³⁺ (1.52 mM) was cytotoxic.
  - [experimental result] HP-Mg and HP-Zn exhibit lower corrosion rates in GS than in SBF, with values of 0.78 mm/y and 0.034 mm/y, respectively.
  - [experimental result] ICP-OES shows Zn²⁺ (0.23 mM) and Mg²⁺ (6.03 mM) concentrations in EC medium are below cytotoxic thresholds.
  - [experimental result] Fe²⁺/Fe³⁺ concentration (1.52 mM) in EC medium exceeds cytotoxic levels, causing reduced cell viability.
  - [experimental result] CCK-8 and SEM show HP-Mg and HP-Zn support high A549 cell density and normal epithelioid morphology, while P-Fe does not.
  - [non-referenced_knowledge] Clinical requirement for pediatric tracheal stents is temporary support (3–12 months) with no long-term foreign body effects [8].
  - [deductive reasoning] Thus, HP-Mg and HP-Zn meet performance criteria: controlled degradation and biocompatibility in respiratory environment.
