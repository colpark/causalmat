"""pages.py: one self-contained HTML page per paper for v2.5, plus an index.

  python3 trace_kit_v2p5/pages.py

Renders only what the files store. No model call, no redrafting, no paraphrase of a key, question,
verdict or caption. Tables truncate; key cards never do.

**The graph is the one each paper's stitch.json names** -- graphs_v07 for 30 papers and graphs_v06b
for 2. Not graphs_v05/first100, which holds only 14 of the 32 and, where it holds one, a different
node set (53 nodes against 40 for jma.2020.11.023, 31 shared). Every node id a v2.5 item cites has
to resolve, so the page draws the graph the items were actually built on, and names it.

CSS, the thumbnailer and the layered graph SVG are imported from trace_kit_v5/paper_report.py, which
built the v5 page this is modelled on.

v5 built traces on MatMech hops. v2.5 builds them on our own graph: every item is exactly TWO steps,
two observations the graph already links, asked so neither answers alone. Composition stitches items
end to end where one item's conclusion claim is another's input. A chain is drawn as items joined,
never as one long trace.

Every verdict is model against model.
"""
import base64, html, io, json, os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v5'))
from paper_report import CSS, thumb, graph_svg, STAGE
E = html.escape
R = lambda *p: os.path.join(ROOT, *p)
PLACEHOLDERS = []

EXTRA = """
.gen{margin:26px 0 8px;font:600 12px ui-monospace,Menlo,monospace;letter-spacing:.06em;
text-transform:uppercase;color:var(--mut)}
.card{border:1px solid var(--line);border-radius:12px;padding:14px 15px;margin:10px 0;background:var(--card)}
.steps{display:flex;gap:12px;flex-wrap:wrap;margin:8px 0}
.stepbox{flex:1 1 300px;border:1px solid var(--line);border-radius:9px;padding:9px 11px;background:var(--bg)}
.stepbox h5{margin:0 0 4px;font:600 10.5px ui-monospace,Menlo,monospace;color:var(--mut);letter-spacing:.06em}
.q{background:var(--chip);border-left:3px solid var(--acc);padding:9px 12px;border-radius:0 8px 8px 0;margin:9px 0}
.q b{display:block;font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.lab{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}
.lab span{font-size:11.5px;background:var(--chip);border-radius:6px;padding:3px 9px;color:var(--mut)}
.lab b{color:var(--ink)}
.flag{font:600 10.5px ui-monospace,Menlo,monospace;padding:2px 8px;border-radius:5px;margin-left:6px;
background:var(--warn);color:#fff}
.flag.ok{background:var(--chip);color:var(--mut)}
.v{font:600 10.5px ui-monospace,Menlo,monospace;padding:1px 6px;border-radius:4px;margin-right:5px}
.v.holds,.v.same_kind,.v.carried,.v.sound{background:var(--chip);color:var(--acc)}
.v.overreaches,.v.mixed,.v.dropped,.v.launders{background:var(--warn);color:#fff}
.v.wrong{background:var(--bad);color:#fff}
.v.na{background:transparent;border:1px solid var(--line);color:var(--mut)}
.chain{border:1px solid var(--acc);border-radius:11px;padding:11px 13px;margin:11px 0;background:var(--card)}
.chainflow{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:7px 0}
.cbox{border:1px solid var(--line);border-radius:8px;padding:5px 9px;background:var(--bg);
font:600 11px ui-monospace,Menlo,monospace}
.cbox.bb{border-color:var(--acc);background:var(--acc);color:#fff}
.cjoin{font:10.5px ui-monospace,Menlo,monospace;color:var(--mut);text-align:center}
.nochain{border:1px dashed var(--warn);border-radius:10px;padding:11px 13px;margin:10px 0;font-size:13px}
.idx td,.idx th{font-size:12px;padding:5px 7px}
.idx tr:hover{background:var(--chip)}
"""


def obj(t, want):
    out, d, s = [], 0, None
    for i, c in enumerate(t or ''):
        if c == '{':
            if d == 0: s = i
            d += 1
        elif c == '}' and d:
            d -= 1
            if not d: out.append(t[s:i + 1])
    for o in sorted(out, key=len, reverse=True):
        for cand in (o, re.sub(r',(\s*[}\]])', r'\1', o)):
            try:
                j = json.loads(cand)
                if want in j: return j
            except Exception: continue
    return None


