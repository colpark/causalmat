# Judge review: Acta_Materialia/10.1016_j.actamat.2015.04.055

**Verdict:** accept with minor fixes. 14 spine nodes, 39 total, one connected path with two branches (beta_o softening; gamma/alpha2 hardening). 1 audit (a1), fair.

## Changes
- e(n9->n12): rel causes -> counteracts. The extra Mo in beta_o adds solid-solution hardening that opposes the softening n12 stands for (v04 counteracts: loss term of a trade-off); MatMech M3 and the F4 linked text say the same. mode/mode_basis dropped from n9->n12 and n10->n12 (n12 now has one causes edge)
- o5 technique TEM:BF -> TEM:brightfield (controlled form)
- o11 technique EBSD:transmission -> TEM:EBSDtransmission (controlled form, normalize_technique.py)
- o8, o8b, o9, o10 technique APT -> APT:proximity (panels are proximity histograms)

## Panel checks (every cited crop opened; 13 crops, 22 node-panel citations)

| node | panels | ruling | correct id | note |
|---|---|---|---|---|
| n7 | F1a, F1b | confirmed | - | bright beta_o islands common in a, rare in b; alpha2 change not judgeable; partial is right |
| n6 | F1a, F1b | confirmed | - | a globular; b has coarse lamellar colonies (left half) |
| o1 | F1a, F1b | confirmed | - | BSE; beta_o arrowed in a |
| o2 | F1a, F1b | confirmed | - | morphology contrast as stated |
| n13 | F2b | confirmed | - | C proxigram ~0.3-0.35 at.% at -4 nm (gamma) to ~0.05 at.% at 6-8 nm (beta_o) |
| n14 | F2b | confirmed | - | peak c_max ~0.68 at.% at ~-0.6 nm |
| o9 | F2b | confirmed | - | levels read correctly |
| o10 | F2b | confirmed | - | c_max position and value read correctly |
| n15 | F3a, F3d | confirmed | - | a has no tick labels; full figure shows a and d share the 6.5-10.5 GPa axis; mode 7.4-7.5 -> 8.35-8.4 |
| o3 | F3a, F3d | confirmed | - | ranges 7.05-8.85 and 7.25-9.65 GPa |
| n16 | F3b, F3e | confirmed | - | shared 8.0-11.5 GPa axis; 8.25-9.9 -> 8.85-10.95 GPa |
| o3b | F3b, F3e | confirmed | - | as stated |
| n12 | F3c, F3f | confirmed | - | shared 8.0-12.0 GPa axis; mode 10.0 -> 8.9 GPa |
| o4 | F3c, F3f | confirmed | - | ranges 9.15-11.55 and 8.45-9.75 GPa |
| a1 | F3f | confirmed | - | mode ~8.9 GPa; 8.0 GPa reference is text-only, marked in requires_unseen |
| n10 | F4a, F4b | confirmed | - | mottled beta_o+omega_o in a with omega_o-indexed SAED spots; featureless beta_o and beta_o-only SAED in b |
| o5 | F4a, F4b | confirmed | - | BF TEM contrast as stated |
| o6 | F4a, F4b | confirmed | - | SAED insets inside both crops; extra spots in a only |
| n21 | F5a | confirmed | - | labelled omega_o (blue) and beta_o (green) regions with OR boundary lines |
| o11 | F5a | confirmed | - | t-EBSD phase map of the tip |
| o8 | F5c | confirmed | - | Mo ~0.35-0.4 at.% in omega_o, ~3 at.% at 8-9 nm in beta_o |
| o8b | F5c | confirmed | - | c_max ~4.7 at.% at ~3 nm |

Overturned: 0.

## Technique mismatches

No cue-class conflicts on cited panels. Controlled-form fixes:
- o5 (F4a): TEM:BF -> TEM:brightfield
- o11 (F5a): EBSD:transmission -> TEM:EBSDtransmission
- o8 (F5c): APT -> APT:proximity
- o8b (F5c): APT -> APT:proximity
- o9 (F2b): APT -> APT:proximity
- o10 (F2b): APT -> APT:proximity

No cited panel has a technique that conflicts with its cue classes (F1, F4, F5a micrograph cue fits SEM/TEM; F2b, F3, F5c have no cue). F2a and F5b (APT reconstructions, false 'micrograph' cue) stay uncited: no node needs them (F2a does not visibly show the C accumulation; F5b's elongated omega_o grains are not on the graph).

read_from: o5 and o11 restate listed annotations ('β+w', 'om') and are 'annotation'; o6 kept 'pixels' (the presence/absence of extra spots is read from the SAED pixels; the only listed F4b string is the {011}beta_o index); o3/o3b/o4/o8/o8b/o9/o10/a1 read values from axes, and c_max is not a listed annotation

## Mode changes
- n12: joint (causes from n10 and n9) -> single causes edge (n10); n9 -> n12 re-relled to counteracts. the Mo solid-solution term opposes the softening; it is not a joint cause of it

## Source checks

No changes. All source/requires_unseen fields checked: table-dependent claims (n7, n9, n19) are text with the tables listed; a1 lists the literature 8.0 GPa value; n17/n18 inferred; figure-sourced nodes (n6, n10, n12-n16, n21) are readable from the cited panels.

## MatMech (read after the graph was final; graph not edited)

Supports 2 · contradicts 0 · not covered 2

| M | cause -> effect | verdict | nodes | note |
|---|---|---|---|---|
| M1 | HIP 1200 C/4 h/200 MPa + furnace cooling -> structurally homogeneous microstructure in both alloys | not_covered | n5, n6 | graph has forging+homogenisation producing the globular vs lamellar morphologies (attributed to C), not HIP or homogeneity |
| M2 | C enrichment in alpha2 and segregation at phase interfaces -> higher hardness of gamma and alpha2 in TNM0.75C | supports | n13, n17, n15, n16, n14 | graph carries dissolved C (solid solution) -> gamma/alpha2 hardening; interface segregation (n14) is not linked to hardness, and C in alpha2 is not shown |
| M3 | suppression of omega_o in beta_o -> beta_o softens in TNM0.75C despite higher Mo | supports | n10, n12, n9, n11 | n10 causes n12; n9 counteracts n12 (Mo solid-solution term) |
| M4 | VAR (TNM) vs VIM (TNM0.75C) melting -> beta_o fraction 19% vs 2% | not_covered | n7, n8 | graph has the beta_o reduction but attributes it to C alpha-stabilisation (as the paper does); melting route absent |
