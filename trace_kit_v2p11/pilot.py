"""pilot.py: v2.11 stricter acceptance, on Nano_Letters 10.1021/acs.nanolett.6b04294 only.

  python3 trace_kit_v2p11/pilot.py <step>

Steps, in order:
  seedsplit / seedsplitcheck / seedsplitcollect   take each seed key apart into atomic claims
  seedarms                                        the four arms on each seed
  seedgrade                                       grade every seed arm against the claim list
  validity                                        one judge per seed and per link
  stacked                                         concatenate arm A and arm C, grade the pile
  ledger                                          the v2.10 caveat ledger, per chain
  decide                                          the six gates; no model call

What is new here is not a harder grader, it is three questions v2.10 never asked.

  The seed was never tested. Every chain on this paper grows from a v2.5 two-step item that was
  written and kept without ever being put to the arms. A chain can only be as good as the thing
  it starts from, so the seed now faces the same gates as a link.

  Nothing checked whether the evidence can carry the claim at all. An item can pass every arm
  gate -- B really does beat A and C -- while the combined claim says something the two
  measurements cannot show between them. The validity judge rules exactly that.

  Nothing checked whether the answer related the two sides or merely listed them. Arm B holds
  everything arm A and arm C hold, so B beating each of them separately is a low bar: stapling
  the two answers together clears it. The stacked baseline is that staple, graded.

Every verdict is model against model.
"""
import collections, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p6'))
from clean import clean  # noqa: E402

OUT = R('results/v2p11/nanolett.6b04294')
CALLS = os.path.join(OUT, 'calls')
PAPER = 'Nano_Letters__10.1021_acs.nanolett.6b04294'
MARGIN, LO, HI = 0.25, 0.10, 0.40
MIN_B, NBAR = 0.60, 0.25


# ---------------------------------------------------------------- data

def load():
    d = {'REC': {}, 'KEY': {}, 'DEC': {}, 'CLM': {}}
    for f in ('results/v2p9/pairs.json', 'results/v2p9/nextlink.json',
              'results/v2p10/deeper_d4.json', 'results/v2p10/deeper_d5.json'):
        for x in json.load(open(R(f)))['pairs_out']: d['REC'][x['item']] = x
    for f in ('results/v2p9/keys.json', 'results/v2p9/keys_nl.json',
              'results/v2p10/keys_d4.json', 'results/v2p10/keys_d5.json'):
        d['KEY'].update(json.load(open(R(f))))
    for f in ('results/v2p9/step4.json', 'results/v2p9/step4_nl.json',
              'results/v2p10/step4_d4.json', 'results/v2p10/step4_d5.json'):
        d['DEC'].update(json.load(open(R(f)))['items_out'])
    for f in ('results/v2p9/step2.json', 'results/v2p9/step2_nl.json',
              'results/v2p10/step2_d4.json', 'results/v2p10/step2_d5.json'):
        d['CLM'].update(json.load(open(R(f)))['items'])
    d['V25'] = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    d['SC'] = json.load(open(os.path.join(OUT, 'scope.json')))
    g = json.load(open(R(json.load(open(R('results/v3', PAPER, 'stitch.json')))['graph'])))
    d['N'] = {n['id']: n for n in g['nodes']}
    d['title'] = g.get('title') or PAPER
    return d


def seed_panels(x, d, node):
    """the crops belonging to one observation of a seed, by that observation's graph node"""
    ids = set((d['N'].get(node) or {}).get('panel_ids') or [])
    return [p for p in x['panels'] if p['panel_id'] in ids]


def panel_block(pans):
    if not pans: return '', ''
    b = '\n'.join(f"  {p['suffix']}   {os.path.realpath(p['crop'])}"
                  for p in pans if p.get('crop'))
    caps = ''.join(f"  {p['suffix']}: {p['caption_span'].strip()}\n"
                   for p in pans if p.get('caption_span'))
    return b, (('\nPanel captions as printed:\n' + caps) if caps else '')


def read(jid):
    f = os.path.join(CALLS, f'{jid}.out.txt')
    return open(f).read() if os.path.exists(f) else ''


