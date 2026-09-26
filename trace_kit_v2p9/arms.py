"""arms.py: v2.9 Step 3 -- four arms per item, one sample each.

  python3 -m trace_kit_v2p9.arms build [borderline]
  python3 -m trace_kit_v2p9.arms grade [borderline]
  python3 -m trace_kit_v2p9.arms collect

  arm A  the new measurement with its panels, v2.8's narrow question
  arm B  the measurement plus the earlier result, v2.8's full question
  arm C  the earlier result alone, v2.8's narrow question
  arm N  the paper named -- title and journal -- and the full question, no evidence at all

Arm N is different here from v2.8b, and deliberately. There it was given a blanked document and
refused in 48 of 48 samples, which measured whether the model WILL answer rather than whether it
COULD. This time it gets the paper's real title and journal and is told to guess and not refuse.
If it can state the key's combined claims from a title, the item was never a test of reasoning.

Every arm carries "Answer as best you can from what you have. Do not refuse.", so a low score is
a failure to reach the claims rather than a decision to stay silent.

Every verdict is model against model.
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402
from trace_kit_v2p6.clean import clean  # noqa: E402
from trace_kit_v2p8.partB import Q_A, topic_of  # noqa: E402
from trace_kit_v2p8.partC import ASK  # noqa: E402

# same recipe for the depth-2 pairs and the depth-3 next links; only the source and suffix differ
SRC = os.environ.get('V2P9_SRC', 'results/v2p9/pairs.json')
TAG = os.environ.get('V2P9_TAG', '')
ARMS = R('results/v2p9/arms' + TAG)
GRADE = R('results/v2p9/grade' + TAG)
TAIL = ("Answer as best you can from what you have. Do not refuse. Answer in prose, at most 250 "
        "words. Say what conclusion this justifies and say plainly what it leaves uncertain.")

WITH_OBS = """{q}

What the measurement says:

  {obs}

Figure panels. Open every one of these with the Read tool before you answer:
{pans}
{caps}{inp}
{tail}"""

ONLY_INPUT = """{q}

You have no new measurement for this step. What you have is a result an earlier step already established, which you may treat as settled:

{inp}
{lims}

{tail}"""

NAMED = """A paper was published with this title, in this journal:

  "{title}"
  {journal}

{q}

You have not been given any measurement, figure or earlier result from it. Give your best guess of what the paper concludes. Do not refuse.

