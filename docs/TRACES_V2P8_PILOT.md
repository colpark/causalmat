# Traces v2.8 pilot — grading answers against the key

Every verdict is model against model.

8 of the 76 derived_input items, one per paper. v2.7 showed that asking a comparer whether two answers differ cannot judge a single item: two samples of one prompt differ 29% of the time. Here the target is fixed. Each item already has a drafted key, so the key is broken into atomic claims and every answer is measured against the same list.

Two things this pilot has that v2.7 did not. A third arm, C, holding the earlier result alone: beating arm A only shows the earlier result added something, and cannot show the measurement was needed at all. And scores averaged over 6 samples before any threshold, rather than a vote over single draws.

## The 8 items and why each was picked

| # | item | journal | label | upstream |
|---|---|---|---|---|
| 1 | `di_acta_materia_com_o10_o14_o12_n13` | Acta Materialia | discriminating | `acta_materia_com_o10_o14` (complementary) |
| 2 | `di_advanced_ene_spi_o1_o12b_o20_n10` | Advanced Energy Materials | discriminating | `advanced_ene_spi_o1_o12b` (spine_edge) |
| 3 | `di_journal_of_a_spi_o13_o20_o22_n15` | Journal of Advanced Ceramics | discriminating | `journal_of_a_spi_o13_o20` (spine_edge) |
| 4 | `di_materials_ch_com_o1_o7_o3_r1` | Materials Characterization | discriminating | `materials_ch_com_o1_o7` (complementary) |
| 5 | `di_journal_of_m_spi_o15_o17_o16_m2` | Journal of Magnesium and Alloys | conditional mechanism | `journal_of_m_spi_o15_o17` (spine_edge) |
| 6 | `di_bioactive_ma_com_o11_o12_n18_o15_n20` | Bioactive Materials | associative | `bioactive_ma_com_o11_o12_n18` (complementary) |
| 7 | `di_advanced_fun_spi_o1_o4_o6_n10` | Advanced Functional Materials | associative | `advanced_fun_spi_o1_o4` (spine_edge) |
| 8 | `di_journal_of_m_spi_o14_o10_o11_f2` | Journal of Materials Science & Technology | conditional mechanism | `journal_of_m_spi_o14_o10` (spine_edge) |

1. **`di_acta_materia_com_o10_o14_o12_n13`** — labelled discriminating, the scarcest causal-strength label in the pool (4 of 76); upstream is a complementary v2.5 item
2. **`di_advanced_ene_spi_o1_o12b_o20_n10`** — labelled discriminating, the scarcest causal-strength label in the pool (4 of 76); upstream is a spine_edge v2.5 item
3. **`di_journal_of_a_spi_o13_o20_o22_n15`** — labelled discriminating, the scarcest causal-strength label in the pool (4 of 76); upstream is a spine_edge v2.5 item
4. **`di_materials_ch_com_o1_o7_o3_r1`** — labelled discriminating, the scarcest causal-strength label in the pool (4 of 76); upstream is a complementary v2.5 item
5. **`di_journal_of_m_spi_o15_o17_o16_m2`** — labelled conditional mechanism; the scarcer of the two remaining labels, 15 of 76 against 56 associative; Journal of Magnesium and Alloys is not yet represented; upstream is a spine_edge v2.5 item
6. **`di_bioactive_ma_com_o11_o12_n18_o15_n20`** — labelled associative; Bioactive Materials is not yet represented; upstream is a complementary v2.5 item
7. **`di_advanced_fun_spi_o1_o4_o6_n10`** — labelled associative; Advanced Functional Materials is not yet represented; upstream is a spine_edge v2.5 item
8. **`di_journal_of_m_spi_o14_o10_o11_f2`** — labelled conditional mechanism; the scarcer of the two remaining labels, 15 of 76 against 56 associative; Journal of Materials Science & Technology is not yet represented; upstream is a spine_edge v2.5 item

Constraints, all asserted in `select.py` rather than eyeballed: 8 items from 8 papers and 8 journals; all 4 discriminating items taken (they sit in 4 different papers, so one-per-paper allows it); upstream mix {'complementary': 3, 'spine_edge': 5}.

## Part A — splitting the key into claims

**Tag agreement between the two agents: 94.7%** (71 of 75). The stop rule was 70%; it did not fire.

All 8 of 8 items have at least one combined claim, so none stopped here.

| tag | claims kept |
|---|---|
| combined | 29 |
| input | 21 |
| observation | 21 |
| limit (carried from the key, not tagged) | 32 |

| item | combined claims |
|---|---|
| `di_acta_materia_com_o10_o14_o12_n13` | 5 |
| `di_advanced_ene_spi_o1_o12b_o20_n10` | 1 |
| `di_journal_of_a_spi_o13_o20_o22_n15` | 2 |
| `di_materials_ch_com_o1_o7_o3_r1` | 4 |
| `di_journal_of_m_spi_o15_o17_o16_m2` | 4 |
| `di_bioactive_ma_com_o11_o12_n18_o15_n20` | 3 |
| `di_advanced_fun_spi_o1_o4_o6_n10` | 7 |
| `di_journal_of_m_spi_o14_o10_o11_f2` | 3 |

The 4 disagreements are substantive, and three of the four run in the direction the checker was told to police — a claim called combined that one side reaches alone:

- `di_advanced_ene_spi_o1_o12b_o20_n10` — proposed **combined**, checker says **observation**
  > Zn is taken up into framework-type lattice positions rather than existing merely as an unlocated bulk quantity in the electrode.
  > *New measurement's ZnN4 tetrahedra linking into the FeC6 framework alone shows Zn occupies lattice sites, not just bulk; earlier quantity data is not needed.*
- `di_advanced_ene_spi_o1_o12b_o20_n10` — proposed **combined**, checker says **observation**
  > The uptake of Zn occurs alongside, and alters, the Mn coordination sphere.
  > *New measurement itself states 'with Zn added' Mn coordination changes MnN3 to MnN4, directly tying Zn uptake to altered Mn coordination.*
