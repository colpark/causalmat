"""pages.py: v2.10 Step 4 -- one page per paper with a passing chain.

  python3 -m trace_kit_v2p10.pages

No model call. Everything on these pages was computed earlier; this only lays it out so a chain
can be read end to end.

The product is the chain. A card shows its links deepest first, each as a block carrying the
result it was handed, the new observation with its panels, the question, the key's combined
claims and limits, and the four arm scores. Between two blocks a band names what travels: the
previous link's proposition, verbatim. That band is the whole claim of this project -- if the
text in it did no work, arm C would have scored as well as arm B, and the numbers on either
side of it say whether it did.

Memorised items get their own section at the end, marked excluded, with what arm N said. They
are on the page because a reader should see what the corpus gives away for free.

CSS, the thumbnailer and the layered graph SVG come from trace_kit_v5/paper_report.py through
trace_kit_v2p5/pages.py, unchanged.

Every verdict is model against model.
"""
import collections, html, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import CSS, EXTRA, EXTRA2, thumb, graph_svg  # noqa: E402

E = html.escape
OUT = R('results/v2p10/pages')

EXTRA3 = """
.chain{border:2px solid var(--acc);border-radius:13px;margin:20px 0;overflow:hidden;background:var(--card)}
.chead{background:var(--chip);padding:11px 15px;font-size:13.5px;border-bottom:1px solid var(--line)}
.link{padding:13px 16px}
.link h4{margin:0 0 8px;font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.travel{background:linear-gradient(var(--chip),var(--chip));border-top:2px dashed var(--acc);
border-bottom:2px dashed var(--acc);padding:11px 16px}
.travel b{display:block;font:600 10.5px ui-monospace,Menlo,monospace;text-transform:uppercase;
letter-spacing:.05em;color:var(--acc);margin-bottom:5px}
.travel p{margin:0;font-size:13px}
.inp{background:var(--bg);border-left:3px solid var(--line);padding:8px 12px;margin:6px 0;font-size:13px}
.obs{background:var(--bg);border-left:3px solid var(--acc);padding:8px 12px;margin:6px 0;font-size:13px}
.qn{font-style:italic;color:var(--mut);font-size:12.5px;margin:6px 0}
.cl{margin:4px 0;font-size:13px;padding-left:16px;position:relative}
.cl:before{content:"▸";position:absolute;left:0;color:var(--acc)}
.cl.lim:before{content:"▹";color:var(--warn)}
.sc{border-collapse:collapse;margin:8px 0;font-size:12px}
.sc td,.sc th{border:1px solid var(--line);padding:3px 9px;text-align:right}
.sc th:first-child,.sc td:first-child{text-align:left}
.sc .hi{background:rgba(42,125,96,.14);font-weight:700}
.mem{border:1px dashed var(--warn);border-radius:10px;padding:12px 14px;margin:10px 0;font-size:13px}
.mem b{color:#8a5d06}
.idx td,.idx th{font-size:12.5px}
"""


def load():
    """one decision map per depth, keyed by link id, so nothing depends on which file it came from"""
    d = {}
    d['DEC'] = {}          # link id -> its arm decision
    d['KEY'] = {}          # link id -> its drafted key
    d['CLM'] = {}          # link id -> its kept claims and limits
    d['REC'] = {}          # link id -> the pair record (observation, panels, question)

    def add(dec_file, key_file, clm_file, src_file):
        f = R(dec_file)
        if os.path.exists(f):
            d['DEC'].update(json.load(open(f))['items_out'])
        f = R(key_file)
        if os.path.exists(f): d['KEY'].update(json.load(open(f)))
        f = R(clm_file)
        if os.path.exists(f): d['CLM'].update(json.load(open(f))['items'])
        f = R(src_file)
        if os.path.exists(f):
            d['REC'].update({x['item']: x for x in json.load(open(f))['pairs_out']})

    add('results/v2p9/step4.json', 'results/v2p9/keys.json',
        'results/v2p9/step2.json', 'results/v2p9/pairs.json')
    add('results/v2p9/step4_nl.json', 'results/v2p9/keys_nl.json',
        'results/v2p9/step2_nl.json', 'results/v2p9/nextlink.json')
    add('results/v2p10/step4_d4.json', 'results/v2p10/keys_d4.json',
        'results/v2p10/step2_d4.json', 'results/v2p10/deeper_d4.json')
    add('results/v2p10/step4_d5.json', 'results/v2p10/keys_d5.json',
        'results/v2p10/step2_d5.json', 'results/v2p10/deeper_d5.json')
    d['PU'] = json.load(open(R('results/v2p10/purge.json')))
    d['D5'] = {i['item']: i for i in
               json.load(open(R('results/v2p5/items.json')))['items']}
    return d


def rec_of(it, d): return d['REC'].get(it)
def dec_of(it, d): return d['DEC'].get(it)
def key_of(it, d): return d['KEY'].get(it) or {}
def claims_of(it, d): return d['CLM'].get(it) or {}


