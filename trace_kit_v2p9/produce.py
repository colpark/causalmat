"""produce.py: v2.9 Step 2 -- draft each key, then split it into checked claims.

  python3 -m trace_kit_v2p9.produce draft    the v2.7 drafter on all 88 pairs
  python3 -m trace_kit_v2p9.produce tag      v2.8's splitter on each drafted key
  python3 -m trace_kit_v2p9.produce check    v2.8's tag checker
  python3 -m trace_kit_v2p9.produce collect  keep only agreed tags; drop items with none

Three calls per pair, every one on Sonnet. Haiku failed all three calibration bars in Step 1,
so there is no cheap path here and the report says so rather than pretending otherwise.

The prompts are the ones already validated: the v2.7 DRAFT_ASK for the key, and v2.8's
SPLIT_ASK and CHECK_ASK for the claims. Nothing about them is new in this run. What is new is
that they run on 88 pairs from 19 papers none of which were in the pilot, so the pass rates
that come out of steps 3 and 4 are out-of-sample.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402

# by file path, not by name: trace_kit_v5 also ships an `items` module and whichever sits
# earlier on sys.path wins, which is how this first tried to import the v5 drafter's rules.
import importlib.util as _ilu  # noqa: E402
_sp = _ilu.spec_from_file_location('v2p5_items', R('trace_kit_v2p5', 'items.py'))
_v25 = _ilu.module_from_spec(_sp); _sp.loader.exec_module(_v25)
DRAFT_ASK, parse_draft = _v25.DRAFT_ASK, _v25.parse_draft
from trace_kit_v2p8.partA import SPLIT_ASK, CHECK_ASK  # noqa: E402
from trace_kit_v2p7.derived_input import QUESTION  # noqa: E402

# the same recipe runs on the depth-2 pairs and on the depth-3 next links; the
# source file and an output suffix are the only difference.
SRC = os.environ.get('V2P9_SRC', 'results/v2p9/pairs.json')
TAG = os.environ.get('V2P9_TAG', '')

DRAFT = R('results/v2p9/draft' + TAG)
SPLIT = R('results/v2p9/split' + TAG)
CHECK = R('results/v2p9/check' + TAG)


def pairs():
    return json.load(open(R(SRC)))['pairs_out']


def graph_nodes(paper, _c={}):
    if paper not in _c:
        gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
        _c[paper] = {n['id']: n for n in json.load(open(R(gp)))['nodes']}
    return _c[paper]


def draft():
    os.makedirs(DRAFT, exist_ok=True)
    P = pairs(); jobs = []
    for x in P:
        N = graph_nodes(x['paper'])
        x['question'] = QUESTION.format(
            topic=(N.get(x['target_claim'], {}).get('type') or 'the sample'))
        lim = '\n'.join('    - ' + t for t in x['input_limits']) or '    - none recorded'
        L = [f"Question as the solver sees it: {x['question']}", '',
             'Observation A is not a raw measurement here. It is a result already established '
             'by an earlier step, handed to this step as settled:',
             f"  {x['input_result']}",
             '  The qualifications recorded on that earlier result:', lim, '',
             f"Observation B ({x['new_observation']['technique']}): {x['new_observation']['text']}",
             '', 'How the graph links them: the earlier result concludes a claim that points to '
                 f"B's claim through a {x['edge']} edge",
             'Panels: ' + ', '.join(p['suffix'] for p in x['panels']), '',
             "What the paper concluded, for your reference as the key's author:",
             f"  {(N.get(x['target_claim']) or {}).get('label')}", '', DRAFT_ASK]
        f = os.path.join(DRAFT, x['item'] + '.txt'); open(f, 'w').write('\n'.join(L))
        jobs.append({'id': x['item'], 'agent': 'net-writer', 'prompt': f,
                     'out': os.path.join(DRAFT, x['item'] + '.out.txt')})
    d = json.load(open(R(SRC))); d['pairs_out'] = P
    json.dump(d, open(R(SRC), 'w'), indent=1)
    json.dump(jobs, open(R('results/v2p9/draft_jobs%s.json' % TAG), 'w'), indent=1)
    print(f'{len(jobs)} draft prompts')
    return jobs


def keys():
    out = {}
    for x in pairs():
        f = os.path.join(DRAFT, x['item'] + '.out.txt')
        if not os.path.exists(f): continue
        k = parse_draft(open(f).read())
        if k and 'proposition' in k and (k.get('proposition') or '').strip():
            out[x['item']] = k
    return out


def tag():
    os.makedirs(SPLIT, exist_ok=True)
    K = keys(); jobs = []
    for x in pairs():
        if x['item'] not in K: continue
        body = SPLIT_ASK.format(inp=x['input_result'], obs=x['new_observation']['text'],
                                prop=K[x['item']]['proposition'])
        f = os.path.join(SPLIT, x['item'] + '.txt'); open(f, 'w').write(body)
        jobs.append({'id': x['item'], 'agent': 'net-writer', 'prompt': f,
                     'out': os.path.join(SPLIT, x['item'] + '.out.txt')})
    json.dump(K, open(R('results/v2p9/keys%s.json' % TAG), 'w'), indent=1)
    json.dump(jobs, open(R('results/v2p9/tag_jobs%s.json' % TAG), 'w'), indent=1)
    print(f'{len(jobs)} tag prompts from {len(K)} drafted keys of {len(pairs())} pairs')
    return jobs


def claims_of(item, d=None):
    f = os.path.join(d or SPLIT, item + '.out.txt')
    if not os.path.exists(f): return None
    o = obj(open(f).read(), 'claims')
    if not o: return None
    out = [{'claim': (c.get('claim') or '').strip(),
            'tag': (c.get('tag') or '').strip().lower()}
           for c in (o.get('claims') or [])]
    out = [c for c in out if c['claim'] and c['tag'] in ('input', 'observation', 'combined')]
    return out or None


def check():
    os.makedirs(CHECK, exist_ok=True)
    jobs, miss = [], []
    for x in pairs():
        cs = claims_of(x['item'])
        if not cs: miss.append(x['item']); continue
        listing = '\n'.join(f"{i}. [{c['tag']}] {c['claim']}" for i, c in enumerate(cs, 1))
        body = CHECK_ASK.format(inp=x['input_result'], obs=x['new_observation']['text'],
                                claims=listing)
        f = os.path.join(CHECK, x['item'] + '.txt'); open(f, 'w').write(body)
        jobs.append({'id': x['item'], 'agent': 'net-contrib', 'prompt': f,
                     'out': os.path.join(CHECK, x['item'] + '.out.txt')})
    json.dump(jobs, open(R('results/v2p9/check_jobs%s.json' % TAG), 'w'), indent=1)
    print(f'{len(jobs)} check prompts, {len(miss)} pairs with no usable split')
    return jobs


def collect():
    K = keys(); out = {}
    tot = agreed = 0
    for x in pairs():
        it = x['item']
        cs = claims_of(it) or []
        f = os.path.join(CHECK, it + '.out.txt')
        o = obj(open(f).read(), 'rulings') if os.path.exists(f) else None
        rul = {int(r['n']): r for r in (o or {}).get('rulings', [])
               if str(r.get('n', '')).strip().isdigit()}
        kept, dropped = [], []
        for i, c in enumerate(cs, 1):
            v = (rul.get(i) or {}).get('verdict', '').strip().lower()
            tot += 1
            if v == 'agree': agreed += 1; kept.append(c)
            else: dropped.append({**c, 'verdict': v or 'no ruling',
                                  'correct_tag': (rul.get(i) or {}).get('correct_tag')})
        lims = [{'claim': str(t).strip(), 'tag': 'limit'}
                for t in ((K.get(it) or {}).get('limits') or []) if str(t).strip()]
        nc = sum(1 for c in kept if c['tag'] == 'combined')
        out[it] = {'paper': x['paper'], 'upstream': x['upstream_item'],
                   'drafted': it in K, 'proposed': len(cs), 'kept': kept, 'dropped': dropped,
                   'limits': lims, 'n_combined': nc, 'n_limit': len(lims),
                   'labels': (K.get(it) or {}).get('labels'),
                   'combines': (K.get(it) or {}).get('combines'),
                   'alive': bool(nc)}
    alive = [k for k, v in out.items() if v['alive']]
    res = {'note': 'v2.9 Step 2. Draft, tag, check. Sonnet throughout.',
           'pairs': len(pairs()), 'drafted': len(K),
           'with_a_split': sum(1 for v in out.values() if v['proposed']),
           'tag_agreement': round(agreed / tot, 3) if tot else None,
           'tags_agreed': agreed, 'tags_proposed': tot,
           'alive': len(alive), 'dropped_no_combined_claim': len(out) - len(alive),
           'combined_hist': dict(sorted(collections.Counter(
               v['n_combined'] for v in out.values()).items())),
           'per_paper_alive': dict(collections.Counter(
               v['paper'] for v in out.values() if v['alive'])),
           'items': out}
    json.dump(res, open(R('results/v2p9/step2%s.json' % TAG), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items()
                      if k not in ('items', 'per_paper_alive')}, indent=1))
    return res


if __name__ == '__main__':
    {'draft': draft, 'tag': tag, 'check': check, 'collect': collect}[sys.argv[1]]()
