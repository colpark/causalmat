# MatMech content for Advanced_Materials/10.1002_adma.202007738 (judge only; not shown to staff)
- material: DNA nanoflower (DNF)  elements: ['C', 'H', 'O', 'N', 'P', 'Mg']  category: ['Nanomaterial', 'Biomaterial']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Rolling circle amplification (RCA) with cholesterol-labeled DNA (Chol-DNA) incorporation
- **Structure**: Flower-shaped, densely packed DNA amplicons with cholesterol decoration
- **Properties**: FRET ratio–optical property
- **Performance**: Ratiometric intracellular ATP detection in prostate cancer cells
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Rolling circle amplification (RCA) with cholesterol-labeled DNA (Chol-DNA) incorporation
- effect: Flower-shaped, densely packed DNA amplicons with cholesterol decoration
- experiment: Synthesis of cholesterol-decorated DNA nanoflowers (CnDNF) | Scanning Electron Microscopy (SEM), Dynamic Light Scattering (DLS), Transmission Electron Microscopy (TEM) | params: RCA reaction time (6 h vs. 20 h), Chol-DNA concentration (1×10⁻⁶ M, 2×10⁻⁶ M, 5×10⁻⁶ M) | result: After 6 h of RCA, discrete nDNF particles (~200–300 nm) formed; after 20 h, larger μDNF microparticles (1–2 μm). Cholesterol incorporation led to slightly smaller structures at higher concentrations.
  - [experimental result] Rolling circle amplification produces long polymeric DNA strands through repetitive copying of a circular template.
  - [non-referenced_knowledge] During RCA, released pyrophosphate ions form Mg₂PPi crystals when Mg²⁺ is present, promoting self-condensation of DNA into flower-shaped structures.
  - [non-referenced_knowledge] Chol-DNA hybridizes in situ during RCA and influences DNA packing via hydrophobic interactions, leading to more compact structures.
  - [image description] Figure shows TEM and SEM images confirming uniform morphology across different Chol-DNA concentrations with slight size reduction at higher cholesterol content.
  - [deductive reasoning] Thus, RCA-based processing yields cholesterol-decorated DNA nanoflowers with controlled structure depending on Chol-DNA concentration and reaction time.
### M2  Structure → Performance
- cause: Flower-shaped, densely packed DNA amplicons with cholesterol decoration
- effect: Ratiometric intracellular ATP detection in prostate cancer cells
- experiment: Flow cytometry and confocal microscopy analysis of cellular uptake and ATP sensing | Confocal microscopy, Flow cytometry, Fluorescence correlation spectroscopy (FCS) | params: Cell type: LNCaP (PSMA-positive) vs. PC3 (PSMA-null); Incubation time: 2 h vs. 24 h; Drug treatment: oligomycin (ATP inhibitor), etoposide (ATP inducer) | result: CnDNF showed significantly higher uptake in LNCaP cells compared to PC3, confirmed by flow cytometry. Confocal imaging revealed red fluorescence from Cy3-labeled CnDNF in LNCaP, indicating successful internalization. FRET ratio changes upon ATP binding demonstrated effective ratiometric sensing.
  - [non-referenced_knowledge] Cholesterol-modified DNA strands enhance cellular uptake by interacting with the lipid bilayer membrane.
  - [experimental result] PSMA-targeting aptamers mediate receptor-specific internalization into LNCaP cells, confirmed by flow cytometry showing higher Cy3 signal in PSMA-expressing cells.
  - [image description] Figure shows preferential uptake of CnDNF in LNCaP cells over PC3, with increased efficiency at higher concentrations.
  - [non-referenced_knowledge] FRET-based signaling occurs when ATP binds to the aptamer, causing release of the acceptor-labeled strand and change in FRET ratio.
  - [image description] Confocal microscopy confirms FRET signal changes in response to ATP modulation by drugs like oligomycin and etoposide.
  - [deductive reasoning] Thus, the structured, cholesterol-decorated DNA nanoflower enables targeted, ratiometric ATP sensing within living cells.
