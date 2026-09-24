"""pages.py: one self-contained page per trace that has a surviving v5 item.

Layout follows the v4 pages. Each item shows the question, the quantity kinds on both sides, the
evidence, and the key -- proposition, limits, what is permitted and what is not, and what is not
identifiable. Every item is marked hand-calibrated or draft, because at 32 papers only seven keys
are hand-written and the rest are model drafts (brief item 10).

Every verdict is model against model.
"""
import base64, html, io, json, os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v4'))
from pages import CSS, JS, b64, graph_svg
E = html.escape

EXTRA = """
.item{border:1px solid var(--line);border-radius:12px;padding:15px;margin:0 0 14px;background:var(--card)}
.badge{font:600 10.5px ui-monospace,Menlo,monospace;padding:2px 7px;border-radius:5px;margin-left:6px}
.badge.hand{background:var(--acc);color:#fff}.badge.draft{background:var(--chip);color:var(--mut)}
.badge.ni{background:transparent;border:1px dashed var(--hide);color:var(--hide)}
.lab{display:flex;gap:8px;flex-wrap:wrap;margin:9px 0}
.lab span{font-size:11.5px;background:var(--chip);border-radius:6px;padding:3px 9px;color:var(--mut)}
.lab b{color:var(--ink)}
.key{border-left:3px solid var(--acc);background:var(--chip);padding:10px 13px;border-radius:0 8px 8px 0;margin:9px 0}
.key h5{margin:0 0 4px;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.lim{border-left:3px solid var(--warn);padding:8px 13px;margin:8px 0;font-size:13px}
.lim h5{margin:0 0 4px;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--warn)}
.ni{border:1px dashed var(--hide);border-radius:9px;padding:9px 12px;margin:8px 0;font-size:13px}
.ni b{color:var(--hide);font-size:11px;text-transform:uppercase;letter-spacing:.05em;display:block}
.qty{font-size:12px;color:var(--mut);margin:6px 0}
"""


