# MatMech content for Advanced_Functional_Materials/10.1002_adfm.202009307 (judge only; not shown to staff)
- material: Redox-active metallopolymers (polyvinylferrocene and polyferrocenylsilane)  elements: ['C', 'H', 'Fe', 'Si']  category: ['Polymer', 'Composite Material']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Electrochemical adsorption and separation factor experiments using chronoamperometry
- **Structure**: Main-chain metallopolymer (polyferrocenylsilane) and pendant-group metallopolymer (polyvinylferrocene)
- **Properties**: Selectivity for transition metal oxyanions–electrochemical property
- **Performance**: Selective capture of heavy metal oxyanions in multicomponent mixtures for environmental remediation and metal recovery
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Electrochemical adsorption and separation factor experiments using chronoamperometry
- effect: Polyvinylferrocene (PVF) undergoes a single-electron oxidation while polyferrocenylsilane (PFS) undergoes a two-electron oxidation due to adjacent ferrocene–ferrocene interactions in the main-chain.
- experiment: Cyclic voltammogram analysis | Electrochemical testing | params: 5 mV/s scan rate in 100 mM NaClO4 under N2 purge | result: PVF-CNT shows one oxidation wave; PFS-CNT shows two oxidation waves indicating distinct redox mechanisms
  - [experimental result] Cyclic voltammograms show distinct oxidation patterns for PVF and PFS electrodes.
  - [image description] Figure 1b,d shows two oxidation waves for PFS-CNT compared to one for PVF-CNT.
  - [referenced knowledge] Main-chain ferrocene polymers exhibit multi-step oxidation due to inter-ferrocene electronic coupling.
  - [non-referenced_knowledge] PFS has adjacent ferrocene units in the polymer backbone while PVF has isolated ferrocene side groups.
  - [deductive reasoning] Thus, the structural difference between main-chain and pendant-group polymers causes distinct redox behavior during electrochemical processing.
### M2  Structure → Property
- cause: Main-chain structure of polyferrocenylsilane (PFS) with electron-donating silane groups
- effect: Lower binding energies to transition metal oxyanions compared to pendant-group polyvinylferrocene (PVF)
- experiment: Quantum mechanical calculations of anion binding | Density-functional theory calculations | params: Binding energy calculations for six oxyanions to Fc+ and FcSi(CH3)3+ | result: All anions showed lower binding energy to FcSi(CH3)3+ than to Fc+
  - [experimental result] DFT calculations show lower binding energies for all six oxyanions to FcSi(CH3)3+ compared to Fc+.
  - [image description] Figure 4c,d compares binding energies showing consistent reduction in anion binding to FcSi(CH3)3+.
  - [referenced knowledge] Electron-donating substituents reduce cation-anion binding by delocalizing positive charge.
  - [non-referenced_knowledge] Silane groups donate electrons to ferrocene units in PFS while PVF has no such substituents.
  - [deductive reasoning] Therefore, the structural difference in substituent effects leads to reduced anion binding strength in PFS compared to PVF.
### M3  Property → Performance
- cause: Potential-dependent selectivity of ferrocene polymers
- effect: Ability to reverse ion preference between competing oxyanions like MoO4²⁻ and CrO4²⁻ based solely on applied potential
- experiment: Separation factor measurements at varying potentials | Chronoamperometric electrosorption tests | params: 1 mM each of competing oxyanions in solution with 20 mM NaClO4 supporting electrolyte | result: Separation factor αMoO4,CrO4 increases from 0.28 at 0.5 V to 1.5 at 1.0 V vs Ag/AgCl for PVF-CNT
  - [experimental result] Separation factor measurements show reversed ion preference at different potentials.
  - [image description] Figure 5a,b demonstrates inversion of α values across 0.5-1.0 V range for two anion pairs.
  - [referenced knowledge] Higher electrode charge density favors ions transferring more charge to satisfy charge neutrality.
  - [non-referenced_knowledge] Ion selectivity depends on both structural affinity and electrostatic driving forces from charge density.
  - [deductive reasoning] Therefore, potential-dependent charge density changes enable reversible control over ion selectivity beyond structural determinants.
### M4  Structure → Property
- cause: Main-chain vs pendant-group architecture of PFS and PVF
- effect: Different selectivity trends for transition metal oxyanions in binary competitive adsorption tests
- experiment: Binary ion-selectivity heat maps | Competitive adsorption tests | params: 1 mM each of two oxyanion sodium salts in solution with 20 mM NaClO4 | result: PFS-CNT selects MoO4²⁻ over CrO4²⁻ (α=2.4), while PVF-CNT prefers CrO4²⁻ (α=0.60)
  - [experimental result] Competitive adsorption tests reveal different selectivity trends for PFS-CNT and PVF-CNT.
  - [image description] Figure 3 heat maps show PFS-CNT favoring MoO4²⁻ over CrO4²⁻ while PVF-CNT shows opposite preference.
  - [referenced knowledge] Polymer structure determines charge distribution and binding geometry affecting ion selectivity.
  - [non-referenced_knowledge] PFS has main-chain ferrocene units with silane substituents while PVF has pendant ferrocene groups.
  - [deductive reasoning] Thus, structural differences between main-chain and pendant-group polymers cause distinct ion selectivity profiles.
