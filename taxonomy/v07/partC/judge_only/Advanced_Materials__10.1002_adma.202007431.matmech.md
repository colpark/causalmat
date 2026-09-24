# MatMech content for Advanced_Materials/10.1002_adma.202007431 (judge only; not shown to staff)
- material: HL38  elements: ['C', 'H', 'O', 'N', 'S', 'Li', 'F', 'I']  category: ['Polymer', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Doping with lithium bis(trifluoromethanesulfonyl)imide and 4-tert-butylpyridine as additives, interface engineering with 2-(2-aminoethyl)thiophene hydroiodide (2-TEAl)
- **Structure**: Strong complexation of Li+ with HL38, lower lithium ion diffusivity
- **Properties**: hole mobility–electrical property, glass transition temperature–thermal property
- **Performance**: Retains 85.9% of initial PCE after 1000 hours at 85°C
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Doping with lithium bis(trifluoromethanesulfonyl)imide and 4-tert-butylpyridine as additives
- effect: Strong complexation of Li+ with HL38, lower lithium ion diffusivity
- experiment: ToF-SIMS depth profiling | Time-of-flight secondary-ion mass spectrometry | params: Aging at 85°C for 1032 hours | result: Less Li+ diffusion observed in HL38-based devices compared to spiro-MeOTAD
  - [experimental result] Doping HL38 with LiTFSI and tBP significantly lowers Li+ ion diffusivity compared to spiro-MeOTAD.
  - [image description] ToF-SIMS shows limited Li+ migration from HL38 to perovskite layer after thermal aging.
  - [non-referenced_knowledge] Carbonyl groups in HL38 are known to interact strongly with Li+ ions, forming stable complexes.
  - [deductive reasoning] Therefore, doping HL38 with LiTFSI results in strong Li+ complexation due to interaction with carbonyl groups, reducing ion mobility.
### M2  Structure → Performance
- cause: Strong complexation of Li+ with HL38, lower lithium ion diffusivity
- effect: Retains 85.9% of initial PCE after 1000 hours at 85°C
- experiment: Thermal aging test | Accelerated thermal stability testing | params: PSCs aged at 85°C for 1032 hours | result: HL38 retains 85.9% of initial PCE; spiro-MeOTAD degrades to 27% of its initial value
  - [experimental result] HL38 shows significantly reduced Li+ ion migration compared to spiro-MeOTAD.
  - [image description] Image analysis confirms minimal Li+ presence in the perovskite layer after aging in HL38-based devices.
  - [non-referenced_knowledge] Reduced Li+ migration preserves interfacial integrity and prevents conductivity loss in the hole transport layer.
  - [deductive reasoning] Thus, suppressed Li+ diffusion in HL38 enhances thermal stability by maintaining structural and electrical integrity under prolonged heating.
### M3  Processing → Property
- cause: Interface engineering with 2-(2-aminoethyl)thiophene hydroiodide (2-TEAl)
- effect: Improved charge extraction and increased open-circuit voltage
- experiment: TRPL spectroscopy and J-V curve analysis | Time-resolved photoluminescence and current-voltage measurements | params: Post-treatment with varying concentrations of 2-TEAI | result: Photoluminescence lifetime decreases, indicating improved charge transfer; PCE increases from 19.60% to 21.98%
  - [experimental result] Treatment with 2-TEAI increases PCE from 19.60% to 21.98%, mainly due to higher V_oc.
  - [image description] TRPL decay becomes faster after 2-TEAI treatment, indicating more efficient charge extraction.
  - [experimental result] UPS measurements show improved valence band alignment between perovskite and HL38 after 2-TEAI treatment.
  - [non-referenced_knowledge] Better band alignment reduces interfacial resistance and minimizes non-radiative recombination.
  - [deductive reasoning] Thus, 2-TEAI treatment enhances photovoltaic performance by optimizing charge extraction and reducing recombination losses.
