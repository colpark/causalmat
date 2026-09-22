# MatMech content for Advanced_Energy_Materials/aenm.202102982 (judge only; not shown to staff)
- material: Zn (zinc)  elements: ['Zn', 'N', 'H', 'O', 'S']  category: ['Metals and Alloys', 'Coatings and Thin Films', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Addition of ammonium acetate (NH₄OAc) additive to aqueous zinc sulfate (ZnSO₄) electrolyte
- **Structure**: Dynamic electrostatic shielding layer around Zn protuberances and suppressed formation of zinc hydroxide sulfate hydrate (ZHSH) by-products
- **Properties**: Coulombic efficiency–electrochemical property, cycling stability–electrochemical property, corrosion resistance–electrochemical property
- **Performance**: Long-term stable cycling of Zn anodes for 3500 h at 1 mA cm⁻² and cumulative areal capacity of 5000 mAh cm⁻² at 10 mA cm⁻²; enhanced full-cell performance with Od-NVO cathode
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Addition of ammonium acetate (NH₄OAc) additive to aqueous zinc sulfate (ZnSO₄) electrolyte
- effect: Formation of a dynamic electrostatic shielding layer around Zn protuberances and suppression of zinc hydroxide sulfate hydrate (ZHSH) precipitation
- experiment: Binding energy calculation and cycling performance of Zn//Zn symmetric cells | Density functional theory (DFT) computation and electrochemical cycling | params: Comparison of NH₄⁺ vs Zn²⁺ binding energy on Zn (101); cycling at 0.5 mA cm⁻² and 0.5 mAh cm⁻² | result: NH₄⁺ has higher binding energy (-2.10 eV) than Zn²⁺ (-0.99 eV); Zn//Zn cell with NH₄⁺ shows improved cycling stability (970 h vs 230 h)
  - [experimental result] NH₄⁺ has a higher binding energy (-2.10 eV) to Zn (101) than Zn²⁺ (-0.99 eV), indicating preferential adsorption.
  - [image description] Figure 1b and 1a show that preferential NH₄⁺ adsorption induces an electrostatic shielding layer around Zn protuberances.
  - [referenced knowledge] Adding competing cations is a known method to suppress dendrite growth by homogenizing ion flux.
  - [non-referenced_knowledge] OAc⁻ hydrolyzes with H⁺ to form HOAc, buffering interfacial pH and preventing local alkalinity that causes ZHSH precipitation.
  - [experimental result] XRD and SEM confirm absence of ZHSH on Zn anodes cycled in NH₄OAc electrolyte, while abundant ZHSH forms in additive-free electrolyte.
  - [deductive reasoning] Thus, NH₄⁺ and OAc⁻ synergistically create a dynamic, self-regulated interface that stabilizes Zn deposition morphology and suppresses corrosion by-products.
### M2  Structure → Properties
- cause: Dynamic electrostatic shielding layer around Zn protuberances and suppressed formation of ZHSH by-products
- effect: High Coulombic efficiency (~99.7%), enhanced cycling stability (3500 h), and improved corrosion resistance
- experiment: Coulombic efficiency measurement in Zn//Cu asymmetric cells and long-term cycling of Zn//Zn cells | Electrochemical testing | params: 1 mA cm⁻², 0.5 mAh cm⁻²; cycling up to 3500 h | result: CE reaches ~99.7% over 1800 cycles in NH₄OAc electrolyte vs. ~98.1% in blank; Zn//Zn cells cycle for 3500 h without failure
  - [image description] The self-regulated interface prevents dendritic Zn growth, as confirmed by SEM and operando microscopy.
  - [experimental result] Absence of ZHSH peaks in XRD indicates suppression of corrosion by-products.
  - [non-referenced_knowledge] Corrosion and hydrogen evolution consume active Zn and increase impedance, lowering CE.
  - [deductive reasoning] With suppressed dendrites and by-products, Zn plating/stripping becomes highly reversible.
  - [experimental result] Measured CE of ~99.7% and 3500 h cycling stability confirm these electrochemical properties are significantly enhanced.
### M3  Properties → Performance
- cause: High Coulombic efficiency (~99.7%), long cycling stability (3500 h), and suppressed corrosion
- effect: High cumulative areal capacity (5000 mAh cm⁻² at 10 mA cm⁻²) and stable full-cell performance with Od-NVO cathode
- experiment: Full-cell testing of Zn//Od-NVO battery and cumulative areal capacity measurement | Galvanostatic charge/discharge cycling | params: 1 A g⁻¹ current density; cumulative capacity tracked over 500 cycles | result: 83.7% capacity retention after 500 cycles with NH₄OAc vs. 32.2% without; cumulative areal capacity reaches 5000 mAh cm⁻²
  - [experimental result] The Zn anode exhibits 99.7% CE and 3500 h stability due to the self-regulated interface.
  - [non-referenced_knowledge] This prevents anode degradation and minimizes by-product generation that could attack the cathode.
  - [image description] SEM of Od-NVO cathode after 50 cycles shows negligible material loss only with NH₄OAc additive.
  - [deductive reasoning] Thus, the stable anode enables stable cathode performance and high capacity retention (83.7%) over 500 cycles.
  - [experimental result] The cumulative areal capacity of 5000 mAh cm⁻² is achieved because Zn is efficiently utilized over thousands of cycles without failure.
### M4  Processing → Performance
- cause: Addition of ammonium acetate (NH₄OAc) additive to aqueous zinc sulfate (ZnSO₄) electrolyte
- effect: Long-term stable cycling of Zn anodes (3500 h at 1 mA cm⁻²) and high cumulative areal capacity (5000 mAh cm⁻² at 10 mA cm⁻²)
- experiment: Long-term cycling of Zn//Zn symmetric cells and full-cell Zn//Od-NVO testing | Galvanostatic cycling | params: 1 mA cm⁻² / 1 mAh cm⁻² for Zn//Zn; 1 A g⁻¹ for Zn//Od-NVO | result: Zn//Zn cycles for 3500 h; Zn//Od-NVO retains 83.7% capacity after 500 cycles; cumulative areal capacity reaches 5000 mAh cm⁻²
  - [experimental result] NH₄OAc is added to ZnSO₄ electrolyte as a low-cost, simple processing step.
  - [experimental result] This single modification enables 3500 h Zn//Zn cycling and 5000 mAh cm⁻² cumulative capacity.
  - [experimental result] Full-cell performance with Od-NVO cathode improves from 32.2% to 83.7% capacity retention.
  - [deductive reasoning] No anode or cathode redesign was required, confirming that the additive alone drives performance enhancement.
