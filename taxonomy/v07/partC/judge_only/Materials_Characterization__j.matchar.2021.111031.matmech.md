# MatMech content for Materials_Characterization/j.matchar.2021.111031 (judge only; not shown to staff)
- material: g-C₃N₄  elements: ['C', 'N']  category: ['Nanomaterial', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Ultrasonic exfoliation of bulk g-C₃N₄ in sulfuric acid aqueous solution, followed by centrifugation, washing, and heating at 200 °C
- **Structure**: Mesoporous two-dimensional nanosheets with higher specific surface area (55.41 m²/g), abundant mesopores (30–50 nm), and reduced layer thickness compared to bulk g-C₃N₄
- **Properties**: narrowed bandgap–optical property, lower charge transfer resistance–electrical property
- **Performance**: 3.3-fold enhancement in photocatalytic hydrogen evolution rate under visible light irradiation
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Ultrasonic exfoliation of bulk g-C₃N₄ in sulfuric acid aqueous solution, followed by centrifugation, washing, and heating at 200 °C
- effect: Mesoporous two-dimensional nanosheets with higher specific surface area (55.41 m²/g), abundant mesopores (30–50 nm), and reduced layer thickness compared to bulk g-C₃N₄
- experiment: FESEM and TEM imaging | FESEM, TEM | params: Imaging of BCN and CNS samples | result: BCN shows layered stacking; CNS exhibits thin 2D layers with 30–50 nm mesopores
  - [experimental result] Bulk g-C₃N₄ (BCN) was exfoliated using ultrasonic treatment in sulfuric acid solution.
  - [image description] FESEM and TEM images show that BCN has a layered-stacking structure, while CNS exhibits thin 2D layers with abundant mesopores (30–50 nm).
  - [non-referenced_knowledge] Reducing material dimensions increases surface area and exposes more reactive sites.
  - [deductive reasoning] Thus, ultrasonic exfoliation transforms bulk g-C₃N₄ into mesoporous 2D nanosheets with higher surface area and porosity.
### M2  Structure → Properties
- cause: Mesoporous two-dimensional nanosheets with higher specific surface area (55.41 m²/g), abundant mesopores (30–50 nm), and reduced layer thickness
- effect: Narrowed bandgap (2.51 eV vs. 2.68 eV) and lower charge transfer resistance
- experiment: UV-vis DRS and EIS measurements | UV-vis diffuse reflectance spectroscopy, Electrochemical impedance spectroscopy | params: Measurement of absorption edge and Nyquist plot radius for BCN and CNS | result: CNS shows redshifted absorption edge and smaller EIS semicircle radius than BCN
  - [experimental result] CNS exhibits a redshifted absorption edge compared to BCN in UV-vis DRS.
  - [experimental result] The bandgap of CNS is calculated to be 2.51 eV, narrower than BCN's 2.68 eV.
  - [experimental result] CNS shows a smaller EIS semicircle radius than BCN, indicating lower charge transfer resistance.
  - [non-referenced_knowledge] Reduced thickness and high surface area in 2D nanosheets improve charge carrier mobility.
  - [non-referenced_knowledge] Narrower bandgap allows absorption of more visible light photons.
  - [deductive reasoning] Thus, the mesoporous nanosheet structure leads to narrowed bandgap and reduced charge transfer resistance.
### M3  Structure → Properties
- cause: Mesoporous two-dimensional nanosheets with higher specific surface area (55.41 m²/g), abundant mesopores (30–50 nm), and reduced layer thickness
- effect: Improved light absorption capacity and enhanced mass transport
- experiment: Nitrogen adsorption-desorption isotherms | BET surface area and pore size analysis | params: Measurement of specific surface area and pore volume using ASAP 2460 | result: CNS has 55.41 m²/g surface area and 0.216 cm³/g pore volume, significantly higher than BCN (7.61 m²/g, 0.055 cm³/g)
  - [experimental result] CNS has a specific surface area of 55.41 m²/g and mesopore volume of 0.216 cm³/g, much higher than BCN.
  - [experimental result] Nitrogen adsorption-desorption isotherms show type IV behavior with H3 hysteresis, confirming mesoporous structure.
  - [non-referenced_knowledge] Mesopores promote multiple light scattering and reflection, increasing photon absorption.
  - [non-referenced_knowledge] High surface area provides more reactive sites for water reduction and hole scavenging.
  - [deductive reasoning] Thus, the mesoporous nanosheet structure enhances light absorption and mass transport.
### M4  Properties → Performance
- cause: Narrowed bandgap (2.51 eV), lower charge transfer resistance, and improved light absorption
- effect: 3.3-fold enhancement in photocatalytic hydrogen evolution rate (97.6 vs. 29.8 μmol g⁻¹ h⁻¹)
- experiment: Photocatalytic hydrogen evolution test | Gas chromatography under visible light (λ > 420 nm) | params: 50 mg catalyst, 90 mL water + 10 mL triethanolamine, 300 W Xe lamp | result: CNS produces 97.6 μmol g⁻¹ h⁻¹ H₂, 3.3 times higher than BCN (29.8 μmol g⁻¹ h⁻¹)
  - [experimental result] CNS has a narrower bandgap (2.51 eV) than BCN (2.68 eV), enabling better visible light absorption.
  - [experimental result] CNS shows lower charge transfer resistance, confirmed by smaller EIS semicircle radius.
  - [experimental result] Lower PL intensity in CNS indicates higher electron-hole separation efficiency.
  - [non-referenced_knowledge] Improved charge separation and broader light absorption increase the number of electrons available for H⁺ reduction.
  - [deductive reasoning] Thus, the enhanced optical and electrical properties lead to a 3.3-fold increase in H₂ evolution rate.
### M5  Structure → Performance
- cause: Mesoporous two-dimensional nanosheets with higher specific surface area (55.41 m²/g), abundant mesopores (30–50 nm), and reduced layer thickness
- effect: 3.3-fold enhancement in photocatalytic hydrogen evolution rate (97.6 vs. 29.8 μmol g⁻¹ h⁻¹)
- experiment: Photocatalytic hydrogen evolution test | Gas chromatography under visible light (λ > 420 nm) | params: 50 mg catalyst, 90 mL water + 10 mL triethanolamine, 300 W Xe lamp | result: CNS produces 97.6 μmol g⁻¹ h⁻¹ H₂, 3.3 times higher than BCN (29.8 μmol g⁻¹ h⁻¹)
  - [experimental result] CNS has higher specific surface area (55.41 m²/g) and abundant mesopores (30–50 nm) compared to BCN.
  - [non-referenced_knowledge] Mesopores facilitate multi-light scattering and enhance light harvesting.
  - [non-referenced_knowledge] High surface area exposes more active sites for H⁺ reduction.
  - [experimental result] CNS exhibits 3.3 times higher H₂ evolution rate than BCN.
  - [deductive reasoning] Thus, the structural features of CNS directly drive its superior photocatalytic performance.
