# MatMech content for Advanced_Composites_and_Hybrid_Materials/s42114-021-00414-x (judge only; not shown to staff)
- material: SCF/GB@rGO/PDMS  elements: ['C', 'H', 'O', 'Si']  category: ['Composite Material', 'Polymer', 'Nanomaterial', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Spatial confining forced network assembly (SCFNA) method with vacuum drying, mixing, compression, and curing at 120°C
- **Structure**: Compact thermal conductive networks of short carbon fibers (SCFs) with hetero-structured glass bubble coated reduced graphene oxide (GB@rGO) fillers filling gaps; core-shell structure of GB@rGO (insulating glass core, conductive rGO shell)
- **Properties**: thermal conductivity–thermal property, electrical conductivity–electrical property, elongation at break–mechanical property, tensile strength–mechanical property
- **Performance**: Superior heat transfer capacity in TIM applications, 5°C lower CPU core temperature compared to commercial thermal grease, flexibility with bending/twisting/folding capability, thermal stability over 5 heating-cooling cycles
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Spatial confining forced network assembly (SCFNA) method involving vacuum drying at 100°C, mixing, compression from initial thickness to 2.0 mm at 120°C for 10 s, and further compression to 0.1–0.6 mm with 10 min pressure-maintained curing at 120°C
- effect: Formation of compact, orderly aligned thermal conductive networks of short carbon fibers (SCFs) within PDMS matrix, with GB@rGO fillers preferentially dispersing in gaps between SCFs to form a core-shell hetero-structure
- experiment: SCF/GB@rGO/PDMS composite fabrication via SCFNA | Composite processing | params: Vacuum drying at 100°C for 3 h; mixing at 40 rpm for 10 min; compression to 2.0 mm at 120°C for 10 s; further compression to 0.1–0.6 mm; curing at 120°C for 10 min | result: Ordered SCF networks and GB@rGO dispersion observed via SEM
  - [experimental result] SCF/GB@rGO/PDMS composites are fabricated using spatial confining forced network assembly (SCFNA) involving vacuum drying, mixing, and controlled compression at 120°C.
  - [image description] Figure 2 shows the schematic of the SCFNA process, where compression forces align SCFs and distribute GB@rGO fillers.
  - [non-referenced_knowledge] SCFs have high aspect ratio and promote phonon transport along their axial direction, forming conductive pathways.
  - [non-referenced_knowledge] GB@rGO has a core-shell structure: insulating glass bubble core reduces heat loss, while conductive rGO shell bridges SCF gaps.
  - [image description] SEM images (Fig. 5 and 6) confirm SCFs are orderly aligned and GB@rGO fills the interstitial spaces, preventing PDMS from occupying high-resistance gaps.
  - [deductive reasoning] Thus, SCFNA enables formation of a compact, interconnected thermal network with reduced phonon scattering at interfaces.
### M2  Structure → Property
- cause: Compact thermal conductive network of aligned SCFs with GB@rGO fillers in interstitial gaps forming a core-shell hetero-structure
- effect: Thermal conductivity (λ) of 23.415 W/m·K at 0.1 mm thickness with 30 wt% SCF and 1 wt% GB@rGO; electrical conductivity of 1330 S/m; elongation at break of 86.75%
- experiment: Thermal conductivity measurement | Laser flash difusivity (LFA 467) | params: Sample thickness: 0.1–2.0 mm; GB@rGO content: 0–6 wt%; λ calculated via λ = α·Cp·ρ | result: λ = 23.415 W/m·K for 0.1 mm-thick composite with 1 wt% GB@rGO; 85.72× enhancement over pure PDMS
  - [image description] SEM images (Fig. 5, 6) confirm SCFs are densely aligned and GB@rGO is located in the gaps between them.
  - [experimental result] Raman, FTIR, XPS, and TGA confirm successful coating of rGO on GB, with preserved sp2 carbon structure for conductivity.
  - [non-referenced_knowledge] GB@rGO has a core-shell structure: insulating glass core reduces heat loss, conductive rGO shell enhances inter-filler coupling.
  - [experimental result] Thermal conductivity peaks at 1 wt% GB@rGO, indicating optimal gap-filling without network disruption.
  - [experimental result] Electrical conductivity follows the same trend, suggesting electrons are the primary carriers for both thermal and electrical transport.
  - [deductive reasoning] Thus, the structure enables efficient phonon and electron transport, resulting in ultrahigh thermal and electrical conductivity.
### M3  Property → Performance
- cause: Ultrahigh thermal conductivity (23.415 W/m·K) and electrical conductivity (1330 S/m) of SCF/GB@rGO/PDMS composite with 1 wt% GB@rGO and 0.1 mm thickness
- effect: Superior heat transfer capacity in TIM applications, evidenced by 5°C lower CPU core temperature than commercial thermal grease and stable performance over 5 heating-cooling cycles
- experiment: TIM performance test using CPU cooling | Thermal interface material test | params: Composite vs. NVV commercial thermal grease (NT-6) between CPU and aluminum heat sink; 10V heating plate; temperature monitored via infrared imager and Master Lu software | result: CPU core temperature 5°C lower with SCF/GB@rGO/PDMS composite than with commercial grease after 600 s full load
  - [experimental result] The composite achieves λ = 23.415 W/m·K, the highest among tested compositions.
  - [image description] Infrared thermal imaging (Fig. 8b, c) shows lower surface temperature on the composite during heating, indicating superior heat transfer.
  - [experimental result] CPU temperature test (Fig. 8e) shows 5°C reduction compared to commercial thermal grease, directly linking high λ to improved performance.
  - [experimental result] Thermal conductivity remains stable over five heating-cooling cycles (Fig. 7c), confirming reliability under operational conditions.
  - [image description] The composite is flexible and can be bent, twisted, and folded without degradation (Fig. 10c, d), enabling conformal contact with irregular surfaces.
  - [deductive reasoning] Thus, the high thermal and electrical properties translate directly to superior TIM performance in real electronic cooling applications.
### M4  Processing → Property
- cause: Spatial confining forced network assembly (SCFNA) with controlled compression to 0.1 mm thickness and curing at 120°C
- effect: Thermal conductivity of 23.415 W/m·K and electrical conductivity of 1330 S/m for SCF(30 wt%)/GB@rGO(1 wt%)/PDMS
- experiment: Thermal and electrical conductivity measurement under varying compression | Laser flash difusivity (LFA 467) and four-probe resistance measurement | params: Sample thickness varied from 2.0 mm to 0.1 mm; GB@rGO content from 0 to 6 wt%; λ and σ measured for each condition | result: λ increases from 0.367 W/m·K (2 mm) to 23.415 W/m·K (0.1 mm); σ increases from 651 S/m (0 wt% GB@rGO) to 1330 S/m (1 wt% GB@rGO)
  - [experimental result] SCFNA involves compression of the composite to thicknesses as low as 0.1 mm, forcing SCFs into close contact.
  - [experimental result] Figure 7a shows thermal conductivity increases 64-fold as thickness decreases from 2 mm to 0.1 mm.
  - [experimental result] Figure 9a shows electrical conductivity peaks at 1 wt% GB@rGO, indicating optimal network connectivity.
  - [non-referenced_knowledge] The same trend in λ and σ suggests both are governed by electron-mediated transport through connected networks.
  - [deductive reasoning] Thus, SCFNA processing directly enhances both thermal and electrical properties by optimizing network density and connectivity.
