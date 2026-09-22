# MatMech content for Materials_Characterization/j.matchar.2017.11.052 (judge only; not shown to staff)
- material: AlSi10Mg  elements: ['Al', 'Si', 'Mg']  category: ['Metals and Alloys', 'Crystalline Material', 'Composite Material', 'Nanomaterial']
- MST chain: Processing → Structure → Property
## Tetrahedron elements
- **Processing**: Selective laser melting (SLM) with laser power of 380 W, powder layer thickness of 30 μm, hatch spacing of 150 μm, and 67° layer rotation
- **Structure**: Columnar α-Al grains with <001> texture surrounded by eutectic Si particles; fine Si precipitates inside α-Al grains more frequent in smaller samples; low-angle boundaries less dense in smaller samples
- **Properties**: Hardness–mechanical property
- **Performance**: None
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Selective laser melting (SLM) with laser power of 380 W, powder layer thickness of 30 μm, hatch spacing of 150 μm, and 67° layer rotation
- effect: Columnar α-Al grains with <001> texture surrounded by eutectic Si particles; fine Si precipitates inside α-Al grains more frequent in smaller samples; low-angle boundaries less dense in smaller samples
- experiment: SLM fabrication of AlSi10Mg samples | Selective laser melting | params: Laser power: 380 W, powder layer thickness: 30 μm, hatch spacing: 150 μm, layer rotation angle: 67°, ambient Ar atmosphere | result: Samples with widths from 0.1 mm to 10 mm fabricated with consistent melt pool morphology and microstructural features varying with size
  - [experimental result] SLM was performed with 380 W laser power, 30 μm layer thickness, 150 μm hatch spacing, and 67° layer rotation.
  - [image description] Optical and EBSD micrographs show columnar α-Al grains with <001> orientation along Z direction in all samples.
  - [non-referenced_knowledge] Rapid solidification during SLM promotes directional grain growth along the thermal gradient.
  - [experimental result] Smaller samples exhibit more fine Si precipitates inside α-Al grains and lower density of low-angle boundaries.
  - [non-referenced_knowledge] Thermal conductivity of AlSi10Mg is high (120–170 W·m⁻¹·K⁻¹), but small samples have reduced heat flow paths to surrounding powder, leading to slower cooling.
  - [deductive reasoning] Slower cooling and additional reheating from laser scanning of overlying powder layers increase time at elevated temperatures, promoting Si precipitation and α-Al recovery.
  - [experimental result] Precipitation of Si reduces supersaturation of Si in α-Al matrix, consistent with lower measured Si phase fraction than equilibrium prediction.
  - [image description] EBSD analysis at 0.5 μm step size confirms lower density of low-angle boundaries in smaller samples, indicating enhanced recovery.
### M2  Structure → Property
- cause: Fine Si precipitates inside columnar α-Al grains and reduced low-angle boundary density in smaller samples
- effect: Decrease in hardness from ~112 Hv (10 mm) to ~107 Hv (0.28 mm)
- experiment: Vickers hardness measurement | Vickers hardness test | params: Load: 0.98 N, indent size: 70–80 μm, measurements at sample center | result: Hardness decreases from ~112 Hv for 10 mm samples to ~107 Hv for 0.28 mm samples
  - [experimental result] Hardness decreases from 112 Hv to 107 Hv as sample width reduces from 10 mm to 0.28 mm.
  - [experimental result] Smaller samples show higher number density and area fraction of Si particles inside α-Al grains.
  - [non-referenced_knowledge] Si particles precipitate from supersaturated α-Al matrix, reducing solute concentration available for solid solution strengthening.
  - [referenced knowledge] Annealing studies confirm that Si precipitation reduces strength even when precipitates are present.
  - [image description] EBSD analysis shows lower density of low-angle boundaries (dislocation arrays) in smaller samples.
  - [non-referenced_knowledge] Reduced dislocation density from recovery lowers strain hardening capacity.
  - [experimental result] Grain size (high-angle boundary spacing) is unchanged, ruling out Hall-Petch effect as the cause.
  - [deductive reasoning] Thus, the dominant contributor to softening is loss of solid solution strengthening and reduced dislocation density.
