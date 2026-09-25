"""partE.py: v2.8 Part E -- one audit page per item, for a person to mark up.

  python3 -m trace_kit_v2p8.partE

Every machine verdict in this pilot rests on two model judgements: the claim tags from Part A
and the stated/absent rulings from Part C. Both are checkable by a person in a few minutes if
the evidence is laid next to them, and neither has ever been checked by one. These pages exist
so that happens.

Each page carries the earlier result, the new measurement, the claim list with its tags and
which of the two agents agreed, one answer from each arm with the grader's ruling and quote on
every claim, and an empty box beside each tag and each ruling. Nothing is filled in. The boxes
are the deliverable.

A note on the brief. Part E commissions these pages; the stop rules say not to build pages in
the pilot. Read together, the stop rule is about the per-paper trace pages that v2.6 step 7
would have produced -- pipeline output that presents results as settled -- and not about an
audit pack whose whole purpose is to let a person contradict the machine. So this is built and
no trace pages are.

Every verdict is model against model, which is exactly the problem these pages are for.
"""
import html, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v5'))
from paper_report import CSS, thumb  # noqa: E402

E = html.escape
OUT = R('results/v2p8/audit')

EXTRA = """
.box{display:inline-block;width:15px;height:15px;border:1.6px solid var(--ink);border-radius:3px;
vertical-align:-2px;margin-right:7px}
.boxes{white-space:nowrap;font-size:11.5px;color:var(--mut)}
.boxes b{font-weight:600;color:var(--ink)}
.cl{border:1px solid var(--line);border-radius:9px;padding:10px 13px;margin:8px 0;background:var(--card)}
.cl.combined{border-left:4px solid var(--acc)}
.cl.limit{border-left:4px solid var(--warn)}
.tag{display:inline-block;font:600 10px ui-monospace,Menlo,monospace;text-transform:uppercase;
letter-spacing:.05em;padding:2px 7px;border-radius:4px;background:var(--chip);margin-right:8px}
.tag.combined{background:rgba(42,125,96,.16);color:var(--acc)}
.tag.limit{background:rgba(224,163,58,.18);color:#8a5d06}
.arm{border:1px solid var(--line);border-radius:11px;padding:0;margin:14px 0;overflow:hidden}
.armh{background:var(--chip);padding:9px 13px;font:600 12.5px system-ui;border-bottom:1px solid var(--line)}
.armb{padding:12px 14px;font-size:13.5px;white-space:pre-wrap}
.rul{font-size:12.5px;padding:8px 14px;border-top:1px dashed var(--line)}
.v{display:inline-block;font:600 10px ui-monospace,Menlo,monospace;padding:2px 6px;border-radius:4px;
margin-right:7px;text-transform:uppercase}
.v.stated{background:rgba(42,125,96,.16);color:var(--acc)}
.v.absent{background:var(--chip);color:var(--mut)}
.v.contradicted{background:var(--warn);color:#fff}
.q{color:var(--mut);font-style:italic}
.num{border-collapse:collapse;margin:10px 0;font-size:13px}
.num td,.num th{border:1px solid var(--line);padding:5px 10px;text-align:right}
.num th:first-child,.num td:first-child{text-align:left}
.hdr{background:var(--chip)}
"""

BOXES = ('<span class="boxes"><span class="box"></span><b>agree</b>&nbsp;&nbsp;'
         '<span class="box"></span><b>disagree</b></span>')


