# MatMech content for Bioactive_Materials/j.bioactmat.2019.12.001 (judge only; not shown to staff)
- material: Mg alloy AZ31  elements: ['Mg', 'Al', 'Zn', 'Ta', 'O']  category: ['Metals and Alloys', 'Ceramic', 'Nanomaterial', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Micro-arc oxidation (MAO) followed by atomic layer deposition (ALD) of Ta₂O₅ nanofilm (500 cycles)
- **Structure**: Amorphous Ta₂O₅ nanofilm sealing micropores and microcracks in MAO coating; MgO phases in MAO layer
- **Properties**: Corrosion current density (i_corr)–electrochemical property; Impedance modulus (|Z|)–electrochemical property
- **Performance**: Enhanced long-term corrosion resistance in Hank's solution; reduced hydrogen evolution; suppression of pitting corrosion compared to MAO-only coating
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Micro-arc oxidation (MAO) followed by atomic layer deposition (ALD) of Ta₂O₅ nanofilm (500 cycles)
- effect: Amorphous Ta₂O₅ nanofilm sealing micropores and microcracks in MAO coating; MgO phases in MAO layer
- experiment: ALD deposition of Ta₂O₅ on MAO-coated AZ31 | Atomic Layer Deposition | params: 500 cycles, Ta precursor: C₁₆H₃₉N₄Ta, O precursor: H₂O, temperature: 130°C (Ta), 20°C (H₂O), purge gas: N₂ (8 sccm), growth rate: 0.1 nm/cycle | result: Ta₂O₅ film thickness ≈ 50 nm; uniform coverage confirmed by SEM and EDS
  - [non-referenced_knowledge] MAO coating on AZ31 has inherent micropores and microcracks due to spark discharge during anodization.
  - [experimental result] ALD uses self-limiting surface reactions with Ta precursor (C₁₆H₃₉N₄Ta) and H₂O to deposit Ta₂O₅ one atomic layer at a time.
  - [non-referenced_knowledge] The MAO surface contains abundant –OH functional groups that react with Ta precursor to form Ta–O–Ta intermediates.
  - [experimental result] XPS confirms Ta 4d and O 1s peaks consistent with Ta₂O₅ and residual N–Ta bonds from incomplete precursor reaction.
  - [image description] SEM and EDS show uniform Ta distribution and significant reduction in pore size after ALD.
  - [experimental result] XRD shows no crystalline Ta₂O₅ peaks, indicating amorphous structure, which enhances sealing by lacking grain boundary pathways.
  - [deductive reasoning] Thus, ALD forms a dense, amorphous Ta₂O₅ nanofilm that conformally seals MAO micropores and microcracks.
### M2  Structure → Property
- cause: Amorphous Ta₂O₅ nanofilm sealing micropores and microcracks in MAO coating
- effect: Corrosion current density (i_corr) decreased three orders of magnitude; impedance modulus (|Z|) increased two to three orders of magnitude
- experiment: Potentiodynamic polarization (PDP) | Electrochemical test | params: Sweep rate: 1 mV/s, range: -2.0 to -0.8 V/SCE, electrolyte: Hank's solution | result: i_corr decreased from 1.05×10⁻⁶ A/cm² (MAO) to 2.23×10⁻⁹ A/cm² (MAO/Ta₂O₅)
  - [structure description] Ta₂O₅ nanofilm seals micropores and microcracks in MAO coating, eliminating direct pathways for aggressive ions.
  - [experimental result] PDP results show i_corr of MAO/Ta₂O₅ is 3 orders of magnitude lower than MAO coating.
  - [experimental result] EIS Bode plots show |Z| at low frequency increased by two orders of magnitude for MAO/Ta₂O₅ vs. MAO.
  - [experimental result] Equivalent circuit fitting reveals R_ct increased from 1.23×10⁵ to 3.99×10⁶ Ω·cm², indicating suppressed charge transfer.
  - [non-referenced_knowledge] Ta₂O₅ is chemically inert and amorphous, minimizing defect-mediated ion transport.
  - [deductive reasoning] Therefore, the sealed structure directly enhances electrochemical properties by blocking corrosion reactions.
### M3  Property → Performance
- cause: Corrosion current density (i_corr) decreased three orders of magnitude; impedance modulus (|Z|) increased two to three orders of magnitude
- effect: Enhanced long-term corrosion resistance in Hank's solution; reduced hydrogen evolution; suppression of pitting corrosion compared to MAO-only coating
- experiment: Hydrogen evolution test (HER) | Immersion test | params: Immersion in Hank's solution for 294 h at 37.5°C, surface area to volume ratio: 40 mL/cm² | result: HER of MAO/Ta₂O₅ remained stable after 168 h, while MAO and substrate showed sharp increases due to coating failure.
  - [experimental result] i_corr of MAO/Ta₂O₅ is 2.23×10⁻⁹ A/cm², three orders lower than MAO (1.05×10⁻⁶ A/cm²).
  - [experimental result] |Z| at 0.01 Hz is two orders higher for MAO/Ta₂O₅ than MAO, indicating superior barrier performance.
  - [experimental result] HER test shows MAO/Ta₂O₅ maintains stable hydrogen evolution after 168 h, while MAO increases sharply due to coating failure.
  - [image description] Macro- and micro-morphology after 294 h show MAO/Ta₂O₅ coating remains mostly intact, with only isolated pits.
  - [experimental result] EDS shows no Ca–P corrosion products on MAO/Ta₂O₅ surface, indicating minimal substrate exposure.
  - [deductive reasoning] Therefore, low i_corr and high |Z| directly enable long-term performance by preventing electrolyte access and hydrogen-induced damage.
### M4  Processing → Performance
- cause: Micro-arc oxidation (MAO) followed by atomic layer deposition (ALD) of Ta₂O₅ nanofilm (500 cycles)
- effect: Enhanced long-term corrosion resistance in Hank's solution; reduced hydrogen evolution; suppression of pitting corrosion compared to MAO-only coating
- experiment: Hydrogen evolution test (HER) and immersion morphology | Immersion test | params: 294 h in Hank's solution at 37.5°C | result: MAO/Ta₂O₅ showed stable HER and minimal surface damage; MAO showed rapid HER increase and severe pitting.
  - [non-referenced_knowledge] MAO alone forms a porous oxide layer with microcracks, allowing ion penetration and galvanic corrosion.
  - [experimental result] ALD of Ta₂O₅ seals these defects, creating a continuous, amorphous barrier.
  - [experimental result] Electrochemical tests show i_corr and |Z| improvements confirm barrier effectiveness.
  - [experimental result] Hydrogen evolution and post-immersion SEM show MAO/Ta₂O₅ resists degradation for 294 h, unlike MAO or organic-sealed coatings.
  - [referenced knowledge] Organic sealers (PLA, chitosan) hydrolyze or peel, whereas Ta₂O₅ is chemically stable.
  - [deductive reasoning] Thus, the MAO/ALD processing sequence directly enables superior long-term performance.
