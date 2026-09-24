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


GEN_COLOUR = {'complementary': 'var(--acc)', 'spine_edge': 'var(--hide)',
              'covariation': 'var(--warn)'}
NO_MERGE = ("This paper's two-step items share no claim in the direction a join needs — no item's "
            "conclusion is another's input — so nothing merged. Every item is in section 6.")


def concludes(it):
    """the claim an item lands on; for a spine edge that is the downstream end"""
    if it.get('_bb'): return (it.get('claims') or [None])[0]
    return it['claims'][1] if it['generator'] == 'spine_edge' and len(it['claims']) > 1 \
        else it['claims'][0]


def jkey(r):
    """(proposition verdict, carried/dropped/na counts, launders) from a join audit reply"""
    if not r: return None
    pv = vn((r.get('proposition') or {}).get('verdict'))
    ls, rows = collections.Counter(), []
    for x in (r.get('limits_survive') or []):
        v = (x.get('verdict') or '').lower()
        c = 'dropped' if 'drop' in v else 'carried' if 'carr' in v else 'na'
        ls[c] += 1; rows.append((c, x.get('limit'), x.get('why')))
    return {'pv': pv, 'counts': ls, 'rows': rows,
            'launders': 'launder' in (r.get('join_verdict') or '').lower(),
            'evidence': (r.get('proposition') or {}).get('evidence')}


def merge_map(paper, chains, jns, joins, byitem, rej, att, N):
    """items as boxes, join claims as nodes between them, edges coloured by the join audit"""
    if not chains: return ''
    nodes, order = {}, []
    for c in chains:
        for n in c['path']:
            if n not in nodes: nodes[n] = {'kind': 'item'}; order.append(n)
    jn_by = {(j['from'], j['to']): j for j in jns}
    # x by longest path
    nxt = collections.defaultdict(list)
    for (a, b) in jn_by: nxt[a].append(b)
    depth = {}
    def dep(n, seen=()):
        if n in depth: return depth[n]
        if n in seen: return 0
        d = 0
        for m in nxt.get(n, []): d = max(d, dep(m, seen + (n,)) + 1)
        depth[n] = d; return d
    for n in order: dep(n)
    maxd = max(depth.values(), default=0)
    col = collections.defaultdict(list)
    for n in order: col[maxd - depth[n]].append(n)
    BW, BH, GX, GY = 150, 30, 250, 62
    pos = {}
    for x, ns in col.items():
        for y, n in enumerate(ns): pos[n] = (40 + x * GX, 46 + y * GY)
    W = 40 + (maxd + 1) * GX + 60
    H = 46 + max((len(v) for v in col.values()), default=1) * GY + 40
    A = [f'<svg viewBox="0 0 {W} {H}" class="gsvg" role="img" aria-label="merge map">']
    for (a, b), j in jn_by.items():
        if a not in pos or b not in pos: continue
        k = jkey(joins.get((a, b)))
        cls = 'me na' if k is None else ('me bad' if k['launders'] else 'me good')
        (x1, y1), (x2, y2) = pos[a], pos[b]
        mx, my = (x1 + BW + x2) / 2, (y1 + y2) / 2
        A.append(f'<line x1="{x1+BW}" y1="{y1}" x2="{mx-28}" y2="{my}" class="{cls}"/>')
        A.append(f'<line x1="{mx+28}" y1="{my}" x2="{x2-3}" y2="{y2}" class="{cls}"/>')
        lbl = (N.get(j['on_claim'], {}).get('label') or '')[:26]
        A.append(f'<g class="jn"><title>{E(j["on_claim"])}: '
                 f'{E((N.get(j["on_claim"],{}).get("label") or "")[:180])}</title>'
                 f'<rect x="{mx-28}" y="{my-11}" width="56" height="22" rx="11"/>'
                 f'<text x="{mx}" y="{my+4}">{E(j["on_claim"])}</text></g>')
        A.append(f'<text x="{mx}" y="{my+24}" class="jlbl">{E(lbl)}</text>')
    for n, (x, y) in pos.items():
        it = byitem.get(n, {})
        bb = it.get('_bb')
        fill = GEN_COLOUR.get(it.get('generator'), 'var(--acc)')
        A.append(f'<g class="mb{" bb" if bb else ""}"><title>{E(n)}</title>'
                 f'<rect x="{x}" y="{y-BH//2}" width="{BW}" height="{BH}" rx="7" '
                 f'style="stroke:{fill}"/>'
                 f'<text x="{x+BW/2}" y="{y+4}">{E(n[-26:])}</text></g>')
        if bb: A.append(f'<text x="{x+BW/2}" y="{y+BH//2+12}" class="jlbl">backbone</text>')
    A.append('</svg>')
    leg = ('<p class="sub"><span class="v carried">carried</span> every upstream limit survives the '
           'join &middot; <span class="v dropped">launders</span> a limit does not reach the next '
           'step &middot; <span class="v na">not audited</span></p>')
    return '\n'.join(A) + leg


