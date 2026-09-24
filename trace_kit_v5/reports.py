"""reports.py: one report per paper, every surviving item with its provenance and its audits.

  python3 trace_kit_v5/reports.py

Each item shows three things the earlier pages did not carry:

  key provenance   hand-written, drafted, or drafted-and-fixed -- and if fixed, the text before the
                   fix beside the text after it, so a rewrite is inspectable rather than silent
  audit verdicts   per statement: holds, overreaches or wrong, with the observation the auditor
                   quoted against it
  quantity kind    same_kind or mixed, naming both quantities

and, where one exists, an audit MISS: something the audit passed that a reader caught.

The audit's reach is stated on every report. A per-statement audit rules whether each stated limit
is TRUE. It never asks whether a needed limit is MISSING, which is why a key can score 47 of 47 on
its limits and still compare charge capacity against discharge capacity.

Every verdict is model against model.
"""
import base64, html, io, json, os, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v4'))
from pages import CSS, JS, b64
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v5'))
from pages import EXTRA
E = html.escape

MORE = """
.prov{font:600 10.5px ui-monospace,Menlo,monospace;padding:2px 8px;border-radius:5px;margin-left:6px}
.prov.hand{background:var(--acc);color:#fff}
.prov.draft{background:var(--chip);color:var(--mut)}
.prov.fixed{background:var(--warn);color:#fff}
.aud{font-size:12.5px;margin:8px 0;border-left:3px solid var(--line);padding:6px 12px}
.aud .v{font:600 11px ui-monospace,Menlo,monospace;padding:1px 6px;border-radius:4px;margin-right:6px}
.v.holds{background:var(--chip);color:var(--acc)}
.v.overreaches{background:var(--warn);color:#fff}
.v.wrong{background:#b3261e;color:#fff}
.v.mixed{background:var(--warn);color:#fff}
.v.same_kind{background:var(--chip);color:var(--acc)}
.was{font-size:12px;color:var(--mut);border-left:2px dashed var(--warn);padding:4px 10px;margin:5px 0}
.miss{border:2px solid #b3261e;border-radius:9px;padding:9px 12px;margin:9px 0;font-size:12.5px}
.miss b{color:#b3261e;font-size:11px;text-transform:uppercase;letter-spacing:.05em;display:block}
.reach{border:1px solid var(--warn);border-radius:10px;padding:12px 14px;margin:0 0 16px;font-size:13px}
.reach b{color:var(--warn)}
"""


def prov_of(it):
    k = it.get('key') or {}
    if k.get('hand_calibrated'): return 'hand', k['hand_calibrated']
    if k.get('proposition_before_audit') or k.get('proposition_before_quantity_fix'):
        return 'fixed', 'drafted, audited and fixed'
    return 'draft', 'drafted key'


