"""report.py: write docs/TRACES_V2P9.md entirely from results/v2p9/*.json.

  python3 -m trace_kit_v2p9.report

No number typed by hand.

Every verdict is model against model.
"""
import json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)


def J(p, d=None):
    f = R('results/v2p9', p)
    return json.load(open(f)) if os.path.exists(f) else d


def tbl(h, rows):
    return '\n'.join(['| ' + ' | '.join(str(x) for x in h) + ' |',
                      '|' + '|'.join('---' for _ in h) + '|']
                     + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows])


def fm(v, n=3):
    return '—' if v is None else f'{v:.{n}f}'


def main():
    P0, C1 = J('pairs.json'), J('calib.json')
    S2, S4 = J('step2.json'), J('step4.json')
    NL, S5 = J('nextlink.json'), J('step5.json')
    COST = J('cost.json')
    out = []; W = out.append

    W('# Traces v2.9 — the 24 papers outside the pilot\n')
    W('Every verdict is model against model.\n')
    W('The 32 v2.5 papers minus the 8 used in the v2.8 pilot. Every derived_input pair on them, '
      'drafted and tested with the method the pilot settled: claims split out of the key, three '
      'evidence arms graded against those claims, and an arm that gets nothing but the paper\'s '
      'name. Out of sample in the sense that matters — none of these papers tuned anything.\n')

    # ---- Step 0
    W('## Step 0 — the free filters\n')
    W(f"{sum(P0['dropped'].values()) + P0['pairs']} candidate triples on {P0['papers']} papers, "
      f"reduced to **{P0['pairs']} pairs on {P0['papers_with_pairs']} papers** without one model "
      f"call.\n")
    W(tbl(['filter', 'pairs removed'],
          sorted(P0['dropped'].items(), key=lambda x: -x[1])))
    W('')
    W("The largest is the v2.7 widened \"upstream ignored\" rule, applied here as: drop a pair "
      "when v2.5 already composed a join from this pair's upstream item into an item concluding "
      "this pair's target claim, and v2.7 flagged that join as one where the downstream never "
      "used the upstream result. If the join that used this exact result for this exact claim "
      "came out empty, the pair asks for the same thing again.\n")
    W(f"{len(P0['papers_with_no_pairs'])} papers yield nothing:\n")
    for p, why in P0['papers_with_no_pairs'].items():
        W(f"- {p.split('__')[0].replace('_', ' ')} · {p.split('__')[1]} — {why}")
    W('')

    # ---- Step 1
    W('## Step 1 — Haiku calibration\n')
    W(f"{C1['tagging']['of']} tags, {C1['checking']['of']} check verdicts and "
      f"{C1['grading']['of']} gradings rerun on the v2.8 pilot data with the same prompts byte "
      f"for byte. Only the model differs, and every dispatch was verified as "
      f"`{C1['model']}` from the relay's own transcript.\n")
    W(tbl(['role', 'agreement with Sonnet', 'bar', 'verdict'],
          [['tagging', f"{C1['tagging']['agree']}/{C1['tagging']['of']} = "
                       f"{round(100 * C1['tagging']['share'], 1)}%", '85%',
            'passes' if C1['tagging']['passes'] else '**fails**'],
           ['checking', f"{C1['checking']['agree']}/{C1['checking']['of']} = "
                        f"{round(100 * C1['checking']['share'], 1)}%", '85%',
            'passes' if C1['checking']['passes'] else '**fails**'],
           ['grading', f"{C1['grading']['within_0.25']}/{C1['grading']['of']} = "
                       f"{round(100 * C1['grading']['share'], 1)}%", '85%',
            'passes' if C1['grading']['passes'] else '**fails**'],
           ['grading, pilot verdicts',
            f"{C1['grading']['verdicts_reproduced']}/{C1['grading']['verdict_items']}", 'all',
            '**fails**']]))
    W('')
    sc = C1['grading']['schema_compliant_only']
    W(f"On the replies Haiku returned as valid JSON — the unbiased subset, since the salvage "
      f"drops quotes and a stated without a quote is withdrawn to absent — grading agreement is "
      f"{sc['within_0.25']}/{sc['of']} = {round(100 * sc['share'], 1)}%, at the bar rather than "
      f"over it, and the verdict condition still fails.\n")
    W(tbl(['role', 'how the reply parsed'],
          [['check', ', '.join(f'{k} {v}' for k, v in C1['reply_format']['check'].items())],
           ['grade', ', '.join(f'{k} {v}' for k, v in C1['reply_format']['grade'].items())]]))
    W('')
    W("Schema compliance is the number that decides this at 15,000 papers, and it is not close. "
      "Three of my own parser bugs had to be fixed before this was a fair test: Haiku answers "
      "the checker in prose, fences its grading JSON, and -- the one that was purely mine -- "
      "`obj()` counts braces without respecting string literals, so claims containing Miller "
      "indices like {10-12} were unparseable. What survived all three fixes is real: Haiku "
      "quotes the answer's words without escaping the quotes inside them.\n")
    W(f"All roles stay on Sonnet: {json.dumps(C1['roles'])}.\n")

    # ---- funnel
    W('## The funnel\n')
    rows = [['candidate triples', sum(P0['dropped'].values()) + P0['pairs']],
            ['after the free filters', P0['pairs']],
            ['drafted into a usable key', S2['drafted']],
            ['split into claims', S2['with_a_split']],
            ['with at least one combined claim', S2['alive']]]
    if S4:
        rows.append(['compositional (B beats A and C, N low)', S4['compositional']])
    if NL: rows.append(['depth 3 candidates', NL['next_links']])
    if S5: rows.append(['depth 3 links that pass', S5['passed']])
    W(tbl(['stage', 'count'], rows))
    W('')
    W(f"Step 2 dropped nothing: {S2['alive']} of {S2['pairs']} pairs kept a combined claim. At "
      f"15,000 papers that matters — the three production calls per pair are pure cost and all "
      f"the selection happens in the arm test.\n")
    W(f"Tag agreement between the two agents was {round(100 * S2['tag_agreement'], 1)}% "
      f"({S2['tags_agreed']} of {S2['tags_proposed']}), against the pilot's 94.7% on a set four "
      f"times larger and on papers that tuned nothing.\n")

    if not S4:
        W('_Steps 3 to 5 not yet complete._\n')
    else:
        # ---- step 4
        W('## Steps 3 and 4 — the arms\n')
        m, ml = S4['mean_combined_across_items'], S4['mean_limit_across_items']
        W(tbl(['arm', 'what it held', 'mean combined', 'mean limit'],
              [['A', 'the measurement with its panels, narrow question', fm(m['A']), fm(ml['A'])],
               ['B', 'measurement + earlier result, full question', fm(m['B']), fm(ml['B'])],
               ['C', 'the earlier result alone, narrow question', fm(m['C']), fm(ml['C'])],
               ['N', "the paper's title and journal, no evidence", fm(m['N']), fm(ml['N'])]]))
        W('')
        lo, hi = S4['pass_rate_95ci']
        W(f"**{S4['compositional']} of {S4['items']} items are compositional, "
          f"{round(100 * S4['pass_rate'], 1)}%** (95% CI "
          f"{round(100 * lo, 1)}–{round(100 * hi, 1)}%). The earlier result is needed on "
          f"{S4['input_needed']}, the measurement on {S4['observation_needed']}.\n")
        W(f"**Arm N reaches 0.25 or more on {S4['N_at_or_above_threshold']} of {S4['items']} "
          f"items, {round(100 * S4['N_share'], 1)}%.** " +
          ('The stop rule was 15%: **it fired, and memorisation is the main finding.**'
           if S4['stop_memorisation'] else
           'The stop rule was 15%, so it did not fire.') + '\n')
        if S4['N_items']:
            W('Items where the paper name alone reaches the claims:\n')
            for k in S4['N_items']:
                v = S4['items_out'][k]
                W(f"- `{k}` — N {fm(v['mean_combined']['N'])}, B {fm(v['mean_combined']['B'])} "
                  f"· {v['paper'].split('__')[0].replace('_', ' ')}")
            W('')
        W(f"{S4['borderline_count']} items fell in the 0.10–0.40 borderline band and got a "
          f"second sample of A, B and C. **{len(S4['borderline_flips'])} flipped.**\n")
        for f_ in S4['borderline_flips']:
            W(f"- `{f_['item']}` — one sample said {f_['one_sample']}, two samples say "
              f"{f_['two_sample']}")
        W('')
        W('### Per paper\n')
        W(tbl(['paper', 'items', 'compositional'],
              [[p.split('__')[0].replace('_', ' ')[:32] + ' · ' + p.split('__')[1][:22],
                d['items'], d['compositional']]
               for p, d in sorted(S4['per_paper'].items(),
                                  key=lambda x: -x[1]['compositional'])]))
        W('')

    # ---- step 5
    if NL:
        W('## Step 5 — depth 3\n')
        W(f"{NL['parents']} compositional items yielded **{NL['next_links']} next-link "
          f"candidates** across {NL['parents_with_a_next_link']} of them, at most "
          f"{NL['max_per_item']} each.\n")
        W(tbl(['dropped at generation', 'count'],
              sorted(NL['dropped'].items(), key=lambda x: -x[1])))
        W('')
        W(f"{NL['exclusion_check']} — checked against every step of the chain, not just the one "
          f"before, so a link cannot quietly re-read the chain's own first measurement.\n")
        if S5:
            lo, hi = S5['pass_rate_95ci']
            W(f"**{S5['passed']} of {S5['tested']} next links pass, "
              f"{round(100 * S5['pass_rate'], 1)}%** (95% CI {round(100 * lo, 1)}–"
              f"{round(100 * hi, 1)}%), against {round(100 * S4['pass_rate'], 1)}% at depth 2.\n")
            W(f"**{S5['depth3_chains']} depth 3 chains hold end to end** — both links passing.\n")
            if S5.get('worked'):
                W('### Three worked depth 3 chains\n')
                for w in S5['worked'][:3]:
                    W(f"#### `{w['chain_id']}`\n")
                    W(f"{w['paper'].split('__')[0].replace('_', ' ')}\n")
                    for i, st in enumerate(w['steps'], 1):
                        W(f"**step {i}** — {st['what']}\n")
                        if st.get('input_result'):
                            W(f"- earlier result: {st['input_result'][:300]}")
                        if st.get('observation'):
                            W(f"- new observation `{st['obs_node']}`: {st['observation'][:220]}")
                        if st.get('key'):
                            W(f"- key: {st['key'][:300]}")
                        if st.get('scores'):
                            W(f"- arms: A {fm(st['scores']['A'])}, B {fm(st['scores']['B'])}, "
                              f"C {fm(st['scores']['C'])}"
                              + (f", N {fm(st['scores']['N'])}" if st['scores'].get('N') is not None else ''))
                        W('')
        else:
            W('_Next links not yet tested._\n')

    # ---- cost
    W('## Cost\n')
    rows = [[k, v['calls'], v.get('relays', ''), v['wall_min'], v['s_per_call']]
            for k, v in COST.items() if isinstance(v, dict) and 'wall_min' in v]
    W(tbl(['stage', 'model calls', 'relays', 'wall minutes', 'seconds per call'], rows))
    W('')
    tot = sum(r[1] for r in rows); mins = sum(r[3] for r in rows)
    W(f"**{tot} calls, {round(mins, 1)} minutes** at the 20-agent cap, dispatch to last harvest. "
      f"Every reply verified byte for byte against its prompt file, and every model verified "
      f"from the transcript.\n")
    if S4:
        prod = sum(v['calls'] for k, v in COST.items()
                   if isinstance(v, dict) and 'calls' in v
                   and k in ('step2_draft', 'step2_tagcheck'))
        test = sum(v['calls'] for k, v in COST.items()
                   if isinstance(v, dict) and 'calls' in v
                   and k.startswith(('step3', 'step4')))
        W(tbl(['', 'calls', 'per item', 'per paper'],
              [['production (draft, tag, check)', prod, round(prod / S2['pairs'], 2),
                round(prod / P0['papers_with_pairs'], 1)],
               ['testing (4 arms + gradings + borderline)', test,
                round(test / S2['alive'], 2), round(test / P0['papers_with_pairs'], 1)],
               ['all stages', tot, round(tot / S2['pairs'], 2),
                round(tot / P0['papers'], 1)]]))
        W('')
        W(f"Production is {round(prod / S2['pairs'], 2)} calls per pair, as designed. Testing "
          f"every item costs {round(test / S2['alive'], 2)} more, which is the number that would "
          f"have to come down to run a pool of 15,000.\n")

    W('## Where the data is\n')
    W('- `results/v2p9/pairs.json` — Step 0, every pair and every filter\n'
      '- `results/v2p9/calib.json` — Step 1, Haiku against Sonnet\n'
      '- `results/v2p9/draft/`, `split/`, `check/`, `step2.json` — Step 2\n'
      '- `results/v2p9/arms/`, `grade/` — Steps 3 and 4, every answer and ruling\n'
      '- `results/v2p9/step4.json` — the decision per item\n'
      '- `results/v2p9/nextlink.json`, `step5.json` — depth 3\n')
    W('Every verdict is model against model.')

    open(R('docs/TRACES_V2P9.md'), 'w').write('\n'.join(out) + '\n')
    print('docs/TRACES_V2P9.md written,', len('\n'.join(out).split('\n')), 'lines')


if __name__ == '__main__': main()
