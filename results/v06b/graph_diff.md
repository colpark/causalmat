# v06b graph diffs

Every verdict here is model against model; no human checked any item.

v06b packets = captions + the paper's linked body text + panel section, no MatMech block or summaries.
v06b against v05 isolates the MatMech block and summaries (the only packet difference); v06b against v06 isolates the linked text.

Totals over eight papers: node sources {'inferred': 23, 'text': 206, 'figure': 92, 'prior_knowledge': 12}; causes modes {'joint': 18}; judge MatMech tally supports 23, contradicts 0, not covered 6.

| paper | panel checks | overturned | cue overrides | MatMech supports / contradicts / not covered |
|---|---|---|---|---|
| Acta_Materialia__10.1016_j.actamat.2014.06.008 | 16 | 0 | 2 | 1 / 0 / 2 |
| Advanced_Energy_Materials__aenm.201301564 | 19 | 0 | 0 | 5 / 0 / 1 |
| Advanced_Energy_Materials__aenm.201501833 | 19 | 0 | 0 | 3 / 0 / 1 |
| Advanced_Functional_Materials__10.1002_adfm.202005093 | 25 | 0 | 6 | 5 / 0 / 0 |
| Advanced_Materials__10.1002_adma.201300071 | 18 | 0 | 0 | 2 / 0 / 0 |
| Bioactive_Materials__j.bioactmat.2019.01.001 | 13 | 0 | 0 | 3 / 0 / 2 |
| Journal_of_Advanced_Ceramics__s40145-019-0334-4 | 14 | 0 | 0 | 2 / 0 / 0 |
| Rare_Metals__s12598-012-0515-6 | 8 | 0 | 0 | 2 / 0 / 0 |

Process note: judge 1 opened the ceramic judge_only MatMech file before its last edits (technique form, requires_unseen); it reports the edits were not informed by it.

# Part A: v06b against v05 (MatMech influence)

## Journal_of_Advanced_Ceramics__s40145-019-0334-4
- spine: 16 -> 13; matched 12, dropped 4, added 1, retyped 1 (changed 31% of v05 spine)
- MEC nodes: 2 -> 4
- evidence nodes: 11 -> 17 (dropped 1, added 7)
- audits: 4 -> 0 (dropped 4, added 0)
- MatMech pairs (judge, v06 graph): supports 2, contradicts 0, not covered 0
  - dropped q2 [HYP/hypothesis]: Reacting ZrSi2, B4C and carbon in situ under pressure, with extra ZrSi2 as a transient liquid, should grow int
  - dropped q5 [DES/route]: One-step in-situ reactive hot pressing at 1550 C for 30 min under 40 MPa in vacuum, instead of sintering pre-m
  - dropped q13 [PRP/value]: Fracture toughness climbs to 6.08 MPa m^1/2 at 20 vol% and stays close to that at 25 vol%
  - dropped q14 [PRP/behavior_class]: Fracture is a mixed mode: larger platelets break transgranularly, smaller ones along their boundaries
  - added c1 [DSC/conclusion]: Reactive hot pressing with ~20 vol% excess ZrSi2 gives interlocking ZrB2 platelets plus nano SiC and the best 
  - retyped q16 [DSC/conclusion] -> h2 [HYP/hypothesis]

