# Writer versus hand: ceramic twelve — run 1

Every verdict here is model against model: the writer is a Sonnet subagent (net-writer, no tools), the structural nets are code, and the reference is the hand-written fixture. No human checked any item.

| T | status | hidden target named (hand / writer) | grader node named (hand / writer) | numbers in key (hand / writer) | unsourced (writer) | answer_key_nodes (hand / writer) | verdict (hand / writer) |
|---|---|---|---|---|---|---|---|
| T1 | control | 1/1 / 1/1 | n/a / n/a | - / 2 | - | q18, r2 / r2 | survives (control) / survives (control) |
| T2 | closed | 0/1 / 1/1 | n/a / n/a | 1 / 1, 2, 3, 50, 100 | - | - / - | closed / closed |
| T3 | closed | 1/1 / 1/1 | n/a / n/a | 2 / 2, 50, 100 | - | - / - | closed / closed |
| T4 | open | 0/2 / 2/2 | n/a / n/a | 0, 2 / 0, 2, 20, 25 | - | - / q9, r10 | survives / survives |
| T5 | open | 1/2 / 2/2 | yes / yes | 0, 10, 15, 20, 25, 91.7, 94.9, 96.4, 97.6, 98.5 / 0, 2, 15, 20, 25, 91.8, 96.4, 98.5 | - | r10, r3 / q10, r3 | survives / flagged [leak] |
| T6 | open | 0/2 / 2/2 | n/a / n/a | - / 0, 20, 25 | - | - / q14, r10 | survives / survives |
| T7 | open | 0/1 / 1/1 | n/a / n/a | - / 2 | - | - / q15, s5 | survives / flagged [leak] |
| T8 | control | 1/1 / 1/1 | n/a / n/a | 20, 25 / 7, 20, 25 | 7 | q19, r9 / r9 | survives (control) / flagged (control) [provenance] |
| T9 | open | 2/2 / 2/2 | n/a / n/a | 2, 15, 20 / 1, 2, 15, 20 | - | q11, q15, r3, r8 / q11, q15 | survives / survives |
| T10 | open | 1/2 / 2/2 | n/a / n/a | - / 2 | - | - / q11, q15 | survives / survives |
| T11 | open | 1/1 / 1/1 | no / yes | 1, 2, 6.05, 15, 17.1, 20, 655 / 0, 1, 2, 4.3, 6.0, 6.05, 12.6, 15, 16.0, 17.1, 20, 25, 91.8, 96.4, 98.5, 505, 568, 655 | - | q17, r8 / q10, q17, r8 | survives / survives |
| T12 | closed | 1/1 / 1/1 | n/a / n/a | 30, 40, 1550 / 30, 40, 1550 | - | - / q5 | closed / closed |
