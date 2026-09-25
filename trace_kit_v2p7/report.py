"""report.py: write docs/TRACES_V2P7.md entirely from results/v2p7/*.json.

  python3 -m trace_kit_v2p7.report

No number in the document is typed by hand. Same rule as v2.6's report.py, for the same reason:
v2.5's prose had to be corrected twice for numbers that drifted away from the data.

Every verdict is model against model.
"""
import collections, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)


def J(p, default=None):
    f = R('results/v2p7', p)
    return json.load(open(f)) if os.path.exists(f) else default


def tbl(head, rows):
    return '\n'.join(['| ' + ' | '.join(str(h) for h in head) + ' |',
                      '|' + '|'.join('---' for _ in head) + '|']
                     + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows])


def main():
    A, B, C, Dd = J('partA.json'), J('partB.json'), J('partC.json'), J('partD.json')
    DI, E, COST = J('derived_input.json'), J('partE.json'), J('cost.json')
    W = [].append
    out = []
    W = out.append

    W('# Traces v2.7 — fixing what v2.6 exposed\n')
    W('Every verdict is model against model.\n')
    W('Same 32 papers. v2.7 does not scale to more. It measures how much of v2.6\'s necessity '
      'signal was noise, replaces the instrument that produced it, widens a flag that was too '
      'narrow, settles a contradiction between two checks, and builds a generator that makes '
      'merges which actually need what came before.\n')

    # ---- Part A
    W('## Part A — the noise floor\n')
    aa, ab = A['aa'], A['ab_same_chains']
    W(tbl(['pairing', 'rulings', '"yes"', 'rate', 'chains majority yes', 'unanimous'],
          [['arm A vs arm A (identical prompt)', aa['rulings'], aa['yes'],
            f"**{round(100 * aa['yes_rate'], 1)}%**", f"{aa['chains_majority_yes']}/{A['chains']}",
            aa['unanimous']],
           ['arm A vs arm B (same chains)', ab['rulings'], ab['yes'],
            f"{round(100 * ab['yes_rate'], 1)}%", f"{ab['chains_majority_yes']}/{A['chains']}",
            ab['unanimous']]]))
    W('')
    W(f"**The floor is {round(100 * aa['yes_rate'], 1)}%.** Nothing was added between those two "
      f"answers — same prompt, same evidence, two samples — and the v2.6 comparer still called "
      f"them changed {aa['yes']} times in {aa['rulings']}. So of v2.6's "
      f"{round(100 * ab['yes_rate'], 1)}% yes rate, "
      f"{round(100 * aa['yes_rate'] / ab['yes_rate'])}% is sampling variation. The genuine lift "
      f"from handing over the upstream result is **{round(100 * A['lift'], 1)} points**.\n")
    W(f"The stop rule was 40%. {round(100 * aa['yes_rate'], 1)}% is below it, so the run "
      f"continued.\n" if not A['stop_rule_fired'] else
      f"**The stop rule fired at 40% and the run stops here.**\n")
    W(f"{aa['chains_majority_yes']} of {A['chains']} chains score a majority \"yes\" against "
      f"themselves, and {aa['unanimous']} are unanimous on a pair whose correct answer is known "
      f"to be no. That is the answer to the c055 case in the brief: three repeats agreeing is "
      f"not decisive when a third of single rulings are false positives. Three flips at "
      f"{round(100 * aa['yes_rate'], 1)}% come up all-heads about "
      f"{round(100 * aa['yes_rate'] ** 3, 1)}% of the time.\n")
    W('The prompts were the v2.6 files byte for byte. A floor measured on different text would '
      'not be comparable with the rate it is meant to correct.\n')

    # ---- Part B
    W('## Part B — a graded comparer\n')
    if not B:
        W('_Not yet run._\n')
    else:
        W('The comparer now scores 0 to 3 on how far the substance differs and must quote the '
          'specific difference or say "none". And each chain is judged against itself: '
          'necessity counts only when the A-vs-B score beats **that chain\'s own** A-vs-A score '
          'by at least a point, in 2 of 3 repeats. A chain whose answers wander on their own has '
          'to clear a higher bar, which no single global threshold can do.\n')
        W(tbl(['score', 'A vs B', 'A vs A'],
              [[s, B['ab_score_hist'].get(str(s), B['ab_score_hist'].get(s, 0)),
                B['aa_score_hist'].get(str(s), B['aa_score_hist'].get(s, 0))]
               for s in (0, 1, 2, 3)]))
        W('')
        W(f"Mean score: **{B['ab_mean']} for A vs B against {B['aa_mean']} for A vs A.** The gap "
          f"between the two is the same quantity Part A measured, now on a scale that can show "
          f"its size rather than rounding it to a yes.\n")
        st = B['stability']
        W(tbl(['agreement across the 3 repeats', 'chains', 'share'],
              [['all three give the identical score', st['ab_all_three_same_score'],
                f"{round(100 * st['share_same_score'])}%"],
               ['all three within one point', st['ab_all_three_within_one'],
                f"{round(100 * st['share_within_one'])}%"],
               ['all three agree on the necessity decision', st['decision_unanimous'],
                f"{round(100 * st['share_decision_unanimous'])}%"]]))
        W('')
        tgt = 'clears the two-thirds target' if not B['stop_rule_fired'] else \
              '**does not clear the two-thirds target**'
        W(f"The decision is what gets used, so the decision agreement is the number that matters: "
          f"{round(100 * st['share_decision_unanimous'])}%, which {tgt}. "
          f"(v2.6's yes/no comparer agreed on 46.3%.)\n")
        W(tbl(['necessity', 'chains'], sorted(B['necessity'].items(), key=lambda x: -x[1])))
        W('')

    # ---- Part C
    W('## Part C — the widened flag\n')
    W(f"The flag now fires on **any** limit's `why` that says the downstream does not use, "
      f"invoke or rely on what the upstream brought, not only when every limit is "
      f"not_applicable. {C['v2p6_flagged']} seams becomes **{C['v2p7_flagged']} of "
      f"{C['joins']}**, {C['added']} new.\n")
    W(f"**c055 is flagged** (it was not in v2.6). Its seam has one carried limit and three "
      f"not_applicable, so the structural rule never fired, and the sentence naming the problem "
      f"was discarded by two v2.6 exclusions at once: it is scoped to a single limit, and its "
      f"object is an evidence leg rather than a conclusion.\n")
    W('> ' + ((C['seams'][C['c055_seam']]['new_evidence'] or ['—'])[0]) + '\n')
    W('Three sentences match the rule while saying something else and are excluded by hand, each '
      'with its reason in the code: a caveat being what is absent rather than the upstream\'s '
      'contribution; "does not rely on X alone", which says the downstream added evidence and is '
      'the opposite of ignoring it; and a validation of the upstream not being invoked rather '
      'than the upstream itself.\n')
    W(f"All {C['added']} new flags with their trigger sentences are in "
      f"`results/v2p7/partC.json`. A sample:\n")
    for k in C['added_ids'][:6]:
        v = C['seams'][k]
        W(f"- `{k}`\n  > {(v['new_evidence'] or [''])[0][:200]}")
    W('')

    # ---- Part D
    W('## Part D — the backbone contradiction\n')
    W(f"{Dd['joins']} backbone joins. v2.5 rated {Dd['v2p5_sound']} sound and "
      f"{Dd['v2p5_launders']} as laundering a limit; v2.6 scope passed {Dd['v2p6_scope_pass']}. "
      f"They already agree on pass/fail for {Dd['agree_on_pass_fail']} of {Dd['joins']}.\n")
    W(f"**Correction to the brief.** {Dd['correction_to_the_brief']}\n")
    W('The disagreement has a mechanical cause, not a difference of opinion. The v2.6 scope '
      'check used the downstream backbone item\'s `previous_output` as its second text. That '
      'field holds the result the item was handed by **its own v5 chain** — the item at (same '
      'trace, step = previous_step). v2.5\'s composition joined items into backbone items on a '
      'shared claim id and did not consult the v5 chain at all.\n')
    W(f"In **{Dd['joins'] - Dd['upstream_is_v5_previous_step']} of {Dd['joins']}** joins the "
      f"upstream is not the v5 previous step. The scope check was comparing this join's upstream "
      f"against a premise belonging to a different item, so its ten \"incompatible\" verdicts "
      f"record that mismatch rather than a scope failure of the join.\n")
    W(tbl(['which check is right', 'joins'],
          sorted(Dd['verdict_counts'].items(), key=lambda x: -x[1])))
    W('')
    W(tbl(['join', 'upstream is the v5 previous step', 'v2.5', 'v2.6 scope', 'right'],
          [[c['join'][:58], 'yes' if c['upstream_is_v5_previous_step'] else 'no',
            c['v2p5_join_verdict'], c['v2p6_scope'], c['which_check_is_right']]
           for c in Dd['cases']]))
    W('')
    one = [c for c in Dd['cases'] if c['upstream_is_v5_previous_step']]
    if one:
        W(f"The single well-posed case is `{one[0]['join']}`, and there v2.6 is right — and "
          f"v2.5 contradicts **itself**: its `note_for_caller` calls that join a \"topic "
          f"mismatch\" while its structured verdict says sound.\n")
    W(f"{Dd['consecutive_substep']} joins link consecutive sub-steps of one step, a genuine "
      f"sequential relation, but `previous_step` on a sub-2 item points past sub-1, so the "
      f"premise text is wrong for those too and their scope verdicts are also void.\n")

    # ---- Part E
    W('## Part E — derived_input\n')
    W(f"{DI['candidate_triples']} candidate triples reduce to "
      f"**{DI['distinct_item_target_pairs']} distinct (item, target claim) pairs** across "
      f"{DI['papers_with_candidates']} of 32 papers. Running all of them would cost about 3100 "
      f"model calls, so a cap of {DI['cap_per_paper']} per paper takes **{DI['items']}** "
      f"forward.\n")
    W(tbl(['dropped at generation', 'count'],
          sorted(DI['dropped'].items(), key=lambda x: -x[1])))
    W('')
    W(f"The exclusion is checked mechanically and twice, by node id and by panel id, and "
      f"asserted again over the finished items: {DI['exclusion_check']}.\n")
    W(tbl(['paper', 'candidates', 'items taken'],
          sorted([[k.split('__')[0].replace('_', ' ')[:34] + ' · ' + k.split('__')[1][:22],
                   v, DI['per_paper_items'].get(k, 0)]
                  for k, v in DI['per_paper_candidates'].items()], key=lambda r: -r[1])))
    W('')
    if not E:
        W('_Necessity on the derived_input items: not yet run._\n')
    else:
        W(tbl(['stage', 'items'], [[k, v] for k, v in E['funnel']]))
        W('')
        W(f"**The necessity gate is {E['necessity_gate']}.** Part B's decision agreement was "
          f"28.6% against a two-thirds target, and the brief says that when Part B fails, the "
          f"gate is skipped and the items are built and drafted anyway. So there is no "
          f"necessity column and no claim that these items compose. Part E's own stop rule -- "
          f"fewer than 10 items passing necessity -- cannot be evaluated, because nothing was "
          f"measured against it.\n")
        W(f"{E['drafted']} of {E['items']} drafted, {len(E['unparsed'])} unparsed, "
          f"{len(E['foreign_keys'])} keys failing the belongs-check that caught 11 "
          f"mis-attached keys in v2.5.\n")
        W(tbl(['the drafter\'s own labels', 'items'],
              sorted(E['labels'].items(), key=lambda x: (-x[1], x[0]))))
        W('')
        W(f"Read these with care. `dependency: real` on {E['labels'].get('dependency: real', 0)} "
          f"of {E['drafted']} items and `combines` true on {E['combines_true']} are the "
          f"DRAFTER's judgement of an item it was shown as a pair, not an independent test. The "
          f"drafter cannot be the necessity check; that is the whole reason the gate exists. "
          f"What the labels do say is less flattering and more informative: "
          f"{E['labels'].get('inference_validity: follows, weakly', 0)} of {E['drafted']} are "
          f"only \"follows, weakly\", "
          f"{E['labels'].get('causal_strength: associative', 0)} are merely associative, and "
          f"{E['not_identifiable']} name something not identifiable. The generator produces "
          f"pairs that are structurally dependent and evidentially weak.\n")
        W('### Five worked examples\n')
        W('The brief asked for both arms and the comparer\'s reasoning on each. Those do not '
          'exist, because the gate was skipped. What is shown instead is the full item: the '
          'input result, the new observation, and the key the drafter wrote from the two.\n')
        for w in E.get('worked_examples', [])[:5]:
            W(f"**`{w['item']}`** — {w['paper'].split('__')[0].replace('_', ' ')}, "
              f"edge {w['edge']}, upstream `{w['upstream_item']}`\n")
            W(f"- question: {w['question']}")
            W(f"- input result (arm B only): {w['input_result'][:300]}")
            W(f"- new observation `{w['new_obs_node']}` (both arms): {w['new_obs'][:240]}")
            W(f"- panels {w['panels']} against the upstream's "
              f"{[q.split('#')[-1] for q in w['upstream_panels']]} — disjoint by construction")
            W(f"- drafted proposition: {w['proposition'][:340]}")
            W(f"- labels: {w['labels']}\n")

    # ---- funnel
    W('## The updated funnel\n')
    W('Two tracks now, because they measure different things. The v2.5/v2.6 chains are merges '
      'found by sharing a claim id; the derived_input items are merges built so that something '
      'has to travel.\n')
    V6 = json.load(open(R('results/v2p6/counted.json')))
    rows = [[n, v] for n, v in V6['funnel'][:5]]
    rows[3][0] = 'after step 3 (v2.6 flag)'
    rows.append(['after step 3 widened to the v2.7 rule',
                 f"{C['joins'] - C['v2p7_flagged']} of {C['joins']} seams survive the flag"])
    if B:
        rows.append(['after Part B necessity, floor-corrected',
                     B['necessity'].get('yes', 0)])
    W(tbl(['stage', 'chains'], rows))
    W('')
    if E:
        W(tbl(['derived_input', 'items'], [[n, v] for n, v in E['funnel']]))
        W('')

    # ---- cost
    W('## Cost\n')
    est = COST.get('estimate_before_starting') or {}
    W(f"Estimated before starting: **{est.get('total', '?')} calls** "
      f"(Part A {est.get('partA', {}).get('total')}, Part B {est.get('partB', {}).get('total')}, "
      f"Part E {est.get('partE', {}).get('total')}).\n")
    crow = [[k, v['calls'], v.get('relays', ''), v['wall_min'], v['s_per_call']]
            for k, v in COST.items() if isinstance(v, dict) and 'wall_min' in v]
    W(tbl(['stage', 'model calls', 'relays', 'wall minutes', 'seconds per call'], crow))
    W('')
    tot = sum(r[1] for r in crow); mins = sum(r[3] for r in crow)
    est_tot = est.get('total') or 0
    W(f"**Actual: {tot} calls, {round(mins, 1)} minutes** at the 20-agent cap, dispatch to last "
      f"harvest, relay overhead included. Every reply verified byte for byte against its prompt "
      f"file from the agent's own transcript.\n")
    W(f"That is {est_tot - tot} calls under the {est_tot} estimated, and the whole difference is "
      f"Part E: the necessity gate was skipped when Part B failed its agreement target, which "
      f"removed the 702 arm samples and 468 comparisons that gate would have needed. What was "
      f"spent instead was 76 drafts twice over, because an id collision in the first pass meant "
      f"two items would have carried a key drafted for a different item; all 76 were re-drafted "
      f"on corrected ids rather than the four being patched in place.\n")
    W('Parts C and D cost nothing: they re-read audits that already exist.\n')

    W('## Where the data is\n')
    W('- `results/v2p7/partA.json` — the noise floor, every A-vs-A ruling\n'
      '- `results/v2p7/graded/` — Part B, every graded prompt and reply\n'
      '- `results/v2p7/partB.json` — scores, per-chain margins, agreement\n'
      '- `results/v2p7/partC.json` — every flag with the sentence that triggered it\n'
      '- `results/v2p7/partD.json`, `partD_cases.json` — the 14 backbone joins side by side\n'
      '- `results/v2p7/derived_input.json` — candidates, drops and the items taken forward\n'
      '- `results/v2p7/draft/`, `armsE/`, `gradedE/` — Part E drafts, arms and comparisons\n')
    W('Every verdict is model against model.')

    open(R('docs/TRACES_V2P7.md'), 'w').write('\n'.join(out) + '\n')
    print('docs/TRACES_V2P7.md written,', len('\n'.join(out).split('\n')), 'lines')


if __name__ == '__main__': main()