## Acta_Materialia__10.1016_j.actamat.2014.06.008
- spine: 17 -> 15; matched 12, dropped 5, added 3, retyped 2 (changed 41% of v05 spine)
- MEC nodes: 1 -> 2
- evidence nodes: 16 -> 16 (dropped 5, added 5)
- audits: 3 -> 3 (dropped 2, added 2)
- MatMech pairs (judge, v06 graph): supports 1, contradicts 0, not covered 2
  - dropped a4 [DES/method]: 3-D CXD on one non-overlapped grain peak of a FIB-isolated 15x15 um island, 2x2 um focused beam, rocking aroun
  - dropped a10 [STR/microstructure/shape]: Grains are columnar: one grain spans the whole film thickness, boundaries running from the substrate to the su
  - dropped a13 [STR/microstructure/orientation]: Neighbourhood of grain g1: g2, g4, g5 share its in-plane orientation and lie along y; g3 and g6 are in-plane m
  - dropped a14 [STR/defect/extended]: Thermal loading stores defects (dislocations) in the grain, preferentially along x where the misoriented bound
  - dropped a17 [PRP/behavior_class]: The heterogeneity evolution is quasi-reversible on cooling, i.e. anelastic rather than a permanent plastic cha
  - added a10 [STR/microstructure/orientation]: Film has a strong {111} fibre texture: nearly all grains <111> out-of-plane, a few <100> grains
  - added a13 [STR/phase/lattice]: On heating, strain heterogeneity in the grain grows mainly along x and falls back quasi-reversibly on cooling;
  - added a14 [STR/microstructure/orientation]: Among g1's neighbours, g3 and g6 are strongly misoriented in-plane from g1, while g2, g4 and g5 are nearly ali
  - retyped a2 [HYP/hypothesis] -> a3 [DES/method]
  - retyped a16 [PRP/value] -> a11 [STR/phase/lattice]

## Advanced_Functional_Materials__10.1002_adfm.202005093
- spine: 19 -> 16; matched 13, dropped 6, added 3, retyped 1 (changed 37% of v05 spine)
- MEC nodes: 2 -> 3
- evidence nodes: 15 -> 25 (dropped 1, added 11)
- audits: 3 -> 4 (dropped 3, added 4)
- MatMech pairs (judge, v06 graph): supports 5, contradicts 0, not covered 0
  - dropped n1 [HYP/need]: Cancer nanomedicine needs one agent that heats, generates ROS and gives imaging contrast under NIR light
  - dropped n6 [DES/modification]: Coat the sheets with bovine serum albumin to give BNs-BSA for intravenous use
  - dropped n7 [DES/variable_sweep]: Sweep bismuthene concentration 25-200 ug/mL, 808 nm power 0.5-1.5 W/cm2, and six in-vivo treatment groups
  - dropped n10 [PRC/synthesis]: Surface functionalisation of the sheets with BSA
  - dropped n18 [PRF/service_capability]: BNs-BSA gives concentration-linear photoacoustic contrast and raises tumour CT contrast in vivo
  - dropped n26 [PRC/stimulus]: 660 nm and 808 nm laser irradiation of dispersions and of tumour-bearing mice
  - added a1 [HYP/gap]: 2D bismuthene has not been used in nanomedicine because engineering it with the needed structure and compositi
  - added a9 [STR/chemistry/composition]: Surface stays oxide-rich after reduction: Bi3+ (Bi2O3) : Bi0 ~ 12:5 from Bi 4f peak areas
  - added a10 [PRP/value]: Bismuthene is a semiconductor with an optical band gap of ~0.69 eV
  - retyped n12 [STR/microstructure/shape] -> a7 [STR/microstructure/feature_size]

## Advanced_Energy_Materials__aenm.201501833
- spine: 16 -> 14; matched 10, dropped 6, added 4, retyped 2 (changed 50% of v05 spine)
- MEC nodes: 1 -> 1
- evidence nodes: 12 -> 18 (dropped 1, added 7)
- audits: 3 -> 3 (dropped 3, added 3)
- MatMech pairs (judge, v06 graph): supports 3, contradicts 0, not covered 1
  - dropped e5 [DES/variable_sweep]: Pristine Ni-MOF against the derived phosphate, over 1-100 mV/s, 1-20 A/g and 10 000 cycles
  - dropped e6 [PRC/synthesis]: Treat the Ni-MOF hydrothermally with sodium phosphate so phosphate ions take the place of the BTC ligands
  - dropped e8 [STR/phase/identity]: The derived solid is largely amorphous with a weak crystalline texture matched to a nickel phosphate card
  - dropped e10 [STR/microstructure/porosity]: Surface porosity opens up and the specific surface area rises from 2.51 to 142.24 m2/g
  - dropped e11 [PRP/value]: Sheet resistance of the electrode film falls from 1049.42 to 714.13 ohm/sq after substitution
  - dropped e12 [PRP/behavior_class]: Charge storage is Faradaic, through a quasi-reversible Ni(II)/Ni(III) redox couple, not double-layer
  - added n4 [DES/route]: Hydrothermal treatment of Ni-MOF with sodium phosphate to substitute BTC by phosphate units
  - added n9 [PRP/value]: NixPyOz electrode film is more conductive than Ni-MOF film
  - added n10 [PRP/value]: NixPyOz electrode has lower charge-transfer resistance and faster ion diffusion than Ni-MOF
  - added n14 [PRF/service_capability]: NixPyOz keeps ~64% of its capacitance from 1 to 20 A/g versus ~21% for Ni-MOF
  - retyped e13 [PRP/value] -> n13 [PRF/figure_of_merit]
  - retyped e4 [DES/route] -> n5 [PRC/synthesis]

