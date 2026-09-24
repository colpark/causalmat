"""pages.py: one self-contained HTML per v4 trace.

  python3 trace_kit_v4/pages.py

Layout follows the v2 case pages (trace_kit_v2/paper_page.py -- the brief calls it
build_v2_pages.py, which does not exist in this repo). Panels are embedded as data URIs so a page
is one file. Tabs: the trace, the whole graph, before causality, provenance.

Provenance is audit-only and is labelled on the page as never shown to a solver.

Every verdict is model against model.
"""
import base64, html, io, json, os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
from PIL import Image
E = html.escape
STAGE = ['HYP', 'DES', 'PRC', 'STR', 'PRP', 'MEC', 'PRF', 'DSC', 'OBS', 'KNW']
_c = {}


def b64(p, maxw=560):
    if p in _c: return _c[p]
    im = Image.open(p).convert('RGB')
    if im.width > maxw: im = im.resize((maxw, max(1, round(im.height * maxw / im.width))), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=82, optimize=True)
    _c[p] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
    return _c[p]


def chips(txt):
    """render trailing [node id] markers as chips"""
    if not txt: return ''
    def rep(m):
        v = m.group(1)
        cls = 'chip inf' if 'writer inference' in v.lower() else 'chip'
        return f'<span class="{cls}">{E(v)}</span>'
    return re.sub(r'\[([^\]]+)\]', rep, E(txt))


def graph_svg(g, trace_claims, step_of):
    N = {n['id']: n for n in g['nodes']}
    col = collections.defaultdict(list)
    for n in g['nodes']:
        col[(n.get('type') or '?').split('/')[0]].append(n['id'])
    order = [s for s in STAGE if s in col] + [k for k in col if k not in STAGE]
    X, Y, pos = 150, 46, {}
    for ci, k in enumerate(order):
        for ri, nid in enumerate(col[k]): pos[nid] = (60 + ci * X, 54 + ri * Y)
    W = 60 + len(order) * X + 120
    H = 54 + max((len(v) for v in col.values()), default=1) * Y + 40
    out = [f'<svg viewBox="0 0 {W} {H}" class="gsvg" role="img" aria-label="argument graph">']
    for ci, k in enumerate(order):
        out.append(f'<text x="{60+ci*X}" y="28" class="gcol">{E(k)}</text>')
    for e in g['edges']:
        a, b = pos.get(e['src']), pos.get(e['dst'])
        if not a or not b: continue
        on = e['src'] in trace_claims and e['dst'] in trace_claims
        out.append(f'<line x1="{a[0]+52}" y1="{a[1]}" x2="{b[0]-4}" y2="{b[1]}" '
                   f'class="{"ge on" if on else "ge"}"/>')
    for nid, (x, y) in pos.items():
        n = N[nid]; on = nid in trace_claims
        st = step_of.get(nid)
        out.append(f'<g class="{"gn on" if on else "gn"}"><title>{E(n.get("label") or "")}</title>'
                   f'<rect x="{x-4}" y="{y-13}" width="56" height="26" rx="7"/>'
                   f'<text x="{x+24}" y="{y+4}">{E(nid)}</text></g>')
        if st:
            out.append(f'<text x="{x+24}" y="{y+26}" class="gstep">step {st}</text>')
    out.append('</svg>')
    return '\n'.join(out)


def v2_for(paper):
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'results/v2/cases', paper, '*', 'case.json'))):
        c = json.load(open(f))
        out.append({'claim': c['claim'], 'claim_text': c.get('claim_text'),
                    'steps': [{'node': s['node'], 'technique': s.get('technique'),
                               'expected': s.get('expected_support'),
                               'observation': s.get('observation')} for s in c['steps']],
                    'closing': c.get('closing_support')})
    return out


