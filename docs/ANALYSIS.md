# Can MatMech carry an FM-advantage benchmark? Domain, corpus and seed workflows

**Date:** 2026-09-18.

**Inputs:**
- MatMech (Liu et al., *Sci. Data* 13:269, 2026; figshare 10.6084/m9.figshare.29815979 v5, MD5-verified, 61,766 records).
- The `fm-advantage-benchmark` skill, rev 2.
- BioReason (see [bioreason_kegg.md](bioreason_kegg.md)).
- The earlier materials run of the skill, [colpark/19C_materials](https://github.com/colpark/19C_materials).

**Where the numbers come from:** every number here comes from `results/corpus_stats.json` (`scripts/corpus_stats.py`) or `results/text_floor.json` (`scripts/text_floor.py`) unless a section says otherwise. Both run with zero model calls.

---

## 0. The answer in brief

1. **MatMech plays the role KEGG plays for BioReason:** a curated causal graph with typed evidence. It is richer than KEGG in one way. Each edge carries a reasoning chain whose steps are labelled with their evidence type, taken from the authors' own argument rather than written after the fact.
2. **The label is the same kind of object, and the same trap applies.**
   - The answer (a mechanism or an effect) is written in the text of a paper that every current LLM has read. **98% of papers are from 2021 or earlier; only 76 are from 2025** (§2).
   - A text lookup with no model already solves the obvious task. It picks the true mechanism among 5 random rivals **98.5%** of the time (95% CI 98.1–98.9, n=3000, one item per paper).
   - That is the BioReason-KEGG pattern (97% from a lookup, §1). The skill would close it at P2/I2 before any agent runs.
3. **Measurement grounding is where the FM advantage can live, and MatMech alone does not contain it.** It holds 425,295 figure *images* and 94,047 mechanisms whose experiment result states a number with a unit. It holds no raw spectra, patterns or structures. Grounding therefore means one or both of:
   - reading measurements back out of figures;
   - joining the material to external measured or computed data.

   Either way, the FM acts as a scorer, generator or simulator on an input the agent constructs. The tasks worth building sit there.
4. **The candidates, and what to build first:**
   - (C1) mechanism discrimination by evidence acquisition, in a replayable in-paper environment;
   - (C2) diagnosing contradictions between papers;
   - (C3) structure consistency from diffraction and microscopy, with a forward-model grader;
   - (C5) a KEGG-style normalised MST graph with a temporal holdout.

   C4, effect prediction (the direct BioReason analogue), is kept only as the SFT warm-up and a negative control. Section 5 gives each candidate's workflow with FMs in the loop, and section 6 gives the SFT/RL recipe.

---

## 1. What we learned from BioReason on KEGG

Details are in [bioreason_kegg.md](bioreason_kegg.md). The pattern is the thing to copy, and the defects are the things to avoid.

| | BioReason on KEGG |
|---|---|
| Graph | KEGG Network Variants. Symbolic pathway strings with curated gene IDs (298 networks) |
| Measurement modality | Ref/alt DNA windows (±2 kb) → frozen DNA FM (Evo2 / NT) → linear projection → Qwen3 |
| Label | 1 of 37 diseases |
| Trace | Claude 3.7 Sonnet rationale written **given the label**; never verified or graded |
| Training | SFT (LoRA), then GRPO with a substring-match reward |
| Skill reading | The infer root sits on the predictor line with no lift. A text lookup takes 97% of the ceiling. 289 of 290 eval questions duplicate a train question. There is no text-kept, DNA-removed ablation. **I2 would close the DNA channel.** |

The reusable recipe is: a curated causal graph, plus a raw-measurement modality read by a domain FM, plus a verifiable reward.

The lesson is to measure the text-only floor and the FM channel's lift **before** building anything.

## 2. MatMech, counted

| Axis | Count |
|---|---|
| Papers / mechanisms / images | 61,766 / 207,200 / 425,295 (all three match the paper) |
| Journals | 15. The largest are Adv. Mater. (15.0k), Nano Lett. (14.9k), AFM (12.8k) and Acta Mater. (12.3k) |
| Link types | P→S 67,246; S→Pr 57,607; Pr→Pf 40,985; S→Pf 22,264; P→Pf 11,698; P→Pr 6,562; ~150 free-form variants with ≤218 each |
| Reasoning-step types, share of mechanisms carrying each | experimental result 96%, non-referenced knowledge 94%, deductive 88%, image description 82%, referenced knowledge 65%, inductive 15% |
| Claimed evidence depth (distinct non-inference step types) | 0–1: 1,335; 2: 23,307; 3: 79,310; 4: 103,140; 5: 108 |
| Mechanism confidence (HHEM + LLM) | ≥0.8: 165,131 (80%); 0.5–0.8: 27,605; <0.5 (flagged hallucination): 14,464 |
| Mechanisms with a figure / a microscopy figure | 197,701 / 74,598 |
| Figure function | characterizing structure 202k; property 74k; performance 33k; processing influence 43k |
| Figure captions mentioning, in figures | TEM 47.0k; SEM 38.6k; **XRD 19.7k**; UV-vis/PL 16.8k; CV/EIS 9.4k; Raman 7.1k; XPS 6.7k; stress–strain 5.0k; EBSD 3.0k; **XAS 1.4k** |
| Experiment type, in mechanisms | TEM 17.7k; SEM 14.1k; XRD 12.2k; electrochemistry 11.6k; tensile 6.2k; UV-vis 5.2k; DFT 4.0k; Raman 3.4k; XPS 3.1k; XAS 0.7k |
| Experiment result stating a number with a unit | 94,047 mechanisms (45%) |
| Cross-paper conflict flag (a found rival claim) | 7,145 mechanisms (3.4%) |
| Material object that is a bare formula (can be joined to MP/OQMD) | 6,829 papers (11%). The element list is present for every paper, which allows a looser chemical-system join |
| **Publication year** | **≤2021: 61,103 (98.9%)**; 2022: 283; 2023: 141; 2024: 163; 2025: 76 |

**What the counts say:**
- **Contamination is the binding axis for any task whose answer is the paper's own statement.** That is skill refusal 14. Only 663 papers postdate 2021, and all of them predate current model cutoffs.
- **The label is LLM-extracted.** It was validated on samples of 400 by materials scientists (paper, Technical Validation). Under D4 it is annotation, not measured truth.
- **Claimed depth is high: 88% of mechanisms claim 3 or more evidence types.** The skill says to trust only measured, leave-one-out depth.

## 3. The text-only floor (the BioReason check, run on MatMech)

`scripts/text_floor.py` uses TF-IDF cosine and no model. It takes one item per paper, n=3000, k=5, so chance is 0.20. Rivals come from other papers with the same link type.

| Template | Random rivals | Rivals the retriever itself would pick |
|---|---|---|
| T1: given cause + effect, pick the mechanism description | **0.985** [0.981, 0.989] | 0.733 [0.718, 0.749] |
| T2: given link + cause, pick the effect | 0.599 [0.581, 0.616] | 0.511 [0.493, 0.529] |

**How to read it:**
- **T1 with random rivals is BioReason-KEGG again.** The description restates the cause and effect, so the floor takes the ceiling and P2 closes it.
- With retrieval-hard rivals (the admissible constructed negatives of shape.md refusal 13), 27% headroom opens up. That headroom is lexical, though. It does not show that any measurement channel adds anything, and an LLM subject has read every source.
- T2 has more headroom, but it is **infer on the predictor line**. It needs a lift and would face I2 exactly as BioReason's DNA channel would.

**Conclusion:** a benchmark whose inputs and answers are MatMech text measures reading comprehension and memory. The FM question needs the answer to be **forced through a measurement**.

## 4. What "grounding on measurements" can mean here

| Route | What it gives | Supply (counted) | Construct-validity risk (I4) |
|---|---|---|---|
| **G1: figures as measurements** | Micrographs, read for grain size, phase fraction, morphology or defects. Plots digitized to curves: XRD, XPS, Raman, stress–strain, CV | 74.6k mechanisms with a microscopy image; about 19.7k XRD figures; about 5k stress–strain figures | Digitization error; composite panels; scale bars. PROXY until checked against the number stated in `experiment.result` |
| **G2: numbers in text as answer keys** | Measured scalars (lattice spacing, WCA, strength, band gap, overpotential) tied to a condition | 94k mechanisms with a number and unit | The number sits in the source text. It is contaminated as an *input*, but usable as a *grader* for an FM computation the agent sets up |
| **G3: external data joined by composition** | Materials Project / OQMD / JARVIS structures and energies; COD / ICSD reference patterns | 6.8k papers with a formula; the element list for the rest | Join ambiguity (polymorph, dopant level). Computed ≠ measured |
| **G4: an FM or physics forward model as grader** | MLIP-relaxed lattice or energy, simulated XRD, DFT on demand | Any G3-joined item | The prior instance measured MLIP-prior lift **+0.003** and FM-weighted XRD **−0.004** at I2 (both closed). A forward model must be certified against the *scored* quantity |

**Grounding rule for every candidate:** the item's answer must be recoverable **only** by running a measurement-reading or physics channel on an input the agent chooses or builds. That puts the FM in the scorer, generator or simulator role, below the predictor line, and makes the I2 lift measurable.

## 5. Candidate tasks and seed workflows (FM in the loop)

Each candidate is ruled against the four roots, per `shape.md`. The FM roles use the manifest vocabulary: encoder, predictor, scorer, generator, simulator. The **branch** is where the agent chooses. The **chain** around it is the mechanical floor built at I1.

### C1: Mechanism discrimination by evidence acquisition (explain + intervene: choose next measurement)

**Item.** One MatMech mechanism: a material, a cause and an effect, with the description and reasoning chain hidden. The candidate set is the true mechanism, retrieval-hard rivals (§3), and the paper's cross-paper conflict rivals where they exist.

**Environment.** Each item comes with a *menu* of evidence units: the paper's experiments, its figures, and its referenced and non-referenced knowledge. The paper recorded all of them, so the outcome of any request can be replayed. This is the in-paper analogue of the combinatorial wafer in the 19C guideline, and it removes the selective-labels block for the evidence the authors actually measured.

**Workflow.**
1. The agent reads the cause and effect and states hypotheses from the K candidates.
2. It requests evidence under a budget (for example 3 units). Figures arrive as images, not as their captions.
3. It sends each figure to FM tools: a microscopy encoder or segmenter for grain size, phase or defects; a plot digitizer for XRD or XPS peaks. Where a candidate makes a quantitative claim, such as "dopant expands the lattice", it runs an MLIP on a G3-joined structure.
4. It rejects rivals with written reasons, then commits a pick and a confidence.

**Classical counterpart.** The same menu, but only captions and the text of `experiment.result`. No image channel and no MLIP.

**Mechanical floor.** TF-IDF or retrieval ranking over all evidence (§3), plus "request the top-similarity evidence first".

**Grader.** The answer key (the paper's mechanism). A proper score on the calibrated probabilities raises the yield from one thresholded binary per item.

**Supply.** 141,388 mechanisms with depth ≥3, an image and confidence ≥0.8. **Contamination-clean supply is 187, from 2025 papers**, and it is still pre-cutoff for recent models.

**Binding risks.**
- **Contamination.** The subject may recognise the paper. Two mitigations: a masked-identity arm (material names and numbers perturbed), and restricting headline claims to items where the image carries information the captions do not. Measure that by leave-one-out depth.
- **The I2 lift of the image channel over captions.** Captions often state the result, so the lift may be zero.

**First count to run.** Take a sample of 200 items. For each, determine whether some *figure* distinguishes the true mechanism from its hardest rival when its caption does not. That fraction is measured image depth, and it decides C1.

### C2: Cross-paper contradiction diagnosis (explain: anomaly diagnosis)

**Item.** A conflict pair: a mechanism claim and a flagged rival sentence from another DOI. There are 7,145 flagged mechanisms. Also include within-paper non-monotone results, such as "CF-4.0MTMS propagates flame despite higher MTMS".

**Task.** Explain which difference between the two systems (processing condition, structural feature, composition) reconciles the claims, using both papers' measurements.

**FM roles.**
- Scorer: an MLIP or property model evaluates the agent's proposed structural difference.
- Encoder: compares micrographs across the two papers.

**Native negatives.** The rival claim is a found negative, not a constructed one.

**Grader.** This is the gap.
- One option is a certified judge, which needs I4/I5 with a wording-perturbation control.
- The other is restricting to pairs where a third paper measured the discriminating condition. That acts as a held-out repeat and is admissible. First count: how many pairs have such a third paper.

**Risk.** The flags come from an LLM detector at cosine ≥0.9. Many flags are nuance or wording disagreements, as in the sample (roughness vs surface energy). Audit a random 100 before counting supply.

### C3: Structure consistency from diffraction and microscopy (generate: inverse problem)

**Item.** A mechanism with an XRD experiment, a formula material and a stated number. There are 1,162 such mechanisms, 923 of them P→S. Examples: an interlayer spacing going from 0.97 to 1.67 nm after intercalation; a phase assignment to a JCPDS card; a peak shift under doping.

**Task.** From the *digitized* pattern (G1), and the micrograph where one exists, build a structural model: phase, lattice change, dopant site or intercalant. It must be consistent with both modalities.

**Workflow.**
1. Digitize the pattern.
2. Pull candidate phases from MP or COD (classical).
3. Build modified structures: substitution, intercalation, strain.
4. Relax them with an MLIP (FM, as generator or simulator).
5. Simulate XRD with pymatgen (classical forward model).
6. Compare with the measured pattern.
7. Check against the microscopy (lattice fringes, SAED).
8. Reject candidates that fail one of the two modalities, with a reason.

This is the "multimodal constraint satisfaction" family in the 19C guideline, and the only family there that produces a native negative.

**Classical counterpart.** Candidate phases from MP/COD without relaxation; Vegard's-law lattice estimates.

**Grader.** Two, both admissible under Gate 2:
- the forward model residual against the measured pattern;
- the stated number in `experiment.result` (for example the d-spacing) as an answer key.

**Yield.** One graded residual per item. It is not thresholded, so this candidate has the best resolving power per item.

**Risk.** 19C closed exactly this channel at I2. FM-weighted XRD had lift −0.004 against a band of 0.17. C3 differs in that the MLIP acts on a structure the *agent builds*, which makes it a LIFT candidate, not a CLOSE. That has to be declared at D4 and rebuilt at I1. Supply falls further once only digitizable single-panel patterns are kept, so count that first.

### C4: Quantitative effect prediction (infer; the BioReason analogue; control only)

**Item.** Cause + link + material, with the sign or magnitude of the measured effect held out (30,568 numeric → Property mechanisms).

**Floor.** T2 in §3 already reaches 0.51–0.60 at k=5.

**Ruling.** It sits on the predictor line, and no honest lift is recorded. **Use it as SFT warm-up data and as the negative control that reproduces the BioReason pattern.** Do not use it as the FM-advantage claim.

### C5: A KEGG-like MST graph with a temporal holdout (generate: procedure; infer lifted by budget)

**Build.**
- Normalise causes and effects to canonical nodes: processing operations with parameters, structural features, and properties with units. KEGG has curated IDs; MatMech has free text. This normalisation is the main engineering cost, and 150 or more free-form link labels show why.
- Aggregate the 207k edges into a graph with mechanism annotations and evidence counts.

**Task.** Given a target property change for a material class, propose a processing → structure → property route.
- The graph is frozen at year ≤ Y and scored against routes reported after Y.
- Use Y=2021, which leaves 663 papers after it. That is the only contamination-respecting split this corpus allows.

**FM roles.**
- Generator: MatterGen or DiffCSP proposes a structure for the needed structural feature.
- Simulator: an MLIP checks stability.

**Grader.** Match against the held-out routes. This is partial credit, and it needs the normalisation to be certified.

**Supply.** Limited by the post-2021 papers (663).

### Ruling summary (provisional; P3 is not yet run under a ratified shape)

| Candidate | Root / subtype | Grader available now | FM role below the line | Binding axis to count next |
|---|---|---|---|---|
| C1 | explain + intervene / evidence acquisition | answer key (+ proper score) | scorer (image FM, MLIP) on agent-chosen evidence | measured image depth; contamination |
| C2 | explain / anomaly diagnosis | judge, or a third-paper repeat | scorer | pairs with a third-paper measurement; flag audit |
| C3 | generate / inverse problem | forward-model residual + stated number | generator / simulator (MLIP on an agent-built structure) | digitizable-pattern supply; I2 lift |
| C4 | infer / point estimate | answer key | predictor only | **closed at Gate 1 without a lift. Control only** |
| C5 | generate / procedure | temporal holdout | generator / simulator | node normalisation validity; post-2021 supply |

**Recommendation.** Take **C3 and C1** to D5.
- C3 has the only grader that is *measured* (the pattern and the stated number) rather than annotated, and an FM role the agent must construct input for.
- C1 has the largest supply and a replayable environment.
- Run both censuses on 200 sampled items before writing any code beyond digitization.

## 6. SFT/RL data built the BioReason way, without its defects

| BioReason step | MatMech version | Fix for the defect |
|---|---|---|
| KEGG network string in the prompt | Material + MST chain + cause/effect (+ normalised nodes after C5) | Deduplicate items by (material system, cause); split by **paper cluster and year**, never by row |
| DNA FM embedding → linear projection | Figure → vision/microscopy encoder, projected; or a structure → MLIP embedding for G3-joined items | Always run the **text-kept, FM-channel-removed or shuffled** ablation (the I2 lift) |
| Claude trace written given the label | MatMech `reasoning_chain`: the authors' own evidence-typed steps, filtered to confidence ≥0.8 | Rewrite "image description" steps so the model must *derive* them from the image input, not copy them from the caption. Otherwise it learns to invent observations |
| GRPO, substring label reward | GRPO with verifiable rewards | Reward options: the numeric match to `experiment.result` with units (G2); the forward-model residual (C3); the pick under a proper score (C1). Add a penalty for evidence cited but never requested (C1). Grade intermediate claims that can be checked by an FM call |
| Single run, n=290, no CIs | — | Use `power.py` (MDE before any claim) and paired per-item scoring |

## 7. What the skill says to do next (zero or low cost, in order)

1. **D1 on seeds:** read 20 full papers, 10 for XRD in C3 and 10 for C1. Count branch points with the rejected option named, and measured image depth. Locators go in the seed ledger.
2. **D2 rules frozen:** confidence ≥0.8; main six links; year split; exclusion ledger.
3. **D3 tau:** cluster by chemical system (element set) and cause embedding; sweep the cut with `tau.py`.
4. **D4 shape record** for C1 and C3, with C2, C4 and C5 as alternatives considered. Declare delta, the channel-lift band and the uptake band.
5. **P2:** the text floor is already measured here (§3). Add per-item headroom.
6. **I1/I2 before any agent:**
   - C3: classical MP+Vegard vs +MLIP on 50 items.
   - C1: captions-only vs +image FM.
   - Rule CLOSE or LIFT with `lift.py`.
7. Only then build the SFT/RL data (§6) for the surviving candidate.

## 8. Limits of this analysis

- **§3 floor:** it uses bag-of-words retrieval. A dense retriever or an LLM would score higher, so the floor is a *lower* bound. For the same reason, the 73% "hard" figure understates how much of T1 is lexical.
- **§2 characterization counts:** these are regex matches on captions and experiment types. They are approximate and not audited.
- **Formula joinability:** the parser is strict and undercounts (for example "Mg alloy" fails, as intended). The element-set join is uncounted.
- **Status of the numbers:** no candidate has been ratified, so every supply number in §5 is provisional under skill refusal 17. They are counted to decide what to count next, not to rule.
