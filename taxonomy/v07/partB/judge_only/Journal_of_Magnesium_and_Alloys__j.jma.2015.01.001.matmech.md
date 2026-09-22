# MatMech content for Journal_of_Magnesium_and_Alloys/j.jma.2015.01.001 (judge only; not shown to staff)
- material: AZ91-SiCp  elements: ['Mg', 'Al', 'Si', 'C', 'O']  category: ['Metals and Alloys', 'Composite Material', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Stir casting with preheated SiC particles added at 750 °C under argon atmosphere, followed by pouring into a 300 °C preheated steel mold
- **Structure**: Grain size reduction from 65 microns (base AZ91) to 22 microns (10 wt% SiCp); near-uniform distribution of SiCp particles; clean Mg-SiCp interface; presence of Mg17Al12 intermetallic phase and traces of MgO and Mg2Si
- **Properties**: Yield strength–mechanical property, Ultimate compressive strength–mechanical property, Ultimate tensile strength–mechanical property, Minimum creep rate–creep property, Stress exponent–creep property
- **Performance**: Improved creep resistance at 175 °C under 80–120 MPa stress; enhanced room temperature mechanical properties with increasing SiCp content
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Stir casting with preheated SiC particles added at 750 °C under argon atmosphere, followed by pouring into a 300 °C preheated steel mold
- effect: Grain size reduction from 65 microns (base AZ91) to 22 microns (10 wt% SiCp); near-uniform distribution of SiCp particles; clean Mg-SiCp interface
- experiment: Microstructural analysis via optical and SEM microscopy | Optical microscopy, Scanning Electron Microscopy (SEM) | params: Etching with acetic picral; SEM accelerating voltage 15–30 keV | result: Grain size reduced to 22 microns at 10 wt% SiCp; particles uniformly distributed with few agglomerations; clean, precipitate-free interface observed
  - [experimental result] SiCp particles were preheated to 600 °C and added during stirring at 750 °C under argon atmosphere.
  - [image description] Optical micrographs show grain size reduction from 65 microns (base alloy) to 22 microns (10 wt% SiCp).
  - [non-referenced_knowledge] SiCp can act as heterogeneous nucleation sites, captured by growing Mg crystals, restricting grain growth.
  - [image description] SEM images reveal clean, precipitate-free Mg-SiCp interfaces, indicating good wettability.
  - [referenced knowledge] Al in AZ91 enhances SiCp wettability, reducing interfacial reactions [13].
  - [deductive reasoning] Thus, stir casting parameters enable grain refinement and strong interfacial bonding.
### M2  Structure → Property
- cause: Grain size reduction and near-uniform distribution of SiCp particles; clean Mg-SiCp interface
- effect: Increase in yield strength and ultimate compressive strength; minimal change in ultimate tensile strength
- experiment: Tensile and compressive mechanical testing | Universal testing machine (INSTRON 8801), compression testing | params: Cross-head speed 2 mm/min; compressive stress applied to cylindrical specimens | result: Yield strength increased with SiCp content; ultimate compressive strength increased significantly; ultimate tensile strength remained similar to base alloy
  - [non-referenced_knowledge] SiCp particles are finely dispersed and act as barriers to dislocation motion.
  - [referenced knowledge] Grain size reduction from 65 to 22 microns enhances strength in the elastic region [14].
  - [experimental result] Yield strength increases progressively with SiCp content, as shown in Fig. 3.
  - [experimental result] Ultimate compressive strength increases due to high hardness of SiCp and crack closure under compression.
  - [non-referenced_knowledge] Ultimate tensile strength remains unchanged due to residual stress, agglomerations, and porosity.
  - [deductive reasoning] Thus, structure (grain size + dispersion) directly enhances yield and compressive strength but not tensile strength.
### M3  Structure → Property
- cause: Grain size reduction and near-uniform distribution of SiCp particles; clean Mg-SiCp interface
- effect: Reduction in minimum creep rate and increase in stress exponent (n) and true stress exponent (nt)
- experiment: Compression creep testing at 175 °C under 80, 100, 120 MPa | ATS lever arm system | params: Temperature: 175 °C; stress levels: 80, 100, 120 MPa; creep rate measured over time | result: Minimum creep rate decreased with increasing SiCp content; stress exponent n increased from 7.2 (base) to 8.9 (25 wt%); true stress exponent nt ranged from 5.4–5.8
  - [experimental result] Creep tests at 175 °C show reduced minimum creep rate with higher SiCp content.
  - [experimental result] Stress exponent n increases from 7.2 to 8.9 with SiCp content, indicating stronger stress dependence.
  - [non-referenced_knowledge] Threshold stress (σ_thr) increases with reinforcement content due to Orowan looping around SiCp particles.
  - [referenced knowledge] True stress exponent nt (5.4–5.8) corresponds to dislocation climb controlled by lattice diffusion [21].
  - [non-referenced_knowledge] Grain refinement and particle dispersion restrict grain boundary sliding and dislocation glide, forcing climb as dominant mechanism.
  - [deductive reasoning] Thus, structure enhances creep resistance by altering deformation mechanism to higher-energy dislocation climb.
### M4  Property → Performance
- cause: Increased yield strength, ultimate compressive strength, and reduced minimum creep rate
- effect: Improved creep resistance and mechanical performance of AZ91-SiCp composites at 175 °C under 80–120 MPa stress
- experiment: Creep performance evaluation under service-like conditions | Compression creep test at 175 °C | params: Stresses: 80, 100, 120 MPa; duration monitored until failure or stabilization | result: Composites with 15–25 wt% SiCp showed significantly longer creep life and lower strain rates under load, indicating improved performance
  - [experimental result] Yield strength and compressive strength increase with SiCp content.
  - [experimental result] Minimum creep rate decreases and true stress exponent remains near 5.5–5.8, indicating stable creep behavior.
  - [non-referenced_knowledge] Creep resistance is critical for components operating above 150 °C, such as engine parts [8].
  - [image description] Composites with 15–25 wt% SiCp show significantly longer creep life under 80–120 MPa.
  - [deductive reasoning] Thus, enhanced properties directly translate to improved performance in real-world high-temperature applications.
### M5  Processing → Performance
- cause: Stir casting with preheated SiC particles added at 750 °C under argon atmosphere
- effect: Improved creep resistance and mechanical performance of AZ91-SiCp composites at 175 °C under 80–120 MPa stress
- experiment: Creep and tensile testing of stir-cast composites | Compression creep test, tensile test | params: Creep: 175 °C, 80–120 MPa; Tensile: ASTM E8, 2 mm/min crosshead speed | result: Composites produced via stir casting showed up to 40% improvement in creep resistance and 25% increase in yield strength compared to base alloy
  - [experimental result] Stir casting was performed at 750 °C with 750 rpm stirring and 10 min mixing after SiCp addition.
  - [image description] This process produced near-uniform SiCp distribution and grain refinement (22 microns at 10 wt%).
  - [non-referenced_knowledge] Grain refinement and dispersion improved yield strength and reduced creep rate.
  - [referenced knowledge] True stress exponent of 5.4–5.8 confirms dislocation climb control, indicating stable creep behavior.
  - [deductive reasoning] Thus, stir casting directly enables superior creep performance under operational loads.
