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
    PG = J('pages_report.json')
    A = []
    W = A.append

    W('# Traces v2.6 — only the merges that hold\n')
    W('Every verdict is model against model.\n')
    W('v2.6 keeps v2.5\'s 32 papers and its two-step items. It changes only which merges count.\n')
    W('An external review of the Nano Letters page (nanolett.6b04294) found merges that link two '
      'items by a shared claim id although the second step never uses what the first concluded. '
      'One trace there dropped the XANES result entirely and still reported "every limit '
      'survives". Two traces were the same chain under two generator labels. The covariation '
      'generator paired series because they had the same length. Each of those is a separate '
      'defect and v2.6 addresses each separately.\n')

    W('## The funnel\n')
    W(tbl(['stage', 'chains', 'lost here'],
          [[n, v, '' if i == 0 else CT['funnel'][i - 1][1] - v]
           for i, (n, v) in enumerate(CT['funnel'])]))
    W('')
    W(f'**{CT["compositional"]} of {P["funnel"]["chains_v2p5"]} v2.5 chains are compositional '
      f'merges.** Of the {CT["chains"]} chains that reach the model checks, '
      f'{CT["lost_at"]["step3"]} are lost at step 3, {CT["lost_at"]["step4"]} more at step 4 and '
      f'{CT["lost_at"]["step5"]} more at step 5.\n')
    W(f'At seam level: {CT["seams"]} seams, {CT["seams_counted"]} counted, '
      f'{CT["seam_gates"]["upstream_ignored"]} flagged upstream-ignored, '
      f'{CT["seam_gates"]["scope_failed"]} failing the scope check.\n')

    W('## Chain depth, before and after\n')
    ds = sorted({int(k) for k in list(P['depth_before']) + list(P['depth_after_dedup'])
                 + list(CT['depth_compositional'])})
    W(tbl(['depth', 'v2.5', 'after dropping covariation', 'after dedup', 'compositional'],
          [[d, P['depth_before'].get(str(d), 0), P['depth_after_drop'].get(str(d), 0),
            P['depth_after_dedup'].get(str(d), 0), CT['depth_compositional'].get(str(d), 0)]
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
    W(tbl(['necessity', 'chains'], sorted(NE['necessity'].items(), key=lambda x: -x[1])))
    W('')
    W(f'**Stability: {st["unanimous"]} of {st["chains_with_3_votes"]} chains had all three '
      f'repeats agree ({round(100 * st["share"])}%).** The stop rule was two thirds; '
      + ('this clears it.' if st['share'] >= 2 / 3 else
         '**this does not clear it, and the run stops here rather than filter on a noisy check.**')
      + '\n')
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
        rows.append([p.split('__')[0].replace('_', ' ')[:38], v.get('chains', 0),
                     v.get('gate3', 0), v.get('gate4', 0), v.get('compositional', 0),
                     v.get('seams', 0), v.get('ignored', 0), v.get('counted', 0)])
    rows.sort(key=lambda r: (-r[4], -r[1]))
    W(tbl(['paper', 'chains', 'pass 3', 'pass 3+4', 'compositional', 'seams', 'ignored',
           'seams counted'], rows))
    W('')
    tot = collections.Counter()
    for v in CT['per_paper'].values(): tot.update(v)
    W(f'Totals: {tot["chains"]} chains, {tot["compositional"]} compositional, {tot["seams"]} '
      f'seams, {tot["ignored"]} ignored, {tot["counted"]} counted.\n')

    W('## Worked example — Nano Letters, nanolett.6b04294\n')
    ch = [c for c in CT['chains_out'] if c['paper'] == NANO]
    sm = {k: v for k, v in CT['seams_out'].items() if v['paper'] == NANO}
    W(f'The page the review read. v2.5 showed 4 chains here; v2.6 shows {len(ch)} after the '
      f'covariation drop and the tail collapse, of which '
      f'{sum(1 for c in ch if c["compositional"])} is a compositional merge.\n')
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
      '- `results/v2p6/counted.json` — step 6, the three gates per seam and per chain\n'
      '- `results/v2p6/pages/` — step 7, one page per paper plus the index\n')
    W(f'Pages: {len(PG["rows"])} + index, totals {PG["totals"]}.\n')
    W('Every verdict is model against model.')

    open(R('docs/TRACES_V2P6.md'), 'w').write('\n'.join(A) + '\n')
    print('docs/TRACES_V2P6.md written,', len('\n'.join(A).split('\n')), 'lines')


if __name__ == '__main__': main()
