"""items.py: v2.5 items from graph pairs, in the v5 key format.

  python3 trace_kit_v2p5/items.py build
  python3 trace_kit_v2p5/items.py prompts
  python3 trace_kit_v2p5/items.py collect
  python3 trace_kit_v2p5/items.py depth3

Each item is one pair of observations the graph links, asked so that neither observation answers it
alone. Depth 2 by construction: the unit IS the combination, so there is no step that can be
answered from its own evidence.

The key format is v5's -- combining proposition, limits, scoring target, three labels -- and so is
the rule that "not identifiable" scores only together with the comparison that shows it.

Panels are handed over whole with the five-panel cap, split across the two observations so neither
side is starved: up to 3 from the larger and the rest from the smaller.

Every verdict is model against model.
"""
import json, os, re, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v3'))
from cut_traces import store_for, panel_record, unmath
from support import claim_support

FM = {'SEM', 'TEM', 'STEM', 'XRD', 'XAS', 'ATOM', 'EBSD', 'AFM', 'CT', 'SAXS', 'LEED'}
CAP = 5

QUESTION = {
 'covariation':
   "Across the series reported here, does {qa} move with {qb}? Give the comparison and say what it "
   "implies.",
 'complementary':
   "What does each of these two measurements establish on its own about {topic}, and what does "
   "putting them together add that neither gives alone?",
 'spine_edge':
   "Does the upstream evidence account for the downstream observation about {topic}? Say what the "
   "combination supports and what it leaves open.",
}

DRAFT_ASK = """You are drafting an answer key, not answering a question.

Say what these two pieces of evidence, taken TOGETHER, actually permit -- and no more. The item
exists because neither one answers the question alone, so a key that could be satisfied from one
side is wrong.

A key that overstates is worse than a key that says a thing cannot be determined. "Not
identifiable" is correct and scorable whenever two candidate causes cannot be separated -- but only
stated together with the comparison that shows it.

Give:
1. the combining proposition: what follows from putting the two together. If nothing does, say so
   and set `combines` false.
2. its limits: what the pair does NOT establish. Include any confound -- two variables moving
   together by construction, a quantity set against a different KIND of quantity (a rate against a
   cumulative amount, a test temperature against a service temperature, an absolute against a
   normalized value), or too few points to support a relationship rather than an ordering.
3. `not_identifiable`: if two causes cannot be separated here, name them. Otherwise null.
4. the quantity kind on each side: rate, amount, cumulative or normalized, with units and window.
5. three labels:
   dependency: real if the conclusion needs BOTH observations, none if one suffices.
   inference_validity: "follows", "follows, weakly", or "does not follow".
   causal_strength: descriptive, associative, conditional mechanism, or discriminating.

Reply as JSON only:
{"combines": true or false, "proposition": "...", "limits": ["..."],
 "not_identifiable": "..." or null,
 "quantity": {"a": {"kind": "...", "what": "..."}, "b": {"kind": "...", "what": "..."}},
 "labels": {"dependency": "...", "inference_validity": "...", "causal_strength": "..."}}"""


def fam(t):
    if isinstance(t, list): t = t[0] if t else None
    return (t or '').split(':')[0].upper()


def topic_of(claims, N):
    return ' / '.join((N[c].get('type') or '?') for c in claims if c in N) or 'the sample'


def split_panels(pa, pb, cap=CAP):
    a, b = list(pa), list(pb)
    keep = []
    while len(keep) < cap and (a or b):
        if a and (len(a) >= len(b) or not b): keep.append(a.pop(0))
        elif b: keep.append(b.pop(0))
    return keep, a + b