def seam(j, r, N, upstream_item):
    """the merge seam: a full-width band, visibly not a step block"""
    cid = j['on_claim']
    ctext = (N.get(cid, {}).get('label') or '')
    A = [f'<div class="seam"><div class="seamhead">merge seam &mdash; joins on '
         f'<code>{E(cid)}</code> {E(ctext[:150])}</div>']
    k = jkey(r)
    if not k:
        A.append('<p class="sub"><span class="v na">not audited</span> the join audit reply for this '
                 'seam did not parse, so no verdict is shown and none is invented.</p></div>')
        return '\n'.join(A), []
    A.append(f'<p><b>joined proposition:</b> <span class="v {E(k["pv"])}">{E(k["pv"])}</span>'
             + (f' &mdash; {E(str(k["evidence"])[:400])}' if k.get('evidence') else '') + '</p>')
    A.append('<div class="lims"><b>what happens to the upstream item&rsquo;s limits</b><ul>')
    dropped = []
    for c, lim, why in k['rows']:
        badge = {'carried': 'carried', 'dropped': 'dropped', 'na': 'not applicable'}[c]
        cls = 'lrow drop' if c == 'dropped' else 'lrow'
        A.append(f'<li class="{cls}"><span class="v {"dropped" if c=="dropped" else "carried" if c=="carried" else "na"}">'
                 f'{badge}</span>{E(str(lim))}'
                 + ('<div class="dropnote">this limit does not reach the next step</div>'
                    if c == 'dropped' else '')
                 + (f'<div class="sub">{E(str(why)[:300])}</div>' if why else '') + '</li>')
        if c == 'dropped': dropped.append((lim, cid))
    A.append('</ul></div>')
    if k['launders']:
        A.append('<p class="launderbar">this seam <b>launders a limit</b>: the upstream conclusion '
                 'was true only within it, and the next step uses the conclusion as if it were not.</p>')
    A.append('</div>')
    return '\n'.join(A), dropped


def trace_card(c, idx, jns, joins, byitem, N, audit, qk, inval, P, shown, seen_seams):
    js = list(zip(c['path'], c['path'][1:]))
    jn_by = {(j['from'], j['to']): j for j in jns}
    ks = [jkey(joins.get(j)) for j in js]
    unaud = any(k is None for k in ks)
    laund = sum(1 for k in ks if k and k['launders'])
    tid = f"trace-{idx}"
    A = [f'<div class="trace" id="{tid}">']
    A.append(f'<div class="thead"><b>{E(tid)}</b> &middot; depth {c["depth"]} &middot; '
             f'{len(c["path"])} items, {len(js)} seams &middot; '
             f'{laund} seam(s) launder a limit &middot; '
             + ('<span class="v na">not audited</span>' if unaud else
                ('<span class="v carried">every limit survives</span>' if not laund
                 else '<span class="v dropped">a limit is lost along this trace</span>'))
             + '</div>')
    lost = []
    for i, n in enumerate(c['path']):
        it = byitem.get(n)
        if it is None: continue
        if n in shown:
            k = (it.get('key') or {})
            A.append(f'<div class="ref">already shown in full above &mdash; <b>{E(n)}</b>, '
                     f'{E(it.get("generator","backbone"))}: {E(str(k.get("proposition"))[:220])}</div>')
        else:
            A.append(item_card(it, audit, qk, inval, P) if not it.get('_bb')
                     else f'<div class="card"><div class="sh"><span class="sn">{E(n)}</span>'
                          f'<span class="flag ok">v5 backbone item</span></div>'
                          f'<p>{E(str((it.get("key") or {}).get("proposition"))[:600])}</p></div>')
            shown.add(n)
        if i < len(js):
            j = jn_by.get(js[i])
            if j:
                h, dr = seam(j, joins.get(js[i]), N, n)
                lost += dr
                if js[i] in seen_seams:
                    # 42 joins are shared by more than one trace, one of them by eight. The seam is
                    # written out once, where it first occurs, and referenced after -- the same rule
                    # the brief sets for a repeated item, so a trace stays readable without the page
                    # printing one seam eight times.
                    k = jkey(joins.get(js[i]))
                    tag = ('not audited' if not k else
                           ('launders a limit' if k['launders'] else 'every limit carried'))
                    A.append(f'<div class="ref">merge seam on <code>{E(j["on_claim"])}</code> '
                             f'&mdash; shown in full in {E(seen_seams[js[i]])}: {E(tag)}</div>')
                else:
                    seen_seams[js[i]] = f"trace-{idx}"
                    A.append(h)
    last = byitem.get(c['path'][-1], {})
    fk = last.get('key') or {}
    surviving = [l for l in (fk.get('limits') or [])]
    A.append('<div class="closing"><b>what this trace ends up asserting</b>'
             f'<p>{E(str(fk.get("proposition"))[:700])}</p>')
    if surviving:
        A.append('<p class="sub"><b>limits still attached at the end:</b></p><ul>')
        for l in surviving[:6]: A.append(f'<li>{E(str(l))}</li>')
        A.append('</ul>')
    if lost:
        A.append('<p class="sub"><b>limits lost along the way:</b></p><ul>')
        for l, cid in lost:
            A.append(f'<li><span class="v dropped">dropped</span>{E(str(l))} '
                     f'<span class="sub">&mdash; at the seam on {E(cid)}</span></li>')
        A.append('</ul>')
    elif not unaud:
        A.append('<p class="sub">No limit was dropped at any seam in this trace.</p>')
    A.append('</div></div>')
    return '\n'.join(A)


