# v07 F: precision of the second read

Every verdict is model against model.

## What was measured

CHECKPOINT_B counted 14 second-read flags on the 32 papers (24 Part B, 8 pilot). A flag is a grading unit (evidence node, cited panels) that net-grader ruled WRONG against net-reread's blind description. The 14 trace flags come from 13 distinct units: ACHM o16/F6b flags T3 and T4. That is 40 or fewer, so every unit was judged; there was no sample.

Each unit went to a fresh judge. The judge got the crop(s), the evidence node's label, the net-reread description(s) and the grader's verdict. It opened the crop(s) itself and ruled `real` (the panel does not show what the node says), `wording` (the panel shows it; the flag comes from naming or framing), `partial` or `unclear`. The judge was a general-purpose subagent, because the registered `net-judge` type has no Read tool and cannot open an image. Prompts: `reread_precision/u*.judge.txt`. Replies: `u*.judge.out.txt`. Every relayed prompt was checked byte for byte against its file (`jobs_a/b.json.harvest.json`). Tool: `trace_kit/reread_precision.py`.

## Result

| ruling | units | trace flags |
|---|---|---|
| real | 1 | 2 |
| wording | 12 | 12 |
| partial | 0 | 0 |
| unclear | 0 | 0 |
| **total** | **13** | **14** |

**Precision (real over all): 1/13 = 8% of units** (2/14 = 14% of trace flags).

The second read is sensitive but not precise. Twelve of the thirteen flags are panels that do show the observation. The one real flag is a wrong panel: the dielectric-loss node cites a bar chart of elongation.

## Examples

### real (1)

- **u02**: Advanced_Composites_and_Hybrid_Materials__s42114-021-00366-2 o16 on F6b (traces T3, T4)
  - Node: BST@Ag1% loss climbs above 100 kHz to ~0.065 at 1 MHz; low-frequency losses exceed 0.026
  - Grader: WRONG — the candidate describes a bar chart of breaking elongation (%) vs Ag-doping content, which is an entirely different figure/technique and content than the key's dielectric loss vs frequency plot for BST@Ag1%, so it contradicts the key.
  - Judge: Panel F6b is a hatched bar chart of breaking elongation (%) for Pure PAEN (6.9), BST@Ag1% (5.8), BST@Ag3% (4.5) and BST@Ag5% (4.4). It has no dielectric loss or frequency data, so it does not show the BST@Ag1% loss rising to about 0.065 at 1 MHz that node o16 claims.

### wording (12)

- **u01**: Acta_Materialia__10.1016_j.actamat.2015.04.055 o2 on F1a+F1b (traces T1)
  - Node: TNM shows globular grains; TNM0.75C shows coarse lamellar colonies among globular grains
  - Grader: WRONG
  - Judge: Panel a shows equiaxed, blocky-to-rounded gamma, alpha2 and beta0 grains with no lamellae, which fits 'globular grains'. Panel b shows coarse lamellar colonies (left half) next to equiaxed grains (right half), which is what the node says for TNM0.75C. The reader called the lamellae 'lath/Widmanstätten-like' and the grains 'angular', but that describes the same features in different words.

- **u03**: Advanced_Materials__10.1002_adma.201702037 o14 on F4b (traces T2)
  - Node: Fitted gel Mo 3d components do not form 3.1 eV doublets (pairs ~1.6 and ~6.8 eV apart); 235.3 eV sits at Mo6+ 3d3/2
  - Grader: WRONG — The candidate describes the gel's Mo 3d spectrum as retaining a normal Mo 3d5/2/3d3/2 doublet with an added "MoS2-PEG" bonding peak near 235 eV, but the key states the fitted gel Mo 3d components specifically do NOT form the expected ~3.1 eV doublet spacing, and that the ~235.3 eV peak is as
  - Judge: In the Gel Mo 3d fit, the two components labeled (MoS2) sit near 229.6 and 231.2 eV, about 1.6 eV apart rather than the 3.1 eV Mo 3d doublet spacing. The small (MoS2-PEG) shoulder near 228.5-229 eV is about 6.5-6.8 eV below the large (MoS2-PEG) peak at about 235.3 eV, so the node's spacing claim is visible in the image. The figure labels the 235.3 eV peak MoS2-PEG, and reading it as Mo6+ 3d3/2 comes from standard reference energies rather than a contradiction in the image. The reader followed the figure's labels and never checked the peak spacing, and the grader counted that difference in framing as a contradiction.

- **u04**: Advanced_Materials__10.1002_adma.201702037 o19 on F2d (traces T3)
  - Node: At 240 min G' is ~0.5 kPa and still rising at 400 min (~1.7 kPa): no 3 kPa plateau within 4 h
  - Grader: WRONG
  - Judge: The PEGSH/(2% MoS2) G' curve is at a few hundred Pa (about 0.3-0.5 kPa) at 240 min and still creeping up to about 1.5-2 kPa at 400 min, never reaching 3 kPa. The reader calls the slowing rise near 400 min a 'plateau', which is a different framing of the same data, not a contradiction.

### partial (0)

None.

### unclear (0)

None.

## Why the wording flags arise

- The reader describes a part of the figure the node does not cover. u10 and u11 are Acta 2014: the node describes the x-z maps and the grader applied the reader's description of the y-x maps.
- Different names for the same feature: nanoflakes, whiskers or petals (u12); network or strings (u13); plateau or slowing rise (u04); globular or equiaxed (u01).
- The grader returned a bare WRONG with no reason in 5 of 13 cases (u01, u04, u07, u08, u12).
- The grader treated a reader who did not see the key's feature as contradicting it (u06: the reader said all three elements were uniform where the node said Ni was patchy; the judge saw Ni patchy).

## All units

| unit | paper | node | panels | ruling |
|---|---|---|---|---|
| u01 | Acta_Materialia__10.1016_j.actamat.2015.04.055 | o2 | F1a+F1b | wording |
| u02 | Advanced_Composites_and_Hybrid_Materials__s42114-021-00366-2 | o16 | F6b | real |
| u03 | Advanced_Materials__10.1002_adma.201702037 | o14 | F4b | wording |
| u04 | Advanced_Materials__10.1002_adma.201702037 | o19 | F2d | wording |
| u05 | Bioactive_Materials__j.bioactmat.2020.01.002 | o15 | F6a+F7a+F8a+F9a | wording |
| u06 | Journal_of_Advanced_Ceramics__s40145-021-0476-z | o6 | F2d | wording |
| u07 | Journal_of_Magnesium_and_Alloys__j.jma.2013.12.002 | n10 | F4a+F4b | wording |
| u08 | Journal_of_Materials_Science_&_Technology__j.jmst.2020.05.053 | o17 | F4b | wording |
| u09 | Journal_of_Materials_Science_&_Technology__j.jmst.2020.05.053 | o12 | F2d | wording |
| u10 | Acta_Materialia__10.1016_j.actamat.2014.06.008 | o6 | F6a+F6b+F6c+F6d+F6e | wording |
| u11 | Acta_Materialia__10.1016_j.actamat.2014.06.008 | o8 | F5a+F5c+F5e | wording |
| u12 | Advanced_Energy_Materials__aenm.201301564 | o1 | F1a+F1b+F1c+F1d | wording |
| u13 | Rare_Metals__s12598-012-0515-6 | o1 | F1a+F1b+F1c | wording |

Every verdict is model against model.
