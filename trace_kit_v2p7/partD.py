"""partD.py: v2.7 Part D -- why the v2.5 audit and the v2.6 scope check disagree on the backbone.

  python3 -m trace_kit_v2p7.partD

No model call, and neither check's output is changed. This works out which of the two is
answering the right question on each of the 14 backbone joins, and the answer turns out to be
structural rather than a matter of taste.

The v2.6 scope check was given two texts: the join's upstream key as TEXT 1, and, as TEXT 2,
the downstream backbone item's `previous_output` field. `previous_output` is the result that
item was handed by ITS OWN v5 chain -- the item at (same trace, step = previous_step). The
v2.5 composition, though, joined items into backbone items on a shared claim id, and it did
not care about the v5 chain.

In 13 of the 14 backbone joins the join's upstream is NOT the v5 chain's previous step. So the
scope check was comparing this join's upstream against a premise belonging to a different item,
and the ten "incompatible" verdicts are recording that mismatch -- not a scope failure of the
join. On those 13, the v2.5 join audit is the check to trust: it saw the downstream item's
actual key.

On the one join where the upstream IS the v5 predecessor, the scope question is well posed, and
there v2.6 is the one to trust.

Two of the 13 deserve their own note: `advanced_ene_M1_M2_M4_s2_1 -> s2_2` and
`bioactive_ma_M5_M7_s2_1 -> s2_2` join consecutive SUB-steps of one step (s2_2's key literally
opens "...and a lower plating overpotential", continuing s2_1). That is a genuine sequential
link, but `previous_step` for a sub-2 item points at the step before, not at sub-1, so the
premise text is wrong there too and the scope verdict is still void.

Every verdict is model against model.
"""
import collections, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
SCOPE_OK = ('supports', 'supports only narrower')


def run():
    V5 = {i['item']: i for i in json.load(open(R('results/v5/items.json')))['items']}
    rows = json.load(open(R('results/v2p7/partD_cases.json')))
    out = []
    for r in rows:
        up, dn = r['join'].split('__')
        d = V5[dn]
        preds = sorted(i['item'] for i in V5.values()
                       if i.get('trace') == d.get('trace') and i.get('step') == d.get('previous_step'))
        is_pred = up in preds
        u = V5.get(up)
        substep = bool(u and u.get('trace') == d.get('trace') and u.get('step') == d.get('step')
                       and (u.get('sub') or 0) == (d.get('sub') or 0) - 1)
        if is_pred:
            who, why = 'v2.6 scope', (
                "The join's upstream IS this item's v5 previous step, so `previous_output` is "
                "genuinely the premise the downstream was handed and the scope question is well "
                "posed. The scope check is right. Note that v2.5's own note_for_caller called "
                "this join a “topic mismatch” while its structured verdict said sound, so "
                "v2.5 contradicted itself here and v2.6 agrees with v2.5's prose.")
        else:
            who, why = 'v2.5 join audit', (
                f"The join's upstream is not this item's v5 previous step ({', '.join(preds) or 'none'}), "
                "so `previous_output` describes a result from a different item. The scope check "
                "compared two texts that were never meant to meet, and its verdict is void for "
                "this join rather than wrong. v2.5 saw the downstream item's actual key."
                + (" This join does link consecutive sub-steps of one step, which is a real "
                   "sequential relation, but `previous_step` on a sub-2 item points past sub-1, "
                   "so the premise text is still the wrong one." if substep else ""))
        out.append({**r, 'upstream_is_v5_previous_step': is_pred,
                    'v5_previous_step_items': preds, 'consecutive_substep': substep,
                    'which_check_is_right': who, 'why': why,
                    'v2p5_passes': r['v2p5_join_verdict'] == 'sound',
                    'v2p6_passes': r['v2p6_scope'] in SCOPE_OK})

    agree = sum(1 for r in out if r['v2p5_passes'] == r['v2p6_passes'])
    res = {
        'note': 'v2.7 Part D. Neither check re-run; this decides which was asked the right '
                'question on each backbone join.',
        'joins': len(out),
        'v2p5_sound': sum(1 for r in out if r['v2p5_passes']),
        'v2p5_launders': sum(1 for r in out if r['v2p5_join_verdict'] == 'launders a limit'),
        'v2p6_scope_pass': sum(1 for r in out if r['v2p6_passes']),
        'v2p6_scope': dict(collections.Counter(r['v2p6_scope'] for r in out)),
        'agree_on_pass_fail': agree,
        'upstream_is_v5_previous_step': sum(1 for r in out if r['upstream_is_v5_previous_step']),
        'consecutive_substep': sum(1 for r in out if r['consecutive_substep']),
        'verdict_counts': dict(collections.Counter(r['which_check_is_right'] for r in out)),
        'correction_to_the_brief':
            "The brief says the v2.5 join audit rated all backbone seams clean. It did not: it "
            f"rated {sum(1 for r in out if r['v2p5_join_verdict'] == 'launders a limit')} of "
            f"{len(out)} as laundering a limit and "
            f"{sum(1 for r in out if r['v2p5_passes'])} as sound. The contradiction is real but "
            "it is narrower than 'all clean against 10 of 14 failing'.",
        'cases': out,
    }
    json.dump(res, open(R('results/v2p7/partD.json'), 'w'), indent=1)
    return res


if __name__ == '__main__':
    r = run()
    print(json.dumps({k: v for k, v in r.items() if k != 'cases'}, indent=1))
