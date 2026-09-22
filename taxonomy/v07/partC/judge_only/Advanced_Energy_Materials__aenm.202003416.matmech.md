# MatMech content for Advanced_Energy_Materials/aenm.202003416 (judge only; not shown to staff)
- material: Lithium (Li) metal  elements: ['Li', 'Cu']  category: ['Metals and Alloys', 'Nanomaterial', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Application of external pressure (2.0–14.0 MPa) to Li|Cu pouch cells
- **Structure**: Transition from branched, porous Li dendrites to smooth, dense, and stocky morphology; increased space utilization and aspect ratio
- **Properties**: Coulombic efficiency–electrochemical property; average current density–electrochemical property; hydrostatic stress–mechanical property; von Mises stress–mechanical property
- **Performance**: Improved cycle life and reduced short-circuit risk in Li metal pouch cells under optimal external pressure
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Application of external pressure (2.0–14.0 MPa) to Li|Cu pouch cells
- effect: Transition from branched, porous Li dendrites to smooth, dense, and stocky morphology; increased space utilization and aspect ratio
- experiment: Mechano-electrochemical phase field simulation | Computational phase field modeling | params: External pressure ranging from 0 to 14.0 MPa; plating capacity of 0.40 mAh cm⁻²; electrolyte modulus of 1.0 GPa | result: Dendrite morphology shifts from branching to smooth and stocky; space utilization increases from 29.4% to 37.3%; aspect ratio increases from 1.6 to 2.8
  - [experimental result] External pressure is applied to Li|Cu pouch cells ranging from 2.0 to 14.0 MPa.
  - [image description] Simulations show that without external pressure, Li dendrites grow with branching morphology due to electric field concentration at tips.
  - [image description] Under external pressure, hydrostatic pressure in Li dendrites shifts from tensile to compressive, with maximum pressure at dendrite tips.
  - [deductive reasoning] Tip growth is inhibited under compressive stress, while lateral growth is promoted, leading to stockier dendrites.
  - [experimental result] Space utilization increases from 29.4% to 37.3% and aspect ratio increases from 1.6 to 2.8 with pressure, confirming densification.
  - [image description] This morphological change is consistent with experimental SEM images (Figure 1c,d) showing smoother Li deposits under pressure.
### M2  Processing → Property
- cause: Application of external pressure (2.0–14.0 MPa) to Li|Cu pouch cells
- effect: Reduction in average current density and inhibition of electroplating reaction rate
- experiment: Mechano-electrochemical phase field simulation | Computational phase field modeling | params: External pressure from 0 to 14.0 MPa; plating time of 100 s; constant voltage of 0.10 V | result: Average current density decreases from 20.49 to 17.44 mA cm⁻² as pressure increases from 0 to 14.0 MPa; plating capacity drops from 0.51 to 0.41 mAh cm⁻²
  - [non-referenced_knowledge] The phase field model includes a mechanical driving force term f_els' derived from elastic strain energy.
  - [non-referenced_knowledge] Equation (64) shows that the reaction rate ∂ξ/∂t is reduced by the term -f_els'(u, ξ), which increases with external pressure.
  - [experimental result] Simulation results show a decrease in average current density from 20.49 to 17.44 mA cm⁻² as pressure increases from 0 to 14.0 MPa.
  - [experimental result] This reduction deviates from linearity, indicating saturation at higher pressures due to maximum stress confinement.
  - [deductive reasoning] Thus, external pressure acts as a mechanical brake on the electroplating reaction, lowering current density.
### M3  Structure → Performance
- cause: Transition from branched, porous Li dendrites to smooth, dense, and stocky morphology
- effect: Improved Coulombic efficiency and extended cycle life in Li metal pouch cells
- experiment: Li|Cu pouch cell electrochemical testing | Coulombic efficiency and polarization curve measurement | params: Current density of 1.0 mA cm⁻²; capacity of 3.0 mAh cm⁻²; with and without external pressure | result: Coulombic efficiency improves under external pressure; cycle life increases from 60 cycles (pouch without pressure) to significantly longer with pressure
  - [referenced knowledge] Dendritic Li has high specific surface area, promoting irreversible side reactions and dead Li formation.
  - [experimental result] External pressure shapes Li into smooth, dense morphology with higher space utilization and aspect ratio.
  - [non-referenced_knowledge] Reduced surface area decreases electrolyte decomposition and Li loss.
  - [image description] Coulombic efficiency improves under pressure, as shown in Figure 1e.
  - [experimental result] Improved CE and reduced dendrite penetration lead to longer cycle life in pouch cells.
### M4  Processing → Performance
- cause: Application of external pressure (2.0–14.0 MPa) to Li|Cu pouch cells
- effect: Improved cycle life and reduced short-circuit risk in Li metal pouch cells
- experiment: Li|Cu pouch cell cycling test | Electrochemical cycling under controlled pressure | params: Pressure range 0–14.0 MPa; current density 1.0 mA cm⁻²; capacity 3.0 mAh cm⁻² | result: Coulombic efficiency and cycle life both improve with pressure up to a threshold; beyond which mechanical instability increases.
  - [non-referenced_knowledge] External pressure improves Li morphology, reducing dendrite penetration and short-circuit risk.
  - [experimental result] Coulombic efficiency and cycle life increase with pressure up to 10–14 MPa (Figure 1e,f).
  - [image description] However, von Mises stress concentrates at dendrite roots under high pressure, increasing fracture risk.
  - [non-referenced_knowledge] Fracture leads to loss of electrical contact and dead Li, reducing CE.
  - [deductive reasoning] Thus, performance improvement is non-monotonic, with an optimal pressure window.
  - [referenced knowledge] Experimental studies report optimal pressure near 1.2 MPa, consistent with the model’s critical pressure threshold for soft electrolytes.
