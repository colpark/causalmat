# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202010261 (judge only; not shown to staff)
- material: Dual-salt polymer electrolyte (DSPE)  elements: ['Li', 'T', 'S', 'F', 'I', 'B', 'O', 'N', 'C', 'H']  category: ['Polymer', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Fabrication via tape casting with PTFE scaffold, PVDF-HFP matrix, dual-salt (LiTFSI and LiBOB), and functional plasticizers (ADN/FEC)
- **Structure**: Ultrathin (20 µm) and non-flammable with stable interface layers on anode and cathode
- **Properties**: Ionic conductivity–electrical property (0.45 mS cm^-1), electrochemical window–electrical property (4.91 V vs. Li/Li+)
- **Performance**: Suppresses Li dendrite formation, maintains high capacity (112 mAh g^-1) over 1000 cycles at 2 C
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Fabrication via tape casting with PTFE scaffold, PVDF-HFP matrix, dual-salt (LiTFSI and LiBOB), and functional plasticizers (ADN/FEC)
- effect: DSPE forms a compact and ultrathin structure with thickness of 20 µm due to infiltration into porous PTFE scaffold
- experiment: SEM characterization of DSPE | Scanning Electron Microscopy | params: Morphology of surface and cross-section | result: Electrolyte filled pores of PTFE scaffold resulting in 20 µm thick DSPE
  - [experimental result] PVDF-HFP works as polymer matrix combining compounds during fabrication
  - [image description] SEM images show electrolyte filled PTFE scaffold pores forming compact structure
  - [non-referenced_knowledge] PTFE provides mechanical stability to thin films
  - [deductive reasoning] Thus, tape casting with PTFE scaffold produces mechanically robust ultrathin DSPE
### M2  Structure → Property
- cause: Ultrathin (20 µm) structure with low areal density (5.6 mg cm^-2)
- effect: High specific energy density of 231 Wh kg^-1 for Li/DSPE/NMC811 cell
- experiment: Energy density calculation | Theoretical Calculation | params: Discharge voltage plateau, active material loading, specific capacity | result: DSPE-based cell achieves 231 Wh kg^-1 vs 157 Wh kg^-1 for CBE system
  - [non-referenced_knowledge] Equation shows energy density depends on discharge voltage and component masses
  - [experimental result] DSPE has much lower areal density than PPS/CBE (5.6 vs 16.0 mg cm^-2)
  - [deductive reasoning] Therefore, lighter DSPE significantly improves calculated specific energy density
### M3  Processing → Property
- cause: Dual-salt synergized with ADN/FEC plasticizers (LiTFSI/LiBOB ratio)
- effect: High ionic conductivity (0.45 mS cm^-1) and large electrochemical window (4.91 V vs Li/Li+)
- experiment: Ionic conductivity measurement | Electrochemical Impedance Spectroscopy | params: Dual salt concentration (1-3 mmol mL^-1) | result: Conductivity peaks at 0.45 mS cm^-1 for 2 mmol mL^-1 formulation
  - [experimental result] Raman spectroscopy shows Li+-ADN/FEC coordination environment
  - [image description] Ab initio simulations reveal ADN dominates first solvation shell of Li+
  - [referenced knowledge] FEC enters second solvation shell based on RDF analysis
  - [deductive reasoning] This coordination structure facilitates Li+ transport through reduced desolvation barrier
### M4  Property → Performance
- cause: High transference number (tLi+ = 0.67) and non-flammable nature
- effect: Suppresses Li dendrite formation over 1200 h cycling at 0.1 mA cm^-2
- experiment: Symmetrical Li/Li cell testing | Galvanostatic Cycling | params: 0.1 mA cm^-2 current density, 0.1 mAh cm^-2 capacity | result: No short-circuiting observed after 1200 h with DSPE vs 501 h with FEC-free variant
  - [experimental result] XPS confirms F- and B-containing groups in SEI from DSPE decomposition
  - [non-referenced_knowledge] FEC additive preferentially bonds with Li creating protective SEI layer
  - [referenced knowledge] Non-flammable DSPE eliminates thermal runaway risk from electrolyte ignition
  - [inductive reasoning] Combined effects lead to dendrite-free Li deposition and improved safety
### M5  Structure → Performance
- cause: Stable interface layers formed on both electrodes from DSPE decomposition
- effect: Maintains 112 mAh g^-1 capacity over 1000 cycles at 2C rate
- experiment: Long-term cycling test | Galvanostatic Cycling | params: 2C rate, 1000 cycles | result: Li/DSPE/NMC811 retains 78.3% initial capacity vs rapid decay in CBE system
  - [experimental result] XPS reveals F-, N-, and B-containing species in CEI from DSPE decomposition
  - [image description] Density functional theory confirms ADN adsorption on NMC811 surface
  - [non-referenced_knowledge] These components create stable CEI that suppresses Ni²+ reduction and Mn dissolution
  - [deductive reasoning] Stable interfaces enable long-term cycling performance at high rates
