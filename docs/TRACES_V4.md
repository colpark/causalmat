# Traces v4: causal traces with a real dependency

Generation only. No arms, no scoring, no removal — this is what a trace looks like once causality is
built in, and what its reasoning reads like.

**Every verdict is model against model.** It is said on every page.

Six traces, 14 steps, built from the links the graph check confirmed. MatMech supplies which
stretches of the spine are causal steps; our graph supplies every word a solver sees. MatMech hop
ids, stage types and figure links are recorded as provenance and are marked on each page as never
shown to a solver. A leak check over every solver-visible field and over the six rendered pages
finds **zero** MatMech spans and zero previous-step answers stated outright.

## How many steps carry a real dependency

Six of the 14 steps are first steps and have no predecessor. Of the **8 steps that have one**:

| dependency | n | which |
|---|---|---|
| **real** | 4 | Acta step 2, adfm step 2, Biomaterials M1→M3→M4 step 2, Biomaterials M2→M4 step 2 |
| **none** | 4 | Acta step 3, Nano Letters step 2, Biomaterials M1→M3→M4 step 3 *(restatement)*, Rare Metals step 2 *(restatement)* |

**The stop rule did not fire, but only just.** It fires on *more* than half; this is exactly half.
That is close enough that it should be read as a warning rather than a pass: on these five papers,
a confirmed causal link produces a reasoning dependency about half the time.

Counting matters here and is stated rather than buried. Had the six first steps been counted as
`none`, the total would be 10 of 14 and the rule would have fired — on an artefact, since a first
step has no predecessor to depend on. The denominator is the 8 steps that could have a dependency.

**Two of the four `none` are restatements**, decided structurally before any model was asked:
the step lands only on claims its predecessor already established — `n12, n16` in Biomaterials
M1→M3→M4 step 3, `s6` in Rare Metals step 2. A step that establishes nothing new cannot depend on
its input because it does not advance the argument. These are a defect in the chain, not a judgement
about the reasoning.

**The other two are genuine stand-alones.** Nano Letters step 2 reads the cycling and voltage-profile
data in F2a–F2d directly, without needing the pore-size and isotherm characterisation from step 1.
Acta step 3 measures tensile ductility by kinking along [0001] — a different loading orientation from
step 2's compression, and interpretable on its own.

**The pattern is positional.** Every first transition (step 2 of a chain) carries a real dependency;
both third steps do not. On this evidence the causal chain is real for one hop and then flattens.

## What the reference reasoning adds that v3b lacked

v3b produced a ruling — correct, partly correct, wrong, cannot tell — and nothing that could be
read. v4 produces the reasoning itself, in five parts per step, with **the node id on every
sentence** and unsourced sentences marked `writer inference` so an assumption is visible rather than
blended into the evidence.

Four things are now on the page that v3b had nowhere to put:

- **the assumption the inference needs**, which v3b never asked for and which is where the real
  weakness sits. Acta step 2: *"the yield stresses measured on these crystals are attributable to
  the LPSO nanoplate microstructure identified and sized in step 1, rather than to some unrelated
  compositional difference."* That is the load-bearing assumption of the whole chain and it is not
  in any panel.
- **what remains open**, per step.
- **what is handed to the next step**, which is what the arrow on the page is labelled with, so the
  dependency is a visible object rather than an inference about the design.
- **the end-to-end reasoning and a named weakest step**, per trace.

## Three steps that now require their predecessor

**Acta Materialia, step 2** — *"Taking the phase you identified and the feature sizes you measured in
step 1 as given, what does the evidence below show about the mechanical property?"* The compression
data gives yield stresses at three heat treatments. Those numbers only become a statement about LPSO
nanoplates because step 1 identified the planar defects as nanoplates and measured their density and
thickness. Without it the step reports three numbers and attributes them to nothing.

**Advanced Functional Materials, step 2** — the writer's own words: *"the PC/HOC/SC ordering of
emission complexity is read as tracking the same PC/HOC/SC ordering of domain size established in
step 1, so that the smallest-domain sample is the one showing the dual peak."* The emission spectra
rank three samples. Turning a ranking of samples into a relationship with domain size needs step 1's
ordering, and nothing in the PL evidence supplies it.

**Biomaterials M2→M4, step 2** — *"Panel F9's HIF-1α band differences and panel F11b's survival curve
are only interpretable as confirming and extending the mechanism from step 1."* The western blot
shows a stronger band for 5Co-MBG; the survival curve declines. Reading either as evidence about a
hypoxia-mimicking pathway requires step 1's Co²⁺ release measurement and the mechanism it supports.

## The pages

`results/v4/pages/<trace>.html`, one self-contained file each, panels embedded as data URIs, zipped
to `results/v4/pages.zip` (1.2 MB). Four tabs: **the trace** (question as the solver sees it, panels
inline, reference reasoning with node ids, the hidden effect, and an arrow between steps labelled
with the proposition passed along and the dependency verdict); **whole graph** (the paper's argument
graph as a layered SVG with the trace's claims and edges highlighted, each labelled with its hop and
stage type); **before causality** (v2, v3b and v4 on the same claims, side by side); and
**provenance** (hop ids, stage types and figures, marked audit-only).

The layout follows `trace_kit_v2/paper_page.py`. The brief refers to `build_v2_pages.py`, which does
not exist in this repo. All six pages were checked for the div-balance fault that broke the v2 pages:
every one balances, with all four tabpanels at equal depth.

## Notes on the build

Three links join at **stage level only** — Acta M2→M3, adfm M1→M2, Nano Letters M1→M2. The hop link
was confirmed, but there is no spine edge or shared claim between those two steps' landing claims
specifically. Recorded as `stage only` rather than upgraded. Two of the three are also the steps that
came back `dependency: none`, which is consistent: where the graph could not join the claims, the
reasoning did not need to either.

Two writer replies did not parse on the first pass and were nearly recorded as `unjudged`, which
would have put the stop rule at 5 of 8 and fired it. Both plainly contained their judgement: one
reply held two JSON objects, so a greedy match spanned both; the other was malformed mid-string. The
parser now walks balanced objects and, failing that, recovers the decision by regex. A judgement the
model made should not be lost to a bracket.
