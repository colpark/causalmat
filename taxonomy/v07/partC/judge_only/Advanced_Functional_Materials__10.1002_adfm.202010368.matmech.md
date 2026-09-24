# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202010368 (judge only; not shown to staff)
- material: Perovskite solar cells (PSCs)  elements: ['Pb', 'I', 'Zn', 'C', 'H', 'O', 'N']  category: ['Crystalline Material', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Formic acid-functionalized 2D metal–organic frameworks (MOFs) as the terminated agent
- **Structure**: MOFs distributed at the grain boundaries, regular morphology, lower defect density
- **Properties**: power conversion efficiency–electrical property, charge recombination–electrical property, charge extraction–electrical property
- **Performance**: Maintained 88% and 81% of initial efficiency after 750h heating at 85°C and 1000h storage in ambient environment
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Formic acid-functionalized 2D metal–organic frameworks (MOFs) as the terminated agent
- effect: MOFs distributed at the grain boundaries, regular morphology, lower defect density
- experiment: Perovskite film synthesis with Zn-cbpp modification | Thin-film deposition with spin coating and annealing | params: Zn-cbpp added to precursor solution (0–3 mg/mL), annealed at 100°C for 60 min | result: Modified films show reduced pinholes, cracks, and PbI₂ accumulation at grain boundaries
  - [experimental result] Zn-cbpp contains abundant nitrogen atoms and carboxylate groups that coordinate with Pb²⁺ ions.
  - [image description] SEM and TEM images show reduced pinholes and crack formation in Zn-cbpp-modified films.
  - [experimental result] XPS shows binding energy shift of Pb 4f peaks, indicating stronger bonding between Zn-cbpp and Pb²⁺ ions.
  - [referenced knowledge] Excess PbI₂ can lead to instability and charge recombination in PSCs.
  - [non-referenced_knowledge] Passivation of grain boundaries lowers defect density and improves film quality.
  - [deductive reasoning] Thus, Zn-cbpp acts as a stable terminated layer at grain boundaries, enhancing structural integrity and crystallinity.
### M2  Structure → Property
- cause: MOFs distributed at the grain boundaries, regular morphology, lower defect density
- effect: Power conversion efficiency increased from 19.59% to 21.28%, reduced charge recombination, faster charge extraction
- experiment: Photovoltaic device characterization | J-V measurement and IPCE analysis | params: Reverse scan direction, AM 1.5G illumination, active area = 0.06 cm² | result: PCE increased from 19.59% to 21.28%, with higher Voc and FF
  - [image description] SEM and AFM data confirm smoother surface and fewer grain boundary defects after Zn-cbpp modification.
  - [experimental result] C-AFM shows reduced current dead zones at grain boundaries in Zn-cbpp-modified films.
  - [experimental result] TRPL lifetime increases from 5.82 ns to 9.55 ns, indicating reduced recombination rate.
  - [referenced knowledge] Lower defect density correlates with reduced trap-assisted recombination and higher photovoltaic efficiency.
  - [non-referenced_knowledge] Defect states act as recombination centers and hinder charge transport in semiconductors.
  - [inductive reasoning] Therefore, grain boundary passivation via Zn-cbpp leads to reduced recombination and faster charge extraction, improving PCE.
### M3  Property → Performance
- cause: Power conversion efficiency increased from 19.59% to 21.28%, reduced charge recombination, faster charge extraction
- effect: Maintained 88% and 81% of initial efficiency after 750h heating at 85°C and 1000h storage in ambient environment
- experiment: Environmental aging tests | Thermal and humidity stability testing | params: Unencapsulated devices aged at 85°C/N₂ atmosphere and ambient conditions (25°C, ~40% RH) | result: Zn-cbpp-modified PSCs retain 88% and 81% of initial efficiency after 750 h and 1000 h, respectively
  - [experimental result] Zn-cbpp increases water contact angle of perovskite films, suggesting hydrophobic effect.
  - [experimental result] XRD and UV-vis data after aging show less PbI₂ formation in Zn-cbpp-modified films.
  - [referenced knowledge] Defects catalyze moisture-induced decomposition of perovskite materials.
  - [non-referenced_knowledge] Passivated grain boundaries prevent water molecule intrusion and phase transition under thermal stress.
  - [deductive reasoning] Thus, Zn-cbpp-enhanced defect passivation and barrier effect improve both thermal and moisture stability of PSCs.
