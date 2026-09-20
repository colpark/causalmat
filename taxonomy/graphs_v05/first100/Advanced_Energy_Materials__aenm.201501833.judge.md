# Judge review — Advanced_Energy_Materials/aenm.201501833 (rank 4)

**Verdict: approved.** No changes.

Ligand substitution of a Ni-BTC MOF into a porous nickel phosphate supercapacitor electrode. Single-branch conversion argument: one hydrothermal act produces four structure claims (bonding, phase, rod shape, porosity) that converge on the mechanism e14 and the capacitance e13, then on cycling performance and the conclusion. 16 spine nodes, one connected path e1 → e16, no orphan claims. Every spine STR/PRP/PRF claim is evidenced or carries `basis: argued` (e14). f6 and f7 are text-only OBS with no figs and correctly carry no mm_op. f4 uses `match_to_reference` against a JCPDS card, which is the right side of the r04 #12 boundary (empirical reference → match; model/fit → overlay).

## Panel checks

| node | panel_ids | ruling |
|---|---|---|
| f11 | `#F5f` | **confirmed** |
| f10 | `#F5e` | **confirmed** |
| f5 | `#F4a`, `#F4b` | **confirmed** |

- **f11 → F5f.** The derived electrode's arc is the larger one and is still rising at Z′ = 14 Ω, while the MOF arc peaks near −Z″ 4.7 Ω and is closing by 10 Ω; the inset gives high-frequency intercepts of ~1.0 Ω (derived) against ~1.4 Ω (MOF). The node reads the panel exactly. Calling this a contradiction of the text — which claims a narrowed semicircle and lower charge-transfer resistance after substitution — rather than a gap in it is correct.
- **f10 → F5e.** 64 % and 19 % are printed on the panel, and the two series run ~1630 → ~1045 F/g and ~400 → ~85 F/g over 1–20 A/g, as claimed. (The 4× ratio in spine node e13 checks out: 1630/400.)
- **f5 → F4a/F4b.** F4a is smooth faceted microrods; F4b is thicker rods blanketed in granular particles and loose debris. Both carry a 1 µm bar burnt into the SEM banner, at ×15,000 and ×16,000, so the comparison is at essentially the same magnification as the note says. Neither is a cross-section or transmission view, so the e18 audit about the unresolvable interior void is right.

All 13 panel_ids used appear in the packet.

## Audits

Three, all genuine and each correctly distinguished. **e17 with OBS f11** is a figure-contradicts-text finding, verified on the crop; it qualifies both the conductivity claim e11 and the mechanism e14, while f11 still records the one thing the panel *does* support for the paper, the lower high-frequency intercept. **e18** is a not-resolved finding (rods called hollow, no cross-section shown), and is labelled `kind: method`, not `anomaly`. The audit budget is respected.

## What the packet got wrong

- F4a: OCR reports the panel label as `（B）` when the panel is (a); F4b's 1 µm bar is read as "2m". Neither misled the staff, who read the banners from the images.
- F5e's `definition` credits the specific-capacitance panel to the MOF-derived electrode alone, although it plots both series.
- F1's record is the synthesis *scheme* (Scheme 1), so the packet's F-numbering runs one ahead of the paper's figure numbers throughout — consistent with the r04 note about this paper's F-id offset. Since the graph cites packet ids and those are internally consistent, nothing needed changing; anyone comparing with the published figure numbers must subtract one.
