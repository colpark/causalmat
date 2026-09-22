# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116661 (judge only; not shown to staff)
- material: 32MnB5 hot-stamping steel  elements: ['Fe', 'Mn', 'B', 'C', 'Mo']  category: ['Metals and Alloys', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Addition of 0.15 wt.% Mo, austenitization at 900°C for 6 min, and quenching
- **Structure**: Fully lath-martensitic microstructure with prior austenite grain boundaries (PAGBs)
- **Properties**: tensile strength–mechanical property, elongation–mechanical property, hydrogen diffusivity–physical property
- **Performance**: Improved resistance to hydrogen embrittlement (HE) with reduced ductility loss and sufficient post-elongation
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Addition of 0.15 wt.% Mo during steel fabrication
- effect: Solute Mo segregates at prior austenite grain boundaries (PAGBs) along with C and B
- experiment: APT analysis of PAGB segregation | Atom Probe Tomography (APT) | params: 3D atom-position reconstruction at PAGBs in Mo steel | result: C, B, and Mo atoms are densely localized at the PAGB; peak Mo concentration reaches ~1.1 at.%
  - [experimental result] APT shows dense localization of Mo, C, and B at PAGBs
  - [image description] APT reconstruction maps confirm segregation of Mo at PAGBs
  - [referenced knowledge] Non-equilibrium segregation mechanism explains Mo accumulation at PAGBs due to vacancy interactions
  - [non-referenced_knowledge] Segregation behavior depends on diffusivity and binding energy between solute atoms and vacancies
  - [deductive reasoning] Thus, Mo segregates to PAGBs through a non-equilibrium process involving vacancy-mediated transport
### M2  Structure → Property
- cause: Segregation of Mo at prior austenite grain boundaries (PAGBs)
- effect: Enhanced grain-boundary cohesion
- experiment: Fracture mode analysis after SSRT | Scanning Electron Microscopy (SEM) | params: Observation of fracture surfaces after H-charging at 3 mA·cm⁻² | result: Mo steel exhibits ductile dimples and quasi-cleavage facets instead of intergranular fracture observed in reference steel
  - [experimental result] SSRT tests show Mo steel fractures in ductile mode with post-elongation
  - [image description] SEM images reveal ductile dimples and quasi-cleavage facets in Mo steel rather than intergranular fracture
  - [referenced knowledge] First-principles calculations show Mo enhances Fe grain-boundary cohesive energy
  - [non-referenced_knowledge] Grain-boundary cohesion is critical in determining fracture mode and resistance to hydrogen embrittlement
  - [deductive reasoning] Therefore, Mo segregation at PAGBs improves cohesion, leading to ductile fracture behavior
### M3  Processing → Property
- cause: Addition of 0.15 wt.% Mo to the steel matrix
- effect: Reduced hydrogen diffusivity in the steel lattice
- experiment: Hydrogen permeation test | Electrochemical permeation measurement | params: Exposed area: 78.5 mm², charging solutions: 0.1M NaOH and 3% NaCl + 0.3% NH₄SCN | result: Apparent H diffusivity decreases by 56% in Mo steel compared to reference (14.2×10⁻¹¹ vs 6.33×10⁻¹¹ m²/s)
  - [experimental result] Hydrogen permeation tests show significantly reduced diffusivity in Mo steel
  - [image description] Permeation curves demonstrate longer breakthrough time in Mo steel
  - [referenced knowledge] Oriani's model links reduced diffusivity to increased binding energy and decreased lattice trapping sites
  - [non-referenced_knowledge] Larger atomic size of Mo creates repulsive strain fields that reduce available lattice trapping sites for H
  - [deductive reasoning] Therefore, Mo reduces H mobility both through thermodynamic interaction and physical strain field effects
### M4  Property → Performance
- cause: Reduced hydrogen diffusivity in Mo steel
- effect: Improved resistance to hydrogen embrittlement with reduced ductility loss
- experiment: Slow-strain-rate tensile (SSRT) testing | Mechanical testing after electrochemical H-charging | params: Strain rate: 10⁻⁴ s⁻¹, H-charging current densities: 0.5 and 3 mA·cm⁻² | result: Elongation loss reduced from 50–79% in reference to 17–26% in Mo steel after H-charging
  - [experimental result] SSRT tests show significantly lower elongation loss in Mo steel after H-charging
  - [image description] Stress-strain curves demonstrate improved ductility retention in Mo steel
  - [referenced knowledge] HELP mechanism explains how H accelerates embrittlement through dislocation interactions
  - [non-referenced_knowledge] Hydrogen-assisted cracking occurs via HELP mechanism where H facilitates dislocation movement and strain localization
  - [deductive reasoning] Thus, reduced H diffusivity in Mo steel limits these interactions, improving HE resistance
