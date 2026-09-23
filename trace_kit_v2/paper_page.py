"""paper_page.py: one self-contained HTML page with every support chain of one paper.

  python3 trace_kit_v2/paper_page.py <paper> [out.html]

Panels are embedded as base64 so the file stands alone. They are downscaled for the page only;
the measurements were made on the native crops in results/v2/paper/<paper>/<claim>/images/.
"""
import base64, glob, html, io, json, os, sys, collections
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MAXW = 760
E = lambda s: html.escape(str(s if s is not None else ''))
LEVEL = {'shown': 'lv-shown', 'partial': 'lv-partial', 'contradicts': 'lv-contra', 'not addressed': 'lv-na'}

_cache = {}
def b64(path):
    if path in _cache: return _cache[path]
    im = Image.open(path).convert('RGB')
    if im.size[0] > MAXW: im = im.resize((MAXW, round(im.size[1] * MAXW / im.size[0])), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=82, optimize=True)
    _cache[path] = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
    return _cache[path]


def necessity_map():
    """measured necessity, keyed by (paper, claim). Empty for chains never measured."""
    out = {}
    for f in glob.glob(os.path.join(ROOT, 'results/v2/necessity/case*.json')):
        o = json.load(open(f)); out[(o['paper'], o['claim'])] = o
    return out


def main(paper, out=None):
    NEC = necessity_map()
    base = os.path.join(ROOT, 'results/v2/paper', paper)
    chains = []
    for f in sorted(glob.glob(os.path.join(base, '*', 'case.json'))):
        ch = json.load(open(f)); ch['_dir'] = os.path.dirname(f); chains.append(ch)
    chains.sort(key=lambda c: (not c.get('spine'), -c['n_steps']))
    title = chains[0].get('claim_text', '')[:0] or paper
    g = json.load(open(os.path.join(ROOT, chains[0]['graph'])))
    paper_title = g.get('title') or paper
    doi = next((p['panel_id'].split('#')[0] for c in chains for s in c['steps'] for p in s['panels']), '')
    allch = sorted({x for c in chains for x in c['channels']})
    npanels = len({p['suffix'] for c in chains for s in c['steps'] for p in s['panels'] if p.get('png')})
    steps_total = sum(c['n_steps'] for c in chains)

    P = []
    A = P.append
    A(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(paper_title)} — support chains</title><style>