def jload(t, want):
    """tolerant reader: plain, then fenced, then brace-scan that knows about string literals"""
    t = (t or '').strip()
    for cand in (t, re.sub(r'^```(?:json)?|```$', '', t, flags=re.M).strip()):
        try:
            j = json.loads(cand)
            if isinstance(j, dict) and want in j: return j
        except Exception: pass
    # a brace counter that ignores braces inside strings. The naive one in v2.5 choked on
    # Miller indices like {10-12}, and these replies quote paper text by design.
    out, d, st, esc, ins = [], 0, None, False, False
    for i, ch in enumerate(t):
        if ins:
            if esc: esc = False
            elif ch == '\\': esc = True
            elif ch == '"': ins = False
            continue
        if ch == '"': ins = True
        elif ch == '{':
            if d == 0: st = i
            d += 1
        elif ch == '}' and d:
            d -= 1
            if not d: out.append(t[st:i + 1])
    for o in sorted(out, key=len, reverse=True):
        for cand in (o, re.sub(r',(\s*[}\]])', r'\1', o)):
            try:
                j = json.loads(cand)
                if want in j: return j
            except Exception: continue
    return None


def job(jobs, jid, agent, text, tag):
    os.makedirs(CALLS, exist_ok=True)
    f = os.path.join(CALLS, f'{jid}.txt'); open(f, 'w').write(text)
    jobs.append({'id': jid, 'agent': agent, 'prompt': f,
                 'out': os.path.join(CALLS, f'{jid}.out.txt'), 'tag': tag})


def save(jobs, name):
    p = os.path.join(OUT, f'jobs_{name}.json')
    json.dump(jobs, open(p, 'w'), indent=1)
    print(f'{len(jobs)} calls -> {os.path.relpath(p, ROOT)}')
    return jobs


# ---------------------------------------------------------------- step 2: the seeds

SEED_SPLIT = """You are taking one answer key apart, not answering anything.

Below are two measurements from one paper and the key that was written for the two together. Break the key's proposition into short atomic claims -- one assertion each, no conjunctions -- and tag every claim with what it would take to reach it.

OBSERVATION A
{a}

OBSERVATION B
{b}

THE KEY'S PROPOSITION
{prop}

Tag each claim exactly one of:

  a            the claim restates or directly follows from OBSERVATION A alone. Someone holding
               only A could write it.
  b            the claim restates or directly follows from OBSERVATION B alone. Someone holding
               only B could write it.
  combined     the claim needs BOTH. Neither observation states it on its own, and it does not
               follow from either alone.

Be strict about "combined". A claim that merely mentions both sides is not combined; it has to assert something -- a link, a comparison, a consequence, a ruling-out -- that neither side carries. If in doubt, tag it a or b.

Keep each claim under 30 words and use the key's own wording where you can.

Return JSON and nothing else:
{{"claims": [{{"claim": "...", "tag": "a" | "b" | "combined"}}, ...]}}"""

SEED_CHECK = """You are checking someone else's labels. You have not seen their reasoning and should not try to reconstruct it.

OBSERVATION A
{a}

OBSERVATION B
{b}

Below are claims, each with a label. The labels mean:

  a            reachable from OBSERVATION A alone
  b            reachable from OBSERVATION B alone
  combined     needs both; neither observation states it or implies it on its own

For each claim, rule whether the label is right.

Rule "disagree" whenever a claim labelled combined is in fact reachable from one side alone -- that is the error that matters here, because a claim wrongly called combined would make an item look like it composes when it does not. Also rule "disagree" if a claim labelled a or b actually needs both.

Return JSON and nothing else, one entry per claim, in the same order:
{{"rulings": [{{"n": 1, "verdict": "agree" | "disagree", "correct_tag": "a" | "b" | "combined", "why": "at most 25 words"}}, ...]}}

THE CLAIMS
{claims}"""

SEED_ARM = """{q}

What the measurement says:
{obs}
{pans}{caps}
Answer as best you can from what you have. Do not refuse. Answer in prose, at most 250 words. Say what conclusion this justifies and say plainly what it leaves uncertain."""

SEED_N = """A paper was published with this title, in this journal:

  "{title}"
  {journal}

{q}

You have not been given any measurement, figure or earlier result from it. Give your best guess of what the paper concludes. Do not refuse.

Answer as best you can from what you have. Do not refuse. Answer in prose, at most 250 words. Say what conclusion this justifies and say plainly what it leaves uncertain."""

Q_ONE = ('What does this measurement establish on its own about {topic}? '
         'Say what it supports and what it leaves open.')


