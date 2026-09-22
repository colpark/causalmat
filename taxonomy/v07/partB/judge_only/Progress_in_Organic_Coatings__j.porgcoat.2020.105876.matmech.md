# MatMech content for Progress_in_Organic_Coatings/j.porgcoat.2020.105876 (judge only; not shown to staff)
- material: polyurea-urethane/epoxy blend  elements: ['C', 'H', 'O', 'S', 'N']  category: ['Polymer', 'Composite Material', 'Nanomaterial', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Blending of furan-terminated thermoplastic polyurea-urethane (FTPU) with epoxy oligomers and bis(4-maleimidophenyl)methane (BMI), followed by curing at 60°C for 24 h
- **Structure**: Nanoscale phase-separated epoxy domains induced by Diels-Alder reaction between furan and maleimide groups; reversible disulfide bonds in FTPU main chains; dynamic interfacial bonding between FTPU and epoxy domains
- **Properties**: tensile strength–mechanical property, tensile modulus–mechanical property, pencil hardness–mechanical property, storage modulus–mechanical property, glass transition temperature–thermal property
- **Performance**: shape-memory effect with 91% fixation ratio and 99% recovery ratio, self-healing efficiency of 80% confirmed by tensile tests, anti-contamination and anti-corrosion performance in 3.5% NaCl and red dye solution
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Blending of furan-terminated thermoplastic polyurea-urethane (FTPU) with epoxy oligomers and bis(4-maleimidophenyl)methane (BMI), followed by curing at 60°C for 24 h
- effect: Nanoscale phase-separated epoxy domains induced by Diels-Alder reaction between furan and maleimide groups; reversible disulfide bonds in FTPU main chains; dynamic interfacial bonding between FTPU and epoxy domains
- experiment: FTIR spectroscopy of FTPU/epoxy blends | Fourier Transform Infrared Spectroscopy | params: Analysis of FT5BE5 at different temperatures (25°C, 90°C, 130°C) | result: New peak at 1774 cm⁻¹ confirms DA adduct formation; retro-DA at 130°C regenerates furan and maleimide peaks (1146 cm⁻¹ and 696 cm⁻¹)
  - [experimental result] FTPU contains furan end-groups and epoxy oligomers contain dangling furan groups.
  - [experimental result] BMI contains maleimide groups that react with furan groups via Diels-Alder reaction.
  - [experimental result] FTIR shows a new peak at 1774 cm⁻¹, assigned to DA adduct, confirming covalent bonding between components.
  - [image description] SEM and AFM images reveal nanoscale phase-separated domains in blends but not in pure FTPU.
  - [experimental result] Reducing BMI content (FT5B0.5E5) leads to less distinct phase separation, indicating crosslinking density controls domain formation.
  - [referenced knowledge] Diels-Alder reactions are known to induce phase separation in polymer blends by creating thermodynamically incompatible crosslinked domains.
  - [deductive reasoning] Therefore, curing promotes DA reactions that generate phase-separated epoxy domains and interfacial bonds via covalent crosslinking.
### M2  Structure → Properties
- cause: Nanoscale phase-separated epoxy domains induced by Diels-Alder reaction between furan and maleimide groups; reversible disulfide bonds in FTPU main chains; dynamic interfacial bonding between FTPU and epoxy domains
- effect: Tensile strength increased from 7.8 MPa to 15.2 MPa; tensile modulus increased from 71 MPa to 209 MPa; pencil hardness improved from 3B-2B to F–H; storage modulus increased; glass transition temperature shifted
- experiment: Tensile test and pencil hardness measurement | Tensile Test | params: Strain rate of 50 mm/min; dumbbell specimens from solvent-cast films | result: Tensile strength doubled (7.8 → 15.2 MPa); modulus increased from 71 to 209 MPa; pencil hardness improved from 3B-2B to F–H
  - [experimental result] FT5BE5 exhibits a tensile modulus of 209 MPa, nearly triple that of pure FTPU (71 MPa).
  - [image description] AFM and SEM show well-defined nanoscale epoxy domains in FT5BE5.
  - [experimental result] FTIR confirms strong interfacial bonding via DA adducts between FTPU and epoxy.
  - [non-referenced_knowledge] Rigid epoxy domains act as reinforcing fillers in the soft FTPU matrix.
  - [non-referenced_knowledge] Strong interfacial bonding prevents debonding and enables efficient stress transfer.
  - [deductive reasoning] Thus, the combination of rigid domains and interfacial bonding increases tensile strength, modulus, and pencil hardness.
### M3  Structure → Performance
- cause: Nanoscale phase-separated epoxy domains induced by Diels-Alder reaction between furan and maleimide groups; reversible disulfide bonds in FTPU main chains; dynamic interfacial bonding between FTPU and epoxy domains
- effect: Shape-memory effect with 91% fixation ratio and 99% recovery ratio; self-healing efficiency of 80% confirmed by tensile tests; anti-contamination and anti-corrosion performance in 3.5% NaCl and red dye solution
- experiment: Shape-memory effect test | Tensile Tester with thermal cycling | params: Strain of 50% at room temperature, fixed for 3 min, heated to 130°C for recovery | result: Fixation ratio (Rf) = 91%; recovery ratio (Rr) = 99%
  - [experimental result] FTPU contains disulfide bonds that allow dynamic exchange and chain mobility.
  - [structure description] Epoxy domains are crosslinked via DA bonds and act as fixed netpoints for shape-memory.
  - [experimental result] Cold drawing fixes strain (Rf = 91%), and heating to 130°C triggers recovery (Rr = 99%).
  - [image description] SEM shows crack width reduction after 130°C heating, confirming shape-memory-assisted closure.
  - [experimental result] Healing efficiency (RH = 80.4%) is achieved after 130°C + 60°C treatment, indicating both closure and chemical repair.
  - [non-referenced_knowledge] Retro-DA at 130°C increases mobility, allowing disulfide exchange and re-entanglement for healing.
  - [deductive reasoning] Thus, phase-separated domains enable shape-memory closure, while disulfide bonds enable chemical healing.
### M4  Processing → Performance
- cause: Blending of furan-terminated thermoplastic polyurea-urethane (FTPU) with epoxy oligomers and bis(4-maleimidophenyl)methane (BMI), followed by curing at 60°C for 24 h
- effect: Self-healing efficiency of 80% confirmed by tensile tests; anti-contamination and anti-corrosion performance in 3.5% NaCl and red dye solution
- experiment: Self-healing efficiency test and corrosion resistance test | Tensile Test and Immersion Test | params: Crack induced by razor blade; healed at 130°C for 30 min + 60°C for 12 h; immersed in 3.5% NaCl or red dye for 5–7 days | result: Healing efficiency RH = 80.4%; no visible corrosion or dye penetration in healed coatings
  - [experimental result] Processing involves blending FTPU and epoxy oligomers with BMI, followed by curing.
  - [experimental result] Curing induces DA reactions that form phase-separated epoxy domains and interfacial bonds.
  - [experimental result] FTPU contains disulfide bonds that enable dynamic exchange.
  - [non-referenced_knowledge] Shape-memory effect allows crack closure at 130°C without manual intervention.
  - [non-referenced_knowledge] Subsequent heating at 60°C allows disulfide exchange and DA reformation to heal the crack chemically.
  - [experimental result] Healed coatings resist NaCl and dye penetration, proving restored barrier function.
  - [deductive reasoning] Thus, processing directly enables the combined shape-memory and chemical healing that delivers performance.
