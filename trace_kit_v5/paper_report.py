"""paper_report.py: one self-contained report per paper, all 32.

  python3 trace_kit_v5/paper_report.py

Five sections, in order: the original graph; all of MatMech's causality; how the traces were
extracted; how the traces merge with that causality; the final traces.

Papers with no surviving item get the same report, and its third and fourth sections say where the
pipeline stopped. Most of them stop in the same place -- the hops attach to evidence and then no two
consecutive hops can be joined.

**Section 2 prints MatMech's cause and effect spans in full.** That is deliberate and is the one
place they appear. It is labelled audit-only on the page, and these reports are excluded from the
solver-facing leak check for that reason; nothing in section 5, which is what a solver would see,
draws on them.

Every verdict is model against model.
"""
import base64, html, io, json, os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v3'))
from cut_traces import store_for, panel_record
from support import claim_support
from PIL import Image
E = html.escape
STAGE = ['HYP', 'DES', 'PRC', 'STR', 'PRP', 'MEC', 'PRF', 'DSC', 'KNW', 'OBS']
_c = {}


def thumb(p, maxw=230):
    if p in _c: return _c[p]
    try:
        im = Image.open(p).convert('RGB')
    except Exception:
        return None
    if im.width > maxw: im = im.resize((maxw, max(1, round(im.height * maxw / im.width))), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=76, optimize=True)
    _c[p] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
    return _c[p]


