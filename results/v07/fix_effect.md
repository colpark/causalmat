# v07: did the fixes help

Every verdict is model against model.

The same 20 papers, run end to end twice. The graphs are the ones the staff and judge already built; only the cutter,
the writer, the nets, the panel check and the gate differ. Set: the 9 papers the figure-numbering lookup touched plus
11 drawn at random from the first 56, **seed 20260922** (`results/v07/fix_effect_set.json`). The after-run wrote to
`results/v07/fix_effect/` through the `V07_PAPERS` root, so the before data is untouched.

| metric | before | after |
|---|---|---|
| traces cut, open, written | 67, 31, 31 | 67, 31, 31 |
| valid, of which partial | **20**, 6 | **24**, 10 |
| text-sufficient | 0 | 0 |
| inspect, by cause | 9 (solver 6, writer 1, cutter 2) | 7 (solver 5, writer 2) |
| items blocked by `scope` | 0 | 0 |
| papers with zero valid | 10 | 9 |
| panel checks | 278 | 454 |
| reread flags, panel-judge real, precision | 27, 3, 11% | 44, 5, 11% |
| dispatches per paper | 22.9 | 42.2 |
| wall minutes per paper | 159.5 | 84.2 |

## What moved

- **Valid per paper rose: 1.0 to 1.2** (20 to 24 items on the same 31 written items).
- **The inspect rate fell: 31% to 23%** (9 to 7 of the gate items).
- Papers with no valid item: 10 to 9.
- The cut is unchanged (67 traces, 31 open, 31 written), so the gain is in the items, not in what survives the cutter.
- **No item was blocked by `scope`.** One item failed the scope net on the first pass and its single rewrite fixed it,
  which is the rule working as intended, far from the quarter that would have stopped the run.
- Partial valids rose from 6 to 10: more items are now graded CORRECT on part of an order or
  mechanism rather than failing outright.
- **No inspect item is a graph or cutter fault any more.** Before: solver 6, writer 1, cutter 2. After: solver 5,
  writer 2. Both remaining writer faults are the same shape, a key that rules on something the question does not ask
  (the out-of-range series in AFM 202005640 T2, the 3 kPa plateau in Adv Mater 201702037 T3).
- The panel check is wider and cheaper per flag: 454 checks against 278, because it
  now reads every cited panel of every node at graph time rather than the given panels of open traces.
  The panel judge ruled 5 of 44 flags real.

## Cost

Dispatches per paper rose from 22.9 to 42.2. The after-run pays for
the wider panel check (454 reads and grades) and the panel judge, and saves the staff fix round.
It does not include the staff and judge dispatches that built the graphs, since the comparison reuses them; the before
figure does include them, so the true gap is wider than the table shows. Wall minutes per paper fell from
159.5 to 84.2, but both are wall-clock spans over a shared queue and say more about how many
relays were running than about the work itself.

## Decision

**Valid per paper is higher (1.0 to 1.2) and the inspect rate is lower (31% to 23%), so the condition to
continue Part C is met.** The remaining failures are solver misreads and two question/key scope mismatches of the kind
`asks_for` is meant to catch; neither points back at the cutter, the panel check or the graph.
