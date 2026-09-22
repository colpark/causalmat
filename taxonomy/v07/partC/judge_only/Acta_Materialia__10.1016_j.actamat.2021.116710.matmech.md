# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116710 (judge only; not shown to staff)
- material: (1-x)NaNbO3-x(Bi0.5Na0.5)TiO3  elements: ['Na', 'Nb', 'O', 'Bi', 'Ti']  category: ['Ceramic', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Conventional solid-state reaction method
- **Structure**: Multiple AFE phases including orthorhombic P (Pbma), orthorhombic R (Pnma), tetragonal (P4bm), and monoclinic (P2_1) phases
- **Properties**: Dielectric permittivity–electrical property, energy-storage density–electrical property, strain–mechanical property
- **Performance**: Thermally-stable capacitors, dielectric energy storage, large-strain ceramic actuators
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Conventional solid-state reaction method with sintering at optimal temperatures (1000–1150 °C)
- effect: (1-x)NaNbO3-x(Bi0.5Na0.5)TiO3 ceramics exhibit dense and uniform microstructure with varying grain sizes depending on composition
- experiment: Grain morphology observation | Field-emission scanning electron microscopy (FE-SEM) | params: Sintering temperature: 1000–1150 °C for 30 min; sample polishing and thermal etching | result: Pure NN and BNT ceramics have larger grains (~7 μm), while NN-BNT solid solutions have smaller grains (~2–3 μm at x = 0.4 and x = 0.6)
  - [experimental result] Samples were sintered at their optimal temperatures between 1000–1150 °C for 30 min before SEM observation.
  - [image description] SEM images show pure NN and BNT ceramics have relatively large grains (~7 μm), compared to NN-BNT binary solid-solution compositions such as ~2–3 μm at x = 0.4 and x = 0.6.
  - [non-referenced_knowledge] Lower sintering temperatures generally result in smaller grain sizes due to limited atomic diffusion and grain boundary mobility.
  - [deductive reasoning] Therefore, the conventional solid-state reaction method with controlled sintering conditions leads to dense and uniform microstructures with composition-dependent grain sizes.
### M2  Structure → Property
- cause: Orthorhombic P (Pbma) and R (Pnma) antiferroelectric phases in NN-rich compositions
- effect: Sharp dielectric permittivity peak around TP-R ~365 °C indicating phase transition from AFE P to AFE R phase
- experiment: Dielectric permittivity measurement | LCR meter | params: Frequency: 1 kHz; temperature range: room temperature to above phase transition | result: Sharp permittivity peak observed around 365 °C in pure NN ceramic
  - [experimental result] Dielectric permittivity was measured at 1 kHz as a function of temperature for (1-x)NN-xBNT ceramics.
  - [image description] A sharp permittivity peak around TP-R ~365 °C was observed in pure NN ceramic, indicating phase transition from AFE P to AFE R.
  - [referenced knowledge] AFE P phase transforms into AFE R phase at ~365 °C in pure NaNbO3.
  - [non-referenced_knowledge] Phase transitions in perovskite oxides alter polarization symmetry, influencing dielectric properties.
  - [deductive reasoning] Thus, the AFE P phase in NN transforms into AFE R phase upon heating, manifesting as a sharp dielectric peak due to reconfiguration of polar order.
### M3  Property → Performance
- cause: Relaxor AFE P4bm phase in BNT-rich compositions
- effect: Low-hysteresis high strain generation under electric field
- experiment: P-E hysteresis and S-E curve measurements | Ferroelectric testing system with laser interferometric vibrometer | params: Electric field cycling at 10 Hz; unipolar and bipolar measurements | result: Pinched P-E loop and enhanced electrostrain (~0.38%) at x = 0.9 composition
  - [experimental result] P-E hysteresis loops and S-E curves were measured at 10 Hz using a ferroelectric testing system coupled with a laser vibrometer.
  - [image description] Pinched P-E loop and significantly enhanced electrostrain (~0.38%) were observed at x = 0.9, indicating low-hysteresis strain generation.
  - [referenced knowledge] Fast polarization response in relaxor AFEs enables excellent electrostrictive performance.
  - [non-referenced_knowledge] Electrostriction scales with the square of the induced polarization, favoring materials with rapid polarization response.
  - [deductive reasoning] Hence, the relaxor AFE P4bm phase generates low-hysteresis, high-strain output under electric field due to its fast and reversible polarization dynamics.
