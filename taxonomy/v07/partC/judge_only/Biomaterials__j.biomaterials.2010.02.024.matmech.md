# MatMech content for Biomaterials/j.biomaterials.2010.02.024 (judge only; not shown to staff)
- material: silk fibroin  elements: ['C', 'H', 'O', 'N', 'S']  category: ['Polymer', 'Nanomaterial', 'Biomaterial']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: salting out with potassium phosphate at varying ionic strengths and pH levels
- **Structure**: silk I (less crystalline) and silk II (crystalline) secondary structures controlled by pH
- **Properties**: zeta potential–electrostatic property, chemical stability–mechanical/structural property
- **Performance**: controlled drug release dependent on charge and secondary structure
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Salting out silk fibroin solution with potassium phosphate at pH 6
- effect: Formation of silk II (crystalline) secondary structure in particles
- experiment: FTIR spectroscopy of silk particles | Fourier transform infrared (FTIR) spectroscopy | params: Analysis of amide I region (1595–1705 cm⁻¹) after salting out with 1.25 M potassium phosphate at pH 6 | result: Absorption bands at 1616–1637 cm⁻¹ and 1695–1705 cm⁻¹ indicate dominant β-sheet (silk II) structure
  - [experimental result] Silk fibroin particles were produced by salting out with 1.25 M potassium phosphate at pH 6.
  - [experimental result] FTIR spectra show strong absorption bands at 1616–1637 cm⁻¹ and 1695–1705 cm⁻¹, characteristic of β-sheet structure.
  - [non-referenced_knowledge] Table 1 quantifies β-sheet content at 37.4% for pH 6 particles, confirming dominant silk II structure.
  - [non-referenced_knowledge] At pH 6, near the isoelectric point (pI=4.53), electrostatic repulsion is minimized, promoting chain proximity.
  - [referenced knowledge] Kosmotropic salts like potassium phosphate enhance hydrophobic interactions and dehydrate protein chains, favoring β-sheet formation.
  - [deductive reasoning] Thus, salting out at pH 6 induces silk II structure via reduced charge repulsion and enhanced hydrophobic packing.
### M2  Processing → Structure
- cause: Salting out silk fibroin solution with potassium phosphate at pH 9
- effect: Formation of silk I (less crystalline) secondary structure in particles
- experiment: FTIR spectroscopy of silk particles | Fourier transform infrared (FTIR) spectroscopy | params: Analysis of amide I region (1595–1705 cm⁻¹) after salting out with 1.25 M potassium phosphate at pH 9 | result: Absorption bands at 1638–1655 cm⁻¹ indicate dominant random coil and α-helix (silk I) structure
  - [experimental result] Silk fibroin particles were produced by salting out with 1.25 M potassium phosphate at pH 9.
  - [experimental result] FTIR spectra show reduced β-sheet peaks and dominant peaks at 1638–1655 cm⁻¹ (random coil) and 1656–1663 cm⁻¹ (α-helix).
  - [non-referenced_knowledge] Table 1 shows β-sheet content is only 21.5% at pH 9, while α-helix and random coil exceed 70%.
  - [non-referenced_knowledge] At pH 9, amino acid side chains (Asp, Glu) are fully deprotonated, creating high negative charge density on the protein.
  - [deductive reasoning] Electrostatic repulsion between chains prevents hydrophobic alignment necessary for β-sheet nucleation.
  - [deductive reasoning] Thus, high pH stabilizes the hydrated, disordered silk I conformation despite salting out.
### M3  Structure → Performance
- cause: Silk fibroin particles with higher silk II (β-sheet) content produced at pH 7
- effect: Increased initial burst release of crystal violet during in vitro drug release
- experiment: In vitro drug release kinetics | UV-Vis spectrometry of released crystal violet | params: Incubation of drug-loaded particles in PBS (pH 7.4) for 7 days; particles produced at pH 7, 8, and 9 | result: Initial burst release (first 3 h): 29% for pH 7 (silk II-rich), 17% for pH 8, 11% for pH 9 (silk I-rich)
  - [experimental result] Crystal violet release was measured from silk particles produced at pH 7, 8, and 9.
  - [experimental result] Particles at pH 7 had highest β-sheet content (31.1%) and showed 29% initial burst release.
  - [experimental result] Particles at pH 9 had lowest β-sheet content (21.5%) and showed only 11% initial burst release.
  - [non-referenced_knowledge] Silk II structure forms crystalline domains that, despite being stable, can create interstitial pores upon particle hydration.
  - [deductive reasoning] Higher crystallinity increases water uptake and swelling, accelerating diffusion of small molecules like crystal violet.
  - [inductive reasoning] Thus, higher silk II content correlates with faster initial drug release due to enhanced matrix permeability.
