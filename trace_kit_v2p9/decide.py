"""decide.py: v2.9 Step 4 -- grade, decide, and rerun the borderline items.

  python3 -m trace_kit_v2p9.decide borderline   which items need a second sample
  python3 -m trace_kit_v2p9.decide collect      the final call on every item

An item is compositional when
    B - A >= 0.25   the earlier result is needed
    B - C >= 0.25   the measurement is needed
    N < 0.25        the paper is not simply known

One sample per arm is cheap and noisy, and v2.7 spent a whole run learning what a single draw
is worth. The borderline rule buys precision only where it changes the answer: if either margin
lands between 0.10 and 0.40, the decision is close enough that one more sample of A, B and C is
worth its three calls, and the item is decided on the 2-sample mean. An item at +0.02 or +0.71
is not going to move, and pays nothing.

Every verdict is model against model.
"""
import collections, json, math, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
from trace_kit_v2p9.arms import score, live  # noqa: E402

LO, HI, MARGIN, NBAR = 0.10, 0.40, 0.25, 0.25


def wilson(k, n, z=1.96):
    """95% interval for a proportion. Small n here, so the normal approximation would lie."""
    if not n: return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(max(0.0, c - h), 4), round(min(1.0, c + h), 4))


def means(it, idx, sfx_list):
    out = {}
    for arm in ('A', 'B', 'C', 'N'):
        vals = []
        for s in sfx_list:
            if arm == 'N' and s != '1': continue
            r = score(it, arm, s, idx)
            if r and r['combined_score'] is not None: vals.append(r)
        if not vals: return None
        out[arm] = {
            'combined': round(sum(v['combined_score'] for v in vals) / len(vals), 4),
            'limit': (round(sum(v['limit_score'] for v in vals
                                if v['limit_score'] is not None) / len(vals), 4)
                      if any(v['limit_score'] is not None for v in vals) else None),
            'contradictions': round(sum(v['contradictions'] for v in vals) / len(vals), 3),
            'n': len(vals)}
    return out


def decide_one(m):
    bA, bC = m['B']['combined'] - m['A']['combined'], m['B']['combined'] - m['C']['combined']
    return {'B_minus_A': round(bA, 4), 'B_minus_C': round(bC, 4),
            'input_needed': bA >= MARGIN, 'observation_needed': bC >= MARGIN,
            'N_ok': m['N']['combined'] < NBAR,
            'compositional': bool(bA >= MARGIN and bC >= MARGIN
                                  and m['N']['combined'] < NBAR)}


def borderline():
    idx = json.load(open(R('results/v2p9/claim_index.json')))
    # the margin itself, not its size: a margin of -0.30 is decided, not close
    out = []
    for it, x, v in live():
        m = means(it, idx, ['1'])
        if not m: continue
        d = decide_one(m)
        if (LO <= d['B_minus_A'] <= HI) or (LO <= d['B_minus_C'] <= HI):
            out.append(it)
    json.dump(out, open(R('results/v2p9/borderline.json'), 'w'), indent=1)
    print(f'{len(out)} of 88 items are borderline and get a second sample of A, B and C')
    return out


def collect():
    idx = json.load(open(R('results/v2p9/claim_index.json')))
    S2 = json.load(open(R('results/v2p9/step2.json')))['items']
    bl = set(json.load(open(R('results/v2p9/borderline.json')))
             if os.path.exists(R('results/v2p9/borderline.json')) else [])
    out, flips, unruled = {}, [], []
    for it, x, v in live():
        one = means(it, idx, ['1'])
        if not one: unruled.append(it); continue
        d1 = decide_one(one)
        two, d2 = None, None
        if it in bl:
            two = means(it, idx, ['1', '2'])
            if two: d2 = decide_one(two)
        final = d2 or d1
        m = two or one
        if d2 and d2['compositional'] != d1['compositional']:
            flips.append({'item': it, 'one_sample': d1['compositional'],
                          'two_sample': d2['compositional']})
        out[it] = {
            'paper': x['paper'], 'upstream': x['upstream_item'],
            'n_combined': S2[it]['n_combined'], 'n_limit': S2[it]['n_limit'],
            'labels': S2[it]['labels'],
            'mean_combined': {a: m[a]['combined'] for a in m},
            'mean_limit': {a: m[a]['limit'] for a in m},
            'mean_contradictions': {a: m[a]['contradictions'] for a in m},
            'samples': {a: m[a]['n'] for a in m},
            'borderline': it in bl, 'one_sample': d1, **final,
            'input_result': x['input_result'], 'input_limits': x['input_limits'],
            'new_observation': x['new_observation'], 'target_claim': x['target_claim'],
            'claim_C': x['claim_C'], 'panels': [p['suffix'] for p in x['panels']],
        }
    good = list(out.values())
    npass = sum(1 for v in good if v['compositional'])
    nhi = [k for k, v in out.items() if not v['N_ok']]
    lo, hi = wilson(npass, len(good))
    res = {
        'note': 'v2.9 Step 4. B beats A and C by >=0.25, N below 0.25.',
        'items': len(good), 'unruled': unruled,
        'compositional': npass,
        'pass_rate': round(npass / len(good), 4) if good else None,
        'pass_rate_95ci': [lo, hi],
        'input_needed': sum(1 for v in good if v['input_needed']),
        'observation_needed': sum(1 for v in good if v['observation_needed']),
        'N_at_or_above_threshold': len(nhi), 'N_items': sorted(nhi),
        'N_share': round(len(nhi) / len(good), 4) if good else None,
        'stop_memorisation': bool(good and len(nhi) / len(good) > 0.15),
        'stop_too_few': bool(npass < 15),
        'borderline_count': len(bl), 'borderline_flips': flips,
        'mean_combined_across_items': {
            a: round(sum(v['mean_combined'][a] for v in good) / len(good), 4)
            for a in ('A', 'B', 'C', 'N')} if good else {},
        'mean_limit_across_items': {
            a: round(sum(v['mean_limit'][a] for v in good
                         if v['mean_limit'][a] is not None) / len(good), 4)
            for a in ('A', 'B', 'C', 'N')} if good else {},
        'per_paper': {p: {'items': sum(1 for v in good if v['paper'] == p),
                          'compositional': sum(1 for v in good
                                               if v['paper'] == p and v['compositional'])}
                      for p in sorted({v['paper'] for v in good})},
        'items_out': out,
    }
    json.dump(res, open(R('results/v2p9/step4.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items()
                      if k not in ('items_out', 'per_paper', 'N_items')}, indent=1))
    return res


if __name__ == '__main__':
    {'borderline': borderline, 'collect': collect}[sys.argv[1]]()
