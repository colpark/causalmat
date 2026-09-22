# MatMech content for Bioactive_Materials/j.bioactmat.2020.02.005 (judge only; not shown to staff)
- material: Ce and Er co-doped TiO₂  elements: ['Ce', 'Er', 'Ti', 'O']  category: ['Crystalline Material', 'Nanomaterial', 'Ceramic']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Sol-gel method followed by calcination at 800 °C
- **Structure**: Mixed anatase-rutile phase with Er³⁺ and Ce³⁺/Ce⁴⁺ ions doped into TiO₂ lattice, surface defects, and up-conversion properties
- **Properties**: Band gap reduction–optical property, photoluminescence intensity reduction–electronic property, photocatalytic activity–photocatalytic property
- **Performance**: Antibacterial efficiency of 91.23% against Staphylococcus aureus and 92.8% against Escherichia coli under visible light irradiation
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Sol–gel method followed by calcination at 800 °C
- effect: Formation of mixed anatase-rutile phase with Er³⁺ and Ce³⁺/Ce⁴⁺ ions doped into the TiO₂ lattice, surface defects, and up-conversion properties
- experiment: XRD analysis of Er–Ce co-doped TiO₂ | X-ray diffraction | params: Cu-Kα radiation (λ = 1.5406 Å), 2θ = 20–80°, calcination at 800 °C | result: Coexistence of anatase and rutile phases; no phase pure anatase or rutile observed
  - [experimental result] Er–Ce co-doped TiO₂ was synthesized via sol–gel method and calcined at 800 °C.
  - [experimental result] XRD spectra show coexistence of anatase and rutile phases, unlike undoped TiO₂ which fully transforms to rutile at 900 °C.
  - [referenced knowledge] Er doping delays anatase-to-rutile transition, as reported in literature.
  - [non-referenced_knowledge] Ce and Er ions substitute Ti⁴⁺ sites due to interstitial channels in anatase structure.
  - [deductive reasoning] Mixed-phase structure with dopant incorporation creates lattice distortions and surface defects.
  - [deductive reasoning] Thus, processing via sol–gel and 800 °C calcination yields a mixed-phase structure with doped rare-earth ions and defects.
### M2  Structure → Properties
- cause: Mixed anatase-rutile phase with Er³⁺ and Ce³⁺/Ce⁴⁺ doping and surface defects
- effect: Reduced band gap, enhanced visible light absorption, suppressed electron-hole recombination (lower PL intensity), and up-conversion of NIR to visible light
- experiment: DR UV–vis spectroscopy | Diffuse reflectance UV–vis spectroscopy | params: Wavelength range 200–800 nm, BaSO₄ reference | result: Co-doped sample Er0.5Ce0.2Ti–O shows significant red shift in absorption edge; band gap reduced to ~2.4 eV from 3.2 eV for pure TiO₂
  - [experimental result] UV–vis spectra show red shift in absorption edge for co-doped TiO₂, indicating band gap reduction.
  - [non-referenced_knowledge] Ce ions have incompletely occupied 4f and 5d orbitals that hybridize with TiO₂ bands, lowering the band gap.
  - [image description] Er³⁺ ions exhibit up-conversion luminescence under 808 nm and 980 nm excitation, converting NIR to visible light.
  - [experimental result] PL intensity is lowest for Er0.5Ce0.2Ti–O, indicating suppressed electron-hole recombination.
  - [referenced knowledge] Ce³⁺/Ce⁴⁺ states act as electron traps, while Er³⁺ intermediate levels facilitate charge transfer.
  - [deductive reasoning] Thus, the structure enables enhanced visible/NIR absorption and prolonged carrier lifetime.
