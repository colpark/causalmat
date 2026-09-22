# MatMech content for Nano_Letters/10.1021_acs.nanolett.6b04294 (judge only; not shown to staff)
- material: Porous Cobalt Oxide (PCO)  elements: ['Co', 'O']  category: ['Nanomaterial', 'Ceramic']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Thermal decomposition of Co-based MOF under air atmosphere
- **Structure**: Porous structure with interconnected nano-sized particles and mesopores
- **Properties**: Reversible capacity–electrochemical property
- **Performance**: Inferior sodium storage performance compared to lithium storage
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Thermal decomposition of Co-based MOF under air atmosphere
- effect: Porous structure with interconnected nano-sized particles and mesopores formed in cobalt oxide
- experiment: HEXRD, TGA, BET surface area analysis | Synchrotron X-ray diffraction, thermogravimetric analysis, nitrogen adsorption-desorption isotherms | params: Calcination at 300°C for 6 h under air atmosphere | result: Formation of porous structure confirmed by SEM/TEM imaging and BET surface area measurement (45.02 m²/g); pore volume measured as 0.172 cm³/g
  - [experimental result] The preparation involved calcination of ZIF-67 precursors at 300°C in air for 6 hours.
  - [image description] SEM and TEM images show interconnected nanoparticles (~10–20 nm) with mesopores in the resulting PCO.
  - [experimental result] BET specific surface area was measured to be 45.02 m²/g with a pore volume of 0.172 cm³/g.
  - [non-referenced_knowledge] Thermal decomposition of MOFs typically leads to porous structures due to gas release during calcination.
  - [deductive reasoning] Thus, thermal decomposition of Co-MOF under air forms a porous cobalt oxide structure with interconnected nanoparticles and mesopores.
### M2  Structure → Performance
- cause: Porous structure with interconnected nano-sized particles and mesopores
- effect: Superior lithium storage performance compared to sodium storage
- experiment: Electrochemical testing | Coin cell assembly and cycling tests | params: Li/Na counter electrodes, FEC additive electrolyte, 0.1C rate | result: Li/PCO cell showed initial discharge capacity of 1330.3 mAh/g and 96.4% capacity retention after 40 cycles vs. Na/PCO cell with 866.2 mAh/g initial discharge capacity and rapid fading
  - [experimental result] The PCO electrode demonstrated reversible capacity of 839.5 mAh/g after 40 cycles at 0.1C with Li counter electrode.
  - [experimental result] In contrast, the Na/PCO cell showed continuous capacity degradation with only 471.6 mAh/g charge capacity after first cycle.
  - [referenced knowledge] Porous structures generally improve ion diffusion kinetics and accommodate volumetric expansion in battery electrodes.
  - [non-referenced_knowledge] Smaller ions like Li⁺ typically exhibit faster diffusion kinetics than larger Na⁺ ions in similar structures.
  - [inductive reasoning] Therefore, the porous structure benefits Li⁺ transport more effectively than Na⁺, explaining the superior lithium storage performance.
### M3  Processing → Performance
- cause: Thermal decomposition of Co-based MOF under air atmosphere
- effect: Inferior sodium storage performance compared to lithium storage
- experiment: Ab initio MD simulations | Computational modeling | params: Simulated lithiation/sodiation of Co₃O₄ surfaces at 1000 K | result: Sodiated Co₃O₄ showed only 36.4% Na oxidation vs. 90% Li oxidation in lithiated Co₃O₄, indicating lower sodiation activity
  - [experimental result] Thermal decomposition of Co-MOF produces porous cobalt oxide with interconnected nanostructure.
  - [experimental result] MD simulations showed only 36.4% Na oxidation vs. 90% Li oxidation in Co₃O₄ systems.
  - [referenced knowledge] Metal oxides typically exhibit different reactivity toward Li⁺ and Na⁺ due to size and bonding differences.
  - [non-referenced_knowledge] Sodium ions have larger radius (1.02 Å) than lithium ions (0.76 Å), affecting diffusion and reaction kinetics.
  - [deductive reasoning] Therefore, thermal decomposition creates a porous oxide structure favorable for smaller Li⁺ ions but not for larger Na⁺, leading to asymmetric storage performance.
