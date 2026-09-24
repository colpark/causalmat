"""compose.py: chains from the v5 backbone plus the v2.5 pairs.

  python3 trace_kit_v2p5/compose.py build      backbone, attachment, composition, convergence
  python3 trace_kit_v2p5/compose.py prompts    audit jobs for each join and each convergence item
  python3 trace_kit_v2p5/compose.py collect

The v5 survivors give causal DIRECTION, because a MatMech hop link was confirmed over them. The
v2.5 pairs give COVERAGE, because they come from our own graph and exist in all 32 papers. Composing
them keeps the direction where it was earned and uses the pairs everywhere else.

Direction, per item kind:
  v5 backbone     input is the previous step's claims, conclusion is its own
  spine_edge      explicit: a -causes/explains-> b, so input a, conclusion b
  complementary   both observations evidence ONE claim, so it has a conclusion and no input. It can
  covariation     open a chain or attach to a node; it cannot be joined onto.

A join is item X to item Y when X's conclusion claim is Y's input claim.

Rejections, in order:
  loop           X feeds Y and Y feeds X, directly or through a cycle
  split          two chains share a MatMech hop, so they are one chain cut in two; the shorter goes
  dropped_limits the joined claim does not carry the upstream item's limits (audited, not computed)

Depth counts derived conclusions only: items that combine two observations. An attachment adds
coverage at a node without adding depth.

Every verdict is model against model.
"""
import json, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def load():
    V5 = {i['item']: i for i in json.load(open(os.path.join(ROOT, 'results/v5/items.json')))['items']}
    S = [r['item'] for r in json.load(open(os.path.join(ROOT, 'results/v5/survival_v5b.json')))['surviving']]
    P = json.load(open(os.path.join(ROOT, 'results/v2p5/items.json')))['items']
    return V5, S, P


def direction(it):
    """(input claims, conclusion claims) or (None, conclusion) for a pair with no upstream"""
    if it.get('_bb'):
        return set(it.get('_prev_claims') or []), set(it['claims'])
    if it['generator'] == 'spine_edge':
        return {it['claims'][0]}, {it['claims'][1]}
    return None, set(it['claims'])


