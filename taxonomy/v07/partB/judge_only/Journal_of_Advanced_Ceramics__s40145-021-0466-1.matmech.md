# MatMech content for Journal_of_Advanced_Ceramics/s40145-021-0466-1 (judge only; not shown to staff)
- material: nitrogen-doped carbon sphere (NPC-1000)  elements: ['C', 'H', 'O', 'N', 'Zn']  category: ['Nanomaterial', 'Ceramic']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: carbonization of biomass carbon spheres mixed with urea and zinc chloride in N₂ atmosphere at 1000 °C for 2 h
- **Structure**: highly porous microstructure with abundant fine pores (<1 nm) and medium-sized pores (~1–10 nm) in microflakes
- **Properties**: electron transfer number–electrochemical property, Tafel slope–electrochemical property, onset potential–electrochemical property, half-wave potential–electrochemical property
- **Performance**: superior oxygen reduction reaction (ORR) performance comparable to or exceeding Pt/C electrocatalyst, with better long-term stability and methanol tolerance
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: carbonization of biomass carbon spheres mixed with urea and zinc chloride in N₂ atmosphere at 1000 °C for 2 h
- effect: highly porous microstructure with abundant fine pores (<1 nm) and medium-sized pores (~1–10 nm) in microflakes
- experiment: BET surface area and pore size distribution analysis | BET gas adsorption/desorption isotherms, NLDFT model | params: NPC-1000 sample; nitrogen adsorption at 77 K; pore size range analyzed from 0.35 nm to 100 nm | result: BET specific surface area of 1786.41 m²·g⁻¹; significant increase in fine pores (<1 nm) and medium-sized pores (~1–10 nm) compared to NPC-800 and NPC-900; NC-1000 (without ZnCl₂) showed much lower pore volume in these ranges
  - [non-referenced_knowledge] Zinc chloride is added as a porogenic agent and melts at ~290 °C during carbonization.
  - [non-referenced_knowledge] Above 900 °C, molten zinc chloride evaporates completely, leaving behind voids in the carbon matrix.
  - [experimental result] BET analysis shows NPC-1000 has the highest specific surface area (1786.41 m²·g⁻¹) and largest volume of fine and medium-sized pores among all samples.
  - [image description] TEM and SEM images confirm the presence of microflakes on NPC-1000 surfaces, which are sparse in lower-temperature samples.
  - [experimental result] NC-1000 (without ZnCl₂) has significantly lower pore volume and surface area, proving ZnCl₂ is responsible for pore generation.
  - [deductive reasoning] Thus, carbonization at 1000 °C with ZnCl₂ creates a highly porous structure with abundant fine and medium pores in microflakes.
### M2  Structure → Performance
- cause: highly porous microstructure with abundant fine pores (<1 nm) and medium-sized pores (~1–10 nm) in microflakes
- effect: superior oxygen reduction reaction (ORR) performance comparable to or exceeding Pt/C electrocatalyst, with better long-term stability and methanol tolerance
- experiment: Rotating ring-disk electrode (RRDE) and Koutecky-Levich analysis | RRDE, K–L plots from LSV | params: Disk current (I_d), ring current (I_r), rotation rates from 225 to 2025 rpm; ring potential fixed at 0.3 V vs. Ag/AgCl | result: NPC-1000 has electron transfer number (n) of 3.6–4.0 (RRDE) and 4.0–4.2 (K–L), indicating dominant four-electron pathway; NPC-800 and NPC-900 show n=1.6–2.2, indicating two-electron pathway; Tafel slope of NPC-1000 is 64.9 mV/dec, lower than Pt/C (68.5 mV/dec).
  - [experimental result] NPC-1000 has the lowest pyridinic and graphitic nitrogen content but the highest ORR performance.
  - [experimental result] RRDE and K–L analysis show NPC-1000 has n≈4.0, indicating dominant four-electron reduction, while NPC-800/900 have n≈2.0, indicating two-electron pathway.
  - [image description] The structure of NPC-1000 contains abundant fine and medium pores in microflakes, as confirmed by BET and TEM.
  - [experimental result] Molecular dynamics simulations show peroxide ions confined in pores of 1–10 nm collide more frequently with pore walls, increasing reaction probability.
  - [non-referenced_knowledge] Peroxide (HO₂⁻) is an intermediate in the two-electron ORR pathway and can be further reduced to OH⁻ via a second two-electron step (Reaction 3).
  - [deductive reasoning] Confinement in nanopores increases the residence time and collision frequency of HO₂⁻ with active sites, favoring Reaction 3 over disproportionation (Reaction 4).
  - [deductive reasoning] Thus, the porous structure enables the space confinement effect to promote complete four-electron ORR despite low active site density.
