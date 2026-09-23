"""survey.py: claims with two or more figure-backed evidence nodes, and the properties each offers.

  python3 trace_kit_v2/survey.py [--out results/v2/candidates.json]

Reads taxonomy/graphs_v07/ and graphs_v06b/ read-only. Writes nothing else.
"""
import argparse, json, os, glob, sys, re
from collections import Counter, defaultdict
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
NO_MODEL = {'ECHEM', 'THERMAL', 'MECH', 'TRANSPORT', 'ASSAY', 'BIO', 'CHROM'}
HAS_MODEL = {'SEM', 'TEM', 'XRD', 'XAS', 'ATOM', 'EBSD', 'AFM', 'CT'}

def fam(t):
    if isinstance(t, list): t = t[0] if t else None
    return (t or '').split(':')[0].upper()


def techs_of(n):
    t = n.get('attrs', {}).get('technique')
    if isinstance(t, list): return [fam(x) for x in t if x]
    return [fam(t)] if t else []

def load(d):
    for f in sorted(glob.glob(os.path.join(ROOT, 'taxonomy', d, '*.json'))):
        b = os.path.basename(f)
        if b.endswith('.build.json') or b.endswith('.pre_judge.json'): continue
        try: g = json.load(open(f))
        except Exception: continue
        if 'nodes' in g: yield b[:-5], d, g

def annotated_panels(P):
    """panel id -> annotation strings, from the paper's ocr.json via the packet convention"""
    j, _, doi = P.partition('__')
    p = os.path.join(ROOT, 'matmech', j, doi, 'panels', 'ocr.json')
    if not os.path.exists(p): return {}
    sys.path.insert(0, os.path.join(ROOT, 'taxonomy'))
    from build_packets_v06 import classify
    out = {}
    for c in json.load(open(p))['crops']:
        ann = [t['text'] for t in c.get('tokens', []) if classify(t['text']) == 'annotation']
        if ann: out[os.path.basename(c['crop'])] = ann
    return out

def main(a):
    rows = []
    for d in ('graphs_v07', 'graphs_v06b'):
      for P, src, g in load(d):
          N = {n['id']: n for n in g['nodes']}
          ev = defaultdict(list)          # claim -> [evidence node]
          rel = defaultdict(dict)
          for e in g['edges']:
              s, t, r = e.get('src'), e.get('dst'), e.get('rel')
              if s in N and t in N:
                  rel[t][s] = r
                  if r in ('evidences', 'qualifies', 'contrasts') and (N[s].get('figs') or N[s].get('panel_ids')):
                      ev[t].append(s)
          for claim, nodes in ev.items():
              figb = [n for n in nodes if (N[n].get('panel_ids') or N[n].get('figs'))]
              if len(figb) < 2: continue
              techs = [fam(N[n].get('attrs', {}).get('technique')) for n in figb]
              techs = [t for t in techs if t]
              pids = [p for n in figb for p in (N[n].get('panel_ids') or [])]
              sup = [N[n].get('attrs', {}).get('image_support') or N[n].get('image_support') for n in figb]
              rels = [rel[claim][n] for n in figb]
              nocrop = [n for n in figb if not (N[n].get('panel_ids') or [])]
              rows.append({
                    'paper': P, 'graphs': src, 'claim': claim, 'claim_type': N[claim].get('type'),
                  'claim_label': (N[claim].get('label') or '')[:160],
                  'spine': bool(N[claim].get('spine')),
                  'evidence': figb, 'n_evidence': len(figb),
                  'techniques': sorted(set(techs)), 'n_techniques': len(set(techs)),
                  'relations': sorted(set(rels)),
                  'supports': sup, 'panel_ids': pids, 'n_panels': len(pids),
                  'no_crop_nodes': nocrop,
                  'has_qualifies_or_contrasts': bool({'qualifies', 'contrasts'} & set(rels)),
                  'oracle_techniques': sorted({t for t in techs if t in NO_MODEL}),
                  'model_techniques': sorted({t for t in techs if t in HAS_MODEL}),
              })
    for r in rows:
        ann = annotated_panels(r['paper'])
        hits = []
        for p in r['panel_ids']:
            suf = p.split('#')[1]
            hits += [f"{suf}:{s}" for f, ss in ann.items() for s in ss if suf.lower() in f.lower()]
        r['annotated_hits'] = sorted(set(hits))[:8]
        r['has_annotated_panel'] = bool(hits)
    json.dump(rows, open(a.out, 'w'), indent=1)
    print(len(rows), 'claims with 2+ figure-backed evidence nodes across',
          len({r['paper'] for r in rows}), 'papers')
    print(' 2+ techniques:', sum(1 for r in rows if r['n_techniques'] >= 2))
    print(' 3+ techniques:', sum(1 for r in rows if r['n_techniques'] >= 3))
    print(' with qualifies/contrasts:', sum(1 for r in rows if r['has_qualifies_or_contrasts']))
    print(' with an oracle technique:', sum(1 for r in rows if r['oracle_techniques']))
    print(' with an annotated panel:', sum(1 for r in rows if r['has_annotated_panel']))
    print(' with a no-crop evidence node:', sum(1 for r in rows if r['no_crop_nodes']))

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--out', default=os.path.join(ROOT, 'results/v2/candidates.json'))
    main(ap.parse_args())
