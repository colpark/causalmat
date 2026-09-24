"""prune.py: v2.6 steps 1 and 2 -- drop covariation, then collapse chains that share a tail.

  python3 -m trace_kit_v2p6.prune

Reads results/v2p5/{items,composed}.json, writes results/v2p6/pruned.json. Touches nothing
under results/v2p5/.

Step 1. The covariation generator paired two numeric series because they had the SAME LENGTH,
not because they were comparable, so 37% of its items put two kinds of quantity side by side.
Every covariation item goes, and with it every join, chain and attachment that names one. A
chain is dropped whole, not truncated: a chain with its middle removed is a different chain,
and we would be inventing a merge nobody generated.

Step 2. Two chains that differ only in their opener are one chain with two ways in. The Nano
Letters review found traces 3 and 4 there were the same chain under two generator labels.
Collapsing on the tail (path minus opener) keeps every opener as a variant, so nothing is lost
from the page -- only the count stops double-reporting one piece of reasoning.

Every verdict is model against model.
"""
import json, os, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)


def load():
    D = json.load(open(R('results/v2p5/items.json')))['items']
    C = json.load(open(R('results/v2p5/composed.json')))
    return D, C


def run():
    D, C = load()
    cov = sorted(i['item'] for i in D if i['generator'] == 'covariation')
    covs = set(cov)

    keep_items = [i for i in D if i['item'] not in covs]
    joins = [j for j in C['joins'] if j['from'] not in covs and j['to'] not in covs]
    att = [a for a in C['attachments'] if a['item'] not in covs]
    rej = [r for r in C['rejected'] if r['from'] not in covs and r['to'] not in covs]
    ch1 = [c for c in C['chains'] if not any(x in covs for x in c['path'])]

    dropped = {
        'items': cov,
        'joins': [f"{j['from']}__{j['to']}" for j in C['joins']
                  if j['from'] in covs or j['to'] in covs],
        'chains': [c['path'] for c in C['chains'] if any(x in covs for x in c['path'])],
        'attachments': [a['item'] for a in C['attachments'] if a['item'] in covs],
        'rejected': [f"{r['from']}__{r['to']}" for r in C['rejected']
                     if r['from'] in covs or r['to'] in covs],
    }

    # Step 2: collapse on the tail. Order is kept stable (first occurrence wins) so the page
    # and the report name the same chain the same way on every run.
    by_tail = collections.OrderedDict()
    for c in ch1:
        t = tuple(c['path'][1:])
        if t not in by_tail:
            by_tail[t] = {'chain': f'c{len(by_tail) + 1:03d}', 'paper': c['paper'],
                          'depth': c['depth'], 'tail': list(t), 'openers': [], 'path': list(c['path'])}
        e = by_tail[t]
        if c['path'][0] not in e['openers']: e['openers'].append(c['path'][0])
        assert e['paper'] == c['paper'] and e['depth'] == c['depth'], t
    chains = list(by_tail.values())

    out = {
        'note': 'v2.6 steps 1-2. Covariation dropped, chains collapsed on their tail.',
        'dropped': dropped,
        'items': [i['item'] for i in keep_items],
        'joins': joins, 'attachments': att, 'rejected': rej,
        'backbone': C['backbone'], 'convergence': C['convergence'],
        'chains': chains,
        'funnel': {
            'chains_v2p5': len(C['chains']),
            'after_drop_covariation': len(ch1),
            'after_dedup': len(chains),
            'joins_v2p5': len(C['joins']), 'joins_after_drop': len(joins),
            'items_v2p5': len(D), 'items_after_drop': len(keep_items),
            'attachments_v2p5': len(C['attachments']), 'attachments_after_drop': len(att),
        },
        'depth_before': dict(sorted(collections.Counter(c['depth'] for c in C['chains']).items())),
        'depth_after_drop': dict(sorted(collections.Counter(c['depth'] for c in ch1).items())),
        'depth_after_dedup': dict(sorted(collections.Counter(c['depth'] for c in chains).items())),
        'collapsed': sum(len(c['openers']) - 1 for c in chains),
    }
    os.makedirs(R('results/v2p6'), exist_ok=True)
    json.dump(out, open(R('results/v2p6/pruned.json'), 'w'), indent=1)
    return out


if __name__ == '__main__':
    o = run()
    print(json.dumps({k: o[k] for k in
                      ('funnel', 'depth_before', 'depth_after_drop', 'depth_after_dedup', 'collapsed')}, indent=1))
    print('dropped:', {k: len(v) for k, v in o['dropped'].items()})
