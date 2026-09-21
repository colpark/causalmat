"""diff_writer.py: compare writer-written traces against the hand-written fixture, trace by trace.

  python diff_writer.py <graph.json> <written.traces.json> <written.validation.json> <fixture.traces.json> <fixture.validation.json> <out.md> [title]
Columns: hidden target named in the key, grader named in the grading note, numbers in the key (and unsourced ones),
answer_key_nodes, structural verdict. Model against model: the writer is a Sonnet subagent, the fixture is hand-written.
"""
import json, re, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from validate_traces import nums

def target_of(t, redacted):
    if t['root'] == 'infer': return [t['evidence'][0], t['seed_claim']]
    if t['subtype'] == 'competing causes': return [h for h in t.get('hidden', []) if h not in redacted]
    if t['subtype'] == 'mechanism' or t['root'] == 'intervene': return [t['seed_claim']]
    return t['evidence'][:1]

def row(t, v, N):
    if t['status'] == 'closed' or not t.get('walk'):
        tgt = [t['seed_claim']]
    else:
        tgt = [x for x in target_of(t, {r['node'] for r in t.get('redactions') or []}) if x in N]
    key = t.get('answer_key', '') or ''; akn = t.get('answer_key_nodes') or []
    cited = set(re.findall(r'\b([a-z]\d+)\b', key)) | set(akn)
    tgt_named = [x for x in tgt if x in cited]
    grader_ids = re.findall(r'\b([a-z]\d+)\b', t.get('grader', ''))
    grading = t.get('grading', '') or ''
    g_named = [x for x in grader_ids if re.search(rf'\b{x}\b', grading)] if grader_ids else None
    knums = sorted(nums(re.sub(r'\b[a-z]\d+\b', '', key)), key=float)
    prov = (v.get('nets') or {}).get('provenance', {})
    return dict(tgt=tgt, tgt_named=tgt_named, grader_ids=grader_ids, grader_named=g_named, any_id_in_grading=sorted(set(re.findall(r'\b([a-z]\d+)\b', grading))),
                nums=knums, missing=prov.get('missing_numbers', []), akn=sorted(akn), verdict=v.get('verdict'), fails=v.get('fails', []))

def main(gp, wp, wvp, fp, fvp, out, title=''):
    N = {n['id']: n for n in json.load(open(gp))['nodes']}
    W = {t['id']: t for t in json.load(open(wp))['traces']}; F = {t['id']: t for t in json.load(open(fp))['traces']}
    WV = {v['id']: v for v in json.load(open(wvp))}; FV = {v['id']: v for v in json.load(open(fvp))}
    L = [f"# Writer versus hand: ceramic twelve{(' — ' + title) if title else ''}", '',
         'Every verdict here is model against model: the writer is a Sonnet subagent (net-writer, no tools), the structural nets are code, and the reference is the hand-written fixture. No human checked any item.', '',
         '| T | status | hidden target named (hand / writer) | grader node named (hand / writer) | numbers in key (hand / writer) | unsourced (writer) | answer_key_nodes (hand / writer) | verdict (hand / writer) |',
         '|---|---|---|---|---|---|---|---|']
    rows = {}
    for tid in F:
        h = row(F[tid], FV.get(tid, {}), N); w = row(W[tid], WV.get(tid, {}), N); rows[tid] = (h, w)
        fmt_t = lambda r: f"{len(r['tgt_named'])}/{len(r['tgt'])}"
        fmt_g = lambda r: 'n/a' if r['grader_named'] is None else ('yes' if r['grader_named'] else 'no')
        fmt_v = lambda r: r['verdict'] + (f" [{', '.join(r['fails'])}]" if r['fails'] else '')
        L.append(f"| {tid} | {F[tid]['status']} | {fmt_t(h)} / {fmt_t(w)} | {fmt_g(h)} / {fmt_g(w)} | {', '.join(h['nums']) or '-'} / {', '.join(w['nums']) or '-'} | {', '.join(w['missing']) or '-'} | {', '.join(h['akn']) or '-'} / {', '.join(w['akn']) or '-'} | {fmt_v(h)} / {fmt_v(w)} |")
    open(out, 'w').write('\n'.join(L) + '\n')
    return rows

if __name__ == '__main__':
    main(*sys.argv[1:8])