### M4  Structure → Performance
- cause: Silk fibroin particles with higher silk I (amorphous) content produced at pH 9
- effect: Slower, more sustained release of crystal violet due to denser, less permeable matrix
- experiment: In vitro drug release kinetics | UV-Vis spectrometry of released crystal violet | params: Incubation of drug-loaded particles in PBS (pH 7.4) for 7 days; particles produced at pH 9 | result: Only 11% initial burst release and sustained release over 7 days for pH 9 particles (silk I-rich)
  - [experimental result] Crystal violet release was measured from particles produced at pH 9, which had dominant silk I structure (Table 1).
  - [experimental result] Initial burst release was only 11% for pH 9 particles, significantly lower than pH 7 (29%).
  - [non-referenced_knowledge] At pH 9, silk fibroin chains are extended and repelled electrostatically, forming a hydrated, amorphous matrix.
  - [deductive reasoning] This amorphous matrix has lower porosity and higher hydration, creating a diffusion barrier for drug molecules.
  - [deductive reasoning] Thus, silk I structure enables prolonged, sustained release by restricting drug diffusion.
### M5  Processing → Property
- cause: Adjusting pH during salting out from pH 4 to pH 9
- effect: Zeta potential of silk fibroin particles becomes more negative
- experiment: Zeta potential measurement | Nanoseries Malvern Zetasizer | params: Particles produced with 1.25 M potassium phosphate at pH 4, 6, 8, and 9; measured after three washes | result: Zeta potential increased from -26.3 mV (pH 4) to -46.0 mV (pH 9)
  - [experimental result] Silk fibroin particles were produced at pH values ranging from 4 to 9 using potassium phosphate salting out.
  - [experimental result] Zeta potential measurements show a linear increase in negativity from -26.3 mV (pH 4) to -46.0 mV (pH 9).
  - [referenced knowledge] The isoelectric point of silk fibroin is 4.53; above this pH, net negative charge increases.
  - [non-referenced_knowledge] As pH increases, carboxyl groups (D, E) and phenolic groups (Y) lose protons, contributing negative charge.
  - [deductive reasoning] Thus, higher pH leads to greater surface negativity, reflected in increasingly negative zeta potential.
### M6  Property → Performance
- cause: Increased negative zeta potential of silk fibroin particles at higher pH
- effect: Enhanced loading efficiency of positively charged drugs like crystal violet and alcian blue
- experiment: Drug loading efficiency | UV-Vis spectrometry of supernatant after incubation | params: Loading of crystal violet, alcian blue, and rhodamine B onto particles produced at pH 8; varying MD:SF molar ratios | result: Loading efficiency >95% for crystal violet and alcian blue at low loadings; zeta potential decreased with loading as surface charge was neutralized
  - [experimental result] Silk fibroin particles produced at pH 8 have zeta potential of approximately -40 mV.
  - [experimental result] Loading efficiency for crystal violet and alcian blue exceeds 95% at low drug-to-protein ratios.
  - [experimental result] Zeta potential decreases with increasing drug loading, indicating neutralization of surface charge by cationic drugs.
  - [non-referenced_knowledge] Crystal violet and alcian blue are positively charged; electrostatic attraction drives their adsorption onto negatively charged particles.
  - [deductive reasoning] Thus, higher negative zeta potential enhances drug loading via Coulombic interactions.
### M7  Processing → Performance
- cause: Salting out with potassium phosphate at ionic strength below 0.75 M
- effect: No particle formation or low yield
- experiment: Salting out efficiency measurement | Light microscopy and gravimetric analysis | params: Potassium phosphate concentrations from 0.25 M to 2.0 M at pH 8 | result: Particle formation threshold at ~0.75 M; below this, no particles observed
  - [experimental result] Salting out efficiency was measured across potassium phosphate concentrations from 0.25 M to 2.0 M.
  - [experimental result] No particles were observed by light microscopy below 0.75 M.
  - [experimental result] Above 0.75 M, efficiency increased sharply to >90% at 1.25 M.
  - [referenced knowledge] Kosmotropic salts like phosphate ions dehydrate proteins and reduce solubility by disrupting hydration shells.
  - [non-referenced_knowledge] Below threshold ionic strength, hydration and electrostatic repulsion dominate, preventing aggregation.
  - [deductive reasoning] Thus, ionic strength must exceed 0.75 M to initiate phase separation and particle formation.
