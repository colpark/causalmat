"""partE.py: v2.7 Part E -- what the derived_input generator produced.

  python3 -m trace_kit_v2p7.partE

Part B's stop rule fired (decision agreement 28.6%, against a two-thirds target), and the brief
says that when it does: skip the necessity gate in Part E, but still build and draft the items.
So there is no necessity column here. The items are built, drafted and checked; nothing claims
they compose until an instrument exists that can say so.

The checks that do run are the ones that do not need a model:
  - the exclusion, by node id and panel id, already asserted in the generator;
  - the drafter's own `combines` flag, which is its judgement that the two sides actually need
    each other -- the nearest thing to a necessity signal available without the gate;
  - a belongs-check, that each key's words overlap its own item's texts, which is how v2.5
    caught 11 keys attached to the wrong item.

Every verdict is model against model.
"""
import collections, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from items import parse_draft  # noqa: E402


def words(t):
    """words AND numbers: a key that agrees through quoted measurements is not foreign"""
    t = (t or '').lower()
    return ({x for x in re.findall(r'[a-z][a-z0-9\-]{3,}', t)}
            | {x for x in re.findall(r'\d+\.?\d*', t) if len(x) > 1})


def run():
    DI = json.load(open(R('results/v2p7/derived_input.json')))
    items = DI['items_out']
    d = R('results/v2p7/draft')
    got, unparsed, foreign = {}, [], []
    for x in items:
        f = os.path.join(d, x['item'] + '.out.txt')
        if not os.path.exists(f): unparsed.append((x['item'], 'no reply')); continue
        k = parse_draft(open(f).read())
        if not k or 'proposition' not in k: unparsed.append((x['item'], 'unparsed')); continue
        mine = words(x['input_result']) | words(x['new_observation']['text']) | \
            words(' '.join(x['input_limits']))
        kw = words(k.get('proposition'))
        share = len(kw & mine) / len(kw) if kw else 0
        if share < 0.15: foreign.append((x['item'], round(share, 3)))
        got[x['item']] = {'key': k, 'overlap': round(share, 3)}

    lab = collections.Counter()
    for v in got.values():
        L = (v['key'].get('labels') or {})
        lab[('causal_strength', (L.get('causal_strength') or '?'))] += 1
        lab[('dependency', (L.get('dependency') or '?'))] += 1
        lab[('inference_validity', (L.get('inference_validity') or '?'))] += 1
    comb = collections.Counter(bool(v['key'].get('combines')) for v in got.values())
    nid = sum(1 for v in got.values() if v['key'].get('not_identifiable'))

    by = {i['item']: i for i in items}
    ex = [x for x in items if x['item'] in got and got[x['item']]['key'].get('combines')][:5]
    worked = [{
        'item': x['item'], 'paper': x['paper'], 'upstream_item': x['upstream_item'],
        'edge': x['edge'], 'question': x.get('question'),
        'input_result': x['input_result'], 'input_limits': x['input_limits'][:2],
        'new_obs_node': x['new_observation']['node'], 'new_obs': x['new_observation']['text'],
        'panels': [p['suffix'] for p in x['panels']],
        'upstream_panels': x['upstream_panel_ids'],
        'proposition': got[x['item']]['key'].get('proposition'),
        'limits': (got[x['item']]['key'].get('limits') or [])[:3],
        'labels': got[x['item']]['key'].get('labels'),
    } for x in ex]

    res = {
        'note': 'v2.7 Part E. Necessity gate skipped: Part B did not clear its agreement target.',
        'necessity_gate': 'skipped, per the Part B stop rule',
        'candidate_triples': DI['candidate_triples'],
        'distinct_pairs': DI['distinct_item_target_pairs'],
        'papers_with_candidates': DI['papers_with_candidates'],
        'cap_per_paper': DI['cap_per_paper'],
        'items': len(items), 'drafted': len(got),
        'unparsed': unparsed, 'foreign_keys': foreign,
        'combines_true': comb[True], 'combines_false': comb[False],
        'not_identifiable': nid,
        'labels': {k[0] + ': ' + k[1]: v for k, v in sorted(lab.items())},
        'funnel': [
            ['candidate triples', DI['candidate_triples']],
            ['distinct (item, target claim) pairs', DI['distinct_item_target_pairs']],
            [f"after the cap of {DI['cap_per_paper']} per paper", len(items)],
            ['drafted', len(got)],
            ['the drafter says the two sides combine', comb[True]],
        ],
        'per_paper_candidates': DI['per_paper_candidates'],
        'per_paper_items': DI['per_paper_items'],
        'worked_examples': worked,
        'keys': {k: v['key'] for k, v in got.items()},
    }
    json.dump(res, open(R('results/v2p7/partE.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items()
                      if k not in ('keys', 'worked_examples', 'per_paper_candidates',
                                   'per_paper_items')}, indent=1))
    return res


if __name__ == '__main__': run()