def v3b_for(trace, nsteps):
    d = os.path.join(ROOT, 'results/v3b', trace)
    q = {}
    f = os.path.join(d, 'full.r1.txt')
    if os.path.exists(f):
        for line in open(f):
            m = re.match(r'- Step (\d+) \[.*?\]: .*bears on \*\*(.+?)\*\*', line.strip())
            if m: q[int(m.group(1))] = m.group(2)
    ans = {}
    f = os.path.join(d, 'full.r1.out.txt')
    if os.path.exists(f):
        m = re.search(r'\{.*\}', open(f).read(), re.S)
        if m:
            try:
                for s in json.loads(m.group(0)).get('steps', []):
                    ans[int(s['step'])] = s.get('shows')
            except Exception: pass
    gr = {}
    f = os.path.join(d, 'grade', 'full.r1.out.txt')
    if os.path.exists(f):
        m = re.search(r'\{.*\}', open(f).read(), re.S)
        if m:
            try:
                for s in json.loads(m.group(0)).get('steps', []):
                    gr[int(s['step'])] = s.get('verdict')
            except Exception: pass
    return [{'step': i, 'property': q.get(i), 'answer': ans.get(i), 'verdict': gr.get(i)}
            for i in range(1, nsteps + 1)]


CSS = """
:root{--bg:#f7f7f5;--card:#fff;--ink:#16181d;--mut:#5d6470;--line:#e2e4e8;--acc:#2f6f4f;
--warn:#8a5a00;--hide:#7a3ea1;--chip:#eef1f5}
:root:not([data-theme=light]) @media (prefers-color-scheme:dark){}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#111317;--card:#181b21;
--ink:#e8eaee;--mut:#9aa3b2;--line:#2a2f38;--acc:#6fbf95;--warn:#e0a33a;--hide:#c79be8;--chip:#222732}}
:root[data-theme="dark"]{--bg:#111317;--card:#181b21;--ink:#e8eaee;--mut:#9aa3b2;--line:#2a2f38;
--acc:#6fbf95;--warn:#e0a33a;--hide:#c79be8;--chip:#222732}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 ui-sans-serif,-apple-system,
"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1080px;margin:0 auto;padding:26px 16px 60px}
h1{font-size:21px;margin:0 0 4px}
.sub{color:var(--mut);font-size:13px;margin:0 0 4px}
.mvm{color:var(--acc);font-size:12.5px;font-weight:600;margin:0 0 18px}
.tabs{display:flex;gap:6px;overflow-x:auto;padding:4px 0 0;margin-bottom:-1px}
.tab{flex:0 0 auto;background:transparent;border:1px solid var(--line);border-radius:9px 9px 0 0;
padding:8px 13px;color:var(--mut);cursor:pointer;font:inherit;font-size:13.5px}
.tab[aria-selected=true]{background:var(--card);color:var(--ink);border-bottom-color:var(--card);font-weight:600}
.panel{background:var(--card);border:1px solid var(--line);border-radius:0 12px 12px 12px;padding:18px}
.step{border:1px solid var(--line);border-radius:12px;padding:14px 15px;margin:0 0 4px;background:var(--card)}
.sh{display:flex;gap:9px;align-items:baseline;flex-wrap:wrap;margin-bottom:8px}
.sn{font:600 12px ui-monospace,Menlo,monospace;background:var(--chip);padding:2px 8px;border-radius:6px}
.prop{color:var(--mut);font-size:13px}
.q{background:var(--chip);border-left:3px solid var(--acc);padding:9px 12px;border-radius:0 8px 8px 0;margin:8px 0}
.q b{font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut);display:block}
.pans{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0}
.pan{border:1px solid var(--line);border-radius:9px;overflow:hidden;background:var(--bg);max-width:290px}
.pan img{display:block;width:100%;height:auto}
.pan .cap{font:11px ui-monospace,Menlo,monospace;color:var(--mut);padding:4px 7px}
.rr{margin:10px 0}
.rr h4{margin:10px 0 4px;font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.rr li{margin:3px 0}
.chip{font:600 10.5px ui-monospace,Menlo,monospace;background:var(--chip);color:var(--mut);
padding:1px 6px;border-radius:5px;margin-left:5px}
.chip.inf{background:transparent;border:1px dashed var(--warn);color:var(--warn)}
.hid{border:1px dashed var(--hide);border-radius:9px;padding:9px 12px;margin:10px 0}
.hid b{color:var(--hide);font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;display:block}
.arrow{text-align:center;color:var(--mut);font-size:12.5px;padding:6px 0 10px}
.arrow .lbl{display:inline-block;border:1px solid var(--line);border-radius:14px;padding:8px 15px;
background:var(--card);max-width:760px;text-align:left}
.comb{margin-top:7px;border-top:1px dashed var(--line);padding-top:7px;font-size:12.5px}
.comb b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--acc);margin-bottom:2px}
.comb.none b{color:var(--warn)}
.comb .from{color:var(--mut);font-size:11.5px;margin-top:3px}
.comb .from span{font-weight:600}
.dep{font-weight:600}.dep.real{color:var(--acc)}.dep.none{color:var(--warn)}
table{width:100%;border-collapse:collapse;font-size:13px;margin:8px 0}
th,td{border-bottom:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top}
th{color:var(--mut);font-size:11.5px;text-transform:uppercase;letter-spacing:.04em}
.gsvg{width:100%;height:auto;background:var(--bg);border:1px solid var(--line);border-radius:10px}
.gcol{font:600 11px ui-monospace,Menlo,monospace;fill:var(--mut)}
.gn rect{fill:var(--card);stroke:var(--line)}
.gn text{font:600 11px ui-monospace,Menlo,monospace;fill:var(--mut);text-anchor:middle}
.gn.on rect{fill:var(--acc);stroke:var(--acc)}.gn.on text{fill:#fff}
.gstep{font:10px ui-monospace,Menlo,monospace;fill:var(--acc);text-anchor:middle}
.ge{stroke:var(--line);stroke-width:1}.ge.on{stroke:var(--acc);stroke-width:2.2}
.audit{border:1px solid var(--warn);border-radius:10px;padding:12px 14px;background:var(--card)}
.audit b{color:var(--warn)}
@media(max-width:640px){.wrap{padding:18px 16px 50px}.pan{max-width:100%}}
"""

