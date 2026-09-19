# Showcase cases: senior investigator review

Scope: three showcase graphs, reviewed against vocab/v04.json, PROTOCOL.md and rounds/r04/judge.md. For each paper I opened at least five figures, choosing those behind spine claims and behind every contradicts/partial/not_shown verdict. After the fixes all three graphs validate against v04: every type, rel, mm_op and modality exists, every endpoint exists, every OBS node with a figure has an mm_op on its out-edges, and each spine is one connected path from HYP to DSC/conclusion. Every node below is referenced by its id in the case JSON. Each case also has a `review` field.

| case | spine | nodes / edges | verdict | changes | audits confirmed / reframed / overturned |
|---|---|---|---|---|---|
| JMA ZK60 + nano-diamond | 17 | 47 / 62 | approved with changes | 3 | 4 / 0 / 1 |
| AEM Ni-Co hydroxide nanocages | 16 | 45 / 54 | approved with changes | 4 | 3 / 1 / 0 |
| Bioactive HAP/PLLA/PGA scaffold | 19 | 49 / 63 | approved with changes | 4 | 3 / 1 / 0 |

## 1. Journal of Magnesium and Alloys, j.jma.2021.03.034

**Figures opened:** F3, F4, F5, F7, F8, F9, F10.

**Verdict: approved with changes.** The spine follows the paper's argument. It runs from need to hypothesis, ZK60 + ND, the ND sweep, powder metallurgy and extrusion, grain refinement, MgZn2/ND dispersion and the ND/Mg interface. From there it splits into two branches:
- a mechanical branch, through attributed Hall-Petch/Orowan strengthening to a yield peak;
- a thermal branch, through argued interface constraint to a 72% CTE drop and dimensional stability.

The two branches meet at the 0.05 wt% design guidance and then the conclusion. The three mechanism nodes are all labelled `attributed` or `argued`, which is right because none of them is measured.