CSS = """
:root{--bg:#f7f7f5;--card:#fff;--ink:#16181d;--mut:#5d6470;--line:#e2e4e8;--acc:#2f6f4f;
--warn:#8a5a00;--hide:#7a3ea1;--chip:#eef1f5;--bad:#b3261e}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#111317;--card:#181b21;
--ink:#e8eaee;--mut:#9aa3b2;--line:#2a2f38;--acc:#6fbf95;--warn:#e0a33a;--hide:#c79be8;
--chip:#222732;--bad:#ff6b5e}}
:root[data-theme="dark"]{--bg:#111317;--card:#181b21;--ink:#e8eaee;--mut:#9aa3b2;--line:#2a2f38;
--acc:#6fbf95;--warn:#e0a33a;--hide:#c79be8;--chip:#222732;--bad:#ff6b5e}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.6 ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:26px 16px 70px}
h1{font-size:22px;margin:0 0 4px}
h2{font-size:17px;margin:34px 0 4px;padding-top:16px;border-top:2px solid var(--line)}
h2 .n{color:var(--mut);font:600 13px ui-monospace,Menlo,monospace;margin-right:8px}
h3{font-size:13.5px;margin:18px 0 6px;color:var(--mut)}
.sub{color:var(--mut);font-size:13px;margin:0 0 4px}
.mvm{color:var(--acc);font-size:12.5px;font-weight:600;margin:0 0 6px}
.lead{color:var(--mut);font-size:13px;margin:4px 0 12px}
table{width:100%;border-collapse:collapse;font-size:12.5px;margin:10px 0}
th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{color:var(--mut);font-size:11px;text-transform:uppercase;letter-spacing:.04em}
code,.id{font:600 11.5px ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 6px;border-radius:5px}
.stage{margin:10px 0;border:1px solid var(--line);border-radius:10px;background:var(--card);padding:10px 12px}
.stage h4{margin:0 0 6px;font:600 11px ui-monospace,Menlo,monospace;color:var(--mut);letter-spacing:.06em}
.node{padding:5px 0;border-bottom:1px dashed var(--line)}
.node:last-child{border-bottom:0}
.sup{font:600 10.5px ui-monospace,Menlo,monospace;padding:1px 6px;border-radius:4px;margin-left:5px}
.sup.shown{background:var(--acc);color:#fff}.sup.partial{background:var(--warn);color:#fff}
.sup.contradicts{background:var(--bad);color:#fff}
.pans{display:flex;flex-wrap:wrap;gap:7px;margin:6px 0}
.pan{border:1px solid var(--line);border-radius:7px;overflow:hidden;background:var(--bg);max-width:236px}
.pan img{display:block;width:100%;height:auto}
.pan .cap{font:10.5px ui-monospace,Menlo,monospace;color:var(--mut);padding:3px 6px}
.audit-only{border:2px solid var(--warn);border-radius:10px;padding:11px 14px;margin:10px 0;background:var(--card)}
.audit-only b{color:var(--warn)}
.hop{border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin:8px 0;background:var(--card)}
.span{font-size:12.5px;color:var(--mut);margin:3px 0}
.span b{color:var(--ink)}
.chain{border:1px solid var(--acc);border-radius:10px;padding:10px 13px;margin:10px 0;background:var(--card)}
.link{font-size:13px;margin:5px 0}
.str{font:600 10.5px ui-monospace,Menlo,monospace;padding:1px 6px;border-radius:4px;margin-right:6px}
.str.span{background:var(--acc);color:#fff}.str.stagegraph{background:var(--chip);color:var(--acc)}
.str.stage_only{background:var(--chip);color:var(--mut)}
.item{border:1px solid var(--line);border-radius:12px;padding:14px 15px;margin:12px 0;background:var(--card)}
.q{background:var(--chip);border-left:3px solid var(--acc);padding:9px 12px;border-radius:0 8px 8px 0;margin:8px 0}
.q b{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut);display:block}
.key{border-left:3px solid var(--acc);background:var(--chip);padding:9px 12px;border-radius:0 8px 8px 0;margin:8px 0}
.lim{border-left:3px solid var(--warn);padding:7px 12px;margin:7px 0;font-size:13px}
.ni{border:1px dashed var(--hide);border-radius:9px;padding:8px 11px;margin:7px 0;font-size:12.5px}
.ni b{color:var(--hide);font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;display:block}
.lab{display:flex;gap:7px;flex-wrap:wrap;margin:8px 0}
.lab span{font-size:11.5px;background:var(--chip);border-radius:6px;padding:3px 9px;color:var(--mut)}
.lab b{color:var(--ink)}
.prov{font:600 10.5px ui-monospace,Menlo,monospace;padding:2px 8px;border-radius:5px;margin-left:6px}
.prov.hand{background:var(--acc);color:#fff}.prov.draft{background:var(--chip);color:var(--mut)}
.prov.fixed{background:var(--warn);color:#fff}
.v{font:600 10.5px ui-monospace,Menlo,monospace;padding:1px 6px;border-radius:4px;margin-right:6px}
.v.holds{background:var(--chip);color:var(--acc)}.v.overreaches{background:var(--warn);color:#fff}
.v.wrong{background:var(--bad);color:#fff}.v.mixed{background:var(--warn);color:#fff}
.v.same_kind{background:var(--chip);color:var(--acc)}
.was{font-size:12px;color:var(--mut);border-left:2px dashed var(--warn);padding:4px 10px;margin:5px 0}
.miss{border:2px solid var(--bad);border-radius:9px;padding:9px 12px;margin:8px 0;font-size:12.5px}
.miss b{color:var(--bad);font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;display:block}
.stop{border:2px solid var(--warn);border-radius:10px;padding:13px 15px;background:var(--card);margin:12px 0}
.stop b{color:var(--warn)}
.gsvg{width:100%;height:auto;background:var(--bg);border:1px solid var(--line);border-radius:10px;margin:10px 0}
.gcol{font:600 10.5px ui-monospace,Menlo,monospace;fill:var(--mut)}
.gn rect{fill:var(--card);stroke:var(--line)}
.gn text{font:600 10px ui-monospace,Menlo,monospace;fill:var(--mut);text-anchor:middle}
.gn.on rect{fill:var(--acc);stroke:var(--acc)}.gn.on text{fill:#fff}
.ge{stroke:var(--line);stroke-width:1}.ge.on{stroke:var(--acc);stroke-width:2.4}
@media(max-width:640px){.wrap{padding:18px 14px 50px}.pan{max-width:100%}}
"""