def topic_of(q):
    m = re.search(r'about ([^?]+?)(?:, and what| that neither|\?)', q)
    return (m.group(1).strip() if m else 'this paper\'s materials') .rstrip(',')


def seedsplit():
    d = load(); jobs = []
    for s in d['SC']['seeds']:
        x = d['V25'][s]
        job(jobs, f'{s}__split', 'net-writer',
            SEED_SPLIT.format(a=x['observation_a']['text'], b=x['observation_b']['text'],
                              prop=x['key']['proposition']), 'seedsplit')
    return save(jobs, 'seedsplit')


def seedsplitcheck():
    d = load(); jobs = []
    for s in d['SC']['seeds']:
        x = d['V25'][s]
        o = jload(read(f'{s}__split'), 'claims')
        if not o: print(f'  {s}: split unparsed'); continue
        cs = [c for c in o['claims'] if isinstance(c, dict) and c.get('claim')]
        json.dump(cs, open(os.path.join(CALLS, f'{s}__split.claims.json'), 'w'), indent=1)
        listing = '\n'.join(f"{i}. [{c.get('tag')}] {c['claim']}" for i, c in enumerate(cs, 1))
        job(jobs, f'{s}__splitcheck', 'net-contrib',
            SEED_CHECK.format(a=x['observation_a']['text'], b=x['observation_b']['text'],
                              claims=listing), 'seedsplitcheck')
    return save(jobs, 'seedsplitcheck')


def seedsplitcollect():
    """only claims both agents tag the same survive, exactly as v2.8 Part A"""
    d = load(); out = {}
    for s in d['SC']['seeds']:
        cs = json.load(open(os.path.join(CALLS, f'{s}__split.claims.json')))
        o = jload(read(f'{s}__splitcheck'), 'rulings') or {'rulings': []}
        byn = {int(r['n']): r for r in o['rulings']
               if isinstance(r, dict) and str(r.get('n', '')).strip().isdigit()}
        kept, dropped = [], []
        for i, c in enumerate(cs, 1):
            r = byn.get(i) or {}
            agree = (r.get('verdict') == 'agree')
            same = (r.get('correct_tag') == c.get('tag'))
            (kept if (agree or same) else dropped).append(
                {'claim': c['claim'], 'tag': c.get('tag'),
                 'checker': r.get('verdict'), 'correct_tag': r.get('correct_tag'),
                 'why': r.get('why', '')})
        lim = [{'claim': t} for t in (d['V25'][s]['key'].get('limits') or [])]
        out[s] = {'kept': kept, 'dropped': dropped, 'limits': lim,
                  'n_combined': sum(1 for c in kept if c['tag'] == 'combined')}
        print(f"{s}: {len(kept)} kept ({out[s]['n_combined']} combined), "
              f"{len(dropped)} dropped, {len(lim)} limits")
    json.dump(out, open(os.path.join(OUT, 'seed_claims.json'), 'w'), indent=1)
    return out


def seedarms():
    d = load(); jobs = []
    for s in d['SC']['seeds']:
        x = d['V25'][s]
        oa, ob = x['observation_a'], x['observation_b']
        pa, pb = seed_panels(x, d, oa['node']), seed_panels(x, d, ob['node'])
        topic = topic_of(x['question'])
        qn = Q_ONE.format(topic=topic)
        ba, ca = panel_block(pa); bb, cb = panel_block(pb)
        both_b, both_c = panel_block(pa + pb)
        P = lambda b: (f'\n\nFigure panels. Open every one of these with the Read tool before '
                       f'you answer:\n{b}\n' if b else '\n')
        # arm A and arm C are symmetric here: one observation each, with that observation's own
        # panels. A seed has no handed-forward text, so there is no narrow/full asymmetry to
        # control for -- both sides get the same one-measurement question.
        body = {
            'A': SEED_ARM.format(q=qn, obs='\n  ' + oa['text'], pans=P(ba), caps=ca),
            'C': SEED_ARM.format(q=qn, obs='\n  ' + ob['text'], pans=P(bb), caps=cb),
            'B': SEED_ARM.format(q=x['question'],
                                 obs=f"\n  Observation A: {oa['text']}\n  Observation B: {ob['text']}",
                                 pans=P(both_b), caps=both_c),
            'N': SEED_N.format(title=d['title'], journal=PAPER.split('__')[0].replace('_', ' '),
                               q=x['question']),
        }
        for arm in ('A', 'B', 'C', 'N'):
            job(jobs, f'{s}__arm{arm}1',
                'net-floor' if arm == 'N' else 'net-fullarm', body[arm], 'seedarm')
    return save(jobs, 'seedarms')




