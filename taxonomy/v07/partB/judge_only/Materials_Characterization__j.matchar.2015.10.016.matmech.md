# MatMech content for Materials_Characterization/j.matchar.2015.10.016 (judge only; not shown to staff)
- material: ZrB₂-SiC composites doped with AlN  elements: ['Zr', 'B', 'Si', 'C', 'Al', 'N']  category: ['Ceramic', 'Composite Material', 'Nanomaterial']
- MST chain: Processing → Structure → Properties
## Tetrahedron elements
- **Processing**: Hot pressing at 1900°C under 10 MPa for 2 h; Pressureless sintering at 1900°C for 2 h under vacuum (5×10⁻² Pa)
- **Structure**: Formation of nano-scale metakaolinite spinel layers, amorphous glassy phases, BN, Al₂OC, and nano-graphite at grain boundaries; grain coarsening; porosity variation with AlN content
- **Properties**: Vickers hardness–mechanical property
- **Performance**: None
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Hot pressing at 1900°C under 10 MPa for 2 h with 1 wt.% AlN addition
- effect: Formation of nano-scale metakaolinite spinel layers and liquid phase enabling fully dense microstructure with minimal porosity
- experiment: Relative density measurement via Archimedes principle | Density measurement | params: 1 wt.% AlN, hot pressing at 1900°C, 10 MPa, 2 h | result: Fully dense composite achieved (relative density ~100%)
  - [experimental result] Hot pressing at 1900°C under 10 MPa with 1 wt.% AlN results in fully dense ZrB₂–SiC composite.
  - [image description] SEM and TEM show thin amorphous layers at grain boundaries in HP1 and HP5 samples.
  - [referenced knowledge] AlN reacts with B₂O₃ impurities to form BN and Al₂O₃ (Eq. 1).
  - [non-referenced_knowledge] Al₂O₃ reacts with SiO₂ from SiC to form metakaolinite spinel (Eq. 2), which melts at low temperature and forms liquid phase.
  - [non-referenced_knowledge] Applied pressure expels gaseous products and compacts particles, allowing liquid phase to fill pores.
  - [deductive reasoning] Thus, liquid phase sintering via metakaolinite spinel formation enables full densification at low AlN content under hot pressing.
### M2  Processing → Structure
- cause: Pressureless sintering at 1900°C for 2 h under vacuum with increasing AlN content (1–5 wt.%)
- effect: Increased porosity due to entrapment of gaseous products (CO, B₂O₃ vapor) and formation of Al₂OC phase
- experiment: Relative density measurement via Archimedes principle | Density measurement | params: 1–5 wt.% AlN, pressureless sintering at 1900°C, 2 h, vacuum 5×10⁻² Pa | result: Relative density decreases with AlN addition; PS5 has lower density than PS0
  - [experimental result] Pressureless sintered samples with AlN show decreasing relative density with increasing AlN content.
  - [experimental result] XRD shows presence of Al₂OC phase in PS5 sample (Fig. 7b).
  - [non-referenced_knowledge] Al₂O₃ (from AlN + B₂O₃ reaction) reacts with carbon to form Al₂OC and CO gas (Eq. 5).
  - [non-referenced_knowledge] Gaseous phases (CO, B₂O₃ vapor) form during sintering but cannot escape without applied pressure.
  - [deductive reasoning] Trapped gases create and enlarge porosities, outweighing benefits of enhanced neck formation.
  - [inductive reasoning] Thus, AlN promotes sintering but increases porosity in pressureless sintering due to gas entrapment.
### M3  Processing → Structure
- cause: Hot pressing at 1900°C under 10 MPa with 5 wt.% AlN addition
- effect: Formation of nano-graphite phase at grain boundaries and BN crystalline phase
- experiment: XRD and TEM analysis of microstructure | XRD, TEM | params: HP5 sample, 5 wt.% AlN, 1900°C, 10 MPa | result: XRD shows BN peak; TEM shows nano-multi-layer graphite at grain boundaries.
  - [experimental result] XRD of HP5 sample shows BN peak, indicating formation of boron nitride.
  - [referenced knowledge] AlN reacts with B₂O₃ to form BN and Al₂O₃ (Eq. 1).
  - [image description] EDS and TEM confirm presence of carbon-rich interfacial layers.
  - [non-referenced_knowledge] Graphitization of residual carbon occurs under high temperature and pressure [40].
  - [deductive reasoning] Thus, nano-graphite forms parallel to grain boundaries due to graphitization of pyrolyzed resin carbon.
### M4  Structure → Property
- cause: Formation of fully dense microstructure with glassy phase and BN in hot pressed 1 wt.% AlN sample
- effect: Highest Vickers hardness observed in HP1 sample
- experiment: Vickers hardness test | Vickers hardness tester | params: 5 kg load, 15 s dwell, polished surfaces | result: HP1 sample shows maximum hardness; HP5 hardness slightly lower.
  - [experimental result] HP1 sample has the highest relative density among all samples.
  - [experimental result] HP1 shows the highest Vickers hardness value (Fig. 2b).
  - [non-referenced_knowledge] Density is a primary factor controlling hardness in ceramics.
  - [image description] HP1 has a balanced microstructure: sufficient glassy phase for densification but not excessive to weaken grain boundaries.
  - [deductive reasoning] Thus, optimal density and microstructure in HP1 yield maximum hardness.
### M5  Structure → Property
- cause: Formation of high porosity and Al₂OC phase in pressureless sintered 5 wt.% AlN sample
- effect: Lowest Vickers hardness observed in PS5 sample
- experiment: Vickers hardness test | Vickers hardness tester | params: 5 kg load, 15 s dwell, polished surfaces | result: PS5 sample has the lowest hardness among all compositions.
  - [experimental result] PS5 sample has the lowest relative density among all samples.
  - [experimental result] PS5 exhibits the lowest Vickers hardness value (Fig. 2b).
  - [non-referenced_knowledge] Porosity reduces effective load-bearing area and promotes crack initiation.
  - [experimental result] XRD confirms presence of Al₂OC, a brittle phase that weakens grain boundaries.
  - [deductive reasoning] Thus, combined effect of porosity and brittle interfacial phases leads to minimal hardness in PS5.
### M6  Processing → Property
- cause: Comparison of hot pressing vs. pressureless sintering with 1 wt.% AlN
- effect: HP1 exhibits significantly higher hardness than PS1 due to density difference
- experiment: Vickers hardness test | Vickers hardness tester | params: HP1 vs. PS1, 1 wt.% AlN, 1900°C, 2 h | result: HP1 hardness is substantially higher than PS1.
  - [experimental result] HP1 sample is fully dense (RD ~100%), PS1 sample has lower RD (~92%).
  - [experimental result] HP1 has significantly higher Vickers hardness than PS1 (Fig. 2b).
  - [non-referenced_knowledge] Hardness in ceramics is directly proportional to density.
  - [deductive reasoning] Thus, the difference in hardness between HP1 and PS1 is primarily due to difference in density caused by processing method.
