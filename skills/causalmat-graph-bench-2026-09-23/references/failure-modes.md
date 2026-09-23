# Failure modes

What went wrong in the reference run, how it was caught, and what it costs if you miss it. Several of
these are invisible in the output — the pipeline produces plausible numbers either way.

## Defects in the pipeline that produced wrong numbers

### Figure numbering: packet ids are positional, not the paper's

Packet id `F<n>` numbers figures by **position in `data.json` `image_info`**, not by `match.json`
`figure_number`, which repeats or skips when a paper has a scheme or an unnumbered figure. Code that
looked figures up by `figure_number` handed out the wrong crop.

Caught by a second read that disagreed with a node the staff had got right. Affected 9 of 32 papers in
one batch and 51 of 168 in another. The damage was mostly in the **cut**, not the check: wrong crops trip
the image-type and missing-crop rules and close traces that should have stayed open. Re-cutting reopened
6 traces.

Fix: `fig_by_number()` in `trace_kit/cut_traces.py`; use it everywhere a packet id resolves to an image.

### `passed_nets` counted closed traces

The row builder counted every validation entry without `fails`, and a *closed* trace has no fails. Over
80 papers it reported 266 where only 112 traces carried verdict `survives`. The funnel read
`written 127 → passed_nets 266`, which is impossible and went unnoticed until the columns were summed.

Fix: count `verdict == 'survives'`. **Sanity-check every funnel for monotonicity.**

### A staff-kept flag still gated the trace

After the panel judge rules a flag `real` and the staff subagent re-opens the panel and **keeps** the
node, the flag is resolved — staff looked at the image. But `graph_flags` filtered only on
`judge == 'real'` and never subtracted the kept set, and `apply_reread` returned stored graph-time flags
verbatim instead of recomputing. Two traces were scored `inspect / graph` **without ever reaching an
arm**.

Effect on the published numbers: inspect cause `graph` read 10 when it was 8; one valid item was missing.
Two of ten items attributed to "the graph misreads the panel" were a pipeline artifact.

Fix: exclude `kept` in `graph_flags`; recompute in `apply_reread` when the flags came from the graph
stage. **Audit: any trace with a `.gate.json.flagged` file and no arm reply deserves a look.**

### The export missed a seventh of the corpus

`export_items.py` walked `os.listdir(results/v07/papers)` — 97 directories for a 100-paper run, because
the 7 pilot papers keep their gate rows in `results/v07/pilot/gate.jsonl`. It exported 105 of 112 valid
items and reported success, because every check it ran was internally consistent.

Fix: walk the union of the directory listing and every paper in `batch.csv`, and **reconcile the export
against `batch.csv` by verdict** as a standing check.

## Defects in the items themselves

### The writer is the largest fixable defect — 16 of 55 inspect items

One shape dominates, seen on five separate papers: **the question puts a claim under test while the key
answers a caveat carried by an `audit` node that the claim never asserted.** An arm that reads the panel
correctly is scored wrong. Examples the inspector found:

- the question asks whether F10a's labelling bears out a claim, which it does; the key's negative hinge is
  the *absence* of a spinel FFT, a decay path that appears only in an audit node's note and never reaches
  the question, the claim or the context;
- the key rests on an unstated severity threshold for "far faster", and compares against the blank rather
  than either centre alone, which is what the claim asserts;
- the key depends on comparing a 9 °C peak-maximum separation to a ~100 °C peak width — a test the
  inspector judged unsound on its own terms, since TPD maxima locate far more precisely than FWHM;
- the question asks about a "20th versus 27th cycle" comparison where the panel is labelled 20th and 21st.

**Fix before scaling further.** Candidate rule for the writer prompt: the key may only assert what the
graded target node asserts; a caveat from an audit node may qualify an answer but may not be the hinge
unless the question names it.

### The cutter withholds what a cross-figure key needs — 5 items

When an audit node's text names a *second* figure, the item still hands over only the first. The key then
turns on a comparison the arm cannot make. Fix: add that panel to `given_panels`, or surface the
contradicted claim as a context bullet.

## The panel check's five false-positive classes

1,632 units → 214 flagged → 48 ruled real → **4 citation fixes**. The 44 the staff overturned fall into
five reproducible classes:

1. **Caption-borne identity.** The panel's sample or phase assignment lives in the caption, not on the
   image, so a blind single-crop reader cannot recover it. Nodes that already declare this in
   `attrs.requires_unseen` are the ones most likely to be flagged spuriously. *Fix: pass
   `requires_unseen` to the reader.*
2. **Composite panels.** Where a "panel" is a whole row — an SEM tile plus four EDX maps — the reader
   describes mostly the EDX tiles, so any SEM-only node citing that row is graded wrong by construction.
   *Fix: split composite rows into per-tile crops, or name the tile in the reader's prompt.*
3. **Similarly-named materials.** A node correctly noting that a figure lacks a `POD-M` arm was flagged
   because the reader found the `V-POD-M` arm.
4. **Legend misreads at crop resolution.** The reader read the curves right and the species labels wrong
   (`TFSI/DME` for the paper's `FSI/HFE/PP13`).
5. **The judge itself.** On one paper the panel judge claimed F5a was a different sample when its caption
   says it is the same pillar from Fig. 3e. On another, the blind reader misread a Jaynes-Cummings fit as
   a phonon-plasmon plot and **all three panel judges on that crop inherited the misreading** — the judge
   fails in a correlated way, not independently.

Class 5 is the reason the staff round exists. Do not drop it while the judge can be wrong in the same
direction three times.

## Environmental contamination

**An MCP server's instructions leaked into subagent tool-result streams.** 202 of 3,689 replies on disk
carry a note from the agent saying it saw an injected "create a document" instruction and ignored it. It
hit exactly the agents whose tool list includes `Read` — 13.2% of second reads, 4.7% of gate arms, 3.6%
of panel judges — and spared the text-only graders and writers entirely.

Every agent refused the instruction and answered the real question, so no verdict is known to be wrong.
But the note lands **in the reply text that a grader then reads**, and the second read is both the most
contaminated channel and the one already known to be imprecise.

Unresolved in the reference run. The options were: strip the note before grading and re-grade the
affected reads (recommended); re-run the reads (the leak is environmental and will recur); or record and
move on. **Check for this before trusting any grader-mediated number**, with a grep for the server's name
across `*.out.txt`.

## Operational

- **Relays alter prompts.** Three times in the reference run. Always `harvest`; never take a relay's
  account of its own work.
- **A relay died mid-batch** on a transient API safeguard error (`reasoning_extraction`) and lost 8 of 12
  jobs. Give relays a retry-once-then-skip rule and always diff the harvest against the job list.
- **`inspect_split.py` honours `V07_PAPERS`**; an earlier version had the path hard-coded and clobbered
  five before-run artefacts during an A/B comparison. Any helper that writes into a paper tree must read
  that variable.
- **Commit before the row exists** and the message summary comes out empty. Run `v07.py row <P>` first.