# ---------------------------------------------------------------- step 3: evidence validity

VALID = """You are judging whether the evidence below can carry the claims that were drawn from it. You are not judging whether the claims are true, and you are not answering the paper's question.

THE EVIDENCE THE ANSWERERS WERE GIVEN
{ev}

THE QUALIFICATIONS RECORDED ALONGSIDE THE KEY
{lims}

For each numbered claim below, rule one of:

  supported     the evidence above can establish this claim. Someone holding exactly this
                evidence, and nothing else, could justifiably assert it.
  overreaches   the evidence points this way but cannot settle it at the strength stated --
                it is asserted more firmly, more generally, or more absolutely than the
                evidence allows.
  unsupported   the evidence cannot show this at all. The techniques shown do not measure the
                quantity the claim is about, or the claim rules out something the evidence
                cannot rule out.

Judge the techniques, not the plausibility. A claim can be perfectly true of the material and still be "unsupported" here, if these particular measurements are not the kind that could show it. A negative or ruling-out claim ("no X", "X is absent", "X is not Y") needs evidence that could have detected X had it been there; if none of the evidence could, the claim is unsupported however likely it is.

For "overreaches" and "unsupported", name in "cannot_show" what the evidence cannot establish, and quote in "quote" the qualification or the observation text that says so. Quote verbatim; if nothing in the text above says it, leave "quote" empty and say so in "cannot_show".

Return JSON and nothing else, one entry per claim, in the same order:
{{"rulings": [{{"n": 1, "verdict": "supported" | "overreaches" | "unsupported", "cannot_show": "", "quote": ""}}, ...]}}

THE CLAIMS
{claims}"""


def claim_list(it, d, S):
    """combined claims first, then limits -- the same order the grader is given"""
    if it in S:
        v = S[it]
        out = [{'claim': c['claim'], 'kind': 'combined'}
               for c in v['kept'] if c['tag'] == 'combined']
        out += [{'claim': c['claim'], 'kind': 'limit'} for c in v['limits']]
        return out
    v = d['CLM'].get(it) or {}
    out = [{'claim': c['claim'], 'kind': 'combined'}
           for c in (v.get('kept') or []) if c['tag'] == 'combined']
    out += [{'claim': c['claim'], 'kind': 'limit'} for c in (v.get('limits') or [])]
    return out


def evidence_of(it, d):
    """what the arms actually saw, as text: observations, panel ids, captions"""
    if it in d['V25']:
        x = d['V25'][it]
        L = [f"Observation A ({x['observation_a'].get('technique')}): {x['observation_a']['text']}",
             f"Observation B ({x['observation_b'].get('technique')}): {x['observation_b']['text']}"]
        pans = x['panels']
        lims = x['key'].get('limits') or []
    else:
        x = d['REC'][it]; k = d['KEY'].get(it) or {}
        L = [f"The earlier result handed to this step: {x['input_result']}",
             f"The new measurement ({x['new_observation'].get('technique')}): "
             f"{x['new_observation']['text']}"]
        pans = x.get('panels') or []
        lims = list(x.get('input_limits') or []) + list(k.get('limits') or [])
    if pans:
        L.append('')
        L.append('Figure panels shown, with the captions as printed:')
        for p in pans:
            L.append(f"  {p['suffix']}: {(p.get('caption_span') or '').strip()}")
    L.append('')
    L.append('No arm was shown a whole figure; every panel above was supplied as a crop.')
    return '\n'.join(L), lims


def validity():
    d = load()
    S = json.load(open(os.path.join(OUT, 'seed_claims.json')))
    jobs = []
    for it in d['SC']['seeds'] + d['SC']['links']:
        cs = claim_list(it, d, S)
        comb = [c for c in cs if c['kind'] == 'combined']
        if not comb: print(f'  {it}: no combined claims'); continue
        ev, lims = evidence_of(it, d)
        job(jobs, f'{it}__validity', 'net-contrib',
            VALID.format(ev=ev,
                         lims='\n'.join('  - ' + str(t) for t in lims) or '  none recorded',
                         claims='\n'.join(f'{i}. {c["claim"]}' for i, c in enumerate(comb, 1))),
            'validity')
    return save(jobs, 'validity')