def build(paper, its):
    A = []; P = A.append
    short = paper.split('__')[0].replace('_', ' ')
    P('<!doctype html><html lang="en"><meta charset="utf-8">')
    P('<meta name="viewport" content="width=device-width,initial-scale=1">')
    P(f'<title>{E(short)}</title><style>{CSS}{EXTRA}{MORE}</style><body><div class="wrap">')
    P(f'<h1>{E(short)}</h1><p class="sub">{E(paper)} &middot; {len(its)} surviving item'
      f'{"s" if len(its) != 1 else ""}</p>')
    P('<p class="mvm">Every verdict is model against model.</p>')
    P('<div class="reach"><b>What the audit reaches, and what it does not.</b> The per-statement '
      'audit rules whether each <i>stated</i> limit is true. It never asks whether a <i>needed</i> '
      'limit is missing. That is why a key can score 47 of 47 on its limits and still compare '
      'quantities of different kinds, and why the quantity-kind ruling is reported separately '
      'below.</div>')
    for it in its:
        k = it.get('key') or {}
        cls, label = prov_of(it)
        L = k.get('labels') or {}
        P('<div class="item">')
        P(f'<div class="sh"><span class="sn">{E(it["item"])}</span>'
          f'<span class="prop">{E(it["property"][:110])}</span>'
          f'<span class="prov {cls}">{E(label)}</span></div>')
        P(f'<div class="lab"><span>dependency <b>{E(str(L.get("dependency")))}</b></span>'
          f'<span>inference <b>{E(str(L.get("inference_validity")))}</b></span>'
          f'<span>causal strength <b>{E(str(L.get("causal_strength")))}</b></span>'
          f'<span>depth <b>{E(str(it.get("depth")))}</b></span>'
          f'<span>lane <b>{"FM" if it.get("fm_lane") else "other"}</b></span></div>')
        q = it.get('quantity_kind')
        if q:
            P(f'<div class="aud"><span class="v {E(q["ruling"])}">{E(q["ruling"])}</span>'
              f'{E(str(q.get("a")))} <i>({E(str(q.get("kind_a")))})</i> against '
              f'{E(str(q.get("b")))} <i>({E(str(q.get("kind_b")))})</i>'
              + ('' if q['ruling'] == 'same_kind' else
                 f' &mdash; same-kind pair available: '
                 f'{"yes" if q.get("same_kind_pair_available") else "no"}')
              + '</div>')
        P(f'<div class="key"><h5>key</h5>{E(str(k.get("proposition")))}</div>')
        for f in ('proposition_before_audit', 'proposition_before_quantity_fix'):
            if k.get(f):
                P(f'<div class="was"><b>before {"the audit" if "audit" in f else "the quantity-kind fix"}:</b> '
                  f'{E(str(k[f])[:420])}</div>')
        if k.get('limits'):
            P('<div class="lim"><h5>limits</h5><ul>')
            for l in k['limits']: P(f'<li>{E(str(l))}</li>')
            P('</ul></div>')
        if k.get('not_identifiable'):
            P(f'<div class="ni"><b>not identifiable</b>{E(str(k["not_identifiable"]))}</div>')
        sc = k.get('scoring') or {}
        if sc:
            P(f'<p class="qty"><b>scoring target:</b> {E(str(sc.get("target")))} &mdash; '
              f'{sc.get("n_required")} required elements. {E(str(sc.get("insufficient_alone")))}</p>')
        a = it.get('audit') or {}
        if a.get('statements'):
            P('<div class="aud"><b>audit</b><ul>')
            for s in a['statements']:
                v = s.get('verdict') or 'unruled'
                P(f'<li><span class="v {E(v)}">{E(v)}</span>{E(str(s.get("what")))}'
                  + (f' &mdash; {E(str(s.get("evidence"))[:220])}' if s.get('evidence') else '')
                  + '</li>')
            P('</ul></div>')
        for m in (a.get('misses') or []):
            P(f'<div class="miss"><b>audit miss &mdash; found by {E(str(m.get("found_by")))}</b>'
              f'{E(str(m.get("what")))}<br><i>{E(str(m.get("why_it_matters")))}</i></div>')
        P('</div>')
    P('</div></body></html>')
    return '\n'.join(A)


def main():
    I = {i['item']: i for i in json.load(open(os.path.join(ROOT, 'results/v5/items.json')))['items']}
    S = [r['item'] for r in json.load(open(os.path.join(ROOT, 'results/v5/survival_v5b.json')))['surviving']]
    by = collections.defaultdict(list)
    for s in S: by[I[s]['paper']].append(I[s])
    out = os.path.join(ROOT, 'results/v5/reports'); os.makedirs(out, exist_ok=True)
    for p, its in sorted(by.items()):
        its.sort(key=lambda x: (x['trace'], x['step'], x['sub']))
        f = os.path.join(out, p + '.html')
        open(f, 'w').write(build(p, its))
    print(f"{len(by)} per-paper reports for {len(S)} items -> results/v5/reports/")
    pr = collections.Counter(prov_of(I[s])[0] for s in S)
    print(f"key provenance across survivors: {dict(pr)}")


if __name__ == '__main__': main()
