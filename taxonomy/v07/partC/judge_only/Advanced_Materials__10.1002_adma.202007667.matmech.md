# MatMech content for Advanced_Materials/10.1002_adma.202007667 (judge only; not shown to staff)
- material: Multilayer bioadhesive patch  elements: ['C', 'H', 'O', 'N', 'S', 'Si']  category: ['Polymer', 'Composite Material', 'Biomaterial', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Property → Performance
## Tetrahedron elements
- **Processing**: Origami-based fabrication, cryogenic grinding, UV curing, spin-coating, and assembly of functional layers
- **Structure**: Microtextured bioadhesive layer, hydrophobic fluid layer, and zwitterionic nonadhesive layer
- **Properties**: Interfacial toughness–mechanical property, shear strength–mechanical property, tensile strength–mechanical property, stretchability–mechanical property, fracture toughness–mechanical property
- **Performance**: Resistance to bacterial adhesion, fibrinogen adsorption, and in vivo fibrous capsule formation; strong adhesion in fluid-rich environments
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Origami-based fabrication, cryogenic grinding, UV curing, spin-coating, and assembly of functional layers
- effect: Microtextured bioadhesive layer, hydrophobic fluid layer, and zwitterionic nonadhesive layer
- experiment: Preparation and Assembly of Multilayer Patch | Material synthesis and assembly | params: Cryogenic grinding of dried bioadhesive material at 30 Hz for 2 min; UV curing (284 nm, 10 W power) for 30 min; spin-coating of PU solution at 400 rpm; silicone oil impingement on microtextured surface | result: Successful formation of a multilayer structure comprising a microtextured bioadhesive interface, hydrophobic protective layer, and zwitterionic antifouling layer
  - [experimental result] Bioadhesive film is cryogenically ground into microparticles to create surface texture.
  - [experimental result] UV curing solidifies precursor solution into a dry bioadhesive layer ready for further processing.
  - [experimental result] Spin-coated PU solution bonds the zwitterionic layer to the bioadhesive substrate.
  - [experimental result] Silicone oil is applied to the textured surface to form a stable hydrophobic barrier.
  - [referenced knowledge] Surface microtexture stabilizes the hydrophobic fluid layer via enhanced capillary forces.
  - [non-referenced_knowledge] Origami-based fabrication allows the patch to adopt diverse geometries for surgical end effector compatibility.
  - [deductive reasoning] Thus, the combination of processing steps results in a structured multilayer patch with defined functional layers.
### M2  Structure → Property
- cause: Microtextured bioadhesive layer, hydrophobic fluid layer, and zwitterionic nonadhesive layer
- effect: Interfacial toughness–mechanical property, shear strength–mechanical property, tensile strength–mechanical property
- experiment: Mechanical Testing of Adhered Patches | Peel test, lap-shear test, tensile test (ASTM standards) | params: Applied pressure: 77.5 kPa; adhered to porcine skin submerged in blood bath | result: Measured interfacial toughness: 536.7 ± 93.4 J/m²; shear strength: 56.1 ± 4.7 kPa; tensile strength: 65.0 ± 8.0 kPa
  - [non-referenced_knowledge] Hydrophobic fluid layer prevents premature contamination of bioadhesive layer during delivery.
  - [experimental result] Pressure above 77.5 kPa triggers dewetting of hydrophobic layer, exposing bioadhesive surface.
  - [referenced knowledge] Exposure of bioadhesive layer initiates physical bonding via hydrogen bonds within seconds.
  - [experimental result] Subsequent covalent bond formation between NHS ester groups and tissue amine groups enhances adhesion strength.
  - [non-referenced_knowledge] Zwitterionic layer resists fouling that could otherwise degrade mechanical performance over time.
  - [inductive reasoning] These structural features lead to high measured values of interfacial toughness, shear strength, and tensile strength.
### M3  Property → Performance
- cause: Interfacial toughness–mechanical property, shear strength–mechanical property, tensile strength–mechanical property
- effect: Resistance to bacterial adhesion, fibrinogen adsorption, and in vivo fibrous capsule formation; strong adhesion in fluid-rich environments
- experiment: In vitro and In vivo Antifouling Evaluation | Fluorescence microscopy, histological analysis | params: Incubation with GFP-expressing E. coli (24 h); exposure to heparinized porcine whole blood spiked with Alexa Fluor 488-tagged fibrinogen (60 min); subcutaneous implantation in rats (2 and 4 weeks) | result: Zwitterionic layer reduces E. coli adhesion to ~0.9 counts/mm² vs. ~1370 counts/mm² on hydrophobic surfaces; <0.1% fibrin coverage vs. ~3.09% on hydrophobic surfaces; fibrous capsule thickness ~135 μm vs. ~1163 μm on hydrophobic implants
  - [non-referenced_knowledge] Zwitterionic layer forms tight hydration shell due to electrostatic interactions between charged groups and water molecules.
  - [referenced knowledge] Hydration shell creates high energy cost for biomolecules and bacteria to adsorb onto the surface.
  - [experimental result] Experimental evaluation confirms significantly reduced bacterial adhesion and fibrinogen adsorption on zwitterionic surfaces.
  - [experimental result] In vivo tests show thinner fibrous capsule formation around zwitterionic-layered implants.
  - [deductive reasoning] Combined with high mechanical strength, these properties ensure robust performance in challenging physiological environments.