def vn(v):
    v = (v or '').strip().lower()
    for k in ('overreach', 'wrong', 'holds'):
        if k in v: return {'overreach': 'overreaches'}.get(k, k)
    return v or 'unruled'


def panel_img(p, paper_figs):
    """crop, else the whole figure, else a named placeholder. Every fallback is counted."""
    c = p.get('crop')
    if c and os.path.exists(c):
        s = thumb(c, 700)
        if s: return f'<figure class="pan"><img src="{s}" alt="{E(p["suffix"])}">' \
                     f'<figcaption class="cap">{E(p["suffix"])}</figcaption></figure>'
    fig = paper_figs.get((p.get('figure') or '').strip())
    if fig and os.path.exists(fig):
        s = thumb(fig, 700)
        if s:
            PLACEHOLDERS.append((p['panel_id'], 'whole figure'))
            return f'<figure class="pan"><img src="{s}" alt="{E(p["suffix"])}">' \
                   f'<figcaption class="cap">{E(p["suffix"])} &mdash; whole figure, no crop</figcaption></figure>'
    PLACEHOLDERS.append((p['panel_id'], 'placeholder'))
    return f'<figure class="pan"><div style="padding:22px 14px;color:var(--mut);font:11px ui-monospace,Menlo,monospace">' \
           f'no image for {E(p["panel_id"])}</div><figcaption class="cap">{E(p["suffix"])}</figcaption></figure>'


def load():
    D = json.load(open(R('results/v2p5/items.json')))['items']
    C = json.load(open(R('results/v2p5/composed.json')))
    PAIRS = json.load(open(R('results/v2p5/pairs.json')))['pairs']
    inval = set(json.load(open(R('results/v2p5/audit_invalidated.json'))))
    V5 = {i['item']: i for i in json.load(open(R('results/v5/items.json')))['items']}
    S5 = set(r['item'] for r in json.load(open(R('results/v5/survival_v5b.json')))['surviving'])
    audit, qk = {}, {}
    for f in sorted(os.listdir(R('results/v2p5/check'))):
        if f.endswith('.out.txt'):
            audit[f[:-len('.out.txt')]] = obj(open(R('results/v2p5/check', f)).read(), 'proposition')
    for f in sorted(os.listdir(R('results/v2p5/qkind'))):
        if f.endswith('.out.txt'):
            qk[f[:-len('.out.txt')]] = obj(open(R('results/v2p5/qkind', f)).read(), 'ruling')
    joins = {}
    known = {f"{j['from']}__{j['to']}": (j['from'], j['to']) for j in C['joins']}
    for f in sorted(os.listdir(R('results/v2p5/joinaudit'))):
        if not f.endswith('.out.txt'): continue
        pair = known.get(f[:-len('.out.txt')])
        if not pair: continue
        joins[pair] = obj(open(R('results/v2p5/joinaudit', f)).read(), 'join_verdict') or \
                      obj(open(R('results/v2p5/joinaudit', f)).read(), 'limits_survive')
    return D, C, PAIRS, inval, V5, S5, audit, qk, joins


def figs_for(paper):
    """whole-figure images, for panels whose crop is missing"""
    out = {}
    for d in glob.glob(R('results/figures', paper, '*')) + glob.glob(R('data/figures', paper, '*')):
        out[os.path.splitext(os.path.basename(d))[0]] = d
    return out