def build():
    V5, S, P = load()
    # --- 1 backbone
    bb = []
    bytrace = collections.defaultdict(list)
    for s in S: bytrace[V5[s]['trace']].append(V5[s])
    for tr, its in bytrace.items():
        its.sort(key=lambda x: (x['step'], x['sub']))
        for i, it in enumerate(its):
            b = dict(it); b['_bb'] = True
            b['_prev_claims'] = its[i - 1]['claims'] if i else []
            b['_item'] = it['item']
            bb.append(b)
    bbclaims = collections.defaultdict(set)
    for b in bb: bbclaims[b['paper']].update(b['claims'])

    # --- 2 attach pairs at backbone nodes
    att = []
    for x in P:
        hit = set(x['claims']) & bbclaims.get(x['paper'], set())
        if not hit: continue
        where = ('at the claim' if x['generator'] == 'complementary'
                 else 'along the link into the claim' if x['generator'] == 'covariation'
                 else 'at the claim (spine edge)')
        att.append({'item': x['item'], 'paper': x['paper'], 'generator': x['generator'],
                    'attachment_claim': sorted(hit), 'where': where})

    # --- 3 compose
    universe = bb + P
    byitem = {}
    for it in universe:
        key = it.get('_item') or it['item']
        byitem[key] = it
    out_edges = collections.defaultdict(list)
    concl = collections.defaultdict(list)
    for k, it in byitem.items():
        _, c = direction(it)
        for cc in c: concl[(it['paper'], cc)].append(k)
    joins, rejected = [], []
    for k, it in byitem.items():
        inp, _ = direction(it)
        if not inp: continue
        for cc in inp:
            for up in concl.get((it['paper'], cc), []):
                if up == k: continue
                joins.append({'from': up, 'to': k, 'on_claim': cc, 'paper': it['paper']})
                out_edges[up].append(k)

    # reject loops
    kept, seen_pair = [], set()
    rev = collections.defaultdict(set)
    for j in joins: rev[j['to']].add(j['from'])
    for j in joins:
        if j['from'] in rev.get(j['to'], set()) and j['to'] in rev.get(j['from'], set()):
            rejected.append({**j, 'why': 'loop: each item feeds the other'}); continue
        kept.append(j)
    # reject splits: two joins sharing a MatMech hop
    byhop = collections.defaultdict(list)
    for j in kept:
        h = byitem[j['from']].get('matmech_hop') or \
            (byitem[j['from']].get('provenance_NOT_SOLVER_VISIBLE') or {}).get('matmech_hop')
        if h: byhop[(j['paper'], h)].append(j)
    final = []
    for j in kept:
        h = byitem[j['from']].get('matmech_hop') or \
            (byitem[j['from']].get('provenance_NOT_SOLVER_VISIBLE') or {}).get('matmech_hop')
        grp = byhop.get((j['paper'], h), [])
        if h and len(grp) > 1 and j is not grp[0]:
            rejected.append({**j, 'why': f'split: shares MatMech hop {h} with another join'}); continue
        final.append(j)

    # chains: maximal paths over the kept joins
    nxt = collections.defaultdict(list)
    for j in final: nxt[j['from']].append(j['to'])
    tails = {j['to'] for j in final}
    chains = []
    for start in {j['from'] for j in final} - tails:
        stack = [[start]]
        while stack:
            path = stack.pop()
            if nxt.get(path[-1]):
                for n in nxt[path[-1]]:
                    if n in path: continue
                    stack.append(path + [n])
            elif len(path) > 1:
                chains.append(path)
    def depth(path):
        return sum(1 for k in path
                   if byitem[k].get('_bb') is None or (byitem[k].get('key') or {}).get('combines'))

    # --- 5 convergence
    conv = []
    for (paper, cc), items in concl.items():
        if len(items) < 2: continue
        ev = {}
        for k in items:
            it = byitem[k]
            ev[k] = {it.get('observation_a', {}).get('node'), it.get('observation_b', {}).get('node')} \
                    if not it.get('_bb') else set(it.get('claims') or [])
        indep = [k for k in items]
        pairsok = [(a, b) for i, a in enumerate(indep) for b in indep[i + 1:]
                   if not (ev[a] & ev[b])]
        if pairsok:
            conv.append({'paper': paper, 'claim': cc, 'routes': items,
                         'independent_route_pairs': len(pairsok)})

    res = {'backbone': [b['_item'] for b in bb], 'attachments': att,
           'joins': final, 'rejected': rejected,
           'chains': [{'path': c, 'depth': depth(c), 'paper': byitem[c[0]]['paper']} for c in chains],
           'convergence': conv, 'note': 'Every verdict is model against model.'}
    json.dump(res, open(os.path.join(ROOT, 'results/v2p5/composed.json'), 'w'), indent=1)

    print(f"backbone items: {len(bb)} over {len({b['paper'] for b in bb})} papers")
    print(f"pairs attached to a backbone claim: {len(att)} "
          f"({dict(collections.Counter(a['generator'] for a in att))})")
    print(f"joins kept: {len(final)}   rejected: {len(rejected)} "
          f"({dict(collections.Counter(r['why'].split(':')[0] for r in rejected))})")
    dd = collections.Counter(c['depth'] for c in res['chains'])
    print(f"composed chains: {len(chains)}  by depth: {dict(sorted(dd.items()))}")
    print(f"convergence claims (two or more independent routes): {len(conv)} "
          f"over {len({c['paper'] for c in conv})} papers")
    print(f"\n{'paper':44s} {'bb':>3s} {'att':>4s} {'chains':>6s} {'conv':>5s}")
    papers = [x['paper'] for x in json.load(open(os.path.join(ROOT, 'results/v5_papers.json')))]
    for p in papers:
        print(f"{p[:44]:44s} {sum(1 for b in bb if b['paper']==p):3d} "
              f"{sum(1 for a in att if a['paper']==p):4d} "
              f"{sum(1 for c in res['chains'] if c['paper']==p):6d} "
              f"{sum(1 for c in conv if c['paper']==p):5d}")


JOIN_ASK = """You are auditing a JOIN: one item's conclusion has been carried forward as another
item's input. Two things to rule on.

FIRST, the joined proposition. Rule `holds`, `overreaches` or `wrong` against the evidence of both
items, and quote what you rule against. Overreaches means it states something the evidence supports
only weakly or in a weaker form -- a cause where only an association is available, a relationship
where only an ordering is.

SECOND, and this is the point of a join: **do the upstream item's limits survive the handoff?**
The upstream conclusion was true only within its limits. If the downstream item uses that
conclusion as if those limits did not apply, the chain has laundered a qualified result into an
unqualified one. For each upstream limit, rule `carried` (the joined claim still respects it),
`dropped` (the joined claim ignores it), or `not_applicable`.

A single dropped limit that changes what the joined claim means is enough to fail the join.

Reply as JSON only:
{"proposition": {"verdict": "...", "evidence": "..."},
 "limits_survive": [{"limit": "...", "verdict": "carried|dropped|not_applicable", "why": "..."}],
 "join_verdict": "sound" or "launders a limit",
 "fix": "corrected joined claim" or null}"""

