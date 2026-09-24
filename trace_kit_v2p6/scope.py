"""scope.py: v2.6 step 4 -- does the qualified upstream result support what the next step needs?

  python3 -m trace_kit_v2p6.scope build     write one prompt per join
  python3 -m trace_kit_v2p6.scope collect   read the replies, write results/v2p6/scope.json

v2.5 joined two items whenever they named the same claim id. Sharing an id is not sharing a
result: the downstream may need the claim for a different specimen, a different material state
or a different quantity than the upstream actually established once its own limits are applied.
This asks that, and only that.

The agent gets two texts and nothing else. No claim ids, no paper-level claim text, no item ids,
no paper or journal name, no panels, no generator label. A scrub runs over both texts and the
prompt is refused if a bare node id survives it, so an id cannot reach the agent by accident.

  TEXT 1  the upstream item's key proposition with the limits its drafter attached.
  TEXT 2  the premise the next step takes as given. For a v5 backbone item that is its own
          `previous_output` field, which is literally the result it was handed. For a v2.5
          pairwise item it is the observation the item reads on the join side -- the one whose
          node evidences the join claim -- plus the question the item then asks.

Every verdict is model against model.
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v3'))
sys.path.insert(0, R('trace_kit_v2p5'))
from support import claim_support  # noqa: E402
from pages import obj  # noqa: E402

OUT = R('results/v2p6/scope')
VERDICTS = ('supports', 'supports only narrower', 'incompatible')

# node ids (n7, o12, a13, b17), MatMech hop ids (M3), and item-id fragments
ID = re.compile(r'\b(?:[noab]\d+[a-z]?|M\d+|s\d+_\d+)\b')


def scrub(t):
    """ids out. The agent must judge two texts, not recognise two nodes."""
    return ID.sub('[id]', t or '')


def items():
    D = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    V5 = {i['item']: i for i in json.load(open(R('results/v5/items.json')))['items']}
    return D, V5, {**V5, **D}


_sup = {}


def sup(paper):
    if paper not in _sup:
        gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
        _sup[paper] = claim_support(json.load(open(R(gp))))
    return _sup[paper]


def upstream_text(it):
    k = it.get('key') or {}
    p = (k.get('proposition') or '').strip()
    lim = [str(x).strip() for x in (k.get('limits') or []) if str(x).strip()]
    if not p: return None
    s = 'TEXT 1 -- an earlier result, with the qualifications its author attached to it\n\n' + p
    if lim:
        s += '\n\nQualifications on that result:\n' + '\n'.join('  - ' + x for x in lim)
    else:
        s += '\n\nQualifications on that result: none were recorded.'
    return s


def shared_obs(up, dn, on_claim, D):
    """does the downstream read the very observation the upstream read on the join side?

    118 of the 121 v2.5-to-v2.5 joins do. That is how v2.5 built them: a join is a shared claim
    id, and the downstream reaches that claim through the same observation. So the premise the
    downstream needs is usually a measurement the upstream item already quotes, which is why
    the scope check can only be one of three gates and not the whole test.
    """
    if dn['item'] not in D: return None
    via = set((sup(dn['paper']).get(on_claim) or {}).get('via') or [])
    dl = {dn[k]['node'] for k in ('observation_a', 'observation_b') if dn[k]['node'] in via}
    ul = ({up[k]['node'] for k in ('observation_a', 'observation_b')} if up['item'] in D
          else {o.get('node') for o in (up.get('observations') or []) if isinstance(o, dict)})
    return bool(dl & ul)


def premise_text(it, on_claim, D):
    """what the next step takes as given, in the next step's own words"""
    if it['item'] not in D and it.get('previous_output'):
        given = str(it['previous_output']).strip()
        asks = str(it.get('property') or '').strip()
        src = 'previous_output'
    else:
        via = set((sup(it['paper']).get(on_claim) or {}).get('via') or [])
        obs = [it[k]['text'] for k in ('observation_a', 'observation_b')
               if it.get(k) and it[k].get('node') in via]
        if not obs: return None, None
        given = ' / '.join(o.strip() for o in obs)
        asks = str(it.get('question') or '').strip()
        src = 'join-side observation'
    s = ('TEXT 2 -- the premise a later step takes as given before it reasons any further\n\n'
         + given)
    if asks: s += '\n\nThe later step then asks: ' + asks
    return s, src


