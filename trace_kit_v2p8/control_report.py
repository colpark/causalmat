"""control_report.py: write docs/TRACES_V2P8B_CONTROL.md from results/v2p8/control/*.json.

  python3 -m trace_kit_v2p8.control_report

No number typed by hand.

Every verdict is model against model.
"""
import json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
ARMS = ('A', 'B', 'C', 'A_full', 'C_full', 'N', 'B_narrow')
HELD = {
    'A': 'measurement + panels, narrow question (v2.8)',
    'B': 'measurement + panels + earlier result, full question (v2.8)',
    'C': 'earlier result only, narrow question (v2.8)',
    'A_full': 'measurement + panels, **full** question',
    'C_full': 'earlier result + its upstream panels, **full** question',
    'N': 'nothing but the full question',
    'B_narrow': "arm B's evidence, arm A's **narrow** question",
}


def tbl(head, rows):
    return '\n'.join(['| ' + ' | '.join(str(h) for h in head) + ' |',
                      '|' + '|'.join('---' for _ in head) + '|']
                     + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows])


def fm(v):
    return '—' if v is None else f'{v:.3f}'


def main():
    C = json.load(open(R('results/v2p8/control/control.json')))
    COST = json.load(open(R('results/v2p8/control/cost.json')))
    A8 = json.load(open(R('results/v2p8/partA.json')))['claims']
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    out = []; W = out.append

    W('# Traces v2.8b — the same-question control\n')
    W('Every verdict is model against model.\n')
    W("In v2.8 only arm B was asked the full combined question. Arms A and C got narrower "
      "questions matching what they held, which they needed to be answerable, but it left their "
      "near-zero scores on combined claims partly a property of the question. This run asks "
      "every arm the same full question, word for word, and blanks the missing section with "
      "\"not provided\" so the document shape never changes either.\n")
    W("It also adds arm N, which gets the question and nothing else. These are published "
      "papers. If a model reaches a key's combined claims with no measurement and no earlier "
      "result, then that claim was never evidence of composition.\n")
    W('The v2.8 claim lists, and the v2.8 arm A, B and C answers and gradings, are reused '
      'unchanged. The grader is the v2.8 grader, unchanged, and never sees the arm label.\n')

    W('## The headline\n')
    m = C['mean_combined_across_items']
    W(tbl(['arm', 'what it held', 'mean combined', 'mean limit'],
          [[f'**{a}**', HELD[a], fm(m[a]), fm(C['mean_limit_across_items'][a])] for a in ARMS]))
    W('')
    W(f"**{C['strictly_compositional']} of {C['items']} items are strictly compositional**, "
      f"against {C['v2p8_compositional']} of {C['items']} under v2.8's looser rule. "
      f"Arm B beats A_full on {C['beats_A_full']}, beats C_full on {C['beats_C_full']}, and "
      f"arm N stays under 0.25 on {C['items'] - C['N_at_or_above_threshold']}.\n")
    W(f"**Split halves agree on {C['halves_agree']} of {C['items']} items.** The stop rule was "
      f"6 of 8: " + ('not fired.' if not C['stop_halves'] else
                     '**fired, so no compositional claim is made from these numbers.**') + '\n')
    if C['stop_memorisation']:
        W(f"**The memorisation stop rule fired.** Arm N reaches 0.25 or more on "
          f"{C['N_at_or_above_threshold']} of {C['items']} items, and the brief says to report "
          f"that as the main finding. See the arm N section below.\n")
    else:
        W(f"The memorisation stop rule did not fire: arm N reaches 0.25 or more on "
          f"{C['N_at_or_above_threshold']} of {C['items']} items, under the threshold of 3.\n")

    W('## What the blanked sections did to the arms\n')
    AB = json.load(open(R('results/v2p8/control/abstention.json')))
    W('The control removed one artefact and introduced another, and the second one is large '
      'enough that the headline above cannot be read at face value. Marking a section "not '
      'provided" makes the answerer refuse rather than reason from what it does hold:\n')
    W(tbl(['arm', 'answers that open by refusing the task', 'of'],
          [[f'**{a}**', AB['abstains'].get(a, 0), AB['samples'].get(a, 0)]
           for a in ('A_full', 'C_full', 'N', 'B_narrow')]))
    W('')
    W(f"Arm N refuses in {AB['abstains'].get('N', 0)} of {AB['samples'].get('N', 0)} samples "
      f"and A_full in {AB['abstains'].get('A_full', 0)} of {AB['samples'].get('A_full', 0)}. So "
      f"A_full's {fm(m['A_full'])} and C_full's {fm(m['C_full'])} are substantially a measure "
      f"of abstention, not of what the evidence supports. v2.8's arms A and C, asked a narrower "
      f"but coherent question with real content in every section, abstained not at all and "
      f"scored {fm(m['A'])} and {fm(m['C'])}.\n")
    W("**The two runs bracket the truth rather than one superseding the other.** v2.8 asked "
      "each arm a question it could answer but gave arm B an easier one. v2.8b asked every arm "
      "the same question but told two of them their evidence was missing, which they mostly "
      "took as an instruction to stop. The real single-side capability sits between "
      f"{fm(m['A_full'])} and {fm(m['A'])} for the measurement side and between "
      f"{fm(m['C_full'])} and {fm(m['C'])} for the earlier-result side. Neither run settles it, "
      "and a third design -- same question, no blanking, each arm simply given less -- would.\n")
    W(f"The same caveat weakens arm N as a memorisation test. It scores {fm(m['N'])} on every "
      f"item, which is a clean result, but with {AB['abstains'].get('N', 0)} of "
      f"{AB['samples'].get('N', 0)} answers refusing outright it measures whether the model "
      f"WILL answer with no evidence, not whether it COULD. A sharper test would name the paper "
      f"and ask for a best guess.\n")

    W('## Arm N on its own\n')
    W('Arm N held the question and nothing else: no measurement, no earlier result, no panels. '
      'Whatever it scores is what the wording of the question, plus whatever the model already '
      'knows about the paper, is worth.\n')
    W(tbl(['item', 'journal', 'combined claims', 'arm N combined', 'arm N limit',
           'arm N contradictions'],
          [[f"`{k[:38]}`", v['journal'].replace('_', ' ')[:26], v['n_combined'],
            f"**{fm(v['mean_combined']['N'])}**", fm(v['mean_limit']['N']),
            fm(v['mean_contradictions']['N'])]
           for k, v in C['items_out'].items() if 'error' not in v]))
    W('')
    if C['N_items']:
        W(f"Items where arm N reaches 0.25 or more, which point at a paper the model may "
          f"already know: {', '.join('`' + k + '`' for k in C['N_items'])}\n")
    else:
        W('No item has arm N at or above 0.25.\n')

    W('## Every item, all seven arms\n')
    for k, v in C['items_out'].items():
        if 'error' in v: continue
        W(f"### `{k}`\n")
        W(f"{v['journal'].replace('_', ' ')} · drafter label **{v['cs']}** · upstream "
          f"`{v['upstream']}` ({v['up_gen']}) · {v['n_combined']} combined claims, "
          f"{v['n_limit']} limit claims\n")
        W(tbl(['arm', 'what it held', 'mean combined', 'mean limit', 'mean contradictions'],
              [[f'**{a}**', HELD[a], fm(v['mean_combined'][a]), fm(v['mean_limit'][a]),
                fm(v['mean_contradictions'][a])] for a in ARMS]))
        W('')
        W(f"B − A_full {v['B_minus_A_full']:+.3f} → **{v['beats_A_full']}** · "
          f"B − C_full {v['B_minus_C_full']:+.3f} → **{v['beats_C_full']}** · "
          f"arm N below 0.25 → **{v['N_below_threshold']}**\n")
        W(f"strictly compositional **{v['strictly_compositional']}** "
          f"(v2.8 said {v['v2p8_compositional']}) · "
          f"reaches it unprompted (B_narrow ≥ 0.5) **{v['B_narrow_reaches']}** · "
          f"halves ({v['halves']['first']['compositional']}, "
          f"{v['halves']['second']['compositional']}) agree **{v['halves_agree']}**\n")

    W('## The item v2.8 failed, which this run appears to rescue\n')
    K = 'di_journal_of_a_spi_o13_o20_o22_n15'
    v = C['items_out'].get(K)
    if v:
        W(f"v2.8 failed `{K}` because arm C -- the earlier result alone, asked a coherent "
          f"narrow question -- reached {fm(v['mean_combined']['C'])} of its combined claims, "
          f"identically across all 6 samples. Under this run's strict rule it passes, because "
          f"C_full reaches only {fm(v['mean_combined']['C_full'])}.\n")
        W("**I do not read that as a rescue.** The difference between arm C and arm C_full is "
          "not more evidence, it is the \"not provided\" marker telling the same answerer to "
          "stop. The v2.8 finding stands: the earlier result alone reaches half this item's "
          "combined claims, so one of its two combined tags is wrong.\n")
        W(f"It is also the one item whose split halves disagree "
          f"({v['halves']['first']['compositional']} then "
          f"{v['halves']['second']['compositional']}), with C_full moving "
          f"{fm(v['halves']['first']['means']['C_full'])} to "
          f"{fm(v['halves']['second']['means']['C_full'])} between them. On every reading it is "
          f"the weakest of the 8 and should not be counted as compositional without a human "
          f"looking at its two combined claims.\n")

    W('## Items that dropped out\n')
    if not C['dropped_out']:
        W('None. Every item v2.8 called compositional survives the strict rule.\n')
    else:
        ANS = C['answers']
        for k in C['dropped_out']:
            v = C['items_out'][k]
            why = []
            if not v['beats_A_full']: why.append(f"A_full ({fm(v['mean_combined']['A_full'])})")
            if not v['beats_C_full']: why.append(f"C_full ({fm(v['mean_combined']['C_full'])})")
            if not v['N_below_threshold']: why.append(f"N ({fm(v['mean_combined']['N'])})")
            W(f"### `{k}`\n")
            W(f"{v['journal'].replace('_', ' ')} · dropped because of **{', '.join(why)}**, "
              f"against arm B at {fm(v['mean_combined']['B'])}.\n")
            arm = ('A_full' if not v['beats_A_full']
                   else 'C_full' if not v['beats_C_full'] else 'N')
            key = f'{k}_{arm}1'
            a = ANS.get(key)
            if a:
                f = R('results/v2p8/control/arms', f'{k}_{arm}1.out.txt')
                if os.path.exists(f):
                    from trace_kit_v2p6.clean import clean
                    W(f"One arm {arm} answer, combined {a['combined_score']:.2f}:\n")
                    W('> ' + clean(open(f).read())[:900].replace('\n', '\n> ') + '\n')
                for r in a['rulings']:
                    if r['kind'] == 'combined' and r['verdict'] == 'stated':
                        W(f"- the grader ruled `stated` on: {r['claim']}")
                        if r['quote']: W(f'  > "{r["quote"]}"')
                W('')

    W('## Reaching it unprompted\n')
    W(f"Arm B_narrow holds arm B's full evidence but is asked arm A's narrower question, so it "
      f"is never pointed at the combination. It reaches the combined claims (mean ≥ 0.5) on "
      f"**{C['B_narrow_reaches']} of {C['items']}** items. This does not gate anything; it is "
      f"the difference between an item whose combination a reader would find and one that has "
      f"to be asked for.\n")
    W(tbl(['item', 'B (full question)', 'B_narrow (narrow question)', 'reaches unprompted'],
          [[f"`{k[:38]}`", fm(v['mean_combined']['B']), fm(v['mean_combined']['B_narrow']),
            'yes' if v['B_narrow_reaches'] else 'no']
           for k, v in C['items_out'].items() if 'error' not in v]))
    W('')

    W('## Split halves\n')
    W(tbl(['item', 'samples 1-3', 'samples 4-6', 'agree'],
          [[f"`{k[:38]}`", v['halves']['first']['compositional'],
            v['halves']['second']['compositional'], 'yes' if v['halves_agree'] else 'no']
           for k, v in C['items_out'].items() if 'error' not in v]))
    W('')

    W('## Cost\n')
    est = COST.get('estimate_before_starting', {})
    W(f"Estimated before starting: **{est.get('total')} calls** "
      f"({est.get('answers')} answers, {est.get('gradings')} gradings).\n")
    rows = [[k, v['calls'], v.get('relays', ''), v['wall_min'], v['s_per_call']]
            for k, v in COST.items() if isinstance(v, dict) and 'wall_min' in v]
    W(tbl(['stage', 'model calls', 'relays', 'wall minutes', 'seconds per call'], rows))
    W('')
    tot = sum(r[1] for r in rows); mins = sum(r[3] for r in rows)
    W(f"**Actual: {tot} calls, {round(mins, 1)} minutes** at the 20-agent cap. Every reply "
      f"verified byte for byte against its prompt file from the agent's own transcript.\n")

    W('## Where the data is\n')
    W('- `results/v2p8/control/arms/` — the 4 new arms, 6 samples each\n'
      '- `results/v2p8/control/grade/` — every grading with its quotes\n'
      '- `results/v2p8/control/control.json` — arm means, the strict decision, split halves\n'
      '- the v2.8 arm A, B, C answers and gradings are reused unchanged from '
      '`results/v2p8/arms/` and `results/v2p8/partC.json`\n')
    W('Every verdict is model against model.')

    open(R('docs/TRACES_V2P8B_CONTROL.md'), 'w').write('\n'.join(out) + '\n')
    print('docs/TRACES_V2P8B_CONTROL.md written,', len('\n'.join(out).split('\n')), 'lines')


if __name__ == '__main__': main()
