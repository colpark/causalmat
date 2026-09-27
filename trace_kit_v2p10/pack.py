"""pack.py: everything v2.10 produced, in one zip you can copy and open offline.

  python3 trace_kit_v2p10/pack.py

No model call. The zip carries a README.html that links the rest, so opening the zip and
double-clicking one file is enough; every page inside is self-contained and fetches nothing.
"""
import collections, html, json, os, sys, zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
E = html.escape
OUT = R('results/v2p10/v2p10_outputs.zip')

PARTS = [
    # (folder in the zip, source dir, glob suffix, what it is)
    ('reports', 'results/v2p10/reports', '.html',
     "the full reasoning story per paper: the paper's argument graph, every chain from depth 2 "
     "to 5, and under each step the figure panel it read, boxed on its own figure, with the "
     "caption and the paper's sentences about it"),
    ('pages', 'results/v2p10/pages', '.html',
     'the compact chain pages: each chain link by link with the four arm scores that decided it'),
]
DOCS = ['TRACES_V2P10_REPORTS.md', 'TRACES_V2P10.md', 'TRACES_V2P9.md', 'TRACES_V2P8B_CONTROL.md',
        'TRACES_V2P8_PILOT.md', 'TRACES_V2P7.md', 'TRACES_V2P6.md', 'TRACES_V2P5.md']
DATA = ['report_chains.json', 'report_data.json', 'report_build.json', 'report_verify.json',
        'report_meta.json', 'reports_cost.json', 'cost.json', 'pages_report.json',
        'purge.json', 'deeper_d4.json', 'deeper_d5.json', 'keys_d4.json', 'keys_d5.json',
        'step2_d4.json', 'step2_d5.json', 'step4_d4.json', 'step4_d5.json']
V9 = ['nextlink.json', 'pairs.json', 'keys.json', 'keys_nl.json', 'step2.json', 'step2_nl.json',
      'step4.json', 'step4_nl.json', 'decide.json', 'decide_nl.json']

CSS = """body{max-width:820px;margin:0 auto;padding:28px 18px 70px;background:#f6f7f5;color:#15171c;
font:15.5px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
h1{font-size:25px;margin:0 0 4px}h2{font-size:17px;margin:30px 0 8px;padding-bottom:6px;
border-bottom:2px solid #e0e3e7}
a{color:#2f6f4f}code{font:12.5px ui-monospace,Menlo,monospace;background:#eceff4;padding:1px 5px;
border-radius:4px}
.sub{color:#5c636f;font-size:13px}
.banner{background:#11342a;color:#eaf5ef;border-radius:12px;padding:13px 17px;font-size:13.5px;
margin:16px 0}
ul{padding-left:20px}li{margin:6px 0}
table{border-collapse:collapse;width:100%;font-size:13.5px;margin:10px 0}
th,td{border:1px solid #e0e3e7;padding:6px 9px;text-align:left}th{background:#eceff4;font-size:12px;
text-transform:uppercase;letter-spacing:.04em}td.n,th.n{text-align:right}"""


def readme(have):
    ch = json.load(open(R('results/v2p10/report_chains.json')))
    L = [f'<!doctype html><html lang="en"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>v2.10 outputs</title><style>{CSS}</style></head><body>',
         '<h1>v2.10 &mdash; the reasoning chains</h1>',
         f'<p class="sub">{ch["chains"]} chains across {ch["papers"]} papers: '
         + ', '.join(f'{n} at depth {k}' for k, n in sorted(ch['by_depth'].items(),
                                                            key=lambda x: int(x[0]))) + '.</p>',
         '<div class="banner">A chain passes only when a model given the new measurement '
         '<i>and</i> the previous step\'s result scores at least 0.25 above the same model given '
         'either one alone, and above a model given the paper\'s name only. '
         '<b>Every verdict is model against model.</b> No step of this was reviewed by a person.'
         '</div>',
         '<p>Everything here is offline. Every page is self-contained &mdash; images are embedded, '
         'nothing is fetched from the network &mdash; so it opens from the unzipped folder with no '
         'server and no internet.</p>']
    for folder, src, _, what in PARTS:
        if folder not in have: continue
        L += [f'<h2>{E(folder)}/</h2>', f'<p>{what}.</p>',
              f'<p><b><a href="{folder}/index.html">open {folder}/index.html</a></b> '
              f'<span class="sub">&middot; {have[folder]} pages</span></p>']
    if 'reports' not in have:
        L += ['<h2>reports/</h2>', '<p class="sub">Not in this copy: the per-paper reports were '
              'still being generated when this zip was written.</p>']
    L += ['<h2>docs/</h2>', '<p>The write-up for each version: what was run, what it cost, and '
          'what the numbers were. Every number in them is generated from the JSON.</p><ul>']
    for d in DOCS:
        if os.path.exists(R('docs', d)): L.append(f'<li><code>docs/{E(d)}</code></li>')
    L += ['</ul>', '<h2>data/</h2>',
          '<p>The records the pages are built from: the chains and their steps, the answer keys '
          'and their qualifications, the four arm scores per item, and the decisions. '
          '<code>data/v2p10/</code> is this version, <code>data/v2p9/</code> the depth-2 and '
          'depth-3 items it builds on.</p>',
          '</body></html>']
    return '\n'.join(L)


def main():
    have, n = {}, 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for folder, src, suf, _ in PARTS:
            p = R(src)
            if not os.path.isdir(p): continue
            fs = sorted(f for f in os.listdir(p) if f.endswith(suf))
            if not fs: continue
            have[folder] = len(fs)
            for f in fs:
                z.write(os.path.join(p, f), f'v2p10_outputs/{folder}/{f}'); n += 1
        for d in DOCS:
            if os.path.exists(R('docs', d)):
                z.write(R('docs', d), f'v2p10_outputs/docs/{d}'); n += 1
        for f in DATA:
            if os.path.exists(R('results/v2p10', f)):
                z.write(R('results/v2p10', f), f'v2p10_outputs/data/v2p10/{f}'); n += 1
        for f in V9:
            if os.path.exists(R('results/v2p9', f)):
                z.write(R('results/v2p9', f), f'v2p10_outputs/data/v2p9/{f}'); n += 1
        z.writestr('v2p10_outputs/README.html', readme(have)); n += 1
    mb = os.path.getsize(OUT) / 1e6
    print(f'{OUT}\n{n} files, {mb:.1f} MB')
    for k, v in have.items(): print(f'  {k}/: {v} pages')
    if 'reports' not in have:
        print('  reports/: NOT YET BUILT -- rerun after reports.py build')
    return OUT


if __name__ == '__main__':
    main()
