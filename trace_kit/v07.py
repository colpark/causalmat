"""v07.py: the v07 per-paper pipeline, one stage per call. Subagent work goes through relay.py job files.

  v07.py prep <P> <part>      spec, cut (A1 skip rule), writer packets and reread tasks for the open traces
                              -> jobs_writer.json, jobs_reread.json
  v07.py rrgrade <P>          after the reread harvest: grader prompts, one per (panel, evidence node) -> jobs_rrgrade.json
  v07.py written <P>          after the writer and rrgrade harvests: reread flags applied, writer merged, nets run;
                              writer pass 2 packets for leak/provenance hits the writer can fix -> jobs_writer2.json
  v07.py written2 <P>         pass 2 merged into written.json, nets run again
  v07.py gate <P>             gate packets for open traces that pass the nets and the second read -> jobs_gate.json
  v07.py grade <P>            grader prompts from the arm replies -> jobs_grade.json (CANNOT DETERMINE is ABSTAIN, no grader)
  v07.py verdict <P>          gate.jsonl rows; full-arm failures not flagged by the second read -> inspect.md for the inspector
  v07.py cause <P>            inspector causes merged into gate.jsonl
  v07.py row <P>              one row of results/v07/batch.csv
  v07.py log <P> <kind> <agent_id>   records a staff/judge/inspector/relay dispatch for the dispatch count and wall time

Paths: packets taxonomy/v07/<part>/packets/<P>.md, graph taxonomy/graphs_v07/<P>.json, spec taxonomy/specs_v07/<P>.json,
everything else results/v07/papers/<P>/. Every verdict is model against model.
"""
import csv, json, os, re, subprocess, sys, time, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
IMG = os.path.join(ROOT, '.v07work', 'rr')
GRAPHS = os.environ.get('V07_GRAPHS', os.path.join(ROOT, 'taxonomy', 'graphs_v07'))
NOTE = "Every verdict is model against model."

def D(P): return os.path.join(ROOT, 'results', 'v07', 'papers', P)
def G(P): return os.path.join(GRAPHS, P + '.json')
def J(p): return json.load(open(p))
def dump(o, p): json.dump(o, open(p, 'w'), indent=1)
def run(*a): subprocess.run([sys.executable, *a], check=True, cwd=ROOT, stdout=subprocess.DEVNULL)

def stamp(P, stage):
    p = os.path.join(D(P), 'timing.json'); t = J(p) if os.path.exists(p) else []
    t.append({'stage': stage, 't': time.time()}); dump(t, p)

def jobs(P, name, items):
    p = os.path.join(D(P), f'jobs_{name}.json'); dump(items, p); print(f'{P} {name}: {len(items)} jobs -> {p}'); return p

def prep(P, part):
    d = D(P); os.makedirs(d, exist_ok=True); stamp(P, 'prep')
    spec = os.path.join(ROOT, 'taxonomy', 'specs_v07', P + '.json'); os.makedirs(os.path.dirname(spec), exist_ok=True)
    run('taxonomy/collapse_modality.py', '--graph', G(P), '--out', spec, '--file', P + '.html')
    cut = os.path.join(d, 'cut.traces.json')
    run('trace_kit/cut_traces.py', G(P), spec, cut)
    C = J(cut); op = [t['id'] for t in C['traces'] if t['status'] == 'open']
    W = os.path.join(d, 'writer')
    if op: run('trace_kit/writer_packets.py', 'build', G(P), cut, W, '--only', ','.join(op))
    jobs(P, 'writer', [{'id': f'{P[:16]}/{T}/writer', 'agent': 'net-writer', 'prompt': os.path.join(W, f'{T}.writer.txt'),
                        'out': os.path.join(W, f'{T}.writer.out.txt')} for T in op])
    R = os.path.join(d, 'reread')
    run('trace_kit/reread.py', 'build', cut, G(P), R, IMG)
    rr = J(os.path.join(R, 'reread.json'))['tasks']
    jobs(P, 'reread', [{'id': f'{P[:16]}/{p}/reread', 'agent': 'net-reread', 'prompt': os.path.join(R, f'{p}.reread.txt'),
                        'out': os.path.join(R, f'{p}.reread.out.txt')} for p in rr])