def item_card(it, audit, qk, inval, P):
    k = it.get('key') or {}
    L = k.get('labels') or {}
    A = [f'<div class="card"><div class="sh"><span class="sn">{E(it["item"])}</span>']
    flags = []
    if it['item'] in inval: flags.append(('flag', 'audit packet invalidated'))
    if it.get('key_quarantined'): flags.append(('flag', 'key refiled after the wrong-item mixup'))
    if it.get('key_provenance'): flags.append(('flag', 'dispatched directly, not via a relay'))
    if it.get('redrafted_late'): flags.append(('flag', 'redrafted late'))
    for c, t in flags: A.append(f'<span class="{c}">{E(t)}</span>')
    A.append('</div>')
    A.append('<div class="steps">')
    for n, side in ((1, 'observation_a'), (2, 'observation_b')):
        o = it[side]
        A.append(f'<div class="stepbox"><h5>step {n} &middot; {E(str(o.get("technique")))}</h5>'
                 f'{E(str(o.get("text")))}</div>')
    A.append('</div>')
    pans = [p for p in it['panels']]
    if pans:
        A.append('<div class="pans">' + ''.join(panel_img(p, P) for p in pans) + '</div>')
    if it.get('panels_dropped_by_cap'):
        A.append(f'<p class="sub">dropped by the five-panel cap: '
                 f'{E(", ".join(it["panels_dropped_by_cap"]))}</p>')
    A.append(f'<div class="q"><b>the question, as the solver sees it</b>{E(it["question"])}</div>')
    A.append(f'<div class="lab"><span>generator <b>{E(it["generator"])}</b></span>'
             f'<span>depth <b>{it.get("depth")}</b></span>'
             f'<span>lane <b>{"FM" if it.get("fm_lane") else "other"}</b></span>'
             f'<span>dependency <b>{E(str(L.get("dependency")))}</b></span>'
             f'<span>inference <b>{E(str(L.get("inference_validity")))}</b></span>'
             f'<span>causal strength <b>{E(str(L.get("causal_strength")))}</b></span></div>')
    A.append(f'<div class="key"><h5>key &mdash; the combining proposition</h5>'
             f'{E(str(k.get("proposition")))}</div>')
    if k.get('limits'):
        A.append('<div class="lim"><h5>limits</h5><ul>')
        for l in k['limits']: A.append(f'<li>{E(str(l))}</li>')
        A.append('</ul></div>')
    if k.get('not_identifiable'):
        A.append(f'<div class="ni"><b>not identifiable</b>{E(str(k["not_identifiable"]))}</div>')
    r = audit.get(it['item'])
    A.append('<h3>key audit</h3>')
    if not r:
        A.append('<p class="sub">not in the audited sample.</p>')
    else:
        A.append('<table><thead><tr><th>statement</th><th>verdict</th><th>evidence quoted</th>'
                 '</tr></thead><tbody>')
        pv = vn((r.get('proposition') or {}).get('verdict'))
        A.append(f'<tr><td>proposition</td><td><span class="v {E(pv)}">{E(pv)}</span></td>'
                 f'<td>{E(str((r.get("proposition") or {}).get("evidence") or "&mdash;"))}</td></tr>')
        for x in (r.get('limits') or []):
            lv = vn(x.get('verdict'))
            A.append(f'<tr><td>limit[{E(str(x.get("index")))}]</td>'
                     f'<td><span class="v {E(lv)}">{E(lv)}</span></td>'
                     f'<td>{E(str(x.get("evidence") or "&mdash;"))}</td></tr>')
        A.append('</tbody></table>')
    q = qk.get(it['item'])
    if q:
        rule = 'mixed' if str(q.get('ruling', '')).lower().startswith('mix') else 'same_kind'
        A.append(f'<p><b>quantity kind:</b> <span class="v {rule}">{rule}</span> '
                 f'{E(str(q.get("quantity_a")))} <i>({E(str(q.get("kind_a")))})</i> against '
                 f'{E(str(q.get("quantity_b")))} <i>({E(str(q.get("kind_b")))})</i>'
                 + (' &mdash; recorded, not applied to the key' if rule == 'mixed' else '') + '</p>')
    A.append('<div class="audit-only"><b>Audit only &mdash; never shown to a solver.</b>'
             '<p class="sub">what the paper concluded, which the key was written from:</p><ul>')
    for c in (it.get('hidden_key_claims') or []): A.append(f'<li>{E(str(c))}</li>')
    A.append(f'</ul><p class="sub">claims {E(", ".join(it["claims"]))}'
             + (f' &middot; MatMech hop {E(str(it["matmech_hop"]))}' if it.get('matmech_hop') else '')
             + (f' &middot; graph relation {E(str(it["rel"]))}' if it.get('rel') else '')
             + '</p></div></div>')
    return '\n'.join(A)