## Advanced_Energy_Materials__aenm.201301564
- spine: 17 -> 13; matched 11, dropped 6, added 2, retyped 2 (changed 47% of v05 spine)
- MEC nodes: 2 -> 1
- evidence nodes: 17 -> 19 (dropped 1, added 3)
- audits: 2 -> 0 (dropped 2, added 0)
- MatMech pairs (judge, v06 graph): supports 5, contradicts 0, not covered 1
  - dropped b3 [DES/base_system]: Hierarchical Cu2S microspheres built from nanoflakes as the counter-electrode catalyst
  - dropped b7 [PRC/treatment]: Calcination of the product at 350 C in Ar
  - dropped b11 [STR/chemistry/bonding]: GO is reduced during the solvothermal step: the oxygen-containing groups are removed and a graphitic RGO netwo
  - dropped b12 [PRP/value]: The composite electrode is a far better polysulfide-reduction catalyst than Pt: about 100x the reduction peak 
  - dropped b13 [PRP/value]: Charge-transfer resistance at the electrode/electrolyte interface falls to about 3.4 ohm for RGO-Cu2S-2, rough
  - dropped b16 [MEC/tradeoff]: Past 10 mL GO the extra RGO covers the Cu2S surface and blocks electrolyte access, so efficiency falls back to
  - added m6 [PRC/synthesis]: One-pot solvothermal reaction at 150 C for 12 h grows Cu2S on GO while reducing GO
  - added m14 [PRP/value]: Polysulfide-reduction activity ranks RGO-Cu2S-2 above Cu2S and far above Pt
  - retyped b15 [PRF/service_capability] -> m15 [PRF/figure_of_merit]
  - retyped b6 [PRC/synthesis] -> m3 [DES/base_system]

## Rare_Metals__s12598-012-0515-6
- spine: 16 -> 13; matched 10, dropped 6, added 3, retyped 2 (changed 50% of v05 spine)
- MEC nodes: 2 -> 3
- evidence nodes: 8 -> 8 (dropped 2, added 2)
- audits: 3 -> 0 (dropped 3, added 0)
- MatMech pairs (judge, v06 graph): supports 2, contradicts 0, not covered 0
  - dropped r1 [HYP/need]: Cast Al-Cu-Mn is held back by a coarse continuous grain-boundary segregation network that caps both strength a
  - dropped r2 [HYP/gap]: How individual rare earths differ from one another in their effect on Al-Cu-Mn microstructure and tensile beha
  - dropped r5 [DES/modification]: Add La or Sm as the rare-earth microalloying element
  - dropped r8 [PRC/treatment]: Solution treat at 525 C/6 h then 545 C/6 h, water quench, age at 170 C for 4 h
  - dropped r9 [STR/microstructure/distribution]: The rare-earth additions break the continuous net-like boundary segregation into separate islands or a much th
  - dropped r13 [PRP/value]: Elongation rises from 7.2% to 9.2% with Sm and 10.6% with La
  - added d1 [DES/base_system]: Base alloy: Al-Cu-Mn, strengthened by theta' precipitates on ageing
  - added s1 [STR/microstructure/distribution]: RE turns the continuous coarse netlike interdendritic phase into discontinuous, finer particles; La more than 
  - added s6 [STR/microstructure/distribution]: RE addition raises the number density of theta' precipitates; La more than Sm
  - retyped r6 [DES/variable_sweep] -> d2 [DES/modification]
  - retyped r4 [DES/base_system] -> p2 [PRC/treatment]