def rrgrade(P, R=None):
    from reread import grader_prompt, units
    R = R or os.path.join(D(P), 'reread'); rr = J(os.path.join(R, 'reread.json')); out = []
    labels = {n: l for k in rr['tasks'].values() for n, l in k['node_labels'].items()}
    for key, u in units(rr).items():
        descs = [(p, open(os.path.join(R, f'{p}.reread.out.txt')).read()) for p in u['panels'] if os.path.exists(os.path.join(R, f'{p}.reread.out.txt'))]
        if len(descs) < len(u['panels']): continue
        q = os.path.join(R, f'{key}.grader.txt'); open(q, 'w').write(grader_prompt(descs, labels[u['node']]))
        out.append({'id': f'{P[:16]}/{key}/rrgrade', 'agent': 'net-grader', 'prompt': q, 'out': q.replace('.grader.txt', '.grader.out.txt')})
    rr['units'] = units(rr); dump(rr, os.path.join(R, 'reread.json'))
    return jobs(P, 'rrgrade', out) if R == os.path.join(D(P), 'reread') else out

def apply_reread(P, R=None):
    R = R or os.path.join(D(P), 'reread'); path = os.path.join(R, 'reread.json'); rr = J(path); flags = {}
    for key, u in rr.get('units', {}).items():
        f = os.path.join(R, f'{key}.grader.out.txt')
        if not os.path.exists(f): continue
        reply = open(f).read().strip(); m = re.match(r'\W*(CORRECT|PARTIAL|WRONG|ABSTAIN)', reply.upper())
        u['verdict'] = m.group(1) if m else 'UNPARSED'; u['why'] = reply
        if u['verdict'] == 'WRONG':
            for T in u['traces']: flags.setdefault(T, []).append({'panels': u['panels'], 'node': u['node'], 'why': reply})
    rr['flags'] = flags; dump(rr, path); return flags

def nets(P, written):
    val = os.path.join(D(P), 'validation.json')
    run('trace_kit/validate_traces.py', G(P), written, val); return J(val)

def feedback(P, written, val):
    import validate_traces as V
    N = {n['id']: n for n in J(G(P))['nodes']}; T = {t['id']: t for t in J(written)['traces']}; fb = {}
    for v in val:
        f = v.get('fails', []); t = T[v['id']]; msgs = []
        if 'leak' in f:
            L = v['nets']['leak']; q = t.get('question', '')
            qb = [b for b in L['bigrams'] if tuple(b.split()) in V.bigrams(q)]; qn = [n for n in L['numbers'] if n in V.nums(q)]
            if qb or qn:
                msgs.append('The leak net flagged your question: it shares ' + ', '.join([f'the word pair "{b}"' for b in qb] + [f'the number {n}' for n in qn]) +
                            ' with the hidden nodes. Write the question again so it does not use them or any other wording from the hidden nodes; refer to the panels and the given nodes instead.')
        if 'provenance' in f:
            m = v['nets']['provenance'].get('missing_numbers') or []
            if m: msgs.append('The provenance net flagged your answer key: it contains ' + ', '.join(m) + ', which no cited node label carries. Use only numbers written in the node labels.')
        if msgs: fb[v['id']] = '\n'.join(msgs)
    return fb

def written_stage(P):
    d = D(P); stamp(P, 'written'); flags = apply_reread(P)
    cut = os.path.join(d, 'cut.traces.json'); W = os.path.join(d, 'writer'); wr = os.path.join(d, 'written.json')
    subprocess.run([sys.executable, 'trace_kit/writer_packets.py', 'merge', cut, W, wr], cwd=ROOT, stdout=subprocess.DEVNULL)
    val = nets(P, wr); fb = feedback(P, wr, val); dump(fb, os.path.join(W, 'feedback_pass2.json'))
    out = []
    if fb:
        P2 = os.path.join(W, 'pass2')
        run('trace_kit/writer_packets.py', 'build', G(P), cut, P2, '--only', ','.join(fb), '--feedback', os.path.join(W, 'feedback_pass2.json'))
        out = [{'id': f'{P[:16]}/{T}/writer2', 'agent': 'net-writer', 'prompt': os.path.join(P2, f'{T}.writer.txt'),
                'out': os.path.join(P2, f'{T}.writer.out.txt')} for T in fb]
    jobs(P, 'writer2', out); print('reread flags:', {k: len(v) for k, v in flags.items()})

def written2(P):
    from writer_packets import parse, FIELDS
    d = D(P); wr = os.path.join(d, 'written.json'); T = J(wr); P2 = os.path.join(d, 'writer', 'pass2')
    for t in T['traces']:
        f = os.path.join(P2, f"{t['id']}.writer.out.txt")
        if os.path.exists(f):
            try:
                r = parse(open(f).read()); t['writer_passes'] = 2
                for k in FIELDS: t[k] = r.get(k, [] if k == 'answer_key_nodes' else '')
            except Exception as e: t['writer_pass2_error'] = str(e)
    dump(T, wr); nets(P, wr)