def steps_of(leaf, d):
    """the chain, root first. Stops at the v2.5 two-step item, which is not itself a link."""
    out, cur = [], leaf
    while cur and cur in d['REC']:
        out.append(cur)
        r = d['REC'][cur]
        nxt = r.get('parent_item') or r.get('upstream_item')
        cur = nxt if nxt in d['REC'] else None
    return list(reversed(out))


def scores_table(v):
    if not v: return ''
    m = v['mean_combined']; ml = v.get('mean_limit') or {}
    rows = [('A', 'the measurement alone'), ('B', '+ the result handed forward'),
            ('C', 'the handed result alone'), ('N', 'the paper name only')]
    h = ['<table class="sc"><tr><th>arm</th><th>what it held</th><th>combined</th><th>limits</th></tr>']
    for a, what in rows:
        cls = ' class="hi"' if a == 'B' else ''
        h.append(f'<tr{cls}><td><b>{a}</b></td><td>{what}</td><td>{m.get(a, 0):.2f}</td>'
                 f'<td>{"—" if ml.get(a) is None else f"{ml[a]:.2f}"}</td></tr>')
    h.append('</table>')
    h.append(f'<p class="sub">B&minus;A {v["B_minus_A"]:+.2f} &middot; B&minus;C '
             f'{v["B_minus_C"]:+.2f} &middot; passes: <b>'
             f'{"yes" if v["compositional"] else "no"}</b>'
             + (' &middot; borderline, decided on 2 samples' if v.get('borderline') else '')
             + '</p>')
    return '\n'.join(h)


def link_block(it, d, first):
    r = rec_of(it, d); v = dec_of(it, d); k = key_of(it, d); c = claims_of(it, d)
    H = ['<div class="link">']
    H.append(f'<h4>{"step 1 &mdash; the two-step item this chain starts from" if first else "next link"}'
             f' &middot; <code>{E(it)}</code></h4>')
    if first and r.get('input_result'):
        H.append(f'<div class="inp"><b>takes as given:</b> {E(r["input_result"][:700])}</div>')
    H.append(f'<div class="obs"><b>new measurement</b> <code>{E(r["new_observation"]["node"])}</code>'
             f' {E(r["new_observation"]["text"][:500])}</div>')
    for p in r.get('panels') or []:
        src = thumb(p['crop'], 700) if p.get('crop') and os.path.exists(p['crop']) else None
        if src:
            H.append(f'<figure class="pan"><img src="{src}" alt="{E(p["suffix"])}">'
                     f'<figcaption class="cap">{E(p["suffix"])}</figcaption></figure>')
    if r.get('question'): H.append(f'<p class="qn">{E(r["question"])}</p>')
    kept = [x for x in (c.get('kept') or []) if x['tag'] == 'combined']
    if kept:
        H.append('<p class="sub"><b>what the key says only both sides give</b></p>')
        for x in kept: H.append(f'<div class="cl">{E(x["claim"])}</div>')
    for x in (c.get('limits') or [])[:4]:
        H.append(f'<div class="cl lim">{E(x["claim"][:260])}</div>')
    H.append(scores_table(v))
    H.append('</div>')
    return '\n'.join(H)