def build():
    pairs = json.load(open(os.path.join(ROOT, 'results/v2p5/pairs.json')))['pairs']
    seen, items, used_ids = set(), [], set()
    for x in pairs:
        k = (x['paper'], x['kind'], tuple(sorted((x['a'], x['b']))))
        if k in seen: continue
        seen.add(k)
        st = json.load(open(os.path.join(ROOT, 'results/v3', x['paper'], 'stitch.json')))
        gp = os.path.join(ROOT, st['graph'])
        g = json.load(open(gp)); N = {n['id']: n for n in g['nodes']}
        store = store_for(gp)
        if x['kind'] == 'spine_edge':
            oa = (x.get('evidence_a') or [None])[0]; ob = (x.get('evidence_b') or [None])[0]
        else:
            oa, ob = x['a'], x['b']
        if not oa or not ob or oa not in N or ob not in N: continue
        if oa == ob:
            # A spine edge whose upstream and downstream claims are evidenced by the SAME
            # observation is not a pair: there is one measurement, so nothing combines. The
            # drafters said as much, returning combines false on all ten.
            continue
        A, B = N[oa], N[ob]

        def pans(n):
            out = []
            for pid in (n.get('panel_ids') or []):
                r = panel_record(store, pid) or {}
                c = r.get('crop')
                out.append({'panel_id': pid, 'suffix': pid.split('#')[-1],
                            'crop': c if c and os.path.exists(c) else None,
                            'figure': r.get('figure'),
                            'caption_span': ' '.join(unmath(r.get('span') or '').split()) or None})
            return [p for p in out if p['crop']]
        keep, dropped = split_panels(pans(A), pans(B))
        if len(keep) < 2: continue
        ta, tb = fam((A.get('attrs') or {}).get('technique')), fam((B.get('attrs') or {}).get('technique'))
        q = QUESTION[x['kind']].format(
            qa=(A.get('attrs') or {}).get('quantity') or 'the first quantity below',
            qb=(B.get('attrs') or {}).get('quantity') or 'the second quantity below',
            topic=topic_of(x['claims'], N))
        # the id was built from the evidence nodes alone, so two different pairs -- a different
        # claim reached through the same two observations -- collided on one id and overwrote each
        # other's prompt and reply. The claims are part of what makes the item.
        base = f"{x['paper'].split('__')[0][:12].lower()}_{x['kind'][:3]}_{oa}_{ob}"
        iid = base if base not in used_ids else base + '_' + '-'.join(x['claims'][:2])
        n_try = 2
        while iid in used_ids:
            iid = f"{base}_{n_try}"; n_try += 1
        used_ids.add(iid)
        items.append({
            'item': iid,
            'paper': x['paper'], 'generator': x['kind'], 'basis': x['basis'],
            'observation_a': {'node': oa, 'text': A.get('label'), 'technique': (A.get('attrs') or {}).get('technique'), 'family': ta},
            'observation_b': {'node': ob, 'text': B.get('label'), 'technique': (B.get('attrs') or {}).get('technique'), 'family': tb},
            'claims': x['claims'],
            'hidden_key_claims': [N[c].get('label') for c in x['claims'] if c in N],
            'question': q, 'panels': keep, 'panels_dropped_by_cap': [p['suffix'] for p in dropped],
            'depth': 2, 'fm_lane': (ta in FM) or (tb in FM),
            'matmech_hop': x.get('matmech_hop'), 'rel': x.get('rel'),
            'series_len': x.get('series_len'),
        })
    json.dump({'items': items, 'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v2p5/items.json'), 'w'), indent=1)
    g = collections.Counter(i['generator'] for i in items)
    print(f"{len(items)} items from {len(seen)} distinct pairs: {dict(g)}")
    print(f"  papers represented: {len({i['paper'] for i in items})} of 32")
    print(f"  FM lane: {sum(1 for i in items if i['fm_lane'])}")
    print(f"  with a MatMech hop: {sum(1 for i in items if i.get('matmech_hop'))}")
    print(f"  panel cap applied: {sum(1 for i in items if i['panels_dropped_by_cap'])}")


def prompts():
    IT = json.load(open(os.path.join(ROOT, 'results/v2p5/items.json')))['items']
    d = os.path.join(ROOT, 'results/v2p5/draft'); os.makedirs(d, exist_ok=True)
    jobs = []
    for it in IT:
        L = [f"Question as the solver sees it: {it['question']}", "",
             f"Observation A ({it['observation_a']['technique']}): {it['observation_a']['text']}",
             f"Observation B ({it['observation_b']['technique']}): {it['observation_b']['text']}",
             "", f"How the graph links them: {it['basis']}",
             "Panels: " + ', '.join(p['suffix'] for p in it['panels']), "",
             "What the paper concluded, for your reference as the key's author:"]
        for c in it['hidden_key_claims']: L.append(f"  {c}")
        L += ["", DRAFT_ASK]
        f = os.path.join(d, it['item'] + '.txt'); open(f, 'w').write("\n".join(L))
        jobs.append({'id': it['item'], 'agent': 'net-writer', 'prompt': os.path.abspath(f),
                     'out': os.path.abspath(os.path.join(d, it['item'] + '.out.txt'))})
    n = 4
    sz = (len(jobs) + n - 1) // n
    for i in range(n):
        json.dump(jobs[i * sz:(i + 1) * sz],
                  open(os.path.join(ROOT, f'.v07work/batch_v2p5_{i+1}.json'), 'w'), indent=1)
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v2p5_all.json'), 'w'), indent=1)
    print(f"{len(jobs)} draft jobs in {n} batches of about {sz}")


def depth3():
    IT = json.load(open(os.path.join(ROOT, 'results/v2p5/items.json')))['items']
    byobs = collections.defaultdict(list)
    for it in IT:
        byobs[(it['paper'], it['observation_a']['node'])].append(it['item'])
        byobs[(it['paper'], it['observation_b']['node'])].append(it['item'])
    joins = {k: v for k, v in byobs.items() if len(v) > 1}
    npairs = sum(len(v) * (len(v) - 1) // 2 for v in joins.values())
    print(f"observations shared by more than one item: {len(joins)}")
    print(f"item pairs that could join into a depth-3 chain: {npairs}")
    bypaper = collections.Counter(k[0] for k in joins)
    print(f"papers where a depth-3 join exists: {len(bypaper)} of 32")
    json.dump({'shared_observations': {f'{k[0]}::{k[1]}': v for k, v in joins.items()},
               'joinable_item_pairs': npairs},
              open(os.path.join(ROOT, 'results/v2p5/depth3.json'), 'w'), indent=1)


if __name__ == '__main__': {'build': build, 'prompts': prompts, 'collect': None,
                            'depth3': depth3}[sys.argv[1]]()