NO_CHAIN_NOTE = ("This paper's pairs share no claim in the direction a join needs, so no chain was "
                 "built. The pairs themselves are above; what is missing is a claim that is one "
                 "item's conclusion and another's input.")


def stitch_section(paper, D, C, joins, V5, S5, g):
    byitem = {i['item']: i for i in D}
    for k, v in V5.items():
        if k in S5: byitem.setdefault(k, {**v, '_bb': True})
    A = ['<h2><span class="n">5</span>How the items stitch</h2>']
    chains = [c for c in C['chains'] if c['paper'] == paper]
    jns = [j for j in C['joins'] if j['paper'] == paper]
    rej = [r for r in C['rejected'] if r['paper'] == paper]
    att = [a for a in C['attachments'] if a['paper'] == paper]
    if not chains:
        A.append(f'<div class="nochain"><b>No chain for this paper.</b> {NO_CHAIN_NOTE}</div>')
    for c in chains:
        js = list(zip(c['path'], c['path'][1:]))
        verdicts = [joins.get(j) for j in js]
        unaud = any(v is None for v in verdicts)
        laund = [bool(v) and 'launder' in (v.get('join_verdict') or '').lower() for v in verdicts]
        A.append('<div class="chain">')
        A.append(f'<b>chain, depth {c["depth"]}</b> &middot; '
                 + ('<span class="v na">not audited</span> one join reply did not parse, so this '
                    'chain has no limit verdict and none is invented for it'
                    if unaud else
                    ('<span class="v carried">every limit survives</span>' if not any(laund)
                     else '<span class="v dropped">a limit is dropped along this chain</span>')))
        A.append('<div class="chainflow">')
        for i, node in enumerate(c['path']):
            bb = ' bb' if byitem.get(node, {}).get('_bb') else ''
            A.append(f'<span class="cbox{bb}">{E(node)}{" &middot; backbone" if bb else ""}</span>')
            if i < len(js):
                A.append(f'<span class="cjoin">&rarr;<br>on {E(js[i] and jns and "" or "")}'
                         f'{E(next((j["on_claim"] for j in jns if (j["from"], j["to"]) == js[i]), "?"))}</span>')
        A.append('</div>')
        A.append(graph_svg(g, {cc for n in c['path'] for cc in (byitem.get(n, {}).get('claims') or [])}))
        A.append('</div>')
    if jns:
        A.append('<h3>joins</h3><table><thead><tr><th>join</th><th>on claim</th>'
                 '<th>proposition</th><th>upstream limits</th><th>verdict</th></tr></thead><tbody>')
        for j in jns:
            r = joins.get((j['from'], j['to']))
            if not r:
                A.append(f'<tr><td>{E(j["from"])} &rarr; {E(j["to"])}</td><td>{E(j["on_claim"])}</td>'
                         f'<td colspan="3"><span class="v na">not audited</span> the reply did not '
                         f'parse</td></tr>')
                continue
            pv = vn((r.get('proposition') or {}).get('verdict'))
            ls = collections.Counter()
            for x in (r.get('limits_survive') or []):
                v = (x.get('verdict') or '').lower()
                ls['dropped' if 'drop' in v else 'carried' if 'carr' in v else 'n/a'] += 1
            lau = 'launder' in (r.get('join_verdict') or '').lower()
            A.append(f'<tr><td>{E(j["from"])} &rarr; {E(j["to"])}</td><td>{E(j["on_claim"])}</td>'
                     f'<td><span class="v {E(pv)}">{E(pv)}</span></td>'
                     f'<td><span class="v carried">{ls["carried"]} carried</span>'
                     f'<span class="v dropped">{ls["dropped"]} dropped</span>'
                     f'<span class="v na">{ls["n/a"]} n/a</span></td>'
                     f'<td>{"<span class=\'v launders\'>launders a limit</span>" if lau else "<span class=\'v sound\'>sound</span>"}</td></tr>')
        A.append('</tbody></table>')
    if rej:
        A.append('<h3>joins rejected</h3><table><thead><tr><th>join</th><th>why</th></tr></thead><tbody>')
        for r in rej:
            A.append(f'<tr><td>{E(r["from"])} &rarr; {E(r["to"])}</td><td>{E(r["why"])}</td></tr>')
        A.append('</tbody></table>')
    if att:
        A.append('<h3>pairs attached to a backbone claim</h3><table><thead><tr><th>item</th>'
                 '<th>generator</th><th>attaches at</th><th>where</th></tr></thead><tbody>')
        for a in att:
            A.append(f'<tr><td>{E(a["item"])}</td><td>{E(a["generator"])}</td>'
                     f'<td>{E(", ".join(a["attachment_claim"]))}</td><td>{E(a["where"])}</td></tr>')
        A.append('</tbody></table>')
    return '\n'.join(A)


