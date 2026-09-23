"""summarize.py: results/v2/v2_summary.json from every case's case.json and gate.json."""
import json, os, glob, collections, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARMS = ('full', 'floor', 'oracle_complete', 'no_image', 'permute_answer', 'permute_image')

def main():
    cases = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'results/v2/cases/*/*/case.json'))):
        d = os.path.dirname(f); ch = json.load(open(f))
        g = json.load(open(os.path.join(d, 'gate.json'))) if os.path.exists(os.path.join(d, 'gate.json')) else {}
        pan = [p for s in ch['steps'] for p in s['panels']]
        cases.append({
            'case': ch['case'], 'paper': ch['paper'], 'claim': ch['claim'],
            'claim_text': ch['claim_text'], 'n_steps': ch['n_steps'], 'channels': ch['channels'],
            'expected_levels': [s['expected_support'] for s in ch['steps']],
            'closing': ch['closing_support'], 'closing_why': ch.get('closing_why'),
            'lanes': ch['lanes'], 'tests': ch['tests'],
            'oracle_steps': [s['node'] for s in ch['steps'] if s['delivery'] == 'oracle'],
            'dropped_panels': ch['dropped_panels'],
            'necessity': {k: v['structural'] for k, v in ch['necessity'].items()},
            'layer_decisions': collections.Counter(p.get('layer_decision') for p in pan),
            'arms': {a: {'steps_correct': (g.get('arms', {}).get(a) or {}).get('steps_correct'),
                         'n_steps': (g.get('arms', {}).get(a) or {}).get('n_steps'),
                         'closing_got': (g.get('arms', {}).get(a) or {}).get('closing_got'),
                         'closing_correct': (g.get('arms', {}).get(a) or {}).get('closing_correct'),
                         'parsed': (g.get('arms', {}).get(a) or {}).get('parsed')} for a in ARMS},
            'item_valid': g.get('item_valid'), 'oracle_carries_the_task': g.get('oracle_carries_the_task'),
            'closing_alone_discriminates': g.get('closing_alone_discriminates'),
            'gt_disputes': g.get('gt_disputes', 0)})
    steps = sum(c['n_steps'] for c in cases)
    disp = sum(c['gt_disputes'] for c in cases)
    dl = [json.loads(l) for l in open(os.path.join(ROOT, 'results/v2/gt_disputes.jsonl'))] if os.path.exists(os.path.join(ROOT, 'results/v2/gt_disputes.jsonl')) else []
    labels = sum(1 for f in glob.glob(os.path.join(ROOT, 'results/v2/labels/*.jsonl')) for _ in open(f))
    layers = collections.Counter(k for c in cases for k, n in c['layer_decisions'].items() for _ in range(n))
    oracle_ge_full = [c['case'] for c in cases
                      if (c['arms']['oracle_complete']['steps_correct'] or 0) >= (c['arms']['full']['steps_correct'] or 0)]
    out = {'date': '2026-09-23', 'branch': 'traces-v2/2026-09-23',
           'note': 'Every verdict is model against model. The four-level ground truth is itself a model label.',
           'cases': cases,
           'totals': {'cases': len(cases), 'graded_steps': steps,
                      'channels_per_case': round(sum(len(c['channels']) for c in cases) / len(cases), 2),
                      'steps_per_case': round(steps / len(cases), 2),
                      'labels_harvested': labels, 'layer_decisions': dict(layers),
                      'gt_disputes': disp, 'gt_dispute_rate': round(disp / steps, 3),
                      'dispute_directions': dict(collections.Counter(f"{d['graph_label']}->{d['arm_label']}" for d in dl)),
                      'items_valid': sum(1 for c in cases if c['item_valid'])},
           'arm_totals': {a: {'steps_correct': sum((c['arms'][a]['steps_correct'] or 0) for c in cases),
                              'of': sum((c['arms'][a]['n_steps'] or 0) for c in cases),
                              'closings_correct': sum(1 for c in cases if c['arms'][a]['closing_correct']),
                              'parsed': sum(1 for c in cases if c['arms'][a]['parsed'])} for a in ARMS},
           'stop_rules': {
             'oracle_matches_full_in_2_or_more': {'fired': len(oracle_ge_full) >= 2, 'cases': oracle_ge_full},
             'gt_disputes_over_one_third': {'fired': disp / steps > 1 / 3, 'rate': round(disp / steps, 3)},
             'single_step_item': {'fired': any(c['n_steps'] < 2 for c in cases)},
             'case1_not_a_chain': {'fired': False}}}
    json.dump(out, open(os.path.join(ROOT, 'results/v2/v2_summary.json'), 'w'), indent=1)
    print(json.dumps(out['totals'], indent=1))
    print('arm totals:', json.dumps(out['arm_totals'], indent=1))
    print('stop rules:', json.dumps(out['stop_rules'], indent=1))

if __name__ == '__main__': main()