def build(trace, its, t):
    g = json.load(open(os.path.join(ROOT, t['graph'])))
    tc = {c for i in its for c in i['claims']}
    step_of = {c: i['step'] for i in its for c in i['claims']}
    A = []; P = A.append
    P('<!doctype html><html lang="en"><meta charset="utf-8">')
    P('<meta name="viewport" content="width=device-width,initial-scale=1">')
    P(f'<title>{E(trace)}</title><style>{CSS}{EXTRA}</style><body><div class="wrap">')
    P(f'<h1>{E(trace)}</h1>')
    P(f'<p class="sub">{E(t["paper"])} &middot; chain {E(" &rarr; ".join(t["chain"]))} '
      f'&middot; {len(its)} surviving item{"s" if len(its)!=1 else ""}</p>')
    P('<p class="mvm">Every verdict is model against model.</p>')
    T = [('items', 'Items'), ('graph', 'Whole graph'), ('prov', 'Provenance')]
    P('<div class="tabs" role="tablist" aria-label="views">')
    for i, (k, l) in enumerate(T):
        P(f'<button class="tab" role="tab" id="tab-{k}" aria-controls="panel-{k}" '
          f'aria-selected="{"true" if not i else "false"}" tabindex="{0 if not i else -1}">{E(l)}</button>')
    P('</div>')

    P('<div class="panel" role="tabpanel" id="panel-items" aria-labelledby="tab-items">')
    for it in its:
        k = it['key']; L = k.get('labels') or {}
        hand = k.get('hand_calibrated')
        P('<div class="item">')
        P(f'<div class="sh"><span class="sn">step {it["step"]}'
          + (f'.{it["sub"]}' if it['of'] > 1 else '') + '</span>'
          f'<span class="prop">{E(it["property"])}</span>'
          f'<span class="badge {"hand" if hand else "draft"}">'
          f'{E(hand) if hand else "drafted key"}</span>'
          + ('<span class="badge ni">not identifiable</span>' if k.get('not_identifiable') else '')
          + ('<span class="badge draft">claims pinned</span>' if it.get('claims_pinned') else '')
          + '</div>')
        if it['previous_output']:
            P(f'<p class="qty">takes from step {it["previous_step"]}: {E(it["previous_output"][:180])}</p>')
        q = k.get('quantity') or {}
        if isinstance(q, dict) and q:
            if 'kind' in q: P(f'<p class="qty"><b>quantity</b> &mdash; {E(q.get("kind"))}: {E(str(q.get("what")))}</p>')
            else:
                for side in ('previous', 'this'):
                    v = q.get(side) or {}
                    if v: P(f'<p class="qty"><b>{side}</b> &mdash; {E(str(v.get("kind")))}: {E(str(v.get("what")))}</p>')
        P(f'<div class="lab"><span>dependency <b>{E(str(L.get("dependency")))}</b></span>'
          f'<span>inference <b>{E(str(L.get("inference_validity")))}</b></span>'
          f'<span>causal strength <b>{E(str(L.get("causal_strength")))}</b></span></div>')
        pans = [p for p in it['panels'] if p.get('png')]
        if pans:
            P('<div class="pans">')
            for p in pans:
                src = b64(os.path.join(ROOT, 'results/v5/traces', trace, p['png']))
                P(f'<figure class="pan"><img src="{src}" alt="panel {E(p["suffix"])}">'
                  f'<figcaption class="cap">{E(p["suffix"])}</figcaption></figure>')
            P('</div>')
        if it['withheld_panels']:
            P(f'<p class="qty">withheld from the solver: {E(", ".join(it["withheld_panels"]))}</p>')
        P(f'<div class="key"><h5>key &mdash; what the evidence permits</h5>{E(str(k.get("proposition")))}</div>')
        if k.get('permitted'):
            P(f'<p class="qty"><b>permitted:</b> {E(str(k["permitted"]))}</p>')
        if k.get('not_permitted'):
            P(f'<p class="qty"><b>not permitted:</b> {E(str(k["not_permitted"]))}</p>')
        if k.get('limits'):
            P('<div class="lim"><h5>limits</h5><ul>')
            for l in k['limits']: P(f'<li>{E(str(l))}</li>')
            P('</ul></div>')
        if k.get('not_identifiable'):
            P(f'<div class="ni"><b>not identifiable</b>{E(str(k["not_identifiable"]))}</div>')
        if k.get('handoff'):
            P(f'<p class="qty"><b>handoff:</b> {E(str(k["handoff"]))}</p>')
            for c in (k.get('handoff_caveats') or []):
                P(f'<p class="qty">&mdash; carrying: {E(str(c))}</p>')
        P('</div>')
    P('</div>')

    P('<div class="panel" role="tabpanel" id="panel-graph" aria-labelledby="tab-graph" hidden>')
    P(graph_svg(g, tc, step_of))
    P('</div>')

    P('<div class="panel" role="tabpanel" id="panel-prov" aria-labelledby="tab-prov" hidden>')
    P('<div class="audit"><b>Audit only &mdash; never shown to a solver.</b>'
      '<table><thead><tr><th>item</th><th>hop</th><th>stage type</th><th>figures</th></tr></thead><tbody>')
    for it in its:
        pv = it['provenance_NOT_SOLVER_VISIBLE']
        P(f'<tr><td>{E(it["item"])}</td><td>{E(pv["matmech_hop"])}</td>'
          f'<td>{E(pv["stage_type"])}</td><td>{E(", ".join(pv.get("matmech_figures") or []))}</td></tr>')
    P('</tbody></table></div></div>')
    P(f'</div><script>{JS}</script></body></html>')
    return '\n'.join(A)


def main():
    I = json.load(open(os.path.join(ROOT, 'results/v5/items.json')))['items']
    S = {r['item'] for r in json.load(open(os.path.join(ROOT, 'results/v5/survival.json')))['surviving']}
    by = collections.defaultdict(list)
    for it in I:
        if it['item'] in S: by[it['trace']].append(it)
    out = os.path.join(ROOT, 'results/v5/pages'); os.makedirs(out, exist_ok=True)
    for tr, its in sorted(by.items()):
        t = json.load(open(os.path.join(ROOT, 'results/v4x', tr, 'trace.json')))
        p = os.path.join(out, tr + '.html')
        open(p, 'w').write(build(tr, sorted(its, key=lambda x: (x['step'], x['sub'])), t))
        print(f"  {os.path.basename(p):40s} {len(its)} items  {os.path.getsize(p)//1024} KB")
    print(f"\n{len(by)} pages for {sum(len(v) for v in by.values())} surviving items")


if __name__ == '__main__': main()
