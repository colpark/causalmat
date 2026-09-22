"""v07_a3.py: the A3 recheck of the eight pilot papers against v06c.

For every v06c gate item (11 valid, 3 text-sufficient, 9 inspect): closed by A1 (skip or no crop), flagged by the second
read (A2: inspect, cause graph), or still open. An open item's trace is unchanged from v06c (same walk, same given panels,
no masking in v06c), so its writer output and gate prompts are byte-identical and its v06c gate verdict stands.
Writes results/v07/pilot/a3.json and results/v07/pilot/gate.jsonl. Every verdict is model against model.
"""
import json, os, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
NOTE = "Every verdict is model against model."

def main():
    old = [json.loads(l) for l in open(os.path.join(ROOT, 'results/v06c/solving_gate.jsonl'))]
    out, rows = [], []
    for r in old:
        P, T = r['paper'], r['trace']
        cut = json.load(open(os.path.join(ROOT, 'results/v07/pilot/cut', P + '.traces.json')))
        t = next(x for x in cut['traces'] if x['id'] == T)
        rr = os.path.join(ROOT, 'results/v07/pilot/reread', P, 'reread.json')
        flags = json.load(open(rr)).get('flags', {}) if os.path.exists(rr) else {}
        rec = {'paper': P, 'trace': T, 'v06c': r['verdict'], 'v06c_partial': r.get('partial'), 'v06c_cause': r.get('cause')}
        if t['status'] == 'closed':
            note = next((m['effect'] for m in reversed(t.get('v2_rules', [])) if m['rule'] in ('skip', 'no_crop')), '')
            rec.update({'v07': 'closed', 'rule': t.get('closed_by'), 'ruling': t['ruling'], 'why': note})
        elif T in flags:
            rec.update({'v07': 'inspect', 'rule': 'second read', 'cause': 'graph',
                        'why': '; '.join(f"{'+'.join(f['panels'])}/{f['node']}: {f['why']}" for f in flags[T])})
        else:
            rec.update({'v07': r['verdict'], 'rule': None, 'why': 'trace unchanged; v06c gate verdict carried'})
        out.append(rec)
        if rec['v07'] != 'closed':
            rows.append({**{k: r[k] for k in ('paper', 'trace', 'root', 'subtype', 'fullarm', 'floor', 'answer_scope')},
                         'verdict': rec['v07'], 'partial': r.get('partial') if rec['v07'] == 'valid' else False,
                         'cause': rec.get('cause') or (r.get('cause') if rec['v07'] == 'inspect' else None),
                         'stage': 'second read' if rec['rule'] == 'second read' else ('gate' if rec['v07'] == 'inspect' else None),
                         'defect': rec['why'] if rec['rule'] == 'second read' else r.get('defect'), 'carried_from': 'v06c', 'note': NOTE})
    json.dump(out, open(os.path.join(ROOT, 'results/v07/pilot/a3.json'), 'w'), indent=1)
    with open(os.path.join(ROOT, 'results/v07/pilot/gate.jsonl'), 'w') as fo:
        for x in rows: fo.write(json.dumps(x) + '\n')
    for x in out: print(f"{x['paper'][:26]:26s} {x['trace']:4s} {x['v06c']:15s} -> {x['v07']:15s} {x['rule'] or '':12s} {x['why'][:110]}")
    from collections import Counter
    print('v07:', dict(Counter(x['v07'] for x in out)))

if __name__ == '__main__': main()
