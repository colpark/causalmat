# MatMech content for Acta_Materialia/10.1016_j.actamat.2021.116790 (judge only; not shown to staff)
- material: FeCrMnNiCo (Cantor alloy)  elements: ['Fe', 'Cr', 'Mn', 'Ni', 'Co']  category: ['Metals and Alloys', 'Crystalline Material', 'Coatings and Thin Films']
- MST chain: Processing → Structure → Performance
## Tetrahedron elements
- **Processing**: Ar+ ion sputtering and annealing cycles at various temperatures and durations
- **Structure**: Surface segregation of Mn and Ni, terraced morphology on (320) surface, anisotropic row-like structure on (110) surface
- **Properties**: Surface segregation–chemical property, Mn desorption–thermal property
- **Performance**: Upper temperature limit for use in high vacuum and aerospace applications
## Extracted mechanisms (MatMech)
### M1  Processing → Structure
- cause: Ar+ ion sputtering and annealing cycles at various temperatures and durations
- effect: Surface segregation of Mn and Ni, terraced morphology on (320) surface, anisotropic row-like structure on (110) surface
- experiment: XPS measurements | X-ray photoelectron spectroscopy | params: Angle-resolved XPS with varying take-off angles (0°–70°), annealing up to 1000 K | result: Mn and Ni surface content increases linearly with temperature up to 873 K; Mn desorbs above this temperature
  - [experimental result] XPS measurements show Mn and Ni surface content increases linearly with annealing temperature up to 873 K
  - [experimental result] Angle-resolved XPS confirms surface segregation with Mn concentration tripling at near-surface regions
  - [image description] STM and LEED data reveal distinct surface structures: anisotropic rows on (110), terraces on (320)
  - [non-referenced_knowledge] Mn exhibits the lowest surface energy among constituent elements, driving its surface enrichment
  - [referenced knowledge] Mn-Ni pair enthalpy of mixing is highly negative, favoring their mutual segregation
  - [deductive reasoning] Thus, Mn surface enrichment facilitates Ni diffusion to the surface, leading to co-segregation under thermal activation
### M2  Structure → Performance
- cause: Surface segregation of Mn and Ni, terraced morphology on (320) surface, anisotropic row-like structure on (110) surface
- effect: Upper temperature limit for use in high vacuum and aerospace applications
- experiment: Thermal desorption analysis | XPS monitoring of surface composition during heating | params: Annealing up to 1000 K, repeated sputtering-annealing cycles | result: Mn desorbs above 873 K, leaving behind Ni-rich surface; memory effect observed after high-temperature exposure
  - [experimental result] XPS shows Mn content decreases abruptly above 873 K while Ni continues to increase
  - [referenced knowledge] Mn has significantly higher vapor pressure than other elements, facilitating desorption
  - [non-referenced_knowledge] Diffusion rate of Mn cannot compensate for desorption flux above 873 K
  - [experimental result] Repeated annealing cycles demonstrate memory effect—surface does not return to original state immediately
  - [deductive reasoning] Thus, Mn desorption alters surface composition beyond HEA concept, limiting usable temperature range
