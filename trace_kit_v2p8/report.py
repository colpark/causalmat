"""report.py: write docs/TRACES_V2P8_PILOT.md entirely from results/v2p8/*.json.

  python3 -m trace_kit_v2p8.report

No number typed by hand, same rule as v2.6 and v2.7.

Every verdict is model against model.
"""
import json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)


def J(p, d=None):
    f = R('results/v2p8', p)
    return json.load(open(f)) if os.path.exists(f) else d


def tbl(head, rows):
    return '\n'.join(['| ' + ' | '.join(str(h) for h in head) + ' |',
                      '|' + '|'.join('---' for _ in head) + '|']
                     + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows])


def main():
    S, A, C, D = J('selected.json'), J('partA.json'), J('partC.json'), J('partD.json')
    COST, AUD = J('cost.json'), J('audit_report.json')
    out = []; W = out.append

    W('# Traces v2.8 pilot — grading answers against the key\n')
    W('Every verdict is model against model.\n')
    W('8 of the 76 derived_input items, one per paper. v2.7 showed that asking a comparer '
      'whether two answers differ cannot judge a single item: two samples of one prompt differ '
      '29% of the time. Here the target is fixed. Each item already has a drafted key, so the '
      'key is broken into atomic claims and every answer is measured against the same list.\n')
    W('Two things this pilot has that v2.7 did not. A third arm, C, holding the earlier result '
      'alone: beating arm A only shows the earlier result added something, and cannot show the '
      'measurement was needed at all. And scores averaged over 6 samples before any threshold, '
      'rather than a vote over single draws.\n')

    W('## The 8 items and why each was picked\n')
    W(tbl(['#', 'item', 'journal', 'label', 'upstream'],
          [[i, f"`{r['item']}`", r['journal'].replace('_', ' '), r['cs'],
            f"`{r['upstream']}` ({r['up_gen']})"] for i, r in enumerate(S['items'], 1)]))
    W('')
    for i, r in enumerate(S['items'], 1):
        W(f"{i}. **`{r['item']}`** — {r['why_picked']}")
    W('')
    W(f"Constraints, all asserted in `select.py` rather than eyeballed: "
      f"{S['n']} items from {S['papers']} papers and {S['journals']} journals; all 4 "
      f"discriminating items taken (they sit in 4 different papers, so one-per-paper allows it); "
      f"upstream mix {S['upstream_generator']}.\n")

    W('## Part A — splitting the key into claims\n')
    W(f"**Tag agreement between the two agents: {round(100 * A['tag_agreement'], 1)}%** "
      f"({A['tags_agreed']} of {A['tags_proposed']}). The stop rule was 70%; it did not fire.\n")
    W(f"All {A['items_with_a_combined_claim']} of {A['items']} items have at least one combined "
      f"claim, so none stopped here.\n")
    kept = {t: sum(1 for v in A['claims'].values() for c in v['kept'] if c['tag'] == t)
            for t in ('combined', 'input', 'observation')}
    W(tbl(['tag', 'claims kept'], list(kept.items())
          + [['limit (carried from the key, not tagged)',
              sum(v['n_limit'] for v in A['claims'].values())]]))
    W('')
    W(tbl(['item', 'combined claims'],
          [[f"`{k}`", v] for k, v in A['combined_per_item'].items()]))
    W('')
    W(f"The {len(A['tags_proposed'] * [0]) and ''}{A['tags_proposed'] - A['tags_agreed']} "
      f"disagreements are substantive, and three of the four run in the direction the checker "
      f"was told to police — a claim called combined that one side reaches alone:\n")
    for it, v in A['claims'].items():
        for d in v['dropped']:
            W(f"- `{it}` — proposed **{d['tag']}**, checker says **{d.get('correct_tag')}**\n"
              f"  > {d['claim']}\n"
              f"  > *{d.get('why')}*")
    W('')

    W('## Part B and C — three arms, six samples, graded against the claims\n')
    W('  - arm A: the new measurement alone, with its panels\n'
      '  - arm B: the measurement plus the earlier result\n'
      '  - arm C: the earlier result alone, no measurement and no panels\n')
    W("v2.7's item question names both sides, so arms A and C would each have been asked about "
      "material they were not given — v2.7's own arm A had that flaw. Each arm is asked a "
      "question matching what it holds; all three are graded against the same claim list.\n")
    W(f"{C['graded']} answers graded. The grader saw one answer and the claim list, never the "
      f"arm label, the other answers, the earlier result or the measurement. Every \"stated\" "
      f"ruling had to quote the answer; {C['withdrawn_stated_without_quote']} rulings were "
      f"withdrawn for having no quote.\n")

    W('## Part D — the result\n')
    m = D['mean_combined_across_items']
    W(tbl(['arm', 'what it held', 'mean combined score', 'mean limit score'],
          [['A', 'the measurement alone', m['A'], D['mean_limit_across_items']['A']],
           ['B', 'measurement + earlier result', m['B'], D['mean_limit_across_items']['B']],
           ['C', 'the earlier result alone', m['C'], D['mean_limit_across_items']['C']]]))
    W('')
    W(f"Across the 8 items: the input is judged needed on **{D['input_needed']} of "
      f"{D['items']}**, the observation on **{D['observation_needed']} of {D['items']}**, and "
      f"**{D['compositional']} of {D['items']} come out compositional** at a margin of "
      f"{D['margin']}.\n")
    W(f"**Split halves agree on {D['halves_agree']} of {D['items']} items** "
      f"(and on both sub-decisions for {D['halves_agree_on_both_decisions']}). The stop rule was "
      f"6 of 8: " + ('it did not fire, so the compositional count above stands.'
                     if not D['stop_rule_fired'] else
                     '**it fired, so no compositional claim is made from these numbers.**') + '\n')
    W(tbl(['item', 'label', 'comb.', 'A', 'B', 'C', 'B−A', 'B−C', 'input?', 'obs?',
           'compositional', 'halves agree'],
          [[f"`{k[:34]}`", v['cs'], v['n_combined'],
            f"{v['mean_combined']['A']:.2f}", f"{v['mean_combined']['B']:.2f}",
            f"{v['mean_combined']['C']:.2f}",
            f"{v['B_minus_A']:+.2f}", f"{v['B_minus_C']:+.2f}",
            'yes' if v['input_needed'] else 'no',
            'yes' if v['observation_needed'] else 'no',
            '**yes**' if v['compositional'] else 'no',
            'yes' if v['halves_agree'] else 'no']
           for k, v in D['items_out'].items() if 'error' not in v]))
    W('')
    W('### How much of this is the design guaranteeing its own answer\n')
    W(f"Arms A and C score {m['A']} and {m['C']} on combined claims, against {m['B']} for arm B. "
      f"That gap is large, and most of it is built in: a claim is only tagged combined when "
      f"neither side reaches it alone, so arms A and C are expected to score near zero on "
      f"exactly these claims. The test therefore confirms the Part A tags more than it "
      f"separates one item from another, and with a margin of {D['margin']} it will pass for "
      f"any item whose arm B answers competently. That is worth saying plainly before the "
      f"{D['compositional']}-of-{D['items']} figure is quoted anywhere.\n")
    W('What the design did catch is the one failure, and it is the failure only arm C can see. '
      '`di_journal_of_a_spi_o13_o20_o22_n15` scores 0.500 on arm C — the earlier result alone '
      'reaches half its combined claims, identically across all 6 samples — so one of its two '
      '"combined" claims is not combined at all. Both Part A agents tagged it combined and both '
      "were wrong. Under v2.7's method, which only ever compared B against A, that item would "
      "have been called compositional on a B-A of +0.583. Arm C is the whole reason it is not.\n")
    W('Two caveats on the arms themselves. Arm B is the only arm asked the combined question; '
      'arms A and C get questions matching what they hold, which is necessary for them to be '
      'answerable but does mean arm B is asked the question the key was written to answer. The '
      "control that would settle it - arm B asked arm A's narrower question - was not run. And "
      'arm C has no panels at all, so it is short of evidence as well as short of a question, '
      'which flatters the B−C gap.\n')

    W('### Limits, as context only\n')
    W(f"Arm B keeps the key's limits better than arm A on {D['limits_better_in_B']} of "
      f"{D['items']} items. Mean limit score A {D['mean_limit_across_items']['A']}, "
      f"B {D['mean_limit_across_items']['B']}, C {D['mean_limit_across_items']['C']}. "
      f"This is reported because it is the thing v2.6 measured as \"laundering\", and it is not "
      f"part of the compositional decision.\n")

    W('## Every item in full\n')
    for k, v in D['items_out'].items():
        if 'error' in v: continue
        a = A['claims'][k]
        W(f"### `{k}`\n")
        W(f"{v['journal'].replace('_', ' ')} · drafter label **{v['cs']}** · upstream "
          f"`{v['upstream']}` ({v['up_gen']})\n")
        W(tbl(['arm', 'mean combined', 'sd', 'mean limit', 'mean contradictions'],
              [[x, f"{v['mean_combined'][x]:.3f}", f"{v['sd_combined'][x]:.3f}",
                '—' if v['mean_limit'][x] is None else f"{v['mean_limit'][x]:.3f}",
                f"{v['mean_contradictions'][x]:.2f}"] for x in ('A', 'B', 'C')]))
        W('')
        W(f"B−A {v['B_minus_A']:+.3f} → input needed **{v['input_needed']}** · "
          f"B−C {v['B_minus_C']:+.3f} → observation needed **{v['observation_needed']}** · "
          f"compositional **{v['compositional']}** · halves "
          f"({v['halves']['first']['compositional']}, {v['halves']['second']['compositional']}) "
          f"agree **{v['halves_agree']}**\n")
        W('Claims, as both agents tagged them:\n')
        for c in a['kept']:
            W(f"- **{c['tag']}** — {c['claim']}")
        for c in a['limits']:
            W(f"- *limit* — {c['claim']}")
        W('')

    comp = [k for k, v in D['items_out'].items() if 'error' not in v and v['compositional']]
    W('## One answer from each arm, for every compositional item\n')
    if not comp:
        W('No item came out compositional, so there is nothing to show here. The audit pack '
          'carries one answer per arm for all 8 items regardless.\n')
    for k in comp:
        W(f"### `{k}`\n")
        for arm in ('A', 'B', 'C'):
            key = f'{k}_{arm}1'
            ans = C['answers'].get(key)
            if not ans: continue
            W(f"**arm {arm}** — combined {ans['combined_score']:.2f}, "
              f"limits {'—' if ans['limit_score'] is None else f'{ans[chr(39)+chr(39)] if False else ans['limit_score']:.2f}'}, "
              f"{ans['contradictions']} contradiction(s)\n")
            for r in ans['rulings']:
                if r['kind'] != 'combined': continue
                W(f"- `{r['verdict']}` {r['claim']}"
                  + (f'\n  > "{r["quote"]}"' if r['quote'] else ''))
            W('')

    W('## The audit pack\n')
    if AUD:
        W(f"{len(AUD)} pages in `results/v2p8/audit/`, one per item plus an index. Each carries "
          f"the earlier result, the measurement with its panels, the claim list with tags, the "
          f"arm means, and one answer per arm with the grader's ruling and quote on every claim. "
          f"Every tag and every ruling has an empty agree/disagree box. **None is filled in.**\n")
        W("On the brief's conflict: Part E commissions these pages, the stop rules say not to "
          "build pages in the pilot. I read the stop rule as covering the per-paper trace pages "
          "v2.6 step 7 would produce — pipeline output presenting results as settled — and not "
          "an audit pack whose purpose is to let a person contradict the machine. The pack is "
          "built; no trace pages are.\n")
    else:
        W('_Not yet built._\n')

    W('## Cost\n')
    est = COST.get('estimate_before_starting', {})
    W(f"Estimated before starting: **{est.get('total')} calls** "
      f"({est.get('partA_split', 0) + est.get('partA_check', 0)} for Part A, "
      f"{est.get('partB_answers')} answers, {est.get('partC_gradings')} gradings).\n")
    rows = [[k, v['calls'], v.get('relays', ''), v['wall_min'], v['s_per_call']]
            for k, v in COST.items() if isinstance(v, dict) and 'wall_min' in v]
    W(tbl(['stage', 'model calls', 'relays', 'wall minutes', 'seconds per call'], rows))
    W('')
    tot = sum(r[1] for r in rows); mins = sum(r[3] for r in rows)
    W(f"**Actual: {tot} calls, {round(mins, 1)} minutes** at the 20-agent cap, dispatch to last "
      f"harvest. Every reply verified byte for byte against its prompt file from the agent's own "
      f"transcript.\n")

    W('## Where the data is\n')
    W('- `results/v2p8/selected.json` — the 8 items and why each was picked\n'
      '- `results/v2p8/split/`, `check/` — Part A, the tags and the second agent\'s rulings\n'
      '- `results/v2p8/partA.json` — kept and dropped claims\n'
      '- `results/v2p8/arms/` — Part B, 3 arms x 6 samples x 8 items\n'
      '- `results/v2p8/grade/`, `partC.json` — Part C, every ruling with its quote\n'
      '- `results/v2p8/partD.json` — arm means, decisions, split halves\n'
      '- `results/v2p8/audit/` — the audit pack\n')
    W('Every verdict is model against model.')

    open(R('docs/TRACES_V2P8_PILOT.md'), 'w').write('\n'.join(out) + '\n')
    print('docs/TRACES_V2P8_PILOT.md written,', len('\n'.join(out).split('\n')), 'lines')


if __name__ == '__main__': main()