- `di_journal_of_a_spi_o13_o20_o22_n15` — proposed **observation**, checker says **combined**
  > This power comparison is taken at the 10 wt% (f-P0.10) loading.
  > *The observation states 10 MOhm resistance, not wt% loading; asserting '10 wt%' conflates that resistance figure with the wt% range mentioned only in the earlier result, so it is not observation-only.*
- `di_advanced_fun_spi_o1_o4_o6_n10` — proposed **combined**, checker says **observation**
  > The size of this strain build-up differs by crystalline state.
  > *The new measurement alone already gives different magnitudes for SC, PC, HOC, directly showing the size differs by phase without needing the earlier result.*

## Part B and C — three arms, six samples, graded against the claims

  - arm A: the new measurement alone, with its panels
  - arm B: the measurement plus the earlier result
  - arm C: the earlier result alone, no measurement and no panels

v2.7's item question names both sides, so arms A and C would each have been asked about material they were not given — v2.7's own arm A had that flaw. Each arm is asked a question matching what it holds; all three are graded against the same claim list.

144 answers graded. The grader saw one answer and the claim list, never the arm label, the other answers, the earlier result or the measurement. Every "stated" ruling had to quote the answer; 0 rulings were withdrawn for having no quote.

## Part D — the result

| arm | what it held | mean combined score | mean limit score |
|---|---|---|---|
| A | the measurement alone | 0.0665 | 0.1292 |
| B | measurement + earlier result | 0.7744 | 0.5649 |
| C | the earlier result alone | 0.0915 | 0.3101 |

Across the 8 items: the input is judged needed on **8 of 8**, the observation on **7 of 8**, and **7 of 8 come out compositional** at a margin of 0.25.

**Split halves agree on 8 of 8 items** (and on both sub-decisions for 8). The stop rule was 6 of 8: it did not fire, so the compositional count above stands.

| item | label | comb. | A | B | C | B−A | B−C | input? | obs? | compositional | halves agree |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `di_acta_materia_com_o10_o14_o12_n1` | discriminating | 5 | 0.13 | 0.60 | 0.00 | +0.47 | +0.60 | yes | yes | **yes** | yes |
| `di_advanced_ene_spi_o1_o12b_o20_n1` | discriminating | 1 | 0.33 | 0.83 | 0.00 | +0.50 | +0.83 | yes | yes | **yes** | yes |
| `di_journal_of_a_spi_o13_o20_o22_n1` | discriminating | 2 | 0.00 | 0.58 | 0.50 | +0.58 | +0.08 | yes | no | no | yes |
| `di_materials_ch_com_o1_o7_o3_r1` | discriminating | 4 | 0.00 | 1.00 | 0.00 | +1.00 | +1.00 | yes | yes | **yes** | yes |
| `di_journal_of_m_spi_o15_o17_o16_m2` | conditional mechanism | 4 | 0.04 | 0.92 | 0.21 | +0.88 | +0.71 | yes | yes | **yes** | yes |
| `di_bioactive_ma_com_o11_o12_n18_o1` | associative | 3 | 0.00 | 1.00 | 0.00 | +1.00 | +1.00 | yes | yes | **yes** | yes |
| `di_advanced_fun_spi_o1_o4_o6_n10` | associative | 7 | 0.02 | 0.60 | 0.02 | +0.57 | +0.57 | yes | yes | **yes** | yes |
| `di_journal_of_m_spi_o14_o10_o11_f2` | conditional mechanism | 3 | 0.00 | 0.67 | 0.00 | +0.67 | +0.67 | yes | yes | **yes** | yes |

### How much of this is the design guaranteeing its own answer

Arms A and C score 0.0665 and 0.0915 on combined claims, against 0.7744 for arm B. That gap is large, and most of it is built in: a claim is only tagged combined when neither side reaches it alone, so arms A and C are expected to score near zero on exactly these claims. The test therefore confirms the Part A tags more than it separates one item from another, and with a margin of 0.25 it will pass for any item whose arm B answers competently. That is worth saying plainly before the 7-of-8 figure is quoted anywhere.

What the design did catch is the one failure, and it is the failure only arm C can see. `di_journal_of_a_spi_o13_o20_o22_n15` scores 0.500 on arm C — the earlier result alone reaches half its combined claims, identically across all 6 samples — so one of its two "combined" claims is not combined at all. Both Part A agents tagged it combined and both were wrong. Under v2.7's method, which only ever compared B against A, that item would have been called compositional on a B-A of +0.583. Arm C is the whole reason it is not.

Two caveats on the arms themselves. Arm B is the only arm asked the combined question; arms A and C get questions matching what they hold, which is necessary for them to be answerable but does mean arm B is asked the question the key was written to answer. The control that would settle it - arm B asked arm A's narrower question - was not run. And arm C has no panels at all, so it is short of evidence as well as short of a question, which flatters the B−C gap.

### Limits, as context only

Arm B keeps the key's limits better than arm A on 8 of 8 items. Mean limit score A 0.1292, B 0.5649, C 0.3101. This is reported because it is the thing v2.6 measured as "laundering", and it is not part of the compositional decision.

## Every item in full

### `di_acta_materia_com_o10_o14_o12_n13`

Acta Materialia · drafter label **discriminating** · upstream `acta_materia_com_o10_o14` (complementary)

| arm | mean combined | sd | mean limit | mean contradictions |
|---|---|---|---|---|
| A | 0.133 | 0.094 | 0.042 | 0.17 |
| B | 0.600 | 0.116 | 0.792 | 0.33 |
| C | 0.000 | 0.000 | 0.083 | 0.00 |

B−A +0.467 → input needed **True** · B−C +0.600 → observation needed **True** · compositional **True** · halves (True, True) agree **True**

Claims, as both agents tagged them:

- **input** — The straight, {10-12}/{01-12}-trace bands are the uniform-orientation (twin) population.
- **input** — The wavy-morphology bands are the continuously-shading, kink-band population.
- **observation** — The RT and 200 C specimens carry {01-12}/{10-12} twin traces.
- **observation** — Twin traces are replaced by {10-10}/{1-100} prismatic slip traces at 300-400 C.
- **observation** — Deformation bands persist at every temperature from RT to 400 C.
- **combined** — The {01-12}/{10-12} twin traces B finds at RT and 200 C are the same uniform-orientation population identified in A.
- **combined** — The deformation bands B finds persisting at every temperature are the wavy, continuously-shading kink-band population identified in A.
- **combined** — Kink banding operates as a deformation mechanism across the whole RT-400 C range even as twinning is replaced by prismatic slip at 300-400 C.
- **combined** — This temperature-dependence-of-mechanism statement cannot be made from B's trace record alone, since it never says what a deformation band is in orientation terms.
- **combined** — This temperature-dependence-of-mechanism statement cannot be made from A alone, since A carries no temperature information.
- *limit* — A's morphology-to-orientation pairing (straight/uniform vs wavy/continuously-shading) was established only via OM+EBSD taken at the orientations/conditions behind A ([11-20] and [01-10] specimens), with no EBSD record at 200, 300, or 400 C, so applying that pairing to the bands B tracks at elevated temperature is an extrapolation of the imaging signature, not a re-measurement of it.
- *limit* — A's link is only a qualitative colour/contrast correspondence (uniform vs continuously varying colour, strong vs faint side-surface contrast), not a measured misorientation magnitude, so the combination cannot say how much the kink-band orientation gradient changes (or stays the same) as temperature rises through the range B covers.
- *limit* — The pairing in A is a co-registration by band type, not a mechanistic proof of what produces the continuous shading, so carrying it into B's temperature series still only yields a correspondence in imaging signature (which bands persist) rather than a demonstrated cause for why kink banding, and not twinning, survives past 200 C.
- *limit* — B reports trace planes and band persistence at the macroscopic/OM level only; it does not itself contain an EBSD orientation map at 300-400 C, so nothing in the pair confirms that the persisting bands still show the graded (rather than uniform) internal orientation at those higher temperatures -- that identification rests entirely on carrying A's RT-established criterion forward.

### `di_advanced_ene_spi_o1_o12b_o20_n10`

Advanced Energy Materials · drafter label **discriminating** · upstream `advanced_ene_spi_o1_o12b` (spine_edge)

| arm | mean combined | sd | mean limit | mean contradictions |
|---|---|---|---|---|
| A | 0.333 | 0.471 | 0.125 | 0.00 |
| B | 0.833 | 0.373 | 0.292 | 0.00 |
| C | 0.000 | 0.000 | 0.833 | 0.67 |

B−A +0.500 → input needed **True** · B−C +0.833 → observation needed **True** · compositional **True** · halves (True, True) agree **True**

Claims, as both agents tagged them:

- **input** — Zn content rises to about 50 at% by the 20th cycle.
- **input** — Zn content settles near 47 at% after cycling.
- **input** — The as-prepared KMnHCF is confirmed as a single, well-matched monoclinic P21/n open framework.
- **observation** — With Zn added, Mn polyhedra convert from MnN3 to MnN4.
- **observation** — Grey ZnN4 tetrahedra link to the FeC6 octahedra.
- **combined** — The substantial, stable quantity of inserted Zn is accommodated at N-coordinated cation sites within the host lattice.
- *limit* — Observation A's phase confirmation is a single as-prepared (cycle 0) snapshot and its Zn trend is cycle-indexed to cycle 20, while observation B's structural description ('with Zn added') is not tied to a specific cycle number, so the pair cannot confirm that this site picture corresponds to the point where Zn reaches the ~47 at% plateau specifically
- *limit* — B is a local, site/coordination-level structural description while A's Zn content is a bulk elemental at% -- combining a bulk amount with a local structural feature supports plausibility of co-location, not a quantitative accounting of what fraction of the ~47 at% Zn occupies these sites versus elsewhere
- *limit* — the combination does not rule out that some portion of the inserted Zn also resides in other positions (e.g., surface phases or partial vacancy occupation) alongside the N-coordinated lattice sites described
- *limit* — no fractional-occupancy or site-resolved refinement quantifying how much Zn sits at these sites is given, so the structural description supports where Zn goes qualitatively but not how completely

### `di_journal_of_a_spi_o13_o20_o22_n15`

Journal of Advanced Ceramics · drafter label **discriminating** · upstream `journal_of_a_spi_o13_o20` (spine_edge)

| arm | mean combined | sd | mean limit | mean contradictions |
|---|---|---|---|---|
| A | 0.000 | 0.000 | 0.000 | 0.00 |
| B | 0.583 | 0.449 | 0.458 | 0.67 |
| C | 0.500 | 0.000 | 0.000 | 0.00 |

B−A +0.583 → input needed **True** · B−C +0.083 → observation needed **False** · compositional **False** · halves (False, False) agree **True**

Claims, as both agents tagged them:

- **input** — Beta-phase-mediated voltage enhancement is restricted to the low-loading window, 0-4 wt%.
- **input** — Over 0-4 wt%, beta content and voltage rise together.
- **input** — Beta content and voltage decouple over 6-10 wt%, with beta easing to ~81% while voltage climbs to 43.0 and 62.0 V.
- **observation** — Power peaks at 136.9 uW for the fiber film versus 21.025 uW for the cast film at 10 MOhm.
- **observation** — The fiber-over-cast power advantage is about 6.5x.
- **combined** — The 10 wt% loading falls within the decoupled regime already identified.
- **input** — Beta-phase enhancement was already established as inoperative as a driver at the 10 wt% loading.
- **combined** — The large fiber-over-cast power advantage at 10 wt% is unlikely to be explained by a beta-phase-content story.
- *limit* — Observation A's decoupling was established within one fiber-film series varying PZT wt%; Observation B compares two different sample morphologies (fiber vs cast film) at a fixed wt%, so extending A's regime conclusion to explain B's fiber/cast gap is an inference across a different comparison axis, not a direct test
- *limit* — Observation B reports no beta-phase (FTIR) measurement for either the fiber or the cast film samples used in the power comparison, so there is no beta-phase data to actually check against the 136.9 uW vs 21.025 uW gap
- *limit* — the two observations are different quantity kinds on both count and axis: A pairs a normalized structural fraction (% beta phase) against an absolute voltage (V) across a wt% series, while B is an absolute power output (uW) at a fixed 10 MOhm load compared across two morphologies -- neither the magnitude nor the mechanism of B's 6.5x gap can be read from A's %-vs-V trend
- *limit* — only one wt% point (10 wt%) is common between the two observations, insufficient to confirm that the fiber sample in B actually sits in the same beta-phase plateau region A describes

