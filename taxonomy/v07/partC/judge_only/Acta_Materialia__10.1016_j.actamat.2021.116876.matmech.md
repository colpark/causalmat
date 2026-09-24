# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116876 (judge only; not shown to staff)
- material: Inconel 718  elements: ['Ni', 'Cr', 'Mo', 'Al', 'Ti', 'Fe']  category: ['Metals and Alloys', 'Crystalline Material']
- MST chain: Processing → Structure → Property
## Tetrahedron elements
- **Processing**: Laser powder bed fusion (LPBF) with bidirectional laser scan strategy
- **Structure**: Single-crystal-like microstructure (SCM) with <110> orientation, crystallographic lamellar microstructure (CLM) with <110>-oriented main layer and <100>-oriented sub-layer, and polycrystalline microstructure (PCM)
- **Properties**: Yield strength–mechanical property, Ultimate tensile strength (UTS)–mechanical property, Elongation–mechanical property
- **Performance**: Superior mechanical properties compared to cast-IN718, including simultaneous improvement in strength and ductility
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Laser powder bed fusion (LPBF) with bidirectional laser scan strategy
- effect: Formation of single-crystal-like microstructure (SCM) with <110> orientation in the build direction (BD)
- experiment: Thermal diffusion simulation and SEM-EBSD analysis | Finite element method (FEM), EBSD mapping, SEM imaging | params: Varying laser power (360 W) and scan speed (1400 mm/s), fixed layer thickness (0.040 mm) and hatch spacing (0.080 mm) | result: Simulation showed stable thermal gradient at melt pool bottom; EBSD confirmed <110>//BD SCM formation
  - [experimental result] LPBF parameters (360 W, 1400 mm/s) produced deep melt pools with flat bottoms.
  - [experimental result] Thermal simulations showed stable thermal gradient aligned with BD in SCM condition.
  - [image description] Figure shows columnar grains growing across multiple melt pools with <110> orientation.
  - [referenced knowledge] Epitaxial growth is favored when solidification follows heat-flow direction.
  - [deductive reasoning] Thus, SCM forms due to epitaxial growth guided by stable heat flow from flat-bottomed melt pools.
### M2  Processing → Structure
- cause: Laser powder bed fusion (LPBF) with bidirectional laser scan strategy
- effect: Formation of crystallographic lamellar microstructure (CLM) with alternating <110>-oriented main layer and <100>-oriented sub-layer
- experiment: Melt pool curvature measurement and texture analysis | Optical microscopy, EBSD, finite element modeling | params: High laser power (360 W), low scan speed (1000 mm/s), fixed hatch spacing (0.080 mm) | result: Measured melt pool curvature of 39.5 μm; EBSD showed alternating <110> and <100> layers
  - [experimental result] CLM condition used 360 W laser power and 1000 mm/s scan speed producing deep melt pools.
  - [experimental result] Curvature measurements showed flatter melt pool bottom (39.5 μm radius) in CLM vs. SCM.
  - [image description] Figure shows alternating <110> and <100> layers matching melt pool geometry.
  - [non-referenced_knowledge] Side-wall nucleation favors <110> while bottom nucleation produces <100> orientation.
  - [deductive reasoning] Therefore, CLM forms through competitive growth from different melt pool regions under stable thermal conditions.
### M3  Structure → Property
- cause: Crystallographic lamellar microstructure (CLM) with alternating <110> and <100> orientations
- effect: Simultaneous improvement in strength and ductility compared to cast IN718
- experiment: Tensile testing of CLM specimens | Uniaxial tensile test | params: Strain rate: 1.67 × 10⁻⁴ s⁻¹, room temperature vacuum environment | result: CLM showed 571 ± 3 MPa yield strength and 23.5% elongation, outperforming cast material
  - [experimental result] Tensile tests showed CLM had higher strength and ductility than SCM despite larger grain size.
  - [experimental result] Table shows CLM has lower stress-transfer coefficient (0.819) than SCM (1.0).
  - [image description] Figure compares stress-strain response showing superior performance of CLM.
  - [referenced knowledge] Texture modifies classical Hall–Petch relationship through Taylor factor dependence.
  - [deductive reasoning] Thus, CLM achieves strength-ductility synergy through texture effects and interfacial strengthening between layers.
