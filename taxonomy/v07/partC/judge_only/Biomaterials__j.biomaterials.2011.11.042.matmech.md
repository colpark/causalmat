# MatMech content for Biomaterials/j.biomaterials.2011.11.042 (judge only; not shown to staff)
- material: Co-containing mesoporous bioactive glass (Co-MBG)  elements: ['Co', 'Ca', 'Si', 'O', 'P']  category: ['Ceramic', 'Nanomaterial', 'Biomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Preparation using co-templates of P123 and polyurethane sponges, followed by calcination at 700°C for 5 h, with substitution of Ca²⁺ by Co²⁺ ions (2% and 5% molar)
- **Structure**: Hierarchically porous structure with large pores (300–500 µm) and well-ordered mesopores (4.1–4.97 nm); decreased specific surface area and pore volume with increasing Co content
- **Properties**: VEGF secretion–biological property, HIF-1α expression–biological property, osteocalcin expression–biological property, sustained ion release–chemical property, antibacterial property–biological property
- **Performance**: Enhanced angiogenesis and osteogenesis in bone tissue engineering, supported BMSC attachment and proliferation, sustained antibiotic release with effective anti-bacterial activity against E. coli
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Preparation using co-templates of P123 and polyurethane sponges, with substitution of Ca²⁺ by Co²⁺ ions (2% and 5% molar)
- effect: Hierarchically porous structure with large pores (300–500 µm) and well-ordered mesopores (4.1–4.97 nm); decreased specific surface area and pore volume with increasing Co content
- experiment: Characterization of Co-MBG scaffolds | SEM, TEM, XRD, BET, BJH | params: Co content: 0%, 2%, 5%; calcination at 700°C for 5 h; P123 and polyurethane sponge templates | result: Co-MBG scaffolds maintained ordered mesopores (4.1–4.97 nm) and large pores (300–500 µm); specific surface area decreased from 290 to 127 m²/g and pore volume from 0.30 to 0.15 cm³/g with increasing Co content
  - [experimental result] Co-MBG scaffolds were prepared using P123 and polyurethane sponge templates to generate meso- and macropores.
  - [image description] TEM and SEM images confirm the presence of well-ordered mesopores (~4.5–5 nm) and large pores (300–500 µm) in all Co-MBG scaffolds.
  - [experimental result] BET/BJH analysis shows specific surface area and pore volume decrease with increasing Co content (290 → 127 m²/g; 0.30 → 0.15 cm³/g).
  - [non-referenced_knowledge] Replacing Ca²⁺ with Co²⁺ may disrupt the self-assembly of P123 micelles during synthesis, leading to less optimal mesopore ordering.
  - [deductive reasoning] Thus, Co²⁺ incorporation modifies the mesoporous structure without destroying its hierarchical architecture.
### M2  Processing → Properties
- cause: Controlled incorporation of Co²⁺ ions (2% and 5%) into MBG scaffolds via co-template synthesis and calcination
- effect: Enhanced VEGF secretion, HIF-1α expression, and osteocalcin gene expression in BMSCs; sustained Co²⁺ ion release
- experiment: Ion release in DMEM and cellular response assays | ICP-AES, ELISA, Western blot, RT-qPCR | params: Scaffolds soaked in DMEM for 1, 3, 7 days; BMSCs cultured on scaffolds for 7 days; Co²⁺ concentrations: 0%, 2%, 5% | result: Co²⁺ release increased with Co content; 2% and 5% Co-MBG significantly increased VEGF secretion, HIF-1α protein expression, and VEGF/OCN mRNA levels compared to pure MBG
  - [experimental result] Co²⁺ ions are incorporated into MBG scaffolds during synthesis by substituting Ca²⁺.
  - [experimental result] ICP-AES shows controlled release of Co²⁺ into DMEM over 7 days, with higher release from 5Co-MBG than 2Co-MBG.
  - [referenced knowledge] Co²⁺ is known to inactivate HIF-prolyl hydroxylases, preventing HIF-1α degradation under normoxia.
  - [experimental result] Western blot shows increased HIF-1α protein levels in BMSCs on Co-MBG scaffolds, correlating with Co content.
  - [experimental result] ELISA and RT-qPCR show elevated VEGF protein and mRNA levels, and increased OCN expression, indicating activation of hypoxia-driven pathways.
  - [deductive reasoning] Thus, Co²⁺ release induces a hypoxia-mimicking cascade that enhances angiogenic and osteogenic gene expression.
### M3  Structure → Properties
- cause: Well-ordered mesoporous structure with high surface area (127–290 m²/g) and nanopore size (4.1–4.97 nm)
- effect: Sustained release of Co²⁺ ions and efficient loading/release of ampicillin, enhancing biological responses (VEGF, HIF-1α) and antibacterial activity
- experiment: Drug loading and release assays | UV spectroscopy, antibacterial colony counting | params: Ampicillin loaded onto 2Co-MBG scaffolds; release measured over 72 h; antibacterial test with E. coli | result: 2Co-MBG scaffolds loaded 5 mg/mL ampicillin and released it sustainably over 72 h; antibacterial efficacy was significantly higher than controls
  - [experimental result] Co-MBG scaffolds have well-ordered mesopores (4.1–4.97 nm) and high surface area (127–290 m²/g), as confirmed by BET and TEM.
  - [referenced knowledge] Mesopores are known to adsorb and slowly release small molecules like antibiotics and metal ions.
  - [experimental result] Ampicillin loading and release profiles show sustained delivery over 72 h from Co-MBG scaffolds.
  - [non-referenced_knowledge] Co²⁺ release kinetics are proportional to mesopore accessibility and surface area, which decrease with higher Co content but remain effective.
  - [deductive reasoning] Thus, the mesoporous structure enables both sustained Co²⁺ release (inducing HIF-1α/VEGF) and antibiotic delivery (antibacterial effect).
### M4  Properties → Performance
- cause: Enhanced VEGF secretion, HIF-1α expression, and sustained ampicillin release
- effect: Improved angiogenesis, osteogenesis, and anti-bacterial activity in bone tissue engineering applications
- experiment: BMSC proliferation, ALP activity, and antibacterial efficacy tests | MTT assay, ALP assay, E. coli colony counting | params: BMSCs cultured on scaffolds for 1–7 days; ampicillin-loaded scaffolds exposed to E. coli for 1–7 days | result: Co-MBG scaffolds supported BMSC attachment and proliferation; ALP activity unchanged; VEGF/HIF-1α increased; ampicillin-loaded scaffolds reduced E. coli colonies by >90%
  - [experimental result] Co-MBG scaffolds induce high VEGF secretion and HIF-1α expression in BMSCs.
  - [referenced knowledge] VEGF promotes angiogenesis, which improves oxygen and nutrient delivery to regenerating bone tissue.
  - [experimental result] Ampicillin is sustainably released from mesopores, reducing E. coli colony formation by >90%.
  - [referenced knowledge] Infection (osteomyelitis) is a major cause of bone graft failure; local antibiotic delivery prevents this.
  - [deductive reasoning] Thus, the combined biological and antibacterial properties enable scaffolds to support both bone formation and infection resistance.