### M3  Structure → Properties
- cause: Presence of Ce³⁺/Ce⁴⁺ mixed valence states on the surface
- effect: Enhanced photocatalytic activity and improved charge carrier separation efficiency
- experiment: XPS analysis of Er0.5Ce0.2Ti–O | X-ray photoelectron spectroscopy | params: Analysis of Ce 3d and Ti 2p core levels | result: Ce 3d spectra show peaks corresponding to both Ce⁴⁺ and Ce³⁺, confirming mixed valence state on surface
  - [experimental result] XPS reveals the presence of both Ce³⁺ and Ce⁴⁺ on the surface of Er0.5Ce0.2Ti–O.
  - [referenced knowledge] Ce³⁺/Ce⁴⁺ redox couples can accept and donate electrons under irradiation.
  - [non-referenced_knowledge] This facilitates charge transfer and reduces electron-hole recombination rate.
  - [deductive reasoning] Thus, surface Ce mixed valence enhances photocatalytic activity.
### M4  Properties → Performance
- cause: Enhanced visible light absorption and suppressed electron-hole recombination
- effect: High antibacterial efficiency of 91.23% against S. aureus and 92.8% against E. coli under visible light
- experiment: Antibacterial assay with spread plate method | Colony-forming unit (CFU) counting | params: 5000 ppm nanoparticles, 20 min visible light irradiation (simulated sunlight, 2 kW/m²), 37°C incubation | result: Er0.5Ce0.2Ti–O achieves 91.23% and 92.8% antibacterial efficiency against S. aureus and E. coli, respectively
  - [experimental result] Er0.5Ce0.2Ti–O shows highest visible light absorption and lowest PL intensity among all samples.
  - [non-referenced_knowledge] Lower PL intensity indicates reduced electron-hole recombination and higher ROS generation potential.
  - [experimental result] Photocatalytic degradation of MO (46.13% in 60 min) confirms high activity under visible light.
  - [referenced knowledge] ROS such as ·OH and ·O₂⁻ are known to disrupt bacterial membranes and cellular components.
  - [deductive reasoning] Thus, enhanced photocatalytic properties lead to higher ROS production and superior antibacterial performance.
### M5  Processing → Properties
- cause: Calcination at 800 °C
- effect: Optimal mixed-phase structure enabling band gap reduction and up-conversion
- experiment: XRD comparison at different calcination temperatures | X-ray diffraction | params: Samples calcined at 700 °C, 800 °C, and 900 °C | result: At 800 °C: mixed phase; at 700 °C: pure anatase; at 900 °C: pure rutile
  - [experimental result] TiO₂ calcined at 800 °C exhibits both anatase and rutile phases (XRD).
  - [experimental result] Pure anatase forms at 700 °C, pure rutile at 900 °C.
  - [referenced knowledge] Mixed-phase TiO₂ is known to enhance photocatalytic activity due to heterojunction-mediated charge separation.
  - [experimental result] Band gap is minimized and visible absorption maximized at 800 °C calcination.
  - [deductive reasoning] Thus, 800 °C calcination produces the optimal structure for enhanced photocatalytic properties.
### M6  Processing → Performance
- cause: Optimal doping concentration (0.5 mol% Er, 0.2 mol% Ce) and calcination at 800 °C
- effect: Maximum antibacterial efficiency of 91.23% and 92.8% against S. aureus and E. coli
- experiment: Antibacterial efficiency test across doping concentrations | CFU counting under visible light | params: Er doping: 0.25–1.0 mol%; Ce doping: 0.1–0.5 mol%; calcination: 800 °C | result: Peak antibacterial efficiency at 0.5 mol% Er and 0.2 mol% Ce; efficiency drops with higher or lower doping
  - [experimental result] Antibacterial efficiency increases with Er doping up to 0.5 mol%, then decreases.
  - [experimental result] Same trend observed for Ce doping, with peak at 0.2 mol%.
  - [referenced knowledge] Higher doping causes quenching of up-conversion and increased recombination centers.
  - [experimental result] 800 °C calcination produces optimal mixed-phase structure for photocatalysis.
  - [deductive reasoning] Thus, the combination of optimal doping and calcination yields maximum ROS production and antibacterial performance.
