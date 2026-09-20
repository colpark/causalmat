# Judge review — Materials_Characterization/j.matchar.2015.10.016 (rank 17)

*Fractographical characterization of hot pressed and pressureless sintered AlN-doped ZrB₂–SiC composites*

**Verdict: approved with changes.** One panel check **overturned**.

Ruling criterion used throughout this batch: **overturned** when the cited panel does not show the node's claim *as stated* — a wrong panel, or a reading the panel contradicts; **confirmed** when the panel shows the claim, even if a number or a word needed tightening.

## Round-4 checklist

- **Spine.** 17 nodes after the one demotion below. HYP(need, gap) → hypothesis → DES(base, modification, sweep) → PRC(hot pressing | pressureless, the control branch) → STR(phase identity, interface, HP porosity | PS porosity) → PRP(fracture mode, hardness) → MEC(liquid-phase sintering | gas entrapment) → DSC/conclusion. Exactly the two-branch-plus-control shape the rule allows: the same AlN chemistry (m9) drives a pressure branch and a pressureless control branch that meet at the hardness node m14. Stage-ordered, connected, no orphan claims.
- **Evidence.** Every spine STR/PRP node has an incoming `evidences` edge. Both MEC nodes carry `basis: argued` — correct, since neither the liquid infiltration nor the gas entrapment is observed; they are argued from the reaction set k2.
- **Types.** m11/m12 as `STR/microstructure/porosity` rather than `distribution` follows the r04 rule (void amount → porosity). m13 as `PRP/behavior_class` (how it fails) rather than `PRF/service_capability` is right. m16 as `MEC/tradeoff` is right: a net outcome explained by one contribution outweighing another.
- **mm_ops.** All name a real act. `register_colocated_views` on o6/o9 is the intended use (a point EDS located on a marked feature of the SEM field). `compare_with_reference_value` on o1 → d1 is right: the prior report is a quoted value, not a plotted curve.
- **Audits.** 3 (a1, a2, lim1) plus one DSC/comparison — within budget, all load-bearing, and all stated as *"the figure does not resolve it"* rather than as contradiction, which is the correct distinction here. The paper's one real figure-vs-text conflict is carried on `image_support` (o6, o9 both `partial`) instead of spawning further nodes, as the audit budget intends.

## Panel checks (crops opened)

| node | panel_ids | ruling | finding |
|---|---|---|---|
| o2 | `#F2a` | **confirmed** | The PS series reads 85.5 → 78.3 → 70.6 → 70.0% at 0/1/3/5 wt% and the HP series 97.5/100/99.3/100 — exactly the node's numbers. The node's flag that the **MatMech summary quotes PS1 at ~92%** is correct; the panel contradicts the summary, and rule 37 was applied properly. |
| o9 | `#F5a` | **OVERTURNED** | F5a is the right panel — paper Fig. 6a (HP5), the arrowed layered boundary band plus its EDS — but it does not show the claim as stated: Zr Lα at ~2.05 keV is the largest peak (~55 counts), not Al (~22). No other panel supports "Al-dominated"; F5b (PS5) is more Zr-dominated still. No `correct_id`; the node has been corrected. |
| o13 | `#F7a` | **confirmed** | Measured on the crop: the 100 nm bar is 91 px, the bright interfacial band is 20–43 px vertically across a boundary inclined ~26°, i.e. **20–43 nm perpendicular**. The node's "~20–40 nm" is right and was evidently read off the bar, not from the text. |

Two further nodes were checked because they carry the interfacial-phase argument: **o6** (`#F4a`) confirmed — Si-dominated at ~2300 counts with a Zr doublet and Al/B/C/N at noise, so `partial` against the text's "mainly boron, carbon, silicon and zirconium" is fair; **o12** (`#F6a`, `#F6b`) confirmed — Al₂OC markers at ~33, ~59, ~63.5° in (b) only, no graphite marker in (b), and the ~33° Al₂OC marker does share its peak with ZrB₂.

No invented panel_id: all 12 cited ids appear in the packet's panel section. The two uncited panels (`#F1a`, `#F1b`) are the starting-powder SEM and XRD and are legitimately off the argument.

## Changes made

1. **o9 — the overturned check.** The label said the HP5 interfacial EDS is "Al-dominated". Read against the keV axis, Zr Lα (2.05 keV) is the largest peak at ~55 counts; Al (1.49 keV) is ~22 and Si (1.74 keV) ~12, with B, C and N clear at 10–13 above a noisy baseline. Label corrected to "clear Al with Si and B, C, N, on a Zr-dominated spectrum", `image_support` lowered **shown → partial**, and `image_note` now carries the peak heights. The node's record of the Fig. 6b/panel-(a) placement defect is kept and extended with the F5b counts.
2. **a1** — `image_note` extended: the ~26° reflection in F6a carries a **ZrB₂** marker as well as the graphite and BN markers. This strengthens the audit — that single peak identifies neither interfacial phase.
3. **m17** (`DSC/design_guidance`) taken **off the spine**. The r04 rule allows a non-conclusion DSC on the spine only when the guidance *is* the paper's headline; here the headline is the fractographic characterization and the conclusion m18 states it. Spine 18 → 17. Added `m13 → m18 supports` so the fracture-mode branch still reaches the conclusion; m17 keeps its `m13/m14 → m17 → m18` edges off-spine.

## Packet panel section

The panel section itself is clean — letters, tiers and crops all check out, and the "detector only; ocr read no label" panels (F3a, F4a, F4b, F5a, F7a) are correctly lettered.

**Record defect, correctly caught by the staff graph and confirmed here:** the packet's figure ids are offset from the paper. Packet **F5 carries the paper's Fig. 6**, **F6 the paper's Fig. 7**, **F7 the paper's Fig. 8**, and the paper's **Fig. 5 is absent from the record** (the captions in the packet say so verbatim while the ids do not). Panel ids follow the packet, which is the right convention, and the graph's `notes` records the offset. This belongs in the r04 §5 defect table alongside the AEM aenm.201501833 offset.

**Second upstream defect:** the MatMech summary block's PS1 relative density (~92%) disagrees with F2a (78.3%). Recorded in o2's `image_note`.
