# MatMech content for Nano_Letters/10.1021_acs.nanolett.0c04023 (judge only; not shown to staff)
- material: CuInP2S6  elements: ['Cu', 'In', 'P', 'S']  category: ['Crystalline Material', 'Composite Material', 'Ceramic']
- MST chain: Processing → Structure → Property
## Tetrahedron elements
- **Processing**: Electric field application for Cu ion migration
- **Structure**: Phase-separated CuInP2S6 and In4/3P2S6 phases
- **Properties**: Ionic conductivity–electrical property
- **Performance**: Anisotropic Cu ion migration under electric fields
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Electric field application for Cu ion migration
- effect: Phase-separated CuInP2S6 and In4/3P2S6 phases
- experiment: Conductive atomic force microscopy (c-AFM) | Electrical conductivity measurement | params: Tip bias of -3.0 V applied on Cu-deficient CIPS flake | result: CIPS phase exhibits high conductivity while the IPS phase is insulating; conductivity increases with slower scanning speeds
  - [experimental result] Cu-deficient CIPS shows local chemical phase separation into CuInP2S6 (CIPS) and In4/3P2S6 (IPS) phases.
  - [image description] PFM images confirm ferroelectricity in the CIPS phase and negligible piezoresponse in the IPS phase.
  - [referenced knowledge] Cu-deficient CIPS undergoes chemical phase separation into Cu-free paraelectric In4/3P2S6 and Cu-rich ferroelectric CuInP2S6 phases.
  - [non-referenced_knowledge] Electric fields can drive ion migration and redistribution in layered materials.
  - [deductive reasoning] Thus, electric field-induced Cu ion migration leads to phase separation between Cu-rich CIPS and Cu-depleted IPS phases.
### M2  Structure → Property
- cause: Phase-separated CuInP2S6 and In4/3P2S6 phases
- effect: Ionic conductivity–electrical property
- experiment: Current-time measurements under bias cycles | Electrical transport | params: Bias-on (60 s, -8 V) and bias-off (varied durations: 1 s, 30 s, 60 s) | result: Time-dependent current relaxation indicates ionic dynamics with two-stage behavior linked to intralayer and interlayer Cu ion migration.
  - [experimental result] I-V curves and time-dependent current measurements reveal ionic conductivity activation dependent on Cu ion migration.
  - [image description] EDS mapping confirms Cu ion accumulation at biased areas, directly linking conduction to Cu ion movement.
  - [referenced knowledge] Cu ion motion has higher activation energy in out-of-plane direction than in-plane direction.
  - [non-referenced_knowledge] Layered structure allows for preferential in-plane and interlayer ion migration paths depending on crystal symmetry and bonding.
  - [inductive reasoning] Therefore, the phase-separated structure enables ionic conductivity via Cu ion migration in the CIPS phase, with anisotropic behavior dictated by structural features.
### M3  Property → Performance
- cause: Ionic conductivity–electrical property
- effect: Anisotropic Cu ion migration under electric fields
- experiment: Local current vs. time measurements under bias cycling | Electrical transport | params: Repeated bias-on (-8 V, 60 s) and bias-off (varied durations) | result: Two-stage current increase observed: first rapid rise attributed to in-plane Cu ion reassembly, followed by slower rise from out-of-plane interlayer migration.
  - [experimental result] Current-time measurements under bias cycling reveal two-stage conduction behavior indicative of in-plane and out-of-plane Cu ion migration.
  - [image description] Surface depressions after bias application correlate with Cu ion depletion zones, confirming long-range ion migration.
  - [referenced knowledge] Cu ion migration in CIPS follows thermally activated behavior with higher activation energy in out-of-plane direction.
  - [non-referenced_knowledge] In layered materials, ionic migration typically exhibits anisotropy due to structural differences between in-plane and interlayer environments.
  - [deductive reasoning] Hence, the ionic conductivity of CIPS enables anisotropic Cu ion migration under electric fields, with faster in-plane movement and slower interlayer hopping requiring higher energy.