def graph_svg(g, on=(), label=None):
    N = {n['id']: n for n in g['nodes']}
    col = collections.defaultdict(list)
    for n in g['nodes']: col[(n.get('type') or '?').split('/')[0]].append(n['id'])
    order = [s for s in STAGE if s in col] + [k for k in col if k not in STAGE]
    X, Y, pos = 128, 40, {}
    for ci, k in enumerate(order):
        for ri, nid in enumerate(col[k]): pos[nid] = (52 + ci * X, 50 + ri * Y)
    W = 52 + len(order) * X + 70
    H = 50 + max((len(v) for v in col.values()), default=1) * Y + 30
    o = [f'<svg viewBox="0 0 {W} {H}" class="gsvg" role="img" aria-label="argument graph">']
    for ci, k in enumerate(order): o.append(f'<text x="{52+ci*X}" y="26" class="gcol">{E(k)}</text>')
    for e in g['edges']:
        a, b = pos.get(e['src']), pos.get(e['dst'])
        if not a or not b: continue
        hot = e['src'] in on and e['dst'] in on
        o.append(f'<line x1="{a[0]+48}" y1="{a[1]}" x2="{b[0]-3}" y2="{b[1]}" '
                 f'class="{"ge on" if hot else "ge"}"/>')
    for nid, (x, y) in pos.items():
        o.append(f'<g class="{"gn on" if nid in on else "gn"}">'
                 f'<title>{E((N[nid].get("label") or "")[:180])}</title>'
                 f'<rect x="{x-3}" y="{y-12}" width="52" height="24" rx="6"/>'
                 f'<text x="{x+23}" y="{y+4}">{E(nid)}</text></g>')
    o.append('</svg>')
    return '\n'.join(o)


