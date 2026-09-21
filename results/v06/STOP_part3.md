# v06 pilot stopped after part 3: stop rule 2

Every verdict here is model against model; no human checked any item.

**Stop rule 2 fired:** 14 of 26 hidden targets (54%) have `source` other than `figure` (text 10, inferred 4). Cutter v2
on the eight judged v06 graphs gives 21 traces: 0 open, 6 control, 15 closed (8 by rule 3 "not derivable from given
panels", 5 by the v1 bare-infer rule, 2 generate with no oracle). Parts 4-6 were not run.

What drives it (from results/v06/cut/*.traces.json and the graphs):
1. **Caption-only condition labels.** 9 of the 10 `text` targets need a fact from the caption: which panel is which
   sample or condition ("panel a = pristine MOF, panel b = NixPyOz", "F1b = Al-Cu-Mn-Sm", "after 500 cycles"). The
   rule counts that as unseen, although the question-only packet could hand the caption span with each panel.
2. **Inferred claims as graded targets.** Infer traces grade the observation and its claim; the claim is usually
   `inferred` from the observation (Acta a10, AFM s2, Adv Mater s2), and every mechanism is `inferred`.
3. **Captions-only packets.** No full text was fetchable (no Elsevier or Springer key on the host; four papers are
   Wiley), so staff had no body text and marked text-dependent claims `text` or `inferred`.
4. Yield is also cut before rule 3 runs: every multi-cause claim is `joint` (18 of 18), so rule 1 removes all
   competing-causes traces, and with denser evidence (v06 cites more panels) few FM nodes are `necessary`, so the
   v1 seeding rule makes about one infer trace per paper.
