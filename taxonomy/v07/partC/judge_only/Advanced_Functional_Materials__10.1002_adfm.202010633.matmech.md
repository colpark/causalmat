# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202010633 (judge only; not shown to staff)
- material: Ni-based catalysts  elements: ['Ni', 'Cu', 'Mo', 'Co', 'N']  category: ['Metals and Alloys', 'Nanomaterial', 'Composite Material']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Alloying, doping, and heterostructure engineering
- **Structure**: Metallic Ni, Ni alloys, and core–shell structures
- **Properties**: Hydrogen binding energy (HBE)–electrochemical property
- **Performance**: Hydrogen oxidation reaction (HOR) activity in alkaline media
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Alloying Ni with Cu using transition metal alloying
- effect: Formation of NiCu binary alloys with modified surface structure
- experiment: NiCu alloy synthesis and characterization | Electrochemical measurements and DFT calculations | params: NiCu binary alloys with ≈40 at% Cu | result: Maximum HOR/HER activity achieved in NiCu alloys with ≈40 at% Cu composition
  - [non-referenced_knowledge] Ni binds hydrogen too strongly, placing it on the left side of the volcano plot for HER.
  - [referenced knowledge] Metallic Cu has weaker hydrogen binding energy compared to Ni.
  - [experimental result] Alloying Ni with Cu modulates the electronic structure and hydrogen adsorption behavior.
  - [deductive reasoning] The optimal NiCu alloy composition (≈40 at% Cu) achieves balanced hydrogen binding and desorption kinetics.
### M2  Structure → Property
- cause: Formation of NiMo alloy nanosheets with interconnected morphology
- effect: Optimized hydrogen and hydroxyl adsorption free energies (ΔG_H and ΔG_OH)
- experiment: STEM imaging and HOR polarization measurements | Scanning Transmission Electron Microscopy (STEM), electrochemical testing | params: Morphology: interconnected nanosheets; Composition: MoNi₄ alloy | result: Higher HOR activity than commercial Pt/C due to optimized adsorption behavior
  - [image description] STEM images show that MoNi₄ possesses interconnected nanosheet morphology.
  - [non-referenced_knowledge] Nanoscale architecture improves charge transport and exposes more active sites.
  - [experimental result] DFT calculations indicate that alloying reduces hydrogen and hydroxyl binding energies.
  - [deductive reasoning] Thus, MoNi₄ alloy nanosheets exhibit superior HOR activity due to structural and electronic effects.
### M3  Property → Performance
- cause: Low hydrogen binding energy (ΔG_H) close to zero
- effect: High HOR activity in alkaline media
- experiment: Free energy calculation and HOR current measurement | Density Functional Theory (DFT) calculations, electrochemical polarization | params: ΔG_H near zero, HOR current density at 50 mV overpotential | result: NiMo₄ exhibits HOR current density of 33.8 mA cm⁻² at 50 mV overpotential in 0.1 M KOH
  - [experimental result] ΔG_H for MoNi₄ is calculated to be near zero, similar to Pt.
  - [image description] Polarization curves show MoNi₄ outperforms Pt/C under identical conditions.
  - [non-referenced_knowledge] A near-optimal ΔG_H minimizes activation barriers for HOR elementary steps.
  - [inductive reasoning] Therefore, low ΔG_H correlates with high HOR activity in alkaline media.
### M4  Processing → Structure
- cause: Nitridation of Co nanoparticles
- effect: Formation of Co₂N/Co heterostructure with interfacial active sites
- experiment: Co nitridation and TEM/XRD analysis | Transmission Electron Microscopy (TEM), X-ray Diffraction (XRD) | params: Nitridation temperature and time, Co/Co₂N interface formation | result: Formation of abundant interfacial sites with enhanced HOR activity
  - [experimental result] Nitridation of Co NPs leads to Co₂N/Co heterostructure formation.
  - [non-referenced_knowledge] Interfaces between Co and Co₂N enable dual-site adsorption of H* and OH*.
  - [experimental result] DFT calculations confirm that the Co/Co₂N interface optimizes ΔG_H and ΔG_OH.
  - [deductive reasoning] Therefore, nitridation-induced heterostructuring improves HOR kinetics via bifunctional mechanism.
### M5  Structure → Property
- cause: Core–shell Ni@h-BN nanostructure
- effect: Reduced hydrogen and hydroxyl binding strengths
- experiment: XPS and electrochemical HOR testing | X-ray Photoelectron Spectroscopy (XPS), cyclic voltammetry | params: Binding energy shifts, HOR current stability | result: Weakened H* and OH* adsorption confirmed by XPS and electrochemical measurements
  - [experimental result] XPS shows binding energy shift indicating electron transfer from Ni to BN layer.
  - [non-referenced_knowledge] Electron depletion lowers the d-band center of Ni, reducing adsorption strength.
  - [referenced knowledge] Lower H* and OH* binding energies correlate with improved HOR kinetics.
  - [deductive reasoning] Thus, Ni@h-BN core–shell structure enhances HOR performance by tuning adsorption energetics.