def convergence_section(paper, C, byitem):
    conv = [c for c in C['convergence'] if c['paper'] == paper]
    if not conv: return ''
    A = ['<h2><span class="n">6</span>Convergence</h2>']
    A.append('<p class="lead">A claim this paper reaches by two routes whose <b>figures</b> are '
             'disjoint. Independence was tested on node ids first, then panels, then figures; only '
             'the figure test is used here.</p>')
    for c in conv:
        A.append(f'<div class="chain"><b>claim {E(c["claim"])}</b> &middot; '
                 f'{len(c["routes"])} routes &middot; independence: {E(c.get("independence","?"))}'
                 '<ul>')
        for r in c['routes']:
            it = byitem.get(r, {})
            pans = ', '.join(p['suffix'] for p in (it.get('panels') or []))
            A.append(f'<li><b>{E(r)}</b> &mdash; panels {E(pans)}</li>')
        A.append('</ul></div>')
    A.append('<div class="nochain"><b>Nobody judged these claims.</b> The independence test was '
             'tightened to figures after the judged runs, and no further model call was made. The '
             'two runs that were judged &mdash; 23 claims at node-id independence and 6 at panel '
             'independence &mdash; cover <b>overlapping routes only</b>. Genuine convergence in this '
             'corpus is 3 claims, unmeasured.</div>')
    return '\n'.join(A)


GEN_NOTE = {
 'complementary': 'two technique families evidencing one claim, so each carries part of the support '
                  'and neither carries all of it',
 'spine_edge': 'two figure-backed claims joined by a `causes` or `explains` edge in our graph',
 'covariation': 'two observations carrying series of the same length over the same samples, in '
                'different quantities',
}


def pairs_section(paper, D, PAIRS):
    live = {i['item'] for i in D if i['paper'] == paper}
    A = ['<h2><span class="n">3</span>How the pairs formed</h2>']
    byg = collections.defaultdict(list)
    for i in D:
        if i['paper'] == paper: byg[i['generator']].append(i)
    if not byg:
        A.append('<p class="sub">No pairs for this paper.</p>'); return '\n'.join(A)
    for g in ('complementary', 'spine_edge', 'covariation'):
        its = byg.get(g)
        if not its: continue
        A.append(f'<h3>{g} &mdash; {GEN_NOTE[g]}</h3>')
        A.append('<table><thead><tr><th>item</th><th>A</th><th>B</th><th>how the graph links them</th>'
                 + ('<th>series</th>' if g == 'covariation' else '') + '</tr></thead><tbody>')
        for it in sorted(its, key=lambda x: x['item']):
            extra = ''
            if g == 'covariation':
                extra = (f'<td>{it.get("series_len") or "?"} values each &mdash; '
                         f'<b>equal-length proxy</b></td>')
            A.append(f'<tr><td>{E(it["item"])}</td>'
                     f'<td>{E(it["observation_a"]["node"])} {E(str(it["observation_a"]["technique"]))}</td>'
                     f'<td>{E(it["observation_b"]["node"])} {E(str(it["observation_b"]["technique"]))}</td>'
                     f'<td>{E(str(it["basis"])[:150])}</td>{extra}</tr>')
        A.append('</tbody></table>')
        if g == 'covariation':
            A.append('<div class="nochain">The covariation generator has no <code>panel_conditions</code> '
                     'field to read. A sample series is detected from the observation text &mdash; three '
                     'or more numbers in one sweep &mdash; and two series pair when they are the '
                     '<b>same length</b>. Length is not comparability, which is why 37% of sampled '
                     'covariation propositions set quantities of different kinds against each other.</div>')
    n_drop = sum(1 for p in PAIRS if p['paper'] == paper) - len(live)
    if n_drop > 0:
        A.append(f'<p class="sub">{n_drop} pair(s) found at the pair stage did not become items: '
                 f'a spine edge whose two claims share one evidence node is not a pair, and ten such '
                 f'self-pairs were dropped across the corpus.</p>')
    return '\n'.join(A)


