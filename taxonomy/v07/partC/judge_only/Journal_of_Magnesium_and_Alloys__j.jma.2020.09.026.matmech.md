# MatMech content for Journal_of_Magnesium_and_Alloys/j.jma.2020.09.026 (judge only; not shown to staff)
- material: AZ31/Ti-6Al-4V  elements: ['Mg', 'Al', 'Ti', 'V', 'Cr']  category: ['Composite Material', 'Metals and Alloys', 'Crystalline Material', 'Nanomaterial']
- MST chain: Processing → Structure → Properties
## Tetrahedron elements
- **Processing**: Friction stir processing (FSP) using a traditional vertical milling machine with rotational speed of 950 rpm, traverse speed of 30 mm/min, 5 passes, and Ti-6Al-4V particle content of 0 to 21 vol.%
- **Structure**: Homogeneous distribution of Ti-6Al-4V particles; grain refinement from 66.7 μm to 4.5 μm due to dynamic recrystallization; broken Ti-6Al-4V particles acting as pinning sites; dense dislocations in matrix; strong interfacial bonding without intermetallic compounds
- **Properties**: tensile strength–mechanical property, yield strength–mechanical property, elongation–ductility
- **Performance**: Improved tensile behavior and retained ductility compared to ceramic-reinforced MMCs; ductile fracture mode observed
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Friction stir processing (FSP) using a traditional vertical milling machine with rotational speed of 950 rpm, traverse speed of 30 mm/min, 5 passes, and Ti-6Al-4V particle content of 0 to 21 vol.%
- effect: Homogeneous distribution of Ti-6Al-4V particles; grain refinement from 66.7 μm to 4.5 μm due to dynamic recrystallization; broken Ti-6Al-4V particles acting as pinning sites; dense dislocations in matrix; strong interfacial bonding without intermetallic compounds
- experiment: Friction stir processing (FSP) | Friction stir processing | params: Rotational speed: 950 rpm, Traverse speed: 30 mm/min, Passes: 5, Ti-6Al-4V content: 0–21 vol.%, Tool: H13 steel with frustum-of-cone pin, Shoulder diameter: 24 mm | result: Homogeneous distribution of Ti-6Al-4V particles, grain refinement, particle breakage, strong interface, no intermetallic compounds detected
  - [experimental result] FSP was performed using a traditional milling machine with 950 rpm rotation, 30 mm/min traverse speed, and 5 passes.
  - [image description] SEM and optical micrographs show homogeneous distribution of Ti-6Al-4V particles throughout the stir zone without agglomeration or segregation.
  - [image description] EBSD images reveal grain refinement from 66.7 μm to 4.5 μm with increased high-angle grain boundaries (40–50%).
  - [non-referenced_knowledge] Dynamic recrystallization is a known mechanism under severe plastic deformation at elevated temperatures.
  - [image description] TEM images show dense dislocations in the AZ31 matrix, attributed to plastic deformation and thermal strain misfit between Ti-6Al-4V and the matrix.
  - [image description] Line EDAX across particle-matrix interface shows no Al diffusion or compound formation, confirming absence of Al3Ti or other brittle phases.
  - [non-referenced_knowledge] FSP operates below the melting point of the matrix, preventing chemical reactions and enabling solid-state bonding.
  - [non-referenced_knowledge] Large Ti-6Al-4V particles fracture under severe plastic strain, creating submicron debris that act as pinning sites hindering grain growth.
  - [deductive reasoning] Thus, FSP parameters induce microstructural changes including homogeneity, grain refinement, dislocation density, and strong interfaces without intermetallics.
### M2  Structure → Properties
- cause: Homogeneous distribution of Ti-6Al-4V particles; grain refinement from 66.7 μm to 4.5 μm due to dynamic recrystallization; broken Ti-6Al-4V particles acting as pinning sites; dense dislocations in matrix; strong interfacial bonding without intermetallic compounds
- effect: Tensile strength increased from 226 MPa to 322 MPa; yield strength increased from 98 MPa to 205 MPa; elongation retained at 9.3% (vs. 14.5% in base metal)
- experiment: Tensile testing | Tensile test | params: Strain rate: 0.5 mm/min; specimen dimensions: 25 mm gauge length, 4 mm width, 4 mm thickness | result: UTS increased from 226 MPa (0 vol.%) to 322 MPa (21 vol.%); yield strength increased from 98 MPa to 205 MPa; elongation decreased from 14.5% to 9.3%
  - [non-referenced_knowledge] Ti-6Al-4V particles have higher tensile strength (950–1050 MPa) than AZ31 matrix (~226 MPa), contributing to strengthening via rule of mixtures.
  - [referenced knowledge] Homogeneous distribution and fine particle size lead to Orowan strengthening, where dislocations bow around particles.
  - [image description] Grain size reduced from 66.7 μm to 4.5 μm, increasing grain boundary density and impeding dislocation motion per Hall-Petch relationship.
  - [image description] Dense dislocations in the matrix from plastic deformation and strain misfit further hinder dislocation motion.
  - [image description] Strong interfacial bonding without voids or intermetallics ensures efficient load transfer from matrix to particles.
  - [non-referenced_knowledge] Ti-6Al-4V particles are ductile and deform plastically under load, reducing stress concentration and enabling continued plastic flow in the matrix.
  - [deductive reasoning] Thus, combined strengthening mechanisms and ductile particle behavior lead to increased UTS, yield strength, and retained elongation.
### M3  Structure → Performance
- cause: Homogeneous distribution of Ti-6Al-4V particles; grain refinement from 66.7 μm to 4.5 μm due to dynamic recrystallization; broken Ti-6Al-4V particles acting as pinning sites; dense dislocations in matrix; strong interfacial bonding without intermetallic compounds
- effect: Improved tensile behavior and retained ductility compared to ceramic-reinforced MMCs; ductile fracture mode observed
- experiment: Tensile testing and fracture analysis | Tensile test and SEM fracture surface analysis | params: Strain rate: 0.5 mm/min; fracture surface examined via SEM | result: Ductile fracture mode observed with dimpled morphology; elongation (9.3%) significantly higher than SiC-reinforced AZ31 MMCs (reported ~3–5%)
  - [non-referenced_knowledge] Ti-6Al-4V particles are ductile and deform plastically under tensile load, unlike brittle ceramic particles.
  - [image description] Strong interfacial bonding prevents premature debonding and crack initiation at particle-matrix interfaces.
  - [image description] Fracture surface SEM images show dimpled morphology, indicative of ductile failure with microvoid coalescence.
  - [referenced knowledge] In contrast, SiC-reinforced AZ31 MMCs exhibit low elongation (<5%) and brittle fracture due to particle cracking and interface failure.
  - [deductive reasoning] Thus, the microstructure enables the composite to achieve both high strength and retained ductility, defining superior performance.