## Bioactive_Materials__j.bioactmat.2019.01.001
- spine: 17 -> 15; matched 8, dropped 9, added 7, retyped 2 (changed 65% of v05 spine)
- MEC nodes: 2 -> 3
- evidence nodes: 12 -> 13 (dropped 2, added 3)
- audits: 4 -> 6 (dropped 1, added 3)
- MatMech pairs (judge, v06 graph): supports 3, contradicts 0, not covered 2
  - dropped b1 [HYP/need]: A paediatric tracheobronchial stent must hold the airway for 3-12 months and then vanish; permanent stents pro
  - dropped b3 [HYP/hypothesis]: Gamble's solution, lower in chloride and richer in bicarbonate and mucin than SBF, should degrade these metals
  - dropped b7 [PRC/forming]: Disks 10 mm x 2 mm cut and ground to 2000 grit SiC
  - dropped b9 [STR/chemistry/composition]: Corrosion layers are carbonate plus phosphate; the GS layers on Mg and Zn carry far less P and Ca than the SBF
  - dropped b11 [PRP/value]: 28-d corrosion rate in GS is well below SBF: 0.78 vs 2.01 (Mg), 0.03 vs 0.10 (Zn), 0.09 vs 0.13 mm/y (Fe)
  - dropped b12 [PRP/value]: HP-Mg is ~240 mV nobler and carries ~12x lower corrosion current in GS than in SBF; Zn and Fe differ little be
  - dropped b13 [PRP/value]: A549 viability with HP-Mg and HP-Zn reaches the negative control by day 5, while P-Fe under indirect and extra
  - dropped b15 [MEC/pathway]: GS mucin suppresses phosphate deposition but its low chloride and bicarbonate buffering limit pitting and hold
  - dropped b16 [MEC/pathway]: Cytotoxicity tracks the released ion dose: 1.52 mM Fe in the extract is toxic to A549 while 6.03 mM Mg and 0.2
  - added s3 [DES/variable_sweep]: Immersion medium GS (with 0.6 g/L mucin, HCO3-/CO2 buffer) vs SBF (Tris/HCl buffer), for 7-28 d
  - added s6 [PRC/stimulus]: Culture of A549 cells with the metals or their extracts for up to 5 d in DC, IC and EC set-ups
  - added s9 [MEC/pathway]: In GS, less chloride and adsorbed mucin and bicarbonate keep the protective product film intact, which slows c
  - added s10 [PRP/value]: HP-Mg degrades about an order of magnitude faster than HP-Zn and P-Fe in both media
  - added s11 [PRP/value]: Degradation is slower in GS than in SBF, most strongly for HP-Mg (28 d: 0.78 vs 2.0 mm/y)
  - added s12 [PRP/value]: HP-Mg and HP-Zn support A549 attachment and proliferation, while P-Fe lowers cell density and viability
  - added s13 [MEC/pathway]: Fe ions released into the medium (~1.5 mM) are cytotoxic, while ~6 mM Mg2+ and ~0.2 mM Zn2+ are tolerated
  - retyped b2 [HYP/gap] -> s1 [HYP/need]
  - retyped b5 [DES/variable_sweep] -> s8 [STR/chemistry/composition]