# ---------------------------------------------------------------- step 4: stacked baseline

GRADE = """You are checking one answer against a fixed list of claims. You are not judging whether the answer is good, and you are not comparing it with anything.

THE ANSWER
{answer}

For each numbered claim below, rule one of:

  stated        the answer asserts this claim, or asserts something that plainly carries it.
                Different wording is fine; the assertion has to be there.
  contradicted  the answer asserts something incompatible with this claim.
  absent        the answer neither asserts it nor denies it.

Quote the answer's own words for every "stated" and every "contradicted". If you cannot quote anything, the ruling is "absent" -- a claim you cannot point to in the text is not stated, however plausible it is that the answerer believed it.

Do not reward an answer for being cautious or for hedging. "Cannot be determined" is not a statement of the claim.

Return JSON and nothing else, one entry per claim, in the same order:
{{"rulings": [{{"n": 1, "verdict": "stated" | "contradicted" | "absent", "quote": "the answer's words, or \\"\\" when absent"}}, ...]}}

THE CLAIMS
{claims}"""

ARMDIRS = ['results/v2p9/arms', 'results/v2p9/arms_nl', 'results/v2p10/arms_d4',
           'results/v2p10/arms_d5']


def arm_answer(it, arm, d):
    """the stored arm reply: a seed's from this run, a link's from v2.9 or v2.10"""
    if it in d['V25']:
        return clean(read(f'{it}__arm{arm}1'))
    for dd in ARMDIRS:
        p = R(dd, f'{it}_{arm}1.out.txt')
        if os.path.exists(p): return clean(open(p).read())
    return ''


def stacked():
    """arm A's answer and arm C's answer, concatenated, nothing added, graded as one answer"""
    d = load()
    S = json.load(open(os.path.join(OUT, 'seed_claims.json')))
    jobs, miss = [], []
    for it in d['SC']['seeds'] + d['SC']['links']:
        a, c = arm_answer(it, 'A', d), arm_answer(it, 'C', d)
        if not a or not c: miss.append(it); continue
        cs = claim_list(it, d, S)
        pile = a.strip() + '\n\n' + c.strip()
        open(os.path.join(CALLS, f'{it}__stackedanswer.txt'), 'w').write(pile)
        job(jobs, f'{it}__stacked', 'net-grader',
            GRADE.format(answer=pile,
                         claims='\n'.join(f'{i}. {c_["claim"]}' for i, c_ in enumerate(cs, 1))),
            'stacked')
    if miss: print(f'  missing an A or C answer: {miss}')
    return save(jobs, 'stacked')


def seedgrade():
    d = load()
    S = json.load(open(os.path.join(OUT, 'seed_claims.json')))
    jobs = []
    for s in d['SC']['seeds']:
        cs = claim_list(s, d, S)
        listing = '\n'.join(f'{i}. {c["claim"]}' for i, c in enumerate(cs, 1))
        for arm in ('A', 'B', 'C', 'N'):
            ans = clean(read(f'{s}__arm{arm}1'))
            if not ans: print(f'  {s} arm {arm}: no answer'); continue
            job(jobs, f'{s}__grade{arm}1', 'net-grader',
                GRADE.format(answer=ans, claims=listing), 'seedgrade')
    json.dump({s: claim_list(s, d, S) for s in d['SC']['seeds']},
              open(os.path.join(OUT, 'seed_claim_index.json'), 'w'), indent=1)
    return save(jobs, 'seedgrade')


# ---------------------------------------------------------------- step 5: the six gates

def rulings_of(t):
    o = jload(t, 'rulings')
    if o: return o['rulings']
    rs = [{'n': int(a), 'verdict': b} for a, b in
          re.findall(r'"n"\s*:\s*(\d+)\s*,\s*"verdict"\s*:\s*"(\w+)"', t or '')]
    return rs


