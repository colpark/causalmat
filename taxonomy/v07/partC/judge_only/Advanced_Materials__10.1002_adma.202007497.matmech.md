# MatMech content for Advanced_Materials/10.1002_adma.202007497 (judge only; not shown to staff)
- material: Zn anode with polyimide coating  elements: ['Zn', 'C', 'H', 'O', 'N']  category: ['Polymer', 'Metals and Alloys', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Polyimide precursor solution spin-coated and crosslinked under UV light, followed by baking at 220°C
- **Structure**: In situ formation of a Zn blanket due to coordination of carbonyl oxygen atoms with Zn ions
- **Properties**: Corrosion resistance–chemical property, Zn transference number–electrical property
- **Performance**: Reduced capacity loss to 10% after ten-hour rest, stable cycling in hydrogel electrolyte, skin-mountable with resistance to deformations and splashing
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Polyimide precursor solution spin-coated and crosslinked under UV light, followed by baking at 220°C
- effect: In situ formation of a Zn blanket due to coordination of carbonyl oxygen atoms with Zn ions
- experiment: FTIR spectroscopy of polyimide after aging in ZnSO4 solution | FTIR spectroscopy | params: Aged for 24 h in 2 M ZnSO4 solution | result: Characteristic peaks of C=O (1720 cm⁻¹) and C-N bonding (1375 cm⁻¹) confirmed successful imidization and Zn coordination
  - [experimental result] Spin-coating and UV crosslinking of the poly(amic acid) precursor forms a thin film on Zn.
  - [image description] Baking at 220 °C triggers imidization and creates stable adhesion between polyimide and Zn.
  - [experimental result] FTIR spectrum confirms presence of C=O and C–N bonds in polyimide structure after imidization.
  - [non-referenced_knowledge] Carbonyl oxygen atoms in polyimide act as electron donors and coordinate with Zn²⁺ ions during cycling.
  - [experimental result] XPS and Auger spectroscopy confirm Zn binding with oxygen atoms in the cycled polyimide.
  - [deductive reasoning] Thus, the coordinated Zn builds up an in situ Zn blanket that minimizes concentration gradients at the interface.
### M2  Structure → Property
- cause: In situ formation of a Zn blanket due to coordination of carbonyl oxygen atoms with Zn ions
- effect: Corrosion resistance–chemical property, Zn transference number–electrical property
- experiment: Tafel polarization and impedance measurements | Electrochemical analysis | params: Linear sweep rate of 1 mV s⁻¹; symmetrical cell configuration | result: Corrosion current reduced by over one order of magnitude; ohmic resistance-controlled process observed
  - [non-referenced_knowledge] Zn ions coordinated with carbonyl oxygen atoms reduce local charge transfer and prevent corrosion.
  - [experimental result] Tafel plots show reduced corrosion current density for piZn compared to bare Zn.
  - [experimental result] Nyquist plots reveal ohmic resistance-controlled suppression of corrosion due to polyimide-induced IR drop.
  - [experimental result] Zn transference number increases from 0.35 (bare Zn) to 0.59 (piZn), indicating cation-dominated transport.
  - [non-referenced_knowledge] Enhanced Zn transference number minimizes concentration gradient and lowers plating/stripping overpotential.
  - [deductive reasoning] Therefore, the Zn blanket improves both corrosion resistance and electrochemical reversibility.
### M3  Property → Performance
- cause: Corrosion resistance–chemical property, Zn transference number–electrical property
- effect: Reduced capacity loss to 10% after ten-hour rest, stable cycling in hydrogel electrolyte, skin-mountable with resistance to deformations and splashing
- experiment: Galvanostatic cycling and rate performance tests | Battery testing system (Arbin 2000) | params: Current density: 4 mA cm⁻²; depth of discharge: 85% | result: piZn microbattery retains 60% capacity after 1000 cycles; coulombic efficiency stabilized at ~99.5%
  - [experimental result] piZn microbattery exhibits only 10% capacity loss after 10-hour rest, compared to 40% for bare Zn.
  - [experimental result] Coulombic efficiency stabilizes at ~99.5%, allowing deep cycling at 85% DOD without degradation.
  - [experimental result] Quasi-solid-state piZn microbattery delivers 400 stable cycles and supercapacitor-level rate performance.
  - [non-referenced_knowledge] The polyimide layer prevents Zn corrosion and dendrite formation, ensuring safe operation under deformation.
  - [experimental result] Skin-mountable microbattery maintains >90% capacity retention after repeated bending and external impact.
  - [inductive reasoning] Therefore, the improved properties translate into superior performance in terms of stability, rate capability, and mechanical robustness.
