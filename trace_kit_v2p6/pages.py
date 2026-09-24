"""pages.py: v2.6 step 7 -- the v2.5 pages, with each seam's three v2.6 gates on it.

  python3 -m trace_kit_v2p6.pages

The v2.5 builder does the work. This module loads it, replaces its seam and trace-card writers
with ones that add the v2.6 verdicts, and forks only `build` and `main`, which is where the
summary line, the trace table and the index live. Everything else -- the CSS, the thumbnailer,
the graph SVG, the item card, the merge map, the MatMech audit box -- is the v2.5 code unchanged.

Per seam the page now says: upstream ignored or not, the scope verdict, the necessity verdict of
the chains it lies on, and whether the merge is counted. A seam that fails is not removed. It
stays where it was, labelled a failed merge, because a merge that does not hold is the clearest
thing on the page.

"Every limit survives" is withdrawn wherever the upstream result was ignored: there was nothing
for a limit to survive into.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
import pages as p5  # noqa: E402

E = p5.E
CNT = {}   # seam key -> step 3/4/6 row
CHN = {}   # chain path tuple -> step 5/6 row

EXTRA3 = """
.g{display:inline-block;font:600 10.5px ui-monospace,Menlo,monospace;padding:2px 7px;border-radius:5px;
margin:0 5px 3px 0;border:1px solid var(--line);background:var(--card)}
.g.pass{background:rgba(42,125,96,.14);border-color:var(--acc);color:var(--acc)}
.g.fail{background:rgba(224,163,58,.16);border-color:var(--warn);color:#8a5d06}
.gates{margin:9px 0 0;padding:9px 11px;border-radius:8px;background:var(--card);border:1px solid var(--line)}
.gates b{font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.counted{background:var(--acc);color:#fff;padding:6px 11px;border-radius:7px;font-size:12.5px;
font-weight:600;margin:9px 0 0;display:inline-block}
.failed{background:var(--warn);color:#fff;padding:6px 11px;border-radius:7px;font-size:12.5px;
font-weight:600;margin:9px 0 0;display:inline-block}
.trace.comp{border-color:var(--acc);border-width:2px}
.trace.nocomp{border-color:var(--line)}
.idx td.c{font-weight:700;color:var(--acc)}
"""


def gate_block(k):
    """the three v2.6 gates for one seam"""
    s = CNT.get(k)
    if not s:
        return ('<div class="gates"><b>v2.6</b><br><span class="g">no v2.6 ruling</span> '
                'this seam was not carried into v2.6.</div>')
    A = ['<div class="gates"><b>v2.6 &mdash; does this merge count?</b><br>']
    A.append(f'<span class="g {"fail" if s["upstream_ignored"] else "pass"}">step 3 '
             + ('upstream ignored' if s['upstream_ignored'] else 'upstream result is used')
             + '</span>')
    sc = s.get('scope') or 'unruled'
    A.append(f'<span class="g {"pass" if s["gate4"] else "fail"}">step 4 scope: {E(sc)}</span>')
    nec = s.get('necessity_of_chains')
    A.append(f'<span class="g {"pass" if nec == "yes" else "fail"}">step 5 necessity: {E(str(nec))}</span>')
    if s['upstream_ignored']:
        A.append('<p class="sub">The join audit said the downstream claim never uses what the '
                 'upstream item concluded, so no limit of the upstream could survive into it. '
                 '&ldquo;Every limit survives&rdquo; is withdrawn for this seam.</p>')
        if s.get('ignored_signals'):
            A.append(f'<p class="sub">signal: {E("; ".join(s["ignored_signals"]))}</p>')
    if s.get('scope_why'):
        A.append(f'<p class="sub">scope: {E(str(s["scope_why"])[:320])}</p>')
    A.append(f'<div class="{"counted" if s["counted"] else "failed"}">'
             + ('this merge counts' if s['counted'] else 'failed merge &mdash; kept as a negative example')
             + '</div></div>')
    return '\n'.join(A)


_seam = p5.seam


def seam(j, r, N, upstream_item):
    h, dropped = _seam(j, r, N, upstream_item)
    k = f"{j['from']}__{j['to']}"
    s = CNT.get(k) or {}
    if s.get('upstream_ignored'):
        # the seam may have shown no dropped limit only because nothing could be dropped
        h = h.replace('<div class="lims"><b>what happens to the upstream item&rsquo;s limits</b>',
                      '<div class="lims"><b>what the audit did with the upstream item&rsquo;s '
                      'limits &mdash; withdrawn, see below</b>')
    assert h.endswith('</div>')
    return h[:-len('</div>')] + gate_block(k) + '</div>', dropped


p5.seam = seam
_trace_card = p5.trace_card


def trace_card(c, idx, jns, joins, byitem, N, audit, qk, inval, P, shown, seen_seams):
    h = _trace_card(c, idx, jns, joins, byitem, N, audit, qk, inval, P, shown, seen_seams)
    row = CHN.get(tuple(c['path'])) or {}
    ign = [k for k in row.get('seams', []) if (CNT.get(k) or {}).get('upstream_ignored')]
    if ign:
        h = h.replace('<span class="v carried">every limit survives</span>',
                      f'<span class="v dropped">upstream ignored at {len(ign)} seam(s)</span>')
    comp = row.get('compositional')
    badge = ('<span class="v carried">compositional merge</span>' if comp
             else '<span class="v dropped">not a compositional merge</span>')
    nec = row.get('necessity')
    votes = '/'.join(row.get('votes') or []) or 'no ruling'
    extra = (f' &middot; {badge} &middot; necessity {E(str(nec))} ({E(votes)})'
             f'{" &middot; " + str(len(row.get("openers") or [])) + " ways in" if len(row.get("openers") or []) > 1 else ""}')
    # the badge goes at the end of the trace header line
    mark = '</div>'
    i = h.find(mark, h.find('<div class="thead">'))
    h = h[:i] + extra + h[i:]
    h = h.replace('<div class="trace" id=', f'<div class="trace {"comp" if comp else "nocomp"}" id=', 1)
    return h


p5.trace_card = trace_card


def load26():
    C = json.load(open(R('results/v2p6/counted.json')))
    P = json.load(open(R('results/v2p6/pruned.json')))
    nec_of = collections.defaultdict(set)
    for c in C['chains_out']:
        for k in c['seams']: nec_of[k].add(c.get('necessity'))
    for k, s in C['seams_out'].items():
        v = nec_of.get(k) or set()
        s['necessity_of_chains'] = 'yes' if 'yes' in v else ('no' if 'no' in v else None)
    CNT.update(C['seams_out'])
    for c in C['chains_out']: CHN[tuple(c['path'])] = c
    return C, P


def build(paper, D, C26, P26, D5, C5, PAIRS, inval, V5, S5, audit, qk, joins):
    """a fork of p5.build: same page, plus the v2.6 gates in the summary, table and index"""
    gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
    g = json.load(open(R(gp))); N = {n['id']: n for n in g['nodes']}
    live = set(P26['items'])
    its = [i for i in D if i['paper'] == paper and i['item'] in live]
    byitem = {i['item']: i for i in D}
    for b in P26['backbone']:
        if b in V5: byitem.setdefault(b, {**V5[b], '_bb': True})
    chains = sorted([c for c in C26['chains_out'] if c['paper'] == paper], key=lambda c: -c['depth'])
    jns = [j for j in P26['joins'] if j['paper'] == paper]
    rej = [r for r in P26['rejected'] if r['paper'] == paper]
    att = [a for a in P26['attachments'] if a['paper'] == paper]
    used = {c for i in its for c in i['claims']} | \
           {i[s]['node'] for i in its for s in ('observation_a', 'observation_b')}
    P = p5.figs_for(paper)
    ks = [p5.jkey(joins.get((j['from'], j['to']))) for j in jns]
    laund = sum(1 for k in ks if k and k['launders'])
    keepall = 0
    for c in chains:
        cks = [p5.jkey(joins.get(j)) for j in zip(c['path'], c['path'][1:])]
        ign = any((CNT.get(f'{a}__{b}') or {}).get('upstream_ignored')
                  for a, b in zip(c['path'], c['path'][1:]))
        if all(cks) and not any(k['launders'] for k in cks) and not ign: keepall += 1
    s = {'items': len(its),
         'comp': sum(1 for i in its if i['generator'] == 'complementary'),
         'edge': sum(1 for i in its if i['generator'] == 'spine_edge'),
         'disc': sum(1 for i in its if ((i.get('key') or {}).get('labels') or {}).get('causal_strength') == 'discriminating'),
         'fm': sum(1 for i in its if i.get('fm_lane')),
         'chains': len(chains), 'compositional': sum(1 for c in chains if c['compositional']),
         'max_depth': max([c['depth'] for c in chains], default=0),
         'joins': len(jns), 'seams_counted': sum(1 for j in jns
                                                 if (CNT.get(f"{j['from']}__{j['to']}") or {}).get('counted')),
         'ignored': sum(1 for j in jns
                        if (CNT.get(f"{j['from']}__{j['to']}") or {}).get('upstream_ignored')),
         'rejected': len(rej), 'launder': laund, 'keepall': keepall,
         'conv': sum(1 for c in P26['convergence'] if c['paper'] == paper)}
    short = paper.split('__')[0].replace('_', ' ')
    A = ['<!doctype html><html lang="en"><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{E(short)} — v2.6</title><style>{p5.CSS}{p5.EXTRA}{p5.EXTRA2}{EXTRA3}</style>'
         '<body><div class="wrap">',
         f'<h1>{E(short)}</h1><p class="sub">{E(paper)} &middot; v2.6</p>',
         '<p class="mvm">Every verdict is model against model.</p>',
         f'<p class="lead"><b>{s["items"]} two-step items</b> &mdash; {s["comp"]} complementary, '
         f'{s["edge"]} spine edge &middot; {s["disc"]} discriminating &middot; {s["fm"]} FM lane '
         f'&middot; <b>{s["chains"]} merged traces</b>, <b>{s["compositional"]} compositional</b>'
         + (f', deepest {s["max_depth"]}' if s['chains'] else '')
         + f' &middot; {s["joins"]} seams, {s["seams_counted"]} counted, {s["ignored"]} ignoring '
         f'the upstream result, {s["launder"]} laundering a limit &middot; {s["rejected"]} joins '
         'rejected' + (f' &middot; {s["conv"]} convergence claim(s)' if s['conv'] else '') + '</p>',
         '<p class="sub">v2.6 drops the covariation generator, collapses traces that differ only '
         'in their opener, and counts a merge only when the upstream result is used, its scope '
         'fits, and removing it changes the last answer.</p>',
         '<h2><span class="n">1</span>The original graph</h2>',
         f'<p class="lead">Drawn from <code>{E(gp)}</code>, the graph these items were built on.</p>',
         p5.graph_svg(g, used),
         p5.matmech_section(paper, {'backbone': P26['backbone']}, V5, S5),
         p5.cut_section(paper, D, chains)]

    A.append('<h2><span class="n">4</span>How the items merge</h2>')
    if not chains:
        A.append(f'<div class="nomerge"><b>Nothing merged.</b> {p5.NO_MERGE}</div>')
    else:
        A.append('<p class="lead">Every box is a two-step item. A round node between two boxes is '
                 'the claim they join on. Edge colour is the v2.5 join audit; the v2.6 verdicts '
                 'are in the table and on every seam.</p>')
        A.append(p5.merge_map(paper, chains, jns, joins, byitem, rej, att, N))
        A.append('<table class="tt"><thead><tr><th>trace</th><th>depth</th><th>ways in</th>'
                 '<th>items in order</th><th>upstream used</th><th>scope</th>'
                 '<th>necessity</th><th>compositional</th></tr></thead><tbody>')
        for i, c in enumerate(chains, 1):
            A.append(f'<tr><td><a href="#trace-{i}">trace-{i}</a></td><td>{c["depth"]}</td>'
                     f'<td>{len(c["openers"])}</td>'
                     f'<td>{E(" &rarr; ".join(c["path"]))}</td>'
                     f'<td>{"yes" if c["gate3"] else "no"}</td>'
                     f'<td>{"ok" if c["gate4"] else "failed"}</td>'
                     f'<td>{E(str(c.get("necessity")))} ({E("/".join(c.get("votes") or []) or "&mdash;")})</td>'
                     f'<td class="{"c" if c["compositional"] else ""}">'
                     f'{"yes" if c["compositional"] else "no"}</td></tr>')
        A.append('</tbody></table>')
    if rej:
        A.append('<h3>joins rejected</h3><table class="tt"><thead><tr><th>join</th><th>why</th>'
                 '</tr></thead><tbody>')
        for r in rej:
            A.append(f'<tr style="opacity:.55"><td>{E(r["from"])} &rarr; {E(r["to"])}</td>'
                     f'<td>{E(r["why"])}</td></tr>')
        A.append('</tbody></table>')
    if att:
        A.append('<h3>attachments</h3><table class="tt"><thead><tr><th>item</th><th>generator</th>'
                 '<th>hangs off claim</th><th>where</th></tr></thead><tbody>')
        for a in att:
            A.append(f'<tr><td>{E(a["item"])}</td><td>{E(a["generator"])}</td>'
                     f'<td>{E(", ".join(a["attachment_claim"]))}</td><td>{E(a["where"])}</td></tr>')
        A.append('</tbody></table>')

    A.append('<h2><span class="n">5</span>The merged traces</h2>')
    shown, seen_seams = set(), {}
    if not chains:
        A.append(f'<div class="nomerge">{p5.NO_MERGE}</div>')
    else:
        A.append('<p class="lead">One card per merged trace, deepest first. Between two step '
                 'blocks a <b>merge seam</b> shows what happened to the upstream limits and, '
                 'below that, the three v2.6 gates and whether the merge counts.</p>')
        for i, c in enumerate(chains, 1):
            A.append(p5.trace_card(c, i, jns, joins, byitem, N, audit, qk, inval, P,
                                   shown, seen_seams))

    A.append('<h2><span class="n">6</span>Items outside any merged trace</h2>')
    inmerge = {n for c in chains for n in c['path']}
    rest = [i for i in its if i['item'] not in inmerge]
    attmap = {a['item']: a for a in att}
    if not rest:
        A.append('<p class="sub">None &mdash; every item merged.</p>')
    else:
        A.append(f'<p class="lead">{len(rest)} item(s) did not merge.</p>')
        byg = collections.defaultdict(list)
        for i in rest: byg[i['generator']].append(i)
        for gname in ('complementary', 'spine_edge'):
            grp = byg.get(gname)
            if not grp: continue
            A.append(f'<div class="gen">{E(gname)} &mdash; {len(grp)} items</div>')
            for i in sorted(grp, key=lambda x: x['item']):
                if i['item'] in attmap:
                    a = attmap[i['item']]
                    A.append(f'<h3>attaches to the trace claim {E(", ".join(a["attachment_claim"]))}</h3>')
                A.append(p5.item_card(i, audit, qk, inval, P))
    A.append(p5.convergence_section(paper, {'convergence': P26['convergence']}, byitem))
    A.append('</div></body></html>')
    return '\n'.join(A), s


def main():
    D5, C5, PAIRS, inval, V5, S5, audit, qk, joins = p5.load()
    C26, P26 = load26()
    papers = [x['paper'] for x in json.load(open(R('results/v5_papers.json')))]
    out = R('results/v2p6/pages'); os.makedirs(out, exist_ok=True)
    rows = []
    for p in papers:
        html_, s = build(p, D5, C26, P26, D5, C5, PAIRS, inval, V5, S5, audit, qk, joins)
        f = os.path.join(out, p + '.html')
        open(f, 'w').write(html_)
        s['paper'] = p; s['kb'] = os.path.getsize(f) // 1024
        rows.append(s)
    keys = ('items', 'comp', 'edge', 'disc', 'fm', 'chains', 'compositional', 'joins',
            'seams_counted', 'ignored', 'rejected', 'launder', 'keepall', 'conv')
    T = {k: sum(r[k] for r in rows) for k in keys}
    A = ['<!doctype html><html lang="en"><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>v2.6 — 32 papers</title><style>{p5.CSS}{p5.EXTRA}{p5.EXTRA2}{EXTRA3}</style>'
         '<body><div class="wrap">',
         '<h1>Traces v2.6 — only the merges that hold</h1>',
         '<p class="mvm">Every verdict is model against model.</p>',
         '<p class="lead">Same 32 papers and the same two-step items as v2.5. What changed is '
         'which merges count: the covariation generator is gone, traces that differ only in their '
         'opener are one trace, and a merge is counted only when the downstream uses the upstream '
         'result, the scope fits, and the last answer changes without it. Numbers agree with '
         'docs/TRACES_V2P6.md.</p>',
         '<table class="idx"><thead><tr><th>paper</th><th>items</th><th>comp</th><th>edge</th>'
         '<th>disc</th><th>FM</th><th>traces</th><th>compositional</th><th>depth</th>'
         '<th>seams</th><th>counted</th><th>ignored</th><th>launder</th><th>rej</th>'
         '<th>size</th></tr></thead><tbody>']
    for r in rows:
        A.append(f'<tr><td><a href="{E(r["paper"])}.html">'
                 f'{E(r["paper"].split("__")[0].replace("_"," ")[:36])}</a></td>'
                 f'<td>{r["items"]}</td><td>{r["comp"]}</td><td>{r["edge"]}</td>'
                 f'<td>{r["disc"]}</td><td>{r["fm"]}</td><td>{r["chains"]}</td>'
                 f'<td class="c">{r["compositional"]}</td><td>{r["max_depth"] or "&mdash;"}</td>'
                 f'<td>{r["joins"]}</td><td>{r["seams_counted"]}</td><td>{r["ignored"]}</td>'
                 f'<td>{r["launder"]}</td><td>{r["rejected"]}</td><td>{r["kb"]} KB</td></tr>')
    A.append('<tr><td><b>total</b></td>' + ''.join(
        f'<td><b>{T[k]}</b></td>' for k in ('items', 'comp', 'edge', 'disc', 'fm', 'chains',
                                            'compositional')) +
        '<td>&mdash;</td>' + ''.join(
        f'<td><b>{T[k]}</b></td>' for k in ('joins', 'seams_counted', 'ignored', 'launder',
                                            'rejected')) + '<td></td></tr>')
    A.append('</tbody></table></div></body></html>')
    open(os.path.join(out, 'index.html'), 'w').write('\n'.join(A))
    ph = collections.Counter(k for _, k in p5.PLACEHOLDERS)
    print(f'{len(rows)} pages + index')
    print(f'totals: {T}')
    print(f'image fallbacks: {dict(ph)}')
    json.dump({'totals': T, 'rows': rows, 'fallbacks': dict(ph)},
              open(R('results/v2p6/pages_report.json'), 'w'), indent=1)


if __name__ == '__main__': main()