def summary(paper, D, C, joins):
    its = [i for i in D if i['paper'] == paper]
    g = collections.Counter(i['generator'] for i in its)
    disc = sum(1 for i in its if ((i.get('key') or {}).get('labels') or {}).get('causal_strength')
               == 'discriminating')
    fm = sum(1 for i in its if i.get('fm_lane'))
    ch = [c for c in C['chains'] if c['paper'] == paper]
    jn = [j for j in C['joins'] if j['paper'] == paper]
    rj = [r for r in C['rejected'] if r['paper'] == paper]
    lau = sum(1 for j in jn if (joins.get((j['from'], j['to'])) or {}) and
              'launder' in ((joins.get((j['from'], j['to'])) or {}).get('join_verdict') or '').lower())
    return {'items': len(its), 'comp': g['complementary'], 'edge': g['spine_edge'],
            'cov': g['covariation'], 'disc': disc, 'fm': fm, 'chains': len(ch),
            'max_depth': max([c['depth'] for c in ch], default=0), 'joins': len(jn),
            'rejected': len(rj), 'launder': lau,
            'conv': sum(1 for c in C['convergence'] if c['paper'] == paper)}


def build(paper, D, C, PAIRS, inval, V5, S5, audit, qk, joins):
    gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
    g = json.load(open(R(gp)))
    its = [i for i in D if i['paper'] == paper]
    byitem = {i['item']: i for i in D}
    used = {c for i in its for c in i['claims']} | \
           {i[s]['node'] for i in its for s in ('observation_a', 'observation_b')}
    P = figs_for(paper)
    s = summary(paper, D, C, joins)
    short = paper.split('__')[0].replace('_', ' ')
    A = ['<!doctype html><html lang="en"><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{E(short)} — v2.5</title><style>{CSS}{EXTRA}</style><body><div class="wrap">',
         f'<h1>{E(short)}</h1><p class="sub">{E(paper)}</p>',
         '<p class="mvm">Every verdict is model against model.</p>',
         f'<p class="lead"><b>{s["items"]} two-step items</b> &mdash; {s["comp"]} complementary, '
         f'{s["edge"]} spine edge, {s["cov"]} covariation &middot; {s["disc"]} discriminating '
         f'&middot; {s["fm"]} FM lane &middot; {s["chains"]} chains'
         + (f', deepest {s["max_depth"]}' if s['chains'] else '')
         + f' &middot; {s["joins"]} joins kept, {s["rejected"]} rejected, '
         f'{s["launder"]} dropping a limit'
         + (f' &middot; {s["conv"]} convergence claim(s)' if s['conv'] else '') + '</p>',
         '<h2><span class="n">2</span>The original graph</h2>',
         f'<p class="lead">Drawn from <code>{E(gp)}</code>, the graph these items were built on. '
         f'Every node any v2.5 item uses is highlighted.</p>',
         graph_svg(g, used)]
    A.append(pairs_section(paper, D, PAIRS))
    A.append('<h2><span class="n">4</span>The two-step items</h2>')
    A.append('<p class="lead">Every item is exactly two steps: two observations the graph already '
             'links, asked so neither answers alone. Chains are these items joined end to end, in '
             'section 5 &mdash; never one long trace.</p>')
    byg = collections.defaultdict(list)
    for i in its: byg[i['generator']].append(i)
    for gname in ('complementary', 'spine_edge', 'covariation'):
        if not byg.get(gname): continue
        A.append(f'<div class="gen">{E(gname)} &mdash; {len(byg[gname])} items</div>')
        for it in sorted(byg[gname], key=lambda x: x['item']):
            A.append(item_card(it, audit, qk, inval, P))
    A.append(stitch_section(paper, D, C, joins, V5, S5, g))
    A.append(convergence_section(paper, C, {**byitem, **V5}))
    A.append('</div></body></html>')
    return '\n'.join(A), s