EXTRA2 = """
.gsvg .me{stroke-width:2.2}
.me.good{stroke:var(--acc)} .me.bad{stroke:var(--warn)} .me.na{stroke:var(--line);stroke-dasharray:4 3}
.jn rect{fill:var(--chip);stroke:var(--line)}
.jn text{font:600 10px ui-monospace,Menlo,monospace;fill:var(--mut);text-anchor:middle}
.jlbl{font:9.5px ui-monospace,Menlo,monospace;fill:var(--mut);text-anchor:middle}
.mb rect{fill:var(--card);stroke-width:2}
.mb text{font:600 10px ui-monospace,Menlo,monospace;fill:var(--ink);text-anchor:middle}
.mb.bb rect{stroke-dasharray:5 3;stroke-width:3}
.trace{border:1px solid var(--acc);border-radius:13px;padding:0;margin:18px 0;overflow:hidden;background:var(--card)}
.thead{background:var(--chip);padding:11px 15px;font-size:13.5px;border-bottom:1px solid var(--line)}
.trace .card{margin:12px 15px;border-radius:10px}
.seam{margin:0;padding:13px 16px;background:linear-gradient(var(--chip),var(--chip));
border-top:2px dashed var(--acc);border-bottom:2px dashed var(--acc)}
.seamhead{font:600 11px ui-monospace,Menlo,monospace;letter-spacing:.05em;text-transform:uppercase;
color:var(--acc);margin-bottom:7px}
.seam .lims{font-size:13px}
.seam .lims b{font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.lrow{margin:6px 0}
.lrow.drop{background:rgba(224,163,58,.13);border-left:3px solid var(--warn);padding:5px 9px;border-radius:0 6px 6px 0}
.dropnote{color:var(--warn);font-weight:600;font-size:12px;margin-top:3px}
.launderbar{background:var(--warn);color:#fff;padding:7px 11px;border-radius:7px;font-size:12.5px;margin:9px 0 0}
.closing{margin:0;padding:13px 16px;border-top:2px solid var(--acc);background:var(--bg)}
.closing b{font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.ref{margin:12px 15px;padding:9px 12px;border:1px dashed var(--line);border-radius:9px;
font-size:12.5px;color:var(--mut)}
.nomerge{border:1px dashed var(--warn);border-radius:10px;padding:12px 14px;margin:10px 0;font-size:13px}
.tt td,.tt th{font-size:12px}
"""