def build(paper, ctx):
    g, hops, stitch, dec, funnel, items, surv, comp = (ctx[k] for k in
        ('graph', 'hops', 'stitch', 'dec', 'funnel', 'items', 'surv', 'comp'))
    N = {n['id']: n for n in g['nodes']}
    store = ctx['store']
    A = []; P = A.append
    short = paper.split('__')[0].replace('_', ' ')
    P('<!doctype html><html lang="en"><meta charset="utf-8">')
    P('<meta name="viewport" content="width=device-width,initial-scale=1">')
    P(f'<title>{E(short)}</title><style>{CSS}</style><body><div class="wrap">')
    P(f'<h1>{E(short)}</h1><p class="sub">{E(paper)}</p>')
    P('<p class="mvm">Every verdict is model against model.</p>')
    P(f'<p class="lead">{funnel["hops"]} MatMech hops &middot; {funnel["attachable"]} attachable '
      f'&middot; {funnel["links"]} links &middot; {funnel["traces"]} traces &middot; '
      f'{len(surv)} surviving item{"s" if len(surv)!=1 else ""}</p>')

    # ---- 1 the original graph
    P('<h2><span class="n">1</span>The original graph</h2>')
    P('<p class="lead">Our argument graph in full, in stage order. Spine claims first, then the '
      'observation nodes with the panels behind them and the image verdict recorded for each.</p>')
    P(graph_svg(g))
    byst = collections.defaultdict(list)
    for n in g['nodes']: byst[(n.get('type') or '?').split('/')[0]].append(n)
    for st in [s for s in STAGE if s in byst] + [k for k in byst if k not in STAGE]:
        P(f'<div class="stage"><h4>{E(st)}</h4>')
        for n in byst[st]:
            sup = n.get('image_support')
            P(f'<div class="node"><span class="id">{E(n["id"])}</span> '
              f'<span class="sub">{E(n.get("type") or "")}</span>'
              + (f'<span class="sup {E(sup)}">{E(sup)}</span>' if sup else '')
              + f'<br>{E(n.get("label") or "")}')
            pids = n.get('panel_ids') or []
            if pids:
                P('<div class="pans">')
                for pid in pids[:8]:
                    r = panel_record(store, pid) or {}
                    src = thumb(r['crop']) if r.get('crop') and os.path.exists(r['crop']) else None
                    if src:
                        P(f'<figure class="pan"><img src="{src}" alt="{E(pid)}">'
                          f'<figcaption class="cap">{E(pid.split("#")[-1])}</figcaption></figure>')
                    else:
                        P(f'<span class="id">{E(pid.split("#")[-1])} (no crop)</span>')
                P('</div>')
            P('</div>')
        P('</div>')

    # ---- 2 MatMech's causality
    P('<h2><span class="n">2</span>MatMech&rsquo;s causality, all of it</h2>')
    P('<div class="audit-only"><b>Audit only. None of section 2 is ever shown to a solver.</b> '
      'MatMech supplies which stretches of the argument are causal steps; every word a solver sees '
      'comes from our graph, in section 5.</div>')
    for h in hops['hops']:
        sp = h['_matmech_span_DO_NOT_PROMPT']
        P(f'<div class="hop"><span class="id">{E(h["id"])}</span> '
          f'<b>{E(str(h.get("stage_type")))}</b>')
        P(f'<div class="span"><b>cause:</b> {E(str(sp.get("cause")))}</div>')
        P(f'<div class="span"><b>effect:</b> {E(str(sp.get("effect")))}</div>')
        P(f'<div class="span"><b>experiment:</b> {E(str(h.get("experiment_name")))} &middot; '
          f'techniques: {E(", ".join(h.get("techniques") or []) or "&mdash;")} &middot; '
          f'figures: {E(", ".join(h.get("figures") or []) or "&mdash;")}</div>')
        ki = h.get('knowledge_imported') or {}
        if ki.get('count'):
            P(f'<div class="span"><b>imported knowledge ({ki["count"]}):</b> '
              + E('; '.join(str(x) for x in (ki.get('items') or []))[:400]) + '</div>')
        P('</div>')

    # ---- 3 extraction
    P('<h2><span class="n">3</span>How the traces were extracted</h2>')
    P('<table><thead><tr><th>hops</th><th>attachable</th><th>links</th><th>usable</th>'
      '<th>traces</th><th>items</th><th>survivors</th></tr></thead><tbody>')
    P(f'<tr><td>{funnel["hops"]}</td><td>{funnel["attachable"]}</td><td>{funnel["links"]}</td>'
      f'<td>{funnel["links"]}</td><td>{funnel["traces"]}</td><td>{funnel["items"]}</td>'
      f'<td>{len(surv)}</td></tr></tbody></table>')
    P('<h3>the stitch, hop by hop</h3>')
    P('<table><thead><tr><th>hop</th><th>our claims matched</th><th>why</th>'
      '<th>completion</th><th>evidence</th></tr></thead><tbody>')
    lex = {x['hop']: x for x in stitch['hops']}
    for h in hops['hops']:
        d = (dec.get('hops') or {}).get(h['id'], {}).get('effect', {})
        cl = d.get('claims') or []
        why = '; '.join(f"{k}: {str(v)[:90]}" for k, v in (d.get('why') or {}).items())
        before = d.get('claims_before_completion')
        repl = [c for c in comp if c['hop'] == h['id'] and c['paper'] == paper]
        rp = '; '.join(f"{r['replaced']} &rarr; {r['with']}" for r in repl) or '&mdash;'
        nev = (lex.get(h['id']) or {}).get('n_evidence', 0)
        P(f'<tr><td><span class="id">{E(h["id"])}</span></td>'
          f'<td>{E(", ".join(cl) or "none")}</td><td>{E(why[:260])}</td>'
          f'<td>{rp}</td><td>{nev}</td></tr>')
    P('</tbody></table>')

    # ---- 4 merge
    P('<h2><span class="n">4</span>How the traces merge with causality</h2>')
    links = [h for h in hops['hops'] if h.get('next')]
    if not links:
        P('<div class="stop"><b>The pipeline stops here.</b> No hop in this paper chains to '
          'another: no two consecutive hops share one of our spine claims or are joined by a spine '
          'edge, so there is no chain to build a trace on. The hops do attach to evidence '
          f'({funnel["attachable"]} of {funnel["hops"]}); what is missing is the join.</div>')
    else:
        P('<table><thead><tr><th>link</th><th>strength</th><th>confirmed by</th></tr></thead><tbody>')
        for h in links:
            s = h.get('chain_strength') or 'unconfirmed'
            P(f'<tr><td><span class="id">{E(h["id"])} &rarr; {E(h["next"])}</span></td>'
              f'<td><span class="str {E(s.replace("+","graph"))}">{E(s)}</span></td>'
              f'<td>{E(str(h.get("link_confirmed_by") or "not confirmed, excluded"))}</td></tr>')
        P('</tbody></table>')
        onc = {c for it in surv for c in it['claims']}
        if onc:
            P('<h3>the confirmed chain, drawn over the paper&rsquo;s argument</h3>')
            P(graph_svg(g, onc))
        elif funnel['items'] == 0:
            P('<div class="stop"><b>Links exist, but not on one path.</b> The confirmed links and '
              'the hops that attach to evidence do not line up into a single chain, so no trace '
              'was built.</div>')

    # ---- 5 final traces
    P('<h2><span class="n">5</span>The final traces</h2>')
    if not surv:
        P('<div class="stop"><b>No surviving item for this paper.</b> '
          + E(ctx['stop_reason']) + '</div>')
    for it in surv:
        k = it.get('key') or {}; L = k.get('labels') or {}
        cls = ('hand' if k.get('hand_calibrated') else
               'fixed' if (k.get('proposition_before_audit') or
                           k.get('proposition_before_quantity_fix')) else 'draft')
        lbl = (k.get('hand_calibrated') if cls == 'hand'
               else 'drafted, audited and fixed' if cls == 'fixed' else 'drafted key')
        P(f'<div class="item"><span class="id">{E(it["item"])}</span>'
          f'<span class="prov {cls}">{E(lbl)}</span>')
        P(f'<div class="q"><b>question, as the solver sees it</b>{E(it["property"])}</div>')
        if it.get('previous_output'):
            P(f'<p class="sub">takes from step {it["previous_step"]}: '
              f'{E(it["previous_output"][:200])}</p>')
        pans = [p for p in it['panels'] if p.get('png')]
        if pans:
            P('<div class="pans">')
            for p in pans:
                fp = os.path.join(ROOT, 'results/v5/traces', it['trace'], p['png'])
                src = thumb(fp) if os.path.exists(fp) else None
                if src: P(f'<figure class="pan"><img src="{src}" alt="{E(p["suffix"])}">'
                          f'<figcaption class="cap">{E(p["suffix"])}</figcaption></figure>')
            P('</div>')
        if it.get('panels_dropped_by_cap'):
            P(f'<p class="sub">dropped by the five-panel cap: '
              f'{E(", ".join(it["panels_dropped_by_cap"]))}</p>')
        P(f'<div class="lab"><span>depth <b>{E(str(it.get("depth")))}</b></span>'
          f'<span>causal strength <b>{E(str(L.get("causal_strength")))}</b></span>'
          f'<span>dependency <b>{E(str(L.get("dependency")))}</b></span>'
          f'<span>inference <b>{E(str(L.get("inference_validity")))}</b></span>'
          f'<span>lane <b>{"FM" if it.get("fm_lane") else "other"}</b></span></div>')
        q = it.get('quantity_kind')
        if q:
            P(f'<p><span class="v {E(q["ruling"])}">{E(q["ruling"])}</span>'
              f'{E(str(q.get("a")))} <i>({E(str(q.get("kind_a")))})</i> against '
              f'{E(str(q.get("b")))} <i>({E(str(q.get("kind_b")))})</i></p>')
        P(f'<div class="key"><b>combining proposition</b><br>{E(str(k.get("proposition")))}</div>')
        for f_, t_ in (('proposition_before_audit', 'the audit'),
                       ('proposition_before_quantity_fix', 'the quantity-kind fix')):
            if k.get(f_): P(f'<div class="was"><b>before {t_}:</b> {E(str(k[f_])[:420])}</div>')
        if k.get('limits'):
            P('<div class="lim"><b>limits</b><ul>')
            for l in k['limits']: P(f'<li>{E(str(l))}</li>')
            P('</ul></div>')
        if k.get('not_identifiable'):
            P(f'<div class="ni"><b>not identifiable</b>{E(str(k["not_identifiable"]))}</div>')
        sc = k.get('scoring') or {}
        if sc: P(f'<p class="sub"><b>scoring target:</b> {E(str(sc.get("target")))} &mdash; '
                 f'{sc.get("n_required")} required elements. {E(str(sc.get("insufficient_alone")))}</p>')
        a = it.get('audit') or {}
        if a.get('statements'):
            P('<h3>audit</h3><table><thead><tr><th>statement</th><th>verdict</th>'
              '<th>evidence quoted</th></tr></thead><tbody>')
            for s in a['statements']:
                v = s.get('verdict') or 'unruled'
                P(f'<tr><td>{E(str(s.get("what")))}</td>'
                  f'<td><span class="v {E(v)}">{E(v)}</span></td>'
                  f'<td>{E(str(s.get("evidence") or "&mdash;")[:300])}</td></tr>')
            P('</tbody></table>')
        for m in (a.get('misses') or []):
            P(f'<div class="miss"><b>audit miss &mdash; found by {E(str(m.get("found_by")))}</b>'
              f'{E(str(m.get("what")))}<br><i>{E(str(m.get("why_it_matters")))}</i></div>')
        P('</div>')
    if ctx['dropped']:
        P('<h3>items dropped</h3><table><thead><tr><th>item</th><th>why</th></tr></thead><tbody>')
        for d in ctx['dropped']:
            P(f'<tr><td><span class="id">{E(d["item"])}</span></td><td>{E(d["why"])}</td></tr>')
        P('</tbody></table>')
    P('</div></body></html>')
    return '\n'.join(A)


