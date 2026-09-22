# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116713 (judge only; not shown to staff)
- material: Ni/NiAl interface  elements: ['Ni', 'Al']  category: ['Metals and Alloys', 'Crystalline Material', 'Composite Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Diffusion annealing at 650°C for 1h, 4h, 6h, 18h, and 48h
- **Structure**: Formation of Ni3Al in two layers with specific crystallographic relationships to NiAl and Ni phases, Al-enriched (Ni) grains
- **Properties**: Growth kinetics–mechanical property, grain size distribution–mechanical property
- **Performance**: Parabolic growth behavior of Ni3Al layers, diffusion-induced recrystallization in (Ni) phase
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Diffusion annealing at 650°C for varying durations (1h, 4h, 6h, 18h, and 48h)
- effect: Ni3Al forms in two distinct layers with specific crystallographic relationships to NiAl and Ni phases
- experiment: EBSD and STEM EDX analysis of diffusion-annealed samples | Electron Backscatter Diffraction (EBSD) combined with Scanning Transmission Electron Microscopy Energy-Dispersive X-ray Spectroscopy (STEM EDX) | params: Annealing temperatures: 650°C; Annealing times: 1h, 4h, 6h, 18h, 48h; Characterization of interface microstructure and orientation relationships | result: Formation of two Ni3Al layers with distinct orientation relationships; grains in first layer exhibit K-S relationship with NiAl, while second layer shows near cube-on-cube relationship with Ni
  - [experimental result] Annealing at 650°C initiates interdiffusion between Ni and NiAl, leading to Ni3Al nucleation.
  - [image description] Figure 1b shows Al concentration profile confirming Ni3Al layer composition (20–25 at% Al in upper layer).
  - [referenced knowledge] Kurdjumov-Sachs orientation relationships are established between Ni3Al and NiAl due to favorable lattice matching.
  - [non-referenced_knowledge] Near cube-on-cube relationship dominates at Ni/Ni3Al interface due to low misorientation and high coherency.
  - [deductive reasoning] Thus, annealing temperature and interfacial symmetry control the crystallographic configuration of newly formed Ni3Al.
### M2  Structure → Property
- cause: Ni3Al grains grow into NiAl phase with Kurdjumov-Sachs orientation relationships
- effect: Grain boundary mobility is reduced, affecting growth kinetics
- experiment: Statistical evaluation of grain size and boundary types | Quantitative EBSD analysis | params: Misorientation angle measurements, grain boundary classification (twin vs. high-angle), texture mapping | result: Ni3Al grains with K-S relationship to NiAl exhibit ~45% fraction with multiple variants; increased fraction of small-angle and twin boundaries observed
  - [image description] EBSD pole figures show multiple K-S variants in Ni3Al grains adjacent to NiAl.
  - [non-referenced_knowledge] These orientation relationships promote the formation of twin and small-angle boundaries at the NiAl/Ni3Al interface.
  - [referenced knowledge] Immobile boundaries act as pinning sites that restrict further grain growth.
  - [inductive reasoning] Therefore, the presence of K-S relationships reduces grain boundary mobility and slows Ni3Al growth kinetics.
### M3  Processing → Structure
- cause: Annealing at 650°C for extended duration (up to 48h)
- effect: Increased fraction of oriented Ni3Al grains (from ~50% to ~80%)
- experiment: Time-dependent texture evolution analysis | EBSD statistical evaluation | params: Annealing time variation (1h, 4h, 6h, 18h, 48h); quantification of oriented grains using pole figures | result: Fraction of Ni3Al grains with defined orientation relationships increases from ~50% after 1h to ~80% after 6h and beyond
  - [experimental result] After 1h of annealing, ~50% of Ni3Al grains exhibit defined orientation relationships.
  - [experimental result] By 6h, this fraction increases to ~80%, indicating progressive texturing over time.
  - [inductive reasoning] This suggests that grains with preferred orientations have higher growth rates.
  - [referenced knowledge] Such behavior aligns with competitive grain growth models where favored orientations dominate over time.
  - [deductive reasoning] Hence, prolonged annealing increases the fraction of oriented Ni3Al grains through selective growth of energetically favorable orientations.
### M4  Structure → Performance
- cause: Formation of Al-enriched (Ni) grains at Ni/Ni3Al interface
- effect: Diffusion-induced recrystallization and accelerated growth of (Ni) grains
- experiment: EBSD and EDX characterization of third layer at Ni/Ni3Al interface | Microstructural and compositional analysis | params: Grain size measurement, Al concentration mapping, misorientation analysis | result: Third layer contains Al-enriched (Ni) grains (~5 at% Al), ~1.6 μm mean size, ~26° misoriented relative to original Ni grains
  - [image description] EDX profile shows ~5 at% Al in the third layer beneath Ni3Al, indicating Al enrichment in Ni.
  - [experimental result] These Al-enriched grains are ~1.6 μm in size, significantly larger than surrounding Ni grains (~0.48 μm).
  - [referenced knowledge] Recrystallization driven by Al diffusion is known to enhance grain boundary mobility.
  - [non-referenced_knowledge] Higher grain boundary mobility enables faster growth and coarsening of Al-enriched Ni grains.
  - [deductive reasoning] Therefore, Al enrichment at the Ni/Ni3Al interface facilitates diffusion-induced recrystallization and accelerates grain growth.
