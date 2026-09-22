"""v07_pilot_rows.py: batch.csv rows for the eight pilot papers (v06b graphs, v06c writer and gate, v07 A1 cut and A2 reread).

Dispatches and wall time are measured from agent transcripts on this host: every transcript whose first prompt names a
pilot paper (journal/doi, journal__doi, or a crop path under matmech/<journal>/<doi>) counts for that paper, with a share
1/k when it names k pilot papers (v06b staff and judge agents each took several). The v07 A2 second-read agents are
matched through their image map. Relays that served several papers count with their share. Wall minutes span the first to
the last timestamp of the paper's agents. Every verdict is model against model.
"""
import csv, glob, json, os, re, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import v07
from relay import dispatches, transcript
from harvest import read

def first_prompt(tr):
    try: return read(tr)[0]
    except Exception: return ''

def main():
    papers = [l.strip().replace('/', '__', 1) for l in open(os.path.join(ROOT, 'taxonomy/v06b_pilot/papers.txt')) if l.strip()]
    keys = {P: [P, P.replace('__', '/', 1), 'matmech/' + P.replace('__', '/', 1)] for P in papers}
    trs = [t for t in glob.glob('/tmp/claude-1000/-home-aid1-Documents-causalmat/*/tasks/*.output') if os.path.basename(t).startswith('a')]
    share, spans = {P: 0.0 for P in papers}, {P: [] for P in papers}
    ids = {P: set() for P in papers}
    for t in trs:
        p = first_prompt(t)
        hit = [P for P in papers if any(k in p for k in keys[P])]
        if not hit: continue
        aid = os.path.basename(t)[:-7]; sp = v07.agent_span(aid)
        for P in hit:
            share[P] += 1 / len(hit); ids[P].add(aid)
            if sp: spans[P].append(sp)
    # v07 A2 second reads (hashed image paths) and their relays
    for P in papers:
        R = os.path.join(ROOT, 'results/v07/pilot/reread', P, 'reread.json')
        if not os.path.exists(R): continue
        imgs = {os.path.basename(k.get('image_original') or k.get('image') or '') for k in json.load(open(R))['tasks'].values()}
        for t in trs:
            aid = os.path.basename(t)[:-7]
            if aid in ids[P]: continue
            p = first_prompt(t)
            if p and any(i and i in p for i in imgs):
                share[P] += 1; ids[P].add(aid); sp = v07.agent_span(aid)
                if sp: spans[P].append(sp)
    out = os.path.join(ROOT, 'results/v07/batch.csv')
    prev = [x for x in csv.DictReader(open(out))] if os.path.exists(out) else []
    rows = [json.loads(l) for l in open(os.path.join(ROOT, 'results/v07/pilot/gate.jsonl'))]
    sys.path.insert(0, os.path.join(ROOT, 'taxonomy')); from build_packets_v06 import classify as cls
    new = []
    for P in papers:
        g = json.load(open(os.path.join(ROOT, 'taxonomy/graphs_v06b', P + '.json')))
        C = json.load(open(os.path.join(ROOT, 'results/v07/pilot/cut', P + '.traces.json')))
        pc = (g.get('review') or {}).get('panel_checks') or []
        j, _, doi = P.partition('__'); base = os.path.join(ROOT, 'matmech', j, doi)
        mj = json.load(open(os.path.join(base, 'panels/match.json')))
        ocr = json.load(open(os.path.join(base, 'panels/ocr.json')))['crops'] if os.path.exists(os.path.join(base, 'panels/ocr.json')) else []
        data = json.load(open(os.path.join(base, 'data.json'))) if os.path.exists(os.path.join(base, 'data.json')) else {}
        closed = Counter()
        for t in C['traces']:
            if t['status'] != 'closed': continue
            last = [m['rule'] for m in t.get('v2_rules', []) if m['rule'] in ('R3', 'R4', 'R6', 'skip', 'no_crop')]
            closed[t.get('closed_by') or ('R6' if (t.get('blocked') or {}).get('reason') == 'panel_modality' else (last[-1] if last else 'other'))] += 1
        R = os.path.join(ROOT, 'results/v07/pilot/reread', P, 'reread.json')
        flags = json.load(open(R)).get('flags', {}) if os.path.exists(R) else {}
        W = os.path.join(ROOT, 'results/v06c/writer', P)
        val = json.load(open(os.path.join(W, 'validation.json'))) if os.path.exists(os.path.join(W, 'validation.json')) else []
        opn = {t['id'] for t in C['traces'] if t['status'] == 'open'}
        mine = [r for r in rows if r['paper'] == P]
        sp = spans[P]
        new.append({'paper': P, 'journal': j, 'year': data.get('year'), 'n_figures': len(mj['figures']),
                    'annotated_share': round(sum(any(cls(t['text']) == 'annotation' for t in c.get('tokens', [])) for c in ocr) / len(ocr), 3) if ocr else '',
                    'graph_nodes': len(g['nodes']), 'graph_spine': sum(1 for n in g['nodes'] if n.get('spine')),
                    'judge_checks': len(pc), 'judge_overturns': sum(1 for x in pc if str(x.get('ruling', '')).lower().startswith('overturn')),
                    'traces_cut': len(C['traces']), 'open': len(opn),
                    'closed_by_rule': '/'.join(f"{k}:{closed.get(k, 0)}" for k in ('R3', 'R4', 'R6', 'skip', 'no_crop')) + (f"/other:{closed['other']}" if closed.get('other') else ''),
                    'written': sum(1 for v in val if v['id'] in opn), 'passed_nets': sum(1 for v in val if v['id'] in opn and not v.get('fails')),
                    'reread_flags': len(flags), 'valid': sum(r['verdict'] == 'valid' for r in mine),
                    'valid_partial': sum(r['verdict'] == 'valid' and bool(r.get('partial')) for r in mine),
                    'text_sufficient': sum(r['verdict'] == 'text-sufficient' for r in mine), 'inspect': sum(r['verdict'] == 'inspect' for r in mine),
                    'inspect_cause': '/'.join(f"{k}:{v}" for k, v in sorted(Counter(r['cause'] for r in mine if r['verdict'] == 'inspect').items(), key=lambda kv: str(kv[0]))),
                    'subagent_dispatches': round(share[P], 1), 'wall_minutes': round((max(s[1] for s in sp) - min(s[0] for s in sp)) / 60, 1) if sp else ''})
    keep = [x for x in prev if x['paper'] not in papers]
    with open(out, 'w', newline='') as fo:
        w = csv.DictWriter(fo, v07.COLS); w.writeheader(); w.writerows(new + keep)
    for r in new: print(r['paper'][:30], r['valid'], r['subagent_dispatches'], r['wall_minutes'])

if __name__ == '__main__': main()
