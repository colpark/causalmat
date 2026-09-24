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


---

# v5b: closing the key audit

## 1. The key audit, sampled and in full

| | sampled 12 | **all 23 drafted survivors** |
|---|---|---|
| propositions hold | 4/12 = 33% | **9/23 = 39%** |
| limits hold | 47/47 = 100% | **86/89 = 97%** |

The sampled figure is what the brief asked for; the full figure supersedes it. **The sample was
optimistic on limits** — across all 23 keys three limits are wrong, not none — and about right on
propositions. Seventeen statements were rewritten, sixteen propositions and one limit set.

The split is the finding, and it is stable across both cuts: **drafters write reliable caveats and
overstated conclusions.** The limits were requested with worked examples of what a confound looks
like; the proposition is where a model wants to conclude something.

The one proposition ruled `wrong` is a misreading, not a nuance. The yield-strength series 93, 113,
124, 127, 136, 142 MPa maps to 0, 5, 10, 15, 20, 25 wt% SiCp, so **127 MPa belongs to 15 wt%**, and
the draft had attributed it to 10 wt% while arguing that 5 and 10 wt% give the largest gains.

## 2. What the audit cannot see

**The per-statement audit rules whether each *stated* limit is true. It never asks whether a
*needed* limit is missing.** That is the whole of its blind spot, and 86 of 89 limits holding says
nothing about it.

Nano Letters is the case that proves it. The auditor correctly struck an unsupported Na-specific
mechanism claim — and its own replacement then compared Li **charge** capacity against Na
**discharge** capacity. Every statement in the key was true; nothing in a per-statement audit could
fire.

Worse, **that key was wrong the same way twice.** The auditor introduced the mismatch, and my own
`collect()` — which re-applied audit fixes on every run — silently reinstated it over the
correction. It survived only because the correction happened to also append a limit, which is luck,
not a safeguard. `collect()` is now idempotent and records when it declines to overwrite.

The correction is stricter than a swap: at cycle 40 the data give Li *charge* (~840 mAh/g) and Na
*discharge* (~70), and **neither Li discharge nor Na charge**, so no like-for-like 40-cycle
comparison exists in this evidence. The key compares first-cycle numbers like with like — 1st
discharge 1330 against 865, 1st charge 870 against 470 — and carries the absence of a same-kind
40-cycle pair as a limit.

## 3. The quantity-kind check, and its own error rate

One further question of all 29 keys: does the proposition compare quantities of different kinds?
The raw result was **14 of 26 ruled `mixed`, 54%** — with 3 unparsed. That number should not be
quoted, because the check has a category error and I reviewed every ruling by hand:

| my review | n | |
|---|---|---|
| **genuine** | 7 | a real mismatch: test against service temperature, rate against cumulative amount, absolute against normalized, fracture against flow stress |
| **borderline** | 2 | cross-assay comparisons, arguable either way; fixes kept and flagged |
| **not a mismatch** | 5 | a covariation *relates* two different quantities — that is what the item is for |

**The checker conflates "relates two different quantities" with "equates two quantities of different
kinds".** Yield stress against nanoplate density, domain size against emission complexity, cobalt
release against surface area — each is the covariation or mechanism check the item exists to test.
Ruling those `mixed` is a category error, not a finding. Corrected rate: **7 genuine of 26 = 27%**,
plus the Nano Letters mismatch found by review rather than by any check.

One ruling was also wrong on its facts: it called the Biomaterials surface areas "not present in
the cited observations at all". They come from step 1, which the item explicitly takes as input —
the checker was shown this step's observations and not the previous step's numbers. A prompt-design
fault in my check, not a fault in the key.

**The check overwrote two hand-calibrated keys before I caught it.** `acta_density_yield` lost the
words "move together", which is the entire covariation, and `biomat_dose_response` was rewritten
too. Both are reverted to the brief's wording, both carry the incident as a logged miss, and the
pass now records a ruling against a hand key rather than applying it. A hand key is the authority
on its own item.

## 4. The reports

**32 self-contained HTML reports**, one per paper including all 16 with no surviving item, in
`results/v5/reports/`, zipped to `results/v5/reports.zip` (8.4 MB). Five sections each: the original
graph in stage order with every evidence node's panels and image verdict; all of MatMech's
causality, spans included and labelled audit-only; how the traces were extracted, with the funnel
and the stitch hop by hop; how the traces merge with that causality, every link with its strength
and what confirmed it, and the confirmed chain drawn over the paper's own argument; and the final
traces with question, panels, proposition, limits, scoring target, depth, causal strength, key
status, every audit verdict beside the text it replaced, and dropped items with their reasons.

Verified: zero external references of any kind, balanced markup, five sections each, and *every
verdict is model against model* on every page.

For the 16 papers with no surviving item, sections 4 and 5 say where the pipeline stopped. For nine
of them the answer is the same and it is the central result of v5: **the hops attach to evidence and
then nothing joins them.**
