"""materialize.py: write a case's panels and panels.csv.

  python3 trace_kit_v2/materialize.py <case_dir>

Every cited panel is handed over WHOLE, unaltered, at its native crop resolution. Published figures
carry the authors' marks; that is the data, and it is measured on as it stands.

Annotation handling was withdrawn on 2026-09-23. The saturation and OCR-box splits, the layer
decisions, masking and the annotation-keyed skip rule are all gone: the removal was destroying the
figure (up to 45% of one panel) and the detection feeding it was not reliable enough to decide
anything on, including which panels to drop.

A panel leaves a chain for one reason only: no crop resolves for it.
"""
import csv, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
from PIL import Image


def main(case_dir):
    ch = json.load(open(os.path.join(case_dir, 'case.json')))
    img = os.path.join(case_dir, 'images'); os.makedirs(img, exist_ok=True)
    rows = []
    for step in ch['steps']:
        for p in step['panels']:
            png = None; size = None
            if p.get('crop') and os.path.exists(p['crop']):
                png = os.path.join(img, p['suffix'] + '.png')
                im = Image.open(p['crop']).convert('RGB')
                im.save(png)                      # native size, no resampling
                size = im.size
            p['png'] = os.path.relpath(png, case_dir) if png else None
            p['width'], p['height'] = (size or (None, None))
            for dead in ('layer_decision', 'layer_why', 'masked_fraction', 'split_ok',
                         'split_method', 'split_coverage', 'n_regions', 'hiding_compliant', 'split_why'):
                p.pop(dead, None)
            rows.append({'file': p['png'] or '', 'panel_id': p['panel_id'], 'suffix': p['suffix'],
                         'step': step['step'], 'node': step['node'], 'technique': step['technique'],
                         'delivery': step['delivery'], 'expected_support': step['expected_support'],
                         'width': p['width'] or '', 'height': p['height'] or '',
                         'resolved': bool(png), 'caption_span': p.get('caption_span') or ''})
    with open(os.path.join(case_dir, 'panels.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
    json.dump(ch, open(os.path.join(case_dir, 'case.json'), 'w'), indent=1)
    n = sum(1 for r in rows if r['resolved'])
    print(f"{ch['case']}: {n}/{len(rows)} panels handed over whole, unaltered")


if __name__ == '__main__': main(sys.argv[1])
