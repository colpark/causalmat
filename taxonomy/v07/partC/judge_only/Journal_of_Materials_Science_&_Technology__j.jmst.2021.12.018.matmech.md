# MatMech content for Journal_of_Materials_Science_&_Technology/j.jmst.2021.12.018 (judge only; not shown to staff)
- material: S-doped g-C₃N₄ / g-C₃N₄  elements: ['C', 'H', 'N', 'S']  category: ['Nanomaterial', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Liquid sulfur-mediated hydrothermal treatment followed by high-temperature pyrolysis under nitrogen atmosphere
- **Structure**: Isotype step-scheme heterojunction with sulfur-doped and sulfur-free active sites; micro/mesoporous lamellar morphology; increased interlayer interaction and reduced crystallinity
- **Properties**: Photocatalytic H₂ evolution rate–photocatalytic property; apparent quantum efficiency–photocatalytic property; charge carrier separation efficiency–electronic property; light absorption range–optical property
- **Performance**: Photocatalytic H₂ evolution rate of 5548.1 μmol g⁻¹ h⁻¹ under visible light irradiation with robust durability over six cycles
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Liquid sulfur-mediated hydrothermal treatment followed by high-temperature pyrolysis under nitrogen atmosphere
- effect: Formation of a sulfur-doped g-C₃N₄ / g-C₃N₄ isotype step-scheme heterojunction with micro/mesoporous lamellar morphology, increased interlayer interaction, and reduced crystallinity
- experiment: Synthesis of S-g-C₃N₄-E | Hydrothermal treatment and pyrolysis | params: 0.4 g g-C₃N₄-E + 2.8 g sulfur powder in 50 mL water, 180°C for 12 h, then pyrolysis at 520°C for 2 h under N₂ | result: Successful formation of sulfur-doped porous g-C₃N₄ with enhanced surface area and porosity
  - [experimental result] Liquid sulfur is introduced via hydrothermal treatment at 180°C, enabling full contact with exfoliated g-C₃N₄-E.
  - [non-referenced_knowledge] Sulfur vapor generated during subsequent pyrolysis at 520°C causes self-gas foaming, creating abundant pores.
  - [experimental result] XRD shows broadened (002) peak and reduced intensity in S-g-C₃N₄-E, indicating decreased crystallinity and enhanced interlayer interaction.
  - [image description] HRTEM and FESEM confirm lamellar morphology with uniform size and porosity.
  - [image description] N₂ adsorption-desorption reveals Type II isotherm with H4 hysteresis, confirming micro/mesoporous structure.
  - [deductive reasoning] Thus, liquid sulfur mediation and pyrolysis jointly create a porous, doped, low-crystallinity structure enabling S-scheme heterojunction formation.
### M2  Structure → Properties
- cause: Isotype step-scheme heterojunction with sulfur-doped and sulfur-free active sites; micro/mesoporous lamellar morphology
- effect: Enhanced charge carrier separation efficiency, prolonged carrier lifetime, increased light absorption range, and higher photocurrent density
- experiment: Photocurrent response and EIS measurements | Transient photocurrent response (TPR) and Electrochemical impedance spectroscopy (EIS) | params: 3-electrode cell with S-g-C₃N₄-E, 0.5 M Na₂SO₄ electrolyte, 10 W Xe lamp illumination | result: S-g-C₃N₄-E exhibits highest photocurrent density and smallest EIS semicircle among all samples
  - [experimental result] XPS and EDX confirm uniform S-doping and coexistence of S-doped and S-free sites within g-C₃N₄ structure.
  - [experimental result] UPS and Mott-Schottky plots show higher Fermi level and CB position in S-free g-C₃N₄ than S-doped regions, indicating R-type and O-type domains.
  - [referenced knowledge] Zeta potential shows opposite surface charges between S-doped and S-free sites, promoting interfacial electrostatic attraction.
  - [deductive reasoning] Internal electric field forms at the interface, facilitating recombination of electrons from O-type and holes from R-type domains.
  - [image description] PL spectra show quenched emission for S-g-C₃N₄-E, indicating suppressed recombination of useful carriers.
  - [image description] Fluorescence decay reveals longer carrier lifetimes (6.826 ns and 1.749 ns) for S-g-C₃N₄-E compared to others.
  - [experimental result] TPR and EIS show higher photocurrent and lower charge transfer resistance, confirming improved charge separation and mobility.
  - [deductive reasoning] Thus, the isotype S-scheme heterojunction and porous structure synergistically enhance charge separation, lifetime, and mobility.
### M3  Structure → Properties
- cause: Increased specific surface area (173.53 m²/g) and micro/mesoporous structure
- effect: Higher density of photocatalytic active sites and improved mass transfer of reactants
- experiment: BET surface area and pore size distribution measurement | N₂ adsorption-desorption isotherm | params: ASAP 2020 analyzer, BJH method applied to adsorption branch | result: S-g-C₃N₄-E has surface area of 173.53 m²/g and pore volume of 0.888 cm³/g, significantly higher than g-C₃N₄-E (102.3 m²/g)
  - [non-referenced_knowledge] Pyrolysis of S@g-C₃N₄-E produces sulfur vapor that causes self-gas foaming, creating pores.
  - [experimental result] BET analysis confirms S-g-C₃N₄-E has 173.53 m²/g surface area, much higher than g-C₃N₄-E (102.3 m²/g).
  - [image description] BJH pore size distribution shows dominant mesopores (2–50 nm) and micropores (<2 nm).
  - [non-referenced_knowledge] High surface area provides more active sites for H₂O adsorption and H₂ evolution reaction.
  - [non-referenced_knowledge] Pores facilitate diffusion of reactants and products, reducing mass transfer limitations.
  - [deductive reasoning] Thus, porosity and high surface area directly enhance photocatalytic activity by increasing active site density and reaction kinetics.
### M4  Structure → Properties
- cause: Sulfur doping into g-C₃N₄ lattice
- effect: Extended visible light absorption range and increased optical absorption strength
- experiment: UV-Vis diffuse reflectance spectroscopy | UV-VIS diffuse reflectance spectra | params: Carry5000 spectrophotometer, 300–700 nm range | result: S-g-C₃N₄-E shows broader absorption edge and higher absorption intensity than g-C₃N₄ and g-C₃N₄-E
  - [non-referenced_knowledge] S atoms replace N or C atoms in the g-C₃N₄ lattice due to similar size and electronegativity differences.
  - [experimental result] XPS S 2p spectrum shows C-S-C bonding at 164.7 eV, confirming successful incorporation into the framework.
  - [image description] UV-Vis DRS shows S-g-C₃N₄-E has absorption edge extended beyond g-C₃N₄-E, with estimated band gap of 2.85 eV vs. 2.75 eV.
  - [deductive reasoning] The red-shifted absorption edge indicates enhanced utilization of visible photons.
  - [image description] Higher absorption intensity suggests increased photon-to-electron conversion efficiency.
  - [deductive reasoning] Thus, S-doping tunes the band structure to improve optical absorption for photocatalysis.
### M5  Properties → Performance
- cause: Enhanced charge carrier separation efficiency, prolonged carrier lifetime, extended light absorption, and high surface area
- effect: Photocatalytic H₂ evolution rate of 5548.1 μmol g⁻¹ h⁻¹ with robust durability over six cycles
- experiment: Photocatalytic H₂ evolution test | Photoreactor with Xe lamp and GC detection | params: 20 mg catalyst, 3 wt% Pt co-catalyst, 300 W Xe lamp (λ ≥ 420 nm), TEOA as sacrificial agent | result: S-g-C₃N₄-E achieves 5548.1 μmol g⁻¹ h⁻¹ H₂ evolution rate, 49× higher than g-C₃N₄-E (111.5 μmol g⁻¹ h⁻¹)
  - [experimental result] S-g-C₃N₄-E exhibits highest H₂ evolution rate (5548.1 μmol g⁻¹ h⁻¹) among all samples.
  - [experimental result] This rate is 49 times higher than g-C₃N₄-E (111.5 μmol g⁻¹ h⁻¹), which already benefits from exfoliation.
  - [experimental result] TPR, EIS, and PL show superior charge separation and reduced recombination in S-g-C₃N₄-E.
  - [experimental result] UV-Vis DRS and band gap analysis confirm enhanced visible light absorption.
  - [experimental result] BET confirms high surface area and porosity provide abundant active sites.
  - [experimental result] Six-cycle test shows negligible activity decay, indicating structural stability.
  - [deductive reasoning] Thus, the synergy of improved charge dynamics, optical response, and surface properties directly enables high performance and durability.