def cut_section(paper, D, chains):
    inmerge = {n for c in chains for n in c['path']}
    A = ['<h2><span class="n">3</span>How the two-step items were cut</h2>',
         '<p class="lead">Each item is two observations the graph already links. Section 5 carries '
         'the content; this is the inventory.</p>']
    byg = collections.defaultdict(list)
    for i in D:
        if i['paper'] == paper: byg[i['generator']].append(i)
    for g in ('complementary', 'spine_edge', 'covariation'):
        its = byg.get(g)
        if not its: continue
        A.append(f'<h3>{g} &mdash; {len(its)} items &mdash; {GEN_NOTE[g]}</h3>')
        A.append('<table class="tt"><thead><tr><th>item</th><th>observation A</th>'
                 '<th>observation B</th><th>concludes</th><th>merges?</th></tr></thead><tbody>')
        for it in sorted(its, key=lambda x: x['item']):
            A.append(f'<tr><td>{E(it["item"])}</td>'
                     f'<td>{E(str(it["observation_a"]["text"])[:70])}</td>'
                     f'<td>{E(str(it["observation_b"]["text"])[:70])}</td>'
                     f'<td>{E(str(concludes(it)))}</td>'
                     f'<td>{"yes" if it["item"] in inmerge else "&mdash;"}</td></tr>')
        A.append('</tbody></table>')
        if g == 'covariation':
            A.append('<p class="sub">Covariation pairs two series of the <b>same length</b> on a '
                     'shared claim. There is no <code>panel_conditions</code> field to read, so the '
                     'series is detected from the observation text and length stands in for a shared '
                     'sweep. That proxy is why 37% of sampled covariation propositions set '
                     'quantities of different kinds against each other.</p>')
    return '\n'.join(A)


GEN_NOTE = {
 'complementary': 'two technique families evidencing one claim',
 'spine_edge': 'two figure-backed claims joined by a causes or explains edge',
 'covariation': 'two series of equal length on a shared claim',
}


def matmech_section(paper, C, V5, S5):
    bb = [b for b in C['backbone'] if V5.get(b, {}).get('paper') == paper]
    if not bb: return ''
    hops = json.load(open(R('results/v3', paper, 'hops.json')))['hops']
    want = {(V5[b].get('provenance_NOT_SOLVER_VISIBLE') or {}).get('matmech_hop') for b in bb}
    hs = [h for h in hops if h['id'] in want]
    if not hs: return ''
    A = ['<h2><span class="n">2</span>MatMech&rsquo;s causality</h2>',
         '<div class="audit-only"><b>Audit only &mdash; never shown to a solver.</b> '
         f'Only the {len(hs)} hop(s) behind this paper&rsquo;s v5 backbone items.']
    for h in hs:
        sp = h['_matmech_span_DO_NOT_PROMPT']
        A.append(f'<div class="hop"><span class="id">{E(h["id"])}</span> <b>{E(str(h.get("stage_type")))}</b>'
                 f'<div class="span"><b>cause:</b> {E(str(sp.get("cause")))}</div>'
                 f'<div class="span"><b>effect:</b> {E(str(sp.get("effect")))}</div>'
                 f'<div class="span">figures {E(", ".join(h.get("figures") or []) or "&mdash;")}</div></div>')
    A.append('</div>')
    return '\n'.join(A)


