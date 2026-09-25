"""partD_build.py: assemble the 14 backbone joins so the two checks can be read side by side.

  python3 -m trace_kit_v2p7.partD_build

No model call and no new verdict. This only lays out, for each backbone join, what the v2.5
join audit said, what the v2.6 scope check said, and -- the part that matters -- the two texts
each check was shown. The checks disagree on 10 of 14 and the disagreement is not a coin toss
between two opinions about the same thing: they were looking at different texts.

Every verdict is model against model.
"""
import json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj, jkey  # noqa: E402


def run():
    SC = json.load(open(R('results/v2p6/scope.json')))['seams']
    P = json.load(open(R('results/v2p6/pruned.json')))
    V5 = {i['item']: i for i in json.load(open(R('results/v5/items.json')))['items']}
    D = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    ALL = {**V5, **D}
    rows = []
    for jn in P['joins']:
        k = f"{jn['from']}__{jn['to']}"
        sc = SC.get(k) or {}
        if sc.get('premise_from') != 'previous_output': continue
        f = R('results/v2p5/joinaudit', k + '.out.txt')
        ja = obj(open(f).read(), 'limits_survive') or obj(open(f).read(), 'join_verdict') \
            if os.path.exists(f) else None
        jk = jkey(ja)
        up, dn = ALL[jn['from']], ALL[jn['to']]
        upk = up.get('key') or {}
        rows.append({
            'join': k, 'paper': jn['paper'], 'on_claim': jn['on_claim'],
            'v2p5_join_verdict': (ja or {}).get('join_verdict'),
            'v2p5_proposition': (jk or {}).get('pv'),
            'v2p5_limits': dict((jk or {}).get('counts') or {}),
            'v2p5_evidence': ((ja or {}).get('proposition') or {}).get('evidence'),
            'v2p5_note': (ja or {}).get('note_for_caller'),
            'v2p6_scope': sc.get('verdict'), 'v2p6_mismatch': sc.get('mismatch'),
            'v2p6_why': sc.get('why'),
            # what each check actually saw
            'text_upstream_key': (upk.get('proposition') or ''),
            'text_upstream_limits': [str(x) for x in (upk.get('limits') or [])],
            'text_downstream_previous_output': dn.get('previous_output'),
            'text_downstream_question': dn.get('property') or dn.get('question'),
            'text_downstream_key': ((dn.get('key') or {}).get('proposition') or ''),
        })
    json.dump(rows, open(R('results/v2p7/partD_cases.json'), 'w'), indent=1)
    print(f'{len(rows)} backbone joins')
    agree = sum(1 for r in rows if (r['v2p6_scope'] in ('supports', 'supports only narrower'))
                == (r['v2p5_join_verdict'] == 'sound'))
    print(f'v2.5 sound: {sum(1 for r in rows if r["v2p5_join_verdict"] == "sound")}/{len(rows)}'
          f' | v2.6 scope pass: {sum(1 for r in rows if r["v2p6_scope"] in ("supports", "supports only narrower"))}/{len(rows)}'
          f' | the two agree on {agree}/{len(rows)}')
    return rows


if __name__ == '__main__': run()