CONV_ASK = """Two routes, with disjoint evidence, reach the same conclusion.

Say, for EACH route separately, whether its evidence warrants the conclusion on its own. Then say
whether the two routes agree -- not merely whether both point the same way, but whether what each
establishes is consistent with what the other establishes, including their limits.

Two routes that both only weakly support a conclusion do not add up to strong support. Say so if
that is the case.

Reply as JSON only:
{"route_a": {"warrants_alone": "yes|partly|no", "why": "..."},
 "route_b": {"warrants_alone": "yes|partly|no", "why": "..."},
 "agree": "yes|partly|no", "why_agree": "...",
 "combined_strength": "descriptive|associative|conditional mechanism|discriminating",
 "caution": "what a reader should not conclude from having two routes"}"""


def _txt(it):
    if it.get('_bb'):
        k = it.get('key') or {}
        return (f"v5 backbone item {it['item']} -- {it.get('property')}\n"
                f"  key: {k.get('proposition')}\n"
                f"  limits: " + '; '.join(k.get('limits') or []))
    k = it.get('key') or {}
    return (f"v2.5 {it['generator']} item {it['item']}\n"
            f"  question: {it['question']}\n"
            f"  A ({it['observation_a']['technique']}): {it['observation_a']['text']}\n"
            f"  B ({it['observation_b']['technique']}): {it['observation_b']['text']}\n"
            f"  key: {k.get('proposition')}\n"
            f"  limits: " + '; '.join(k.get('limits') or []))


def prompts():
    V5, S, P = load()
    C = json.load(open(os.path.join(ROOT, 'results/v2p5/composed.json')))
    byitem = {}
    for s in S:
        b = dict(V5[s]); b['_bb'] = True; byitem[s] = b
    for x in P: byitem[x['item']] = x
    d = os.path.join(ROOT, 'results/v2p5/joinaudit'); os.makedirs(d, exist_ok=True)
    jobs = []
    for j in C['joins']:
        u, v = byitem.get(j['from']), byitem.get(j['to'])
        if not u or not v: continue
        if not (u.get('key') and v.get('key')): continue
        L = [f"The join: {j['from']}  --->  {j['to']}   on claim {j['on_claim']}", "",
             "UPSTREAM ITEM", _txt(u), "", "DOWNSTREAM ITEM", _txt(v), "",
             "The joined claim, as the chain now asserts it:",
             f"  {(v.get('key') or {}).get('proposition')}", "", JOIN_ASK]
        f = os.path.join(d, f"{j['from']}__{j['to']}.txt"); open(f, 'w').write("\n".join(L))
        jobs.append({'id': f"{j['from']}__{j['to']}", 'agent': 'net-judge',
                     'prompt': os.path.abspath(f),
                     'out': os.path.abspath(os.path.join(d, f"{j['from']}__{j['to']}.out.txt"))})
    cd = os.path.join(ROOT, 'results/v2p5/convergence'); os.makedirs(cd, exist_ok=True)
    cjobs = []
    for c in C['convergence']:
        rts = [byitem.get(r) for r in c['routes'] if byitem.get(r)]
        rts = [r for r in rts if r.get('key')]
        if len(rts) < 2: continue
        L = [f"Both routes conclude about claim {c['claim']} in {c['paper']}", "",
             "ROUTE A", _txt(rts[0]), "", "ROUTE B", _txt(rts[1]), "", CONV_ASK]
        f = os.path.join(cd, f"{c['paper'][:20]}_{c['claim']}.txt"); open(f, 'w').write("\n".join(L))
        cjobs.append({'id': f"conv_{c['paper'][:20]}_{c['claim']}", 'agent': 'net-judge',
                      'prompt': os.path.abspath(f),
                      'out': os.path.abspath(f.replace('.txt', '.out.txt'))})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v2p5_join.json'), 'w'), indent=1)
    json.dump(cjobs, open(os.path.join(ROOT, '.v07work/batch_v2p5_conv.json'), 'w'), indent=1)
    print(f"{len(jobs)} join audits, {len(cjobs)} convergence items")
    if len(jobs) < len(C['joins']):
        print(f"  ({len(C['joins']) - len(jobs)} joins skipped: an endpoint has no key yet)")


if __name__ == '__main__': {'build': build, 'prompts': prompts}[sys.argv[1]]()