def grade_scores(text, cs):
    """combined score, limit score and contradiction count, exactly as v2.9 scored them"""
    rs = rulings_of(text)
    if not rs: return None
    byn = {int(r['n']): r for r in rs if str(r.get('n', '')).strip().isdigit()}
    nc = sum(1 for c in cs if c['kind'] == 'combined')
    nl = sum(1 for c in cs if c['kind'] == 'limit')
    c_ = l_ = con = 0
    rows = []
    for i, c in enumerate(cs, 1):
        r = byn.get(i) or {}
        v = (r.get('verdict') or '').strip().lower()
        q = (r.get('quote') or '').strip()
        # v2.9's rule: "stated" with nothing quoted is not stated
        if v == 'stated' and not q: v = 'absent'
        if v == 'stated':
            if c['kind'] == 'combined': c_ += 1
            else: l_ += 1
        elif v == 'contradicted': con += 1
        rows.append({'n': i, 'kind': c['kind'], 'claim': c['claim'], 'verdict': v or 'absent',
                     'quote': q[:300]})
    return {'combined': round(c_ / nc, 4) if nc else None,
            'limit': round(l_ / nl, 4) if nl else None,
            'contradictions': con, 'n_combined': nc, 'n_limit': nl, 'rows': rows}


def link_scores(it, d):
    """the four arm means already decided in v2.9 or v2.10, reused unchanged"""
    v = d['DEC'].get(it)
    if not v: return None
    return {'A': v['mean_combined'].get('A'), 'B': v['mean_combined'].get('B'),
            'C': v['mean_combined'].get('C'), 'N': v['mean_combined'].get('N'),
            'limit': v.get('mean_limit') or {},
            'contradictions': (v.get('mean_contradictions') or {}).get('B'),
            'borderline': bool(v.get('borderline')), 'samples': v.get('samples')}


def gates(it, d, S, sc, stack, val):
    """the six gates. Every one is a fact already on disk; nothing is judged here."""
    g, why = {}, {}
    A, B, C, N = sc.get('A'), sc.get('B'), sc.get('C'), sc.get('N')
    lim = sc.get('limit') or {}
    bA = None if (B is None or A is None) else round(B - A, 4)
    bC = None if (B is None or C is None) else round(B - C, 4)
    bS = None if (B is None or stack is None) else round(B - stack, 4)

    g['1_dependency'] = bool(bA is not None and bC is not None
                             and bA >= MARGIN and bC >= MARGIN)
    why['1_dependency'] = f'B-A {bA:+.2f}, B-C {bC:+.2f}, both must be >= +{MARGIN:.2f}' \
        if bA is not None and bC is not None else 'a score is missing'

    g['2_relation'] = bool(bS is not None and bS >= MARGIN)
    why['2_relation'] = (f'B {B:.2f} vs stacked {stack:.2f}, B-stacked {bS:+.2f}, '
                         f'must be >= +{MARGIN:.2f}') if bS is not None else 'no stacked score'

    g['3_absolute'] = bool(B is not None and B >= MIN_B)
    why['3_absolute'] = f'B {B:.2f}, must be >= {MIN_B:.2f}' if B is not None else 'no B score'

    con = sc.get('contradictions')
    g['4_no_contradictions'] = bool(con is not None and con == 0)
    why['4_no_contradictions'] = f'{con} contradicted claim(s) in arm B' if con is not None \
        else 'contradiction count not recorded'

    lb, lc = lim.get('B'), lim.get('C')
    g['5_caveats'] = bool(lb is not None and lc is not None and lb >= lc)
    why['5_caveats'] = (f"B's limit score {lb:.2f} vs C's {lc:.2f}, B must be >= C"
                        if lb is not None and lc is not None else 'a limit score is missing')

    bad = [v for v in val if v['verdict'] in ('unsupported', 'overreaches')
           and not v.get('excused')]
    g['6_validity'] = not bad
    why['6_validity'] = (f'{len(bad)} combined claim(s) ruled '
                         + ', '.join(sorted({v['verdict'] for v in bad})) if bad
                         else f'all {len(val)} combined claims ruled supported'
                         + (f' ({sum(1 for v in val if v.get("excused"))} overreach excused '
                            f'because the key already states that limit)'
                            if any(v.get('excused') for v in val) else ''))

    first = next((k for k in sorted(g) if not g[k]), None)
    return {'gates': g, 'why': why, 'passed': all(g.values()), 'first_failed': first,
            'B_minus_A': bA, 'B_minus_C': bC, 'B_minus_stacked': bS,
            'scores': {'A': A, 'B': B, 'C': C, 'N': N, 'stacked': stack,
                       'limit_B': lb, 'limit_C': lc, 'contradictions': con},
            'additive_not_relational': bool(g['1_dependency'] and not g['2_relation'])}


