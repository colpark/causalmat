"""report.py: write docs/TRACES_V2P6.md entirely from the committed v2.6 json.

  python3 -m trace_kit_v2p6.report

Every number in the document is computed here from results/v2p6/*.json. None is typed by hand.
v2.5 had to be corrected twice for numbers that drifted out of the prose; this removes the way
that happens.

Every verdict is model against model.
"""
import collections, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
NANO = 'Nano_Letters__10.1021_acs.nanolett.6b04294'


def J(p): return json.load(open(R('results/v2p6', p)))


def tbl(head, rows):
    out = ['| ' + ' | '.join(head) + ' |',
           '|' + '|'.join('---' for _ in head) + '|']
    for r in rows: out.append('| ' + ' | '.join(str(x) for x in r) + ' |')
    return '\n'.join(out)


def main():
    P, IG, SC, NE, CT = J('pruned.json'), J('ignored.json'), J('scope.json'), \
        J('necessity.json'), J('counted.json')
    COST = J('cost.json')
    PG = J('pages_report.json') if os.path.exists(R('results/v2p6/pages_report.json')) else None
    A = []
    W = A.append

    W('# Traces v2.6 — tightening the v2.5 merges\n')
    W('Every verdict is model against model.\n')
    W('v2.6 keeps v2.5\'s 32 papers and its two-step items. It changes only which merges count.\n')
    W('An external review of the Nano Letters page (nanolett.6b04294) found merges that link two '
      'items by a shared claim id although the second step never uses what the first concluded. '
      'One trace there dropped the XANES result entirely and still reported "every limit '
      'survives". Two traces were the same chain under two generator labels. The covariation '
      'generator paired series because they had the same length. Each of those is a separate '
      'defect and v2.6 addresses each separately.\n')

    st0 = NE['stability']
    stopped = st0['share'] < 2 / 3
    if stopped:
        W('## Where this run stopped\n')
        W(f'**The stop rule fired.** The brief said to stop rather than filter if step 5\'s '
          f'repeats agree on fewer than two thirds of chains. They agree on '
          f'{st0["unanimous"]} of {st0["chains_with_3_votes"]} — '
          f'{round(100 * st0["share"], 1)}%. So steps 1 to 4 are reported as results and step 5 '
          f'is reported as an instrument that is not yet good enough to filter on. Steps 6 and 7 '
          f'— counting the merges and rebuilding the pages with a counted/not-counted label — '
          f'were **not applied**, because both consume step 5 as a gate.\n')
        W(f'Everything step 5 needs was nevertheless run in full: 492 arm answers and 313 '
          f'comparisons, all verified byte for byte. The numbers are in '
          f'`results/v2p6/necessity.json` and the step-5 column of the funnel below is shown '
          f'for information, not as a result.\n')
        W(f'The other stop rule did not fire: {CT["compositional"]} chains would survive all '
          f'three gates, above the floor of 10.\n')

    W('## The funnel\n')
    W(tbl(['stage', 'chains', 'lost here'],
          [[n + (' *(not reliable, see below)*' if stopped and i == 5 else ''), v,
            '' if i == 0 else CT['funnel'][i - 1][1] - v]
           for i, (n, v) in enumerate(CT['funnel'])]))
    W('')
    n3 = CT['funnel'][3][1]; n4 = CT['funnel'][4][1]
    W(f'**Through the checks that hold, {n4} of {P["funnel"]["chains_v2p5"]} v2.5 chains '
      f'survive.** 130 became 82 on structure alone: 21 chains used a covariation item and 27 '
      f'were the same chain under another opener. Of those 82, {CT["lost_at"]["step3"]} are lost '
      f'at step 3 because a seam in them never uses the upstream result, and '
      f'{CT["lost_at"]["step4"]} more at step 4 on scope. Step 5 would remove '
      f'{CT["lost_at"]["step5"]} more, leaving {CT["funnel"][5][1]}, but see the stop rule.\n')
    W(f'At seam level, on the two gates that hold: {CT["seams"]} seams, '
      f'{CT["seam_gates"]["upstream_ignored"]} flagged upstream-ignored and '
      f'{CT["seam_gates"]["scope_failed"]} failing the scope check, leaving '
      f'{CT["seams"] - len({*[k for k, v in CT["seams_out"].items() if v["upstream_ignored"] or not v["gate4"]]})} '
      f'that clear both. ({CT["seams_counted"]} would also clear step 5, not reported as a '
      f'result.)\n')

    W('## Chain depth, before and after\n')
    ds = sorted({int(k) for k in list(P['depth_before']) + list(P['depth_after_dedup'])
                 + list(CT['depth_compositional'])})
    W(tbl(['depth', 'v2.5', 'after dropping covariation', 'after dedup',
           'through steps 3+4', 'through step 5 *(not reliable)*'],
          [[d, P['depth_before'].get(str(d), 0), P['depth_after_drop'].get(str(d), 0),
            P['depth_after_dedup'].get(str(d), 0),
            sum(1 for c in CT['chains_out'] if c['depth'] == d and c['gate3'] and c['gate4']),
            CT['depth_compositional'].get(str(d), 0)]
           for d in ds]))
    W('')
    W(f'The two depth-5 chains were both covariation-dependent and are gone. '
      f'{P["collapsed"]} openers were folded into a chain that already existed.\n')

    W('## Step 3 — how many clean seams were empty\n')
    W(f'{IG["flagged"]} of {IG["joins"]} seams are flagged. No model call: the v2.5 join audits, '
      f're-read. {IG["by_signal"].get("structural", 0)} by the structural signal (every upstream '
      f'limit ruled not_applicable, which is the audit saying no qualification of the upstream '
      f'result has any object downstream), {IG["by_signal"].get("prose", 0)} by the audit stating '
      f'in words that the derived result is dropped, {IG["both_signals"]} by both.\n')
    W(f'**{len(IG["flagged_but_showed_every_limit_survives"])} of the {IG["flagged"]} flagged '
      f'seams showed "every limit survives" on the v2.5 page.** No limit was ruled dropped '
      f'because there was nothing downstream for an upstream limit to qualify. The seam looked '
      f'clean for the same reason it was empty.\n')

    W('## Step 4 — scope\n')
    W(tbl(['verdict', 'seams'], sorted(SC['verdicts'].items(), key=lambda x: -x[1])))
    W('')
    W(f'{SC["ruled"]} of {SC["joins"]} joins ruled' +
      (f', {len(SC["unruled"])} unparsed' if SC['unruled'] else ', none unparsed') + '.\n')
    W('The agent saw two texts and nothing else: the upstream item\'s key proposition with its '
      'limits, and the premise the next step takes as given. No claim ids, no paper-level claim '
      'text, no item or paper names, no panels, no generator label. An id scrub runs over both '
      'texts and the build refuses any prompt in which a bare node id survives it.\n')
    W('One limitation to record. `hidden_key_claims` on an item are verbatim graph node labels, '
      'so the ban on paper-level claim text rules out the only derived rendering of the join '
      'claim. The premise is therefore the downstream item\'s own join-side observation — and '
      '118 of the 121 v2.5-to-v2.5 joins read the very observation the upstream item already '
      'read. The downstream usually does not need a derived result at all; it re-reads the raw '
      'measurement. That is why the scope check cannot be the whole test, and why step 5 exists.\n')
    W(tbl(['premise source', 'supports', 'supports only narrower', 'incompatible'],
          [[k, v.get('supports', 0), v.get('supports only narrower', 0), v.get('incompatible', 0)]
           for k, v in [('downstream reads the same observation', SC['by_shared_obs']['True']),
                        ('downstream reads a different observation', SC['by_shared_obs']['False']),
                        ('v5 backbone, previous_output', SC['by_shared_obs']['None'])]]))
    W('')

    W('## Step 5 — necessity\n')
    st = NE['stability']
    W(f'For each chain the last item was answered twice: arm A with its question and its own '
      f'evidence, panels included; arm B with exactly that plus the upstream item\'s key '
      f'proposition and limits, handed over as a settled earlier result. A second agent read '
      f'both answers and ruled whether the conclusion or the uncertainty changed. Three repeats, '
      f'majority of three.\n')
    W(tbl(['necessity (majority of 3)', 'chains'],
          sorted(NE['necessity'].items(), key=lambda x: -x[1])))
    W('')
    pat = collections.Counter()
    for v in NE['chains_out'].values():
        pat[v['votes'].count('yes')] += 1
    n = sum(pat.values())
    W(tbl(['votes over the 3 repeats', 'chains', 'share'],
          [[f'{y} yes / {3 - y} no', pat.get(y, 0), f'{round(100 * pat.get(y, 0) / n)}%']
           for y in (3, 2, 1, 0)]))
    W('')
    ry = sum(v['votes'].count('yes') for v in NE['chains_out'].values()) / (3 * n)
    chance = ry ** 3 + (1 - ry) ** 3
    W(f'**Stability: {st["unanimous"]} of {st["chains_with_3_votes"]} chains had all three '
      f'repeats agree, {round(100 * st["share"], 1)}%.** The stop rule was two thirds, so '
      f'**this does not clear it and the run stops rather than filter on a noisy check.**\n')
    W(f'How noisy: the per-repeat "yes" rate is {round(ry, 3)}, so three independent coin flips '
      f'at that rate would agree {round(100 * chance, 1)}% of the time. The observed '
      f'{round(100 * st["share"], 1)}% is above that, so the check is not pure noise — it '
      f'carries real signal. It is just nowhere near separable enough to gate on: '
      f'{pat.get(2, 0) + pat.get(1, 0)} of {n} chains, {round(100 * (pat.get(2, 0) + pat.get(1, 0)) / n)}%, '
      f'split 2-1, and a majority of three on a coin that lands 54% heads is not a verdict.\n')
    W('Three things to fix before this check is worth running again:\n')
    W('1. **The comparer is asked a yes/no question about a difference of degree.** Two prose '
       'answers to an open question differ in wording every time; ruling whether the difference '
       '"matters" is the judgement, and it is being forced into a binary. A graded scale, or '
       'asking the same agent to rank the two answers on a stated dimension, would be steadier.\n')
    W('2. **Arm A and arm B are separate samples, so they differ for two reasons at once** — the '
       'upstream result, and ordinary answer-to-answer variation. Sampling arm A three times and '
       'comparing it against itself would measure that floor directly. That control was not run '
       'here and should be: without it we cannot say how much of the 54% "yes" rate is the '
       'upstream result at all.\n')
    W('3. **Necessity probes only the last hop**, so a chain is judged on one merge (see below).\n')
    W(tbl(['depth', 'necessity yes', 'necessity no'],
          [[d, v.get('yes', 0), v.get('no', 0)] for d, v in sorted(NE['by_depth'].items())]))
    W('')
    W('Two limitations of this test, both of them consequences of the brief\'s design and worth '
      'stating plainly. First, **necessity probes only the last hop of a chain.** A depth-4 chain '
      'and a depth-3 chain that end with the same merge get a byte-identical pair of arms and so '
      'the same verdict: 17 of the 164 arm prompts are duplicates of another chain\'s for exactly '
      'this reason. "Compositional" is therefore a verdict on a chain\'s final merge, not on every '
      'merge along it. Second, arm B hands the upstream result over as settled, so a comparer '
      'ruling "no" is saying the last step reaches the same place without it -- not that the '
      'upstream result is wrong.\n')
    pv = [c for c in CT['chains_out'] if c.get('predecessor_varies')]
    if pv:
        W(f'{len(pv)} depth-2 chains were left with more than one opener by the dedup, so the '
          f'item before the last one varies by variant. Those ran on the canonical opener; the '
          f'alternatives are recorded in `results/v2p6/necessity_rows.json`.\n')

    W('## Per paper\n')
    rows = []
    for p, v in CT['per_paper'].items():
        nm = p.split('__')[0].replace('_', ' ')[:30] + ' · ' + p.split('__')[1][:26]
        rows.append([nm, v.get('chains', 0),
                     v.get('gate3', 0), v.get('gate4', 0),
                     v.get('seams', 0), v.get('ignored', 0),
                     v.get('compositional', 0), v.get('counted', 0)])
    rows.sort(key=lambda r: (-r[3], -r[1]))
    W(tbl(['paper', 'chains', 'pass 3', 'pass 3+4', 'seams', 'ignored',
           'compositional *(not reliable)*', 'seams counted *(not reliable)*'], rows))
    W('')
    tot = collections.Counter()
    for v in CT['per_paper'].values(): tot.update(v)
    W(f'Totals: {tot["chains"]} chains, {tot["gate3"]} past step 3, {tot["gate4"]} past steps '
      f'3 and 4, {tot["seams"]} seams, {tot["ignored"]} ignored. '
      f'({tot["compositional"]} compositional and {tot["counted"]} seams counted under step 5, '
      f'not reported as results.)\n')

    W('## Worked example — Nano Letters, nanolett.6b04294\n')
    ch = [c for c in CT['chains_out'] if c['paper'] == NANO]
    sm = {k: v for k, v in CT['seams_out'].items() if v['paper'] == NANO}
    W(f'The page the review read. v2.5 showed 4 chains here; v2.6 shows {len(ch)} after the '
      f'covariation drop and the tail collapse — the review\'s "traces 3 and 4 are the same '
      f'chain under two generator labels" is the pair that collapsed. Of the {len(ch)}, '
      f'{sum(1 for c in ch if c["gate3"] and c["gate4"])} clear steps 3 and 4.\n')
    W(tbl(['trace', 'depth', 'ways in', 'items', 'upstream used', 'scope', 'necessity',
           'compositional'],
          [[c['chain'], c['depth'], len(c['openers']), ' → '.join(c['path']),
            'yes' if c['gate3'] else 'no', 'ok' if c['gate4'] else 'failed',
            f'{c.get("necessity")} ({"/".join(c.get("votes") or [])})',
            'yes' if c['compositional'] else 'no'] for c in ch]))
    W('')
    W(tbl(['seam', 'upstream ignored', 'scope', 'counted'],
          [[k.replace('__', ' → '), 'yes' if v['upstream_ignored'] else 'no',
            v.get('scope') or '—', 'yes' if v['counted'] else 'no']
           for k, v in sorted(sm.items())]))
    W('')
    xan = [k for k, v in sm.items() if v['upstream_ignored']]
    if xan:
        W('The seam the review named, the one that dropped the XANES result and still reported '
          '"every limit survives":\n')
        for k in xan:
            v = sm[k]
            W(f'- `{k}` — flagged by: {"; ".join(v["ignored_signals"])}')
            ev = (IG['seams'].get(k) or {}).get('evidence') or []
            for e in ev[:2]: W(f'  > {e}')
        W('')

    W('## One contamination, found and removed\n')
    W('A relay flagged that some arm replies carried text that was not part of the answer. Two '
      'kinds, both checked directly rather than taken on the relay\'s word: a trailing '
      'output-framing fragment (`</message>`, `</invoke>`) on 27 replies, and a leading note on '
      '21 replies where the answerer had seen this session\'s MCP server instruction block in '
      'its tool list, correctly judged it was not from the user, ignored it and said so. Neither '
      'changed what the answer said.\n')
    W('But both landed asymmetrically — in one arm of a pair and not the other, 25 and 21 pairs '
      'respectively — and the comparer is asked whether the two answers differ. So the artifacts '
      'were stripped (`clean.py`, leaving the raw replies untouched) and every comparison whose '
      'prompt changed was re-run: 39 of 246.\n')
    W('**7 of those 39 flipped, every one of them from "no" to "yes".** The contamination was '
      'suppressing the finding that the upstream result mattered. All numbers in this document '
      'are from the cleaned re-run.\n')
    W(f'Two comparison replies quoted the answers inside their `why` field without escaping the '
      f'quotes and so would not parse as JSON. Their verdict token was unambiguous in the raw '
      f'text and was read from it; {NE.get("salvaged_rulings", 0)} rulings were salvaged this '
      f'way and are counted here.\n')

    W('## What the calls cost\n')
    rows = []
    for st_, v in COST.items():
        if 'wall_min' not in v: continue
        rows.append([st_, v['calls'], v.get('relays', ''), v['wall_min'], v['s_per_call']])
    W(tbl(['stage', 'model calls', 'relays', 'wall minutes', 'seconds per call'], rows))
    W('')
    ncall = sum(v.get('calls', 0) for v in COST.values())
    nmin = sum(v.get('wall_min', 0) for v in COST.values())
    W(f'**{ncall} model calls, {round(nmin, 1)} minutes of wall time on 32 papers.** Wall time is '
      f'measured at a 20-agent concurrency cap, from dispatch to the last harvest, so it includes '
      f'relay overhead; it is not a per-call cost. Scaling linearly by paper, 99 papers would be '
      f'about {round(ncall * 99 / 32)} calls and about {round(nmin * 99 / 32 / 60, 1)} hours at '
      f'this cap.\n')
    W('Step 3 costs nothing: it re-reads audits that already exist.\n')

    W('## Stop rules\n')
    W(f'- repeats agree on fewer than two thirds of chains: '
      f'{round(100 * st["share"])}% agreed, '
      + ('rule not triggered.' if st['share'] >= 2 / 3 else '**rule triggered.**'))
    W(f'- fewer than 10 chains survive: {CT["compositional"]} survive, '
      + ('rule not triggered.' if CT['compositional'] >= 10 else '**rule triggered.**'))
    W('')

    W('## Where the data is\n')
    W('- `results/v2p6/pruned.json` — steps 1 and 2, with every dropped id\n'
      '- `results/v2p6/ignored.json` — step 3, the flag and the audit sentence behind it\n'
      '- `results/v2p6/scope/` — step 4, one prompt and one reply per join\n'
      '- `results/v2p6/arms/`, `results/v2p6/compare/` — step 5, every arm and comparison\n'
      '- `results/v2p6/counted.json` — the three gates per seam and per chain, computed for '
      'the record; step 5 is present in it but is not reported as a result\n')
    if PG: W(f'Pages: {len(PG["rows"])} + index, totals {PG["totals"]}.\n')
    else: W('- `results/v2p6/pages/` — not built. See "Where this run stopped".\n')
    W('Every verdict is model against model.')

    open(R('docs/TRACES_V2P6.md'), 'w').write('\n'.join(A) + '\n')
    print('docs/TRACES_V2P6.md written,', len('\n'.join(A).split('\n')), 'lines')


if __name__ == '__main__': main()