:root{{color-scheme:light;--ink:#1c2430;--mut:#66727f;--line:#dde3ea;--bg:#f7f8fa;--card:#fff;
--sh:#e8f0f7;--sh-i:#1f6e9e;--pa:#fdf3e3;--pa-i:#c08a2e;--co:#fbeae8;--co-i:#b9312c;--na:#eef0f2;--na-i:#8a8f98;--ok:#e7f3ec;--ok-i:#2f8f5b}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{color-scheme:dark;--ink:#e6ebf1;--mut:#9aa6b4;--line:#2b3440;--bg:#12171d;--card:#1a2129;
--sh:#12303f;--sh-i:#4aa3d4;--pa:#3a2f16;--pa-i:#d8a33f;--co:#3b1f1e;--co-i:#e0716b;--na:#232a32;--na-i:#8a95a2;--ok:#16301f;--ok-i:#54b47c}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:1080px;margin:0 auto;padding:28px 18px 80px}}
h1{{font-size:24px;line-height:1.25;margin:0 0 6px}}
.sub{{color:var(--mut);font-size:13px;margin-bottom:20px}}
.stats{{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 26px}}
.stat{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;min-width:96px}}
.stat b{{display:block;font-size:20px;line-height:1.2}}
.stat span{{color:var(--mut);font-size:11px;text-transform:uppercase;letter-spacing:.04em}}
.hint{{color:var(--mut);font-size:12px;margin:0 0 8px}}
.note{{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--na-i);
border-radius:8px;padding:12px 14px;color:var(--mut);font-size:13px;margin-bottom:26px}}
.tabs{{display:flex;gap:6px;overflow-x:auto;padding:4px 0 10px;margin-bottom:-1px;scrollbar-width:thin;-webkit-overflow-scrolling:touch}}
.tab{{flex:0 0 auto;background:transparent;border:1px solid var(--line);border-radius:9px 9px 0 0;
padding:9px 13px;cursor:pointer;color:var(--mut);font:inherit;font-size:13px;line-height:1.25;text-align:left;white-space:nowrap}}
.tab:hover{{color:var(--ink)}}
.tab[aria-selected=true]{{background:var(--card);color:var(--ink);border-bottom-color:var(--card);font-weight:600}}
.tab .tn{{font:600 12px ui-monospace,SFMono-Regular,Menlo,monospace;display:block}}
.tab .tm{{font-size:11px;opacity:.75}}
.tab:focus-visible{{outline:2px solid var(--sh-i);outline-offset:2px}}
.chain{{background:var(--card);border:1px solid var(--line);border-radius:0 12px 12px 12px;padding:18px;margin-bottom:20px}}
.chain[hidden]{{display:none!important}}
.chead{{display:flex;flex-wrap:wrap;gap:8px;align-items:baseline;margin-bottom:6px}}
.cid{{font:600 12px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--mut)}}
.badge{{font-size:11px;padding:2px 8px;border-radius:99px;border:1px solid var(--line);color:var(--mut)}}
.badge.spine{{background:var(--ok);border-color:var(--ok-i);color:var(--ok-i)}}
.claim{{font-size:16px;font-weight:600;margin:2px 0 10px}}
.meta{{color:var(--mut);font-size:12px;margin-bottom:14px}}
.step{{border-top:1px solid var(--line);padding:14px 0 4px}}
.srow{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:6px}}
.sn{{font:600 12px ui-monospace,monospace;background:var(--na);color:var(--na-i);border-radius:6px;padding:2px 7px}}
.lv{{font-size:11px;font-weight:600;padding:2px 9px;border-radius:99px;text-transform:uppercase;letter-spacing:.03em}}
.lv-shown{{background:var(--sh);color:var(--sh-i)}}.lv-partial{{background:var(--pa);color:var(--pa-i)}}
.lv-contra{{background:var(--co);color:var(--co-i)}}.lv-na{{background:var(--na);color:var(--na-i)}}
.tech{{font:12px ui-monospace,monospace;color:var(--mut)}}
.obs{{font-size:14px;margin:4px 0 10px}}
.pans{{display:flex;flex-wrap:wrap;gap:10px}}
figure{{margin:0;max-width:240px}}
figure img{{width:100%;height:auto;border:1px solid var(--line);border-radius:8px;display:block;background:#fff;cursor:zoom-in}}
figcaption{{font:11px ui-monospace,monospace;color:var(--mut);margin-top:4px}}
.oracle{{background:var(--pa);border-left:3px solid var(--pa-i);border-radius:8px;padding:10px 12px;font-size:13px}}
.close{{border-top:1px solid var(--line);margin-top:12px;padding-top:12px;font-size:13px;color:var(--mut)}}
.close b{{color:var(--ink)}}
.drop{{background:var(--co);border-left:3px solid var(--co-i);border-radius:8px;padding:9px 12px;font-size:12.5px;margin-top:10px}}
.nec{{border-top:1px solid var(--line);margin-top:14px;padding-top:12px}}
.nec h4{{margin:0 0 4px;font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}}
.nec .lead{{font-size:13px;margin-bottom:8px}}
.nec table{{width:100%;border-collapse:collapse;font-size:12.5px}}
.nec th{{text-align:left;color:var(--mut);font-size:10.5px;text-transform:uppercase;letter-spacing:.03em;padding:4px 6px;border-bottom:1px solid var(--line)}}
.nec td{{padding:5px 6px;border-bottom:1px solid var(--line)}}
.nec td.n{{text-align:right;font:12px ui-monospace,Menlo,monospace}}
.yes{{color:var(--ok-i);font-weight:600}}.no{{color:var(--mut)}}
.measured{{background:var(--ok);border-color:var(--ok-i);color:var(--ok-i)}}
dialog{{border:0;background:transparent;max-width:96vw;max-height:96vh;padding:0}}
dialog::backdrop{{background:rgba(0,0,0,.82)}}
dialog img{{max-width:96vw;max-height:92vh;border-radius:10px;display:block}}
dialog p{{color:#fff;font:12px ui-monospace,monospace;text-align:center;margin:8px 0 0}}
@media (max-width:640px){{figure{{max-width:46%}}.wrap{{padding:20px 14px 60px}}
.chain{{border-radius:12px}}.tabs{{padding-bottom:8px}}.tab{{border-radius:9px}}}}
</style></head><body><div class="wrap">""")
    A(f"<h1>{E(paper_title)}</h1>")
    A(f'<div class="sub">{E(paper.split("__")[0].replace("_"," "))} &middot; {E(doi)} &middot; support chains, every claim with two or more figure-backed evidence nodes</div>')
    A('<div class="stats">')
    for v, k in ((len(chains), 'chains'), (steps_total, 'steps'), (npanels, 'panels'), (len(allch), 'channels')):
        A(f'<div class="stat"><b>{v}</b><span>{k}</span></div>')
    A('</div>')
    A('<div class="note"><b>Every verdict is model against model.</b> Each chain is cut from the paper\'s '
      'argument graph; the level on each step is the graph\'s own four-level support label, and the closing '
      'line is the claim\'s support profile. Panels are handed over whole and unaltered &mdash; annotation '
      'removal was withdrawn on 2026-09-23. Images here are downscaled for the page; the measurements were '
      'made on the native crops. No item on this page has been checked by a person.</div>')

    A('<p class="hint">One tab per chain. Arrow keys move between them, and each tab has its own link.</p>')
    A('<div class="tabs" role="tablist" aria-label="Support chains">')
    for i, c in enumerate(chains):
        sel = 'true' if i == 0 else 'false'
        A(f'<button class="tab" role="tab" id="tab-{E(c["claim"])}" aria-controls="panel-{E(c["claim"])}" '
          f'aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">'
          f'<span class="tn">{E(c["claim"])}</span>'
          f'<span class="tm">{c["n_steps"]} steps &middot; {E(", ".join(c["channels"])[:26])}</span></button>')
    A('</div>')

    for i, c in enumerate(chains):
        A(f'<div class="chain" role="tabpanel" id="panel-{E(c["claim"])}" '
          f'aria-labelledby="tab-{E(c["claim"])}" tabindex="0"{"" if i == 0 else " hidden"}>')
        A('<div class="chead">')
        A(f'<span class="cid">{E(c["claim"])}</span>')
        if c.get('spine'): A('<span class="badge spine">spine</span>')
        nec = NEC.get((paper, c['claim']))
        if nec: A('<span class="badge measured">necessity measured</span>')
        A(f'<span class="badge">{E(c.get("claim_type"))}</span>')
        A(f'<span class="badge">{c["n_steps"]} steps</span>')
        A(f'<span class="badge">{E(", ".join(c["channels"]))}</span>')
        A('</div>')
        A(f'<div class="claim">{E(c["claim_text"])}</div>')
        lanes = c['lanes']; tests = c['tests']
        A(f'<div class="meta">{lanes["fm"]} instrument step{"s" if lanes["fm"]!=1 else ""}, '
          f'{lanes["oracle"]} served as text &middot; perception {tests["perception"]}, '
          f'selection {tests["selection"]}, integration {tests["integration"]}</div>')
        for s in c['steps']:
            A('<div class="step"><div class="srow">')
            A(f'<span class="sn">{s["step"]}</span>')
            A(f'<span class="lv {LEVEL.get(s["expected_support"],"lv-na")}">{E(s["expected_support"])}</span>')
            A(f'<span class="tech">{E(s["technique"])}</span>')
            A(f'<span class="tech">&middot; {E(s["relation"])} &middot; {E(s["tests"])}</span>')
            A('</div>')
            A(f'<div class="obs">{E(s["observation"])}</div>')
            if s['delivery'] == 'oracle':
                A(f'<div class="oracle"><b>Served as a plain-text tool result</b> &mdash; {E(s["family"])} has no model or simulator.</div>')
            else:
                A('<div class="pans">')
                for p in s['panels']:
                    if not p.get('png'): continue
                    src = b64(os.path.join(c['_dir'], p['png']))
                    cap = E((p.get('caption_span') or '')[:90])
                    A(f'<figure><img src="{src}" alt="panel {E(p["suffix"])}" loading="lazy" '
                      f'data-suffix="{E(p["suffix"])}"><figcaption>{E(p["suffix"])} &middot; '
                      f'{p.get("width")}&times;{p.get("height")}</figcaption></figure>')
                A('</div>')
            A('</div>')          # close .step -- without this every step nests inside the last
        if c['dropped_panels']:
            for d in c['dropped_panels']:
                A(f'<div class="drop"><b>Panel dropped:</b> {E(d["node"])} &mdash; {E(d["reason"])}</div>')
        if nec:
            A('<div class="nec"><h4>Measured necessity, by removal</h4>')
            A(f'<div class="lead">With every panel: <b>{E(nec["full_verdict"])}</b> '
              f'({nec["full_confidence"]}). With none: <b>{E(nec["confidence_floor"]["verdict"])}</b> '
              f'({nec["confidence_floor"]["confidence"]}). '
              f'Answered by <code>net-claim</code> (sonnet) from panels alone, {nec["repeats"]} repeats, '
              f'threshold drop &gt; {nec["threshold"]}.</div>')
            A('<table><thead><tr><th>remove</th><th>verdict without it</th><th class="n">drop</th>'
              '<th class="n">rank</th><th>necessary</th></tr></thead><tbody>')
            for r in sorted(nec['channels'], key=lambda x: (x['drop'] is None, -(x['drop'] or 0))):
                tag = f'channel {E(r["channel"])} ({r["n_panels"]})'
                A(f'<tr><td>{tag}</td><td>{E(r["verdict_without"])}</td><td class="n">{r["drop"]}</td>'
                  f'<td class="n">{r.get("rank","-")}{" tie" if r.get("tied") else ""}</td>'
                  f'<td class="{"yes" if r["necessary"] else "no"}">{"yes" if r["necessary"] else "no"}</td></tr>')
            for r in sorted(nec['panels'], key=lambda x: (x['drop'] is None, -(x['drop'] or 0))):
                A(f'<tr><td>panel {E(r["panel"])}</td><td>{E(r["verdict_without"])}</td>'
                  f'<td class="n">{r["drop"]}</td><td class="n">{r.get("rank","-")}{" tie" if r.get("tied") else ""}</td>'
                  f'<td class="{"yes" if r["necessary"] else "no"}">{"yes" if r["necessary"] else "no"}</td></tr>')
            A('</tbody></table>')
            A(f'<div class="lead" style="margin-top:8px">Split: <b>{E(nec["split"])}</b> at panel level, '
              f'<b>{E(nec["channel_split"])}</b> at channel level. Necessity is relative to this answerer, '
              f'this prompt and this model.</div></div>')
        A(f'<div class="close"><b>Closing: {E(c["closing_support"])}</b>')
        if c.get('closing_why'): A(f' &mdash; {E(c["closing_why"])}')
        if c['closing_missing']:
            A('<br>Not carried by any panel: ' + E('; '.join(c['closing_missing'])[:400]))
        A('</div></div>')
    A('</div><dialog id="zoom"><img><p></p></dialog><script>')
    A("""const tabs=[...document.querySelectorAll('[role=tab]')];
const panels=[...document.querySelectorAll('[role=tabpanel]')];
function show(id,push){
  tabs.forEach(t=>{const on=t.id==='tab-'+id;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;});
  panels.forEach(p=>{p.hidden=p.id!=='panel-'+id;});
  if(push&&history.replaceState)history.replaceState(null,'','#'+id);
}
tabs.forEach(t=>t.addEventListener('click',()=>show(t.id.slice(4),true)));
document.querySelector('[role=tablist]').addEventListener('keydown',e=>{
  const i=tabs.findIndex(t=>t.getAttribute('aria-selected')==='true');
  let n=null;
  if(e.key==='ArrowRight')n=(i+1)%tabs.length;
  else if(e.key==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;
  else if(e.key==='Home')n=0;
  else if(e.key==='End')n=tabs.length-1;
  if(n===null)return;
  e.preventDefault();show(tabs[n].id.slice(4),true);tabs[n].focus();
});
function fromHash(){const k=decodeURIComponent(location.hash.slice(1));
  if(k&&document.getElementById('panel-'+k))show(k,false);}
fromHash();addEventListener('hashchange',fromHash);
const dlg=document.getElementById('zoom');
document.querySelectorAll('figure img').forEach(i=>i.addEventListener('click',()=>{
  dlg.querySelector('img').src=i.src;dlg.querySelector('p').textContent=i.dataset.suffix;dlg.showModal();}));
dlg.addEventListener('click',()=>dlg.close());
addEventListener('keydown',e=>{if(e.key==='Escape'&&dlg.open)dlg.close();});""")
    A('</script></body></html>')
    out = out or os.path.join(ROOT, 'site', f'{paper}_chains.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write('\n'.join(P))
    print(f"{len(chains)} chains, {steps_total} steps, {npanels} panels -> {os.path.relpath(out, ROOT)} "
          f"({os.path.getsize(out)/1e6:.1f} MB, self-contained)")


if __name__ == '__main__': main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
