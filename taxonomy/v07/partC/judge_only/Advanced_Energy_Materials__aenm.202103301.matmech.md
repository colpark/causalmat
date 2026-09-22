# MatMech content for Advanced_Energy_Materials/aenm.202103301 (judge only; not shown to staff)
- material: Ni-WO₂  elements: ['Ni', 'W', 'O', 'H']  category: ['Nanomaterial', 'Ceramic', 'Crystalline Material']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Hydrothermal synthesis followed by annealing in Ar/H₂ (95/5) gas at 600 °C for 2 h
- **Structure**: Monoclinic WO₂ nanowires with Ni dopants substituting W sites, elongated W-W/Ni bond length, and reduced W 5d orbital occupancy
- **Properties**: Hydrogen adsorption Gibbs free energy (ΔG_H*)–electrochemical property, Tafel slope–electrochemical property, overpotential–electrochemical property
- **Performance**: Overpotential of 41 mV at -10 mA cm⁻² and stable operation for 100 h at -100 mA cm⁻² in 1.0 M KOH for hydrogen evolution reaction
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Hydrothermal synthesis followed by annealing in Ar/H₂ (95/5) gas at 600 °C for 2 h
- effect: Formation of monoclinic WO₂ nanowires with Ni dopants substituting W sites, elongated W-W/Ni bond length, and porous morphology
- experiment: Synthesis of Ni-WO₂ nanowires | Hydrothermal synthesis and annealing | params: Hydrothermal at 165 °C for 6 h, followed by annealing in Ar/H₂ (95/5) at 600 °C for 2 h | result: Formation of ordered porous nanowire arrays with homogeneous Ni distribution
  - [experimental result] Ni-WO₂ nanowires are synthesized via hydrothermal growth on carbon paper using ammonium paratungstate and nickel nitrate.
  - [experimental result] Subsequent annealing in Ar/H₂ at 600 °C transforms the precursor into a porous nanowire structure with improved crystallinity.
  - [image description] SEM and TEM images confirm the formation of ordered nanowires with ~50 nm diameter and ~1 μm length after annealing.
  - [image description] HRTEM shows lattice fringes of 0.343 nm corresponding to the (011) plane of monoclinic WO₂, indicating phase retention.
  - [non-referenced_knowledge] Reductive annealing promotes oxygen vacancy formation and dopant incorporation into the WO₂ lattice, altering local coordination.
  - [deductive reasoning] Thus, the processing conditions directly yield a structured Ni-doped WO₂ nanowire with modified metal-metal bonding environment.
### M2  Structure → Property
- cause: Ni dopants substituting W sites, elongated W-W/Ni bond length, and reduced W 5d orbital occupancy
- effect: Weakened hydrogen adsorption strength (ΔG_H* = -0.44 eV) and reduced Tafel slope (79 mV dec⁻¹)
- experiment: DFT calculations of hydrogen adsorption energy | Density Functional Theory (DFT) simulation | params: CASTEP code, PBE functional, 450 eV cutoff, 1×2×1 k-point mesh for (011) surface | result: W-Ni site exhibits ΔG_H* = -0.44 eV, closest to thermoneutral value (0 eV), while W-W site is too strong (-1.21 eV)
  - [experimental result] DFT calculations show that Ni doping introduces anti-bonding orbital filling in W-M bonds, reducing bond order.
  - [experimental result] Projected density of states (PDOS) reveal linear decoupling between W 5d and Ni 3d orbitals upon doping.
  - [experimental result] Mulliken bond order of W-Ni (0.25) is significantly lower than W-W (0.61), indicating weaker interaction.
  - [non-referenced_knowledge] The reduced W 5d occupancy shifts the d-band center away from Fermi level, weakening H* adsorption.
  - [image description] Figure 1e shows ΔG_H* for W-Ni is -0.44 eV, near the thermoneutral optimum for HER.
  - [deductive reasoning] Thus, Ni-induced d-d orbital modulation optimizes hydrogen adsorption energy, a key catalytic property.
### M3  Structure → Property
- cause: Ni doping induces longer W-W/Ni bond length and charge redistribution around W sites
- effect: Reduced work function (from 5.39 eV to 5.25 eV) and enhanced interfacial charge-transfer kinetics (Rct from 379 Ω to 51 Ω)
- experiment: XPS and XANES/EXAFS measurements | X-ray Photoelectron Spectroscopy (XPS), X-ray Absorption Near Edge Structure (XANES), Extended X-ray Absorption Fine Structure (EXAFS) | params: W L₃-edge XANES, W 4f XPS, FT-EXAFS fitting, wavelet transform analysis | result: W 4f peak shifts +0.2 eV to higher binding energy; W-W/Ni bond length increases from 2.44 Å to 2.53 Å; EXAFS confirms longer coordination
  - [experimental result] XPS shows W 4f₇/₂ binding energy shifts +0.2 eV to higher values after Ni doping, indicating electron depletion at W sites.
  - [experimental result] XANES confirms oxidized electronic structure of W in Ni-WO₂, consistent with reduced d-band occupancy.
  - [experimental result] EXAFS and WT analysis reveal increased W-W/Ni bond length from 2.44 Å to 2.53 Å.
  - [image description] Electron density difference maps show reduced charge accumulation between Ni and W atoms.
  - [non-referenced_knowledge] Lower electron density at W sites reduces the energy barrier for electron transfer to adsorbed species.
  - [experimental result] Ultraviolet photoelectron spectroscopy confirms work function decreases from 5.39 eV to 5.25 eV.
  - [experimental result] EIS shows charge-transfer resistance drops from 379 Ω to 51 Ω, indicating faster kinetics.
  - [deductive reasoning] Thus, structural changes induced by Ni doping enhance charge transfer properties critical for HER.
### M4  Property → Performance
- cause: Optimized hydrogen adsorption (ΔG_H* = -0.44 eV), low Tafel slope (79 mV dec⁻¹), and low charge-transfer resistance (51 Ω)
- effect: Overpotential of 41 mV at -10 mA cm⁻² and stable operation for 100 h at -100 mA cm⁻² in 1.0 M KOH
- experiment: Linear sweep voltammetry (LSV) and chronopotentiometry | Electrochemical performance testing | params: 1.0 M KOH, scan rate 5 mV s⁻¹, 90% IR compensation, current density -10 to -100 mA cm⁻² | result: Ni-WO₂/NF achieves η₁₀ = 41 mV and η₁₀₀ = 112 mV; maintains stability over 100 h at -100 mA cm⁻²
  - [experimental result] DFT predicts W-Ni site has ΔG_H* = -0.44 eV, closest to thermoneutral value among all M-WO₂ variants.
  - [experimental result] LSV measurements confirm Ni-WO₂/CP has lowest overpotential (83 mV at -10 mA cm⁻²) among all doped samples.
  - [experimental result] Tafel slope of Ni-WO₂/CP is 79 mV dec⁻¹, significantly lower than WO₂ (127 mV dec⁻¹), indicating faster HER kinetics.
  - [experimental result] EIS shows Ni-WO₂ has Rct of 51 Ω, nearly 7.5x lower than pure WO₂ (379 Ω), enabling efficient charge transfer.
  - [experimental result] When Ni-WO₂ is grown on nickel foam (NF), overpotential drops further to 41 mV due to improved conductivity and mass transport.
  - [experimental result] Chronopotentiometry shows no significant degradation after 100 h at -100 mA cm⁻², confirming structural and catalytic stability.
  - [deductive reasoning] Thus, the optimized electronic and structural properties directly enable superior HER performance.
