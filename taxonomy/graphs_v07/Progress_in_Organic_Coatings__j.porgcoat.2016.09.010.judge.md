# Judge review: Progress_in_Organic_Coatings/j.porgcoat.2016.09.010

**Verdict: accept with minor changes.**

Round-4 checklist:
- **Spine:** the spine reads as the paper's argument. It has 18 connected nodes: need, hypothesis, Ce/APTES design and sweep, Ce dip, APTES grafting, coating, partial Ce coverage, grafted silane, non-polar surface, H2 evolution, dispersion, NH2-epoxy MEC, barrier MEC, impedance ranking, salt spray, adhesion loss, conclusion.
- **Evidence:** every spine STR/PRP/PRF claim has evidence. Both MEC nodes are basis=argued.
- **v04 rules:** v04-valid. I checked types, rels and mm_ops against vocab/v04.json.
- **mm_ops:** each op names what the reader does.
- **Audits:** 5 (o5, o10, o20, o21, o22). I checked each against its image and all are fair.

## Changes
- o7, o8: source figure -> text. The solvent identity (MEK, butyl acetate) appears only in the captions.
- o9, o10, n12: source figure -> text. That the gas is H2 and that the test runs in pH 1.0 acid appears only in the caption.
- n8: source figure -> text. Two facts are not on the panel: that the samples are Ce-bath-treated particles (caption), and that EDS reads surface Ce (linked text).
- o16: source figure -> text. That the photographs show steel after the coating was peeled appears only in the caption.
- o19: technique MECH:pull_off -> OPTICAL:photograph. Source figure -> text.
- o1: the label no longer says "surface".
- o22: image_note now records that Un3 (F8a) also shows a cavity, so the cavities are not unique to S3.
- n10->n12 and n26->n12 (causes): mode alternative -> joint.

## Panel checks (18 crop citations on 14 nodes; all opened; 0 overturned)
| node | panel(s) | ruling | note |
|---|---|---|---|
| n8 | F1b | confirmed | Ce inset 0.5/0.6/1.1/0.9% |
| o1 | F1b | confirmed | same bars |
| o3 | F2c | confirmed | four O 1s components; Al-O tallest |
| o20 | F2b | confirmed | Al metal at ~78.2 eV sits above Al2O3 at ~75.4 eV |
| o21 | F2c | confirmed | peak heights CeO2 < Ce-OH < Ce2O, the reverse of the text |
| o4 | F3a, F3b | confirmed | no visible layer; cues micrograph/SEM are compatible |
| o6 | F4 | confirmed | 425 C retention ranking as labelled |
| o7 | F6a, F6b | confirmed | Al 3750->1260 NTU; Ce-Al pH 3.4-4.2 track Al |
| o8 | F5b | confirmed | silanised 850-1050 vs Al ~490 NTU |
| o11 | F8a, F8b | confirmed | S3 particles still clustered |
| o22 | F8b | confirmed | cavities ~290-460 nm |
| o16 | F9b, F9c, F9d | confirmed | S2 bright, rust only at the scribe |
| o18 | F12a, F12b, F12c | confirmed | blank ~44.5%, S4 ~18.2%, S2 ~18.5% |
| o19 | F11c | confirmed | wet S2 has a small bare patch; wet blank is fully bare |

I also opened the uncited panels behind nodes that carry `fig_ref`: F2 whole (the o5 inset), F7 whole (o9, o10, n12) and F10 whole (o12, o13). All match their labels.

## Technique mismatches
- **o19 / F11c:** the crop is a photograph of the dolly areas. Technique changed MECH:pull_off -> OPTICAL:photograph.
- **o12, o13 / F10a-c:** the OCR cue is XRD, which is incompatible with ECHEM:EIS. The crops are the correct Bode plots, and the cue is a misfire, probably from the "Phase Angle" axis label. This is not the known micrograph misfire, so I kept the staff's dropped citation (figs F10, panel_ids [], fig_ref).
- cue_overrides: none.
- read_from: no errors. o3 and o20 restate annotation labels and are already marked "annotation".

## Mode changes
- n10->n12 and n26->n12: alternative -> joint. The choice between barrier protection and H2 trapping is weighed only in linked text for F7. No caption or figure shows it.

## MatMech tally (recorded after the graph was final; graph not edited)
Supports 4, contradicts 1, not covered 0.

- **M1** (Ce + APTES treatment -> Ce layer + grafted APTES): supports (n5, n6, n9, n10). The graph adds that Ce coverage is only partial.
- **M2** (Ce/APTES surface -> corrosion resistance + hydrophobicity): supports (n9-n12). The graph qualifies it with the H2-trapping co-cause (n26) and the o10 audit.
- **M3** (dispersion -> adhesion, low porosity): supports (n13, n15, n19). The support covers adhesion retention after salt spray only. By the text, the blank has the highest dry pull-off strength.
- **M4** (Si-Ce-Al in epoxy -> superior protection): supports (n16, n18). S4 is level with S2. The graph does not support the Ce-APTES synergy that M4 argues for.
- **M5** (Si-Ce-Al -> the highest protection of all): contradicts (n16, n18, n20, o11, o16). Three points:
  - F9d shows S2 at least as clean as S4.
  - The imaged S coating (S3, the only one imaged) still has clustered particles.
  - The conclusion names Si-Al-2 as best.
