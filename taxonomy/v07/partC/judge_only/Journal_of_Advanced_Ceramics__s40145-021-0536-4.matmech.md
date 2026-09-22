# MatMech content for Journal_of_Advanced_Ceramics/s40145-021-0536-4 (judge only; not shown to staff)
- material: PcBN  elements: ['B', 'C', 'Al', 'Si', 'N', 'Ti', 'Zr', 'O']  category: ['Composite Material', 'Ceramic', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Spark plasma sintering (SPS) at 1400–1700 °C with a heating rate of 125 °C/min and 35 MPa axial pressure
- **Structure**: SiAlON phase as binder with uniform distribution of cBN particles; formation of TiN, AlN, TiB₂, and AlB₂ in S3; low porosity (<0.8%) in S1 and S2; absence of hBN phase in S1 and S2
- **Properties**: flexural strength–mechanical property, fracture toughness–mechanical property, Vickers hardness–mechanical property
- **Performance**: maintenance of high flexural strength (467 ± 18 MPa) and fracture toughness (5.13 ± 0.40 MPa·m¹/²) at 800 °C during high-temperature machining
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Spark plasma sintering (SPS) at 1400–1700 °C with a heating rate of 125 °C/min and 35 MPa axial pressure
- effect: Formation of SiAlON phase (β-SiAlON and O'-SiAlON) in Sample S1 due to reaction between Si₃N₄, Al₂O₃, and AlN; suppression of cBN to hBN phase transformation; low apparent porosity (<0.8%) and uniform distribution of cBN particles surrounded by binder phases
- experiment: SPS sintering of PcBN composites | Spark plasma sintering | params: Temperature: 1400–1700 °C; heating rate: 125 °C/min; axial pressure: 35 MPa; holding time: 10 min; vacuum environment | result: Sample S1 achieved 0.44% porosity at 1600 °C; no hBN detected by XRD; Sample S3 showed high porosity (7.68%) and phase transformation products (TiN, AlN, TiB₂, AlB₂)
  - [experimental result] SPS was performed at 1400–1700 °C with a heating rate of 125 °C/min and 35 MPa pressure.
  - [experimental result] XRD results show new phases (β-SiAlON, O'-SiAlON) in Sample S1, formed by reaction of Si₃N₄, Al₂O₃, and AlN.
  - [experimental result] No hBN phase was detected in S1 and S2, indicating suppression of cBN decomposition.
  - [referenced knowledge] SPS has high heating rate and short holding time, which reduces exposure of cBN to high temperatures and inhibits phase transformation.
  - [image description] BSE images show uniform distribution of cBN particles surrounded by binder phases in S1 and S2, with no interfacial defects.
  - [experimental result] Low apparent porosity (<0.8%) in S1 and S2 correlates with high bulk density and improved mechanical integrity.
  - [non-referenced_knowledge] Dense microstructure with strong interfacial bonding enhances load transfer from matrix to hard cBN particles.
  - [deductive reasoning] Thus, SPS processing leads to SiAlON-bonded, low-porosity microstructures with preserved cBN integrity.
### M2  Structure → Properties
- cause: SiAlON phase as binder with uniform cBN distribution and low porosity (<0.8%) in Sample S1
- effect: Optimal flexural strength (465 ± 29 MPa) and fracture toughness (5.62 ± 0.37 MPa·m¹/²) at 1600 °C; high Vickers hardness (15.59 ± 0.54 GPa)
- experiment: Three-point flexural and SENB tests | Mechanical testing | params: Span: 20 mm (flexural), 16 mm (toughness); crosshead speed: 0.5 mm/min (flexural), 0.05 mm/min (toughness); load: 500 g for 5 s (HV) | result: S1: flexural strength 465 ± 29 MPa, fracture toughness 5.62 ± 0.37 MPa·m¹/², hardness 15.59 ± 0.54 GPa; S2 and S3 showed significantly lower values
  - [experimental result] Sample S1 exhibits the highest flexural strength and fracture toughness among all samples.
  - [image description] Fracture surfaces show both cBN particle pullout and brittle fracture of SiAlON phase.
  - [image description] Crack propagation paths cross both cBN particles and SiAlON phases, with deflection at interfaces.
  - [referenced knowledge] Mixed transgranular and intergranular fracture increases energy dissipation compared to pure interfacial failure.
  - [non-referenced_knowledge] Strong bonding between cBN and SiAlON prevents interfacial debonding and enables effective load transfer.
  - [non-referenced_knowledge] Low porosity minimizes flaws that initiate cracks.
  - [deductive reasoning] Thus, the SiAlON-based structure with dense, well-bonded microstructure maximizes mechanical properties.
### M3  Structure → Properties
- cause: Al₂O₃–ZrO₂(3Y) binder system in Sample S2 with high thermal expansion mismatch and no chemical reaction
- effect: Low flexural strength (145 ± 7 MPa) and fracture toughness (3.52 ± 0.21 MPa·m¹/²) despite low porosity
- experiment: Three-point flexural and SENB tests | Mechanical testing | params: Span: 20 mm (flexural), 16 mm (toughness); crosshead speed: 0.5 mm/min (flexural), 0.05 mm/min (toughness) | result: S2 flexural strength and fracture toughness are significantly lower than S1, despite low porosity (0.74%)
  - [experimental result] Sample S2 has low porosity (0.74%) but exhibits the lowest flexural strength and fracture toughness.
  - [experimental result] XRD shows no new phases in S2, indicating no chemical bonding between Al₂O₃, ZrO₂, and cBN.
  - [image description] Fracture surfaces show extensive cBN pullout and deep pits, suggesting weak adhesion.
  - [image description] Crack propagation is predominantly along cBN–Al₂O₃ interfaces, not through grains.
  - [referenced knowledge] Thermal expansion coefficient of Al₂O₃ (7.2 × 10⁻⁶ K⁻¹) is much higher than cBN (1.2–3.4 × 10⁻⁶ K⁻¹), generating high interfacial stress.
  - [non-referenced_knowledge] Weak interfaces allow rapid crack propagation with minimal energy absorption.
  - [deductive reasoning] Thus, despite high density, the absence of chemical bonding and thermal mismatch degrade mechanical properties.
### M4  Structure → Properties
- cause: Al–Ti metal binder system in Sample S3 with high porosity (7.68%) and cBN agglomeration
- effect: Low flexural strength and fracture toughness despite high bulk density; inferior mechanical properties
- experiment: Archimedes density and mechanical testing | Density and mechanical measurement | params: Density via ISO 18754:2003; flexural and fracture tests at RT | result: S3 has highest bulk density (3.49 g/cm³) but highest porosity (7.68%) and lowest flexural strength and fracture toughness
  - [experimental result] Sample S3 has the highest bulk density (3.49 g/cm³) but also the highest apparent porosity (7.68%).
  - [image description] BSE images show cBN particle agglomeration and non-uniform distribution.
  - [image description] Fracture surfaces reveal visible pores and cracks.
  - [image description] Cracks propagate through binder phases (TiN, AlN) rather than cBN particles.
  - [referenced knowledge] Metal phases (Al, Ti) form reaction products (TiN, AlN) with high hardness but lower toughness than SiAlON.
  - [non-referenced_knowledge] Porosity and agglomeration reduce effective load-bearing cross-section and create crack initiation sites.
  - [deductive reasoning] Thus, despite high density, the microstructure is flawed, leading to poor mechanical performance.
### M5  Properties → Performance
- cause: High flexural strength (465 ± 29 MPa) and fracture toughness (5.62 ± 0.37 MPa·m¹/²) of Sample S1 at room temperature
- effect: Maintenance of high flexural strength (467 ± 18 MPa) and fracture toughness (5.13 ± 0.40 MPa·m¹/²) at 800 °C during high-temperature machining
- experiment: High-temperature mechanical testing | Flexural and fracture toughness tests at 400, 600, and 800 °C | params: Tested in furnace; 5 min hold at target temperature; same test parameters as RT | result: Flexural strength increases slightly to 545 ± 37 MPa at 600 °C and remains high at 467 ± 18 MPa at 800 °C; fracture toughness decreases only 8.7% to 5.13 ± 0.40 MPa·m¹/² at 800 °C
  - [experimental result] Sample S1 exhibits the highest room-temperature flexural strength and fracture toughness.
  - [experimental result] High-temperature tests show flexural strength remains above 450 MPa and fracture toughness is only 8.7% lower at 800 °C.
  - [image description] Fracture surfaces at 800 °C show similar features to RT: cBN pullout and SiAlON brittle fracture.
  - [image description] Crack propagation still involves both phases, indicating retained interfacial bonding.
  - [referenced knowledge] SiAlON has known high-temperature strength and thermal shock resistance.
  - [non-referenced_knowledge] The binder–cBN interface remains stable, preventing degradation at high temperatures.
  - [deductive reasoning] Thus, the mechanical properties of S1 are preserved at 800 °C, enabling reliable high-temperature performance.
