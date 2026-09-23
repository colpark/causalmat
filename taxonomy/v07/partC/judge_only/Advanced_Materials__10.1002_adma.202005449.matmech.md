# MatMech content for Advanced_Materials/10.1002_adma.202005449 (judge only; not shown to staff)
- material: MXene (Ti3C2Tx)  elements: ['Ti', 'C', 'T', 'H', 'O', 'S', 'F', 'N', 'P', 'V', 'A', 'L', 'I', 'E', 'M']  category: ['Nanomaterial', 'Composite Material', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Screen printing of aqueous MXene inks
- **Structure**: 2D delaminated structure with large interlayer spacing and parallel alignment of MXene nanosheets
- **Properties**: areal capacitance–electrochemical property, energy density–electrochemical property, conductivity–electrical property
- **Performance**: High voltage output in series (60 V), sensitivity to body movements with fast response time (35 ms)
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Screen printing of aqueous MXene inks with high concentration and shear-thinning behavior
- effect: Formation of parallelly aligned MXene nanosheets with a highly ordered lamellar architecture
- experiment: Rheological measurements and SEM imaging of printed MXene films | Rheometry & SEM | params: Shear rate (0.05–100 s⁻¹), alternating low/high shear rates, cross-sectional SEM imaging | result: H-MXene ink showed high apparent viscosity at low shear rate (3548 Pa·s) and shear-thinning behavior; SEM confirmed parallel alignment of MXene nanosheets after printing.
  - [experimental result] H-MXene ink exhibits high viscosity (3548 Pa·s) at low shear rate and strong shear-thinning behavior.
  - [image description] Cross-sectional SEM images confirm that MXene nanosheets are aligned in-plane after printing.
  - [non-referenced_knowledge] Shear-induced alignment of 2D materials enhances in-plane ion transport.
  - [deductive reasoning] Thus, screen printing leads to parallel alignment of MXene nanosheets due to shear interaction during extrusion.
### M2  Structure → Property
- cause: Parallelly aligned MXene nanosheets with large interlayer spacing (1.2 nm)
- effect: Ultrahigh areal capacitance (1.1 F cm⁻²)
- experiment: Electrochemical testing of MX-MSCs | Cyclic Voltammetry (CV), Galvanostatic Charge-Discharge (GCD) | params: Aqueous H₂SO₄/PVA gel electrolyte, current density 0.4 mA cm⁻² | result: MX-MSCs-10L exhibited areal capacitance of 1108 mF cm⁻², significantly higher than thinner devices.
  - [experimental result] The interlayer spacing of MXene nanosheets is 1.2 nm, allowing facile ion diffusion.
  - [non-referenced_knowledge] Parallel alignment of MXene sheets forms a continuous conductive network with reduced internal resistance.
  - [experimental result] MX-MSCs-10L achieved an areal capacitance of 1108 mF cm⁻², significantly higher than thinner devices.
  - [deductive reasoning] Expanded interlayer spacing and aligned structure enhance ion accessibility and conductivity.
### M3  Property → Performance
- cause: Ultrahigh areal capacitance (1.1 F cm⁻²) and high energy density (13.8 µWh cm⁻²)
- effect: High voltage output in series (60 V)
- experiment: Series connection of 100 MX-MSCs | Electrochemical measurement | params: Serial connection of 100 units, linear geometry | result: 100 tandem MX-MSCs output a record voltage of 60 V.
  - [experimental result] Each MX-MSC delivers ~0.6 V under full charge.
  - [experimental result] Connecting 100 units in series yields a cumulative voltage of 60 V.
  - [non-referenced_knowledge] Uniform performance across cells ensures consistent voltage scaling.
  - [inductive reasoning] Thus, high individual capacitance combined with uniformity enables scalable voltage output in series.
### M4  Processing → Performance
- cause: Screen printing of MXene-based LTO and LFP battery-type inks
- effect: Robust areal energy density (154 µWh cm⁻²) in MX-LIMBs
- experiment: Fabrication and electrochemical testing of MX-LIMBs | Galvanostatic cycling, bending tests | params: LiTFSI ionogel electrolyte, 20–100 µA cm⁻² current densities | result: MX-LIMBs delivered 154 µWh cm⁻² energy density and retained 82% capacity after 1000 cycles.
  - [experimental result] MXene-based LTO and LFP inks were prepared without binders or solvents.
  - [image description] SEM images show uniform distribution of LTO/LFP within MXene matrix.
  - [non-referenced_knowledge] Binder-free construction minimizes dead weight and maximizes active material utilization.
  - [deductive reasoning] Thus, additive-free printing enables high areal energy density and mechanical stability.
### M5  Property → Performance
- cause: High sensitivity and fast response time of MXene hydrogel sensor
- effect: Sensitivity to body movements with response time of 35 ms
- experiment: Sensor response to finger and elbow bending | Electromechanical testing | params: Bending angle variation, vertical pressing | result: Current signal changed by ~12% during finger bending; response time measured at 35 ms.
  - [experimental result] MXene hydrogel sensor showed ~12% current variation during finger bending.
  - [experimental result] Response time was measured as 35 ms under vertical pressing.
  - [non-referenced_knowledge] MXene hydrogel exhibits piezoresistive behavior due to strain-induced changes in MXene network resistance.
  - [deductive reasoning] Therefore, MXene hydrogel converts mechanical strain from body movement into rapid electrical signals.
