# MatMech content for Advanced_Energy_Materials/aenm.202003639 (judge only; not shown to staff)
- material: K₂MnFe(CN)₆  elements: ['K', 'Mn', 'Fe', 'C', 'N', 'Zn', 'F', 'S', 'O']  category: ['Crystalline Material', 'Ceramic']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Synthesized using a citrate-assisted controlled precipitation method at room temperature; electrochemical cycling in 30 m KFSI + 1 m Zn(CF₃SO₃)₂ electrolyte
- **Structure**: Phase transformation from monoclinic K₂MnFe(CN)₆ to rhombohedral K₂Zn₃[Fe(CN)₆]₂ with MnN₆ octahedra replaced by ZnN₄ tetrahedra
- **Properties**: Capacity–electrochemical property
- **Performance**: Stable capacity of 100 mAh g⁻¹ over 400 cycles with 98% retention in zinc-ion battery
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Electrochemical cycling in 30 m KFSI + 1 m Zn(CF₃SO₃)₂ electrolyte
- effect: Phase transformation from monoclinic K₂MnFe(CN)₆ to rhombohedral K₂Zn₃[Fe(CN)₆]₂ with MnN₆ octahedra replaced by ZnN₄ tetrahedra
- experiment: In situ XRD | X-ray diffraction | params: Cycling at 0.2 A g⁻¹ in 30 m KFSI + 1 m Zn(CF₃SO₃)₂ electrolyte; monitoring structural evolution over 100 cycles | result: New peaks at 16.52° and 21.92° appear after 4 cycles; patterns after 20–100 cycles match K₂Zn₃[Fe(CN)₆]₂ (JCPDS No. 33–1061); monoclinic phase disappears
  - [experimental result] Electrochemical cycling in Zn²⁺-containing electrolyte leads to Zn²⁺ insertion into K₂MnFe(CN)₆.
  - [experimental result] In situ XRD shows new diffraction peaks matching K₂Zn₃[Fe(CN)₆]₂ after 4–100 cycles, confirming phase transformation.
  - [experimental result] ICP and EDS show Mn content decreases to near zero after 100 cycles while Zn content increases, indicating Mn replacement by Zn.
  - [deductive reasoning] DFT calculations reveal Zn²⁺ insertion induces strong Jahn-Teller distortion in MnN₆ octahedra, converting them to MnN₄ tetrahedra.
  - [non-referenced_knowledge] Mn³⁺ disproportionation (2Mn³⁺ → Mn²⁺ + Mn⁴⁺) occurs, releasing Mn²⁺ into electrolyte and facilitating Zn²⁺ incorporation.
  - [image description] ZnN₄ tetrahedra form stable linkages with Fe(CN)₆ octahedra via cyanide bridges, creating wider ionic channels.
  - [non-referenced_knowledge] The rhombohedral K₂Zn₃[Fe(CN)₆]₂ structure is more accommodating for Zn²⁺ diffusion than the original monoclinic phase.
  - [deductive reasoning] Thus, Zn²⁺ insertion drives a structural transformation from monoclinic to rhombohedral phase via Jahn-Teller distortion and Mn replacement.
### M2  Structure → Performance
- cause: Rhombohedral K₂Zn₃[Fe(CN)₆]₂ phase with ZnN₄ tetrahedra and wider ionic channels
- effect: Stable capacity of 100 mAh g⁻¹ over 400 cycles with 98% retention in zinc-ion battery
- experiment: Long-term galvanostatic cycling | Charge-discharge test | params: Current density: 0.2 A g⁻¹; voltage range: 0.5–2.0 V; 400 cycles | result: Capacity stabilizes at ~100 mAh g⁻¹ after 100 cycles; 98% retention from cycle 100 to 400; coulombic efficiency increases to 99–100%
  - [experimental result] After 100 cycles, XRD and EDS confirm complete transformation to K₂Zn₃[Fe(CN)₆]₂ phase.
  - [image description] The new structure features ZnN₄ tetrahedra instead of MnN₆ octahedra, creating wider channels for ion transport.
  - [non-referenced_knowledge] Tetrahedral coordination reduces lattice distortion during Zn²⁺ (de)intercalation compared to octahedral sites.
  - [experimental result] Electrochemical cycling shows capacity stabilizes at 100 mAh g⁻¹ with 98% retention over 300 additional cycles.
  - [experimental result] Coulombic efficiency increases to 99–100% after phase transition, indicating highly reversible ion storage.
  - [deductive reasoning] Thus, the new rhombohedral structure with ZnN₄ tetrahedra enables exceptional cycling stability.
