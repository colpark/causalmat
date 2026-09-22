# MatMech content for Nano_Letters/10.1021_acs.nanolett.5b03976 (judge only; not shown to staff)
- material: Germanium (Ge) nanowire  elements: ['Ge']  category: ['Crystalline Material', 'Nanomaterial']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Fabrication using electron beam lithography, HBr/Cl2 dry etch, KOH wet etch, and atomic layer deposition (ALD)
- **Structure**: Highly strained Ge nanowire with a pseudo-heterostructure and high-Q nanophotonic cavity
- **Properties**: Direct bandgap light emission–optical property, tensile strain–mechanical property
- **Performance**: Enhanced photoluminescence with quality factors up to 2,000, tunable emission wavelength over 400 nm
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Fabrication using electron beam lithography, HBr/Cl2 dry etch, KOH wet etch, and atomic layer deposition (ALD)
- effect: Highly strained Ge nanowire with a pseudo-heterostructure and high-Q nanophotonic cavity
- experiment: Nanowire strain measurement | Raman spectroscopy | params: Strain levels of 0%, 1.95%, and 2.37% measured | result: Uniform strain distribution along the central segment of the nanowire confirmed experimentally
  - [experimental result] The Ge layer is patterned using a single electron beam lithography step followed by HBr/Cl2 dry etch to define the nanowire structure.
  - [non-referenced_knowledge] After patterning, the Al2O3 sacrificial layer is selectively removed using KOH wet etch, releasing the slightly strained Ge layer from the substrate and allowing large pads to contract, amplifying the strain in the nanowire.
  - [image description] Figure 3c presents a strain map for a fabricated device, showing a uniform strain of ~2.4% along the narrow central segment of the nanowire, consistent with FEM simulations.
  - [non-referenced_knowledge] Tensile strain reduces the bandgap of Ge, creating a spatial variation in the strain profile that forms a pseudo-heterostructure which confines carriers to the nanowire region.
  - [deductive reasoning] Therefore, the fabrication process leads to a highly strained Ge nanowire with a pseudo-heterostructure capable of supporting high-Q optical cavities.
### M2  Structure → Property
- cause: Highly strained Ge nanowire with a pseudo-heterostructure and high-Q nanophotonic cavity
- effect: Direct bandgap light emission–optical property, tensile strain–mechanical property
- experiment: Photoluminescence measurements | Spectroscopy | params: Measured under continuous-wave (CW) and pulsed laser excitation at varying pump powers | result: Emission peak redshifts from ~1560 nm to >1980 nm with increased strain; Q-factors up to 2020 observed
  - [experimental result] The structure supports optical modes with radiative quality factors of over 10⁴ while retaining very high (>2%) mechanical strain along the nanowire.
  - [image description] Figure 4a shows photoluminescence spectra from unstrained, 1.95%, and 2.37% strained nanowires, demonstrating a redshift in emission peak with increasing strain, indicating bandgap narrowing.
  - [non-referenced_knowledge] Empirical pseudopotential method (EPM) modeling confirms that strain-induced valence band splitting increases available optical gain.
  - [referenced knowledge] Net optical gain improves significantly with increased strain from 1.95% to 2.37%, confirming that structural strain directly influences optical properties.
  - [deductive reasoning] Thus, the strained nanowire structure enables direct bandgap behavior and enhances optical emission efficiency.
### M3  Property → Performance
- cause: Direct bandgap light emission–optical property, tensile strain–mechanical property
- effect: Enhanced photoluminescence with quality factors up to 2,000, tunable emission wavelength over 400 nm
- experiment: Pump-dependent photoluminescence analysis | Spectroscopy | params: Varying incident pump power from 2.5 mW to 20 mW | result: Net optical gain decreases with increasing pump power due to free-carrier absorption but improves significantly with increased strain
  - [experimental result] Photoluminescence measurements show emission tunability over more than 400 nm with increasing strain, achieved with a single lithography step.
  - [image description] A Q-factor of 2,020 was observed in Lorentzian fits to resonance peaks, limited by sidewall roughness and material absorption.
  - [non-referenced_knowledge] Net optical gain calculations show a significant reduction in loss with increased strain, improving photoluminescence efficiency.
  - [referenced knowledge] Modeling predicts that further strain increase could enable room temperature lasing in Ge.
  - [inductive reasoning] Therefore, the combination of direct bandgap emission, high strain, and high-Q cavity enables enhanced photoluminescence performance with wide tunability.