def page(it, S, A, Cc, D, DI, keys):
    s = next(x for x in S if x['item'] == it)
    x = DI[it]
    a = A['claims'][it]
    d = D['items_out'][it]
    P = [f'<!doctype html><html lang="en"><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{E(it)} — v2.8 audit</title><style>{CSS}{EXTRA}</style><body><div class="wrap">',
         f'<h1>{E(s["journal"].replace("_", " "))}</h1>',
         f'<p class="sub"><code>{E(it)}</code> &middot; {E(s["paper"])}</p>',
         '<p class="mvm">Every verdict is model against model. This page is for a person to '
         'disagree with one.</p>',
         f'<p class="lead">Drafter label <b>{E(s["cs"])}</b> &middot; upstream '
         f'<code>{E(s["upstream"])}</code> ({E(s["up_gen"])}) &middot; edge {E(x["edge"])} '
         f'&middot; {d["n_combined"]} combined claims, {d["n_limit"]} limit claims</p>',

         '<h2><span class="n">1</span>What the earlier step established</h2>',
         f'<p>{E(x["input_result"])}</p>',
         '<p class="sub"><b>qualifications recorded on it</b></p><ul>']
    for t in x['input_limits']: P.append(f'<li>{E(str(t))}</li>')
    P.append('</ul>')

    P += ['<h2><span class="n">2</span>The new measurement</h2>',
          f'<p><code>{E(x["new_observation"]["node"])}</code> {E(x["new_observation"]["text"])}</p>']
    for p in x['panels']:
        src = thumb(p['crop'], 620) if p.get('crop') and os.path.exists(p['crop']) else None
        if src:
            P.append(f'<figure class="pan"><img src="{src}" alt="{E(p["suffix"])}">'
                     f'<figcaption class="cap">{E(p["suffix"])}</figcaption></figure>')
    P.append('<p class="sub">These panels do not appear in the upstream item; the exclusion was '
             'checked by node id and by panel id when the item was built.</p>')

    P += ['<h2><span class="n">3</span>The claims, and their tags</h2>',
          '<p class="lead">One agent proposed each tag; a second, shown only the earlier result '
          'and the measurement, ruled it. Only claims both tagged the same are scored. Tick a box '
          'if you agree or disagree with the tag.</p>']
    for c in a['kept']:
        P.append(f'<div class="cl {c["tag"]}"><span class="tag {c["tag"]}">{E(c["tag"])}</span>'
                 f'{E(c["claim"])}<div style="margin-top:7px">{BOXES}</div></div>')
    if a['dropped']:
        P.append('<h3>claims the two agents tagged differently, and so are not scored</h3>')
        for c in a['dropped']:
            P.append(f'<div class="cl"><span class="tag">{E(c["tag"])} &rarr; '
                     f'{E(str(c.get("correct_tag")))}</span>{E(c["claim"])}'
                     f'<div class="sub">{E(str(c.get("why")))}</div>'
                     f'<div style="margin-top:7px">{BOXES}</div></div>')
    P.append('<h3>limit claims, carried from the key and not tagged</h3>')
    for c in a['limits']:
        P.append(f'<div class="cl limit"><span class="tag limit">limit</span>{E(c["claim"])}'
                 f'<div style="margin-top:7px">{BOXES}</div></div>')

    P += ['<h2><span class="n">4</span>The numbers</h2>',
          '<table class="num"><tr class="hdr"><th>arm</th><th>what it held</th>'
          '<th>mean combined</th><th>mean limit</th><th>mean contradictions</th></tr>']
    what = {'A': 'the measurement alone', 'B': 'measurement + earlier result',
            'C': 'the earlier result alone'}
    for arm in ('A', 'B', 'C'):
        P.append(f'<tr><td><b>{arm}</b></td><td>{what[arm]}</td>'
                 f'<td>{d["mean_combined"][arm]:.3f}</td>'
                 f'<td>{"" if d["mean_limit"][arm] is None else f"{d[chr(39)+chr(39)] if False else d["mean_limit"][arm]:.3f}"}</td>'
                 f'<td>{d["mean_contradictions"][arm]:.2f}</td></tr>')
    P.append('</table>')
    P.append(f'<p>B &minus; A = <b>{d["B_minus_A"]:+.3f}</b> &rarr; input needed: '
             f'<b>{"yes" if d["input_needed"] else "no"}</b> &middot; '
             f'B &minus; C = <b>{d["B_minus_C"]:+.3f}</b> &rarr; observation needed: '
             f'<b>{"yes" if d["observation_needed"] else "no"}</b> &middot; '
             f'compositional: <b>{"yes" if d["compositional"] else "no"}</b> '
             f'(margin {D["margin"]})</p>')
    P.append(f'<p class="sub">split halves agree: '
             f'<b>{"yes" if d["halves_agree"] else "no"}</b> &mdash; '
             f'samples 1-3 say {d["halves"]["first"]["compositional"]}, '
             f'samples 4-6 say {d["halves"]["second"]["compositional"]}</p>')

    P.append('<h2><span class="n">5</span>One answer from each arm, with the grader&rsquo;s '
             'rulings</h2>')
    P.append('<p class="lead">The grader saw only the answer and the claim list &mdash; never '
             'the arm, the other answers, the earlier result or the measurement. Tick a box '
             'beside any ruling you would have made differently.</p>')
    for arm in ('A', 'B', 'C'):
        key = f'{it}_{arm}1'
        ans = Cc['answers'].get(key)
        if not ans: continue
        raw = open(R('results/v2p8/arms', f'{it}_{arm}1.out.txt')).read()
        from trace_kit_v2p6.clean import clean
        P.append(f'<div class="arm"><div class="armh">arm {arm} &mdash; {what[arm]} '
                 f'&middot; combined {ans["combined_score"]:.2f}, '
                 f'limits {"" if ans["limit_score"] is None else f"{ans[chr(39)+chr(39)] if False else ans["limit_score"]:.2f}"}, '
                 f'{ans["contradictions"]} contradiction(s)</div>')
        P.append(f'<div class="armb">{E(clean(raw))}</div>')
        for r in ans['rulings']:
            P.append(f'<div class="rul"><span class="v {E(r["verdict"])}">{E(r["verdict"])}</span>'
                     f'<span class="tag {E(r["kind"])}">{E(r["kind"])}</span>{E(r["claim"])}'
                     + (f'<div class="q">&ldquo;{E(r["quote"])}&rdquo;</div>' if r['quote'] else '')
                     + f'<div style="margin-top:6px">{BOXES}</div></div>')
        P.append('</div>')
    P.append('</div></body></html>')
    return '\n'.join(P)


