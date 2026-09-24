# MatMech content for Advanced_Materials/10.1002_adma.202006716 (judge only; not shown to staff)
- material: Porous carbonaceous electrodes  elements: ['C', 'H', 'N', 'O']  category: ['Polymer', 'Composite Material']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Non-solvent induced phase separation (NIPS) with varying ratios of polyacrylonitrile (PAN) to poly(vinylpyrrolidone) (PVP)
- **Structure**: Bimodal porous structure with interconnected large macrovoids (>50 μm) and smaller microvoids (<5 μm)
- **Properties**: Volumetric ECSA–electrochemical property, permeability–mechanical property
- **Performance**: Improved power density and reduced kinetic and mass transport overpotentials in redox flow batteries
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Non-solvent induced phase separation (NIPS) with varying ratios of polyacrylonitrile (PAN) to poly(vinylpyrrolidone) (PVP)
- effect: Bimodal porous structure with interconnected large macrovoids (>50 μm) and smaller microvoids (<5 μm)
- experiment: Scanning Electron Microscopy (SEM) and X-ray Tomography (XTM) | Microstructural characterization | params: Varying PAN:PVP ratios (1:1, 3:4, 2:3), SEM imaging at 70 kV acceleration voltage; XTM using Zeiss Xradia 620 Versa with 20× objective, 50 kV voltage | result: SEM revealed finger-like macrovoids (>100 μm) connected to microvoid networks. XTM confirmed internal honeycomb-like distribution of macrovoids in all PSP materials.
  - [experimental result] A viscous mixture of PAN and PVP in DMF was cast and immersed in water to initiate phase separation and PVP leaching.
  - [image description] SEM images show macrovoids (>100 μm) interconnected with microvoid networks across samples with different PAN:PVP ratios.
  - [referenced knowledge] Phase separation techniques like NIPS enable generation of non-fibrous porous materials with long-range interconnected microstructures.
  - [non-referenced_knowledge] Thermodynamics and kinetics of phase separation determine the final microstructure, which is tunable via polymer ratio and solvent conditions.
  - [deductive reasoning] Therefore, varying PAN:PVP ratio during NIPS results in bimodal porous structures with interconnected macro- and micro-voids.
### M2  Structure → Performance
- cause: Bimodal porous structure with interconnected large macrovoids (>50 μm) and smaller microvoids (<5 μm)
- effect: Improved power density and reduced kinetic and mass transport overpotentials in redox flow batteries
- experiment: Single-electrolyte flow cell polarization and impedance testing | Electrochemical performance testing | params: Iron chloride single-electrolyte setup with linear velocity of 5 cm/s; EIS measurements at open-circuit potential with Randles-like circuit model | result: PSP electrodes showed lower polarization losses and reduced charge-transfer resistance compared to SGL 29AA. PSP-2:3 demonstrated best performance due to optimal pore balance.
  - [experimental result] Flow cell experiments showed that PSP electrodes outperformed commercial SGL 29AA in terms of polarization losses and charge-transfer resistance.
  - [image description] PSP-2:3 had higher porosity and permeability than other samples, leading to reduced pressure losses and better electrochemical performance.
  - [referenced knowledge] Interconnected porous networks enhance convective transport while high surface area regions improve reaction kinetics.
  - [non-referenced_knowledge] Optimal pore structure balances electrolyte transport efficiency and electrochemically active surface area.
  - [deductive reasoning] Thus, the bimodal pore structure in PSP electrodes improves power density by simultaneously enhancing electrolyte transport and electrochemical activity.
### M3  Processing → Performance
- cause: Non-solvent induced phase separation (NIPS) with varying ratios of polyacrylonitrile (PAN) to poly(vinylpyrrolidone) (PVP)
- effect: Improved power density and reduced kinetic and mass transport overpotentials in redox flow batteries
- experiment: Full-cell vanadium RFB discharge polarization and impedance testing | Battery performance evaluation | params: Vanadium electrolyte (1.5 M V in 2.6 M H2SO4), linear velocity of 10 cm/s, EIS measurements at 50% SoC | result: PSP-2:3 electrode achieved significantly enhanced power density (≈1.5 W/cm²) compared to SGL 29AA (≈0.9 W/cm²), with reduced total resistance.
  - [experimental result] Full-cell tests showed that PSP-2:3 electrode delivered significantly higher power density than commercial SGL 29AA electrode in VRFB configuration.
  - [image description] Nyquist plots indicated reduced charge-transfer resistance and ohmic losses in PSP-2:3 compared to SGL 29AA.
  - [referenced knowledge] Tailoring electrode microstructure through scalable methods enhances performance in convection-driven electrochemical systems.
  - [non-referenced_knowledge] Controlling pore architecture during synthesis directly impacts electrochemical performance metrics such as power density and overpotential.
  - [inductive reasoning] Therefore, NIPS-based processing with tailored PAN:PVP ratios improves RFB performance by generating optimized pore structures that minimize resistive losses.
