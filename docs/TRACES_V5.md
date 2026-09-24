# Traces v5: calibrated keys, repaired items, 32 papers

Generation only. **Every verdict is model against model**, and it is said on every page.

v4b established that the items require reasoning. Two reviews then found that the keys overstated
what the evidence permits. v5 recalibrates the keys and scales the methodology from 5 papers to 32.

## The funnel

| stage | count |
|---|---|
| papers with a graph and a MatMech mechanism record | 104 |
| papers selected | **32** |
| hops | 175 |
| hops attachable to panel evidence | 129 |
| links confirmed (8 span + 36 stage+graph) | 44 of 52 |
| traces built | 30 |
| traces after the spine | 25 |
| steps | 53 |
| **items** | **60** over 18 papers |
| **items surviving** | **30** over 22 traces |

## What was dropped, and why

**14 papers produce no item at all, and not one was lost for lack of evidence.**

| reason | papers |
|---|---|
| no confirmed link anywhere in the paper | 9 |
| links and attachable hops do not lie on one path | 5 |

The instructive cases are the papers where the evidence is present and the chain is not.
`j.jma.2020.09.027` has 7 hops, **all 7 attachable, zero confirmed links**. `j.jmst.2020.05.053` is
the same. `j.bioactmat.2020.01.002` has 8 hops, 6 attachable, no link. Every hop in those papers
sits on figures our graph reads, but no two consecutive hops share a spine claim or are joined by a
spine edge. This is the v3 finding at scale: **attaching a hop to evidence is easy; joining two hops
into a chain our graph will vouch for is what fails.**

**30 of 60 items drop**, for two reasons:

| reason | items |
|---|---|
| the key says nothing combines — a single-step item, not a cross-step one | 27 |
| dependency not real under the key | 3 |

An item survives only if its key contains a proposition combining the previous step's output with
this step's evidence, the inference follows, and the dependency is real.

## The surviving 30

| causal strength | items |
|---|---|
| associative | 20 |
| conditional mechanism | 4 |
| discriminating | 3 |
| descriptive | 3 |

**22 of the 30 survivors carry a key that names something as not identifiable.** Across all 60
items it is 40. That is the calibration doing its work: two thirds of the time the honest key says
two candidate causes cannot be separated, and that is a scorable answer rather than a failure to
answer.

Only **3 items are discriminating** — the strongest level, where the evidence picks one explanation
over another. Two of those three are hand-calibrated.

## Hand-calibrated against drafted

Seven keys are hand-written from the brief. **The other 53 are model drafts and are marked as drafts
on every item and every page.** At five papers every combining proposition was hand-written; at 175
hops that is not possible, and pretending otherwise would misrepresent the artefact. Six
hand-calibrated items survive; the seventh, the antibiotic item, drops because its own label says
the dependency is none.

The seven, and what each fixes:

- **Acta, split in two.** Depth counts derived conclusions, and the density-yield covariation and
  the [0001] loading comparison are two. The density key now says *consistent with a strengthening
  contribution from the nanoplates* and records that plate **thickness moves the opposite way**,
  28 → 84 → 14 nm against density 9.8 → 0.3 → 9.0, so the two plate descriptors do not covary with
  each other and the comparison cannot isolate which carries the strength. The loading item states
  that ~355 MPa is a fracture stress and ~72 MPa a flow stress: **not a yield ratio**, and dividing
  them gives a number with no mechanical meaning.
- **Biomaterials, branched into three.** The texture key is that **cobalt inventory and texture
  cannot be separated here** — adding cobalt both lowers the texture and raises the inventory, so
  ruling out a direction is not ruling out a cause. HIF-1α → VEGF is removed; the dose-response item
  asks whether the two readouts describe one dose response and the key is that they do not, since
  2Co raises VEGF and 5Co does not. The antibiotic item notes that cumulative release plateaus by
  72 h while survival keeps falling to day 7.
- **AFM** defines emission complexity as the number of resolved bands below 150 K counting a
  distinct IR tail, states the window and excitation, and records that three samples made by three
  growth routes confound domain size with route.
- **Rare Metals** uses Table 3, 311 → 376 → 406 MPa, with the Cu-content difference as a confound.

## What the scale-up broke, and what that says

**`net-decompose` is not stable across runs.** The v3 run that built v4 matched Acta M1 to n2, n8
and n9; re-running it for this batch returned n8 alone, dropping the nanoplate density series that
the entire density-versus-yield comparison rests on. The same instability cost Nano Letters M3 its
n17 in 4 of 6 byte-identical runs. Acta step 1 is therefore **pinned** to n8 and n9, and the pin is
recorded on the item and shown on the page. Any result that depends on a single decompose run should
be read with that in mind.

**Two of the brief's fixes conflicted.** Trimming step 1 to one property was taking whichever
property sorted first, which on Acta kept the phase identity and threw away the density series. The
trim now keeps the property group with a graph edge into the next step's claims.

**A hand key was silently dropped by a dictionary.** Two hand keys target Biomaterials step 2,
because the brief branches that step, and a plain `{(paper, step): key}` lookup kept only the last.
Fixed, and all seven now apply.

## Checks

- **350 decompose replies and 60 key drafts, all verified byte-for-byte** from the agents' own
  transcripts across five relay batches. 2.15 claims per hop over 175 hops, inside the
  discrimination limit.
- **Output-schema conflict, checked and clear.** The `net-writer` agent definition carries its own
  output schema that competes with the drafting prompt's. Three drafters reported noticing it. All
  59 parseable replies used the prompt's schema and **none** used the definition's.
- **One reply claimed to have repaired its own trailing comma and had not.** The parser now strips
  trailing commas as a fallback; a reply asserting its JSON is valid is not evidence that it is.
- **Leak check: 0 genuine leaks over 22 pages.** Two matches were coincidental — "Friction stir
  processing (FSP)" is a MatMech cause span and also the wording of our own node n3, because it is
  simply the name of a technique. `leakcheck.py` now counts a match as a leak only when the phrase
  is absent from our graph's own labels.
- All 22 pages balance, three tabpanels at equal depth, 214 panels embedded.

## Pages

`results/v5/pages/<trace>.html`, 22 pages for the 30 surviving items, zipped to
`results/v5/pages.zip` (2.4 MB). Tabs: items, whole graph, provenance. Every item shows its
question, the quantity kind on each side, the evidence, and the key with its limits, what is
permitted, what is not, and what is not identifiable — plus its three labels and whether the key is
hand-calibrated or drafted.
