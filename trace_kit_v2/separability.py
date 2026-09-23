"""separability.py: does the contribution label separate, or is supports_part a constant?

  python3 trace_kit_v2/separability.py sample    60 edges, stratified, -> .v07work/sep_inputs.jsonl
  python3 trace_kit_v2/separability.py collect   -> results/v2/separability.json

Strata (the brief):
  single_evidence  claims with exactly ONE figure-backed evidence node: one panel is all there is
  reference_match  evidence read against a reference: XRD/SAED with a PDF or reference match, an XPS
                   binding-energy assignment, a lattice-spacing match -- where one panel plausibly settles it
  random_rest      drawn at random from the remaining pool

If establishes appears readily in the first two, the label separates and the five cases were the hard
end. If it is near-absent there too, the label is degenerate and labelling the pool buys a constant.
"""
import json, os, random, re, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contrib import scrub, guard, MAP, parse

ORPHAN = re.compile(r'\b[a-l]\d\b')          # residual bare panel letters: a1, c1, g2, h1


def readable(obs):
    """an observation that survives scrubbing as a sentence. Dense panel-by-panel readings scrub to
    nonsense ('the data/the data, g1/g2, h1') and a label over nonsense is worthless, so they are
    dropped from the sample and replaced rather than dispatched."""
    t = scrub(obs)
    if len(t) < 40: return False, 'too short after scrubbing'
    if len(ORPHAN.findall(t)) >= 2: return False, 'residual bare panel letters after scrubbing'
    if t.lower().count('the data') >= 3: return False, 'scrubbing replaced most of the sentence'
    return True, None
SEED = 0
N = 20
REF = re.compile(r'\b(PDF[- ]?\d|JCPDS|ICDD|reference (?:pattern|spectrum|card)|indexed to|indexes to|'
                 r'matches? (?:the )?(?:reference|standard|literature)|d[- ]spacing|lattice (?:spacing|fringe)|'
                 r'binding energy|eV\b.*\bassigned|assigned to .*\bat \d|SAED|standard card)', re.I)
REF_TECH = ('XRD', 'SAED', 'XPS', 'TEM:SAED', 'TEM:HRTEM')


def fam(t):
    if isinstance(t, list): t = t[0] if t else None
    return (t or '').split(':')[0].upper()


def edges():
    """every (claim, figure-backed evidence node) edge in the graphs, with what we need to stratify"""
    out = []
    for d in ('graphs_v07', 'graphs_v06b'):
        for f in sorted(glob.glob(os.path.join(ROOT, 'taxonomy', d, '*.json'))):
            b = os.path.basename(f)
            if b.endswith(('.build.json', '.pre_judge.json')): continue
            try: g = json.load(open(f))
            except Exception: continue
            if 'nodes' not in g: continue
            N_ = {n['id']: n for n in g['nodes']}
            ev = {}
            for e in g['edges']:
                s, t, r = e.get('src'), e.get('dst'), e.get('rel')
                if s in N_ and t in N_ and r in ('evidences', 'qualifies', 'contrasts', 'rules_out') \
                   and (N_[s].get('panel_ids') or N_[s].get('figs')):
                    ev.setdefault(t, []).append((s, r))
            for claim, lst in ev.items():
                for s, r in lst:
                    n = N_[s]
                    tech = n.get('attrs', {}).get('technique')
                    out.append({'paper': b[:-5], 'graphs': d, 'claim_id': claim, 'node': s, 'relation': r,
                                'technique': tech, 'family': fam(tech),
                                'image_support': n.get('image_support'),
                                'n_evidence_on_claim': len(lst),
                                'claim_text': N_[claim].get('label') or '',
                                'observation': n.get('label') or ''})
    keep, dropped = [], []
    for e in out:
        if not (e['claim_text'] and e['observation']): continue
        ok, why = readable(e['observation'])
        (keep if ok else dropped).append(e if ok else dict(e, drop_reason=why))
    globals()['_DROPPED'] = dropped
    return keep


