"""select.py: v2.8 Step 0 -- choose the 8 pilot items, deterministically and with a reason each.

  python3 -m trace_kit_v2p8.select

The brief's constraints: 8 items from 8 different papers; the 4 "discriminating" ones as far as
one-per-paper allows; the rest "associative" or "conditional mechanism" spread across journals;
at least 2 whose input result came from a complementary v2.5 item and at least 2 from a
spine_edge item.

The 4 discriminating items happen to sit in 4 different papers, so all 4 are taken, and they are
already 2 complementary and 2 spine_edge -- the generator-mix constraint is satisfied before the
other 4 are chosen. Those 4 are then picked one per journal from journals not yet used,
preferring "conditional mechanism" over "associative" because it is the scarcer label (15 against
56), and preferring a spine_edge upstream where one is available so the pilot is not dominated by
complementary. Ties break on the item id, so the choice is reproducible.

Every verdict is model against model.
"""
import collections, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)


def run():
    rows = json.load(open(R('results/v2p8/pool.json')))
    picked, reasons = [], {}

    disc = sorted([r for r in rows if r['cs'] == 'discriminating'], key=lambda r: r['item'])
    seen_paper = set()
    for r in disc:
        if r['paper'] in seen_paper: continue
        seen_paper.add(r['paper']); picked.append(r)
        reasons[r['item']] = (
            f"labelled discriminating, the scarcest causal-strength label in the pool "
            f"(4 of 76); upstream is a {r['up_gen']} v2.5 item")

    used_j = {r['journal'] for r in picked}
    rest = [r for r in rows
            if r['cs'] in ('associative', 'conditional mechanism')
            and r['journal'] not in used_j and r['paper'] not in seen_paper]
    byj = collections.defaultdict(list)
    for r in rest: byj[r['journal']].append(r)

    def rank(r):
        return (0 if r['cs'] == 'conditional mechanism' else 1,
                0 if r['up_gen'] == 'spine_edge' else 1, r['item'])

    # journals with the most candidates first, so the pilot spreads where the pool is deepest
    order = sorted(byj, key=lambda j: (-len(byj[j]), j))
    for j in order:
        if len(picked) >= 8: break
        r = sorted(byj[j], key=rank)[0]
        if r['paper'] in seen_paper: continue
        seen_paper.add(r['paper']); picked.append(r)
        why = [f"labelled {r['cs']}"]
        if r['cs'] == 'conditional mechanism':
            why.append('the scarcer of the two remaining labels, 15 of 76 against 56 associative')
        why.append(f"{j.replace('_', ' ')} is not yet represented")
        why.append(f"upstream is a {r['up_gen']} v2.5 item")
        reasons[r['item']] = '; '.join(why)

    gens = collections.Counter(r['up_gen'] for r in picked)
    out = {
        'note': 'v2.8 Step 0. The 8 pilot items, chosen before anything was run.',
        'n': len(picked),
        'papers': len({r['paper'] for r in picked}),
        'journals': len({r['journal'] for r in picked}),
        'causal_strength': dict(collections.Counter(r['cs'] for r in picked)),
        'upstream_generator': dict(gens),
        'constraints': {
            'eight from eight papers': len({r['paper'] for r in picked}) == 8 and len(picked) == 8,
            'all four discriminating taken': sum(1 for r in picked if r['cs'] == 'discriminating') == 4,
            'at least two complementary upstream': gens['complementary'] >= 2,
            'at least two spine_edge upstream': gens['spine_edge'] >= 2,
        },
        'items': [{**r, 'why_picked': reasons[r['item']]} for r in picked],
    }
    assert all(out['constraints'].values()), out['constraints']
    json.dump(out, open(R('results/v2p8/selected.json'), 'w'), indent=1)
    return out


if __name__ == '__main__':
    o = run()
    print(json.dumps({k: v for k, v in o.items() if k != 'items'}, indent=1))
    for i, r in enumerate(o['items'], 1):
        print(f"\n{i}. {r['item']}")
        print(f"   {r['journal'].replace('_', ' ')}  |  {r['cs']}  |  upstream {r['upstream']} ({r['up_gen']})")
        print(f"   why: {r['why_picked']}")