## Advanced_Materials__10.1002_adma.201300071
- spine: 20 -> 14; matched 12, dropped 8, added 2, retyped 2 (changed 50% of v05 spine)
- MEC nodes: 1 -> 2
- evidence nodes: 15 -> 18 (dropped 1, added 4)
- audits: 5 -> 3 (dropped 5, added 3)
- MatMech pairs (judge, v06 graph): supports 2, contradicts 0, not covered 0
  - dropped n6 [PRC/synthesis]: Hydrothermal synthesis of SnO2 nanocrystals
  - dropped n8 [PRC/synthesis]: Hydrazine monohydrate vapour at 120 C for 2 h reduces the GO and dopes it with nitrogen
  - dropped n9 [DES/variable_sweep]: Current density stepped 0.5, 1, 2, 5, 10, 20 A/g and back, plus 500 cycles at fixed rate
  - dropped n10 [PRC/stimulus]: Galvanostatic lithiation/delithiation of the electrode for 500 cycles
  - dropped n11 [STR/microstructure/feature_size]: SnO2 nanocrystals are 4-5 nm and the vapour reduction does not coarsen them
  - dropped n12 [STR/microstructure/distribution]: Nanocrystals are uniformly confined inside the graphene sheets, with only a few exposed at the outer surface
  - dropped n13 [STR/phase/identity]: The nanocrystals are polycrystalline tetragonal rutile SnO2 (JCPDS 41-1445)
  - dropped n19 [STR/microstructure/distribution]: After 500 cycles Sn is still spread through the carbon with no Sn-rich clusters
  - added b6 [PRC/synthesis]: Hydrazine-vapour reduction of the SnO2 NC / graphene oxide assembly gives the SnO2NC@N-RGO hybrid
  - added b8 [STR/microstructure/distribution]: Uniform SnO2 nanocrystals are homogeneously distributed throughout the graphene sheets
  - retyped n17 [PRP/value] -> b13 [PRF/service_capability]
  - retyped n7 [PRC/forming] -> b9 [STR/microstructure/porosity]


# Part B: v06b against v06 (linked text contribution)

## Journal_of_Advanced_Ceramics__s40145-019-0334-4
- spine: 13 -> 13; matched 10, dropped 3, added 3, retyped 2 (changed 38% of v05 spine)
- MEC nodes: 2 -> 4
- evidence nodes: 19 -> 17 (dropped 5, added 3)
- audits: 2 -> 0 (dropped 2, added 0)
- MatMech pairs (judge, v06 graph): supports 2, contradicts 0, not covered 0
  - dropped j5 [PRC/synthesis]: Reactive hot pressing of the powder mixtures into dense ZrB2-SiC composites
  - dropped j9 [STR/microstructure/distribution]: SiC is nano-sized and clustered in SiC-rich regions between the ZrB2 platelets
  - dropped j10 [PRP/value]: Fracture toughness rises from ~4.3 (RZSZ-0) to ~6.1 MPa m^1/2 at RZSZ-20 and stays ~6.0 at RZSZ-25
  - added s1 [STR/phase/identity]: Reaction (1) completes: composite is ZrB2 + SiC with trace WSi2 and ZrO2, no starting-powder peaks
  - added m1 [MEC/pathway]: Exothermic Reaction (1) locally melts/deforms ZrSi2; the liquid aids densification and transports Zr, B to fas
  - added s5 [STR/microstructure/feature_size]: Excess ZrSi2 refines in-situ SiC from submicron (RZSZ-0) to nano-sized grains
  - retyped j3 [DES/route] -> d1 [DES/base_system]
  - retyped j6 [STR/phase/identity] -> p1 [PRC/synthesis]

## Acta_Materialia__10.1016_j.actamat.2014.06.008
- spine: 12 -> 15; matched 10, dropped 2, added 5, retyped 0 (changed 17% of v05 spine)
- MEC nodes: 1 -> 2
- evidence nodes: 16 -> 16 (dropped 1, added 1)
- audits: 2 -> 3 (dropped 2, added 3)
- MatMech pairs (judge, v06 graph): supports 1, contradicts 0, not covered 2
  - dropped a8 [STR/phase/lattice]: Mean out-of-plane strain of the grain rises on heating and falls on cooling along a hysteretic, open loop
  - dropped a10 [STR/defect/extended]: Defects enter the grain along x during heating while the displacement field stays uniform through the film thi
  - added a7 [PRC/deposition]: Physical vapour deposition of a 475 nm Au film on fused silica
  - added a8 [PRC/treatment]: Flame anneal 30 s at 800-900 C to grow the grains laterally
  - added a10 [STR/microstructure/orientation]: Film has a strong {111} fibre texture: nearly all grains <111> out-of-plane, a few <100> grains
  - added a14 [STR/microstructure/orientation]: Among g1's neighbours, g3 and g6 are strongly misoriented in-plane from g1, while g2, g4 and g5 are nearly ali
  - added a17 [PRF/service_capability]: In-situ CXD tracks the 3-D strain field of one sub-micron grain through a full thermal cycle

