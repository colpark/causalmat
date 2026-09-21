"""writer_packets.py: one net-writer packet per trace, and the merge of the writer's replies back into a traces file.

  build: python writer_packets.py build <graph.json> <traces.json> <out_dir> [--loo]
         --loo drops the exemplar with the same id as the trace (used on the ceramic paper, whose hand-written
         twelve ARE the exemplars; without it the writer would be handed its own answer key)
  merge: python writer_packets.py merge <traces.json> <out_dir> <written.json>
         reads <out_dir>/<T>.writer.out.txt, parses the JSON reply, writes the four fields into a copy
"""
import json, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
EXEMPLARS = os.path.join(HERE, 'fixtures', 'writer_exemplars.json')
FIELDS = ('question', 'answer_key', 'grading', 'answer_key_nodes')
DROP = FIELDS + ('validation',)
EX_DROP = ('linear', 'walk')   # exemplars are for form and length of the written fields; their step lists only add bulk

def referenced(t):
    ids = set(t.get('hidden', [])) | set(t.get('evidence', [])) | {t.get('seed_claim')}
    ids |= {s['node'] for s in t.get('walk', [])} | {n for s in t.get('linear', []) for n in s['nodes']}
    ids |= {r['node'] for r in t.get('redactions', [])}
    ids |= set(re.findall(r'\b([a-z]\d+)\b', t.get('grader', '') + ' ' + t.get('ruling', '')))
    return ids

def build(graph_path, traces_path, out_dir, loo=False):
    g = json.load(open(graph_path)); N = {n['id']: n for n in g['nodes']}
    T = json.load(open(traces_path)); ex = json.load(open(EXEMPLARS))
    os.makedirs(out_dir, exist_ok=True)
    for t in T['traces']:
        rec = {k: v for k, v in t.items() if k not in DROP}
        labels = {i: {'type': N[i]['type'], 'label': N[i]['label']} for i in sorted(referenced(t)) if i in N}
        exs = [{k: v for k, v in e.items() if k not in EX_DROP} for e in ex if not (loo and e['id'] == t['id'])]
        txt = ("Write the question, answer key, grading note and answer_key_nodes for this trace.\n\n"
               "TRACE RECORD\n" + json.dumps(rec, indent=1) +
               "\n\nNODE LABELS (every node the trace references)\n" + json.dumps(labels, indent=1) +
               "\n\nWORKED EXAMPLES (follow their form and length)\n" + json.dumps(exs, separators=(',', ':')) +
               '\n\nReply with JSON only: {"question": "...", "answer_key": "...", "grading": "...", "answer_key_nodes": [...]}')
        open(os.path.join(out_dir, f"{t['id']}.writer.txt"), 'w').write(txt)
    print(len(T['traces']), 'packets ->', out_dir)

def parse(txt):
    m = re.search(r'\{.*\}', txt, re.S)
    return json.loads(m.group(0))

def merge(traces_path, out_dir, written_path, suffix='writer.out.txt'):
    T = json.load(open(traces_path)); bad = []
    for t in T['traces']:
        p = os.path.join(out_dir, f"{t['id']}.{suffix}")
        if not os.path.exists(p): bad.append((t['id'], 'no reply')); continue
        try: r = parse(open(p).read())
        except Exception as e: bad.append((t['id'], f'unparsable: {e}')); continue
        for k in FIELDS: t[k] = r.get(k, [] if k == 'answer_key_nodes' else '')
    json.dump(T, open(written_path, 'w'), indent=1)
    print('merged ->', written_path, 'problems:', bad)
    return bad

if __name__ == '__main__':
    if sys.argv[1] == 'build': build(sys.argv[2], sys.argv[3], sys.argv[4], '--loo' in sys.argv)
    else: merge(sys.argv[2], sys.argv[3], sys.argv[4], *(sys.argv[5:6]))
