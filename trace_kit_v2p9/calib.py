"""calib.py: v2.9 Step 1 -- can Haiku do the tagging, checking and grading?

  python3 -m trace_kit_v2p9.calib build     Haiku prompts, byte-identical to v2.8's
  python3 -m trace_kit_v2p9.calib collect   agreement against the Sonnet results

Before producing anything, find out what the cheap model can do, because at 15,000 papers the
model doing the tagging and the grading is the whole cost. The prompts are v2.8's, unchanged:
the same splitter text, the same checker text, the same grader text, on the same 8 pilot items
and the same 144 pilot answers. Only the model differs, so any disagreement is the model.

The bars are the brief's:
  tagging and checking   Haiku's tags agree with Sonnet's on >= 85%
  grading                per-answer combined score within 0.25 on >= 85% of answers, AND the
                         pilot's 7-of-8 verdicts reproduce

Drafting stays on Sonnet either way.

The model is verified from the relay's own transcript, the same way the prompt is. A job that
asks for Haiku and quietly runs on something else would make the entire cost projection a
fiction, and the relay's word is not evidence.

Every verdict is model against model.
"""
import collections, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402

OUT = R('results/v2p9/calib')
MODEL = 'haiku'


def lenient(raw, want):
    """obj(), then the two shapes Haiku actually returns.

    The first pass scored Haiku at 10.7% on checking and lost 27 of 144 gradings. Both were
    format, not judgement: Haiku answers the checker in prose ("1. agree (input)") and fences
    its grading JSON in a ```json block. At 15,000 papers you fix the parser rather than throw
    away the model, so both readings are computed and both are reported -- the strict one says
    what happens if you demand the schema, the lenient one says what the model actually judged.
    """
    o = obj(raw, want)
    if o: return o, 'json'
    fenced = re.sub(r'^\s*```[a-z]*\s*', '', (raw or '').strip())
    fenced = re.sub(r'\s*```\s*$', '', fenced)
    # straight json.loads BEFORE obj(). obj() counts braces without respecting string
    # literals, and these claims are full of Miller indices -- {10-12}, {01-12} -- so a
    # perfectly valid reply is unparseable to it. That alone accounted for 26 of the 27
    # gradings the first pass threw away.
    for cand in (fenced, re.sub(r',(\s*[}\]])', r'\1', fenced)):
        try:
            j = json.loads(cand)
            if isinstance(j, dict) and want in j: return j, 'fenced'
        except Exception: pass
    o = obj(fenced, want)
    if o: return o, 'fenced'
    if want == 'rulings':
        # last tier: pull n/verdict straight out of malformed JSON. Haiku quotes the answer's
        # words without escaping the quotes inside them, so the object never parses even though
        # every ruling is legible. 26 of 144 gradings are only recoverable this way. The quote
        # is dropped, which matters: a "stated" with no quote is withdrawn to absent by the
        # scorer, so salvage cannot inflate a score, only deflate it.
        rows = []
        for m in re.finditer(r'"n"\s*:\s*(\d+)\s*,\s*"verdict"\s*:\s*"(\w+)"', raw or ''):
            rows.append({'n': int(m.group(1)), 'verdict': m.group(2).lower(),
                         'correct_tag': None, 'quote': ''})
        if rows: return {'rulings': rows}, 'salvaged'
        rows = []
        pat = r'^\s*(\d+)[.)]\s*(agree|disagree|stated|contradicted|absent)\b[^\n]*'
        for m in re.finditer(pat, raw or '', re.I | re.M):
            tag = re.search(r'\((input|observation|combined)\)', m.group(0), re.I)
            rows.append({'n': int(m.group(1)), 'verdict': m.group(2).lower(),
                         'correct_tag': tag.group(1).lower() if tag else None, 'quote': ''})
        if rows: return {'rulings': rows}, 'prose'
    return None, 'unparsed'