## Advanced_Functional_Materials__10.1002_adfm.202005093
- spine: 14 -> 16; matched 12, dropped 2, added 4, retyped 1 (changed 21% of v05 spine)
- MEC nodes: 2 -> 3
- evidence nodes: 19 -> 25 (dropped 1, added 7)
- audits: 3 -> 4 (dropped 3, added 4)
- MatMech pairs (judge, v06 graph): supports 5, contradicts 0, not covered 0
  - dropped h1 [HYP/need]: Cancer phototherapy needs one agent that combines photothermal, photodynamic and imaging functions
  - dropped s2 [STR/microstructure/shape]: Bismuthene forms thin 2D plates about 250-350 nm across and ~14 nm thick
  - added a1 [HYP/gap]: 2D bismuthene has not been used in nanomedicine because engineering it with the needed structure and compositi
  - added a4 [DES/route]: Water-mediated freeze-thaw intercalation/exfoliation with bath sonication, then NaBH4 reduction; organic-solve
  - added a7 [STR/microstructure/feature_size]: Free-standing lamellar nanosheets ~200 nm across and ~14 nm thick
  - added a9 [STR/chemistry/composition]: Surface stays oxide-rich after reduction: Bi3+ (Bi2O3) : Bi0 ~ 12:5 from Bi 4f peak areas
  - retyped c1 [PRC/synthesis] -> a5 [PRC/treatment]

## Advanced_Energy_Materials__aenm.201501833
- spine: 14 -> 14; matched 12, dropped 2, added 2, retyped 4 (changed 43% of v05 spine)
- MEC nodes: 1 -> 1
- evidence nodes: 15 -> 18 (dropped 2, added 5)
- audits: 2 -> 3 (dropped 1, added 2)
- MatMech pairs (judge, v06 graph): supports 3, contradicts 0, not covered 1
  - dropped a5 [STR/chemistry/bonding]: Carboxylate linkers are removed and P-O phosphate groups now coordinate Ni in the product
  - dropped a6 [STR/phase/identity]: The product is a poorly crystalline nickel phosphate indexed to JCPDS 04-010-2575
  - added n5 [PRC/synthesis]: Hydrothermal ligand substitution converts Ni-MOF into MOF-derived NixPyOz
  - added n13 [PRF/figure_of_merit]: NixPyOz reaches ~1620 F/g at 1 A/g, about four times Ni-MOF (~400 F/g)
  - retyped a11 [PRF/figure_of_merit] -> n14 [PRF/service_capability]
  - retyped a4 [PRC/synthesis] -> n4 [DES/route]
  - retyped a3 [DES/route] -> n6 [STR/chemistry/bonding]
  - retyped a10 [PRP/value] -> n1 [HYP/need]

## Advanced_Energy_Materials__aenm.201301564
- spine: 13 -> 13; matched 12, dropped 1, added 1, retyped 1 (changed 15% of v05 spine)
- MEC nodes: 1 -> 1
- evidence nodes: 18 -> 19 (dropped 1, added 2)
- audits: 1 -> 0 (dropped 1, added 0)
- MatMech pairs (judge, v06 graph): supports 5, contradicts 0, not covered 1
  - dropped b9 [STR/chemistry/bonding]: GO is reduced during the solvothermal step: oxygen groups largely removed and sp2 carbon restored
  - added m1 [HYP/need]: Pt counter electrodes perform poorly in polysulfide-electrolyte QDSSCs
  - retyped b13 [PRF/service_capability] -> m15 [PRF/figure_of_merit]