{tail}"""


def title_of(paper, _c={}):
    if paper not in _c:
        gp = json.load(open(R('results/v3', paper, 'stitch.json')))['graph']
        _c[paper] = json.load(open(R(gp))).get('title') or paper
    return _c[paper]


def live():
    S2 = json.load(open(R('results/v2p9/step2%s.json' % TAG)))['items']
    P = {x['item']: x for x in json.load(open(R(SRC)))['pairs_out']}
    return [(k, P[k], v) for k, v in S2.items() if v['alive'] and k in P]


def build(which='first'):
    os.makedirs(ARMS, exist_ok=True)
    jobs = []
    items = live()
    if which == 'borderline':
        items = [(k, x, v) for k, x, v in items
                 if k in set(json.load(open(R('results/v2p9/borderline%s.json' % TAG))))]
        sfx, arms = '2', ('A', 'B', 'C')
    else:
        sfx, arms = '1', ('A', 'B', 'C', 'N')
    for it, x, v in items:
        pans = '\n'.join(f"  {p['suffix']}   {os.path.realpath(p['crop'])}"
                         for p in x['panels'] if p.get('crop'))
        caps = ''.join(f"  {p['suffix']}: {p['caption_span'].strip()}\n"
                       for p in x['panels'] if p.get('caption_span'))
        caps = ('\nPanel captions as printed:\n' + caps + '\n') if caps else '\n'
        lims = ('\nThe qualifications recorded on that earlier result:\n'
                + '\n'.join('  - ' + t for t in x['input_limits'])) if x['input_limits'] \
            else '\nNo qualifications were recorded on that earlier result.'
        qf = x['question']; qn = Q_A.format(topic=topic_of(qf))
        body = {
            'A': WITH_OBS.format(q=qn, obs=x['new_observation']['text'], pans=pans, caps=caps,
                                 inp='', tail=TAIL),
            'B': WITH_OBS.format(q=qf, obs=x['new_observation']['text'], pans=pans, caps=caps,
                                 inp='An earlier step in this work already established the '
                                     'following, and you may treat it as settled:\n\n'
                                     + x['input_result'] + lims + '\n', tail=TAIL),
            'C': ONLY_INPUT.format(q=qn, inp=x['input_result'], lims=lims, tail=TAIL),
            'N': NAMED.format(title=title_of(x['paper']),
                              journal=x['paper'].split('__')[0].replace('_', ' '),
                              q=qf, tail=TAIL),
        }
        for arm in arms:
            f = os.path.join(ARMS, f'{it}_{arm}{sfx}.txt')
            open(f, 'w').write(body[arm])
            jobs.append({'id': f'{it}_{arm}{sfx}', 'agent':
                         'net-floor' if arm in ('C', 'N') else 'net-fullarm',
                         'prompt': f, 'out': os.path.join(ARMS, f'{it}_{arm}{sfx}.out.txt')})
    n = R('results/v2p9/arm_jobs_%s%s.json' % (which, TAG))
    json.dump(jobs, open(n, 'w'), indent=1)
    print(f'{len(jobs)} answers for {len(items)} items ({which})')
    return jobs


def claim_list(v):
    return ([{'claim': c['claim'], 'kind': 'combined'}
             for c in v['kept'] if c['tag'] == 'combined']
            + [{'claim': c['claim'], 'kind': 'limit'} for c in v['limits']])


def grade(which='first'):
    os.makedirs(GRADE, exist_ok=True)
    idx = {}
    jobs, miss = [], []
    for it, x, v in live():
        idx[it] = claim_list(v)
    json.dump(idx, open(R('results/v2p9/claim_index%s.json' % TAG), 'w'), indent=1)
    for j in json.load(open(R('results/v2p9/arm_jobs_%s%s.json' % (which, TAG)))):
        it = j['id'].rsplit('_', 1)[0]
        if not os.path.exists(j['out']): miss.append(j['id']); continue
        listing = '\n'.join(f"{i}. {c['claim']}" for i, c in enumerate(idx[it], 1))
        body = ASK.format(answer=clean(open(j['out']).read()), claims=listing)
        f = os.path.join(GRADE, j['id'] + '.txt'); open(f, 'w').write(body)
        jobs.append({'id': j['id'], 'agent': 'net-grader', 'prompt': f,
                     'out': os.path.join(GRADE, j['id'] + '.out.txt')})
    json.dump(jobs, open(R('results/v2p9/grade_jobs_%s%s.json' % (which, TAG)), 'w'), indent=1)
    print(f'{len(jobs)} gradings ({which}), {len(miss)} answers missing: {miss[:6]}')
    return jobs


def read_rulings(raw):
    """obj(), then json.loads, then a regex over the n/verdict pairs.

    Two failure modes seen in this run, both of which silently dropped a whole item from the
    denominator before they were caught. obj() counts braces without respecting string
    literals, so a claim quoting a Miller index like {10-12} breaks it; and a grader quoting
    the answer's words without escaping the quotes inside them produces JSON that never parses
    although every ruling is legible. The regex tier drops the quote, and a stated with no
    quote is withdrawn to absent below, so salvage can only lower a score, never raise it.
    """
    o = obj(raw, 'rulings')
    if o: return o
    t = re.sub(r'^\s*```[a-z]*\s*', '', (raw or '').strip())
    t = re.sub(r'\s*```\s*$', '', t)
    for cand in (t, re.sub(r',(\s*[}\]])', r'\1', t)):
        try:
            j = json.loads(cand)
            if isinstance(j, dict) and 'rulings' in j: return j
        except Exception: pass
    rows = [{'n': int(m.group(1)), 'verdict': m.group(2).lower(), 'quote': ''}
            for m in re.finditer(r'"n"\s*:\s*(\d+)\s*,\s*"verdict"\s*:\s*"(\w+)"', raw or '')]
    return {'rulings': rows} if rows else None


def score(it, arm, sfx, idx):
    f = os.path.join(GRADE, f'{it}_{arm}{sfx}.out.txt')
    o = read_rulings(open(f).read()) if os.path.exists(f) else None
    if not o: return None
    cs = idx[it]
    rul = {int(r['n']): r for r in o.get('rulings', [])
           if str(r.get('n', '')).strip().isdigit()}
    nc = sum(1 for c in cs if c['kind'] == 'combined')
    nl = sum(1 for c in cs if c['kind'] == 'limit')
    c_ = l_ = con = 0
    rows = []
    for i, c in enumerate(cs, 1):
        r = rul.get(i) or {}
        v = (r.get('verdict') or '').strip().lower()
        q = (r.get('quote') or '').strip()
        if v == 'stated' and not q: v = 'absent'
        if v == 'stated':
            if c['kind'] == 'combined': c_ += 1
            else: l_ += 1
        elif v == 'contradicted': con += 1
        rows.append({'n': i, 'kind': c['kind'], 'claim': c['claim'], 'verdict': v or 'absent',
                     'quote': q[:300]})
    return {'combined_score': round(c_ / nc, 4) if nc else None,
            'limit_score': round(l_ / nl, 4) if nl else None,
            'contradictions': con, 'rulings': rows}


if __name__ == '__main__':
    cmd = sys.argv[1]; which = sys.argv[2] if len(sys.argv) > 2 else 'first'
    {'build': build, 'grade': grade}[cmd](which)
