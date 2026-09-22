# MatMech content for Journal_of_Magnesium_and_Alloys/j.jma.2019.01.003 (judge only; not shown to staff)
- material: AZ31/10 vol.% fly ash magnesium matrix composite  elements: ['Mg', 'Al', 'Zn', 'Si', 'O']  category: ['Composite Material', 'Metals and Alloys', 'Crystalline Material', 'Nanomaterial']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Conventional stir casting and friction stir processing (FSP)
- **Structure**: Coarse grain structure (145 μm) and inhomogeneous FA particle dispersion in stir cast composite; fine, equiaxed grains (4 μm) and homogeneous FA particle dispersion with disintegration but no interfacial reaction in FSP composite
- **Properties**: Microhardness–mechanical property, Wear rate–tribological property, Coefficient of friction–tribological property
- **Performance**: Higher wear resistance and lower coefficient of friction in FSP composite under sliding wear conditions
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Conventional stir casting
- effect: Inhomogeneous dispersion of fly ash particles and coarse grain structure (145 μm) with interfacial reactions producing compounds like MgO, Mg₂Si, and MgAl₂O₄
- experiment: Microstructural characterization via optical microscopy and FESEM | Optical microscopy, FESEM | params: Examination of stir cast AZ31/10 vol.% FA composite at various locations (top, middle, bottom) | result: Inhomogeneous FA dispersion, particle decomposition, and absence of continuous segregation along grain boundaries
  - [experimental result] Fly ash particles were introduced into molten AZ31 at 720°C and mechanically stirred.
  - [image description] Optical and SEM micrographs show inhomogeneous dispersion and particle decomposition.
  - [referenced knowledge] Elevated casting temperature triggers interfacial reactions forming MgO, Mg₂Si, and MgAl₂O₄ with negative ΔG.
  - [referenced knowledge] Density difference between FA and molten Mg causes particle movement during holding and solidification.
  - [non-referenced_knowledge] Slow cooling in preheated mold allows unrestricted grain growth, producing coarse grains.
  - [deductive reasoning] Thus, stir casting results in inhomogeneous dispersion, interfacial reactions, and coarse grains.
### M2  Processing → Structure
- cause: Friction stir processing (FSP)
- effect: Homogeneous dispersion of fly ash particles, fine equiaxed grains (4 μm), disintegration of particles without interfacial reaction
- experiment: Friction stir processing with HCHCr tool at 1200 rpm and 40 mm/min | Friction stir processing | params: Tool rotational speed: 1200 rpm, traverse speed: 40 mm/min, shoulder diameter: 18 mm, pin diameter: 6 mm, pin length: 5 mm | result: Homogeneous FA dispersion, fine grains (4 μm), no interfacial compounds, particle disintegration
  - [experimental result] FA particles were packed into a groove on AZ31 plate and processed via FSP at 1200 rpm and 40 mm/min.
  - [non-referenced_knowledge] FSP generates frictional heat and intense shear, plasticizing the matrix without melting.
  - [referenced knowledge] Rotating tool induces 3D material flow, thoroughly mixing FA particles with matrix.
  - [image description] FESEM shows FA particles disintegrated into smaller debris with sharp, reaction-free interfaces.
  - [image description] EBSD reveals fine equiaxed grains (4 μm) due to dynamic recrystallization.
  - [non-referenced_knowledge] Disintegrated FA particles pin grain boundaries, suppressing grain growth.
  - [deductive reasoning] Thus, FSP yields homogeneous dispersion, fine grains, and clean interfaces without decomposition.
### M3  Structure → Property
- cause: Homogeneous dispersion, fine grains, and clean interfaces in FSP composite
- effect: Higher microhardness (94 HV) and lower wear rate (280 × 10⁻⁵ mm³/m)
- experiment: Microhardness testing and pin-on-disc wear test | Microhardness tester (500 g load, 15 s), Pin-on-disc wear apparatus (ASTM G99-04A) | params: Load: 20 N, sliding velocity: 1.0 m/s, sliding distance: 3000 m | result: FSP composite: 94 HV, 280 × 10⁻⁵ mm³/m wear rate; Stir cast: 62 HV, 420 × 10⁻⁵ mm³/m wear rate
  - [image description] FSP composite exhibits homogeneous FA dispersion and fine grains (4 μm).
  - [experimental result] Microhardness of FSP composite is 94 HV, 51% higher than stir cast (62 HV).
  - [referenced knowledge] Orowan strengthening mechanism is activated by fine, uniformly distributed particles diverting dislocations.
  - [referenced knowledge] Hall-Petch relationship explains increased hardness due to reduced grain size.
  - [experimental result] Wear rate of FSP composite is 33% lower than stir cast (280 vs. 420 × 10⁻⁵ mm³/m).
  - [referenced knowledge] Archard’s law links higher hardness to lower wear rate.
  - [non-referenced_knowledge] Homogeneous dispersion prevents localized plowing, and fine debris enables three-body abrasion.
  - [deductive reasoning] Thus, FSP microstructure directly enhances hardness and wear resistance.
### M4  Structure → Property
- cause: Inhomogeneous dispersion, coarse grains, and interfacial reactions in stir cast composite
- effect: Lower microhardness (62 HV) and higher wear rate (420 × 10⁻⁵ mm³/m)
- experiment: Microhardness testing and pin-on-disc wear test | Microhardness tester (500 g load, 15 s), Pin-on-disc wear apparatus (ASTM G99-04A) | params: Load: 20 N, sliding velocity: 1.0 m/s, sliding distance: 3000 m | result: Stir cast composite: 62 HV, 420 × 10⁻⁵ mm³/m wear rate
  - [image description] Stir cast composite shows inhomogeneous FA dispersion and coarse grains (145 μm).
  - [experimental result] Microhardness is only 62 HV, significantly lower than FSP composite (94 HV).
  - [referenced knowledge] Interfacial reactions form compounds that weaken matrix-reinforcement bonding.
  - [referenced knowledge] Coarse grains reduce strength via Hall-Petch relationship.
  - [non-referenced_knowledge] Particle-free zones in microstructure lead to localized plastic deformation under load.
  - [experimental result] Wear rate is higher (420 × 10⁻⁵ mm³/m) due to bulk material removal from weak zones.
  - [deductive reasoning] Thus, poor microstructure directly results in inferior mechanical and tribological properties.
### M5  Property → Performance
- cause: Higher microhardness and lower coefficient of friction in FSP composite
- effect: Superior wear resistance under sliding conditions
- experiment: Pin-on-disc sliding wear test | Pin-on-disc wear apparatus (DUCOM TR20-LE) | params: 20 N load, 1.0 m/s velocity, 3000 m sliding distance | result: FSP composite wear rate: 280 × 10⁻⁵ mm³/m (33% lower than stir cast); COF: 0.35 vs. 0.48
  - [experimental result] FSP composite has higher microhardness (94 HV) and lower COF (0.35) compared to stir cast (62 HV, 0.48).
  - [referenced knowledge] Archard’s law dictates that higher hardness leads to lower wear rate.
  - [referenced knowledge] Lower COF reduces shear stress at sliding interface, decreasing material removal.
  - [experimental result] Wear rate of FSP composite is 33% lower than stir cast (280 vs. 420 × 10⁻⁵ mm³/m).
  - [deductive reasoning] Thus, enhanced hardness and reduced friction directly improve wear performance.