JS = """const tabs=[...document.querySelectorAll('[role=tab]')],ps=[...document.querySelectorAll('[role=tabpanel]')];
function show(id){tabs.forEach(t=>{const on=t.id==='tab-'+id;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1});
ps.forEach(p=>{p.hidden=p.id!=='panel-'+id})}
tabs.forEach(t=>t.addEventListener('click',()=>show(t.id.slice(4))));
document.querySelector('[role=tablist]').addEventListener('keydown',e=>{
const i=tabs.findIndex(t=>t.getAttribute('aria-selected')==='true');let n=null;
if(e.key==='ArrowRight')n=(i+1)%tabs.length;else if(e.key==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;
if(n!==null){show(tabs[n].id.slice(4));tabs[n].focus();e.preventDefault()}});"""


def build(t):
    d = os.path.join(ROOT, 'results/v4', t['trace'])
    dep = {r['step']: r for r in json.load(open(os.path.join(d, 'dependency.json')))['steps']}
    g = json.load(open(os.path.join(ROOT, t['graph'])))
    tc = {c for s in t['steps'] for c in s['claims']}
    step_of = {c: s['step'] for s in t['steps'] for c in s['claims']}
    A = []
    P = A.append
    P(f'<!doctype html><html lang="en"><meta charset="utf-8">')
    P(f'<meta name="viewport" content="width=device-width,initial-scale=1">')
    P(f'<title>{E(t["trace"])}</title><style>{CSS}</style><body><div class="wrap">')
    P(f'<h1>{E(t["trace"])}</h1>')
    P(f'<p class="sub">{E(t["paper"])} &middot; chain {E(" &rarr; ".join(t["chain"]))} '
      f'&middot; {len(t["steps"])} steps</p>')
    P('<p class="mvm">Every verdict is model against model.</p>')
    T = [('trace', 'The trace'), ('graph', 'Whole graph'),
         ('before', 'Before causality'), ('prov', 'Provenance')]
    P('<div class="tabs" role="tablist" aria-label="views">')
    for i, (k, lbl) in enumerate(T):
        P(f'<button class="tab" role="tab" id="tab-{k}" aria-controls="panel-{k}" '
          f'aria-selected="{"true" if not i else "false"}" tabindex="{0 if not i else -1}">{E(lbl)}</button>')
    P('</div>')

    # --- the trace
    P('<div class="panel" role="tabpanel" id="panel-trace" aria-labelledby="tab-trace">')
    for i, s in enumerate(t['steps']):
        r = s.get('reference_reasoning') or {}
        dd = dep.get(s['step'], {})
        P('<div class="step">')
        P(f'<div class="sh"><span class="sn">step {s["step"]}</span>'
          f'<span class="prop">{E(s["property"])}</span></div>')
        P(f'<div class="q"><b>question, as the solver sees it</b>{E(s["question"])}</div>')
        pans = [p for p in s['panels'] if p.get('png')]
        if pans:
            P('<div class="pans">')
            for p in pans:
                src = b64(os.path.join(ROOT, 'results/v3/traces', t['trace'], p['png']))
                P(f'<figure class="pan"><img src="{src}" alt="panel {E(p["suffix"])}">'
                  f'<figcaption class="cap">{E(p["suffix"])}</figcaption></figure>')
            P('</div>')
        else:
            P(f'<p class="prop">Delivered as a measurement, not an image &mdash; {E(str(s["technique"]))}.</p>')
        if r:
            P('<div class="rr">')
            P('<h4>what each observation shows</h4><ul>')
            for o in (r.get('observations') or []): P(f'<li>{chips(o)}</li>')
            P('</ul>')
            for k, lbl in (('proposition', 'the proposition it supports'),
                           ('assumption', 'the assumption the inference needs'),
                           ('open', 'what remains open'),
                           ('handoff', 'what is handed to the next step')):
                if r.get(k): P(f'<h4>{lbl}</h4><p>{chips(r[k])}</p>')
            P('</div>')
        P(f'<div class="hid"><b>hidden effect &mdash; not shown to the solver</b>{E(s["output"])}</div>')
        P('</div>')
        if i + 1 < len(t['steps']):
            nxt = t['steps'][i + 1]
            nd = dep.get(nxt['step'], {})
            cmb = nxt.get('combining')
            cls = 'real' if nd.get('dependency') == 'real' else 'none'
            P('<div class="arrow"><div class="lbl">')
            P(f'&darr; passes on: {E((r.get("handoff") or s["output_short"] or "")[:150])}')
            P(f'<br><span class="dep {cls}">dependency: {E(str(nd.get("dependency")))}'
              f'{" &middot; " + E(cmb["kind"]) if cmb else ""}</span>')
            if cmb:
                P(f'<div class="comb"><b>combining proposition</b>{E(cmb["proposition"])}'
                  f'<div class="from"><span>from step {s["step"]}:</span> {E(cmb["from_previous"])}</div>'
                  f'<div class="from"><span>from step {nxt["step"]}:</span> {E(cmb["from_this"])}</div>'
                  f'</div>')
            elif nd.get('why'):
                P(f'<div class="comb none"><b>no combining proposition</b>{E(str(nd["why"])[:300])}</div>')
            P('</div></div>')
    if t.get('end_to_end'):
        e = t['end_to_end']
        P('<div class="step"><div class="sh"><span class="sn">end to end</span></div><ul>')
        for line in (e.get('reasoning') or []): P(f'<li>{chips(line)}</li>')
        P('</ul>')
        if e.get('weakest_step'):
            P(f'<p><b>weakest step:</b> step {E(str(e["weakest_step"]))} &mdash; {E(str(e.get("why_weakest")))}</p>')
        P('</div>')
    P('</div>')

    # --- whole graph
    P('<div class="panel" role="tabpanel" id="panel-graph" aria-labelledby="tab-graph" hidden>')
    P('<p class="sub">The paper&rsquo;s argument graph. The trace&rsquo;s claims and the edges '
      'between them are highlighted; hover a node for its label.</p>')
    P(graph_svg(g, tc, step_of))
    P('<table><thead><tr><th>step</th><th>claims</th><th>hop</th><th>stage type</th></tr></thead><tbody>')
    for s in t['steps']:
        pv = s['provenance_NOT_SOLVER_VISIBLE']
        P(f'<tr><td>{s["step"]}</td><td>{E(", ".join(s["claims"]))}</td>'
          f'<td>{E(pv["matmech_hop"])}</td><td>{E(pv["stage_type"])}</td></tr>')
    P('</tbody></table></div>')

    # --- before causality
    P('<div class="panel" role="tabpanel" id="panel-before" aria-labelledby="tab-before" hidden>')
    P('<p class="sub">The same claims, as the three designs put them. v2 asked whether evidence '
      'supports a claim. v3b hid the effect and asked what the evidence establishes. v4 adds the '
      'dependency between steps.</p>')
    v3 = {r['step']: r for r in v3b_for(t['trace'], len(t['steps']))}
    P('<table><thead><tr><th>step</th><th>v2</th><th>v3b</th><th>v4</th></tr></thead><tbody>')
    v2c = v2_for(t['paper'])
    for s in t['steps']:
        b = v3.get(s['step'], {})
        v2txt = '; '.join(f"{c['claim']}: {len(c['steps'])} evidence steps &rarr; {c['closing']}"
                          for c in v2c) or '&mdash; not a v2 case'
        dd = dep.get(s['step'], {})
        P(f'<tr><td>{s["step"]}</td><td>{v2txt}</td>'
          f'<td><i>{E(str(b.get("property")))}</i><br>{E(str(b.get("answer"))[:230])}'
          f'<br><b>{E(str(b.get("verdict")))}</b></td>'
          f'<td>{E(s["question"][:200])}<br><b>dependency: {E(str(dd.get("dependency")))}</b>'
          + (f'<br><i>v4 said {E(str(dd.get("v4_label")))}; re-judged on the data</i>'
             if dd.get('v4_label') and dd.get('v4_label') != dd.get('dependency') else '')
          + f'<br>{E(str(dd.get("why"))[:220])}</td></tr>')
    P('</tbody></table></div>')

    # --- provenance
    P('<div class="panel" role="tabpanel" id="panel-prov" aria-labelledby="tab-prov" hidden>')
    P('<div class="audit"><b>Audit only &mdash; none of this is ever shown to a solver.</b>'
      '<p class="sub">MatMech supplied which stretches of the spine are causal steps. Every word a '
      'solver sees comes from our graph.</p>')
    P('<table><thead><tr><th>step</th><th>hop</th><th>stage type</th><th>figures</th>'
      '<th>link confirmed by</th></tr></thead><tbody>')
    for s in t['steps']:
        pv = s['provenance_NOT_SOLVER_VISIBLE']
        P(f'<tr><td>{s["step"]}</td><td>{E(pv["matmech_hop"])}</td><td>{E(pv["stage_type"])}</td>'
          f'<td>{E(", ".join(pv.get("matmech_figures") or []))}</td>'
          f'<td>{E(str(pv.get("link_confirmed_by") or "&mdash;"))}</td></tr>')
    P('</tbody></table></div></div>')

    P(f'</div><script>{JS}</script></body></html>')
    return '\n'.join(A)


def main():
    out = os.path.join(ROOT, 'results/v4/pages'); os.makedirs(out, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(ROOT, 'results/v4/*/trace.json'))):
        t = json.load(open(f))
        p = os.path.join(out, t['trace'] + '.html')
        open(p, 'w').write(build(t))
        print(f"  {os.path.relpath(p, ROOT):46s} {os.path.getsize(p)//1024} KB")


if __name__ == '__main__': main()
