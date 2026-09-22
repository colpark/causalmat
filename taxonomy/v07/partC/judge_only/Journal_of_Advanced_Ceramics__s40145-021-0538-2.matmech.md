# MatMech content for Journal_of_Advanced_Ceramics/s40145-021-0538-2 (judge only; not shown to staff)
- material: Al₂O₃-YSZ  elements: ['Al', 'O', 'Y', 'Zr']  category: ['Ceramic', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Atmospheric plasma spraying (APS)
- **Structure**: Cubic phase dominance with 78.56% crystallinity; amorphous phase at grain boundaries; columnar and equiaxed grain morphology; phase transition from cubic to tetragonal zirconia during thermal cycling
- **Properties**: Crack size–mechanical property; microstrain–mechanical property; crystallinity–structural property
- **Performance**: Thermal cycle life; coating spalling failure
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Atmospheric plasma spraying (APS)
- effect: Al₂O₃-YSZ coatings exhibit cubic phase dominance (≈100% cubic phase), 78.56% crystallinity, amorphous phase at grain boundaries, and mixed columnar/equiaxed grain morphology
- experiment: XRD phase analysis and SEM/EBSD microstructure characterization | X-ray diffraction (XRD), Scanning electron microscopy (SEM), Electron backscatter diffraction (EBSD) | params: As-sprayed coatings analyzed for phase composition and grain structure | result: Al₂O₃-YSZ coatings show nearly 100% cubic phase and 78.56% crystallinity; no α-Al₂O₃ peak detected; amorphous phase inferred near cracks
  - [experimental result] Al₂O₃-YSZ coatings were prepared by atmospheric plasma spraying (APS).
  - [experimental result] XRD analysis shows nearly 100% cubic phase in Al₂O₃-YSZ and only 5% cubic phase in YSZ.
  - [non-referenced_knowledge] No α-Al₂O₃ peak is detected, suggesting Al atoms are incorporated into ZrO₂ lattice or form amorphous phase at boundaries.
  - [image description] EBSD and SEM show amorphous regions near cracks and reduced crystallinity (78.56%) in Al₂O₃-YSZ.
  - [non-referenced_knowledge] Rapid cooling in APS stabilizes the high-temperature cubic phase of zirconia and inhibits full crystallization.
  - [deductive reasoning] Thus, APS processing results in a microstructure dominated by cubic phase, amorphous boundaries, and reduced crystallinity.
### M2  Structure → Performance
- cause: Low crystallinity (78.56%) and amorphous phase at grain boundaries in Al₂O₃-YSZ coatings
- effect: Larger crack size (26 μm vs. 12 μm) and reduced thermal cycle life
- experiment: Crack size measurement via Image J analysis of SEM images | Image analysis of SEM micrographs | params: Statistical analysis of crack sizes in Al₂O₃-YSZ and YSZ coatings | result: Average crack size in Al₂O₃-YSZ is 26 μm, significantly larger than 12 μm in YSZ; correlated with low crystallinity
  - [experimental result] Al₂O₃-YSZ coatings have 78.56% crystallinity, significantly lower than YSZ (~100%).
  - [image description] EBSD and SEM show amorphous phase concentrated near cracks.
  - [experimental result] Crack size in Al₂O₃-YSZ is 26 μm, twice that of YSZ (12 μm).
  - [referenced knowledge] According to Griffith’s theory, larger cracks reduce fracture strength.
  - [non-referenced_knowledge] Amorphous phases are mechanically weaker and concentrate stress.
  - [deductive reasoning] Thus, low crystallinity and amorphous boundaries cause larger cracks, reducing thermal cycle life.
### M3  Structure → Performance
- cause: High microstrain and grain orientation change (5.42° average) in Al₂O₃-YSZ coatings during thermal cycling
- effect: Accelerated crack propagation and connection, leading to reduced thermal cycle life
- experiment: EBSD-based grain orientation change and XRD-based microstrain measurement | EBSD orientation analysis, XRD peak broadening analysis | params: Change in Euler angles and microstrain calculated over 5 thermal cycles | result: Average grain orientation change: 5.42° for Al₂O₃-YSZ vs. 1.49° for YSZ; microstrain in Al₂O₃-YSZ is significantly higher
  - [experimental result] EBSD analysis of 10 grains shows average orientation change of 5.42° in Al₂O₃-YSZ after 5 cycles.
  - [experimental result] XRD analysis confirms higher microstrain in Al₂O₃-YSZ compared to YSZ.
  - [image description] The degree of grain orientation change is positively correlated with microstrain.
  - [referenced knowledge] Microstrain induces microscopic stress in the megapascal range.
  - [non-referenced_knowledge] Microstress promotes crack nucleation and propagation at grain boundaries.
  - [deductive reasoning] Thus, high microstrain and orientation change in Al₂O₃-YSZ lead to faster crack propagation and reduced thermal cycle life.
### M4  Structure → Performance
- cause: Columnar vs. equiaxed grain morphology in Al₂O₃-YSZ coatings
- effect: Different crack propagation modes: intergranular in equiaxed grains vs. transgranular in columnar grains, affecting failure rate
- experiment: EBSD and SEM analysis of crack propagation paths in two grain morphologies | EBSD orientation mapping, SEM crack path analysis | params: Analysis of sites 1 (equiaxed) and 2 (columnar) near cracks | result: Cracks propagate intergranularly in equiaxed grains and transgranularly in columnar grains; transgranular cracks branch and require more energy to propagate
  - [image description] EBSD images show intergranular crack propagation in equiaxed grain regions (site 1).
  - [image description] Transgranular crack propagation is observed in columnar grain regions (site 2).
  - [image description] SEM reveals voids and high stress concentration at equiaxed grain boundaries.
  - [referenced knowledge] Transgranular cracks require more fracture energy to propagate through the grain interior.
  - [non-referenced_knowledge] Columnar grains impede vertical crack penetration by forcing horizontal crack branching.
  - [deductive reasoning] Thus, equiaxed morphology accelerates failure via easy intergranular paths, while columnar morphology partially resists it.
### M5  Structure → Performance
- cause: Phase transition from cubic to tetragonal zirconia during thermal cycling (after 5–10 cycles)
- effect: Sudden spalling failure of Al₂O₃-YSZ coatings due to 2% volume shrinkage and stress concentration at pre-existing cracks
- experiment: XRD phase analysis after 5, 10, and 40 thermal cycles | X-ray diffraction (XRD) | params: Monitoring peak at 43° and splitting at 73° indicating t-ZrO₂ formation | result: After 10 cycles, a new peak at 43° and peak splitting at 73° confirm cubic-to-tetragonal phase transition; spalling peaks at 5–10 cycles
  - [experimental result] XRD shows cubic phase dominates in as-sprayed Al₂O₃-YSZ.
  - [experimental result] After 10 thermal cycles, new XRD peaks at 43° and 73° confirm tetragonal phase formation.
  - [referenced knowledge] The cubic-to-tetragonal transition involves 2% volume shrinkage without diffusion.
  - [image description] Spalling occurs most severely between 5–10 cycles, coinciding with phase transition.
  - [non-referenced_knowledge] Pre-existing cracks (from low crystallinity) provide stress concentration sites.
  - [deductive reasoning] Volume shrinkage during phase transition generates tensile stress at crack tips, exceeding fracture toughness.
  - [deductive reasoning] Thus, phase transition is the direct cause of spalling failure.
### M6  Structure → Performance
- cause: Phase transition from cubic to tetragonal zirconia after 10 cycles
- effect: Reduction in microstrain and grain orientation change, slowing further spalling
- experiment: EBSD and XRD analysis after 10–40 thermal cycles | EBSD orientation change measurement, XRD microstrain analysis | params: Grain orientation change and XRD peak broadening after 10, 20, 30, and 40 cycles | result: After 10 cycles, grain orientation change drops to ~1.5° (similar to YSZ); microstrain also decreases
  - [experimental result] After 10 thermal cycles, grain orientation change in Al₂O₃-YSZ drops to 1.5°, similar to YSZ.
  - [experimental result] Microstrain also decreases significantly after 10 cycles.
  - [experimental result] XRD confirms the phase is now tetragonal.
  - [referenced knowledge] Tetragonal zirconia has higher fracture toughness and lower microstrain than cubic phase.
  - [deductive reasoning] Thus, the transformed tetragonal phase stabilizes the microstructure and reduces further degradation.