def main():
    papers = [x['paper'] for x in json.load(open(os.path.join(ROOT, 'results/v5_papers.json')))]
    I = {i['item']: i for i in json.load(open(os.path.join(ROOT, 'results/v5/items.json')))['items']}
    S = [r['item'] for r in json.load(open(os.path.join(ROOT, 'results/v5/survival_v5b.json')))['surviving']]
    drops = json.load(open(os.path.join(ROOT, 'results/v5/survival.json')))['dropped']
    fun = {r['paper']: r for r in json.load(open(os.path.join(ROOT, 'results/v5/funnel.json')))['rows']}
    comp = json.load(open(os.path.join(ROOT, 'results/v3/completion_log.json')))
    out = os.path.join(ROOT, 'results/v5/reports'); os.makedirs(out, exist_ok=True)
    tot = 0
    for p in papers:
        st = json.load(open(os.path.join(ROOT, 'results/v3', p, 'stitch.json')))
        gp = os.path.join(ROOT, st['graph'])
        f = fun[p]
        surv = sorted([I[s] for s in S if I[s]['paper'] == p],
                      key=lambda x: (x['trace'], x['step'], x['sub']))
        dr = [d for d in drops if I.get(d['item'], {}).get('paper') == p]
        for a, b in [('journal_of_m_M2_M4_s2_2', 'merged into journal_of_m_M2_M4_s2_1')]:
            if a in I and I[a]['paper'] == p: dr.append({'item': a, 'why': I[a].get('merge_why', b)})
        reason = ('no confirmed link anywhere in this paper, so no chain' if f['links'] == 0 else
                  'the confirmed links and the attachable hops do not lie on one path'
                  if f['traces'] == 0 else
                  'every item was dropped: its key contained no combining proposition, or the '
                  'dependency was not real')
        ctx = {'graph': json.load(open(gp)),
               'hops': json.load(open(os.path.join(ROOT, 'results/v3', p, 'hops.json'))),
               'stitch': st,
               'dec': json.load(open(os.path.join(ROOT, 'results/v3', p, 'decompose.json'))),
               'funnel': f, 'items': I, 'surv': surv, 'comp': comp,
               'store': store_for(gp), 'dropped': dr, 'stop_reason': reason}
        fp = os.path.join(out, p + '.html')
        open(fp, 'w').write(build(p, ctx))
        tot += os.path.getsize(fp)
        print(f"  {p[:56]:56s} {len(surv)} items  {os.path.getsize(fp)//1024:5d} KB")
    print(f"\n{len(papers)} reports, {tot//1024//1024} MB total")


if __name__ == '__main__': main()