def main():
    D, C, PAIRS, inval, V5, S5, audit, qk, joins = load()
    papers = [x['paper'] for x in json.load(open(R('results/v5_papers.json')))]
    out = R('results/v2p5/pages'); os.makedirs(out, exist_ok=True)
    rows = []
    for p in papers:
        html_, s = build(p, D, C, PAIRS, inval, V5, S5, audit, qk, joins)
        f = os.path.join(out, p + '.html')
        open(f, 'w').write(html_)
        s['paper'] = p; s['kb'] = os.path.getsize(f) // 1024
        rows.append(s)
        print(f"  {p[:52]:52s} {s['items']:3d} items  {s['kb']:6d} KB")
    T = {k: sum(r[k] for r in rows) for k in ('items', 'comp', 'edge', 'cov', 'disc', 'fm',
                                              'chains', 'joins', 'rejected', 'launder', 'conv')}
    A = ['<!doctype html><html lang="en"><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>v2.5 — 32 papers</title><style>{CSS}{EXTRA}</style><body><div class="wrap">',
         '<h1>Traces v2.5 — pairwise items from the graph</h1>',
         '<p class="mvm">Every verdict is model against model.</p>',
         '<p class="lead">One page per paper. Every item is two steps; chains are items joined end '
         'to end. Numbers agree with docs/TRACES_V2P5.md and trace_kit_v2p5/doc_numbers.py.</p>',
         '<table class="idx"><thead><tr><th>paper</th><th>items</th><th>comp</th><th>edge</th>'
         '<th>cov</th><th>disc</th><th>FM</th><th>chains</th><th>depth</th><th>joins</th>'
         '<th>rej</th><th>launder</th><th>conv</th><th>size</th></tr></thead><tbody>']
    for r in rows:
        A.append(f'<tr><td><a href="{E(r["paper"])}.html">{E(r["paper"].split("__")[0].replace("_"," ")[:38])}</a></td>'
                 f'<td>{r["items"]}</td><td>{r["comp"]}</td><td>{r["edge"]}</td><td>{r["cov"]}</td>'
                 f'<td>{r["disc"]}</td><td>{r["fm"]}</td><td>{r["chains"]}</td>'
                 f'<td>{r["max_depth"] or "&mdash;"}</td><td>{r["joins"]}</td><td>{r["rejected"]}</td>'
                 f'<td>{r["launder"]}</td><td>{r["conv"]}</td><td>{r["kb"]} KB</td></tr>')
    A.append(f'<tr><td><b>total</b></td><td><b>{T["items"]}</b></td><td><b>{T["comp"]}</b></td>'
             f'<td><b>{T["edge"]}</b></td><td><b>{T["cov"]}</b></td><td><b>{T["disc"]}</b></td>'
             f'<td><b>{T["fm"]}</b></td><td><b>{T["chains"]}</b></td><td>&mdash;</td>'
             f'<td><b>{T["joins"]}</b></td><td><b>{T["rejected"]}</b></td>'
             f'<td><b>{T["launder"]}</b></td><td><b>{T["conv"]}</b></td><td></td></tr>')
    A.append('</tbody></table></div></body></html>')
    open(os.path.join(out, 'index.html'), 'w').write('\n'.join(A))
    ph = collections.Counter(k for _, k in PLACEHOLDERS)
    print(f"\n{len(rows)} pages + index. totals: {T}")
    print(f"image fallbacks: {dict(ph)} over {len(PLACEHOLDERS)} panels")
    json.dump({'totals': T, 'rows': rows, 'fallbacks': dict(ph),
               'fallback_panels': PLACEHOLDERS},
              open(R('results/v2p5/pages_report.json'), 'w'), indent=1)


if __name__ == '__main__': main()