**Changes**
1. **Overturned audit o7c.** F7c shows the ~8 nm interlayer between MgZn2 and alpha-Mg fringes, in the region boxed on F7b. The paper text says the same thing. The claim that the interlayer sits at ND/alpha-Mg appears only in the MatMech summary, so this is a figure-vs-summary error, not a figure-vs-paper conflict (ruling #37). I removed `o7c -qualifies-> c18` and `text_silent`, rewrote the notes for o7c, c18 and the case, and left o7c as evidence for s_int2.
2. **o28:** changed provenance from measured to derived, and added `o9cd -derives-> o28` (convert_to_quantity, via = known_relation). I softened the image_note: the figure agrees with the text's numbers, and the alloy/composite offset is possible but untested.
3. **o8b:** added to the image_note that the 0.15 wt% compression curve has a yield-point drop. Its lead over 0.1 wt% therefore holds whether yield is read at the peak or at 0.2% offset.

**Key multimodal steps**
- **Registration (F6):** the HAADF bright particle, the Zn/Mg EDX maps and the line scan are overlaid to identify the particle as MgZn2. This agrees with the XRD assignment, but F3 marks MgZn2 only on the 0.2 wt% trace.
- **Series correlation (F4f × F8a → o24):** grain size and yield do not move together. At 0.05 wt% yield rises while grain size is unchanged, and 0.2 wt% has the finest grains but is weaker. This qualifies the attributed Hall-Petch lead term.
- **Quantity conversion plus a figure-vs-text check (F9, F10):** strain divided by 273 K reproduces the stated CTEs. However, the cycle-5 residual strain is highest at 0.1 wt%, which goes against the text's claim that stability improves with ND content.

**Audits**
- **Confirmed:**
  - o8b: the figure contradicts the text. Compression yield peaks at 0.15 wt%, not 0.1 wt%.
  - o_res: the figure contradicts the text. Residual strain is not monotone in ND content.
  - o24: a figure-derived series undercuts an attributed mechanism.
  - o28: the figure agrees with the text's numbers, but a 72% step at ~0.03 vol% followed by a plateau does not fit the argued "more interface, lower CTE" scaling.
- **Overturned:** o7c (see change 1).

## 2. Advanced Energy Materials, aenm.201401880

**Figures opened:** F2, F3, F4, F5.

**Verdict: approved with changes.** The spine is clean. It runs from the gap (why activity varies with the metal ratio) to the hypothesis, then the ADH family, the Co sweep and the cage architecture, then the etching and co-precipitation step, then shape, amorphous state and composition. Composition leads to computed O* binding and on to the activity volcano. The spine then reaches eta10 = 0.35 V qualification and 10 h / 4e- stability, and ends at the conclusion. The architecture gain (m2) is correctly kept off the spine as attributed, because its evidence is in the SI.

I checked these figure readings myself and they hold:
- the F3c Tafel lines give ~230 mV/dec for Ni(OH)2, against the 182 plotted in F3b;
- the RRDE ring current in F3e is about −140 µA;
- F3f gives a peroxide share of ~2%.

**Changes**
1. **o15** relabelled as a non-resolution audit. F3a cannot resolve a sub-mA onset at 1.48 V on its 0–20 mA cm⁻² axis. The figure leaves the claim unresolved; it does not contradict it.
2. **m1:** changed `basis` from evidenced to argued. F5 itself labels the reactivity→activity link "deduction", and the only support is a rank match over four compositions.
3. **o23:** changed provenance from computed to derived, and added derives edges from o11 (measured) and o22 (DFT).
4. Added modality on the non-OBS nodes that carry figures: p1 and m1 are schematic, k2 is simulation_render.

**Key multimodal steps**
- **Measured vs computed series correlation (F3b × F4b → m1):** the measured activity volcano and the DFT O* binding curve share their rank order and peak near 67–73% Co. This is the paper's only bridge from reactivity to activity.
- **Current-to-charge-balance conversion (F3e, F3f):** Faradaic efficiency is I_ring/(I_disk·N) ≈ 0.97–0.99. Together with the ~2% peroxide read from the co-plotted ring current, this closes the 4e- claim.
- **Registration plus spectrum-vs-formula check (F2c–e):** the EDS line scan is registered on one cage and shows Co and Ni rising at both walls, consistent with a hollow shell. The EDS spectrum also shows Cu and S, which the formula NiCo2.7(OH)x omits.

**Audits**
- **Confirmed:**
  - o2: the figure contradicts the text. F2b shows debris, against "exclusively nanocages".
  - o8: the source of the Cu/S peaks is not resolved. The Cu could come from the TEM grid or from template residue.
  - o23: the volcano match rests on only four shared compositions.
- **Reframed:** o15, from "contradicts" to "does not resolve".
- **Overturned:** none.

## 3. Bioactive Materials, j.bioactmat.2020.09.001

**Figures opened:** F2, F5, F6, F7, F9.

**Verdict: approved with changes.** The spine is 19 nodes, just within the limit. It runs from the PGA-blending hypothesis to the blended phases, then hydrophilicity, hydrolysis and HAP exposure, then apatite formation. That branch meets the strength-loss branch at the trade-off. The spine then goes through the 3# down-select to cytocompatibility, in-vivo repair and the conclusion.

**Changes**
1. **s1** relabelled. F2a shows the HAP reflection only in 1#. HAP retention in 2#–5# rests on the FTIR PO4/OH bands and the TGA residue, so "crystalline HAP" was not shown.
2. **o11** label corrected to the F5d values: 2# starts at pH ~5.7, which is outside the 3.2–4.5 range the label gave. I also narrowed the note to the PBS medium. The pH of the SBF and of the cell media is not reported, so this audit is a plausibility audit, not a measured contradiction.
3. **o22** relabelled from "no evident difference" to "cannot be ranked": the columns carry no group labels and there are no per-group quantities.
4. **o13 → s3** (register_colocated_views): added a note that the registration cannot be verified, because the EDS analysed area is not marked (see a2).

**Key multimodal steps**
- **Three modalities converging on one claim (F2a–c → s1):** FTIR carries HAP retention where XRD loses the peak, and DSC shows PLLA and PGA melting separately.
- **Series correlation (F5a × F5c → b13):** water uptake and weight loss rise together across the five blends. This is the only support for the hydrophilicity → hydrolysis pathway.
- **Cross-figure scale comparison (F6f vs F1a → a1):** the "exposed HAP" particles are 2–4 µm rods, more than 10× the size of the raw HAP needles. The degradation-exposes-HAP step therefore cannot be read as bare filler.

**Audits**
- **Confirmed:**
  - a1: the identity of the exposed particles is not resolved.
  - a2: the Au M line overlaps P K, and the EDS area is not marked, so the Ca/P ratio does not establish apatite.
  - o11: the degradation medium is acidic (scope narrowed to PBS).
- **Reframed:** o22, from "contradicts" to "does not resolve".
- **Overturned:** none.

## What these three decompositions show about multimodal reasoning in a materials paper

Three papers from three fields (a Mg composite, an electrocatalyst and a bone scaffold) use the same small set of figure acts, and the spine depends on them more than the text admits.

1. **Several modalities converge on one claim.** Examples are XRD + FTIR + DSC for phase content, and XRD + SAED + EDX for MgZn2. The reader has to know which modality is actually carrying the claim, because it is often not the one the text cites: FTIR, not XRD, shows that HAP survives.
2. **Co-located views are registered.** The reader overlays an EDX map or line scan on the image it was taken from. This act fails silently when the analysed area is not marked (Bioactive F7) or when the maps do not overlay (Bioactive F1b).
3. **Two series are correlated across the same design variable.** Examples are grain size against yield, water uptake against weight loss, and measured activity against DFT binding. This is how every mechanism in these papers is argued, and in all three papers it is the weakest link: a rank match over 4–5 points, with no test that separates the proposed cause from the alternatives.
4. **Figures are checked against the text.** Each paper has at least one headline number or ranking that the figure contradicts or does not resolve:
   - JMA: the compression peak, and the monotone stability claim;
   - AEM: the onset overpotential;
   - Bioactive: "more bone than controls".

   In this review the distinction between "contradicts" and "does not resolve" mattered more than any type label: two of the audits reclassified here had overstated a non-resolution as a contradiction. A third audit was really a conflict with the MatMech summary, not with the paper.

For the project lead: a text-only extractor would reproduce these papers' spines almost unchanged. The figures are what show where the spine is weak. That is roughly 3–5 audit points per paper, and it takes the four acts above to find them.
