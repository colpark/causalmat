"""partA.py: v2.8 Part A -- split each key into atomic claims, then check the tags independently.

  python3 -m trace_kit_v2p8.partA split     one prompt per item
  python3 -m trace_kit_v2p8.partA check     the tag-check prompts, built from the split replies
  python3 -m trace_kit_v2p8.partA collect   keep only the claims both agents tag the same

The point of the whole pilot is to stop asking whether two answers differ and start asking
whether an answer reaches the key. That needs the key broken into pieces that can be found or
not found in an answer, and each piece labelled by what it takes to reach it:

  input        restates step 1's conclusion. An answer can have it from the input result alone.
  observation  restates the new measurement. An answer can have it from the observation alone.
  combined     needs both, and neither side states it alone. This is the only tag that can show
               composition, so an item with none of these does not combine and stops here.

The splitter proposes the tags. A second agent sees the input result, the new observation and
the claim list -- but not the splitter's reasoning -- and rules each tag agree or disagree. Only
claims both agree on survive. The key's limits are carried through separately as "limit" claims
and are not tagged, because a limit is a thing the answer should say regardless of which side
it came from.

Every verdict is model against model.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402

SPLIT = R('results/v2p8/split')
CHECK = R('results/v2p8/check')

SPLIT_ASK = """You are taking one answer key apart, not answering anything.

Below is a result established by an earlier step, a new measurement, and the key that was written for the two together. Break the key's proposition into short atomic claims -- one assertion each, no conjunctions -- and tag every claim with what it would take to reach it.