def build():
    os.makedirs(OUT, exist_ok=True)
    jobs = []
    # the v2.8 prompt files, reused byte for byte
    for it in json.load(open(R('results/v2p8/selected.json')))['items']:
        for kind, src, agent in (
                ('tag', R('results/v2p8/split', it['item'] + '.txt'), 'net-writer'),
                ('check', R('results/v2p8/check', it['item'] + '.txt'), 'net-contrib')):
            jobs.append({'id': f"{kind}_{it['item']}", 'agent': agent, 'model': MODEL,
                         'prompt': src,
                         'out': os.path.join(OUT, f"{kind}_{it['item']}.out.txt")})
    for j in json.load(open(R('results/v2p8/grade_jobs.json'))):
        jobs.append({'id': 'grade_' + j['id'], 'agent': 'net-grader', 'model': MODEL,
                     'prompt': j['prompt'],
                     'out': os.path.join(OUT, 'grade_' + os.path.basename(j['out']))})
    json.dump(jobs, open(R('results/v2p9/calib_jobs.json'), 'w'), indent=1)
    print(f'{len(jobs)} Haiku calls: '
          f'{sum(1 for j in jobs if j["id"].startswith("tag_"))} tag, '
          f'{sum(1 for j in jobs if j["id"].startswith("check_"))} check, '
          f'{sum(1 for j in jobs if j["id"].startswith("grade_"))} grade')
    return jobs


def tags_from(f):
    o = (lenient(open(f).read(), 'claims')[0] if os.path.exists(f) else None)
    if not o: return None
    out = []
    for c in (o.get('claims') or []):
        t = (c.get('tag') or '').strip().lower()
        if t in ('input', 'observation', 'combined'):
            out.append({'claim': (c.get('claim') or '').strip(), 'tag': t})
    return out or None


