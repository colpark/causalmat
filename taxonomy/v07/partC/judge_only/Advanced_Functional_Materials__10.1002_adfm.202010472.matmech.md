# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202010472 (judge only; not shown to staff)
- material: CoSAs-NGST (Cobalt single-atom anchored on nitrogen-doped graphene-sheet@tube)  elements: ['Co', 'C', 'N', 'Zn', 'H']  category: ['Nanomaterial', 'Composite Material', 'Ceramic']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Derived from Co, Zn-coordinated zeolitic imidazolate framework (CoZn-ZIF) in the presence of dicyandiamide
- **Structure**: Hybrid structure with bamboo-like graphene tube and sheet, CoN4-rich graphene tube
- **Properties**: ORR/OER bifunctional catalytic performance–electrochemical property, charge–discharge voltage drop–electrochemical property
- **Performance**: Superb ORR/OER bifunctional catalytic performance, notably small charge–discharge voltage drop of 0.93 V in rechargeable zinc–air battery
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Derived from Co, Zn-coordinated zeolitic imidazolate framework (CoZn-ZIF) in the presence of dicyandiamide
- effect: Formation of hybrid structure with bamboo-like graphene tube and sheet, CoN4-rich graphene tube
- experiment: Thermogravimetric and DSC analysis | TG-DSC | params: Heating under N₂ atmosphere, temperature range 25–900°C | result: Four-stage decomposition identified; dicyandiamide-induced condensation at 500–750°C leads to nanotube growth via NH₃ and C₃N₄ intermediates
  - [experimental result] Thermal analysis showed condensation of tri-s-triazine molecules into g-C₃N₄ at ~500°C.
  - [non-referenced_knowledge] Released NH₃ provides nitrogen source and micro-atmosphere for in-situ carbonization.
  - [image description] Figure shows multiwalled graphene tubes rooted on sheets with isolated Co atoms visible as bright dots.
  - [non-referenced_knowledge] Micromolecules from dicyandiamide interact with ZIF framework to disassemble bulk morphology into low-dimensional hybrid.
  - [deductive reasoning] Thus, pyrolysis of CoZn-ZIF with dicyandiamide leads to hybrid structure with enhanced CoN4-rich graphene tube formation.
### M2  Structure → Property
- cause: Hybrid structure with bamboo-like graphene tube and sheet, CoN4-rich graphene tube
- effect: Enhanced ORR/OER bifunctional electrocatalytic activity
- experiment: Electrochemical measurements | LSV, Tafel, RRDE | params: O₂/N₂-saturated 0.1 M KOH, rotating disk electrode | result: CoSAs-NGST exhibits onset potential of 0.99 V vs RHE, half-wave potential of 0.89 V, Tafel slope of 65 mV/dec, and electron transfer number ≈4
  - [experimental result] EELS data confirms higher concentration of pyridinic nitrogen and CoN4 coordination in tube structure.
  - [image description] HAADF-STEM shows uniform distribution of isolated Co atoms across both tube and sheet regions.
  - [non-referenced_knowledge] Curved graphene tubes elevate p-band center, reducing oxygen adsorption barrier.
  - [non-referenced_knowledge] DFT modeling reveals distinct rate-determining steps between CoN4-tube and CoN4-sheet, enabling synergistic bifunctionality.
  - [deductive reasoning] Therefore, hierarchical structure with enriched CoN4 sites enables superior ORR/OER kinetics via curvature effects and bifunctional synergy.
### M3  Property → Performance
- cause: ORR/OER bifunctional catalytic performance
- effect: Notably small charge–discharge voltage drop of 0.93 V in rechargeable zinc–air battery
- experiment: Zinc–air battery testing | Galvanostatic cycling | params: Current density: 5 mA/cm², cycle time: 20 min/cycle | result: Voltage gap remains stable at 0.93 V after 133 h (399 cycles), outperforming Pt/C + RuO₂ (1.57 V gap after 70 h)
  - [experimental result] Electrochemical impedance spectroscopy shows CoSAs-NGST has lower Rct (24.9 Ω) than CoSAs-NPC (31.2 Ω).
  - [image description] Battery demonstrates stable cycling for 133 h (399 cycles) with only 0.93 V voltage gap.
  - [non-referenced_knowledge] High surface area and mesoporous architecture enhance mass transport and durability.
  - [referenced knowledge] Superior bifunctional activity directly correlates with reduced polarization losses in practical devices.
  - [inductive reasoning] Therefore, the low ORR/OER overpotential and high stability of CoSAs-NGST lead to excellent battery performance with minimal voltage degradation.