def excuse(v, lims):
    """an overreach the key already owns is not a new fault -- gate 6 says so explicitly"""
    if v['verdict'] != 'overreaches': return False
    q = (v.get('quote') or '').strip()
    if not q: return False
    return any(q[:60].lower() in str(t).lower() for t in lims)


def families(d):
    """chains grouped by shared prefix.

    Sharing a seed is not sharing a prefix: C85 grows from the same two-step item as C19 and
    C20 but takes a different first link, so it is its own family. The grouping key is the root
    link, and the shared depth is the seed plus the links every chain in the group has in common.
    """
    ch = d['SC']['chains']
    g = collections.defaultdict(list)
    for cid, c in ch.items(): g[c['steps'][0]].append(cid)
    out = {}
    for i, (root, ids) in enumerate(sorted(g.items(), key=lambda kv: sorted(kv[1])), 1):
        ids = sorted(ids)
        pre = None
        for cid in ids:
            st = ch[cid]['steps']
            pre = list(st) if pre is None else [a for a, b in zip(pre, st) if a == b]
        out[f'F{i}'] = {'seed': ch[ids[0]]['seed'], 'root': root,
                        'shared_links': pre, 'shared_steps': 1 + len(pre),
                        'chains': ids}
    return out


def decide():
    d = load()
    S = json.load(open(os.path.join(OUT, 'seed_claims.json')))
    SIX = json.load(open(os.path.join(OUT, 'seed_claim_index.json')))
    units, stack_rows = {}, []
    for it in d['SC']['seeds'] + d['SC']['links']:
        cs = claim_list(it, d, S)
        is_seed = it in d['V25']
        # scores
        if is_seed:
            sc = {}
            for arm in ('A', 'B', 'C', 'N'):
                g = grade_scores(read(f'{it}__grade{arm}1'), cs)
                sc[arm] = g['combined'] if g else None
                if arm in ('B', 'C'): sc.setdefault('limit', {})[arm] = g['limit'] if g else None
                if arm == 'B': sc['contradictions'] = g['contradictions'] if g else None
            sc['borderline'] = False; sc['samples'] = 1
        else:
            sc = link_scores(it, d) or {}
        # stacked
        st = grade_scores(read(f'{it}__stacked'), cs)
        sc_stack = st['combined'] if st else None
        stack_rows.append({'unit': it, 'seed': is_seed, 'B': sc.get('B'),
                           'A': sc.get('A'), 'C': sc.get('C'), 'stacked': sc_stack})
        # validity
        comb = [c for c in cs if c['kind'] == 'combined']
        lims = [c['claim'] for c in cs if c['kind'] == 'limit']
        vr = rulings_of(read(f'{it}__validity'))
        byn = {int(r['n']): r for r in vr if str(r.get('n', '')).strip().isdigit()}
        val = []
        for i, c in enumerate(comb, 1):
            r = byn.get(i) or {}
            v = {'n': i, 'claim': c['claim'],
                 'verdict': (r.get('verdict') or 'unruled').strip().lower(),
                 'cannot_show': (r.get('cannot_show') or '').strip(),
                 'quote': (r.get('quote') or '').strip()}
            v['excused'] = excuse(v, lims)
            val.append(v)
        units[it] = {'is_seed': is_seed, 'claims': cs, 'validity': val,
                     **gates(it, d, S, sc, sc_stack, val)}
        units[it]['scores']['stacked'] = sc_stack
        units[it]['borderline'] = sc.get('borderline'); units[it]['samples'] = sc.get('samples')

    # chains
    chains = {}
    for cid, c in d['SC']['chains'].items():
        seq = [c['seed']] + c['steps']
        fails = [u for u in seq if not units[u]['passed']]
        chains[cid] = {'depth': c['depth'], 'seed': c['seed'], 'steps': c['steps'],
                       'units': seq, 'failing_units': fails,
                       'first_failing_unit': fails[0] if fails else None,
                       'first_failed_gate': units[fails[0]]['first_failed'] if fails else None,
                       'gates_passed': not fails, 'v2p10_accepted': True}
    fam = families(d)
    for f, v in fam.items():
        v['accepted'] = [c for c in v['chains'] if chains[c]['gates_passed']]
        v['rejected'] = [c for c in v['chains'] if not chains[c]['gates_passed']]

    res = {'note': 'v2.11 Step 5: the six gates on every seed and link, then the chains.',
           'paper': PAPER, 'units': units, 'chains': chains, 'families': fam,
           'stacked_table': stack_rows}
    json.dump(res, open(os.path.join(OUT, 'decide.json'), 'w'), indent=1)
    np_ = sum(1 for u in units.values() if u['passed'])
    print(f"{np_} of {len(units)} units pass all six gates")
    for it, u in units.items():
        tag = 'seed' if u['is_seed'] else 'link'
        print(f"  [{tag}] {it[:54]:54s} {'PASS' if u['passed'] else 'FAIL ' + str(u['first_failed'])}")
    print()
    print(f"{sum(1 for c in chains.values() if c['gates_passed'])} of {len(chains)} chains accepted; "
          f"{sum(1 for v in fam.values() if v['accepted'])} of {len(fam)} families have one")
    return res


