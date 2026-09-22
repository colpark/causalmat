# Judge review: Advanced_Functional_Materials/10.1002_adfm.202005640

**Verdict: accept with changes.** Structure only. No figure or crop was opened, and panel citations and techniques are left to the blind second read.

## Spine and rules
- **Spine:** 15 connected nodes (was 16): gap s1 -> hypothesis s2 -> PCO base s3 + delta sweep s4 + dynamic I-V method s5 -> PLD s6 -> anneal/quench s7 -> defect concentration s10 + argued tripole ordering s12 -> MEC m2 (tripoles constrict pathways) -> prefactor rise p3; branch: s10 -> Em rise p2 (counteracts p1) -> tradeoff t1 -> vacancy mobility rises with delta p1 -> conclusion d1. The stages run in order, with one main line and one opposing branch.
- **Evidence:** s10 (o3, k1, k2); s12 (basis argued, k6, o8 qualifies); m2 (k6); p3 (o21); p2 (o17); t1 (o21, and p4 as support); p1 (o15, o18, o20, o19 qualifies).
- **v04:** all types, rels and mm_ops are valid, and every figure-bearing OBS edge carries an op. No claim has two or more causes edges.
- **Audits:** 3 (o8, o19, d2). All are fair: o19 is a text-silent series that breaks the monotonic trend; o8 sets Raman association against the tripole argument; d2 is the authors' own open question.

## Changes
- **f1 taken off the spine and retyped** from PRF/service_capability to PRP/behavior_class (object = assembly). The hysteretic crossbar I-V is how the mobility is extracted; it is not a result of mobility rising with delta, so `p1 -causes-> f1` was wrong. The edges are now `f1 -supports-> p1` and `p1 -supports-> d1`, and `f1 -> d1` is removed.
- **p1 retyped** from PRP/descriptor to PRP/value: vacancy mobility is the headline measured property.
- **o10 relabelled** to a single reading. Its temperature dependence moved to image_note.

## Splits and merges
- **p3 split:** p3 keeps "the prefactor rises from ~40 to ~5600 with delta". New **p4** (PRP/value, side) holds "log prefactor rises linearly with Em (Meyer-Neldel-like)". o21 evidences p4, and p4 supports t1.
- **s13 split:** s13 keeps "electronic conductivity falls ~17x". New **p5** (PRP/value, electrical, side) holds "electronic Ea rises from 0.36 to 0.51 eV". The o12 evidence moved from s13 to p5, and s10 causes p5.
- **s11 split:** s11 keeps "defect association grows with delta". New **s15** (STR/phase/lattice, side) holds "local lattice distortion grows". The o6 and o8 evidence moved from s11 to s15, o7 also evidences s15, s10 causes s15, and k3 is a premise for s15.
- Merges: none.

## Source / read_from changes
- source changed from figure to text, with requires_unseen filled:
  - p1: the plotted mu_i is the oxygen-vacancy mobility from Eq. 1.
  - p2: the activation energy is read as the migration enthalpy (Eq. 2).
  - s13, o11 and o12: bulk conductivity ≈ sigma_e, per the F4b caption.
- read_from: no changes. The annotation readings (o12, o15, o17, o20) are already "annotation". In o14 and o1 the listed strings serve only as series or region identifiers.

## Mode changes
- None. After the edits, no claim has two or more causes edges.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 3, contradicts 0, not covered 0.
- **M1** PLD (+annealing) -> polycrystalline columnar film: **supports** (s6, s8, s9, o1, o2). The graph links this state to PLD only, not to annealing.
- **M2** vacancies / Pr valence (delta) -> higher ionic mobility, with Em rising weakly: **supports** (s10, s12, p2, p3, p4, t1, p1). The mechanisms differ: the graph argues for a prefactor tied to quenched-in tripoles (m2), while MatMech reads it as percolative pathways. MatMech gives 13x, while the graph has ~1.2-1.3 decades.
- **M3** anneal in varied pO2 + quench -> modulated vacancy concentration and Pr valence: **supports** (s7, s10, o3, k2).
