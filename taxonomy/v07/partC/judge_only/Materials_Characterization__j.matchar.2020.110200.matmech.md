# MatMech content for Materials_Characterization/j.matchar.2020.110200 (judge only; not shown to staff)
- material: IN718 superalloy  elements: ['Ni', 'Cr', 'Fe', 'Nb', 'Mo', 'Ti', 'Al', 'Co']  category: ['Metals and Alloys', 'Crystalline Material', 'Composite Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Selective laser melting (SLM) with laser power of 150 W, laser velocity of 1000 mm/s, layer thickness of 30 μm, and island scanning strategy
- **Structure**: Columnar grains with ⟨001⟩ orientation parallel to building direction in side view; equiaxed grains with Laves phases at intercellular regions in top view; (100) fiber texture dominant in both views
- **Properties**: maximum force–mechanical property, yield strength–mechanical property, ultimate tensile strength–mechanical property
- **Performance**: Mechanical anisotropy at room and high temperatures (650 °C); ductile fracture in side view at room temperature, brittle intergranular fracture in side view and transgranular brittle fracture with Laves phases in top view at high temperature
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Selective laser melting (SLM) with laser power of 150 W, laser velocity of 1000 mm/s, layer thickness of 30 μm, and island scanning strategy
- effect: Columnar grains with ⟨001⟩ orientation parallel to building direction in side view; equiaxed grains with Laves phases at intercellular regions in top view; (100) fiber texture dominant in both views
- experiment: EBSD orientation mapping and XRD pole figure analysis | EBSD, XRD | params: 15 kV, 20 nm step size for high magnification; 20 kV, 3 μm step size for low magnification; XRD texture parameter method | result: Strong (100) fiber texture with ⟨001⟩ orientation along building direction in side view; equiaxed grains and intercellular Laves phases in top view; texture parameter TP(200) = 3.0 (side) and 3.2 (top)
  - [experimental result] SLM process uses laser power of 150 W and scanning strategy that creates directional heat flow along the building direction.
  - [experimental result] XRD and EBSD analyses show dominant (100) fiber texture with ⟨001⟩ orientation parallel to building direction in side view.
  - [non-referenced_knowledge] ⟨001⟩ is the easiest growth direction in FCC metals like IN718 under directional solidification.
  - [image description] SEM and EBSD images reveal columnar grains extending through multiple layers in side view, while top view shows equiaxed grains and intercellular precipitates.
  - [referenced knowledge] Nb segregation during rapid cooling leads to formation of Laves phases at intercellular regions, as confirmed by EDS.
  - [deductive reasoning] Thus, processing parameters induce anisotropic microstructure: columnar ⟨001⟩ grains in side view, equiaxed grains with Laves phases in top view.
### M2  Structure → Properties
- cause: Columnar grains with ⟨001⟩ orientation parallel to building direction in side view; equiaxed grains with Laves phases at intercellular regions in top view; (100) fiber texture dominant in both views
- effect: 54% greater maximum force in side view than top view at room temperature; significant drop in side view maximum force at 650 °C; no significant change in top view at 650 °C
- experiment: Small punch test (SPT) and uniaxial tensile testing | Small punch test, tensile test | params: Room temperature (25 °C) and 650 °C; punch diameter 2.5 mm; specimen thickness 500 μm; tensile velocity 0.5 mm/min | result: Side view: 1691 N max force (RT), 1065 N (650 °C); Top view: 1096 N max force (RT), 1133 N (650 °C); SPT-calculated YS and UTS match tensile test results within 2%
  - [image description] Side view samples have columnar grains with ⟨001⟩ orientation perpendicular to SPT load direction.
  - [non-referenced_knowledge] This orientation aligns slip systems close to 45° to the applied load, maximizing Schmid factor.
  - [experimental result] SPT curves show wider plastic zone (zone II) in side view at room temperature, indicating higher work hardening.
  - [image description] Side view samples contain more melt pool boundaries and residual stresses due to higher layer count (290 layers vs. 17).
  - [non-referenced_knowledge] Higher dislocation density from residual stresses enhances work hardening at room temperature.
  - [referenced knowledge] At 650 °C, continuous Laves chains in side view impede plasticity and promote brittle fracture.
  - [image description] Top view has equiaxed grains with discrete Laves phases and low residual stress, maintaining strength at high temperature.
  - [deductive reasoning] Thus, microstructure anisotropy causes mechanical anisotropy: side view stronger at RT, top view more stable at HT.
### M3  Structure → Performance
- cause: Columnar grains with ⟨001⟩ orientation parallel to building direction in side view; equiaxed grains with Laves phases at intercellular regions in top view; (100) fiber texture dominant in both views
- effect: Ductile fracture with dimples in side view at room temperature; transgranular brittle fracture with Laves phases in top view at room temperature; intergranular brittle fracture in side view and cleavage with Laves phases in top view at 650 °C
- experiment: Fractography of SPT samples using SEM | SEM fractography | params: High-resolution imaging of fracture surfaces after SPT at 25 °C and 650 °C | result: Side view RT: ductile dimples; Top view RT: flat brittle cleavage; Side view HT: intergranular fracture with mountain-like facets; Top view HT: transgranular cleavage with Nb-rich Laves particles
  - [image description] Side view fracture surface at room temperature shows parabolic dimples, indicating ductile transgranular fracture.
  - [image description] Top view fracture surface at room temperature shows flat, brittle cleavage without dimples.
  - [referenced knowledge] Laves phases are identified by EDS as Nb-rich precipitates on top view fracture surface at 650 °C.
  - [image description] At 650 °C, side view shows mountain-like facets matching columnar grain size, indicating intergranular fracture.
  - [non-referenced_knowledge] Grain boundaries in columnar structure are weakened at high temperature due to segregation and reduced cohesion.
  - [non-referenced_knowledge] Laves phases act as stress concentrators and crack initiation sites in top view, leading to transgranular cleavage.
  - [deductive reasoning] Thus, fracture performance is directly controlled by microstructure: columnar grains → intergranular HT failure; Laves phases → brittle transgranular failure.
### M4  Processing → Properties
- cause: Selective laser melting (SLM) with laser power of 150 W, laser velocity of 1000 mm/s, layer thickness of 30 μm, and island scanning strategy
- effect: 54% greater maximum force in side view than top view at room temperature; 37% decrease in side view maximum force at 650 °C; no significant change in top view at 650 °C
- experiment: Small punch test (SPT) and tensile validation | Small punch test, uniaxial tensile test | params: RT and 650 °C; SPT disc thickness 500 μm; tensile gauge length 20 mm; displacement rate 0.5 mm/min | result: Side view max force: 1691 N (RT), 1065 N (650 °C); Top view max force: 1096 N (RT), 1133 N (650 °C); SPT-calculated YS/UTS match tensile results within 2%
  - [experimental result] SLM process parameters (150 W, 1000 mm/s, 30 μm layer) create strong directional heat flow along building direction.
  - [non-referenced_knowledge] This results in columnar ⟨001⟩ grains in side view and equiaxed grains with Laves phases in top view.
  - [non-referenced_knowledge] Columnar grains in side view provide higher Schmid factor and residual stress, increasing RT strength.
  - [non-referenced_knowledge] At 650 °C, columnar grain boundaries weaken and Laves chains embrittle side view, reducing strength.
  - [image description] Top view lacks strong texture and has low residual stress, maintaining consistent strength at HT.
  - [deductive reasoning] Thus, SLM processing directly determines anisotropic mechanical properties via microstructure.