TASK = """You are given two texts from a chain of reasoning about one set of experiments. Judge one thing only: whether the first text, read together with its own qualifications, supports the second.

{t1}

{t2}

Does TEXT 1, as qualified, support TEXT 2 -- the same sample or specimen set, the same material state, the same measurement scope and conditions, the same quantity?

Choose exactly one:

  supports                 TEXT 1, with its qualifications applied, establishes what TEXT 2 takes as given. Sample, state, scope and quantity all line up.
  supports only narrower   TEXT 1 establishes something real, but narrower than TEXT 2 assumes: a subset of the specimens, a different state or condition, a weaker or more hedged version of the quantity, or a qualification TEXT 2 quietly sets aside.
  incompatible             TEXT 1 does not bear on TEXT 2, or bears on it the wrong way: a different quantity, a different specimen, a different experiment, or a contradiction.

Judge the texts as written. Do not credit either text with anything it does not say, and do not repair a mismatch by assuming the two must be about the same thing because they appear in one chain.

Return JSON and nothing else:
{{"verdict": "supports" | "supports only narrower" | "incompatible",
 "mismatch": "sample" | "state" | "scope" | "quantity" | "none",
 "why": "at most 60 words, quoting the words in TEXT 1 and in TEXT 2 that decide it"}}"""


def build():
    P = json.load(open(R('results/v2p6/pruned.json')))
    D, V5, ALL = items()
    os.makedirs(OUT, exist_ok=True)
    jobs, skipped = [], []
    for j in P['joins']:
        k = f"{j['from']}__{j['to']}"
        up, dn = ALL[j['from']], ALL[j['to']]
        t1 = upstream_text(up)
        t2, src = premise_text(dn, j['on_claim'], D)
        if not t1 or not t2:
            skipped.append({'join': k, 'why': 'no upstream key' if not t1 else 'no premise'})
            continue
        body = TASK.format(t1=scrub(t1), t2=scrub(t2))
        leak = ID.findall(body)
        assert not leak, (k, leak[:5])
        f = os.path.join(OUT, k + '.txt')
        open(f, 'w').write(body)
        jobs.append({'id': k, 'agent': 'net-judge', 'prompt': f,
                     'out': os.path.join(OUT, k + '.out.txt'), '_premise_from': src,
                     '_shared_obs': shared_obs(up, dn, j['on_claim'], D)})
    json.dump(jobs, open(R('results/v2p6/scope_jobs.json'), 'w'), indent=1)
    json.dump(skipped, open(R('results/v2p6/scope_skipped.json'), 'w'), indent=1)
    print(f'{len(jobs)} scope prompts, {len(skipped)} skipped')
    return jobs


def vn(v):
    v = (v or '').strip().lower()
    if 'incompat' in v: return 'incompatible'
    if 'narrow' in v: return 'supports only narrower'
    if 'support' in v: return 'supports'
    return None


def collect():
    jobs = json.load(open(R('results/v2p6/scope_jobs.json')))
    out, miss = {}, []
    for j in jobs:
        if not os.path.exists(j['out']): miss.append(j['id']); continue
        o = obj(open(j['out']).read(), 'verdict')
        v = vn((o or {}).get('verdict'))
        if not v: miss.append(j['id']); continue
        out[j['id']] = {'verdict': v, 'mismatch': (o.get('mismatch') or '').strip().lower(),
                        'why': (o.get('why') or '').strip(), 'premise_from': j['_premise_from'],
                        'shared_obs': j['_shared_obs']}
    import collections
    res = {'note': 'v2.6 step 4. One net-judge call per join, two texts only.',
           'joins': len(jobs), 'ruled': len(out), 'unruled': miss,
           'verdicts': dict(collections.Counter(v['verdict'] for v in out.values())),
           'mismatch': dict(collections.Counter(v['mismatch'] for v in out.values())),
           'by_shared_obs': {str(k): dict(collections.Counter(
               x['verdict'] for x in out.values() if x['shared_obs'] is k))
               for k in (True, False, None)},
           'seams': out}
    json.dump(res, open(R('results/v2p6/scope.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'seams'}, indent=1))
    return res


if __name__ == '__main__':
    {'build': build, 'collect': collect}[sys.argv[1]]()