def gate(P):
    d = D(P); stamp(P, 'gate'); import gate_packets
    wr = os.path.join(d, 'written.json'); val = os.path.join(d, 'validation.json'); gd = os.path.join(d, 'gate')
    flags = J(os.path.join(d, 'reread', 'reread.json')).get('flags', {})
    gate_packets.main(P, wr, val, gd, G(P))
    out = []
    for f in sorted(glob.glob(os.path.join(gd, 'T*.gate.json'))):
        pk = J(f); T = pk['trace']
        if T in flags: os.rename(f, f + '.flagged'); continue
        for arm, agent in (('fullarm', 'net-fullarm'), ('floor', 'net-floor')):
            q = os.path.join(gd, f'{T}.{arm}.txt'); open(q, 'w').write(pk[arm])
            out.append({'id': f'{P[:16]}/{T}/{arm}', 'agent': agent, 'prompt': q, 'out': os.path.join(gd, f'{T}.{arm}.out.txt')})
    jobs(P, 'gate', out)

def grade(P):
    from gate_harvest import grader_prompt
    gd = os.path.join(D(P), 'gate'); out = []
    for f in sorted(glob.glob(os.path.join(gd, 'T*.gate.json'))):
        pk = J(f); T = pk['trace']; q = pk['fullarm'].split('Question: ', 1)[1].split('\n\nImages', 1)[0]
        for arm in ('fullarm', 'floor'):
            a = os.path.join(gd, f'{T}.{arm}.out.txt')
            if not os.path.exists(a): continue
            cand = open(a).read()
            if cand.strip().upper().startswith('CANNOT DETERMINE'):
                open(os.path.join(gd, f'{T}.grader.{arm}.out.txt'), 'w').write('ABSTAIN (candidate says CANNOT DETERMINE; not sent to the grader)'); continue
            p = os.path.join(gd, f'{T}.grader.{arm}.txt'); open(p, 'w').write(grader_prompt(pk, q, cand))
            out.append({'id': f'{P[:16]}/{T}/grader.{arm}', 'agent': 'net-grader', 'prompt': p, 'out': p.replace('.txt', '.out.txt')})
    jobs(P, 'grade', out)

def word(p):
    if not os.path.exists(p): return None
    m = re.match(r'\W*(CORRECT|PARTIAL|WRONG|ABSTAIN)', open(p).read().strip().upper()); return m.group(1) if m else 'UNPARSED'

def classify(full, floor):
    if full in ('CORRECT', 'PARTIAL'):
        if floor == 'CORRECT' or (floor == 'PARTIAL' and full == 'PARTIAL'): return 'text-sufficient'
        return 'valid'
    return 'inspect'