### `di_materials_ch_com_o1_o7_o3_r1`

Materials Characterization · drafter label **discriminating** · upstream `materials_ch_com_o1_o7` (complementary)

| arm | mean combined | sd | mean limit | mean contradictions |
|---|---|---|---|---|
| A | 0.000 | 0.000 | 0.000 | 0.00 |
| B | 1.000 | 0.000 | 0.444 | 0.67 |
| C | 0.000 | 0.000 | 0.056 | 0.00 |

B−A +1.000 → input needed **True** · B−C +1.000 → observation needed **True** · compositional **True** · halves (True, True) agree **True**

Claims, as both agents tagged them:

- **input** — The HP composites at 1 wt% and 5 wt% AlN are both essentially fully dense, reaching ~100% relative density.
- **input** — SEM fracture imaging shows no open pores and transgranular fracture facets at 1 and 5 wt% AlN.
- **input** — The near-100% relative density figure corresponds to an observably pore-free microstructure, not a measurement artifact.
- **observation** — HP hardness peaks at ~20.3 GPa at 1 wt% AlN.
- **observation** — HP hardness falls to ~19.2 GPa at 5 wt% AlN.
- **combined** — The hardness decline from 1 wt% to 5 wt% AlN cannot be explained by a difference in residual porosity between those two compositions.
- **combined** — Because both compositions are confirmed equally dense/pore-free, porosity variation cannot account for the observed hardness drop.
- **combined** — The two observations together rule out porosity/density variation as the cause of the hardness decline from 1 wt% to 5 wt% AlN.
- **combined** — Whatever drives the hardness decline from 1 to 5 wt% AlN must be something other than a loss of densification.
- *limit* — The pair only supports this porosity-is-not-the-cause conclusion for the 1 wt% vs 5 wt% comparison, since those are the two compositions the earlier result explicitly confirms as fully dense; it says nothing about whether the lower hardness at 0 wt% (where density is only ~97.5%, i.e. not confirmed pore-free) is or is not attributable to porosity
- *limit* — The SEM evidence behind the earlier result is a qualitative, single-fracture-surface inspection, not a quantitative wt%-resolved porosity measurement, so 'equally pore-free' is a qualitative judgment, not a measured equivalence, weakening how firmly porosity can be excluded as a contributor
- *limit* — Neither observation identifies what does cause the hardness peak at 1 wt% and subsequent decline at 3-5 wt% (e.g., grain size, AlN distribution, or grain-boundary effects); the combination only excludes one candidate explanation (density/porosity), it does not supply the actual mechanism

### `di_journal_of_m_spi_o15_o17_o16_m2`

Journal of Magnesium and Alloys · drafter label **conditional mechanism** · upstream `journal_of_m_spi_o15_o17` (spine_edge)

| arm | mean combined | sd | mean limit | mean contradictions |
|---|---|---|---|---|
| A | 0.042 | 0.093 | 0.200 | 0.00 |
| B | 0.917 | 0.118 | 0.533 | 1.17 |
| C | 0.208 | 0.093 | 0.800 | 0.17 |

B−A +0.875 → input needed **True** · B−C +0.708 → observation needed **True** · compositional **True** · halves (True, True) agree **True**

Claims, as both agents tagged them:

- **input** — Surface b shows shallower grooves with fine debris and no large craters, versus plain abrasive grooves on surface a.
- **observation** — Wear debris collected from surface a consists of flat flakes about 20-40 um.
- **observation** — Wear debris collected from surface b is mostly fine particles under 5 um with loose agglomerates.
- **combined** — FA presence shifts the wear-debris regime from coarse flake-type debris to fine particulate debris.
- **combined** — The debris-size data corroborates the groove-morphology result, strengthening the case beyond either observation alone.
- **combined** — A debris-mediated component, fine particles acting as a rolling three-body medium, accompanies the reduced/shallower cutting on surface b.
- **combined** — The debris-size evidence forms an independent line of evidence added to the surface-groove observation.
- *limit* — Neither observation analyzes debris composition, so it still cannot be confirmed that the fine b-debris (or the fine debris seen on surface b's grooves in the earlier result) originates from fractured FA layers rather than from matrix wear -- the debris-size data does not resolve this open point from the earlier result
- *limit* — The pairing shows fine debris is present and is smaller/more numerous as agglomerates on surface b, but does not establish that this debris causes the shallower grooves rather than merely co-occurring with them
- *limit* — The two proposed sub-mechanisms -- FA blocking asperity penetration (barrier effect) vs. fractured FA fine debris rolling as a three-body medium -- both remain consistent with 'shallower grooves + fine debris + fine wear particles'; the debris-size comparison does not discriminate between them
- *limit* — Both observations remain qualitative/descriptive (SEM images, debris size impressions) from what appears to be single-instance sampling, not quantified counts or statistics, so the combination does not upgrade the evidence to a measured, compared metric
- *limit* — The panels describe only two surfaces' debris and two surfaces' grooves; full exclusion of localized adhesive wear or alternative debris sources elsewhere on the worn surface is still not established

### `di_bioactive_ma_com_o11_o12_n18_o15_n20`

Bioactive Materials · drafter label **associative** · upstream `bioactive_ma_com_o11_o12_n18` (complementary)

| arm | mean combined | sd | mean limit | mean contradictions |
|---|---|---|---|---|
| A | 0.000 | 0.000 | 0.375 | 0.00 |
| B | 1.000 | 0.000 | 0.667 | 0.00 |
| C | 0.000 | 0.000 | 0.167 | 0.00 |

B−A +1.000 → input needed **True** · B−C +1.000 → observation needed **True** · compositional **True** · halves (True, True) agree **True**

Claims, as both agents tagged them:

- **input** — BVLD/NO-PPAmF has the fewest adhered platelets among the five surfaces.
- **input** — BVLD/NO-PPAmF morphology is the least spread/round of the five surfaces.
- **observation** — 316L SS and PPAmF shunt-tube lumens are filled with dark thrombus.
- **observation** — BVLD-PPAmF and NO-PPAmF shunt tubes are only partly open.
- **observation** — BVLD/NO-PPAmF lumen and foil are nearly clean.
- **input** — The platelet count/morphology result alone says nothing about whole-device thrombus outcome.
- **observation** — The photographs alone say nothing about platelet number or shape.
- **combined** — The five-surface ranking holds at two different levels, cellular and macroscopic.
- **combined** — The surface with most suppressed platelet adhesion/activation is also the surface with least macroscopic thrombus.
- **combined** — The cellular-level anti-platelet effect on BVLD/NO-PPAmF co-occurs with a macroscopic anti-thrombotic effect on the same surface.
- *limit* — The photographs are described only qualitatively (filled with dark thrombus / partly open / nearly clean); no thrombus mass, occlusion percentage, or flow-retention number is attached to Observation B itself, so the correspondence with the platelet counts is visual/descriptive, not a measured or tested relationship
- *limit* — No statistics or error bars back either observation (carried over from Observation A's own qualification), so the parallel ordering across the same five surfaces is descriptive, not statistically supported
- *limit* — The pair only shows platelet suppression and reduced macroscopic thrombus moving together across surfaces; it does not show that platelet suppression is what produces the reduced thrombus -- other blood components (coagulation factors, fibrin, other cells) could also be suppressed on BVLD/NO-PPAmF and contribute to the clean lumen, and this pairing cannot rule that out
- *limit* — The two sides are different kinds of quantity (a cellular density/morphology assay versus a whole-tube visual appearance), so their co-occurrence across surfaces is a correspondence of rankings, not a single measured mechanism linking them

### `di_advanced_fun_spi_o1_o4_o6_n10`

Advanced Functional Materials · drafter label **associative** · upstream `advanced_fun_spi_o1_o4` (spine_edge)

| arm | mean combined | sd | mean limit | mean contradictions |
|---|---|---|---|---|
| A | 0.024 | 0.053 | 0.000 | 0.33 |
| B | 0.595 | 0.053 | 0.792 | 0.17 |
| C | 0.024 | 0.053 | 0.375 | 0.17 |

B−A +0.571 → input needed **True** · B−C +0.571 → observation needed **True** · compositional **True** · halves (True, True) agree **True**

Claims, as both agents tagged them:

- **observation** — SC's peak width narrows from ~100% down to ~50% at 150 K.
- **observation** — PC-242 peak width shows a sharp transient rise to ~260% around 150-155 K.
- **observation** — HOC peak width shows a sharp transient rise to ~128% around 150-155 K.
- **input** — SC is the coarse-domain phase with smooth/near-linear peak-position shift.
- **input** — PC and HOC are the finer/less-uniform-domain phases already flagged for curved/offset peak-position shifts.
- **combined** — The phase whose peak width narrows (SC) is the same phase already established as coarse-domain and smooth-expansion.
- **combined** — The phases whose peak width shows a sharp transient rise (PC, HOC) are the same phases already flagged for curved/offset shifts.
- **combined** — Observation A and Observation B track different signatures of the lattice: average peak position versus peak breadth.
- **combined** — The two datasets, despite tracking different signatures, point to the same phase ordering.
- **combined** — Together the datasets support that a build-up of inhomogeneous residual strain occurs toward the transition.
- **combined** — Peak-position smoothness (Observation A) alone only implied the strain build-up indirectly.
- **combined** — Peak-width alone (Observation B) only showed this for three isolated phases without the domain-size framing.
- *limit* — The domain-size/phase confound already recorded on Observation A is not resolved by adding B: PC, HOC and SC still differ in composition/crystal structure as well as domain size, so whether domain size or phase identity drives the strain-inhomogeneity magnitude remains unsettled
- *limit* — Still only three phase categories (SC, PC, HOC) are compared, so the correspondence is an ordering across three points, not a dose-response between domain size and peak-width magnitude
- *limit* — Peak width (B) and peak-position shift (A) are different kinds of lattice signatures -- breadth/dispersion of the reflection versus its mean shift with temperature -- so their agreement in direction is a cross-signature corroboration, not a repeated measurement of the same quantity
- *limit* — The percentages themselves (260%, 128%, 50%) do not scale in proportion to the domain-size figures given in A, so no quantitative (only ordinal) relationship between domain scale and strain-inhomogeneity size is supported

### `di_journal_of_m_spi_o14_o10_o11_f2`

Journal of Materials Science & Technology · drafter label **conditional mechanism** · upstream `journal_of_m_spi_o14_o10` (spine_edge)

| arm | mean combined | sd | mean limit | mean contradictions |
|---|---|---|---|---|
| A | 0.000 | 0.000 | 0.292 | 0.00 |
| B | 0.667 | 0.333 | 0.542 | 0.00 |
| C | 0.000 | 0.000 | 0.167 | 0.00 |

B−A +0.667 → input needed **True** · B−C +0.667 → observation needed **True** · compositional **True** · halves (True, True) agree **True**

Claims, as both agents tagged them:

- **input** — Across the four common samples, higher steady photocurrent ranks in the same order as H2 evolution rate.
- **input** — Ag0.25Pd0.75-ZIS tops both the photocurrent ranking and the H2 evolution ranking.
- **input** — Steady photocurrent is taken as an indicator of charge-carrier separation.
- **observation** — The apparent quantum yield (AQY) falls with wavelength, from 18.3% at 400 nm to 0.19% at 550 nm.
- **observation** — The AQY's wavelength dependence tracks the absorption edge.
- **observation** — AQY tracking the absorption edge shows the H2-evolution figure of merit is a genuinely light-driven, photocatalytic process.
- **combined** — This light-driven, absorption-tracking process occurs in the same composition series where photocurrent tracks H2 performance.
- **combined** — Light harvesting (absorption-matched AQY) and charge separation (photocurrent ranking) are consistent, non-contradicting pieces of the mechanistic picture.
- **combined** — This consistency between light harvesting and charge separation underlies the activity of the top-performing composition.
- *limit* — Photocurrent (current density) and H2 evolution rate (molar rate) are different kinds of quantity whose matching rank order (Observation A) is not a quantitative or unit-comparable relationship, and AQY (a normalized %, photon-to-H2 efficiency by wavelength) is yet a third kind of quantity not directly comparable in magnitude to either.
- *limit* — Observation B's AQY spectrum concerns wavelength dependence for the reaction, not a composition series; it does not report AQY across the Ag:Pd compositions, so it cannot confirm that AQY itself follows the same Ag0.25Pd0.75-ZIS > Pd-ZIS > Ag-ZIS > ZIS ordering seen for photocurrent and H2 rate in Observation A.
- *limit* — Only four points overlap in Observation A (too few for a dose-response curve or an effect size), and Observation A already cannot rule out that Ag:Pd composition drives photocurrent and H2 evolution independently rather than photocurrent causing the H2 evolution difference; adding B's absorption-tracking result does not resolve this confound.
- *limit* — Observation B shows AQY tracks the absorption edge, which is consistent with light absorption governing the reaction, but this alone does not establish how much of the composition-dependent performance advantage is attributable to absorption versus to charge separation.

## One answer from each arm, for every compositional item

### `di_acta_materia_com_o10_o14_o12_n13`

**arm A** — combined 0.00, limits 0.00, 0 contradiction(s)

- `absent` The {01-12}/{10-12} twin traces B finds at RT and 200 C are the same uniform-orientation population identified in A.
- `absent` The deformation bands B finds persisting at every temperature are the wavy, continuously-shading kink-band population identified in A.
- `absent` Kink banding operates as a deformation mechanism across the whole RT-400 C range even as twinning is replaced by prismatic slip at 300-400 C.
- `absent` This temperature-dependence-of-mechanism statement cannot be made from B's trace record alone, since it never says what a deformation band is in orientation terms.
- `absent` This temperature-dependence-of-mechanism statement cannot be made from A alone, since A carries no temperature information.

**arm B** — combined 0.40, limits 1.00, 2 contradiction(s)

- `stated` The {01-12}/{10-12} twin traces B finds at RT and 200 C are the same uniform-orientation population identified in A.
  > "Read against the earlier OM+EBSD result (which showed, for these same two orientations, that the straight {10-12}/{01-12}-trace bands are twin-like with uniform EBSD colour...)"
- `contradicted` The deformation bands B finds persisting at every temperature are the wavy, continuously-shading kink-band population identified in A.
  > "this figure is macroscopic OM only, with no EBSD at 300-400°C, so it cannot confirm that the "deformation band" labelled at high temperature still shows the same wavy morphology, strong/faint (0001)-side contrast asymmetry, or continuously-shading EBSD colour that defined the band class at RT — it i"
- `contradicted` Kink banding operates as a deformation mechanism across the whole RT-400 C range even as twinning is replaced by prismatic slip at 300-400 C.
  > "it is only labelled by the same name, not re-verified by the same two-technique signature... no misorientation magnitude or mechanistic cause is established at any temperature."
- `stated` This temperature-dependence-of-mechanism statement cannot be made from B's trace record alone, since it never says what a deformation band is in orientation terms.
  > "this figure is macroscopic OM only, with no EBSD at 300-400°C, so it cannot confirm that the "deformation band" labelled at high temperature still shows the same wavy morphology, strong/faint (0001)-side contrast asymmetry, or continuously-shading EBSD colour that defined the band class at RT"
- `absent` This temperature-dependence-of-mechanism statement cannot be made from A alone, since A carries no temperature information.

**arm C** — combined 0.00, limits 0.50, 0 contradiction(s)

- `absent` The {01-12}/{10-12} twin traces B finds at RT and 200 C are the same uniform-orientation population identified in A.
- `absent` The deformation bands B finds persisting at every temperature are the wavy, continuously-shading kink-band population identified in A.
- `absent` Kink banding operates as a deformation mechanism across the whole RT-400 C range even as twinning is replaced by prismatic slip at 300-400 C.
- `absent` This temperature-dependence-of-mechanism statement cannot be made from B's trace record alone, since it never says what a deformation band is in orientation terms.
- `absent` This temperature-dependence-of-mechanism statement cannot be made from A alone, since A carries no temperature information.

### `di_advanced_ene_spi_o1_o12b_o20_n10`

**arm A** — combined 0.00, limits 0.00, 0 contradiction(s)

- `absent` The substantial, stable quantity of inserted Zn is accommodated at N-coordinated cation sites within the host lattice.

**arm B** — combined 0.00, limits 0.25, 0 contradiction(s)

- `absent` The substantial, stable quantity of inserted Zn is accommodated at N-coordinated cation sites within the host lattice.

**arm C** — combined 0.00, limits 1.00, 1 contradiction(s)

- `contradicted` The substantial, stable quantity of inserted Zn is accommodated at N-coordinated cation sites within the host lattice.
  > "nothing in the evidence ties them together mechanistically ... these two ... measurements ... can only support co-occurrence in the same material, not that the framework hosts or accommodates the Zn"

### `di_materials_ch_com_o1_o7_o3_r1`

**arm A** — combined 0.00, limits 0.00, 0 contradiction(s)

- `absent` The hardness decline from 1 wt% to 5 wt% AlN cannot be explained by a difference in residual porosity between those two compositions.
- `absent` Because both compositions are confirmed equally dense/pore-free, porosity variation cannot account for the observed hardness drop.
- `absent` The two observations together rule out porosity/density variation as the cause of the hardness decline from 1 wt% to 5 wt% AlN.
- `absent` Whatever drives the hardness decline from 1 to 5 wt% AlN must be something other than a loss of densification.

**arm B** — combined 1.00, limits 0.33, 1 contradiction(s)

- `stated` The hardness decline from 1 wt% to 5 wt% AlN cannot be explained by a difference in residual porosity between those two compositions.
  > "full densification alone cannot explain the hardness plateau/decline from 1 to 5 wt%, since 5 wt% is just as dense and just as pore-free as 1 wt% yet measurably softer"
- `stated` Because both compositions are confirmed equally dense/pore-free, porosity variation cannot account for the observed hardness drop.
  > "since 5 wt% is just as dense and just as pore-free as 1 wt% yet measurably softer"
- `stated` The two observations together rule out porosity/density variation as the cause of the hardness decline from 1 wt% to 5 wt% AlN.
  > "the combination therefore establishes that density/porosity is not the controlling variable for HP hardness differences among the fully-dense compositions (1, 3, 5 wt%)"
- `stated` Whatever drives the hardness decline from 1 to 5 wt% AlN must be something other than a loss of densification.
  > "it also shows that full densification alone cannot explain the hardness plateau/decline from 1 to 5 wt%"

**arm C** — combined 0.00, limits 0.00, 0 contradiction(s)

- `absent` The hardness decline from 1 wt% to 5 wt% AlN cannot be explained by a difference in residual porosity between those two compositions.
- `absent` Because both compositions are confirmed equally dense/pore-free, porosity variation cannot account for the observed hardness drop.
- `absent` The two observations together rule out porosity/density variation as the cause of the hardness decline from 1 wt% to 5 wt% AlN.
- `absent` Whatever drives the hardness decline from 1 to 5 wt% AlN must be something other than a loss of densification.

### `di_journal_of_m_spi_o15_o17_o16_m2`

**arm A** — combined 0.00, limits 0.40, 0 contradiction(s)

- `absent` FA presence shifts the wear-debris regime from coarse flake-type debris to fine particulate debris.
- `absent` The debris-size data corroborates the groove-morphology result, strengthening the case beyond either observation alone.
- `absent` A debris-mediated component, fine particles acting as a rolling three-body medium, accompanies the reduced/shallower cutting on surface b.
- `absent` The debris-size evidence forms an independent line of evidence added to the surface-groove observation.

**arm B** — combined 1.00, limits 0.40, 2 contradiction(s)

- `stated` FA presence shifts the wear-debris regime from coarse flake-type debris to fine particulate debris.
  > "Panel b (FSP) shows a field of much finer particles, mostly well under 5 µm... the FA-bearing (FSP) surface wears by a milder, fine-particulate abrasive mode rather than coarse flake delamination"
- `stated` The debris-size data corroborates the groove-morphology result, strengthening the case beyond either observation alone.
  > "this debris-size measurement corroborates and sharpens that earlier qualitative impression... This strengthens the case"
- `stated` A debris-mediated component, fine particles acting as a rolling three-body medium, accompanies the reduced/shallower cutting on surface b.
  > "the fine, loosely agglomerated particle morphology specifically favors the "fine debris rolling as three-body abrasive" sub-mechanism over the "FA blocking asperity penetration" sub-mechanism"
- `stated` The debris-size evidence forms an independent line of evidence added to the surface-groove observation.
  > "this debris-size measurement corroborates and sharpens that earlier qualitative impression: it is not just that surface b "looks" covered in finer material, the debris particles themselves are measurably an order of magnitude smaller"

**arm C** — combined 0.25, limits 0.80, 0 contradiction(s)

- `absent` FA presence shifts the wear-debris regime from coarse flake-type debris to fine particulate debris.
- `absent` The debris-size data corroborates the groove-morphology result, strengthening the case beyond either observation alone.
- `stated` A debris-mediated component, fine particles acting as a rolling three-body medium, accompanies the reduced/shallower cutting on surface b.
  > "the FA-containing surface shows shallower grooves with fine debris and still no large craters, which is consistent with a mechanism-of-change (MEC) in which dispersed FA moderates the severity of abrasive cutting -- either by blocking asperity penetration or by generating fine debris that rolls as a"
- `absent` The debris-size evidence forms an independent line of evidence added to the surface-groove observation.

### `di_bioactive_ma_com_o11_o12_n18_o15_n20`

**arm A** — combined 0.00, limits 0.50, 0 contradiction(s)

- `absent` The five-surface ranking holds at two different levels, cellular and macroscopic.
- `absent` The surface with most suppressed platelet adhesion/activation is also the surface with least macroscopic thrombus.
- `absent` The cellular-level anti-platelet effect on BVLD/NO-PPAmF co-occurs with a macroscopic anti-thrombotic effect on the same surface.

**arm B** — combined 1.00, limits 0.50, 0 contradiction(s)

- `stated` The five-surface ranking holds at two different levels, cellular and macroscopic.
  > "show the same five-surface ordering already seen at the cellular level"
- `stated` The surface with most suppressed platelet adhesion/activation is also the surface with least macroscopic thrombus.
  > "BVLD/NO-PPAmF uniquely combines the lowest platelet count with the least-spread, least-activated platelet morphology ... BVLD/NO-PPAmF has a nearly clean lumen and foil (least clot)"
- `stated` The cellular-level anti-platelet effect on BVLD/NO-PPAmF co-occurs with a macroscopic anti-thrombotic effect on the same surface.
  > "the platelet-level suppression (fewer, rounder, less-activated platelets) on BVLD/NO-PPAmF is accompanied by a macroscopic, whole-vessel reduction in gross thrombus formation after 2 h of blood circulation"

**arm C** — combined 0.00, limits 0.25, 0 contradiction(s)

- `absent` The five-surface ranking holds at two different levels, cellular and macroscopic.
- `absent` The surface with most suppressed platelet adhesion/activation is also the surface with least macroscopic thrombus.
- `absent` The cellular-level anti-platelet effect on BVLD/NO-PPAmF co-occurs with a macroscopic anti-thrombotic effect on the same surface.

### `di_advanced_fun_spi_o1_o4_o6_n10`

**arm A** — combined 0.00, limits 0.00, 0 contradiction(s)

- `absent` The phase whose peak width narrows (SC) is the same phase already established as coarse-domain and smooth-expansion.
- `absent` The phases whose peak width shows a sharp transient rise (PC, HOC) are the same phases already flagged for curved/offset shifts.
- `absent` Observation A and Observation B track different signatures of the lattice: average peak position versus peak breadth.
- `absent` The two datasets, despite tracking different signatures, point to the same phase ordering.
- `absent` Together the datasets support that a build-up of inhomogeneous residual strain occurs toward the transition.
- `absent` Peak-position smoothness (Observation A) alone only implied the strain build-up indirectly.
- `absent` Peak-width alone (Observation B) only showed this for three isolated phases without the domain-size framing.

**arm B** — combined 0.57, limits 0.75, 0 contradiction(s)

- `stated` The phase whose peak width narrows (SC) is the same phase already established as coarse-domain and smooth-expansion.
  > "the coarse, smooth-expanding SC domains actually sharpen"
- `stated` The phases whose peak width shows a sharp transient rise (PC, HOC) are the same phases already flagged for curved/offset shifts.
  > "matching the domain-size ordering already established ... and matching which phases showed curved/offset vs. smooth peak-position shifts"
- `stated` Observation A and Observation B track different signatures of the lattice: average peak position versus peak breadth.
  > "the same ~150 K event drives both the lattice-expansion curvature and a coincident, magnitude-graded change in peak width"
- `stated` The two datasets, despite tracking different signatures, point to the same phase ordering.
  > "two independent XRD observables (peak position and peak width) converge on the same temperature and the same three-phase ordering"
- `absent` Together the datasets support that a build-up of inhomogeneous residual strain occurs toward the transition.
- `absent` Peak-position smoothness (Observation A) alone only implied the strain build-up indirectly.
- `absent` Peak-width alone (Observation B) only showed this for three isolated phases without the domain-size framing.

**arm C** — combined 0.00, limits 0.50, 0 contradiction(s)

- `absent` The phase whose peak width narrows (SC) is the same phase already established as coarse-domain and smooth-expansion.
- `absent` The phases whose peak width shows a sharp transient rise (PC, HOC) are the same phases already flagged for curved/offset shifts.
- `absent` Observation A and Observation B track different signatures of the lattice: average peak position versus peak breadth.
- `absent` The two datasets, despite tracking different signatures, point to the same phase ordering.
- `absent` Together the datasets support that a build-up of inhomogeneous residual strain occurs toward the transition.
- `absent` Peak-position smoothness (Observation A) alone only implied the strain build-up indirectly.
- `absent` Peak-width alone (Observation B) only showed this for three isolated phases without the domain-size framing.

### `di_journal_of_m_spi_o14_o10_o11_f2`

**arm A** — combined 0.00, limits 0.25, 0 contradiction(s)

- `absent` This light-driven, absorption-tracking process occurs in the same composition series where photocurrent tracks H2 performance.
- `absent` Light harvesting (absorption-matched AQY) and charge separation (photocurrent ranking) are consistent, non-contradicting pieces of the mechanistic picture.
- `absent` This consistency between light harvesting and charge separation underlies the activity of the top-performing composition.

**arm B** — combined 0.33, limits 0.50, 0 contradiction(s)

- `stated` This light-driven, absorption-tracking process occurs in the same composition series where photocurrent tracks H2 performance.
  > "confirming that the high activity of Ag0.25Pd0.75-ZIS is genuinely a light-absorption-driven photocatalytic process rather than a wavelength-independent or dark artifact"
- `absent` Light harvesting (absorption-matched AQY) and charge separation (photocurrent ranking) are consistent, non-contradicting pieces of the mechanistic picture.
- `absent` This consistency between light harvesting and charge separation underlies the activity of the top-performing composition.

**arm C** — combined 0.00, limits 0.25, 0 contradiction(s)

- `absent` This light-driven, absorption-tracking process occurs in the same composition series where photocurrent tracks H2 performance.
- `absent` Light harvesting (absorption-matched AQY) and charge separation (photocurrent ranking) are consistent, non-contradicting pieces of the mechanistic picture.
- `absent` This consistency between light harvesting and charge separation underlies the activity of the top-performing composition.

## The audit pack

8 pages in `results/v2p8/audit/`, one per item plus an index. Each carries the earlier result, the measurement with its panels, the claim list with tags, the arm means, and one answer per arm with the grader's ruling and quote on every claim. Every tag and every ruling has an empty agree/disagree box. **None is filled in.**

On the brief's conflict: Part E commissions these pages, the stop rules say not to build pages in the pilot. I read the stop rule as covering the per-paper trace pages v2.6 step 7 would produce — pipeline output presenting results as settled — and not an audit pack whose purpose is to let a person contradict the machine. The pack is built; no trace pages are.

## Cost

Estimated before starting: **304 calls** (16 for Part A, 144 answers, 144 gradings).

| stage | model calls | relays | wall minutes | seconds per call |
|---|---|---|---|---|
| partA_split | 16 | 2 | 6.8 | 25.64 |
| partB_answers | 144 | 4 | 8.6 | 3.58 |
| partC_gradings | 144 | 4 | 12.7 | 5.29 |

**Actual: 304 calls, 28.1 minutes** at the 20-agent cap, dispatch to last harvest. Every reply verified byte for byte against its prompt file from the agent's own transcript.

## Where the data is

- `results/v2p8/selected.json` — the 8 items and why each was picked
- `results/v2p8/split/`, `check/` — Part A, the tags and the second agent's rulings
- `results/v2p8/partA.json` — kept and dropped claims
- `results/v2p8/arms/` — Part B, 3 arms x 6 samples x 8 items
- `results/v2p8/grade/`, `partC.json` — Part C, every ruling with its quote
- `results/v2p8/partD.json` — arm means, decisions, split halves
- `results/v2p8/audit/` — the audit pack

Every verdict is model against model.