def run():
    os.makedirs(OUT, exist_ok=True)
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    A = json.load(open(R('results/v2p8/partA.json')))
    Cc = json.load(open(R('results/v2p8/partC.json')))
    D = json.load(open(R('results/v2p8/partD.json')))
    DI = {x['item']: x for x in json.load(open(R('results/v2p7/derived_input.json')))['items_out']}
    keys = json.load(open(R('results/v2p7/partE.json')))['keys']
    rows = []
    for s in S:
        it = s['item']
        h = page(it, S, A, Cc, D, DI, keys)
        f = os.path.join(OUT, it + '.html'); open(f, 'w').write(h)
        rows.append({'item': it, 'kb': os.path.getsize(f) // 1024,
                     'compositional': D['items_out'][it]['compositional']})
    idx = ['<!doctype html><html lang="en"><meta charset="utf-8">',
           f'<title>v2.8 audit pack</title><style>{CSS}{EXTRA}</style><body><div class="wrap">',
           '<h1>v2.8 pilot — audit pack</h1>',
           '<p class="mvm">Every verdict is model against model. These pages are for a person '
           'to disagree with one.</p>',
           '<p class="lead">Eight items. Each page carries the earlier result, the new '
           'measurement, the claim list with its tags, the arm means, and one answer per arm '
           'with the grader&rsquo;s ruling and quote on every claim. Every tag and every ruling '
           'has an empty agree/disagree box. None is filled in.</p>',
           '<table class="num"><tr class="hdr"><th>item</th><th>compositional</th><th>size</th></tr>']
    for r in rows:
        idx.append(f'<tr><td><a href="{E(r["item"])}.html">{E(r["item"])}</a></td>'
                   f'<td>{"yes" if r["compositional"] else "no"}</td><td>{r["kb"]} KB</td></tr>')
    idx.append('</table></div></body></html>')
    open(os.path.join(OUT, 'index.html'), 'w').write('\n'.join(idx))
    print(f'{len(rows)} audit pages + index')
    json.dump(rows, open(R('results/v2p8/audit_report.json'), 'w'), indent=1)
    return rows


if __name__ == '__main__': run()