THE EARLIER RESULT (step 1's conclusion)
{inp}

THE NEW MEASUREMENT
{obs}

THE KEY'S PROPOSITION
{prop}

Tag each claim exactly one of:

  input        the claim restates or directly follows from THE EARLIER RESULT alone. Someone
               holding only the earlier result could write it.
  observation  the claim restates or directly follows from THE NEW MEASUREMENT alone. Someone
               holding only the measurement could write it.
  combined     the claim needs BOTH. Neither the earlier result nor the measurement states it on
               its own, and it does not follow from either alone.

Be strict about "combined". A claim that merely mentions both sides is not combined; it has to
assert something -- a link, a comparison, a consequence, a ruling-out -- that neither side
carries. If in doubt, tag it input or observation.

Keep each claim under 30 words and use the key's own wording where you can.

Return JSON and nothing else:
{{"claims": [{{"claim": "...", "tag": "input" | "observation" | "combined"}}, ...]}}"""

CHECK_ASK = """You are checking someone else's labels. You have not seen their reasoning and should not try to reconstruct it.

THE EARLIER RESULT (step 1's conclusion)
{inp}

THE NEW MEASUREMENT
{obs}

Below are claims, each with a label. The labels mean:

  input        reachable from THE EARLIER RESULT alone
  observation  reachable from THE NEW MEASUREMENT alone
  combined     needs both; neither side states it or implies it on its own

For each claim, rule whether the label is right.

Rule "disagree" whenever a claim labelled combined is in fact reachable from one side alone -- that is the error that matters here, because a claim wrongly called combined would make an item look like it composes when it does not. Also rule "disagree" if a claim labelled input or observation actually needs both.

Return JSON and nothing else, one entry per claim, in the same order:
{{"rulings": [{{"n": 1, "verdict": "agree" | "disagree", "correct_tag": "input" | "observation" | "combined", "why": "at most 25 words"}}, ...]}}

THE CLAIMS
{claims}"""


def items():
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    DI = {x['item']: x for x in json.load(open(R('results/v2p7/derived_input.json')))['items_out']}
    K = json.load(open(R('results/v2p7/partE.json')))['keys']
    out = []
    for s in S:
        x = DI[s['item']]
        out.append({**s, 'x': x, 'key': K[s['item']]})
    return out


def split():
    os.makedirs(SPLIT, exist_ok=True)
    jobs = []
    for r in items():
        body = SPLIT_ASK.format(inp=r['x']['input_result'],
                                obs=r['x']['new_observation']['text'],
                                prop=r['key'].get('proposition'))
        f = os.path.join(SPLIT, r['item'] + '.txt'); open(f, 'w').write(body)
        jobs.append({'id': r['item'], 'agent': 'net-writer', 'prompt': f,
                     'out': os.path.join(SPLIT, r['item'] + '.out.txt')})
    json.dump(jobs, open(R('results/v2p8/split_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} split prompts')
    return jobs


def claims_of(item):
    f = os.path.join(SPLIT, item + '.out.txt')
    if not os.path.exists(f): return None
    o = obj(open(f).read(), 'claims')
    if not o: return None
    out = []
    for c in (o.get('claims') or []):
        t = (c.get('tag') or '').strip().lower()
        if t not in ('input', 'observation', 'combined'): continue
        s = (c.get('claim') or '').strip()
        if s: out.append({'claim': s, 'tag': t})
    return out or None


def check():
    os.makedirs(CHECK, exist_ok=True)
    jobs, miss = [], []
    for r in items():
        cs = claims_of(r['item'])
        if not cs: miss.append(r['item']); continue
        listing = '\n'.join(f"{i}. [{c['tag']}] {c['claim']}" for i, c in enumerate(cs, 1))
        body = CHECK_ASK.format(inp=r['x']['input_result'],
                                obs=r['x']['new_observation']['text'], claims=listing)
        f = os.path.join(CHECK, r['item'] + '.txt'); open(f, 'w').write(body)
        jobs.append({'id': r['item'], 'agent': 'net-contrib', 'prompt': f,
                     'out': os.path.join(CHECK, r['item'] + '.out.txt')})
    json.dump(jobs, open(R('results/v2p8/check_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} tag-check prompts, {len(miss)} items with no usable split: {miss}')
    return jobs


def collect():
    out, tot, agreed = {}, 0, 0
    for r in items():
        cs = claims_of(r['item']) or []
        f = os.path.join(CHECK, r['item'] + '.out.txt')
        o = obj(open(f).read(), 'rulings') if os.path.exists(f) else None
        rul = {int(x['n']): x for x in (o or {}).get('rulings', [])
               if str(x.get('n', '')).strip().isdigit()}
        kept, dropped = [], []
        for i, c in enumerate(cs, 1):
            v = (rul.get(i) or {}).get('verdict', '').strip().lower()
            tot += 1
            if v == 'agree':
                agreed += 1; kept.append({**c, 'agreed': True})
            else:
                dropped.append({**c, 'verdict': v or 'no ruling',
                                'correct_tag': (rul.get(i) or {}).get('correct_tag'),
                                'why': (rul.get(i) or {}).get('why')})
        lims = [{'claim': str(t).strip(), 'tag': 'limit'}
                for t in (r['key'].get('limits') or []) if str(t).strip()]
        out[r['item']] = {
            'paper': r['paper'], 'journal': r['journal'], 'cs': r['cs'],
            'upstream': r['upstream'], 'up_gen': r['up_gen'],
            'proposed': len(cs), 'kept': kept, 'dropped': dropped,
            'limits': lims,
            'n_combined': sum(1 for c in kept if c['tag'] == 'combined'),
            'n_input': sum(1 for c in kept if c['tag'] == 'input'),
            'n_observation': sum(1 for c in kept if c['tag'] == 'observation'),
            'n_limit': len(lims),
        }
    share = round(agreed / tot, 3) if tot else None
    res = {'note': 'v2.8 Part A. Two agents; only claims both tag the same survive.',
           'items': len(out), 'tags_proposed': tot, 'tags_agreed': agreed,
           'tag_agreement': share,
           'stop_rule_fired': bool(tot and share < 0.70),
           'items_with_a_combined_claim': sum(1 for v in out.values() if v['n_combined']),
           'items_with_no_combined_claim': sorted(k for k, v in out.items() if not v['n_combined']),
           'combined_per_item': {k: v['n_combined'] for k, v in out.items()},
           'claims': out}
    json.dump(res, open(R('results/v2p8/partA.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'claims'}, indent=1))
    return res


if __name__ == '__main__':
    {'split': split, 'check': check, 'collect': collect}[sys.argv[1]]()