### M4  Property → Performance
- cause: Improved strength and ductility in CLM microstructure
- effect: Superior mechanical performance compared to cast IN718
- experiment: Comparison with cast material | Mechanical property benchmarking | params: Post-heat treated cast IN718 data from literature | result: CLM matched or exceeded cast material in all measured properties without heat treatment
  - [experimental result] Tensile tests showed CLM achieved 571 MPa strength with 23.5% elongation without heat treatment.
  - [experimental result] Table compares CLM favorably to cast material which requires heat treatment.
  - [image description] Figure shows CLM outperforms cast material in both strength and ductility.
  - [non-referenced_knowledge] Overcoming strength-ductility trade-off is major goal in structural materials development.
  - [inductive reasoning] Therefore, CLM represents breakthrough in achieving both high strength and ductility simultaneously through tailored microstructure.
### M5  Structure → Property
- cause: Single-crystal-like microstructure (SCM) with <110> orientation
- effect: Moderate strength and good ductility in LPBF-fabricated Inconel 718
- experiment: Tensile testing of SCM specimens | Uniaxial tensile test | params: Strain rate: 1.67 × 10⁻⁴ s⁻¹, room temperature vacuum environment | result: SCM showed 557 ± 7 MPa yield strength and 20.2% elongation
  - [experimental result] Tensile tests showed SCM had intermediate strength and ductility between CLM and PCM.
  - [image description] Grain size map shows SCM has large, elongated grains with fewer boundaries.
  - [non-referenced_knowledge] SCM lacks strong interlayer interfaces present in CLM but avoids grain boundary weakening in PCM.
  - [deductive reasoning] Therefore, SCM provides balanced mechanical performance through epitaxial grain structure with minimal defects.
### M6  Structure → Property
- cause: Polycrystalline microstructure (PCM) with weak orientation
- effect: High strength but limited ductility in LPBF-fabricated Inconel 718
- experiment: Tensile testing of PCM specimens | Uniaxial tensile test | params: Strain rate: 1.67 × 10⁻⁴ s⁻¹, room temperature vacuum environment | result: PCM showed 652 ± 8 MPa yield strength but only 11.6% elongation
  - [experimental result] Tensile tests showed PCM had highest strength but lowest ductility among tested structures.
  - [experimental result] Table shows PCM has smallest average grain size (16.4 μm) among microstructures.
  - [image description] Figure confirms PCM's poor ductility despite fine grain structure.
  - [referenced knowledge] Hall–Petch relation explains strength increase with decreasing grain size.
  - [deductive reasoning] Therefore, PCM demonstrates classical Hall–Petch strengthening but lacks ductility-enhancing texture effects.
### M7  Property → Performance
- cause: Polycrystalline microstructure (PCM) with weak orientation
- effect: Limited mechanical performance compared to optimized microstructures
- experiment: Mechanical performance evaluation | Comparative mechanical testing | params: Benchmarking against CLM and SCM microstructures | result: PCM exhibited inferior strength-ductility combination compared to CLM and SCM
  - [experimental result] Tensile tests showed PCM had worst strength-ductility combination among tested microstructures.
  - [experimental result] Table compares PCM unfavorably to CLM and SCM in mechanical performance.
  - [image description] Figure illustrates PCM's position on strength-ductility spectrum.
  - [non-referenced_knowledge] AM offers unique capability to tailor microstructures beyond conventional processing limits.
  - [inductive reasoning] Therefore, PCM demonstrates limitations of conventional microstructure approaches in AM context.
