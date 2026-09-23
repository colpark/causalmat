"""export_panels.py: the five v2 cases' panels, whole and unaltered, for the pages.

  python3 trace_kit_v2/export_panels.py

Every cited panel is exported exactly as the answerer received it: the native crop, PNG, no resizing,
no masking. There is no layer/ directory -- annotation handling was withdrawn on 2026-09-23.
"""
import json, os, re, glob, hashlib, sys
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'export/v2_panels')


def main():
    if os.path.isdir(OUT):
        import shutil; shutil.rmtree(OUT)
    rows, unresolved = [], []
    sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
    from cut_traces import store_for, panel_record
    for f in sorted(glob.glob(os.path.join(ROOT, 'results/v2/cases/*/*/case.json'))):
        ch = json.load(open(f)); cd = os.path.dirname(f)
        d = os.path.join(OUT, ch['case'])
        os.makedirs(os.path.join(d, 'panels'), exist_ok=True)
        os.makedirs(os.path.join(d, 'figures'), exist_ok=True)
        figs = set(); seen = set()
        for step in ch['steps']:
            for p in step['panels']:
                if p['suffix'] in seen: continue
                seen.add(p['suffix'])
                src = os.path.join(cd, p['png']) if p.get('png') else None
                if not src or not os.path.exists(src):
                    unresolved.append({'case': ch['case'], 'panel': p['suffix'],
                                       'why': 'no crop resolves for this panel id'}); continue
                dst = os.path.join(d, 'panels', p['suffix'] + '.png')
                im = Image.open(src); im.save(dst)
                fig = p.get('figure'); frel = None
                if fig and os.path.exists(fig):
                    m = re.match(r'F(\d+)', p['suffix']); fn = f"fig{m.group(1)}.png" if m else 'fig.png'
                    fo = os.path.join(d, 'figures', fn)
                    if fn not in figs: Image.open(fig).convert('RGB').save(fo); figs.add(fn)
                    frel = os.path.relpath(fo, OUT)
                rows.append({'case': ch['case'], 'paper': ch['paper'], 'claim': ch['claim'],
                             'panel_id': p['panel_id'], 'suffix': p['suffix'], 'step': step['step'],
                             'technique': step['technique'], 'delivery': step['delivery'],
                             'file': os.path.relpath(dst, OUT), 'width': im.size[0], 'height': im.size[1],
                             'figure': frel, 'resolved': True,
                             'sha256_16': hashlib.sha256(open(dst, 'rb').read()).hexdigest()[:16]})
        for dp in ch.get('dropped_panels') or []:
            st = store_for(os.path.join(ROOT, ch['graph']))
            # a dropped node may cite a whole figure via figs with no panel_ids at all, which is
            # exactly why nothing could be handed over. Resolve the figure so the drop is showable.
            g = json.load(open(os.path.join(ROOT, ch['graph'])))
            node = {n['id']: n for n in g['nodes']}.get(dp['node'], {})
            pids = list(dp.get('panel_ids') or []) or [f"{ch['claim_text'] and ''}{fg}" for fg in (node.get('figs') or [])]
            doi = next((x['panel_id'].split('#')[0] for st_ in ch['steps'] for x in st_['panels']), None)
            pids = [p if '#' in str(p) else f"{doi}#{p}" for p in pids]
            for pid in pids:
                r = panel_record(st, pid) or {}
                fg = r.get('figure')
                if fg and os.path.exists(fg):
                    m = re.search(r'#F(\d+)', pid); fn = f"dropped_fig{m.group(1)}.png" if m else 'dropped.png'
                    fo = os.path.join(d, 'figures', fn); Image.open(fg).convert('RGB').save(fo)
                    rows.append({'case': ch['case'], 'paper': ch['paper'], 'claim': ch['claim'],
                                 'panel_id': pid, 'suffix': pid.split('#')[1], 'step': None,
                                 'technique': dp.get('technique'), 'delivery': None, 'file': None,
                                 'width': None, 'height': None, 'figure': os.path.relpath(fo, OUT),
                                 'resolved': False, 'note': 'dropped from the chain: ' + dp['reason']})
    json.dump({'date': '2026-09-23', 'panels': sum(1 for r in rows if r['resolved']),
               'note': 'Every panel is the native crop, whole and unaltered. Annotation handling was '
                       'withdrawn on 2026-09-23; there is no layer directory and nothing is masked. '
                       'Every verdict is model against model.',
               'unresolved': unresolved, 'rows': rows},
              open(os.path.join(OUT, 'manifest_resolved.json'), 'w'), indent=1)
    import collections
    ok = [r for r in rows if r['resolved']]
    print(f"{len(ok)} panels exported whole, {len(unresolved)} unresolved")
    print('by case:', dict(collections.Counter(r['case'] for r in ok)))
    small = [r for r in ok if r['width'] <= 80 or r['height'] <= 80]
    print('PNGs <= 80px:', len(small))
    print('dropped-figure rows:', sum(1 for r in rows if not r['resolved']))


if __name__ == '__main__': main()
