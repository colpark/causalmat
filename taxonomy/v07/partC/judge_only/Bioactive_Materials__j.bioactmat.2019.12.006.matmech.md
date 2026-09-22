# MatMech content for Bioactive_Materials/j.bioactmat.2019.12.006 (judge only; not shown to staff)
- material: 316L stainless steel with PPAmF coating  elements: ['Fe', 'Cr', 'Ni', 'C', 'H', 'O', 'N', 'F', 'S', 'Na']  category: ['Metals and Alloys', 'Polymer', 'Composite Material', 'Nanomaterial', 'Coatings and Thin Films', 'Biomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Pulsed radio frequency plasma polymerization of allylamine (PPAm) and hexafluoroethane/acetylene (C-F) to form a composite PPAmF coating, followed by surface grafting of bivalirudin (BVLD) via NHS-EDC coupling and bulk loading of nitric oxide (NO) under high pressure with sodium methoxide
- **Structure**: Multilayered composite coating with alternating hydrophilic PPAm (amine-rich) and hydrophobic C-F layers; formation of diazeniumdiolate (NONOate) groups in the bulk for NO storage
- **Properties**: Anti-platelet–biological property, Anti-coagulant–biological property, Nitric oxide release–chemical property, Water contact angle–surface property
- **Performance**: Highly endothelium-mimetic thromboresistant property in ex vivo blood circulation; reduced platelet adhesion, fibrinogen adsorption/activation, and thrombus formation; sustained NO release over 8 hours; maintenance of 90.4% blood flow rate after 2 hours of circulation
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Pulsed radio frequency plasma polymerization of allylamine (PPAm) and hexafluoroethane/acetylene (C-F) to form a composite PPAmF coating with alternating hydrophilic and hydrophobic layers
- effect: Formation of a multilayered composite coating with alternating 30 nm PPAm layers and 20 nm C-F layers, resulting in a structure that resists water invasion and reduces hydrolytic degradation of diazeniumdiolates
- experiment: PPAmF coating fabrication | Pulsed radio frequency plasma polymerization | params: 6 sccm allylamine, 0.5 sccm Ar, 80 W RF power, 25% duty cycle (ton=250 μs, toff=750 μs), 150 V bias; C-F: 5 sccm C2F6, 0.5 sccm C2H2, 90 W RF power, 80% duty cycle, 150 V bias; 10-layer PPAm + 9-layer C-F, total PPAm thickness ~300 nm | result: PPAmF coating successfully fabricated with alternating hydrophilic and hydrophobic nano-layers
  - [experimental result] PPAm and C-F coatings are deposited using pulsed RF plasma polymerization with specific gas flows and power parameters.
  - [experimental result] The PPAmF coating consists of 10 alternating layers of PPAm (30 nm) and C-F (20 nm), creating a multilayered nanostructure.
  - [non-referenced_knowledge] Hydrophobic C-F layers resist water invasion, which is known to accelerate hydrolysis of diazeniumdiolates.
  - [experimental result] The layered architecture reduces burst release and extends NO release duration to over 8 hours compared to single-layer PPAm.
  - [deductive reasoning] Thus, the processing method of alternating layer deposition directly engineers a structure that enhances stability of NO storage.
### M2  Processing → Structure
- cause: Surface grafting of bivalirudin (BVLD) via NHS-EDC coupling reaction on PPAmF coating
- effect: Covalent immobilization of BVLD onto surface primary amine groups of PPAmF, preserving the bulk amine groups for NO loading
- experiment: BVLD immobilization via NHS-EDC coupling | Chemical grafting | params: 1 mg/mL BVLD in WSC solution (MES, NHS, EDC), pH 5.6, 12 h reaction time | result: Successful covalent immobilization of BVLD on PPAmF surface confirmed by GATR-FTIR and QCM-D
  - [experimental result] BVLD is immobilized using NHS-EDC chemistry in aqueous solution at pH 5.6.
  - [image description] GATR-FTIR shows new C=O and O-H peaks after BVLD grafting, confirming covalent bonding.
  - [non-referenced_knowledge] Primary amines are more nucleophilic and reactive toward NHS-EDC than secondary amines.
  - [experimental result] XPS data show higher concentration of secondary amines than primary amines in PPAm, suggesting surface primary amines are accessible for grafting.
  - [deductive reasoning] Therefore, BVLD grafting occurs selectively on surface primary amines, preserving bulk secondary amines for NO loading.
### M3  Processing → Structure
- cause: Bulk loading of nitric oxide (NO) under high pressure using sodium methoxide solution
- effect: Formation of N-diazeniumdiolates (NONOates) within the bulk of PPAmF coating via reaction of NO with secondary amine groups
- experiment: NO loading under high pressure | High-pressure gas reaction | params: 0.5 M NaOMe solution, 75 psi NO gas, 3 days reaction time | result: Successful formation of diazeniumdiolates confirmed by GATR-FTIR and XPS
  - [experimental result] PPAmF coating contains abundant secondary amine groups, as confirmed by XPS and derivatization analysis.
  - [experimental result] NO is loaded under high pressure in the presence of sodium methoxide, a strong base that deprotonates amines to enhance nucleophilicity.
  - [image description] GATR-FTIR shows characteristic peaks of NONOates (1735, 1610, 1480, 1386 cm⁻¹) after NO loading.
  - [referenced knowledge] Secondary amines react with NO to form diazeniumdiolates (R2N-N(O)=NO⁻), a known chemical pathway.
  - [deductive reasoning] Thus, the processing step of high-pressure NO loading directly creates NONOate functional groups in the bulk of the coating.
### M4  Structure → Properties
- cause: Multilayered PPAmF structure with surface-grafted BVLD and bulk-loaded NONOates
- effect: Simultaneous anti-platelet (via NO release) and anti-coagulant (via BVLD inhibition of thrombin) biological properties
- experiment: Thrombin activity assay | Enzymatic activity measurement | params: Incubation with human thrombin (2 μg/mL), detection of cleaved substrate S2238 at 405 nm | result: BVLD-PPAmF and BVLD/NO-PPAmF show significantly lower thrombin activity than controls
  - [experimental result] BVLD is covalently grafted onto surface primary amines of PPAmF.
  - [experimental result] NO is stored as NONOates in the bulk via reaction with secondary amines.
  - [referenced knowledge] BVLD inhibits thrombin, preventing fibrinogen activation and fibrin network formation.
  - [referenced knowledge] NO diffuses and activates soluble guanylyl cyclase in platelets, increasing cGMP and suppressing activation.
  - [non-referenced_knowledge] Thrombosis requires both platelet activation and fibrin formation; dual inhibition is more effective than single-agent strategies.
  - [deductive reasoning] Thus, the layered structure enables synergistic anti-platelet and anti-coagulant properties.
### M5  Structure → Properties
- cause: Presence of diazeniumdiolates (NONOates) in the PPAmF bulk and hydrophobic C-F barrier layers
- effect: Sustained NO release over 8 hours with reduced burst release compared to single-layer PPAm
- experiment: NO release measurement | Chemiluminescence NO analyzer | params: PBS at pH 7.4, 37°C, NO detected until <1 ppb | result: PPAmF/NO releases NO for >8 hours; single-layer PPAm/NO releases for only ~1 hour
  - [experimental result] NO is stored as diazeniumdiolates (NONOates) in the PPAmF coating bulk.
  - [referenced knowledge] NONOates release NO via hydrolysis, which is accelerated by water exposure.
  - [experimental result] Single-layer PPAm (hydrophilic) releases NO rapidly (<1 h) due to easy water penetration.
  - [experimental result] PPAmF composite has alternating hydrophobic C-F layers that limit water diffusion into the coating.
  - [non-referenced_knowledge] Hydrophobic barriers reduce hydrolysis rate of NONOates, extending NO release to >8 hours.
  - [deductive reasoning] Therefore, the layered structure directly modulates the kinetics of NO release by controlling water access.
### M6  Structure → Performance
- cause: Dual-functional structure with surface BVLD and bulk NO storage in PPAmF coating
- effect: Highly endothelium-mimetic thromboresistant performance in ex vivo rabbit AV shunt model with 90.4% blood flow retention and minimal thrombus
- experiment: Ex vivo blood circulation assay | Arteriovenous shunt model | params: New Zealand white rabbit, 2 h circulation, no systemic anticoagulation, 316L SS foils with coatings | result: BVLD/NO-PPAmF shows 3.3±1.2% occlusion and 1.7±1.2 mg thrombus weight, with 90.4±4.2% blood flow retention
  - [experimental result] The PPAmF coating has surface BVLD that inhibits thrombin and prevents fibrin formation.
  - [experimental result] The coating has bulk NONOates that release NO to suppress platelet activation via cGMP.
  - [non-referenced_knowledge] Thrombosis requires both platelet activation and fibrin formation, as shown in vivo.
  - [experimental result] Single-function coatings (BVLD-only or NO-only) reduce thrombosis but not as effectively as dual-function.
  - [experimental result] In ex vivo rabbit AV shunt, BVLD/NO-PPAmF achieves 90.4% blood flow retention and minimal thrombus, matching endothelial function.
  - [deductive reasoning] Thus, the structural integration of dual functionalities enables endothelium-mimetic performance.
### M7  Properties → Performance
- cause: Sustained NO release (>8 h) and high BVLD bioactivity
- effect: Significantly reduced platelet adhesion, fibrinogen adsorption/activation, and thrombus formation in vivo
- experiment: Platelet adhesion assay | SEM quantification after PRP incubation | params: 30 min incubation in PRP, SEM imaging, platelet count and activation rate analysis | result: BVLD/NO-PPAmF shows 2.1-fold reduction in platelet adhesion vs. BVLD-PPAmF and 32.5-fold vs. NO-PPAmF
  - [experimental result] BVLD/NO-PPAmF coating releases NO for over 8 hours, maintaining therapeutic concentration.
  - [experimental result] GATR-FTIR and thrombin assay confirm BVLD retains bioactivity after grafting.
  - [experimental result] Platelet adhesion is reduced 2.1-fold compared to BVLD-only and 32.5-fold compared to NO-only.
  - [experimental result] Fibrinogen adsorption and activation are significantly reduced only when BVLD is present.
  - [non-referenced_knowledge] Sustained NO release continuously inhibits platelets, while BVLD continuously inhibits thrombin.
  - [deductive reasoning] This dual, sustained inhibition results in minimal thrombus formation and high blood flow retention.
