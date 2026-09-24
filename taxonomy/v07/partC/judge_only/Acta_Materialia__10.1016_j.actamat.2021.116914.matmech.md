# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116914 (judge only; not shown to staff)
- material: Ni-rich layered oxide (NLO) cathodes  elements: ['Ni', 'Co', 'Mn', 'Na', 'Fe', 'O']  category: ['Crystalline Material', 'Ceramic']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Co-precipitation method and calcination at 900°C for 12h under pure oxygen atmosphere
- **Structure**: Layered α-NaFeO2 structure with R3m space group, intergranular and intragranular cracks along (001) basal plane
- **Properties**: Voltage decay–electrochemical property, Capacity fading–electrochemical property
- **Performance**: Severe intergranular cracking in polycrystalline NLOs leads to fast voltage decay and capacity fading, while minor intragranular cracking in single-crystal NLOs improves cyclability and reversible capacity
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Co-precipitation method and calcination at 900°C for 12h under pure oxygen atmosphere
- effect: Layered α-NaFeO₂ structure with R3m space group, intergranular and intragranular cracks along (001) basal plane
- experiment: Synthesis of NLO materials | Coprecipitation and calcination | params: Ni:Co:Mn = 0.83:0.1:0.07; calcined at 900°C for 12h under O₂ atmosphere | result: Formation of single-crystal S83 particles (~5μm) with layered α-NaFeO₂ structure
  - [experimental result] N83 and S83 were synthesized via co-precipitation followed by calcination at different temperatures.
  - [image description] XRD patterns show layered α-NaFeO₂ structure with clear split of (018)/(110) peaks indicating high crystallinity in S83.
  - [non-referenced_knowledge] Higher calcination temperature increases Li/Ni disorder degree, leading to slight lattice shrinkage.
  - [referenced knowledge] Layered α-NaFeO₂ structure exhibits strong elastic anisotropy during cycling, particularly along (001) direction.
  - [deductive reasoning] Thus, processing conditions lead to layered α-NaFeO₂ structure with anisotropic mechanical properties that govern crack initiation along (001) basal plane.
### M2  Structure → Performance
- cause: Intergranular and intragranular cracks along (001) basal plane
- effect: Severe intergranular cracking in polycrystalline NLOs leads to fast voltage decay and capacity fading, while minor intragranular cracking in single-crystal NLOs improves cyclability and reversible capacity
- experiment: Cross-sectional SEM analysis of cycled particles | Field-emission scanning electron microscopy | params: Cycling between 2.8–4.5 V, up to 100 cycles | result: Polycrystalline N83 shows severe intergranular cracking while single-crystal S83 exhibits minor intragranular cracking
  - [image description] Cross-sectional SEM shows extensive intergranular cracking in N83 after 100 cycles, while S83 maintains structural integrity.
  - [experimental result] Intragranular cracks occur within primary particles but do not significantly degrade performance.
  - [non-referenced_knowledge] Intergranular cracking breaks connections between primary particles, reducing overall conductivity.
  - [referenced knowledge] Surface reconstruction and HF attack preferentially occur on nonpolar surfaces exposed by cracks.
  - [inductive reasoning] Therefore, intergranular cracking in polycrystalline NLOs accelerates voltage decay and capacity fading compared to single-crystal materials with minimal intragranular cracking.
### M3  Structure → Property
- cause: Layered α-NaFeO₂ structure with R3m space group
- effect: Voltage decay and capacity fading – electrochemical properties
- experiment: Galvanostatic charge-discharge testing | Electrochemical characterization | params: Rate of 0.1C between 2.8–4.3 V and 2.8–4.5 V | result: N83 shows higher initial capacity but faster voltage decay than S83
  - [experimental result] Initial discharge capacity of N83 (205 mAh/g) is higher than S83 (188 mAh/g), but voltage decays faster during cycling.
  - [image description] S83 material maintains higher average voltage over cycling due to better structural stability.
  - [non-referenced_knowledge] Layered structure enables high capacity but is prone to phase transformation and oxygen release during delithiation.
  - [referenced knowledge] Voltage decay correlates with structural degradation and Mn/Co dissolution from the layered phase.
  - [deductive reasoning] Therefore, the layered α-NaFeO₂ structure provides high initial capacity but contributes to voltage decay and capacity fading through structural degradation mechanisms.
### M4  Processing → Performance
- cause: Co-precipitation method and calcination at 900°C for 12h under pure oxygen atmosphere
- effect: Severe intergranular cracking in polycrystalline NLOs leads to fast voltage decay and capacity fading, while minor intragranular cracking in single-crystal NLOs improves cyclability and reversible capacity
- experiment: Comparison of polycrystalline and single-crystal NLOs | Electrochemical testing and SEM analysis | params: Cycling between 2.8–4.5 V for up to 100 cycles | result: Single-crystal S83 shows improved capacity retention (94.2% after 100 cycles) compared to polycrystalline N83
  - [image description] Single-crystal S83 retains particle integrity with minimal cracking, while polycrystalline N83 undergoes extensive intergranular fracture.
  - [experimental result] Higher calcination temperature for S83 increases cation mixing and surface reconstruction layer thickness.
  - [non-referenced_knowledge] Grain boundaries serve as preferential sites for crack initiation and electrolyte interaction.
  - [referenced knowledge] Single-crystal materials avoid intergranular cracking and associated TM dissolution, preserving electrochemical performance.
  - [inductive reasoning] Therefore, processing conditions that produce single-crystal morphology improve cycling stability by preventing intergranular cracking and subsequent degradation processes.
