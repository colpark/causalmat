"""all_paper_pages.py: one self-contained page per paper, plus an index.

  python3 trace_kit_v2/all_paper_pages.py [--out export/v2_pages] [--limit N]

Pages go to export/ rather than site/ because they embed publisher figures and total well over a
hundred megabytes; site/ is tracked. The generator is tracked, the output is not.
"""
import argparse, collections, html, json, os, sys, time, traceback
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paper_chains, paper_page
E = lambda s: html.escape(str(s if s is not None else ''))


def main(a):
    cands = json.load(open(os.path.join(ROOT, 'results/v2/candidates.json')))
    papers = sorted({c['paper'] for c in cands})
    if a.limit: papers = papers[:a.limit]
    out = os.path.join(ROOT, a.out); os.makedirs(out, exist_ok=True)
    paper_page.MAXW = a.width
    rows, t0 = [], time.time()
    for i, p in enumerate(papers, 1):
        try:
            import io, contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf): paper_chains.main(p)
            dst = os.path.join(out, p + '.html')
            with contextlib.redirect_stdout(buf): paper_page.main(p, dst)
            import glob
            chains = [json.load(open(f)) for f in glob.glob(os.path.join(ROOT, 'results/v2/paper', p, '*', 'case.json'))]
            rows.append({'paper': p, 'file': p + '.html', 'chains': len(chains),
                         'steps': sum(c['n_steps'] for c in chains),
                         'panels': len({q['suffix'] for c in chains for s in c['steps'] for q in s['panels'] if q.get('png')}),
                         'channels': sorted({x for c in chains for x in c['channels']}),
                         'title': (chains[0].get('claim_text') and json.load(open(os.path.join(ROOT, chains[0]['graph']))).get('title')) or p,
                         'bytes': os.path.getsize(dst)})
            paper_page._cache.clear()
        except Exception as e:
            rows.append({'paper': p, 'error': f"{type(e).__name__}: {e}"})
        if i % 10 == 0 or i == len(papers):
            ok = sum(1 for r in rows if 'error' not in r)
            print(f"  {i}/{len(papers)}  {ok} built, {time.time()-t0:.0f}s", flush=True)
    ok = [r for r in rows if 'error' not in r]
    tot = sum(r['bytes'] for r in ok)
    # index
    H = [f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>causalmat support chains — {len(ok)} papers</title><style>
:root{{color-scheme:light;--ink:#1c2430;--mut:#66727f;--line:#dde3ea;--bg:#f7f8fa;--card:#fff;--ac:#1f6e9e}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{color-scheme:dark;--ink:#e6ebf1;--mut:#9aa6b4;--line:#2b3440;--bg:#12171d;--card:#1a2129;--ac:#4aa3d4}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:1040px;margin:0 auto;padding:28px 18px 80px}}
h1{{font-size:24px;margin:0 0 6px}}.sub{{color:var(--mut);font-size:13px;margin-bottom:18px}}
.stats{{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:20px}}
.stat{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;min-width:92px}}
.stat b{{display:block;font-size:20px}}.stat span{{color:var(--mut);font-size:11px;text-transform:uppercase;letter-spacing:.04em}}
input{{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:9px;background:var(--card);color:var(--ink);font:inherit;margin-bottom:14px}}
table{{width:100%;border-collapse:collapse;font-size:13.5px}}
th{{text-align:left;color:var(--mut);font-size:11px;text-transform:uppercase;letter-spacing:.04em;padding:6px 8px;border-bottom:1px solid var(--line)}}
td{{padding:8px;border-bottom:1px solid var(--line);vertical-align:top}}
td.n{{text-align:right;font:12px ui-monospace,Menlo,monospace;color:var(--mut);white-space:nowrap}}
a{{color:var(--ac);text-decoration:none}}a:hover{{text-decoration:underline}}
.j{{color:var(--mut);font-size:11.5px}}.ch{{color:var(--mut);font:11px ui-monospace,monospace}}
.note{{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--mut);border-radius:8px;padding:12px 14px;color:var(--mut);font-size:13px;margin-bottom:20px}}
</style></head><body><div class="wrap">
<h1>Support chains</h1>
<div class="sub">Every claim in the corpus carrying two or more figure-backed evidence nodes, one page per paper, one tab per chain.</div>
<div class="stats">
<div class="stat"><b>{len(ok)}</b><span>papers</span></div>
<div class="stat"><b>{sum(r['chains'] for r in ok)}</b><span>chains</span></div>
<div class="stat"><b>{sum(r['steps'] for r in ok)}</b><span>steps</span></div>
<div class="stat"><b>{sum(r['panels'] for r in ok)}</b><span>panels</span></div>
</div>
<div class="note"><b>Every verdict is model against model.</b> Each chain is cut from the paper's argument graph;
the level on each step is the graph's own four-level support label. Panels are handed over whole and unaltered.
Nothing here has been checked by a person.</div>
<input id="q" placeholder="filter by paper, journal or technique" autocomplete="off">
<table><thead><tr><th>paper</th><th>channels</th><th class="n">chains</th><th class="n">steps</th><th class="n">panels</th></tr></thead><tbody id="tb">"""]
    for r in sorted(ok, key=lambda x: -x['chains']):
        j = r['paper'].split('__')[0].replace('_', ' ')
        H.append(f'<tr data-k="{E((r["paper"]+" "+j+" "+" ".join(r["channels"])).lower())}">'
                 f'<td><a href="{E(r["file"])}">{E(r["title"][:96])}</a><div class="j">{E(j)}</div></td>'
                 f'<td class="ch">{E(", ".join(r["channels"]))}</td>'
                 f'<td class="n">{r["chains"]}</td><td class="n">{r["steps"]}</td><td class="n">{r["panels"]}</td></tr>')
    H.append("""</tbody></table></div><script>
const q=document.getElementById('q'),rows=[...document.querySelectorAll('#tb tr')];
q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();
rows.forEach(r=>r.hidden=v&&!r.dataset.k.includes(v));});
</script></body></html>""")
    open(os.path.join(out, 'index.html'), 'w').write('\n'.join(H))
    json.dump({'papers': len(ok), 'chains': sum(r['chains'] for r in ok),
               'steps': sum(r['steps'] for r in ok), 'bytes': tot,
               'errors': [r for r in rows if 'error' in r],
               'note': 'Every verdict is model against model.'},
              open(os.path.join(out, 'index.json'), 'w'), indent=1)
    print(f"\n{len(ok)} pages, {sum(r['chains'] for r in ok)} chains, {sum(r['steps'] for r in ok)} steps, "
          f"{tot/1e6:.0f} MB -> {a.out}/index.html")
    for r in rows:
        if 'error' in r: print('  ERROR', r['paper'][:50], r['error'][:80])


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='export/v2_pages')
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--width', type=int, default=640)
    main(ap.parse_args())