def build(paper, D, C, PAIRS, inval, V5, S5, audit, qk, joins):
    gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
    g = json.load(open(R(gp))); N = {n['id']: n for n in g['nodes']}
    its = [i for i in D if i['paper'] == paper]
    byitem = {i['item']: i for i in D}
    for b in C['backbone']:
        if b in V5: byitem.setdefault(b, {**V5[b], '_bb': True})
    chains = sorted([c for c in C['chains'] if c['paper'] == paper],
                    key=lambda c: -c['depth'])
    jns = [j for j in C['joins'] if j['paper'] == paper]
    rej = [r for r in C['rejected'] if r['paper'] == paper]
    att = [a for a in C['attachments'] if a['paper'] == paper]
    used = {c for i in its for c in i['claims']} | \
           {i[s]['node'] for i in its for s in ('observation_a', 'observation_b')}
    P = figs_for(paper)
    ks = [jkey(joins.get((j['from'], j['to']))) for j in jns]
    laund = sum(1 for k in ks if k and k['launders'])
    keepall = 0
    for c in chains:
        cks = [jkey(joins.get(j)) for j in zip(c['path'], c['path'][1:])]
        if all(cks) and not any(k['launders'] for k in cks): keepall += 1
    s = {'items': len(its),
         'comp': sum(1 for i in its if i['generator'] == 'complementary'),
         'edge': sum(1 for i in its if i['generator'] == 'spine_edge'),
         'cov': sum(1 for i in its if i['generator'] == 'covariation'),
         'disc': sum(1 for i in its if ((i.get('key') or {}).get('labels') or {}).get('causal_strength') == 'discriminating'),
         'fm': sum(1 for i in its if i.get('fm_lane')),
         'chains': len(chains), 'max_depth': max([c['depth'] for c in chains], default=0),
         'joins': len(jns), 'rejected': len(rej), 'launder': laund, 'keepall': keepall,
         'conv': sum(1 for c in C['convergence'] if c['paper'] == paper)}
    short = paper.split('__')[0].replace('_', ' ')
    A = ['<!doctype html><html lang="en"><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{E(short)} — v2.5</title><style>{CSS}{EXTRA}{EXTRA2}</style><body><div class="wrap">',
         f'<h1>{E(short)}</h1><p class="sub">{E(paper)}</p>',
         '<p class="mvm">Every verdict is model against model.</p>',
         f'<p class="lead"><b>{s["items"]} two-step items</b> &mdash; {s["comp"]} complementary, '
         f'{s["edge"]} spine edge, {s["cov"]} covariation &middot; {s["disc"]} discriminating '
         f'&middot; {s["fm"]} FM lane &middot; <b>{s["chains"]} merged traces</b>'
         + (f', deepest {s["max_depth"]}' if s['chains'] else '')
         + f' &middot; {s["joins"]} seams, {s["launder"]} laundering a limit, '
         f'{s["keepall"]} trace(s) keeping every limit &middot; {s["rejected"]} joins rejected'
         + (f' &middot; {s["conv"]} convergence claim(s)' if s['conv'] else '') + '</p>',
         '<h2><span class="n">1</span>The original graph</h2>',
         f'<p class="lead">Drawn from <code>{E(gp)}</code>, the graph these items were built on.</p>',
         graph_svg(g, used),
         matmech_section(paper, C, V5, S5),
         cut_section(paper, D, chains)]

    A.append('<h2><span class="n">4</span>How the items merge</h2>')
    if not chains:
        A.append(f'<div class="nomerge"><b>Nothing merged.</b> {NO_MERGE}</div>')
    else:
        A.append('<p class="lead">Every box is a two-step item. A round node between two boxes is '
                 'the claim they join on: one item&rsquo;s conclusion is the next item&rsquo;s input. '
                 'Edge colour is the join audit.</p>')
        A.append(merge_map(paper, chains, jns, joins, byitem, rej, att, N))
        A.append('<table class="tt"><thead><tr><th>trace</th><th>depth</th><th>items in order</th>'
                 '<th>join claims</th><th>every limit survives</th></tr></thead><tbody>')
        for i, c in enumerate(chains, 1):
            js = list(zip(c['path'], c['path'][1:]))
            cks = [jkey(joins.get(j)) for j in js]
            jc = [next((j['on_claim'] for j in jns if (j['from'], j['to']) == p_), '?') for p_ in js]
            verdict = ('not audited' if not all(cks) else
                       ('yes' if not any(k['launders'] for k in cks) else 'no'))
            A.append(f'<tr><td><a href="#trace-{i}">trace-{i}</a></td><td>{c["depth"]}</td>'
                     f'<td>{E(" &rarr; ".join(c["path"]))}</td><td>{E(", ".join(jc))}</td>'
                     f'<td>{verdict}</td></tr>')
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
        A.append(f'<div class="nomerge">{NO_MERGE}</div>')
    else:
        A.append('<p class="lead">One card per merged trace, deepest first. A step block is one '
                 'two-step item. Between them, a <b>merge seam</b> shows what happened to the '
                 'upstream item&rsquo;s limits when its conclusion was carried forward.</p>')
        for i, c in enumerate(chains, 1):
            A.append(trace_card(c, i, jns, joins, byitem, N, audit, qk, inval, P, shown,
                                 seen_seams))

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
        for gname in ('complementary', 'spine_edge', 'covariation'):
            grp = byg.get(gname)
            if not grp: continue
            A.append(f'<div class="gen">{E(gname)} &mdash; {len(grp)} items</div>')
            withatt = [i for i in grp if i['item'] in attmap]
            plain = [i for i in grp if i['item'] not in attmap]
            for i in sorted(withatt, key=lambda x: x['item']):
                a = attmap[i['item']]
                A.append(f'<h3>attaches to the trace claim {E(", ".join(a["attachment_claim"]))}</h3>')
                A.append(item_card(i, audit, qk, inval, P))
            for i in sorted(plain, key=lambda x: x['item']):
                A.append(item_card(i, audit, qk, inval, P))
    A.append(convergence_section(paper, C, byitem))
    A.append('</div></body></html>')
    return '\n'.join(A), s


