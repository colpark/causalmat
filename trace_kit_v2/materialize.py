"""materialize.py: write a case's images, annotation layers, panels.csv and label set.

  python3 trace_kit_v2/materialize.py <case_dir>

Plan section 3. Per panel one layer decision is taken and declared:
  as_is        the split cannot hide the whole layer (text-only OCR boxes, or no split at all), or the
               annotation IS the graded feature -- the author's label becomes the claim under test
  hidden       saturation split caught text and marks together; the clean panel is handed over and the
               masked regions are declared
  exemplar     the annotated panel is shown as an exemplar and the item is graded on clean siblings
Never inpaints: a hidden region is a flat median-grey block, visible and declared.
"""
import csv, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import annotate
from PIL import Image


def decide(panel, step):
    """the layer decision for one panel, with the reason recorded"""
    if not panel['crop']:
        return 'dropped', 'no crop resolves for this panel id'
    if not panel['split_ok']:
        return 'as_is', f"no layer could be split ({panel['split_why']}); panel handed over whole and declared"
    if step['read_from'] == 'annotation':
        return 'as_is', ("the observation is read from the author's annotation, so masking it would overlap the graded "
                         "feature; the author's label is the claim under test instead")
    if not panel['hiding_compliant']:
        return 'as_is', ("only OCR text boxes could be found, and hiding words while arrows or marks remain is forbidden; "
                         "panel handed over whole and declared")
    return 'hidden', 'saturation split caught the whole layer; clean panel handed over, masked regions declared'


def main(case_dir):
    ch = json.load(open(os.path.join(case_dir, 'case.json')))
    img = os.path.join(case_dir, 'images'); lay = os.path.join(img, 'layer')
    os.makedirs(lay, exist_ok=True)
    labels_dir = os.path.join(ROOT, 'results/v2/labels'); os.makedirs(labels_dir, exist_ok=True)
    pan_dir = os.path.join(ROOT, 'results/v2/panels', ch['paper']); os.makedirs(pan_dir, exist_ok=True)
    rows, labels = [], []
    for step in ch['steps']:
        for p in step['panels']:
            dec, why = decide(p, step)
            p['layer_decision'] = dec; p['layer_why'] = why
            png = masked = None
            if p['crop']:
                toks = []
                from cut_traces import store_for, panel_record
                st = store_for(os.path.join(ROOT, ch['graph']))
                r = panel_record(st, p['panel_id']) or {}
                toks = (r.get('ocr') or {}).get('tokens') or []
                sp = annotate.split(p['crop'], toks)
                png = os.path.join(img, p['suffix'] + '.png')
                if dec == 'hidden' and sp['ok']:
                    sp['clean'].save(png); masked = round(sp['masked_fraction'], 4)
                    sp['overlay'].save(os.path.join(lay, p['suffix'] + '.layer.png'))
                    sp['layer_mask'].save(os.path.join(lay, p['suffix'] + '.mask.png'))
                else:
                    Image.open(p['crop']).convert('RGB').save(png)
                    if sp['ok']:
                        sp['overlay'].save(os.path.join(lay, p['suffix'] + '.layer.png'))
                # the label set: harvested whether or not the item used it (plan section 3, last bullet)
                for t in toks:
                    labels.append({'paper': ch['paper'], 'panel_id': p['panel_id'], 'suffix': p['suffix'],
                                   'kind': 'text', 'text': t.get('text'), 'box': t.get('box'),
                                   'score': t.get('score'), 'technique': step['technique'],
                                   'used_by_item': dec != 'hidden'})
                for reg in (sp.get('regions') or []):
                    labels.append({'paper': ch['paper'], 'panel_id': p['panel_id'], 'suffix': p['suffix'],
                                   'kind': 'mark', 'text': None, 'box': reg['box'], 'area': reg['area'],
                                   'technique': step['technique'], 'split_method': sp['method'],
                                   'used_by_item': dec != 'hidden'})
            p['png'] = os.path.relpath(png, case_dir) if png else None
            p['masked_fraction'] = masked
            rows.append({'file': p['png'] or '', 'panel_id': p['panel_id'], 'step': step['step'],
                         'node': step['node'], 'technique': step['technique'], 'delivery': step['delivery'],
                         'expected_support': step['expected_support'],
                         'layer_decision': dec, 'layer_why': why,
                         'split_method': p['split_method'], 'split_ok': p['split_ok'],
                         'n_regions': p['n_regions'], 'masked_fraction': masked if masked is not None else '',
                         'ocr_tokens': p['ocr_tokens'], 'caption_span': p['caption_span'] or ''})
    with open(os.path.join(case_dir, 'panels.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
    lp = os.path.join(labels_dir, ch['paper'] + '.jsonl')
    with open(lp, 'a') as f:
        for l in labels: f.write(json.dumps(l) + '\n')
    json.dump(ch, open(os.path.join(case_dir, 'case.json'), 'w'), indent=1)
    print(f"{ch['case']}: {len(rows)} panels, {sum(1 for r in rows if r['layer_decision']=='hidden')} hidden, "
          f"{sum(1 for r in rows if r['layer_decision']=='as_is')} as_is, {len(labels)} labels -> {os.path.relpath(lp, ROOT)}")
    for r in rows: print(f"   {r['panel_id'].split('#')[1]:5s} {r['layer_decision']:8s} {r['layer_why'][:82]}")


if __name__ == '__main__': main(sys.argv[1])
