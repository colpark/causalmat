# Reasoning-trace redesign: support chains, annotation layers, necessity

causalmat working plan. 23 September 2026. Supersedes the single-panel cutter used through v07.
Counts are from the 83 argument graphs and 320 cut traces of the 80-paper run on branch
`v07-scale/2026-09-21`.

## Why the change

The v07 cutter produced 115 open traces that are all depth 1, all single evidence node, and all either
3 or 5 reasoning steps. Half are "does this figure support this claim". Every intervene,
competing-cause and generate trace closed. Meanwhile the graphs behind them average 15.7 spine
claims and 6.6 technique families per paper, and hold 350 claims with two or more figure-backed
evidence nodes, 153 of them spanning two or more techniques, each panel already carrying a
four-level support label. The bottleneck was the cutter, not the corpus. Two rules did most of the
damage: a trace died if any one panel was annotated (89 closures) or missing (35 closures).

## 1. Recut for support chains

- Seed at spine claims with two or more figure-backed evidence nodes. 350 qualify; 153 span two or more technique families.
- Present panels in the paper's own argument order, one step per panel.
- Per step, ask what the panel contributes on the four-level scale: shown, partial, not addressed, contradicts. Ground truth is the existing image_support field plus the edge relation.
- Close the chain with the overall support level and what is still missing.
- Every trace needs at least one step where a foundation model acts on real data, or it goes to a different pile.
- Keep the three hard rules from v06c: the cited panel must match the node's technique; the answer must be findable from what is given; nothing from after the answer may appear on the sheet.
- Record answer_scope so partial answers are first-class rather than failures.

## 2. A chain survives a bad panel

- Drop the offending panel and keep the chain when the remaining evidence still carries the claim.
- Record which panel was dropped and why, so the trace's depth and channel count stay honest.
- Close the trace only if dropping the panel leaves the claim unsupported.

## 3. Annotations become a layer, not a deletion

- Split each panel by colour saturation into a clean image and an annotation layer holding text, arrows and boxes with coordinates. Fall back to the stored OCR boxes for white or black annotations.
- Three uses, chosen per item: hide the layer for perception; show the annotated panel as an exemplar and test on the unannotated panels of the same series; or make the author's label the claim under test.
- Hide the whole layer, not only the words. An arrow still says where to look.
- Do not inpaint by default. Leave the removed region visible as a mask and declare it.
- A masked or repaired region may never overlap the feature being graded.
- Prefer clean panels over repaired ones, which series figures usually make possible.
- Skipping remains only as the fallback when the split fails.

- Harvest every extracted label into a separate localization set whether or not the item survives: text, arrow endpoint, box, sample, technique.

## 4. Oracles for modalities with no model

- Serve only modalities with no model or simulator: electrochemistry, thermal, mechanical, transport, assays.
- Return an ordinary tool result in plain text. Do not invent a special token; a bespoke protocol is learned before the reasoning and cannot be told apart from it afterwards.
- Return measurements from observation nodes, never interpretations from claim nodes.
- Instrument channels with a model or simulator always hand over the real data and are graded on the read.
- Some oracle returns should be partial or contradicting, drawn from the existing audits, so the model does not learn to trust tool output blindly.
- Tag each step with what it tests: perception, selection, or integration. Report those separately rather than as one blended score.
- Run an oracle-complete arm, every step served as text, as the generalized floor test. If it succeeds, the item is text-sufficient.

## 5. Necessity, without combinatorial cost

- Structural leave-one-out on every step, no model calls: remove the step and ask whether the graded target still has shown support.
- Use the floor and full arms as brackets. Floor correct means nothing was necessary; full arm failing makes necessity meaningless. Skip further work in both cases.
- Empirical leave-one-out only on FM-lane steps, typically one to three per trace, so two or three extra calls per item. Never enumerate subsets.
- Greedy backward elimination on a 50-item calibration sample, to detect redundant pairs that single leave-one-out marks as both unnecessary.
- Ablate at channel or step-group level, not node level. Node-level necessity already failed once: with every figure opened, evidence is dense and every single node looks redundant.
- On the calibration sample repeat each ablation three times and take the majority. Elsewhere report necessity as a confidence, not a binary.
- Steps that fail necessity move to a perception set. They are not reasoning steps and must not pad chains.

## 6. Alignment controls before scaling

- Three controls: permute the answer, permute the image, remove the image.
- Permute across task types so a swapped image is certainly wrong.
- Run before scaling and report per modality. This is the cheapest direct test of whether an item needs its pictures.

## 7. Close the two open writer faults

- Fill graded_target, which is null on the failing items, so the scope check can run at all.
- Check quantities, not node ids. If the key leans on a number, sample or range the question never mentions, fail the item. Both open faults share this shape: a key ruling on the >0.05 series when the question bounded the claim to 0.032–0.042, and a key ruling on a 3 kPa plateau the question never raised.

- Copy the claim text into the question rather than paraphrasing a narrowed version of it.
- Allow partial verdicts on rejection items instead of forcing yes or no. Both open faults are better items as partial rulings.
- One rewrite on failure, then block.

## Then scale

Run the remaining 120 papers only after 1 to 7 are in place, with per-paper cost and yield recorded
as now. Running them under the current cutter would mass-produce the item type we are replacing.

## Parked, and why

- Belief-update items (predict, measure, revise). The corpus has 18 claims with both a computation and a measurement and 16 of them agree: papers publish the surviving trajectory. Needs constructed counterfactuals or raw data, not extraction.
- Request-based environment as a general protocol. Choosing from a curated menu of five measurements is an easier problem wearing the costume of a harder one, and the menu itself leaks. Keep it only where a next-measurement decision is genuinely held out.
- Raw beamline and CFN data. The right long-term source: no annotations, no memorization, no copyright. Needs the specimen-level join between beamlines and electron microscopy before items can be graded. All three reuse the support-chain schema, so each gets cheaper once section 1 exists.

## Standing caveat

No item in this pipeline has been checked by a person. Every verdict, including the four-level support labels this
redesign is built on, was produced by a model reviewing another model. At a few hundred items a human audit
is still affordable and is the cheapest way to find out whether "valid" means what we think it means.

---

Source: `trace_redesign_plan.pdf`, committed alongside this file.
