"""select_v07.py: the 168 new papers for v07 Part C, deterministic.

  python taxonomy/select_v07.py [--n 168] [--out results/v07/selection.json]

Source /home/aid1/panels/fm_supply_papers.json, excluding every paper graphed in v04, v05, v06 or v07 (graphs_v04,
graphs_v05/first100, graphs_v06, graphs_v06b, graphs_v07, and the Part B list). Eligible:
  - SEM confirmed on an accepted panel ("panels" in sem_sources)
  - at least two other modalities figure-backed ("panels" in their modality_sources)
  - 4 to 12 figures, at least 60% of them tier A or B (figures_AB / n_figures)
Journal quota: proportional to the eligible pool (largest remainder), at least 3 per journal (or all it has).
Within a journal: year descending, then DOI. Recorded, not filtered: journal, year, figure count, modality set,
annotated share (share of OCR'd crops carrying a word or phrase that is not a letter, tick, unit, axis title or scale bar).
"""
import argparse, glob, json, os, sys
from collections import Counter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'taxonomy'))
from build_packets_v06 import classify

def graphed():
    out = set()
    for d in ('graphs_v04', 'graphs_v05/first100', 'graphs_v06', 'graphs_v06b', 'graphs_v07'):
        for p in glob.glob(os.path.join(ROOT, 'taxonomy', d, '*.json')):
            if p.endswith(('.build.json',)): continue
            try: pid = json.load(open(p)).get('paper_id') or ''
            except Exception: continue
            if pid: out.add(pid.split('/')[-1])
            out.add(os.path.basename(p)[:-5].partition('__')[2])
    for l in open(os.path.join(ROOT, 'taxonomy', 'v07', 'partB', 'papers.txt')): out.add(l.strip().split('/')[-1])
    return {x for x in out if x}

def yr(y):
    # 'Unknown Year' and missing years sort last
    return int(y) if str(y).isdigit() else 0

def annotated_share(journal, doi):
    p = os.path.join(ROOT, 'matmech', journal, doi, 'panels', 'ocr.json')
    if not os.path.exists(p): return None
    crops = json.load(open(p)).get('crops', [])
    if not crops: return None
    return round(sum(any(classify(t['text']) == 'annotation' for t in c.get('tokens', [])) for c in crops) / len(crops), 3)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, default=168)
    ap.add_argument('--out', default=os.path.join(ROOT, 'results', 'v07', 'selection.json')); a = ap.parse_args()
    supply = json.load(open('/home/aid1/panels/fm_supply_papers.json')); done = graphed()
    def figmods(r): return sorted(m for m, s in r['modality_sources'].items() if 'panels' in s)
    pool = [r for r in supply if r['doi'] not in done and 'panels' in r['sem_sources'] and 4 <= r['n_figures'] <= 12
            and r['figures_AB'] / r['n_figures'] >= 0.6 and len([m for m in figmods(r) if m != 'electron micrograph']) >= 2
            and os.path.exists(os.path.join(ROOT, 'matmech', r['journal'], r['doi'], 'panels', 'match.json'))]
    by = Counter(r['journal'] for r in pool); J = sorted(by)
    # quota: journals whose proportional share falls below min(3, available) are fixed there; the rest of the n is
    # shared in proportion to the pool among the others (largest remainder), repeating until no share falls below its floor
    floor = {j: min(3, by[j]) for j in J}; fixed = {}
    while True:
        free = [j for j in J if j not in fixed]; n_free = a.n - sum(fixed.values()); tot = sum(by[j] for j in free)
        share = {j: n_free * by[j] / tot for j in free}
        low = [j for j in free if share[j] < floor[j] or share[j] > by[j]]
        if not low: break
        for j in low: fixed[j] = floor[j] if share[j] < floor[j] else by[j]
    q = dict(fixed); q.update({j: int(share[j]) for j in free}); left = a.n - sum(q.values())
    for j in sorted(free, key=lambda j: (-(share[j] - int(share[j])), j)):
        if left <= 0: break
        q[j] += 1; left -= 1
    sel = []
    for j in J:
        rs = sorted((r for r in pool if r['journal'] == j), key=lambda r: (-yr(r['year']), r['doi']))[:q[j]]
        for r in rs:
            sel.append({'paper': f"{j}/{r['doi']}", 'journal': j, 'year': r['year'], 'n_figures': r['n_figures'],
                        'figures_AB': r['figures_AB'], 'modalities': figmods(r), 'annotated_share': annotated_share(j, r['doi'])})
    # blocks of 24 interleave journals so each block spans the set: round-robin over journals in pool order
    order, rest = [], {j: [s for s in sel if s['journal'] == j] for j in J}
    while any(rest.values()):
        for j in J:
            if rest[j]: order.append(rest[j].pop(0))
    for i, s in enumerate(order): s['rank'] = i + 1; s['block'] = i // 24 + 1
    json.dump({'source': '/home/aid1/panels/fm_supply_papers.json', 'n_supply': len(supply), 'excluded_graphed': len(done),
               'eligible': len(pool), 'eligible_by_journal': dict(by), 'quota': q,
               'rule': __doc__.split('\n\n', 1)[1].strip(), 'papers': order}, open(a.out, 'w'), indent=1)
    print(len(pool), 'eligible;', len(order), 'selected;', q)

if __name__ == '__main__': main()
