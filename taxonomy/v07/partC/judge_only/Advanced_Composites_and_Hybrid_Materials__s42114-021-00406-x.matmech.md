# MatMech content for Advanced_Composites_and_Hybrid_Materials/s42114-021-00406-x (judge only; not shown to staff)
- material: PLA/PCL/4PIL/8CNT  elements: ['C', 'H', 'O', 'N', 'P']  category: ['Polymer', 'Composite Material', 'Nanomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Melt blending with controlled blending time (2, 4, 6, 8 min) in a HAAKE torque rheometer at 180°C and 50 rpm, followed by hot-pressing at 180°C and 5 MPa
- **Structure**: Selective localization of PIL-modified CNTs at the co-continuous PLA/PCL interface and PCL phase, with refined co-continuous phase structure and improved interfacial compatibilization
- **Properties**: Electrical conductivity–electrical property, tensile strength–mechanical property, elongation at break–mechanical property
- **Performance**: EMI shielding effectiveness up to 41 dB with dominant absorption mechanism (SE_A > SE_R)
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Melt blending with controlled blending time (2, 4, 6, 8 min) in a HAAKE torque rheometer at 180°C and 50 rpm
- effect: Selective localization of PIL-modified CNTs at the co-continuous PLA/PCL interface and PCL phase, with refined co-continuous phase structure
- experiment: Melt blending with varying time | Melt blending in HAAKE torque rheometer | params: Blending times: 2, 4, 6, 8 min; temperature: 180°C; rotor speed: 50 rpm | result: CNTs migrate from PLA to PCL phase; interfacial localization peaks at 6 min; co-continuous phase size decreases with blending time
  - [experimental result] CNTs are initially premixed with PLA during the first 4 min of blending.
  - [referenced knowledge] The viscosity ratio of PLA to PCL is ~16, making PCL the thermodynamically preferred phase for CNTs (wetting coefficient = 0.58).
  - [image description] FE-SEM images show CNTs migrating from PLA to PCL phase with increasing blending time from 2 to 8 min.
  - [non-referenced_knowledge] PILs contain MEPGMA segments with high affinity for both PLA and PCL, expanding the interfacial layer and acting as compatibilizers.
  - [non-referenced_knowledge] The π–π interaction between imidazole groups of PILs and CNTs enhances CNT dispersion and interfacial anchoring.
  - [deductive reasoning] Thus, blending time controls migration kinetics, and PILs enable thermodynamic stabilization of CNTs at the interface, forming a refined co-continuous structure.
### M2  Structure → Properties
- cause: Selective localization of PIL-modified CNTs at the PLA/PCL interface and PCL phase, forming a continuous conductive network
- effect: Significantly increased electrical conductivity and enhanced mechanical properties (tensile strength and elongation at break)
- experiment: Electrical conductivity measurement | Four-probe tester | params: Sample dimensions: 10×10×1 mm³; measurement at room temperature | result: PLA/PCL/4PIL/8CNT-6m composite shows highest conductivity (2.48 S/m); 50-fold increase over PLA/PCL/8CNT-6m (0.046 S/m)
  - [image description] CNTs are selectively localized at the PLA/PCL interface at 6 min blending time, forming a 3D conductive network.
  - [experimental result] Electrical conductivity peaks at 6 min blending for PLA/PCL/4PIL/8CNT (2.48 S/m), significantly higher than other blends.
  - [non-referenced_knowledge] PILs improve dispersion and reduce CNT agglomeration, enhancing interfacial connectivity.
  - [experimental result] Tensile elongation at break reaches maximum (135.4%) at 6 min blending, indicating improved ductility from interfacial compatibilization.
  - [experimental result] Storage modulus increases with blending time up to 6 min, reflecting restricted polymer chain mobility due to interfacial CNT network.
  - [deductive reasoning] Thus, interfacial CNT localization simultaneously improves electrical and mechanical properties via percolation and stress transfer enhancement.
### M3  Properties → Performance
- cause: High electrical conductivity (2.48 S/m) from interfacial CNT network and enhanced conductive loss
- effect: EMI shielding effectiveness reaches 41 dB with dominant absorption mechanism (SE_A > SE_R)
- experiment: EMI shielding effectiveness measurement | Vector network analyzer (N5247A, Agilent) | params: Frequency range: 8.2–12.4 GHz; sample size: 10×10×1 mm³ | result: PLA/PCL/4PIL/8CNT-6m achieves maximum EMI SE of 41 dB; SE_A > SE_R, indicating absorption-dominated shielding
  - [experimental result] Electrical conductivity of PLA/PCL/4PIL/8CNT-6m reaches 2.48 S/m due to interfacial CNT network.
  - [experimental result] EMI SE peaks at 41 dB for the same composite, matching the peak conductivity value.
  - [image description] SE_A (absorption) is significantly higher than SE_R (reflection) for all samples, indicating absorption is the dominant mechanism.
  - [non-referenced_knowledge] High conductivity enables multiple internal reflections and Joule heating of EM waves.
  - [referenced knowledge] Interfacial network improves impedance matching, allowing EM waves to enter rather than reflect.
  - [deductive reasoning] Thus, the conductive network formed by interfacial CNTs enables efficient EM wave absorption, achieving high EMI shielding performance.
### M4  Processing → Properties
- cause: Melt blending time of 6 min with PIL modification
- effect: Optimal electrical conductivity (2.48 S/m) and mechanical elongation at break (135.4%)
- experiment: Electrical conductivity and tensile testing | Four-probe tester and universal testing machine | params: Blending times: 2, 4, 6, 8 min; CNTs: 8 wt%; PILs: 4 wt% | result: Max conductivity (2.48 S/m) and elongation at break (135.4%) both occur at 6 min blending time
  - [image description] At 6 min blending, CNTs are predominantly localized at the PLA/PCL interface, forming a continuous conductive network.
  - [experimental result] Electrical conductivity and elongation at break both reach maximum values at 6 min blending.
  - [experimental result] At 8 min blending, CNTs migrate deeper into PCL phase, breaking the interfacial network and reducing conductivity and ductility.
  - [non-referenced_knowledge] Interfacial CNTs enhance both electron transport and interfacial adhesion.
  - [deductive reasoning] Thus, 6 min blending is the processing optimum for achieving peak electrical and mechanical properties.
