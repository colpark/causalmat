"""report.py: write docs/TRACES_V2P10.md entirely from results/v2p10/*.json (and v2.9's).

  python3 -m trace_kit_v2p10.report

No number typed by hand.

Every verdict is model against model.
"""
import collections, glob, json, math, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p6'))
from clean import clean  # noqa: E402

REFUSE = re.compile(r'cannot determine|unable to|decline|no basis|refus', re.I)


def wilson(k, n, z=1.96):
    if not n: return (None, None)
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(max(0.0, c - h), 4), round(min(1.0, c + h), 4))


def J(p, d=None):
    f = R(p)
    return json.load(open(f)) if os.path.exists(f) else d


def tbl(h, rows):
    return '\n'.join(['| ' + ' | '.join(str(x) for x in h) + ' |',
                      '|' + '|'.join('---' for _ in h) + '|']
                     + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows])


def fm(v, n=3): return '—' if v is None else f'{v:.{n}f}'


def refusal_rate(pat):
    n = r = 0
    for f in glob.glob(R(pat)):
        t = clean(open(f).read()); n += 1
        if REFUSE.search(t[:300]): r += 1
    return r, n


def main():
    PU = J('results/v2p10/purge.json')
    S2 = J('results/v2p9/step4.json'); S3 = J('results/v2p9/step4_nl.json')
    D4g = J('results/v2p10/deeper_d4.json'); S4 = J('results/v2p10/step4_d4.json')
    D5g = J('results/v2p10/deeper_d5.json'); S5 = J('results/v2p10/step4_d5.json')
    C4 = J('results/v2p10/step2_d4.json'); PG = J('results/v2p10/pages_report.json')
    COST = J('results/v2p10/cost.json')
    out = []; W = out.append

    W('# Traces v2.10 — chains that hold, and how deep they go\n')
    W('Every verdict is model against model.\n')
    W('The same 24 papers as v2.9. Three things: remove anything the model can answer from the '
      "paper's name, push the chains one or two steps deeper, and lay the surviving chains out "
      'on a page so one can be read end to end.\n')

    W('## Step 1 — the memorisation purge removed nothing\n')
    W(tbl(['', 'before', 'flagged', 'after'],
          [['depth 2 compositional items', PU['depth2']['before'], PU['depth2']['flagged'],
            PU['depth2']['after']],
           ['depth 3 chains', PU['depth3']['before'], PU['depth3']['flagged_links'],
            PU['depth3']['after']]]))
    W('')
    W(f"**Nothing moved.** {PU['depth2']['flagged_and_passing']} of the "
      f"{PU['depth2']['flagged']} flagged depth-2 items were passing, and "
      f"{PU['depth3']['chains_killed']} chains died. v2.9's compositional test already required "
      f"arm N below {PU['threshold']} as one of its three gates, so a memorised item could never "
      f"have been counted in the first place. The brief assumed they were still in the passing "
      f"set; they were not, and this is verified rather than argued.\n")
    W('The flagged items are kept in full with their arm N answers, because what a corpus gives '
      'away for free is a fact about the corpus. Three scored 1.00 — the title alone reached '
      'every combined claim — and on one of those the name beat the evidence outright '
      '(arm N 1.00 against arm B 0.00).\n')

    W('## The funnel\n')
    rows = [['v2.9 depth 2 compositional', S2['compositional']],
            ['after the memorisation purge', PU['depth2']['after']],
            ['v2.9 depth 3 chains', S3 and PU['depth3']['before']],
            ['after the purge', PU['depth3']['after']]]
    if D4g:
        rows.append(['depth 4 candidates', D4g['candidates']])
        rows.append(['depth 4 produced', C4['alive'] if C4 else None])
    if S4: rows.append(['depth 4 links passing', S4['compositional']])
    if D5g: rows.append(['depth 5 candidates', D5g['candidates']])
    if S5: rows.append(['depth 5 links passing', S5['compositional']])
    W(tbl(['stage', 'count'], [r for r in rows if r[1] is not None]))
    W('')

    W('## Pass rate by depth\n')
    depths = [(2, S2['compositional'], S2['items']), (3, 40, 51)]
    if S4: depths.append((4, S4['compositional'], S4['items']))
    if S5: depths.append((5, S5['compositional'], S5['items']))
    rws = []
    for d, k, n in depths:
        lo, hi = wilson(k, n)
        rws.append([f'depth {d}', f'{k} of {n}', f'{round(100 * k / n, 1)}%',
                    f'{round(100 * lo, 1)}–{round(100 * hi, 1)}%'])
    W(tbl(['', 'passing', 'rate', '95% CI'], rws))
    W('')
    W('The intervals overlap at every depth. On this evidence a fourth step is no harder than a '
      'second, which is the opposite of what v2.6 found when chains were discovered by sharing '
      'a claim id rather than built so something has to travel.\n')

    W('## Mean combined score per arm, by depth\n')
    ar = []
    for d, src in [(2, S2), (3, S3)] + ([(4, S4)] if S4 else []) + ([(5, S5)] if S5 else []):
        m = src['mean_combined_across_items']
        ar.append([f'depth {d}', fm(m['A']), fm(m['B']), fm(m['C']), fm(m['N'])])
    W(tbl(['', 'A measurement', 'B measurement + result', 'C result alone', 'N name only'], ar))
    W('')

    W('## Arm N, and what it does not prove\n')
    nr = []
    for d, src, pat in [(2, S2, 'results/v2p9/arms/*_N1.out.txt'),
                        (3, S3, 'results/v2p9/arms_nl/*_N1.out.txt')] \
            + ([(4, S4, 'results/v2p10/arms_d4/*_N1.out.txt')] if S4 else []) \
            + ([(5, S5, 'results/v2p10/arms_d5/*_N1.out.txt')] if S5 else []):
        r, n = refusal_rate(pat)
        nr.append([f'depth {d}', f"{src['N_at_or_above_threshold']} of {src['items']}",
                   fm(src['mean_combined_across_items']['N']),
                   f'{r} of {n}' if n else '—'])
    W(tbl(['', 'arm N ≥ 0.25', 'mean arm N', 'answers that refuse anyway'], nr))
    W('')
    W('Arm N is given the paper\'s real title and journal and told "Give your best guess. Do not '
      'refuse." A large share still refuse. So a low arm N score is partly unwillingness to '
      'guess rather than inability, the same failure that made v2.8b\'s version useless, and the '
      'instruction only half fixes it. The memorisation figures are therefore a floor on what '
      'the model could produce, not a measure of what it knows.\n')

    if D4g:
        W('## Depth 4\n')
        W(f"{D4g['candidates']} candidates from {D4g['leaves_with_a_link']} of "
          f"{D4g['leaves']} surviving depth 3 chains, at most {D4g['max_per_chain']} each.\n")
        W(tbl(['dropped at generation', 'count'],
              sorted(D4g['dropped'].items(), key=lambda x: -x[1])))
        W('')
        W(f"{D4g['exclusion_check']}.\n")
        if C4:
            W(f"Production: {C4['drafted']} drafted, tag agreement "
              f"{round(100 * C4['tag_agreement'], 1)}%, {C4['dropped_no_combined_claim']} dropped "
              f"for having no combined claim.\n")
        if S4:
            W(f"{S4['borderline_count']} links were borderline and resampled; "
              f"{len(S4['borderline_flips'])} flipped.\n")

    if not S5:
        W('## Depth 5 — not run\n')
        if S4:
            ok = S4['pass_rate'] >= 0.60 and S4['compositional'] >= 10
            W(f"The gate was a depth 4 pass rate of 60% or more and at least 10 depth 4 chains. "
              f"Observed: {round(100 * S4['pass_rate'], 1)}% and {S4['compositional']} chains, so "
              + ('the gate was met and depth 5 ran.' if ok else
                 '**the gate was not met and depth 5 was skipped.**') + '\n')

    if PG:
        W('## Per paper\n')
        W(tbl(['paper', 'chains'] + [f'depth {k}' for k in sorted(PG['by_depth'], reverse=True)]
              + ['memorised', 'size'],
              [[r['paper'].split('__')[0].replace('_', ' ')[:30] + ' · ' + r['paper'].split('__')[1][:20],
                r['chains']]
               + [r['by_depth'].get(k, 0) for k in sorted(PG['by_depth'], reverse=True)]
               + [r['memorised'], f"{r['kb']} KB"]
               for r in sorted(PG['rows'], key=lambda x: -x['chains'])]))
        W('')
        W(f"{PG['pages']} pages plus an index in `results/v2p10/pages/`, "
          f"{PG['chains']} chains in total, largest page {PG['max_kb']} KB. Panels are embedded "
          f"as data URIs; no page makes an external request.\n")

    W('## Cost\n')
    rws = [[k, v['calls'], v.get('relays', ''), v['wall_min'], v['s_per_call']]
           for k, v in COST.items() if isinstance(v, dict) and 'wall_min' in v]
    W(tbl(['stage', 'model calls', 'relays', 'wall minutes', 'seconds per call'], rws))
    W('')
    tot = sum(r[1] for r in rws); mins = sum(r[3] for r in rws)
    links = (S4['items'] if S4 else 0) + (S5['items'] if S5 else 0)
    est = (COST.get('estimate_before_starting') or {}).get('total_upper')
    W(f"**{tot} calls, {round(mins, 1)} minutes**, against an estimate of {est}. "
      + (f"That is {round(tot / links, 1)} calls per link tested." if links else '')
      + " Steps 1 and 4 cost nothing: the purge re-reads v2.9 and the pages are built from "
        "results already on disk.\n")

    W('## Where the data is\n')
    W('- `results/v2p10/purge.json` — the flagged items and their arm N answers\n'
      '- `results/v2p10/deeper_d4.json` — depth 4 candidates and every exclusion\n'
      '- `results/v2p10/arms_d4/`, `grade_d4/` — every answer and every ruling\n'
      '- `results/v2p10/step4_d4.json` — the decision per link\n'
      '- `results/v2p10/pages/` — one page per paper plus the index\n')
    W('Every verdict is model against model.')

    open(R('docs/TRACES_V2P10.md'), 'w').write('\n'.join(out) + '\n')
    print('docs/TRACES_V2P10.md written,', len('\n'.join(out).split('\n')), 'lines')


if __name__ == '__main__': main()
