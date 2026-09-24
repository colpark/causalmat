# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c04204 (judge only; not shown to staff)
- material: WS2/WSe2  elements: ['W', 'S', 'Se']  category: ['Crystalline Material', 'Nanomaterial', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property
## Tetrahedron elements
- **Processing**: Modulated metal−organic chemical vapor deposition (MOCVD)
- **Structure**: Coherent interface with nearly uniform strain on each side of the heterojunction
- **Properties**: bandgap reduction–electronic property
- **Performance**: Type-II band alignment and ultranarrow electronic transition region
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Modulated metal−organic chemical vapor deposition (MOCVD)
- effect: Coherent interface with nearly uniform strain on each side of the heterojunction
- experiment: STM imaging and FFT analysis | Scanning Tunneling Microscopy | params: Growth on SiO2/Si wafers, transfer to HOPG for STM characterization | result: Atomic-resolution images show no misfit dislocations at the interface; moiré patterns indicate uniform strain distribution
  - [non-referenced_knowledge] WS2 and WSe2 have different lattice constants due to chalcogen atom size difference (S vs Se).
  - [experimental result] MOCVD growth was used to fabricate WS2/WSe2 superlattices with large coherent interfaces (>50 nm).
  - [image description] No dislocations were observed at the interface in inverse FFT analysis of STM images.
  - [image description] Uniform moiré patterns indicate consistent strain across the interface region.
  - [deductive reasoning] Thus, lattice mismatch is accommodated by uniform strain rather than structural defects.
### M2  Structure → Property
- cause: Nearly uniform tensile strain in WS2 and compressive strain in WSe2
- effect: Bandgap reduction in WS2 (~240 meV), no significant change in WSe2
- experiment: Scanning Tunneling Spectroscopy (STS) | dI/dV spectroscopy | params: Constant-height and constant-current measurements far from and near the heterojunction interface | result: STS shows 240 meV bandgap reduction in WS2 compared to pristine samples; WSe2 bandgap remains unchanged
  - [referenced knowledge] First-principles calculations predict ~170 meV bandgap reduction per 1% isotropic strain in WS2.
  - [experimental result] STS measurements show 240 meV reduction in WS2 bandgap in heterostructure compared to pristine samples.
  - [non-referenced_knowledge] Fractional area change in WS2 estimated as 2.8% based on measured bandgap reduction.
  - [experimental result] WSe2 experiences compressive strain but shows no significant bandgap change, consistent with theoretical predictions.
  - [deductive reasoning] Therefore, uniform tensile strain in WS2 reduces its bandgap while compressive strain in WSe2 has negligible effect.
### M3  Property → Performance
- cause: Bandgap reduction in WS2 and rigid band shift due to charge transfer
- effect: Type-II band alignment and ultranarrow electronic transition region (~3 nm width)
- experiment: Spatially-resolved dI/dV mapping across interface | Scanning Tunneling Spectroscopy | params: Constant-current dI/dV sweeps across the heterojunction interface | result: Electronic states merge rapidly over ~3 nm; K-point states collapse in energy on WSe2 side; Q-point states merge with K-point in WS2 side
  - [experimental result] Far from the interface, band shifts are rigid due to charge transfer effects.
  - [experimental result] Near the interface, K-point valence band states in WSe2 collapse rapidly in energy.
  - [experimental result] K- and Q-point conduction band states in WS2 merge over similar length scale (~3 nm).
  - [non-referenced_knowledge] This length scale cannot be explained by strain effects which are mostly uniform.
  - [referenced knowledge] Wave function hybridization across the interface provides the natural explanation for this electronic length scale.
  - [deductive reasoning] Therefore, strain-induced bandgap changes combined with wave function mixing produce type-II alignment and ultranarrow transition region.