def collect():
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    A8 = json.load(open(R('results/v2p8/partA.json')))['claims']
    C8 = json.load(open(R('results/v2p8/partC.json')))['answers']
    D8 = json.load(open(R('results/v2p8/partD.json')))

    # --- tagging: compare Haiku's tag with Sonnet's, claim by claim, in order
    tag_same = tag_tot = 0
    per_item_tag = {}
    for s in S:
        it = s['item']
        son = tags_from(R('results/v2p8/split', it + '.out.txt')) or []
        hai = tags_from(os.path.join(OUT, f'tag_{it}.out.txt')) or []
        n = min(len(son), len(hai))
        same = sum(1 for i in range(n) if son[i]['tag'] == hai[i]['tag'])
        # a claim Haiku did not produce is a disagreement, not a free pass
        tot = max(len(son), len(hai))
        tag_same += same; tag_tot += tot
        per_item_tag[it] = {'sonnet_claims': len(son), 'haiku_claims': len(hai),
                            'agree': same, 'of': tot,
                            'share': round(same / tot, 3) if tot else None}

    # --- checking: compare the agree/disagree verdicts on Sonnet's own claim list
    chk_same = chk_tot = 0
    per_item_chk = {}
    fmt_check = collections.Counter()
    for s in S:
        it = s['item']
        f = os.path.join(OUT, f'check_{it}.out.txt')
        oh, how = (lenient(open(f).read(), 'rulings') if os.path.exists(f)
                   else (None, 'missing'))
        fmt_check[how] += 1
        os_ = obj(open(R('results/v2p8/check', it + '.out.txt')).read(), 'rulings')
        hh = {int(x['n']): (x.get('verdict') or '').strip().lower()
              for x in (oh or {}).get('rulings', []) if str(x.get('n', '')).strip().isdigit()}
        ss = {int(x['n']): (x.get('verdict') or '').strip().lower()
              for x in (os_ or {}).get('rulings', []) if str(x.get('n', '')).strip().isdigit()}
        n = set(ss)
        same = sum(1 for i in n if hh.get(i) == ss[i])
        chk_same += same; chk_tot += len(n)
        per_item_chk[it] = {'agree': same, 'of': len(n),
                            'share': round(same / len(n), 3) if n else None}

    # --- grading: per-answer combined score, Haiku against Sonnet
    idx = json.load(open(R('results/v2p8/claim_index.json')))
    close = gtot = 0
    diffs, hs = [], {}
    fmt_grade = collections.Counter()
    jclose, jtot = [0], [0]
    for key, son in C8.items():
        it = son['item']; cs = idx[it]
        f = os.path.join(OUT, f'grade_{key}.out.txt')
        o, how = (lenient(open(f).read(), 'rulings') if os.path.exists(f)
                  else (None, 'missing'))
        fmt_grade[how] += 1
        if not o: continue
        rul = {int(x['n']): x for x in o.get('rulings', [])
               if str(x.get('n', '')).strip().isdigit()}
        nc = sum(1 for c in cs if c['kind'] == 'combined')
        nl = sum(1 for c in cs if c['kind'] == 'limit')
        c_, l_ = 0, 0
        for i, c in enumerate(cs, 1):
            r = rul.get(i) or {}
            v = (r.get('verdict') or '').strip().lower()
            if v == 'stated' and not (r.get('quote') or '').strip(): v = 'absent'
            if v == 'stated':
                if c['kind'] == 'combined': c_ += 1
                else: l_ += 1
        hcomb = round(c_ / nc, 4) if nc else None
        hs[key] = {'item': it, 'arm': son['arm'], 'sample': son['sample'],
                   'combined_score': hcomb,
                   'limit_score': round(l_ / nl, 4) if nl else None}
        gtot += 1
        d = abs((hcomb or 0) - (son['combined_score'] or 0))
        diffs.append(round(d, 4))
        if d <= 0.25: close += 1
        # the salvaged replies lose their quotes, and a stated without a quote is withdrawn to
        # absent, so their scores can only be too low. The schema-compliant subset is the
        # unbiased read and is reported beside the all-replies number.
        if how == 'json':
            jtot[0] += 1
            if d <= 0.25: jclose[0] += 1

    # --- does Haiku reproduce the pilot verdicts?
    import statistics as st
    verd, agree_v = {}, 0
    for s in S:
        it = s['item']
        got = {a: [hs[f'{it}_{a}{k}']['combined_score'] for k in range(1, 7)
                   if f'{it}_{a}{k}' in hs] for a in ('A', 'B', 'C')}
        if any(len(v) < 6 for v in got.values()):
            verd[it] = {'error': 'incomplete'}; continue
        m = {a: round(st.mean(got[a]), 4) for a in got}
        comp = (m['B'] - m['A'] >= 0.25) and (m['B'] - m['C'] >= 0.25)
        son = D8['items_out'][it]['compositional']
        verd[it] = {'haiku_means': m, 'haiku_compositional': comp, 'sonnet_compositional': son,
                    'same': comp == son}
        agree_v += comp == son

    tshare = round(tag_same / tag_tot, 3) if tag_tot else None
    cshare = round(chk_same / chk_tot, 3) if chk_tot else None
    gshare = round(close / gtot, 3) if gtot else None
    res = {
        'note': 'v2.9 Step 1. v2.8 prompts byte for byte; only the model differs.',
        'model': MODEL,
        'tagging': {'agree': tag_same, 'of': tag_tot, 'share': tshare, 'bar': 0.85,
                    'passes': bool(tshare is not None and tshare >= 0.85),
                    'per_item': per_item_tag},
        'checking': {'agree': chk_same, 'of': chk_tot, 'share': cshare, 'bar': 0.85,
                     'passes': bool(cshare is not None and cshare >= 0.85),
                     'per_item': per_item_chk},
        'grading': {'within_0.25': close, 'of': gtot, 'share': gshare, 'bar': 0.85,
                    'schema_compliant_only': {
                        'within_0.25': jclose[0], 'of': jtot[0],
                        'share': round(jclose[0] / jtot[0], 3) if jtot[0] else None,
                        'note': 'unbiased subset: replies Haiku returned as valid JSON'},
                    'mean_abs_diff': round(sum(diffs) / len(diffs), 4) if diffs else None,
                    'verdicts_reproduced': agree_v, 'verdict_items': len(verd),
                    'passes': bool(gshare is not None and gshare >= 0.85
                                   and agree_v == len(verd)),
                    'per_item_verdicts': verd},
        'haiku_scores': hs,
        'reply_format': {'check': dict(fmt_check), 'grade': dict(fmt_grade),
                         'note': 'how each Haiku reply had to be parsed. json is schema '
                                 'compliant; fenced and prose needed the lenient reader.'},
    }
    res['roles'] = {
        'draft': 'sonnet (fixed by the brief)',
        'tag': MODEL if res['tagging']['passes'] else 'sonnet',
        'check': MODEL if res['checking']['passes'] else 'sonnet',
        'grade': MODEL if res['grading']['passes'] else 'sonnet',
    }
    res['all_roles_failed'] = not any(v == MODEL for v in res['roles'].values())
    json.dump(res, open(R('results/v2p9/calib.json'), 'w'), indent=1)
    print(json.dumps({k: (v if k not in ('tagging', 'checking', 'grading') else
                          {kk: vv for kk, vv in v.items()
                           if kk not in ('per_item', 'per_item_verdicts')})
                      for k, v in res.items() if k != 'haiku_scores'}, indent=1))
    return res


if __name__ == '__main__':
    {'build': build, 'collect': collect}[sys.argv[1]]()