## Rare_Metals__s12598-012-0515-6
- spine: 13 -> 13; matched 8, dropped 5, added 5, retyped 1 (changed 46% of v05 spine)
- MEC nodes: 3 -> 3
- evidence nodes: 10 -> 8 (dropped 2, added 0)
- audits: 2 -> 0 (dropped 2, added 0)
- MatMech pairs (judge, v06 graph): supports 2, contradicts 0, not covered 0
  - dropped r2 [DES/base_system]: Al-Cu-Mn casting alloy as the base
  - dropped r4 [DES/variable_sweep]: Three alloys compared: Al-Cu-Mn, Al-Cu-Mn-Sm and Al-Cu-Mn-La
  - dropped r8 [STR/microstructure/distribution]: RE addition breaks the continuous interdendritic Al2Cu eutectic network into isolated (Sm) or fine fragmented 
  - dropped r9 [STR/phase/fraction]: La removes the Al-Al2Cu eutectic melting event at ~548 C; the base and Sm alloys retain it
  - dropped r11 [MEC/pathway]: Finer, denser plate precipitates obstruct dislocation glide more effectively (precipitation strengthening)
  - added s1 [STR/microstructure/distribution]: RE turns the continuous coarse netlike interdendritic phase into discontinuous, finer particles; La more than 
  - added m1 [MEC/pathway]: Oversized La atoms distort the Al lattice and bind vacancies, providing nucleation sites for theta'
  - added s5 [STR/microstructure/feature_size]: RE addition refines the theta' platelets on {001}Al; La refines more than Sm
  - added s6 [STR/microstructure/distribution]: RE addition raises the number density of theta' precipitates; La more than Sm
  - added m3 [MEC/pathway]: Denser, finer theta' gives stronger precipitation hardening
  - retyped r10 [STR/microstructure/feature_size] -> d1 [DES/base_system]

## Bioactive_Materials__j.bioactmat.2019.01.001
- spine: 16 -> 15; matched 12, dropped 4, added 3, retyped 0 (changed 25% of v05 spine)
- MEC nodes: 2 -> 3
- evidence nodes: 15 -> 13 (dropped 3, added 1)
- audits: 4 -> 6 (dropped 4, added 6)
- MatMech pairs (judge, v06 graph): supports 3, contradicts 0, not covered 2
  - dropped b2 [HYP/gap]: Degradation and cytocompatibility of Mg, Zn and Fe have not been compared under airway-relevant in-vitro condi
  - dropped b9 [PRP/value]: Electrochemical corrosion tendency ranks Mg > Zn > Fe; SBF lowers Ecorr and raises icorr, most for Mg
  - dropped b10 [PRP/value]: Immersion degradation rate ranks Mg >> Zn > Fe and is far higher in SBF than in GS
  - dropped b12 [PRP/value]: HP-Mg and HP-Zn support A549 growth in IC and EC; P-Fe suppresses viability in IC and, by day 5, EC
  - added s10 [PRP/value]: HP-Mg degrades about an order of magnitude faster than HP-Zn and P-Fe in both media
  - added s11 [PRP/value]: Degradation is slower in GS than in SBF, most strongly for HP-Mg (28 d: 0.78 vs 2.0 mm/y)
  - added s12 [PRP/value]: HP-Mg and HP-Zn support A549 attachment and proliferation, while P-Fe lowers cell density and viability

## Advanced_Materials__10.1002_adma.201300071
- spine: 14 -> 14; matched 11, dropped 3, added 3, retyped 3 (changed 43% of v05 spine)
- MEC nodes: 3 -> 2
- evidence nodes: 16 -> 18 (dropped 1, added 3)
- audits: 2 -> 3 (dropped 2, added 3)
- MatMech pairs (judge, v06 graph): supports 2, contradicts 0, not covered 0
  - dropped h2 [HYP/hypothesis]: Binding SnO2 nanocrystals inside N-doped graphene sheets should give a high-capacity, long-life, high-rate ano
  - dropped s1 [STR/phase/identity]: The nanocrystals are rutile SnO2, unchanged by the N-RGO
  - dropped s2 [STR/microstructure/feature_size]: SnO2 crystallites are about 4-6 nm
  - added b3 [DES/base_system]: Ultrasmall SnO2 nanocrystals (4-5 nm) as the high-capacity active phase
  - added b5 [DES/route]: In-situ hydrazine monohydrate vapour reduction to reduce and N-dope the graphene while binding the nanocrystal
  - added b7 [STR/interface]: SnO2 nanocrystals are chemically bonded to N-RGO through interfacial Sn-N-C and Sn-O-C bonds
  - retyped d1 [DES/architecture] -> b4 [DES/modification]
  - retyped m1 [MEC/pathway] -> b2 [HYP/hypothesis]
  - retyped s6 [STR/interface] -> b9 [STR/microstructure/porosity]

