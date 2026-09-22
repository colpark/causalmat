# v07 fix 2: the blind read screens, the panel judge decides

Every verdict is model against model.

## What changed
- A reread flag no longer sends a trace to inspect by itself, and no longer asks staff to change `panel_ids`.
- Every WRONG unit goes to **`net-panel-judge`** (`.claude/agents/net-panel-judge.md`, Read and nothing else). It opens
  the cited crop and rules `real` (the crop does not describe the node, naming what the crop shows) or `ok`.
- Only `real` flags the trace (cause `graph`) and writes the citation into the paper's staff fix packet.
- Driver: `v07.py pjudge` builds one job per WRONG unit, `v07.py pjapply` applies the rulings, and per-trace flags now
  follow the judge alone, not the blind read and not the staff round.

## Result on every existing flag
All 121 graph-time flags on the 45 papers that had any were re-ruled (the run had grown past the 62 in the prompt:
80 papers, 1063 panel checks, 132 flags counting the 13 per-trace flags of the first 32 papers).

| | |
|---|---|
| panel checks | 1063 |
| flags (WRONG units) | 121 graph-time (132 with the first 32 papers' per-trace flags) |
| panel judge `real` | **27** |
| panel judge `ok` | 94 |
| **precision** | **27/121 = 22%** |

- **Traces returning from inspect to the gate: 0.** The staff round that the judge replaces had already cleared those
  flags paper by paper, so the traces had already been gated. Under the new pipeline the staff round is gone and the
  judge does that work in one dispatch instead of a staff agent opening the same figure.
- **Traces newly sent to inspect: 0.** Of the 27 real flags, only one node (Acta 2021.116710 `a1`/`o11`) is evidence of
  an open trace, and that trace was already inspect.
- The 27 real citations are queued in each paper's `rrgraph/fix.md`. They are **not applied yet**: part 5 compares
  before and after on the same graphs, so changing graphs first would confound it.
- The stop rule (fewer than 3 real) does not fire: the judge finds 27, so the screen keeps earning its dispatches.

## What the judge overturns
The judge disagrees with the staff round often: many units staff kept ("the reader misread it") the judge rules real,
because it asks a narrower question. Staff asked whether the node is defensible; the judge asks whether **this crop**
shows what the node says. Examples: a node citing a wear-volume bar chart for a weld-pool current claim; a Raman
waterfall whose trend runs opposite to the node; an EBSD orientation map cited for a micrograph claim.

One ruling (`Biomaterials 2010.02.024 o6.F2c`) was dispatched directly after two relays altered its prompt, and my
paste differed from the file by one character (`cm-1` for `cm⁻¹`). It is recorded in `reread.json` as
`judge_prompt_exact: false`. Its ruling was `ok`.

`batch.csv` now carries `reread_flags`, `paneljudge_real` and `paneljudge_precision` per paper.
