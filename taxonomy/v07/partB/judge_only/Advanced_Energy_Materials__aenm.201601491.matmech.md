# MatMech content for Advanced_Energy_Materials/aenm.201601491 (judge only; not shown to staff)
- material: V/Fe PBA (vanadium hexacyanoferrate Prussian blue analogue)  elements: ['V', 'Fe', 'C', 'N', 'O', 'H', 'Na']  category: ['Crystalline Material', 'Nanomaterial', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Co-precipitation method with optimization of acidity (1 vol% HCl) and molar ratios of precursor solutions, followed by heating at 60°C for 3 h and vacuum drying at 80°C
- **Structure**: Cubic crystal structure with V and Fe ions octahedrally coordinated by cyanide bridges; 1/6 of cyanide groups replaced by oxygen atoms; 1/3 of hexacyanoferrate sites vacant; 3D hydrogen-bonding network with zeolitic and ligand water molecules
- **Properties**: 91 mA h g⁻¹–electrochemical capacity, 54 mA h g⁻¹ at 3520 mA g⁻¹–rate capability, multiple-electron redox reactions–electrochemical property
- **Performance**: High cycling stability (80% capacity retention after 250 cycles at 880 mA g⁻¹), suitability for large-scale stationary energy storage systems due to high efficiency, low cost, and aqueous electrolyte compatibility
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Co-precipitation method with optimization of acidity (1 vol% HCl) and molar ratios of precursor solutions
- effect: V/Fe PBA exhibits high crystallinity with cubic phase structure, reduced amorphous content, and well-grown crystallites of tens of nanometers
- experiment: X-ray diffraction (XRD) analysis | XRD | params: Cu Ka1 radiation (λ = 0.154 nm); comparison of simple mixing, co-precipitation without HCl, and co-precipitation with 1 vol% HCl | result: Co-precipitation with HCl produced sharp, well-defined diffraction peaks indexed to cubic V₃[Fe(CN)₆]₂ (PDF 00-042-1440) with no broad amorphous background
  - [experimental result] Co-precipitation with HCl maintains a constant molar ratio of VCl₂ to Na₄Fe(CN)₆ throughout synthesis.
  - [referenced knowledge] HCl increases acidity, which retards crystal growth rate according to prior literature.
  - [experimental result] XRD patterns show sharper peaks and no amorphous background for HCl-assisted co-precipitation compared to other methods.
  - [image description] TEM reveals well-defined crystallites (tens of nm) with limited amorphous regions only in HCl-co-precipitated samples.
  - [deductive reasoning] Thus, controlled synthesis conditions enable long-range atomic ordering and high crystallinity in V/Fe PBA.
### M2  Structure → Property
- cause: Cubic crystal structure with 1/6 cyanide replaced by oxygen, 1/3 hexacyanoferrate sites vacant, and 3D hydrogen-bonding network from zeolitic/ligand water
- effect: Multiple-electron redox reactions of both V and Fe ions, enabling high specific capacity (91 mA h g⁻¹) and low activation energy for ion diffusion
- experiment: Ex situ XANES analysis of Fe and V K-edges | X-ray Absorption Near Edge Spectroscopy | params: Measured at various charge states (0.45–1.15 V vs. Ag/AgCl); reference spectra: FeO, Fe₂O₃, V₂O₃, VO₂, V₂O₅ | result: Systematic shift of Fe and V K-edge energies with charge state confirms reversible redox: V³⁺ ↔ V⁴⁺ ↔ V⁵⁺ and Fe²⁺ ↔ Fe³⁺
  - [image description] V/Fe PBA structure contains oxygen-substituted cyanide bridges and vacant Fe(CN)₆ sites, distorting V coordination from ideal octahedron.
  - [experimental result] V K-edge XANES shows strong pre-edge peak, indicating distorted local symmetry around V, consistent with V=O bonds.
  - [experimental result] Fe and V K-edge energies shift systematically with charge, proving both ions participate in redox reactions.
  - [experimental result] FT-IR shows broad peak at ~3430 cm⁻¹, confirming presence of zeolitic and ligand water molecules.
  - [referenced knowledge] 3D hydrogen-bonding network enables proton mobility via Grotthuss mechanism, reducing activation energy for ion diffusion.
  - [deductive reasoning] Thus, structural defects and water networks enable multiple-electron redox and fast kinetics, leading to high capacity.
### M3  Structure → Property
- cause: Large lattice parameter (>10 Å) and open framework of V/Fe PBA
- effect: Facile diffusion kinetics of Na⁺ ions and high rate capability (54 mA h g⁻¹ at 3520 mA g⁻¹)
- experiment: Rate capability test | Galvanostatic charge/discharge | params: Current densities from 55 to 3520 mA g⁻¹; 5 cycles per current density | result: Discharge capacity of 54 mA h g⁻¹ retained at 3520 mA g⁻¹ (64× higher than 55 mA g⁻¹), with 57% capacity retention at ultra-high rate
  - [experimental result] V/Fe PBA has a cubic structure with lattice parameter >10 Å, as confirmed by XRD indexing.
  - [non-referenced_knowledge] Large lattice parameter reduces steric hindrance and allows guest ions to intercalate with minimal dehydration.
  - [experimental result] Rate capability test shows 54 mA h g⁻¹ capacity at 3520 mA g⁻¹, significantly higher than other PBAs.
  - [experimental result] CV and dQ/dV plots show preserved redox peaks even at high rates, indicating fast kinetics.
  - [deductive reasoning] Thus, the open framework enables rapid Na⁺ transport, leading to high rate capability.
### M4  Processing → Performance
- cause: Optimized co-precipitation with HCl yields high crystallinity and uniform morphology
- effect: High cycling stability (80% capacity retention after 250 cycles at 880 mA g⁻¹) and suitability for large-scale energy storage
- experiment: Long-term cycling test | Galvanostatic cycling | params: 880 and 1760 mA g⁻¹ for 1000 cycles; 110 mA g⁻¹ for initial activation | result: Capacity retention of 80% after 250 cycles at 880 mA g⁻¹; decay rate of only 0.015–0.018% per cycle after initial stabilization
  - [experimental result] V/Fe PBA synthesized with HCl shows high crystallinity (XRD, TEM).
  - [experimental result] XRD patterns remain unchanged after 250 cycles, indicating structural integrity.
  - [image description] SEM shows no morphological degradation after cycling.
  - [experimental result] ICP-OES shows low V/Fe dissolution (<1.5% after 250 cycles), preventing active material loss.
  - [experimental result] High capacity retention (80%) and stable coulombic efficiency confirm long-term performance.
  - [deductive reasoning] Thus, optimized processing enables structural stability, which directly enhances long-term performance.
### M5  Structure → Performance
- cause: Presence of amorphous regions surrounding crystalline V/Fe PBA particles
- effect: Increased charge-transfer resistance (Rct) during cycling, contributing to initial capacity fade
- experiment: Electrochemical impedance spectroscopy (EIS) | EIS | params: Frequency range 0.005–100,000 Hz; measured at fully charged state (1.15 V) after cycles 3, 30, 60, 100, 150, 200, 250 | result: Rct sharply increased during early cycles (3–30) then saturated; Rfilm and Re remained stable
  - [image description] TEM shows amorphous regions surrounding crystalline V/Fe PBA particles.
  - [experimental result] EIS reveals sharp increase in Rct during early cycles, while Rfilm and Re remain constant.
  - [experimental result] Rct increase correlates with initial capacity decay (Figure 2A, S3A).
  - [non-referenced_knowledge] Amorphous regions act as resistive interfaces hindering electron/ion transport at electrode-electrolyte boundary.
  - [deductive reasoning] Thus, amorphous structure causes increased Rct, leading to initial capacity loss.
### M6  Property → Performance
- cause: Multiple-electron redox reactions of V and Fe ions (V³⁺/V⁴⁺/V⁵⁺ and Fe²⁺/Fe³⁺)
- effect: High specific capacity (91 mA h g⁻¹) and superior energy density compared to single-metal PBAs
- experiment: Ex situ XANES analysis | X-ray Absorption Near Edge Spectroscopy | params: Fe and V K-edge spectra measured at multiple charge states; compared to reference oxides | result: Both Fe and V ions undergo reversible redox; capacity of ~43 mA h g⁻¹ per single-electron process implies two-electron contribution from V and one from Fe
  - [experimental result] XANES shows systematic shift in both Fe and V K-edges with charge, proving both ions change oxidation state.
  - [experimental result] Measured capacity of 91 mA h g⁻¹ is more than double the theoretical single-electron capacity (~43 mA h g⁻¹).
  - [non-referenced_knowledge] V contributes two redox couples (V³⁺/V⁴⁺ and V⁴⁺/V⁵⁺), Fe contributes one (Fe²⁺/Fe³⁺), totaling three electrons per V₃Fe₂ unit.
  - [deductive reasoning] Thus, multi-electron redox reactions from dual-metal centers explain the high capacity.
