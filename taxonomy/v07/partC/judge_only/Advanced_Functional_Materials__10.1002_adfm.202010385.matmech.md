# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202010385 (judge only; not shown to staff)
- material: SnO2  elements: ['Sn', 'O', 'Rb', 'F']  category: ['Ceramic', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Modification with rubidium fluoride (RbF) via two methods: adding RbF into SnO2 colloidal dispersion and depositing RbF at the SnO2/perovskite interface
- **Structure**: Formation of F-Sn bonds, Rb+ cations escaping into interstitial sites of the perovskite lattice
- **Properties**: electron mobility–electrical property, conductivity–electrical property, open-circuit voltage–electrical property
- **Performance**: Improved power conversion efficiency (PCE) of perovskite solar cells (PSCs), suppressed hysteresis, reduced ion migration in perovskite
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Adding RbF into SnO2 colloidal dispersion
- effect: Formation of F-Sn bonds, changing electron cloud density around Sn atoms
- experiment: XPS analysis | X-ray photoelectron spectroscopy | params: Comparing SnO2 films with and without RbF treatment | result: Sn 3d peak shifts ~0.3 eV toward lower binding energy for SnO2-RbF, indicating changed electron cloud density
  - [experimental result] XPS shows a shift in the Sn 3d peak for SnO2-RbF, indicating a change in electron cloud density around Sn atoms.
  - [image description] The Sn 3d peak shift suggests strong bonding between F and Sn when RbF is introduced into the bulk SnO2.
  - [referenced knowledge] Strong bonding between F and Sn changes electron cloud density.
  - [non-referenced_knowledge] Dopants like F⁻ can alter the electronic structure of metal oxides by forming strong bonds with cations like Sn⁴⁺.
  - [deductive reasoning] Thus, the introduction of RbF into SnO2 modifies its structure through F–Sn bonding, which changes the electron distribution and enhances electron mobility.
### M2  Structure → Property
- cause: Formation of F–Sn bonds in SnO2
- effect: Improved electron mobility and conductivity of SnO2
- experiment: Space charge-limited current (SCLC) measurements | Electron mobility measurement | params: Device structure: ITO/Al/ETL/Al | result: Electron mobility increases from 3.65×10⁻⁴ cm² V⁻¹ s⁻¹ (SnO2) to 5.69×10⁻⁴ cm² V⁻¹ s⁻¹ (SnO2-RbF)
  - [experimental result] SCLC measurements show increased electron mobility in SnO2-RbF compared to pure SnO2.
  - [image description] I–V curves indicate higher conductivity for SnO2-RbF films.
  - [referenced knowledge] Enhanced electron mobility improves charge transport at ETL/perovskite interface.
  - [non-referenced_knowledge] Optimized bonding environment around Sn atoms reduces electron scattering, improving mobility.
  - [deductive reasoning] Therefore, F–Sn bonding in SnO2 directly enhances its electrical properties, leading to better electron transport performance.
### M3  Structure → Property
- cause: Rb⁺ cations escaping into perovskite lattice interstitial sites
- effect: Reduced ion migration and non-radiative recombination
- experiment: Time-of-flight secondary ion mass spectrometry (ToF-SIMS) | Depth profiling | params: Analyzing Rb⁺ and F⁻ distribution across SnO2/perovskite interface | result: Rb⁺ distributes homogeneously in perovskite layer while F⁻ remains at the interface
  - [experimental result] ToF-SIMS shows Rb⁺ penetrating into the perovskite layer while F⁻ remains at the interface.
  - [image description] Figure shows homogeneous Rb⁺ distribution in perovskite, suggesting interstitial occupation.
  - [referenced knowledge] Interstitial halogen defects are major sources of traps in mixed halide perovskites.
  - [referenced knowledge] Alkali metals like Rb⁺ reduce deep traps by interacting with interstitial halide defects.
  - [non-referenced_knowledge] By occupying interstitial sites, Rb⁺ suppresses ion migration and stabilizes the perovskite lattice.
  - [inductive reasoning] Hence, Rb⁺ incorporation into perovskite interstitial sites inhibits ion migration and reduces trap density, decreasing non-radiative recombination.
### M4  Property → Performance
- cause: Increased electron mobility and reduced interfacial recombination
- effect: Higher short-circuit current (Jsc) and improved power conversion efficiency (PCE)
- experiment: Photoluminescence (PL) and time-resolved PL (TRPL) measurements | Charge carrier dynamics characterization | params: Excitation wavelength: 485 nm; measuring steady-state and time-resolved PL intensity | result: SnO2-RbF-based perovskite films show stronger PL intensity and faster decay times, indicating better charge extraction
  - [experimental result] TRPL shows shorter τ₁ (42.68 ns) for SnO2-RbF/perovskite, indicating faster charge extraction.
  - [image description] PL intensity is higher for RbF-modified films, suggesting fewer defects and better charge transport.
  - [referenced knowledge] Fast decay component corresponds to charge quenching at ETL/perovskite interface.
  - [non-referenced_knowledge] Faster charge extraction reduces recombination losses and increases collected current.
  - [deductive reasoning] Therefore, enhanced electron mobility and reduced interfacial recombination directly lead to higher Jsc and improved PCE.
### M5  Property → Performance
- cause: Suppressed ion migration and reduced trap density
- effect: Higher open-circuit voltage (Voc) and reduced hysteresis in PSCs
- experiment: Dark I–V measurements on electron-only devices | Trap density evaluation | params: Device structure: ITO/various SnO2/perovskite/PCBM/Ag | result: Trap density decreases from 1.88×10¹⁵ cm⁻³ (SnO2) to 1.12×10¹⁵ cm⁻³ (SnO2/RbF)
  - [experimental result] Dark I–V measurements show reduced trap density in SnO2/RbF-based devices.
  - [image description] Image shows lower trap-filled limit voltage for RbF-modified devices, indicating fewer traps.
  - [referenced knowledge] Interstitial halogen defects are major trap contributors in perovskite.
  - [referenced knowledge] Rb⁺ binds to interstitial halogen defects, reducing deep trap density.
  - [non-referenced_knowledge] Fewer traps mean less non-radiative recombination, which increases open-circuit voltage.
  - [deductive reasoning] Therefore, reduced trap density from Rb⁺ incorporation leads to higher Voc and suppressed hysteresis in PSCs.
