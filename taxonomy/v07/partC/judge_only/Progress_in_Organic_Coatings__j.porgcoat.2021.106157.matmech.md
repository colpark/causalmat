# MatMech content for Progress_in_Organic_Coatings/j.porgcoat.2021.106157 (judge only; not shown to staff)
- material: AZ31 Mg alloy  elements: ['Mg', 'Al', 'Zn', 'C', 'H', 'O']  category: ['Metals and Alloys', 'Polymer', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Alkaline pretreatment in 1 M NaOH at 80°C for 4 h, followed by drop-casting of PCL/lawsone (1% w/w) inner layer and pure PCL top layer
- **Structure**: Bi-layered polymeric coating with inner PCL/lawsone layer and outer pure PCL layer; formation of Mg(OH)₂ passive layer on substrate; insoluble Mg²⁺-lawsone complexes at defect sites
- **Properties**: Corrosion current density–electrochemical property, Inhibition efficiency–electrochemical property, Contact angle–surface property, Antibacterial activity–biological property, Cytocompatibility–biological property
- **Performance**: Reduced hydrogen evolution, suppressed pH increase, long-term corrosion resistance in Hank’s solution, inhibition of E. coli and S. aureus, >85% cell viability of hFOB cells
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Alkaline pretreatment in 1 M NaOH at 80°C for 4 h, followed by drop-casting of PCL/lawsone (1% w/w) inner layer and pure PCL top layer
- effect: Bi-layered polymeric coating with inner PCL/lawsone layer and outer pure PCL layer; formation of Mg(OH)₂ passive layer on substrate
- experiment: Coating fabrication | Drop-casting and alkaline treatment | params: 1 M NaOH at 80°C for 4 h; 1% w/w lawsone in PCL solution; 200 μL per side; 24 h drying at room temperature | result: Formation of a compact, uniform bi-layered coating with 10 μm total thickness and 4 μm Mg(OH)₂ layer
  - [experimental result] AZ31 samples were immersed in 1 M NaOH at 80°C for 4 h to form a passive Mg(OH)₂ layer.
  - [referenced knowledge] The Mg(OH)₂ layer prevents corrosion during coating application and ensures homogenous coating formation [47].
  - [experimental result] PCL/lawsone solution (1% w/w) was drop-cast as an inner functional layer, followed by pure PCL as a top barrier layer.
  - [image description] SEM cross-section (Fig. 2E) confirms the bi-layered structure with distinct inner and outer polymer layers and underlying oxide.
  - [deductive reasoning] This processing sequence intentionally creates a structure where lawsone is encapsulated and released only upon coating damage.
### M2  Structure → Property
- cause: Bi-layered polymeric coating with inner PCL/lawsone layer and outer pure PCL layer; formation of Mg(OH)₂ passive layer on substrate
- effect: Corrosion current density reduced to 5.9 × 10⁻⁸ A/cm²; inhibition efficiency of 98.3%; contact angle of 96.1° ± 1.6°; antibacterial zone of inhibition of 26 mm for E. coli and 22 mm for S. aureus
- experiment: Electrochemical polarization and EIS | Potentiodynamic polarization and Electrochemical Impedance Spectroscopy | params: Hank’s solution, scan rate 1 mV/s, frequency range 10⁻² to 10⁵ Hz, AC amplitude ±10 mV | result: PCL-LS showed lowest I_corr (5.9 × 10⁻⁸ A/cm²) and highest IE (98.3%); EIS showed highest R_ct (50.2 kΩ cm²)
  - [experimental result] PCL-LS coating exhibits I_corr = 5.9 × 10⁻⁸ A/cm² and IE = 98.3%, significantly lower than bare AZ31 (3.7 × 10⁻⁶ A/cm²).
  - [referenced knowledge] Lawsone chelates dissolving Mg²⁺ ions to form insoluble complexes that block active corrosion sites [36, 38].
  - [experimental result] Contact angle of PCL-LS is 96.1° ± 1.6°, indicating hydrophobic surface that resists water penetration [61].
  - [non-referenced_knowledge] Hydrophobicity reduces electrolyte access to the metal surface, enhancing barrier properties.
  - [image description] PCL-LS shows 26 mm inhibition zone against E. coli and 22 mm against S. aureus due to lawsone's quinone groups disrupting bacterial membranes [43].
  - [deductive reasoning] Thus, the structure enables lawsone to provide dual functionality: corrosion inhibition via chelation and antibacterial activity via protein inactivation.
### M3  Structure → Property
- cause: Bi-layered polymeric coating with inner PCL/lawsone layer and outer pure PCL layer
- effect: Cytocompatibility >85% viability of human fetal osteoblast (hFOB) cells
- experiment: CCK-8 cytocompatibility assay | Cell viability test | params: hFOB 1.19 cells exposed to sample leachates for 1, 3, and 5 days; CCK-8 reagent; absorbance at 450 nm | result: PCL-LS and PCL coatings showed >85% cell viability after 5 days, significantly higher than uncoated AZ31
  - [referenced knowledge] Uncoated AZ31 shows low cell viability due to rapid degradation, high pH, and H₂ gas formation [92].
  - [experimental result] PCL-LS coating reduces hydrogen evolution by 84% and pH increase compared to bare AZ31 (Fig. 9A,B).
  - [experimental result] CCK-8 assay shows >85% viability for PCL-LS after 5 days, comparable to control.
  - [non-referenced_knowledge] The outer PCL layer limits lawsone release, preventing cytotoxicity from high local concentrations.
  - [deductive reasoning] Thus, the bi-layered structure maintains a biocompatible microenvironment by suppressing degradation products.
### M4  Structure → Performance
- cause: Bi-layered polymeric coating with inner PCL/lawsone layer and outer pure PCL layer; formation of Mg(OH)₂ passive layer on substrate
- effect: Reduced hydrogen evolution (1.25 ± 0.28 mL·cm⁻² after 7 days), suppressed pH increase (8.16 ± 0.10), and intact surface morphology after 7-day immersion
- experiment: Immersion test with H₂ evolution and pH monitoring | In vitro immersion in Hank’s solution | params: 7 days at 37°C, 20 mL/cm² volume-to-area ratio, H₂ collected via inverted funnel-burette, pH recorded daily | result: PCL-LS: H₂ evolution = 1.25 mL·cm⁻², final pH = 8.16; compared to AZ31: 7.92 mL·cm⁻², pH = 10.88
  - [referenced knowledge] The Mg(OH)₂ layer from alkaline pretreatment provides initial corrosion resistance [47].
  - [experimental result] PCL-LS coating reduces H₂ evolution to 1.25 mL·cm⁻² vs. 7.92 mL·cm⁻² for bare AZ31.
  - [non-referenced_knowledge] The reaction Mg + 2H₂O → Mg²⁺ + 2OH⁻ + H₂(g) links H₂ evolution directly to pH increase [83].
  - [experimental result] Final pH for PCL-LS is 8.16, far below AZ31’s 10.88, indicating suppressed alkalization.
  - [image description] SEM (Fig. 8) confirms PCL-LS surface remains intact, while uncoated samples are heavily corroded.
  - [deductive reasoning] Thus, the structure prevents both initial and long-term degradation, achieving superior performance.
### M5  Processing → Performance
- cause: Drop-casting of PCL/lawsone (1% w/w) inner layer and pure PCL top layer
- effect: Long-term stable corrosion resistance maintained over 7-day immersion, with no inductive loop in EIS and stable |Z|₀.₀₁Hz
- experiment: Long-term EIS monitoring | Electrochemical Impedance Spectroscopy over 7 days | params: EIS measured after 1, 3, and 7 days immersion in Hank’s solution | result: PCL-LS maintained high R_ct and |Z|₀.₀₁Hz over 7 days; PCL showed rapid decline; no inductive loop in PCL-LS after 7 days
  - [experimental result] PCL coating shows decreasing |Z|₀.₀₁Hz and emergence of inductive loop after 3–7 days, indicating water penetration and pitting [79].
  - [experimental result] PCL-LS maintains stable |Z|₀.₀₁Hz and no inductive loop even after 7 days, indicating no pitting corrosion [80].
  - [experimental result] R_ct of PCL-LS remains high (2.05 × 10⁴ Ω cm² at day 7) due to lawsone's chelation of Mg²⁺ forming protective complexes [81].
  - [non-referenced_knowledge] Lawsone release from inner layer continuously seals defects, preventing electrolyte penetration.
  - [deductive reasoning] Thus, the processing method of embedding lawsone in a bi-layered structure enables long-term performance.
### M6  Processing → Performance
- cause: Alkaline pretreatment in 1 M NaOH at 80°C for 4 h
- effect: Improved coating adhesion strength (4B grade) and reduced initial corrosion rate
- experiment: Cross-cut tape adhesion test | ASTM D3359 adhesion test | params: 100 squares of 1 mm², adhesive tape pulled at 180° after 90 s | result: Adhesion grade 4B for AZ31-OH/PCL-LS vs. 3B for untreated AZ31/PCL-LS
  - [experimental result] AZ31 samples were treated in 1 M NaOH at 80°C for 4 h to form Mg(OH)₂ layer.
  - [experimental result] ATR-FTIR confirms hydroxyl peak at 3700 cm⁻¹, verifying Mg(OH)₂ formation [57].
  - [experimental result] Cross-cut test shows 4B adhesion on AZ31-OH vs. 3B on untreated AZ31 [62].
  - [referenced knowledge] Hydroxyl groups on Mg(OH)₂ form hydrogen bonds with PCL’s ester/carbonyl groups, improving interfacial adhesion [62].
  - [non-referenced_knowledge] Strong adhesion prevents under-coating corrosion and delamination, improving long-term performance.
  - [deductive reasoning] Thus, alkaline pretreatment enhances both mechanical adhesion and initial corrosion resistance.