### M3  Processing → Property
- cause: Electrochemical cycling in 30 m KFSI + 1 m Zn(CF₃SO₃)₂ electrolyte
- effect: Emergence of a single voltage plateau and enhanced redox reversibility
- experiment: Cyclic voltammetry (CV) | Cyclic voltammetry | params: Scan rate: 0.5 mV s⁻¹; electrolyte: 30 m KFSI + 1 m Zn(CF₃SO₃)₂ | result: Initial CV shows four redox peaks; after 100 cycles, only one pair of peaks remains, indicating simplified redox mechanism
  - [experimental result] Initial CV shows four redox peaks, indicating multiple redox couples (Mn and Fe).
  - [experimental result] After 100 cycles, CV and charge-discharge profiles show a single redox plateau.
  - [experimental result] XANES confirms Fe³⁺/Fe²⁺ as the dominant redox couple after transformation; Mn contribution vanishes.
  - [image description] Phase transformation replaces Mn sites with Zn, removing Mn-based redox activity.
  - [deductive reasoning] Thus, the system evolves to a single, stable Fe³⁺/Fe²⁺ redox process with improved reversibility.
### M4  Processing → Structure
- cause: Synthesis via citrate-assisted controlled precipitation method at room temperature
- effect: Formation of monoclinic K₂MnFe(CN)₆ with low Fe(CN)₆ vacancies and high crystallinity
- experiment: XRD Rietveld refinement | X-ray diffraction | params: Cu Kα radiation; Rietveld refinement of as-synthesized KMnHCF | result: Monoclinic structure with space group P2₁/n; Rₚ = 1.58%, Rₚₚ = 2.39%; low vacancy concentration inferred from stoichiometry
  - [experimental result] KMnHCF is synthesized using citrate-assisted controlled precipitation.
  - [experimental result] Rietveld refinement confirms monoclinic structure with low R-factors, indicating high crystallinity.
  - [experimental result] TGA and ICP show near-stoichiometric composition (K₁.₆Mn[Fe(CN)₆]₀.₉₄·0.63H₂O), suggesting minimal vacancies.
  - [non-referenced_knowledge] Citrate chelates metal ions, slowing precipitation and allowing ordered crystal growth.
  - [deductive reasoning] Thus, the synthesis method produces a high-quality monoclinic precursor essential for controlled phase transformation.
### M5  Structure → Property
- cause: Rhombohedral K₂Zn₃[Fe(CN)₆]₂ structure with ZnN₄ tetrahedra
- effect: High Fe³⁺/Fe²⁺ redox reversibility and low polarization
- experiment: XANES at Fe K-edge | X-ray absorption near edge structure | params: After 100 cycles; pristine, charged (2.0 V), and discharged (0.5 V) states | result: Fe K-edge peak shifts from 7128.6 eV (Fe²⁺) to 7129.6 eV (Fe³⁺); sharp, symmetric peak indicates high reversibility
  - [experimental result] XANES shows clear, reversible Fe K-edge shift between 7128.6 eV and 7129.6 eV after 100 cycles.
  - [experimental result] DOS calculations show degenerate states in K₂MnFe(CN)₆ are lifted upon Zn²⁺ insertion, reducing electronic instability.
  - [image description] Tetrahedral ZnN₄ sites provide geometric and electronic stability to adjacent Fe(CN)₆ units.
  - [non-referenced_knowledge] A symmetric, non-degenerate electronic structure facilitates smooth electron transfer during redox.
  - [deductive reasoning] Thus, the new structure enables highly reversible Fe-based redox with low polarization.
