# MatMech content for Journal_of_Advanced_Ceramics/s40145-021-0537-3 (judge only; not shown to staff)
- material: PZT/PVDF  elements: ['C', 'H', 'F', 'Pb', 'Zr', 'Ti', 'O']  category: ['Composite Material', 'Polymer', 'Ceramic', 'Nanomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Electrospinning followed by laminating under 15 MPa at 30 °C
- **Structure**: Porous, multi-layered structure with highly oriented PZT/PVDF fibers and enhanced β-phase content in PVDF
- **Properties**: tensile strength–mechanical property, Young’s modulus–mechanical property, elongation at break–mechanical property, output voltage–electrical property, output power–electrical property, sensitivity–electrical property
- **Performance**: High-efficiency mechanical energy harvesting from human motions (e.g., finger pressing, fist beating) with stable output over 3000 cycles and ability to light 21 LEDs or charge capacitors
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Electrospinning of PZT/PVDF solution under a constant voltage of 11.20 kV with a rotating collector at 3000 rpm and laminating the fiber membranes under 15 MPa at 30 °C
- effect: Formation of a porous, multi-layered structure with highly oriented PZT/PVDF fibers, surface fibers compressed for higher density, and internal fibers remaining separated
- experiment: Fiber film fabrication via laminating | Mechanical compression | params: 15 MPa pressure, 30 °C, 60 min, 2–12 layers of electrospun membranes | result: Fiber films with thicknesses of ~40 to ~220 μm achieved; no interface observed in cross-section, indicating good layer adhesion
  - [experimental result] Electrospinning was performed with a rotating collector at 3000 rpm, producing highly oriented PZT/PVDF fibers.
  - [image description] SEM images show aligned fibers with uniform distribution of PZT particles (Fig. 2a, a1–a4).
  - [non-referenced_knowledge] Aligned fibers are easier to compress and enhance piezoelectric output due to uniform β-phase orientation.
  - [experimental result] Laminating 2–12 layers under 15 MPa at 30 °C compresses surface fibers while preserving internal porosity.
  - [image description] Cross-section SEM (Fig. 3c) shows no interface between layers, confirming effective bonding without fiber damage.
  - [deductive reasoning] This structure increases surface fiber density and preserves internal voids, enhancing bound charge density and stress transfer.
### M2  Processing → Structure
- cause: Electrospinning with PZT particles embedded in PVDF solution under high electric field
- effect: Enhanced β-phase content in PVDF due to polarization and stretching during electrospinning
- experiment: XRD and FTIR analysis of PVDF phases | X-ray diffraction (XRD), Fourier-transform infrared spectroscopy (FTIR) | params: Cu Kα radiation, 15°–25° 2θ range; ATR mode, 700–1500 cm⁻¹ | result: In fiber films, α-phase peak at 18.8° disappears; β-phase peak at 20.6° emerges and intensifies with PZT content; FTIR shows enhanced β-phase peaks at 840 and 1430 cm⁻¹
  - [experimental result] Electrospinning applies a 11.20 kV electric field and fiber stretching, which promotes chain alignment.
  - [experimental result] XRD shows disappearance of α-phase peak (18.8°) and shift of β-phase peak to 20.6° in fiber films vs. cast films.
  - [experimental result] FTIR confirms enhanced β-phase absorption at 840 and 1430 cm⁻¹ in fiber films.
  - [non-referenced_knowledge] PZT particles have polarized surfaces with positive/negative charges that attract -CH₂ and -CF₂ groups of PVDF.
  - [deductive reasoning] This charge interaction facilitates PVDF chain alignment and stabilizes the polar β-phase.
  - [inductive reasoning] Hence, electrospinning with PZT doping significantly increases β-phase content in PVDF.
### M3  Structure → Properties
- cause: Porous, multi-layered structure with highly oriented fibers and enhanced β-phase content
- effect: High output voltage (62.0 V), high output power (136.9 μW), and high sensitivity (12.4 V·N⁻¹)
- experiment: Piezoelectric output measurement under 5 N pressure at 3 Hz | Digital oscilloscope measurement | params: 5 N periodic pressure, 3 Hz frequency, 220 μm film thickness, 10 wt% PZT | result: Output voltage of 62.0 V and power of 136.9 μW; sensitivity of 12.4 V·N⁻¹
  - [image description] The laminated structure has dense surface fibers and separated internal fibers (Fig. 3d,e).
  - [image description] KPFM shows stronger surface potential in fiber films than cast films, indicating higher bound charge density (Fig. 5d,f).
  - [experimental result] XRD and FTIR confirm high β-phase content (up to 83.16%) due to PZT doping and electrospinning.
  - [non-referenced_knowledge] Polar β-phase dipoles align normal to fiber axis, and pressure compresses the structure, rotating dipoles and generating voltage (Fig. 6a,b).
  - [deductive reasoning] More fibers activated per unit area and higher dipole density lead to increased voltage and power output.
### M4  Structure → Properties
- cause: Porous, multi-layered fiber structure with separated internal fibers and compressed surface fibers
- effect: High flexibility with Young’s modulus of 227.2 MPa and elongation at break of 262.3%
- experiment: Tensile test of f-P0.10 fiber film vs. cast film | Tensile testing | params: Zwick/Roell Z020, 2 mm/min strain rate, perpendicular/parallel to fiber axis | result: Young’s modulus dropped to 227.2 MPa (F⊥fibers) and 499.2 MPa (F//fibers); elongation at break increased to 262.3% vs. 17.7% for cast film
  - [experimental result] Tensile test shows fiber film has Young’s modulus of 227.2 MPa (F⊥fibers), much lower than cast film (1614 MPa).
  - [experimental result] Elongation at break of fiber film is 262.3%, 14.8× higher than cast film’s 17.7%.
  - [image description] The porous internal structure and fiber separation reduce inter-fiber crystalline connectivity.
  - [non-referenced_knowledge] Lower crystallinity increases amorphous regions, which are more deformable and elastic.
  - [deductive reasoning] Thus, the porous multi-layered structure enhances flexibility without sacrificing structural integrity.
### M5  Properties → Performance
- cause: High output voltage (62.0 V), high output power (136.9 μW), and high sensitivity (12.4 V·N⁻¹)
- effect: Ability to light 21 LEDs in series and charge a 1 μF capacitor to 6.4 V within 65 s under human motion
- experiment: LED lighting and capacitor charging test | Circuit performance test | params: Rectifier bridge connected to PENG, 1–47 μF capacitors, finger pressing (5 N, 3 Hz) | result: 21 green LEDs lit directly; 1 μF capacitor charged to 6.4 V in 65 s
  - [experimental result] The f-P0.10 fiber-based PENG outputs 62.0 V and 136.9 μW under 5 N pressure (Fig. 7b,e).
  - [experimental result] Sensitivity is 12.4 V·N⁻¹, 3.4× higher than cast film-based PENG.
  - [non-referenced_knowledge] These values exceed the threshold required to drive LEDs and charge capacitors (typically >5 V and >10 μW).
  - [experimental result] Rectifier circuit converts AC output to DC, charging 1 μF capacitor to 6.4 V in 65 s and lighting 21 LEDs.
  - [experimental result] Stable output over 3000 cycles confirms performance durability under real-world conditions.
  - [deductive reasoning] Thus, the electrical properties translate directly into high-performance energy harvesting capability.
### M6  Processing → Properties
- cause: Laminating process under 15 MPa at 30 °C
- effect: Enhanced piezoelectric sensitivity (12.4 V·N⁻¹) and output power (136.9 μW)
- experiment: Sensitivity and power comparison between fiber and cast films | Piezoelectric output measurement | params: 5 N pressure, 3 Hz, 220 μm thickness, f-P0.10 vs. 10 wt% cast film | result: Fiber film sensitivity: 12.4 V·N⁻¹; power: 136.9 μW; cast film sensitivity: 3.6 V·N⁻¹; power: 21.025 μW
  - [image description] Laminating under 15 MPa compresses surface fibers, increasing their density (Fig. 3d).
  - [image description] Internal fibers remain separated, preserving flexibility while enabling stress transfer to all layers.
  - [non-referenced_knowledge] This structure ensures more fibers are activated under pressure, compared to isolated particles in cast films.
  - [deductive reasoning] Higher stress transfer efficiency leads to greater dipole rotation and higher bound charge density.
  - [experimental result] Resulting in 3.4× higher sensitivity and 6.5× higher power than cast film.
