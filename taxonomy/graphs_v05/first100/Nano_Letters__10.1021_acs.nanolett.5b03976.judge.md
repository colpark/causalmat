# Judge review — Nano_Letters/10.1021_acs.nanolett.5b03976 (rank 24)

*Direct Bandgap Light Emission from Strained Germanium Nanowires Coupled with High-Q Nanophotonic Cavities*

**Verdict: approved with changes.**

## Round-4 checklist

- **Spine.** 19 nodes after the cycle fix below. HYP(need, gap) → hypothesis → DES(base, **architecture**, sweep, **route**) → PRC(e-beam litho/etch → KOH undercut → ALD) → STR(shape, lattice strain, interface) → MEC(band shift) → PRP(PL redshift) → PRF(cavity Q and power handling) → PRP(net gain) → MEC(loss identification) → DSC/conclusion. Two branches after the strained structure — an emission branch and a gain branch — meeting at the negative-result conclusion.
- **g7 as `DES/route` with `purpose: decouple`** is a good call: the capillary reattachment exists only to give the wire a heat path, which is what makes the 10× pump-power range possible. Ruling #27.
- **Evidence.** Every spine STR/PRP/PRF claim has an incoming `evidences` edge. g14 carries `basis: argued` — right, since the pseudo-heterostructure is inferred from the strain maps rather than measured.
- **Types.** g12 `STR/phase/lattice` (lattice strain) rather than `microstructure/orientation` is correct. g18 `MEC/identification` rather than `pathway` is correct under the r04 rule — the operative loss is picked from a known catalogue (IVBA vs conduction-band FCA) by a model. g16 `PRF/service_capability` with `attrs.condition` follows ruling #36.
- **mm_ops.** Strong throughout: `match_to_design` on h1 (fabricated device against its intended geometry), `overlay_model_on_data` on h11 and on a3 (model reference → overlay, per ruling #12), `compare_coplotted_quantities` on h12 (separated loss terms on shared axes), `assess_spatial_distribution` on the two strain maps.
- **Audits.** 3 plus a `DSC/limitation` and a `DSC/comparison` — inside budget and unusually well placed for a negative-result paper. Each hits a different link: a1 the strain-contrast premise (g14), a2 the cavity claim (g16), a3 the circularity of the gain-model comparison (g18).

## Panel checks (crops opened)

Ruling criterion used throughout this batch: **overturned** when the cited panel does not show the node's claim *as stated* — a wrong panel, or a reading the panel contradicts; **confirmed** when the panel shows the claim, even if a number or a word needed tightening.

| node | panel_ids | ruling | finding |
|---|---|---|---|
| a2 | `#F4a` | **confirmed** | Exactly right, and the most consequential audit here. The 1.95% trace (red) is a dense comb of sharp resonances peaking at ~2700; the 2.37% trace (blue) is a **smooth envelope** peaking at ~1100 with no comb anywhere. The caption credits both strained wires with high-Q resonances, so `image_support: contradicts` is the correct grade, and the Q and FSR claims do rest on the 1.95% device alone. h6's numbers (0% ~280 near 1560 nm; 1.95% comb maxima ~2700; 2.37% ~1100) and limg1's grey detector-limit band above 2000 nm also check out on this panel. |
| a1 | `#F3b`, `#F3c` | **confirmed** | Confirmed on both. F3b (FEM) shows the pads black at essentially zero with faint red only at the taper fillets; F3c (Raman) shows the pads at a clear dark red, ~0.5–0.8% on the same 0–2.4% scale. The paper's "the Raman result matches the FEM simulation" holds for the wire and not for the pads — and it is the wire-to-pad contrast that g14 rests on. h3's note that the wire is clipped pure white at the top of the scale is also right. |
| h10 | `#F5a` | **confirmed** | F5a reads −350 (2.37%) and −520 (1.95%) at 5 mW, and −1250 and −1970 at 22 mW, negative throughout — the node's numbers exactly. The 1.95% error bars at 22 mW span roughly −1600 to −2380, and the two series do nearly touch at 5 mW. |

No invented panel_id: all 14 cited ids appear in the packet's panel section. The two uncited panels are the process schematic (`#F2a`) and a second interferometry view (`#F2d`).

## Changes made

1. **Spine cycle removed.** `g17 → g18 supports` and `g18 → g17 explains` formed a two-node loop, so the spine was not a stage-ordered path (only two of the 61 graphs in r01–r04 plus this batch contain such a pair). Kept `g17 → g18` — the negative measured gain is what licenses the loss identification — and moved the `explains` edge to **`g18 → g19`**, which is what the paper's conclusion actually says: inter-valence-band and free-carrier absorption hold the gain negative, so no lasing is seen. g18 now reaches the conclusion under its own rel.
2. **h7, h10** — `provenance: derived` → **`measured`**. Both read the paper's own reduction of data in the same panel (a Lorentzian fit; net gain against pump power), with no OBS parent in this graph, and v04 requires an incoming `derives` edge for `derived`.
3. **a3** — `provenance: derived` → **`computed`**. This is the one case in my eight papers where `computed` is the right answer rather than `measured`: the carrier-density abscissa the node reads *is* model output (a calculation of absorbed power plus a fit to theory), which is precisely what `computed` records, and it needs no `derives` edge. That is also the audit's whole point.
4. **h2** — `image_note` sharpened. The undercut region sits at ~0 nm while the wafer outside it runs +20 nm on the right and +30 to +38 nm on the left, so "20–25 nm below" is the **right-hand** reference; the trench-edge notches fall below −50 nm.

## Packet panel section

Nothing wrong. 16 panels across five figures, all tier A. Three OCR disagreements (`#F3a` read as "e", `#F4b` and `#F5b` as "q") are all cases where the detector letter is right and OCR has picked up a neighbouring glyph — `#F3a` in particular is the FDTD E_y panel, correctly lettered a.

**Text/figure conflicts recorded in the graph and confirmed here:**
- The Figure 5 caption puts the 1.95% device at **1961 nm** while the body text says **1923 nm**. Carried on h10's `image_note`.
- The Figure 4 caption credits both strained devices with high-Q resonances; F4a shows the 2.37% trace has none. This is the a2 audit, and it is a genuine caption-contradicts-figure case rather than an unresolved reading.
- F5c is **entirely model output** — no measurement separates inter-valence-band from conduction-band free-carrier loss. Correctly flagged in h12's `image_note` with `provenance: computed`, rather than presented as evidence.