def build():
    d = load()
    os.makedirs(OUT, exist_ok=True)
    # every passing chain, by leaf
    chains = []
    for it in d['PU']['live_depth2']:
        chains.append({'leaf': it, 'depth': 2})
    for it in d['PU']['live_depth3']:
        chains.append({'leaf': it, 'depth': 3})
    for it, v in d['DEC'].items():
        if not v.get('compositional'): continue
        if it.startswith('d4_'): chains.append({'leaf': it, 'depth': 4})
        elif it.startswith('d5_'): chains.append({'leaf': it, 'depth': 5})
    # a shorter chain fully contained in a longer passing one is not listed separately
    longest = {}
    for c in chains:
        for s in steps_of(c['leaf'], d):
            longest[s] = max(longest.get(s, 0), c['depth'])
    keep = [c for c in chains if longest.get(c['leaf'], 0) == c['depth']]

    bypaper = collections.defaultdict(list)
    for c in keep:
        r = rec_of(c['leaf'], d)
        bypaper[r['paper']].append(c)

    mem = collections.defaultdict(list)
    for m in d['PU']['memorised_record']: mem[m['paper']].append(m)

    rows = []
    for paper, cs in sorted(bypaper.items()):
        cs.sort(key=lambda c: -c['depth'])
        gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
        g = json.load(open(R(gp)))
        used = set()
        for c in cs:
            for s in steps_of(c['leaf'], d):
                r = rec_of(s, d)
                used.add(r['new_observation']['node'])
                used.add(r['target_claim']); used.add(r['claim_C'])
                for n in r.get('upstream_obs_nodes') or r.get('chain_obs_nodes') or []:
                    used.add(n)
        short = paper.split('__')[0].replace('_', ' ')
        bd = collections.Counter(c['depth'] for c in cs)
        A = ['<!doctype html><html lang="en"><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             f'<title>{E(short)} — v2.10</title><style>{CSS}{EXTRA}{EXTRA2}{EXTRA3}</style>',
             '<body><div class="wrap">',
             f'<h1>{E(short)}</h1><p class="sub">{E(paper)} &middot; v2.10</p>',
             '<p class="mvm">Every verdict is model against model.</p>',
             f'<p class="lead"><b>{len(cs)} passing chain(s)</b> &mdash; '
             + ', '.join(f'{n} at depth {k}' for k, n in sorted(bd.items(), reverse=True))
             + f' &middot; {len(mem.get(paper, []))} item(s) excluded as memorised</p>',
             '<h2><span class="n">1</span>The paper&rsquo;s argument graph</h2>',
             '<p class="lead">Every node a passing chain touches is highlighted.</p>',
             graph_svg(g, used),
             '<h2><span class="n">2</span>The chains</h2>',
             '<p class="lead">Deepest first. Each block is one link. The band between two blocks '
             'carries the previous link&rsquo;s conclusion forward, which is the thing the arm '
             'scores test.</p>']
        for i, c in enumerate(cs, 1):
            steps = steps_of(c['leaf'], d)
            A.append(f'<div class="chain"><div class="chead"><b>chain {i}</b> &middot; '
                     f'depth {c["depth"]} &middot; {len(steps)} link(s)</div>')
            for j, s in enumerate(steps):
                A.append(link_block(s, d, j == 0))
                if j < len(steps) - 1:
                    k = key_of(s, d)
                    A.append('<div class="travel"><b>what travels to the next link</b>'
                             f'<p>{E(str(k.get("proposition"))[:700])}</p></div>')
            A.append('</div>')
        if mem.get(paper):
            A.append('<h2><span class="n">3</span>Excluded as memorised</h2>')
            A.append('<p class="lead">Arm N was given only the paper&rsquo;s title and journal '
                     'and told to guess. These items reached the key from that alone, so they '
                     'are not evidence of reasoning and are excluded.</p>')
            for m in mem[paper]:
                A.append(f'<div class="mem"><b>excluded</b> <code>{E(m["item"])}</code> '
                         f'&middot; depth {m["depth"]} &middot; arm N {m["N"]:.2f}, '
                         f'arm B {m["B"]:.2f}'
                         f'<div class="sub">what the name alone produced: '
                         f'{E((m["arm_N_answer"] or "")[:500])}</div></div>')
        A.append('</div></body></html>')
        f = os.path.join(OUT, paper + '.html')
        open(f, 'w').write('\n'.join(A))
        rows.append({'paper': paper, 'chains': len(cs), 'by_depth': dict(bd),
                     'memorised': len(mem.get(paper, [])),
                     'kb': os.path.getsize(f) // 1024})

    T = collections.Counter()
    for r in rows:
        for k, n in r['by_depth'].items(): T[k] += n
    I = ['<!doctype html><html lang="en"><meta charset="utf-8">',
         f'<title>v2.10 — chains</title><style>{CSS}{EXTRA}{EXTRA2}{EXTRA3}</style>',
         '<body><div class="wrap">',
         '<h1>Traces v2.10 — chains that hold</h1>',
         '<p class="mvm">Every verdict is model against model.</p>',
         '<p class="lead">Chains built so that each step needs the one before it, and tested '
         'by grading four arms against the key&rsquo;s own claims. A chain appears here only if '
         'every one of its links passed. Numbers agree with docs/TRACES_V2P10.md.</p>',
         '<table class="idx"><thead><tr><th>paper</th><th>chains</th>'
         + ''.join(f'<th>depth {k}</th>' for k in sorted(T, reverse=True))
         + '<th>memorised</th><th>size</th></tr></thead><tbody>']
    for r in sorted(rows, key=lambda x: -x['chains']):
        I.append(f'<tr><td><a href="{E(r["paper"])}.html">'
                 f'{E(r["paper"].split("__")[0].replace("_", " ")[:34])}</a></td>'
                 f'<td>{r["chains"]}</td>'
                 + ''.join(f'<td>{r["by_depth"].get(k, 0)}</td>' for k in sorted(T, reverse=True))
                 + f'<td>{r["memorised"]}</td><td>{r["kb"]} KB</td></tr>')
    I.append(f'<tr><td><b>total</b></td><td><b>{sum(r["chains"] for r in rows)}</b></td>'
             + ''.join(f'<td><b>{T[k]}</b></td>' for k in sorted(T, reverse=True))
             + f'<td><b>{sum(r["memorised"] for r in rows)}</b></td><td></td></tr>')
    I.append('</tbody></table></div></body></html>')
    open(os.path.join(OUT, 'index.html'), 'w').write('\n'.join(I))
    res = {'pages': len(rows), 'chains': sum(r['chains'] for r in rows),
           'by_depth': dict(T), 'rows': rows,
           'max_kb': max((r['kb'] for r in rows), default=0)}
    json.dump(res, open(R('results/v2p10/pages_report.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'rows'}, indent=1))
    return res


if __name__ == '__main__': build()