def verdict(P):
    d = D(P); stamp(P, 'verdict'); gd = os.path.join(d, 'gate'); rows = []
    W = {t['id']: t for t in J(os.path.join(d, 'written.json'))['traces']}
    flags = J(os.path.join(d, 'reread', 'reread.json')).get('flags', {})
    for T, fl in flags.items():
        if T in W and W[T]['status'] == 'open':
            rows.append({'paper': P, 'trace': T, 'root': W[T]['root'], 'subtype': W[T]['subtype'], 'fullarm': None, 'floor': None,
                         'verdict': 'inspect', 'partial': False, 'cause': 'graph', 'stage': 'second read',
                         'defect': '; '.join(f"{'+'.join(x['panels'])}/{x['node']}: {x['why'][:200]}" for x in fl), 'note': NOTE})
    pend = []
    for f in sorted(glob.glob(os.path.join(gd, 'T*.gate.json'))):
        pk = J(f); T = pk['trace']
        full, floor = word(os.path.join(gd, f'{T}.grader.fullarm.out.txt')), word(os.path.join(gd, f'{T}.grader.floor.out.txt'))
        v = classify(full, floor)
        r = {'paper': P, 'trace': T, 'root': pk['root'], 'subtype': pk['subtype'], 'writer_passes': W[T].get('writer_passes', 1),
             'fullarm': full, 'floor': floor, 'verdict': v, 'partial': v == 'valid' and full == 'PARTIAL', 'cause': None,
             'stage': 'gate' if v == 'inspect' else None, 'defect': None, 'answer_scope': pk['key']['answer_scope'], 'note': NOTE}
        rows.append(r)
        if v == 'inspect': pend.append(T)
    with open(os.path.join(d, 'gate.jsonl'), 'w') as fo:
        for r in rows: fo.write(json.dumps(r) + '\n')
    if pend:
        L = [f"# Inspect packet: {P}\n", "For each item below the image-reading arm (net-fullarm) failed the solving gate. Decide the cause of each failure. "
             "Open the images listed in the arm's prompt with Read. Causes: graph (the graph's evidence node misreads the panel, or the claim is not in "
             "the panel), cutter (the item gives the wrong panels, withholds what the key needs, or the answer is written on the image), writer (the "
             "question or key is unclear, paraphrased past recognition, or asks for more than the key supports), grader (the arm's answer was in fact "
             "right), solver (the item is fair and the arm misread it).\n",
             "Reply with JSON only: {\"items\": [{\"trace\": \"T..\", \"cause\": \"graph|cutter|writer|grader|solver\", \"defect\": \"one sentence\"}]}\n"]
        for T in pend:
            pk = J(os.path.join(gd, f'{T}.gate.json'))
            L += [f"\n## {T}\n### Arm prompt\n{pk['fullarm']}\n### Answer key (answer_scope {pk['key']['answer_scope']})\n{pk['key']['answer_key']}\n"
                  f"### Grading note\n{pk['key']['grading']}\n### Arm answer\n{open(os.path.join(gd, f'{T}.fullarm.out.txt')).read().strip()}\n"
                  f"### Grader\n{open(os.path.join(gd, f'{T}.grader.fullarm.out.txt')).read().strip()}\n"]
        open(os.path.join(d, 'inspect.md'), 'w').write('\n'.join(L))
    print(P, {k: sum(r['verdict'] == k for r in rows) for k in ('valid', 'text-sufficient', 'inspect')}, 'inspect pending:', pend)

def cause(P):
    d = D(P); f = os.path.join(d, 'inspect.out.txt')
    from writer_packets import parse
    C = {x['trace']: x for x in parse(open(f).read()).get('items', [])} if os.path.exists(f) else {}
    rows = [json.loads(l) for l in open(os.path.join(d, 'gate.jsonl'))]
    for r in rows:
        if r['verdict'] == 'inspect' and r['cause'] is None and r['trace'] in C:
            r['cause'] = C[r['trace']].get('cause'); r['defect'] = C[r['trace']].get('defect')
    with open(os.path.join(d, 'gate.jsonl'), 'w') as fo:
        for r in rows: fo.write(json.dumps(r) + '\n')
    stamp(P, 'done'); print(P, [(r['trace'], r['cause']) for r in rows if r['verdict'] == 'inspect'])

def log(P, kind, agent_id):
    p = os.path.join(D(P), 'dispatch_log.json'); os.makedirs(D(P), exist_ok=True)
    L = J(p) if os.path.exists(p) else []; L.append({'kind': kind, 'agent_id': agent_id, 't': time.time()}); dump(L, p)

def agent_span(aid):
    """first and last timestamps of an agent transcript (seconds since epoch)"""
    from relay import transcript
    tr = transcript(aid); ts = []
    if not os.path.exists(tr): return None
    from datetime import datetime
    for l in open(tr):
        try: t = json.loads(l).get('timestamp')
        except ValueError: continue
        if t: ts.append(datetime.fromisoformat(t.replace('Z', '+00:00')).timestamp())
    return (min(ts), max(ts)) if ts else None

COLS = ['paper', 'journal', 'year', 'n_figures', 'annotated_share', 'graph_nodes', 'graph_spine', 'judge_checks', 'judge_overturns',
        'traces_cut', 'open', 'closed_by_rule', 'written', 'passed_nets', 'reread_flags', 'valid', 'valid_partial', 'text_sufficient',
        'inspect', 'inspect_cause', 'subagent_dispatches', 'wall_minutes']

