"""partD.py: v2.8 Part D -- decide necessity from arm means, and test it on split halves.

  python3 -m trace_kit_v2p8.partD

  the input is needed        mean combined score, arm B minus arm A, at least 0.25
  the observation is needed  mean combined score, arm B minus arm C, at least 0.25
  compositional              both

Two decisions, not one, and the second is the one v2.7 could not make. Beating arm A says the
earlier result added something. Beating arm C says the measurement did. An item that beats A but
not C is restating step 1 with a picture attached; an item that beats C but not A is a
measurement that needed no history. Only both together is composition.

Means over 6 samples, not a vote over single draws. v2.7 Part B thresholded a difference of two
single scores and got 28.6% agreement out of it; the same scores averaged first were far
steadier. The split-half check is here to show whether that holds: decide from samples 1-3 and
from samples 4-6 separately and see if the two halves say the same thing.

Every verdict is model against model.
"""
import collections, json, os, statistics as stats

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
MARGIN = 0.25
ARMS = ('A', 'B', 'C')


def decide(mB, mA, mC):
    inp = (mB - mA) >= MARGIN
    obs = (mB - mC) >= MARGIN
    return inp, obs, bool(inp and obs)


def run():
    C = json.load(open(R('results/v2p8/partC.json')))['answers']
    A = json.load(open(R('results/v2p8/partA.json')))['claims']
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    out = {}
    for s in S:
        it = s['item']
        got = {a: [C[f'{it}_{a}{k}'] for k in range(1, 7) if f'{it}_{a}{k}' in C] for a in ARMS}
        if any(len(v) < 6 for v in got.values()):
            out[it] = {'error': 'incomplete', 'have': {a: len(v) for a, v in got.items()}}
            continue
        comb = {a: [x['combined_score'] for x in got[a]] for a in ARMS}
        lim = {a: [x['limit_score'] for x in got[a]] for a in ARMS}
        con = {a: [x['contradictions'] for x in got[a]] for a in ARMS}
        m = {a: round(stats.mean(comb[a]), 4) for a in ARMS}
        ml = {a: (round(stats.mean([v for v in lim[a] if v is not None]), 4)
                  if any(v is not None for v in lim[a]) else None) for a in ARMS}
        inp, obs, compo = decide(m['B'], m['A'], m['C'])
        halves = {}
        for name, idx in (('first', slice(0, 3)), ('second', slice(3, 6))):
            hm = {a: round(stats.mean(comb[a][idx]), 4) for a in ARMS}
            hi, ho, hc = decide(hm['B'], hm['A'], hm['C'])
            halves[name] = {'means': hm, 'input_needed': hi, 'observation_needed': ho,
                            'compositional': hc}
        out[it] = {
            'paper': s['paper'], 'journal': s['journal'], 'cs': s['cs'],
            'upstream': s['upstream'], 'up_gen': s['up_gen'],
            'n_combined': A[it]['n_combined'], 'n_limit': A[it]['n_limit'],
            'mean_combined': m, 'mean_limit': ml,
            'sd_combined': {a: round(stats.pstdev(comb[a]), 4) for a in ARMS},
            'mean_contradictions': {a: round(stats.mean(con[a]), 3) for a in ARMS},
            'B_minus_A': round(m['B'] - m['A'], 4),
            'B_minus_C': round(m['B'] - m['C'], 4),
            'input_needed': inp, 'observation_needed': obs, 'compositional': compo,
            'halves': halves,
            'halves_agree': halves['first']['compositional'] == halves['second']['compositional'],
            'halves_agree_on_both_decisions': (
                halves['first']['input_needed'] == halves['second']['input_needed']
                and halves['first']['observation_needed'] == halves['second']['observation_needed']),
            'limits_kept_better_in_B_than_A': (
                None if ml['A'] is None or ml['B'] is None else ml['B'] > ml['A']),
        }
    good = [v for v in out.values() if 'error' not in v]
    agree = sum(1 for v in good if v['halves_agree'])
    res = {
        'note': 'v2.8 Part D. Necessity from arm means over 6 samples; margin 0.25.',
        'margin': MARGIN, 'items': len(good),
        'mean_combined_across_items': {
            a: round(stats.mean([v['mean_combined'][a] for v in good]), 4) for a in ARMS},
        'mean_limit_across_items': {
            a: round(stats.mean([v['mean_limit'][a] for v in good
                                 if v['mean_limit'][a] is not None]), 4) for a in ARMS},
        'input_needed': sum(1 for v in good if v['input_needed']),
        'observation_needed': sum(1 for v in good if v['observation_needed']),
        'compositional': sum(1 for v in good if v['compositional']),
        'compositional_items': sorted(k for k, v in out.items()
                                      if 'error' not in v and v['compositional']),
        'halves_agree': agree,
        'halves_agree_on_both_decisions': sum(
            1 for v in good if v['halves_agree_on_both_decisions']),
        'stop_rule_fired': bool(agree < 6),
        'limits_better_in_B': sum(1 for v in good if v['limits_kept_better_in_B_than_A']),
        'items_out': out,
    }
    json.dump(res, open(R('results/v2p8/partD.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'items_out'}, indent=1))
    return res


if __name__ == '__main__': run()
