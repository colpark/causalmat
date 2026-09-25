"""derived_input.py: v2.7 Part E -- a generator that makes the downstream need the upstream.

  python3 -m trace_kit_v2p7.derived_input build

v2.6's finding was that in 118 of 121 joins the downstream item re-reads the very observation
the upstream item read. The two items share evidence; nothing is passed forward. No amount of
filtering repairs that, because the generators never made a pair where a conclusion had to
travel. This one does.

For each claim C that a v2.5 item concludes:
  - the input result is that item's key proposition and its limits;
  - the new observation is one the upstream item did NOT use, which evidences a claim that C
    points at through a causes, explains or supports edge;
  - the question asks what the two together settle, and is written so that neither side answers
    it alone: the new observation is one link further down the spine than the input result, so
    reading it gives you the downstream fact without the upstream cause, and holding the input
    result gives you the cause without knowing what it produced.

The exclusion is the whole point, so it is checked mechanically and twice: by node id (the new
observation's node is not either of the upstream item's observation nodes) and by panel id (the
new item's panels and the upstream item's panels are disjoint sets). A candidate that fails
either check is dropped and counted, never repaired.

196 distinct (item, target claim) candidates exist across 28 of the 32 papers. Running all of
them through the necessity check would cost about 3100 model calls, so this caps at 3 per paper
and says so; the full candidate count is reported either way.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v3'))
sys.path.insert(0, R('trace_kit_v2p5'))
from support import claim_support  # noqa: E402
from items import panel_record, store_for, unmath  # noqa: E402

REL = {'causes', 'explains', 'supports'}
CAP_PER_PAPER = 3
MAX_PANELS = 5


def concludes(it):
    """the claim an item lands on; for a spine edge that is the downstream end"""
    return (it['claims'][1] if it['generator'] == 'spine_edge' and len(it['claims']) > 1
            else it['claims'][0])


def panels_of(node, store):
    """the panel records an observation node carries, resolved from the paper's panel store.

    The first version scavenged these off whatever v2.5 item happened to have used the same
    observation, which silently dropped 121 candidates whose observation no item had touched --
    exactly the observations this generator is looking for.
    """
    out = []
    for pid in (node.get('panel_ids') or []):
        r = panel_record(store, pid) or {}
        c = r.get('crop')
        out.append({'panel_id': pid, 'suffix': pid.split('#')[-1],
                    'crop': c if c and os.path.exists(c) else None,
                    'figure': r.get('figure'),
                    'caption_span': ' '.join(unmath(r.get('span') or '').split()) or None})
    return [q for q in out if q['crop']]


def build():
    D = [i for i in json.load(open(R('results/v2p5/items.json')))['items']
         if i['generator'] != 'covariation']
    papers = [x['paper'] for x in json.load(open(R('results/v5_papers.json')))]
    cand, items, drops = [], [], collections.Counter()
    per_paper = collections.Counter()
    for p in papers:
        gp = json.load(open(R('results/v3', p, 'stitch.json')))['graph']
        gr = json.load(open(R(gp)))
        store = store_for(R(gp))
        N = {n['id']: n for n in gr['nodes']}
        sup = claim_support(gr)
        obs_of = collections.defaultdict(set)
        for c, r in sup.items(): obs_of[c] |= set(r['via'])
        oe = collections.defaultdict(set)
        for e in gr['edges']:
            if e.get('rel') in REL: oe[e['src']].add(e['dst'])
        pits = [i for i in D if i['paper'] == p]
        seen_pair = set()
        for it in pits:
            used_nodes = {it['observation_a']['node'], it['observation_b']['node']}
            used_pans = {q.get('panel_id') for q in (it.get('panels') or []) if q.get('panel_id')}
            C = concludes(it)
            k = (it.get('key') or {})
            if not (k.get('proposition') or '').strip(): continue
            for tgt in sorted(oe.get(C, ())):
                for o in sorted(obs_of.get(tgt, ())):
                    if o in used_nodes: drops['new obs is one the upstream used'] += 1; continue
                    node = N.get(o) or {}
                    if not node.get('panel_ids'): drops['new obs has no panels'] += 1; continue
                    pans = panels_of(node, store)
                    if not pans: drops['no panel record for the new obs'] += 1; continue
                    npans = {q.get('panel_id') for q in pans if q.get('panel_id')}
                    if npans & used_pans:
                        drops['new obs shares a panel with the upstream'] += 1; continue
                    cand.append({'paper': p, 'upstream': it['item'], 'claim_C': C,
                                 'target_claim': tgt, 'new_obs': o})
                    if (it['item'], tgt) in seen_pair: continue
                    seen_pair.add((it['item'], tgt))
                    if per_paper[p] >= CAP_PER_PAPER:
                        drops['over the per-paper cap'] += 1; continue
                    per_paper[p] += 1
                    items.append({
                        # the FULL upstream item id, not its last token. Taking the last token
                        # collapsed journal_of_a_spi_o13_o20 and journal_of_a_spi_o25_o20 to the
                        # same id, so one item's prompt overwrote the other's and one of the two
                        # keys would have been attached to the wrong item. That is the v2.5 id
                        # collision again, which mis-attached 11 keys before it was caught.
                        'item': f"di_{it['item']}_{o}_{tgt}",
                        'paper': p, 'generator': 'derived_input',
                        'upstream_item': it['item'], 'claim_C': C, 'target_claim': tgt,
                        'input_result': (k.get('proposition') or '').strip(),
                        'input_limits': [str(x) for x in (k.get('limits') or [])],
                        'new_observation': {'node': o, 'text': (node.get('label') or '').strip(),
                                            'technique': node.get('technique')},
                        'panels': pans[:MAX_PANELS],
                        'panels_dropped_by_cap': max(0, len(pans) - MAX_PANELS),
                        'upstream_obs_nodes': sorted(used_nodes),
                        'upstream_panel_ids': sorted(x for x in used_pans),
                        'edge': f'{C} -> {tgt}',
                    })
    ids = [x['item'] for x in items]
    assert len(ids) == len(set(ids)), \
        [k for k, n in collections.Counter(ids).items() if n > 1]

    # the mechanical exclusion check, run again over the finished items
    fails = []
    for x in items:
        if x['new_observation']['node'] in x['upstream_obs_nodes']:
            fails.append((x['item'], 'node id overlap'))
        np_ = {q.get('panel_id') for q in x['panels'] if q.get('panel_id')}
        if np_ & set(x['upstream_panel_ids']):
            fails.append((x['item'], 'panel id overlap'))
    assert not fails, fails[:5]

    out = {'note': 'v2.7 Part E. derived_input candidates and the items taken forward.',
           'candidate_triples': len(cand),
           'distinct_item_target_pairs': len({(c['upstream'], c['target_claim']) for c in cand}),
           'papers_with_candidates': len({c['paper'] for c in cand}),
           'cap_per_paper': CAP_PER_PAPER, 'items': len(items),
           'dropped': dict(drops),
           'per_paper_candidates': dict(collections.Counter(c['paper'] for c in cand)),
           'per_paper_items': dict(per_paper),
           'exclusion_check': 'passed: no item shares an observation node or a panel id with '
                              'its upstream item',
           'items_out': items}
    json.dump(out, open(R('results/v2p7/derived_input.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ('items_out', 'per_paper_candidates', 'per_paper_items')}, indent=1))
    return out





QUESTION = ("What does this measurement, read together with the established earlier result "
            "below, settle about {topic} that neither settles on its own? Say what the "
            "combination supports and what it leaves open.")


def question_for(x, N):
    t = (N.get(x['target_claim'], {}).get('type') or 'the sample')
    return QUESTION.format(topic=t)


def prompts():
    """the v2.5 drafter and the v2.5 rules, with the input result standing in for observation A"""
    sys.path.insert(0, R('trace_kit_v2p5'))
    from items import DRAFT_ASK  # the same rules text, not a paraphrase
    d = json.load(open(R('results/v2p7/derived_input.json')))
    out = R('results/v2p7/draft'); os.makedirs(out, exist_ok=True)
    jobs = []
    for x in d['items_out']:
        gp = json.load(open(R('results/v3', x['paper'], 'stitch.json')))['graph']
        N = {n['id']: n for n in json.load(open(R(gp)))['nodes']}
        x['question'] = question_for(x, N)
        lim = '\n'.join('    - ' + t for t in x['input_limits']) or '    - none recorded'
        L = [f"Question as the solver sees it: {x['question']}", '',
             'Observation A is not a raw measurement here. It is a result already established '
             'by an earlier step, handed to this step as settled:',
             f"  {x['input_result']}",
             '  The qualifications recorded on that earlier result:', lim, '',
             f"Observation B ({x['new_observation']['technique']}): {x['new_observation']['text']}",
             '', f"How the graph links them: the earlier result concludes a claim that points to "
                 f"B's claim through a {x['edge']} edge",
             'Panels: ' + ', '.join(p['suffix'] for p in x['panels']), '',
             'What the paper concluded, for your reference as the key\'s author:',
             f"  {(N.get(x['target_claim']) or {}).get('label')}", '', DRAFT_ASK]
        f = os.path.join(out, x['item'] + '.txt')
        open(f, 'w').write('\n'.join(L))
        jobs.append({'id': x['item'], 'agent': 'net-writer', 'prompt': f,
                     'out': os.path.join(out, x['item'] + '.out.txt')})
    json.dump(d, open(R('results/v2p7/derived_input.json'), 'w'), indent=1)
    json.dump(jobs, open(R('results/v2p7/draft_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} draft prompts')
    return jobs


if __name__ == '__main__':
    {'build': build, 'prompts': prompts}[sys.argv[1]]()