# ---------------------------------------------------------------- the caveat ledger

LEDGER = """A chain of reasoning attached qualifications to its intermediate results. The question is whether the chain's final conclusion still respects them.

THE QUALIFICATIONS, in the order the chain attached them
{limits}

THE CHAIN'S FINAL CONCLUSION
{final}

For each qualification, rule how the final conclusion stands towards it:

  respects      the final conclusion stays inside the qualification, or restates it, or is about
                something the qualification does not touch while not overreaching it.
  ignores       the final conclusion asserts something the qualification says the evidence
                cannot support, without acknowledging it.
  contradicts   the final conclusion asserts the opposite of the qualification.

Quote the words of the final conclusion that decide each ruling. If you cannot quote anything, the ruling is "respects".

Return JSON and nothing else:
{{"rulings": [{{"n": 1, "verdict": "respects" | "ignores" | "contradicts", "quote": "...", "why": "at most 30 words"}}, ...]}}"""


def chain_limits(cid, d):
    """every qualification the chain collected, seed first, in the order attached"""
    c = d['SC']['chains'][cid]
    out = [('seed', str(t)) for t in (d['V25'][c['seed']]['key'].get('limits') or [])]
    for i, st in enumerate(c['steps'], 2):
        for t in ((d['KEY'].get(st) or {}).get('limits') or []):
            out.append((f'step {i}', str(t)))
    return out


def ledger():
    d = load(); jobs = []
    for cid, c in sorted(d['SC']['chains'].items()):
        lim = chain_limits(cid, d)
        fin = (d['KEY'].get(c['steps'][-1]) or {}).get('proposition') or ''
        job(jobs, f'{cid}__ledger', 'net-contrib',
            LEDGER.format(limits='\n'.join(f'{i}. [{w}] {t}' for i, (w, t) in enumerate(lim, 1))
                          or '  none recorded', final=fin), 'ledger')
    return save(jobs, 'ledger')


def ledgercollect():
    d = load()
    res = {}
    for cid in sorted(d['SC']['chains']):
        lim = chain_limits(cid, d)
        rs = rulings_of(read(f'{cid}__ledger'))
        byn = {int(r['n']): r for r in rs if str(r.get('n', '')).strip().isdigit()}
        rows = []
        for i, (w, t) in enumerate(lim, 1):
            r = byn.get(i) or {}
            v = r.get('verdict') if r.get('verdict') in ('respects', 'ignores', 'contradicts') \
                else None
            rows.append({'n': i, 'where': w, 'limit': t, 'verdict': v,
                         'quote': (r.get('quote') or '').strip(),
                         'why': (r.get('why') or '').strip()})
        bad = [x for x in rows if x['verdict'] in ('ignores', 'contradicts')]
        res[cid] = {'rows': rows, 'n': len(rows), 'bad': len(bad),
                    'ledger_rejects': bool(bad),
                    'counts': dict(collections.Counter(x['verdict'] or 'unruled' for x in rows))}
        print(f"{cid}: {len(rows)} qualifications, {res[cid]['counts']}")
    json.dump(res, open(os.path.join(OUT, 'ledger.json'), 'w'), indent=1)
    return res


if __name__ == '__main__':
    F = {'seedsplit': seedsplit, 'seedsplitcheck': seedsplitcheck,
         'seedsplitcollect': seedsplitcollect, 'seedarms': seedarms,
         'seedgrade': seedgrade, 'validity': validity, 'stacked': stacked, 'decide': decide, 'ledger': ledger, 'ledgercollect': ledgercollect}
    F[sys.argv[1]]()