def sample():
    E = edges()
    rnd = random.Random(SEED)
    single = [e for e in E if e['n_evidence_on_claim'] == 1]
    ref = [e for e in E if e['n_evidence_on_claim'] > 1
           and (REF.search(e['observation']) or (e['family'] in REF_TECH and REF.search(e['observation'] or '')))
           or (e['family'] in ('XRD', 'SAED') and REF.search(e['observation'] or ''))]
    if len(ref) < N:   # widen: any XRD/SAED/XPS identity read on a multi-evidence claim
        extra = [e for e in E if e['n_evidence_on_claim'] > 1 and e['family'] in REF_TECH and e not in ref]
        rnd.shuffle(extra); ref = ref + extra[:N - len(ref)]
    rest = [e for e in E if e not in single and e not in ref]
    rnd.shuffle(single); rnd.shuffle(ref); rnd.shuffle(rest)
    picked = ([dict(e, stratum='single_evidence') for e in single[:N]]
              + [dict(e, stratum='reference_match') for e in ref[:N]]
              + [dict(e, stratum='random_rest') for e in rest[:N]])
    work = os.path.join(ROOT, '.v07work/sep'); os.makedirs(work, exist_ok=True)
    jobs, leaks = [], []
    for i, e in enumerate(picked):
        e['uid'] = f"sep{i:03d}"
        t = (f"Claim: {e['claim_text']}\n\nObservation: {scrub(e['observation'])}\n\n"
             f"Relation: the observation {e['relation']} the claim.")
        bad = guard(t)
        if bad: leaks.append((e['uid'], bad)); continue
        p = os.path.join(work, e['uid'] + '.txt'); open(p, 'w').write(t)
        jobs.append({'id': f"sep/{e['uid']}/contrib", 'agent': 'net-contrib', 'prompt': p,
                     'out': os.path.join(work, e['uid'] + '.out.txt')})
    with open(os.path.join(ROOT, '.v07work/sep_inputs.jsonl'), 'w') as f:
        for e in picked: f.write(json.dumps(e) + '\n')
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_sep.json'), 'w'), indent=1)
    json.dump({'papers': ['sep'], 'stage': 'contrib'}, open(os.path.join(ROOT, '.v07work/batch_sep.meta.json'), 'w'), indent=1)
    import collections
    dr = globals().get('_DROPPED', [])
    print(f"pool: {len(E)} figure-backed evidence edges usable, {len(dr)} dropped as unreadable after scrubbing")
    import collections as _c
    if dr: print("   drop reasons:", dict(_c.Counter(d['drop_reason'] for d in dr)))
    print(f"  single_evidence available {len(single)}, reference_match {len(ref)}, rest {len(rest)}")
    print(f"sampled {len(picked)}: " + str(dict(collections.Counter(e['stratum'] for e in picked))))
    print(f"{len(jobs)} prompts pass the guard")
    if leaks:
        print("LEAK, refusing to dispatch:", leaks[:5]); sys.exit(2)


def collect():
    import collections
    rows = [json.loads(l) for l in open(os.path.join(ROOT, '.v07work/sep_inputs.jsonl'))]
    work = os.path.join(ROOT, '.v07work/sep')
    out = []
    for e in rows:
        f = os.path.join(work, e['uid'] + '.out.txt')
        j = parse(open(f).read()) if os.path.exists(f) else None
        if not j: continue
        c = (j.get('contribution') or '').strip().lower().replace(' ', '_')
        out.append({**e, 'observation_as_labelled': scrub(e['observation']),
                    'contribution': c, 'mapped_support': MAP.get(c), 'why': j.get('why'),
                    'unsettled': j.get('unsettled') or []})
    by = collections.defaultdict(collections.Counter)
    for o in out: by[o['stratum']][o['contribution']] += 1
    res = {'n': len(out), 'by_stratum': {k: dict(v) for k, v in by.items()},
           'establishes_rate': {k: round(v.get('establishes', 0) / sum(v.values()), 3) for k, v in by.items()},
           'note': 'Every verdict is model against model.'}
    json.dump({'summary': res, 'labels': out}, open(os.path.join(ROOT, 'results/v2/separability.json'), 'w'), indent=1)
    for k, v in by.items():
        tot = sum(v.values())
        print(f"  {k:16s} n={tot:2d}  " + "  ".join(f"{a}={n}" for a, n in v.most_common())
              + f"   establishes {v.get('establishes',0)/tot:.0%}")
    return res


if __name__ == '__main__': {'sample': sample, 'collect': collect}[sys.argv[1]]()
