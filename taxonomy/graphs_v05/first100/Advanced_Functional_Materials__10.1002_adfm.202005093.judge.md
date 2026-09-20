# Judge review — Advanced_Functional_Materials/10.1002_adfm.202005093

**Engineering 2D Multifunctional Ultrathin Bismuthene for Multiple Photonic Nanomedicine** (rank 9)

**Verdict: approved with changes.**

## Checklist

- **Spine.** Reads as the paper's argument: need for one NIR agent → freeze-thaw + NaBH4 route → few-layered bismuthene → 0.69 eV gap and NIR absorbance → heat + ROS → PA/CT imaging and tumour eradication → conclusion. It was 20 nodes with **two roots**: n1 (HYP/need) and n11 (MEC/pathway, water intercalation prising the Bi layers apart), which had no incoming spine edge — only a KNW premise. n11 is now `spine: false` (19 spine nodes, one root, connected).
- **Evidence.** Every spine STR/PRP/PRF claim has an `evidences` edge; the two MEC nodes carry `attrs.basis = argued`. No orphan claims.
- **Types.** Correct under v04 rules. o4 as `OBS/signal/reference_match` (whole pattern against PDF cards) rather than `feature_assignment` is the right side of the r04 rule; o6 `characteristic_value` for the Tauc intercept and o7/o11/o12 `fitted_parameter` are right; n17 as PRP/value with `proxy = DPBF absorbance decay` keeps `basis = evidenced`, which the v04 proxy rule allows.
- **mm_ops.** One correction: `o3 -> n13` used `register_colocated_views`, but the act that yields "0.227 nm fringe spacing" is a measurement on the F2h enlargement → `measure_feature_metric`. The rest name what a reader actually does (compare stacked XPS panels; read the Tauc intercept; fit A/L vs concentration).
- **Audits (3, ≤5).** o2 (AFM 14 nm ⇒ ~35 layers, undercutting "few-layered") and o5→n21 (XPS: reduction only partial, Bi2O3 doublet still the largest) both genuinely change support, and both are stated as qualifications, not contradictions — correct, since the figures agree with themselves and only bound the text's wording.

## Panel checks

| node | panel_ids | ruling | finding |
|---|---|---|---|
| o2 | `#F2c`, `#F2j` | **confirmed** | F2j is the AFM height image with a line profile annotated **14 nm** between two green arrows and a 0–20 nm colour bar. F2c is the 200 nm-scale TEM of bismuthene. Both carry the claim. |
| o5 | `#F2m` | **confirmed** | F2m shows the two stacked Bi 4f spectra with every component labelled. Bismuthene (top): Bi 4f7/2(Bi) is about half the height of Bi 4f7/2(Bi2O3). Bismuthene oxide (bottom): Bi 4f7/2(Bi) is a small shoulder. Bi2O3 dominates in both, exactly as the node says. |
| o15 | `#F5f` | **confirmed** | F5f is the six-arm tumour-volume plot to day 22 and shows the claimed ranking and the flat combined arm. The panel is right; three of the node's six day-22 numbers were not, and were re-read (below). |

No invented panel ids: every id in the graph appears in the packet's panel section.

## Changes applied

1. `n11` → `spine: false` (spine connectivity; 20 → 19 spine nodes).
2. `o3 -> n13` mm_op `register_colocated_views` → `measure_feature_metric`.
3. `o15` label re-read from the F5f crop: BNs-BSA ~2380 (the highest arm, marked n.s. against PBS), PBS ~2100, lasers ~1520 (was ~1750), +660 nm ~1480, +808 nm ~370, +both ~0 mm³. `image_note` corrected: the 660 nm arm separates from the PBS/BNs-BSA cluster from about day 8, not day 12.

## What the packet got wrong

- **Figure numbering is offset, and the graph's `notes` already records it:** packet F4 carries the paper's Figure 5 caption, packet F5 the paper's Figure 6; the paper's Figure 4 is absent from the record. Panel ids are built on the packet numbering (`#F5f` is the paper's Fig. 6f), which is the right convention — ids follow the image file, not the caption — but anyone tracing back to the PDF must apply the offset.
- **OCR noise in the panel section, not in the graph:** `#F2c` cues read "scale bar 200mm" (it is 200 nm) and `#F2h` reads "scale bar 0.227 mm" (0.227 nm, and it is the fringe spacing, not a scale bar). `#F2k` image_labels are garbled ("zto", "名馆"). The graph did not inherit any of these.
- The caption for `#F3b` says "normalized absorbance at 470 nm" while the panel axis reads 421 nm and the main text says 410 nm; the graph records this in `o8.attrs.image_note` rather than inventing a value.