def row(P, meta_path=None):
    d = D(P); g = J(G(P)); C = J(os.path.join(d, 'cut.traces.json'))
    rows = [json.loads(l) for l in open(os.path.join(d, 'gate.jsonl'))] if os.path.exists(os.path.join(d, 'gate.jsonl')) else []
    rv = g.get('review') or {}; pc = rv.get('panel_checks') or []
    j, _, doi = P.partition('__'); base = os.path.join(ROOT, 'matmech', j, doi)
    mj = J(os.path.join(base, 'panels', 'match.json')); data = J(os.path.join(base, 'data.json')) if os.path.exists(os.path.join(base, 'data.json')) else {}
    ocr = J(os.path.join(base, 'panels', 'ocr.json'))['crops'] if os.path.exists(os.path.join(base, 'panels', 'ocr.json')) else []
    sys.path.insert(0, os.path.join(ROOT, 'taxonomy')); from build_packets_v06 import classify as cls
    ann = sum(any(cls(t['text']) == 'annotation' for t in c.get('tokens', [])) for c in ocr)
    from collections import Counter
    closed = Counter()
    for t in C['traces']:
        if t['status'] != 'closed': continue
        last = [m['rule'] for m in t.get('v2_rules', []) if m['rule'] in ('R3', 'R4', 'R6', 'skip', 'no_crop')]
        k = t.get('closed_by') or ('R6' if (t.get('blocked') or {}).get('reason') == 'panel_modality' else (last[-1] if last else 'other'))
        closed[k] += 1
    val = J(os.path.join(d, 'validation.json')) if os.path.exists(os.path.join(d, 'validation.json')) else []
    flags = J(os.path.join(d, 'reread', 'reread.json')).get('flags', {})
    # dispatches: every harvested job (writer, reread, graders, arms) plus logged staff/judge/inspector/relay agents
    ids = set()
    for h in glob.glob(os.path.join(d, 'jobs_*.json.harvest.json')):
        for x in J(h)['jobs']:
            if x.get('agent_id'): ids.add(x['agent_id'])
    logd = J(os.path.join(d, 'dispatch_log.json')) if os.path.exists(os.path.join(d, 'dispatch_log.json')) else []
    ids |= {x['agent_id'] for x in logd}
    spans = [s for s in (agent_span(a) for a in ids) if s]
    wall = (max(s[1] for s in spans) - min(s[0] for s in spans)) / 60 if spans else None
    sp = set(g.get('spine') or []) if isinstance(g.get('spine'), list) else None
    r = {'paper': P, 'journal': j, 'year': data.get('year') or (data.get('paper_info') or {}).get('year'), 'n_figures': len(mj['figures']),
         'annotated_share': round(ann / len(ocr), 3) if ocr else None, 'graph_nodes': len(g['nodes']),
         'graph_spine': len(sp) if sp is not None else sum(1 for n in g['nodes'] if n.get('spine')),
         'judge_checks': len(pc), 'judge_overturns': sum(1 for x in pc if str(x.get('ruling', '')).lower().startswith('overturn')),
         'traces_cut': len(C['traces']), 'open': sum(t['status'] == 'open' for t in C['traces']),
         'closed_by_rule': '/'.join(f"{k}:{closed.get(k, 0)}" for k in ('R3', 'R4', 'R6', 'skip', 'no_crop')) + (f"/other:{closed['other']}" if closed.get('other') else ''),
         'written': sum(1 for f in glob.glob(os.path.join(d, 'writer', 'T*.writer.out.txt'))),
         'passed_nets': sum(1 for v in val if not v.get('fails')), 'reread_flags': len(flags),
         'valid': sum(x['verdict'] == 'valid' for x in rows), 'valid_partial': sum(x['verdict'] == 'valid' and x.get('partial') for x in rows),
         'text_sufficient': sum(x['verdict'] == 'text-sufficient' for x in rows), 'inspect': sum(x['verdict'] == 'inspect' for x in rows),
         'inspect_cause': '/'.join(f"{k}:{v}" for k, v in sorted(Counter(x['cause'] for x in rows if x['verdict'] == 'inspect').items(), key=lambda kv: str(kv[0]))),
         'subagent_dispatches': len(ids), 'wall_minutes': round(wall, 1) if wall is not None else None}
    out = os.path.join(ROOT, 'results', 'v07', 'batch.csv'); new = not os.path.exists(out)
    prev = [x for x in csv.DictReader(open(out))] if not new else []
    prev = [x for x in prev if x['paper'] != P] + [{k: r[k] for k in COLS}]
    with open(out, 'w', newline='') as fo:
        w = csv.DictWriter(fo, COLS); w.writeheader(); w.writerows(prev)
    print(json.dumps(r))

if __name__ == '__main__':
    a = sys.argv
    {'prep': lambda: prep(a[2], a[3]), 'rrgrade': lambda: rrgrade(a[2]), 'written': lambda: written_stage(a[2]),
     'written2': lambda: written2(a[2]), 'gate': lambda: gate(a[2]), 'grade': lambda: grade(a[2]), 'verdict': lambda: verdict(a[2]),
     'cause': lambda: cause(a[2]), 'row': lambda: row(a[2]), 'log': lambda: log(a[2], a[3], a[4])}[a[1]]()
