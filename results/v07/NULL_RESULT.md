# v07 fix 4: forced difference

Every verdict is model against model.

**The claim reproduces.** The earlier scan missed it because the directive is not in the question text: it is the
trace's `answer_format`, which `gate_packets.py` appends to the question when it builds the arm prompt. The block-2
inspector named two items, and both are real:

| item | question | key | format before |
|---|---|---|---|
| Bioactive 2020.01.001 T1 | how does the nanorod morphology compare between the two coatings? | "no visible difference in rod shape between the two coatings" | state the difference between the two conditions; do not rank |
| J Adv Ceram 0538-2 T3 | how does the sample's condition compare between the two panels? | "its condition appears the same in both panels - nothing visibly different" | same |

**The fix** (`cut_traces.py`, the compare subtype): the format now follows the key's shape and always allows the two
answers a negative key needs.

> state how the two conditions compare, including if they look the same; do not rank. Answer "no visible difference"
> when they look the same, or "cannot determine" when the panels cannot settle it.

Both items are tagged `null_result: true` in the cut, the written record, the gate packet and the gate row, and both
were re-run through the arms and the grader.

| | before | after |
|---|---|---|
| Bioactive 2020.01.001 T1 | inspect (writer) | **valid** (full arm CORRECT, floor ABSTAIN) |
| J Adv Ceram 0538-2 T3 | inspect (writer) | **valid** (full arm CORRECT, floor ABSTAIN) |

**Null-result accuracy, reported separately: 2 of 2 valid.** An item whose true answer is "these look the same" is
worth keeping: both need the images (the floor arm abstains in each case), and both are now answerable as written.
Old prompts and replies are kept as `.pre_fix4`.
