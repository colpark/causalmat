# MatMech content for Progress_in_Organic_Coatings/j.porgcoat.2021.106672 (judge only; not shown to staff)
- material: MXene/CeO₂ polyurethane composite coating  elements: ['C', 'H', 'O', 'Ce', 'Ti', 'Cl', 'N']  category: ['Composite Material', 'Polymer', 'Nanomaterial', 'Coatings and Thin Films', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Dopamine self-polymerization on CeO₂ and MXene surfaces, furan modification, grafting with maleimide-capped polyurethane, and curing at 60°C
- **Structure**: Lamellar MXene structure with PDA-coated CeO₂ nanoparticles dispersed in polyurethane matrix; DA dynamic covalent bonds formed between furan-modified fillers and PU chains
- **Properties**: Tensile strength–mechanical property, Young's modulus–mechanical property, thermal stability–thermal property, impedance modulus–electrochemical property
- **Performance**: Superior corrosion resistance in 3.5 wt% NaCl solution for up to 100 days; sunlight-triggered self-healing of scratches with restoration of mechanical and anticorrosive properties
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Dopamine self-polymerization on CeO₂ and MXene surfaces, followed by furan modification and grafting with maleimide-capped polyurethane
- effect: Formation of furan-modified CeO₂ (F-d@Ce) and MXene (F-d@MX) nanoparticles with polydopamine (PDA) coating, enabling covalent DA bonding with polyurethane matrix
- experiment: FTIR and XPS characterization of modified nanoparticles | FTIR spectroscopy, X-ray photoelectron spectroscopy | params: Analysis of F-d@Ce and F-d@MX before and after PU grafting; FTIR peak at 732 cm⁻¹ for furan ring; XPS detection of N1s and Cls peaks | result: FTIR confirmed furan grafting; XPS showed nitrogen and carbon signals from dopamine, proving PDA coating; furan peak disappeared after PU crosslinking, indicating DA bond formation
  - [experimental result] Dopamine hydrochloride was added to CeO₂ and MXene dispersions and stirred for 24 h to form dopamine-coated nanoparticles (d@Ce and d@MX).
  - [experimental result] FTIR spectra showed a peak at 732 cm⁻¹ corresponding to furan ring after furfuryl mercaptan grafting, confirming successful modification.
  - [experimental result] XPS spectra revealed N1s and Cls peaks in F-d@Ce and F-d@MX, proving dopamine incorporation onto nanoparticle surfaces.
  - [image description] SEM images showed roughened surfaces of modified nanoparticles, indicating PDA coating formation.
  - [experimental result] XRD peaks of MXene (006) and (008) disappeared after crosslinking, indicating integration of MXene nanosheets into PU chains.
  - [non-referenced_knowledge] Furan groups on modified nanoparticles can react with maleimide end-groups of PU via Diels-Alder reaction to form covalent crosslinks.
  - [deductive reasoning] Thus, dopamine polymerization and furan modification enable covalent bonding between fillers and PU, forming a structurally integrated composite.
### M2  Structure → Properties
- cause: Lamellar structure of MXene and dispersed PDA-coated CeO₂ nanoparticles within the polyurethane matrix
- effect: Enhanced tensile strength, Young’s modulus, thermal stability, and electrochemical impedance
- experiment: Tensile testing and TGA analysis | Tensile stress-strain test, Thermogravimetric analysis | params: Tested PCM0.5 to PCM5 composites; heating rate 10 K/min from 50 to 800°C under N₂ | result: Tensile strength increased from 8.48 MPa (mPU) to 23.95 MPa (PCM2); T₅% thermal degradation temperature increased from 251°C (mPU) to 301°C (PCM2)
  - [non-referenced_knowledge] MXene has a 2D lamellar structure that increases the diffusion path of corrosive ions through the coating.
  - [referenced knowledge] CeO₂ nanoparticles react with OH⁻ to form insoluble cerium compounds that block cathodic reaction sites.
  - [experimental result] Tensile strength increased from 8.48 MPa (mPU) to 23.95 MPa (PCM2) due to crosslinking and reinforcement by fillers.
  - [experimental result] Thermal degradation temperature (T₅%) increased by ~50°C in PCM2 compared to mPU, indicating enhanced stability from rigid inorganic fillers.
  - [experimental result] EIS impedance modulus at 0.01 Hz reached 1.87×10⁹ Ω cm² for PCM2, far exceeding mPU (9.2×10⁷ Ω cm²), due to combined barrier and inhibition effects.
  - [deductive reasoning] Thus, the lamellar MXene and inhibited CeO₂ in the PU matrix synergistically enhance mechanical, thermal, and electrochemical properties.
### M3  Structure → Performance
- cause: Covalent DA-bonded network with synergistic MXene (barrier) and CeO₂ (inhibition) structures
- effect: Exceptional long-term corrosion resistance (>100 days) and sunlight-triggered self-healing of mechanical and protective functions
- experiment: Electrochemical impedance spectroscopy (EIS) over 100 days immersion | EIS in 3.5 wt% NaCl solution | params: Frequency range 10⁴ to 10⁻² Hz, 10 mV AC amplitude; measured at 1, 30, 60, and 100 days | result: PCM2 maintained impedance >10⁷ Ω cm² at 100 days, while mPU dropped to 212 Ω cm²; PCM2 showed largest capacitive arc in Nyquist plots
  - [experimental result] PCM2 exhibited the highest impedance (1.87×10⁹ Ω cm²) after 1 day immersion due to combined MXene barrier and CeO₂ inhibition.
  - [experimental result] After 100 days, only PCM2 maintained impedance >10⁷ Ω cm², demonstrating superior long-term performance.
  - [experimental result] PDA and MXene have high photothermal conversion efficiency, raising coating temperature to 120°C within 1 min under sunlight (200 mW/cm²).
  - [image description] POM and SEM showed complete healing of scratches after 1 min sunlight exposure, confirming restoration of surface continuity.
  - [experimental result] Stress-strain curves showed >98% recovery of mechanical properties after healing, confirming DA bond reformation.
  - [experimental result] EIS after healing showed no significant drop in impedance, proving restored corrosion resistance.
  - [non-referenced_knowledge] DA bonds are thermally reversible; heating breaks and reforms bonds, enabling autonomous repair.
  - [deductive reasoning] Thus, the structure enables both long-term corrosion protection and sunlight-triggered self-healing performance.
### M4  Processing → Performance
- cause: Curing at 60°C and sunlight-triggered DA bond formation
- effect: Coating achieves high corrosion resistance and rapid self-healing under ambient sunlight
- experiment: Sunlight self-healing test with EIS and stress-strain recovery | Sunlight exposure + EIS + tensile testing | params: Scratched PCM2 exposed to 200 mW/cm² sunlight for 1 min; then tested for mechanical and electrochemical recovery | result: Mechanical properties recovered >98%; corrosion resistance unchanged after healing (EIS impedance >10⁷ Ω cm²)
  - [experimental result] Composite films were cured at 60°C for 24 h to complete PU crosslinking via DA reaction.
  - [experimental result] After artificial scratching, sunlight exposure (200 mW/cm²) for 1 min raised temperature to 120°C, sufficient to reverse DA bonds.
  - [image description] POM and SEM confirmed scratch disappearance after healing.
  - [experimental result] Tensile strength recovered to >98% of original value after one healing cycle.
  - [experimental result] EIS after healing showed impedance values identical to pre-damaged coating, confirming restored corrosion protection.
  - [non-referenced_knowledge] The DA bond network formed during curing is thermally reversible, allowing healing without degradation of performance.
  - [deductive reasoning] Therefore, the processing route (curing + photothermal activation) directly enables high-performance corrosion protection with self-healing capability.
