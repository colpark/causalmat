# MatMech content for Advanced_Energy_Materials/aenm.202003738 (judge only; not shown to staff)
- material: NCM523||graphite lithium ion cell  elements: ['C', 'H', 'O', 'F', 'Li', 'Ni', 'Co', 'Mn', 'P']  category: ['Crystalline Material', 'Nanomaterial', 'Composite Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Use of ethylene carbonate (EC)-free electrolyte (1.0 M LiPF6 in ethyl methyl carbonate, EMC) without any additives
- **Structure**: Reduced transition metal (TM) deposits and suppressed Li dendrite formation on graphite anode; altered SEI composition with increased Li_xPO_yF_z species
- **Properties**: Electrochemical stability–electrical property, ionic conductivity–electrical property, transition metal scavenging–chemical property
- **Performance**: Rollover-free high-voltage performance at 4.5 V with suppressed capacity fade
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Use of ethylene carbonate (EC)-free electrolyte (1.0 M LiPF6 in ethyl methyl carbonate, EMC) without any additives
- effect: Reduced transition metal (TM) deposits and suppressed Li dendrite formation on graphite anode; altered SEI composition with increased Li_xPO_yF_z species
- experiment: SEM-EDX analysis of graphite anode after 100 cycles | Scanning Electron Microscopy with Energy Dispersive X-ray Spectroscopy | params: Anodes cycled in EC-based and EC-free electrolytes in Al2O3-NCM523||graphite cells at 4.5 V | result: EC-based electrolyte shows visible TM deposits (Co, Mn, Ni) and Li dendrites at identical spots; EC-free electrolyte shows no such deposits or dendrites
  - [non-referenced_knowledge] EC-free electrolyte (1.0 M LiPF6 in EMC) lacks ethylene carbonate, which is known to be highly reductive and stabilize SEI.
  - [experimental result] In the absence of EC, LiPF6 undergoes enhanced degradation at the graphite anode, producing Li_xPO_yF_z species (e.g., PO3F2-).
  - [experimental result] XPS analysis confirms significantly higher concentration of Li_xPO_yF_z species on both anode and cathode in EC-free electrolyte.
  - [experimental result] Precipitation experiments show that adding PO3F2- to EC-based electrolyte containing Ni2+ and Co2+ reduces TM ion concentration from ~750 ppm to ~1–5 ppm.
  - [image description] SEM-EDX images reveal TM deposits and Li dendrites co-localized on graphite anodes cycled in EC-based electrolyte, but absent in EC-free electrolyte.
  - [referenced knowledge] TM deposits on graphite serve as nucleation sites for Li dendrite growth, as established in prior literature.
  - [non-referenced_knowledge] Li_xPO_yF_z species scavenge dissolved TMs via chelation, preventing their transport and deposition on the anode.
  - [deductive reasoning] Thus, EC-free electrolyte suppresses TM cross-talk and dendrite formation by generating TM-scavenging Li_xPO_yF_z species.
### M2  Structure → Performance
- cause: Reduced transition metal (TM) deposits and suppressed Li dendrite formation on graphite anode; altered SEI composition with increased Li_xPO_yF_z species
- effect: Rollover-free high-voltage performance at 4.5 V with suppressed capacity fade
- experiment: Charge/discharge cycling of NCM523||graphite cells at 4.5 V | Constant current-constant voltage cycling | params: Cycling between 2.8–4.5 V at 1 C rate for >100 cycles in EC-based and EC-free electrolytes | result: EC-based electrolyte shows sudden capacity fade (rollover) at cycle ~45; EC-free electrolyte shows no rollover and stable capacity retention.
  - [experimental result] SEM-EDX and XPS show that EC-free electrolyte leads to minimal TM deposits and higher Li_xPO_yF_z concentration on the anode.
  - [non-referenced_knowledge] The absence of TM deposits eliminates nucleation sites for Li dendrite growth.
  - [experimental result] Electrochemical cycling reveals that EC-based electrolyte cells suffer rollover failure at cycle ~45, accompanied by random charge capacity spikes and voltage noise.
  - [referenced knowledge] Voltage noise in the 85th cycle is a known signature of Li dendrite penetration causing micro short-circuits.
  - [experimental result] In EC-free cells, no such spikes or noise occur, indicating absence of dendrites and short circuits.
  - [experimental result] Adding LiDFP (a source of Li_xPO_yF_z) to EC-based electrolyte eliminates rollover, confirming that Li_xPO_yF_z species are the key structural factor enabling performance.
  - [deductive reasoning] Therefore, the structural suppression of TMs and dendrites directly enables rollover-free performance.
