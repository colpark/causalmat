"""decompose.py: model-based decomposition of each hop's effect into our spine claims.

  python3 trace_kit_v3/decompose.py prompts   one net-decompose job per hop (and per chain link)
  python3 trace_kit_v3/decompose.py collect   -> results/v3/<paper>/decompose.json

net-decompose is a MATCHER. It may see MatMech spans; its output feeds attachment and chaining only
and never reaches a solver prompt. The lexical result is kept beside it, never overwritten.
"""
import json, os, re, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, '.v07work/decomp')
PAPERS = ['Rare_Metals__s12598-012-0515-6', 'Biomaterials__j.biomaterials.2011.11.042',
          'Advanced_Functional_Materials__10.1002_adfm.202008088',
          'Nano_Letters__10.1021_acs.nanolett.6b04294',
          'Acta_Materialia__10.1016_j.actamat.2021.116797']


def claims_of(paper):
    st = json.load(open(os.path.join(ROOT, 'results/v3', paper, 'stitch.json')))
    g = json.load(open(os.path.join(ROOT, st['graph'])))
    cs = [n for n in g['nodes'] if n.get('spine') and not (n.get('type') or '').startswith('OBS')]
    if not cs: cs = [n for n in g['nodes'] if not (n.get('type') or '').startswith('OBS')]
    return g, cs


def text(effect, cs):
    L = [f"Effect: {effect}", "", "Claims:"]
    for c in cs:
        L.append(f"- {c['id']}: {c.get('label')}")
    return "\n".join(L)


def prompts():
    os.makedirs(WORK, exist_ok=True)
    jobs = []
    for p in PAPERS:
        hops = json.load(open(os.path.join(ROOT, 'results/v3', p, 'hops.json')))
        _, cs = claims_of(p)
        for h in hops['hops']:
            sp = h['_matmech_span_DO_NOT_PROMPT']
            for kind, span in (('effect', sp['effect']), ('cause', sp['cause'])):
                if not span: continue
                f = os.path.join(WORK, f"{p}.{h['id']}.{kind}.txt")
                open(f, 'w').write(text(span, cs))
                jobs.append({'id': f"{p}/{h['id']}/{kind}", 'agent': 'net-decompose',
                             'prompt': f, 'out': os.path.join(WORK, f"{p}.{h['id']}.{kind}.out.txt")})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_decomp.json'), 'w'), indent=1)
    json.dump({'papers': PAPERS, 'stage': 'decompose'},
              open(os.path.join(ROOT, '.v07work/batch_decomp.meta.json'), 'w'), indent=1)
    import collections
    print(f"{len(jobs)} decomposition jobs over {len(PAPERS)} papers")
    print(dict(collections.Counter(j['id'].split('/')[0][:28] for j in jobs)))


def parse(t):
    m = re.search(r'\{.*\}', t or '', re.S)
    if not m: return None
    try: return json.loads(m.group(0))
    except Exception: return None


def collect():
    tot_m = tot_h = 0
    for p in PAPERS:
        hops = json.load(open(os.path.join(ROOT, 'results/v3', p, 'hops.json')))
        g, cs = claims_of(p)
        ids = {c['id'] for c in cs}
        out = {}
        for h in hops['hops']:
            rec = {}
            for kind in ('effect', 'cause'):
                f = os.path.join(WORK, f"{p}.{h['id']}.{kind}.out.txt")
                j = parse(open(f).read()) if os.path.exists(f) else None
                ms = [m for m in ((j or {}).get('matches') or [])
                      if m.get('claim') in ids and m.get('same_fact') is not False]
                rec[kind] = {'claims': [m['claim'] for m in ms],
                             'why': {m['claim']: m.get('why') for m in ms},
                             'unmatched_parts': (j or {}).get('unmatched_parts') or [],
                             'parsed': bool(j)}
            out[h['id']] = rec
            tot_m += len(rec['effect']['claims']); tot_h += 1
        json.dump({'paper': p, 'n_spine_claims': len(cs), 'hops': out,
                   'note': 'net-decompose is a matcher; its output never reaches a solver prompt. '
                           'Every verdict is model against model.'},
                  open(os.path.join(ROOT, 'results/v3', p, 'decompose.json'), 'w'), indent=1)
        print(f"  {p[:44]:44s} {len(cs):2d} claims, effect matches: "
              + ", ".join(f"{k}={len(v['effect']['claims'])}" for k, v in out.items()))
    print(f"\n{tot_m} effect matches over {tot_h} hops = {tot_m/tot_h:.2f} per hop "
          f"(stop rule: more than 3)")


if __name__ == '__main__': {'prompts': prompts, 'collect': collect}[sys.argv[1]]()