def convergence_section(paper, C, byitem):
    conv = [c for c in C['convergence'] if c['paper'] == paper]
    if not conv: return ''
    A = ['<h2><span class="n">7</span>Convergence</h2>',
         '<p class="lead">A claim this paper reaches by two routes whose <b>figures</b> are '
         'disjoint.</p>']
    for c in conv:
        A.append(f'<div class="chain"><b>claim {E(c["claim"])}</b> &middot; {len(c["routes"])} routes '
                 f'&middot; independence: {E(c.get("independence","?"))}<ul>')
        for r in c['routes']:
            it = byitem.get(r, {})
            A.append(f'<li><b>{E(r)}</b> &mdash; panels '
                     f'{E(", ".join(p["suffix"] for p in (it.get("panels") or [])))}</li>')
        A.append('</ul></div>')
    A.append('<div class="nomerge"><b>Nobody judged these claims.</b> Independence was tightened to '
             'figures after the judged runs and no further model call was made. The two judged runs '
             '&mdash; 23 claims at node-id independence, 6 at panel independence &mdash; cover '
             '<b>overlapping routes only</b>. Genuine convergence here is 3 claims, unmeasured.</div>')
    return '\n'.join(A)


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
    T = {k: sum(r[k] for r in rows) for k in ('items', 'comp', 'edge', 'cov', 'disc', 'fm',
                                              'chains', 'joins', 'rejected', 'launder', 'keepall',
                                              'conv')}
    A = ['<!doctype html><html lang="en"><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>v2.5 — 32 papers</title><style>{CSS}{EXTRA}{EXTRA2}</style><body><div class="wrap">',
         '<h1>Traces v2.5 — two-step items, merged into traces</h1>',
         '<p class="mvm">Every verdict is model against model.</p>',
         '<p class="lead">Every item holds two steps. Composition merges them back into longer '
         'traces wherever one item&rsquo;s conclusion claim is the next item&rsquo;s input. The '
         'merged trace is the product. Numbers agree with docs/TRACES_V2P5.md.</p>',
         '<table class="idx"><thead><tr><th>paper</th><th>items</th><th>comp</th><th>edge</th>'
         '<th>cov</th><th>disc</th><th>FM</th><th>traces</th><th>depth</th><th>seams</th>'
         '<th>launder</th><th>all&nbsp;limits</th><th>rej</th><th>conv</th><th>size</th></tr></thead><tbody>']
    for r in rows:
        A.append(f'<tr><td><a href="{E(r["paper"])}.html">{E(r["paper"].split("__")[0].replace("_"," ")[:36])}</a></td>'
                 f'<td>{r["items"]}</td><td>{r["comp"]}</td><td>{r["edge"]}</td><td>{r["cov"]}</td>'
                 f'<td>{r["disc"]}</td><td>{r["fm"]}</td><td>{r["chains"]}</td>'
                 f'<td>{r["max_depth"] or "&mdash;"}</td><td>{r["joins"]}</td><td>{r["launder"]}</td>'
                 f'<td>{r["keepall"]}</td><td>{r["rejected"]}</td><td>{r["conv"]}</td>'
                 f'<td>{r["kb"]} KB</td></tr>')
    A.append(f'<tr><td><b>total</b></td><td><b>{T["items"]}</b></td><td><b>{T["comp"]}</b></td>'
             f'<td><b>{T["edge"]}</b></td><td><b>{T["cov"]}</b></td><td><b>{T["disc"]}</b></td>'
             f'<td><b>{T["fm"]}</b></td><td><b>{T["chains"]}</b></td><td>&mdash;</td>'
             f'<td><b>{T["joins"]}</b></td><td><b>{T["launder"]}</b></td>'
             f'<td><b>{T["keepall"]}</b></td><td><b>{T["rejected"]}</b></td>'
             f'<td><b>{T["conv"]}</b></td><td></td></tr>')
    A.append('</tbody></table></div></body></html>')
    open(os.path.join(out, 'index.html'), 'w').write('\n'.join(A))
    ph = collections.Counter(k for _, k in PLACEHOLDERS)
    print(f"{len(rows)} pages + index")
    print(f"totals: {T}")
    print(f"image fallbacks: {dict(ph)}")
    json.dump({'totals': T, 'rows': rows, 'fallbacks': dict(ph)},
              open(R('results/v2p5/pages_report.json'), 'w'), indent=1)


if __name__ == '__main__': main()
