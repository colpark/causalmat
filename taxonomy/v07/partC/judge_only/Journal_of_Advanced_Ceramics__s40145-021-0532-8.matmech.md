# MatMech content for Journal_of_Advanced_Ceramics/s40145-021-0532-8 (judge only; not shown to staff)
- material: Ba₀.₁₀₅Na₀.₃₂₅Sr₀.₂₄₅₋₁.₅ₓ□₀.₅ₓBi₀.₃₂₅₊ₓTiO₃ (BNS₀.₂₄₅₋₁.₅ₓ□₀.₅ₓBi₀.₃₂₅₊ₓT)  elements: ['Ba', 'Na', 'Sr', 'Bi', 'Ti', 'O']  category: ['Ceramic', 'Crystalline Material']
- MST chain: Processing → Structure → Properties → Performance
## Tetrahedron elements
- **Processing**: Pressureless solid-state sintering at 1180–1240 °C for 2 h in air, followed by furnace cooling
- **Structure**: Pseudocubic perovskite structure with Sr vacancies and enhanced polar nanoregions (PNRs); reduced grain boundary effects and increased lattice distortion
- **Properties**: recoverable energy storage density–energy storage property, dielectric constant–dielectric property, remnant polarization–ferroelectric property, energy efficiency–energy storage property
- **Performance**: High recoverable energy density (1.8 J/cm³) at low electric field (110 kV/cm), excellent temperature stability (±15% dielectric constant from 40–350 °C), high charge–discharge rate (t₀.₉ ≈ 0.1 μs), and fatigue endurance over 10⁵ cycles
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Pressureless solid-state sintering at 1180–1240 °C for 2 h in air, followed by furnace cooling
- effect: Formation of pseudocubic perovskite structure with Sr vacancies and enhanced polar nanoregions (PNRs); increased grain size and densification
- experiment: Solid-state sintering process | Pressureless sintering | params: 1180–1240 °C for 2 h in air, furnace cooling | result: High-density ceramics with uniform grain morphology and no secondary phases
  - [experimental result] Ceramics are sintered at 1180–1240 °C for 2 h in air, followed by furnace cooling.
  - [non-referenced_knowledge] Bi³⁺ replaces Sr²⁺ on the A-site, requiring charge compensation via Sr vacancy formation.
  - [non-referenced_knowledge] Sr vacancies induce lattice strain, reducing grain boundary competition and accelerating mass transfer.
  - [image description] SEM images show increased grain size with higher x values, confirming enhanced densification and grain growth.
  - [experimental result] XRD confirms pure pseudocubic perovskite phase without secondary phases, indicating structural homogeneity.
  - [deductive reasoning] Thus, sintering conditions and A-site substitution synergistically produce a dense, vacancy-stabilized perovskite structure.
### M2  Structure → Property
- cause: Sr vacancies and enhanced polar nanoregions (PNRs) in pseudocubic perovskite structure
- effect: Reduced remnant polarization (Pᵣ) and improved thermal evolution of PNRs, leading to enhanced dielectric temperature stability and relaxor behavior
- experiment: Raman spectroscopy and dielectric measurement | Raman spectroscopy, impedance analyzer | params: Temperature range: 25–275 °C; frequency: 1 kHz–1 MHz | result: ν₂ and ν₆ Raman modes shift gradually with temperature; dielectric peak at Tₘ₂ emerges and shifts with x; TCC ≤ ±15% from 40–350 °C for x=0.06
  - [non-referenced_knowledge] Sr vacancies are formed due to Bi³⁺ substitution for Sr²⁺ during synthesis.
  - [experimental result] Raman spectra show gradual shifts in ν₂ and ν₆ modes with temperature, indicating continuous structural evolution without abrupt phase transition.
  - [experimental result] Dielectric measurements reveal a new peak Tₘ₂ that increases with x, attributed to thermal evolution of PNRs.
  - [experimental result] TCC remains ≤ ±15% from 40–350 °C for x=0.06, demonstrating exceptional temperature stability.
  - [referenced knowledge] PNRs are dynamically sensitive to thermal stimuli and are stabilized by vacancy-induced local disorder.
  - [deductive reasoning] Thus, Sr vacancies enhance relaxor behavior by suppressing long-range order and enabling smooth thermal evolution of PNRs.
### M3  Structure → Property
- cause: Increased lattice distortion and reduced grain boundary effects due to Sr vacancies
- effect: Enhanced energy efficiency (η) and recoverable energy density (Wᵣₑ𝒸)
- experiment: P–E hysteresis loop measurement | Ferroelectric analyzer (Trek 609B) | params: Electric field: 60 kV/cm, frequency: 10 Hz, temperature: room temperature | result: P–E loops become slimmer with increasing x; maximum Pₘₐₓ–Pᵣ = 27.52 μC/cm² at x=0.06; η reaches 72% at x=0.06
  - [experimental result] Raman and XRD data confirm increased lattice distortion with higher x values.
  - [experimental result] P–E loops become progressively slimmer with increasing x, indicating reduced hysteresis loss.
  - [experimental result] Pᵣ decreases sharply at x=0.06, while Pₘₐₓ–Pᵣ peaks at 27.52 μC/cm².
  - [non-referenced_knowledge] Slender loops imply that polarization is more reversible under field reversal.
  - [deductive reasoning] Thus, lattice distortion from Sr vacancies enhances energy efficiency by minimizing irreversible polarization loss.
### M4  Property → Performance
- cause: High recoverable energy density (Wᵣₑ𝒸 = 1.8 J/cm³) and energy efficiency (η = 72%) at low electric field (110 kV/cm)
- effect: Superior performance in pulsed power capacitor applications with high charge–discharge rate and fatigue endurance
- experiment: Charge–discharge measurement | RLC circuit (CFD-003) | params: Load resistance: 100 Ω, electric field: 80–110 kV/cm, temperature: 30–150 °C, cycle number: up to 10⁵ | result: t₀.₉ ≈ 0.1 μs; W𝒹 ≈ 1.5 J/cm³ at 110 kV/cm; Wᵣₑ𝒸 and η remain stable over 10⁵ cycles and temperature range
  - [experimental result] Wᵣₑ𝒸 reaches 1.8 J/cm³ at 110 kV/cm, the highest among lead-free ceramics under <160 kV/cm.
  - [experimental result] η reaches 72% at x=0.06, indicating minimal energy loss during charge–discharge cycles.
  - [experimental result] Discharge time t₀.₉ is 0.1 μs, enabling pulse power delivery.
  - [experimental result] Wᵣₑ𝒸 and η remain stable over 10⁵ cycles and temperatures from 30–150 °C.
  - [deductive reasoning] Thus, the optimized properties directly enable high-performance pulsed power capacitor operation.
### M5  Processing → Performance
- cause: Pressureless solid-state sintering at 1180–1240 °C with A-site defect engineering
- effect: Achievement of high recoverable energy density (1.8 J/cm³), excellent temperature stability (±15% from 40–350 °C), and fatigue endurance over 10⁵ cycles
- experiment: Sintering and performance testing | Solid-state sintering, dielectric, P–E, and discharge measurements | params: Sintering: 1180–1240 °C; testing: 10 Hz, 30–350 °C, 10⁵ cycles | result: Wᵣₑ𝒸 = 1.8 J/cm³ at 110 kV/cm; TCC ≤ ±15% from 40–350 °C; no degradation after 10⁵ cycles
  - [non-referenced_knowledge] A-site defect engineering is introduced by adjusting Bi/Sr ratio during synthesis.
  - [experimental result] Pressureless sintering at 1180–1240 °C enables full densification and vacancy stabilization without secondary phases.
  - [experimental result] This results in reduced Pᵣ and enhanced PNR thermal evolution, as confirmed by P–E and dielectric measurements.
  - [experimental result] Consequently, Wᵣₑ𝒸 reaches 1.8 J/cm³ at 110 kV/cm and TCC remains within ±15% from 40–350 °C.
  - [experimental result] Fatigue tests confirm stability over 10⁵ cycles, proving robustness.
  - [deductive reasoning] Thus, the sintering process with A-site engineering directly enables the observed high performance.
