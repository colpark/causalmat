"""stage2.py: label the chain steps, then link each observation step to a panel.

  python3 groundchain_v1/stage2.py label      build the labelling calls (answerer, 1 per paper)
  python3 groundchain_v1/stage2.py collect    read them back
  python3 groundchain_v1/stage2.py link       build the link-confirmation calls (checker)
  python3 groundchain_v1/stage2.py linked     read them back, keep only author-supported links

The M2M chain is silver: an LLM wrote it and almost no step cites a figure. So a link is kept
only when the AUTHORS state that observation in their own text -- the caption span or the body
use sentence that match/v4 already attached to the panel. The checker rules on that one thing.
Every M2M claim with no author text behind it is logged, not quietly dropped.
"""
import collections, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CORPUS, OUT, ANSWERER, CHECKER

CALLS = os.path.join(OUT, 'calls')
STEP = re.compile(r'\[Begin Step (\d+)\](.*?)\[End Step \1\]', re.S)
KINDS = ('system', 'variable', 'observation', 'mechanism', 'conclusion')


def papers():
    """the fetched papers, in pick order"""
    P = json.load(open(os.path.join(OUT, 'select_picks.json')))['picks']
    out = []
    for x in P:
        for j in os.listdir(CORPUS):
            f = os.path.join(CORPUS, j, x['doi'].replace('/', '_'))
            if os.path.isdir(f):
                out.append({**x, 'folder': f}); break
    return out


def chain_of(doi):
    import csv
    csv.field_size_limit(10 ** 7)
    from config import CSV
    for r in csv.DictReader(open(CSV)):
        if r['doi'].strip() == doi:
            got = [(int(n), t.strip()) for n, t in STEP.findall(r['reasoning_process'])]
            return [t for _, t in sorted(got)], r
    return [], {}


def panels_of(folder):
    p = os.path.join(folder, 'panels', 'match.json')
    if not os.path.exists(p): return []
    out = []
    for f in json.load(open(p))['figures']:
        for pan in f.get('panels', []):
            out.append({'figure': f['file'], 'tier': f['tier'], 'label': pan.get('label'),
                        'crop': pan.get('crop'), 'definition': pan.get('definition'),
                        'use': pan.get('use') or [], 'panel_id': f"{f['file']}#{pan.get('label')}"})
    return out


LABEL = """Below is a six-step reasoning chain that an automated system wrote about one experimental paper. Label what each step is doing.

{chain}

Label each step exactly one of:

  system        names the material, device or setup being studied, without asserting a result.
  variable      names what was varied, substituted, controlled or compared.
  observation   states something that was measured or seen -- a trend, a value, a comparison,
                a feature in data. This is the kind of step a figure panel could show.
  mechanism     explains why, in terms of a process or cause.
  conclusion    states what the work establishes overall.

A step can describe a measurement and still be a `mechanism` if its point is the explanation. Judge the step's job in the chain, not its vocabulary.

For every step labelled `observation`, also give the single physical property it is about, in at most eight words, as `property`.

Return JSON and nothing else:
{{"steps": [{{"n": 1, "kind": "system|variable|observation|mechanism|conclusion", "property": ""}}, ...]}}"""


def label():
    jobs = []
    os.makedirs(CALLS, exist_ok=True)
    for p in papers():
        steps, _ = chain_of(p['doi'])
        if not steps: print(f"  {p['doi']}: no chain"); continue
        body = '\n'.join(f'[Step {i}] {t}' for i, t in enumerate(steps, 1))
        jid = p['doi'].replace('/', '_') + '__label'
        f = os.path.join(CALLS, jid + '.txt'); open(f, 'w').write(LABEL.format(chain=body))
        jobs.append({'id': jid, 'agent': ANSWERER['agent'], 'model': ANSWERER['model'],
                     'prompt': f, 'out': os.path.join(CALLS, jid + '.out.txt')})
    json.dump(jobs, open(os.path.join(OUT, 'jobs_label.json'), 'w'), indent=1)
    print(f'{len(jobs)} labelling calls')
    return jobs


def jload(t, want):
    t = (t or '').strip()
    for c in (t, re.sub(r'^```(?:json)?|```$', '', t, flags=re.M).strip()):
        try:
            j = json.loads(c)
            if isinstance(j, dict) and want in j: return j
        except Exception: pass
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
        try:
            j = json.loads(o)
            if want in j: return j
        except Exception: continue
    return None


def rd(jid):
    f = os.path.join(CALLS, jid + '.out.txt')
    return open(f).read() if os.path.exists(f) else ''


def collect():
    out = {}
    for p in papers():
        steps, _ = chain_of(p['doi'])
        jid = p['doi'].replace('/', '_') + '__label'
        j = jload(rd(jid), 'steps')
        if not j: print(f"  {p['doi']}: unparsed"); continue
        byn = {int(s['n']): s for s in j['steps'] if str(s.get('n', '')).strip().isdigit()}
        rows = []
        for i, t in enumerate(steps, 1):
            s = byn.get(i) or {}
            k = s.get('kind') if s.get('kind') in KINDS else None
            rows.append({'n': i, 'text': t, 'kind': k, 'property': (s.get('property') or '').strip()})
        out[p['doi']] = rows
        c = collections.Counter(r['kind'] for r in rows)
        print(f"  {p['doi'][:34]:34s} {dict(c)}")
    json.dump(out, open(os.path.join(OUT, 'steps.json'), 'w'), indent=1)
    return out


LINK = """A sentence below was written by an automated system summarising one paper. Separately, the paper's own authors wrote the caption and body text quoted underneath it. Rule whether the authors themselves state the same finding.

THE AUTOMATED SYSTEM'S SENTENCE
{claim}

THE AUTHORS' OWN TEXT FOR THIS FIGURE PANEL
caption: {definition}
body: {use}

Rule one of:

  states        the authors' text asserts the same finding about the same property. Different
                wording and extra detail are fine; the assertion has to be there.
  related       the authors' text is about the same panel or property but does not assert this
                particular finding.
  absent        the authors' text does not carry this finding at all.

Quote the authors' own words for `states`. If you cannot quote them, the ruling is not `states`.

Return JSON and nothing else:
{{"verdict": "states|related|absent", "quote": "", "property": "the property both are about, at most eight words"}}"""


def link():
    """one checker call per (observation step, candidate panel) -- the panel a caption or use
    sentence already mentions. The chain never cites figures, so the candidate set comes from
    match/v4's own definition and use spans, not from the chain."""
    S = json.load(open(os.path.join(OUT, 'steps.json')))
    jobs, cand = [], {}
    for p in papers():
        rows = S.get(p['doi']) or []
        pans = panels_of(p['folder'])
        for r in rows:
            if r['kind'] != 'observation': continue
            # score each panel by word overlap with the step, take the best few
            words = {w for w in re.findall(r'[a-z0-9]{4,}', r['text'].lower())}
            scored = []
            for pan in pans:
                txt = ((pan['definition'] or '') + ' ' + ' '.join(pan['use'])).lower()
                if not txt.strip(): continue
                ov = len(words & {w for w in re.findall(r'[a-z0-9]{4,}', txt)})
                if ov: scored.append((ov, pan))
            scored.sort(key=lambda x: -x[0])
            for ov, pan in scored[:2]:
                jid = f"{p['doi'].replace('/', '_')}__s{r['n']}__{re.sub(r'[^A-Za-z0-9]', '', pan['panel_id'])[:26]}"
                f = os.path.join(CALLS, jid + '.txt')
                open(f, 'w').write(LINK.format(
                    claim=r['text'], definition=pan['definition'] or '(none)',
                    use=' '.join(pan['use']) or '(none)'))
                jobs.append({'id': jid, 'agent': CHECKER['agent'], 'model': CHECKER['model'],
                             'prompt': f, 'out': os.path.join(CALLS, jid + '.out.txt')})
                cand[jid] = {'doi': p['doi'], 'step': r['n'], 'panel': pan['panel_id'],
                             'crop': pan['crop'], 'tier': pan['tier'], 'overlap': ov,
                             'definition': pan['definition'], 'use': pan['use'],
                             'step_text': r['text'], 'property': r['property']}
    json.dump(cand, open(os.path.join(OUT, 'link_candidates.json'), 'w'), indent=1)
    json.dump(jobs, open(os.path.join(OUT, 'jobs_link.json'), 'w'), indent=1)
    print(f'{len(jobs)} link-confirmation calls over '
          f'{len({v["doi"] for v in cand.values()})} papers')
    return jobs


def linked():
    C = json.load(open(os.path.join(OUT, 'link_candidates.json')))
    keep, unsupported, tally = {}, [], collections.Counter()
    for jid, c in C.items():
        j = jload(rd(jid), 'verdict') or {}
        v = j.get('verdict') if j.get('verdict') in ('states', 'related', 'absent') else None
        q = (j.get('quote') or '').strip()
        tally[v or 'unruled'] += 1
        rec = {**c, 'verdict': v, 'quote': q, 'property_agreed': (j.get('property') or '').strip()}
        # the brief's rule: keep the link only if the authors state that observation themselves
        if v == 'states' and q:
            keep.setdefault((c['doi'], c['step']), []).append(rec)
        else:
            unsupported.append(rec)
    out = {f'{k[0]}|{k[1]}': v for k, v in keep.items()}
    json.dump({'kept': out, 'unsupported_m2m_claims': unsupported, 'tally': dict(tally)},
              open(os.path.join(OUT, 'links.json'), 'w'), indent=1)
    print(json.dumps(dict(tally), indent=1))
    print(f'{len(out)} observation steps linked; {len(unsupported)} candidate links rejected')
    return out




def figlink():
    """Panel-level linking returned 0 of 12. The rejections all point one way: an M2M
    observation step is written across techniques ("FT-IR, DSC, XRD, DMA, SEM ... collectively
    indicate"), so no single panel's caption states it. This asks the same question at the
    granularity the steps are actually written at -- one whole figure, all its panels' captions
    and use sentences together -- before concluding the chain cannot be grounded at all."""
    S = json.load(open(os.path.join(OUT, 'steps.json')))
    jobs, cand = [], {}
    for p in papers():
        pj = os.path.join(p['folder'], 'panels', 'match.json')
        if not os.path.exists(pj): continue
        figs = json.load(open(pj))['figures']
        for r in (S.get(p['doi']) or []):
            if r['kind'] != 'observation': continue
            words = {w for w in re.findall(r'[a-z0-9]{4,}', r['text'].lower())}
            scored = []
            for f in figs:
                caps = [pan.get('definition') or '' for pan in f.get('panels', [])]
                uses = [u for pan in f.get('panels', []) for u in (pan.get('use') or [])]
                txt = (' '.join(caps) + ' ' + ' '.join(uses)).lower()
                if not txt.strip(): continue
                ov = len(words & {w for w in re.findall(r'[a-z0-9]{4,}', txt)})
                if ov: scored.append((ov, f, caps, uses))
            scored.sort(key=lambda x: -x[0])
            for ov, f, caps, uses in scored[:2]:
                jid = (f"{p['doi'].replace('/', '_')}__f{r['n']}__"
                       f"{re.sub(r'[^A-Za-z0-9]', '', f['file'])[-12:]}")
                fp = os.path.join(CALLS, jid + '.txt')
                open(fp, 'w').write(LINK.format(
                    claim=r['text'],
                    definition=' | '.join(c for c in caps if c) or '(none)',
                    use=' '.join(uses) or '(none)'))
                jobs.append({'id': jid, 'agent': CHECKER['agent'], 'model': CHECKER['model'],
                             'prompt': fp, 'out': os.path.join(CALLS, jid + '.out.txt')})
                cand[jid] = {'doi': p['doi'], 'step': r['n'], 'figure': f['file'],
                             'tier': f['tier'], 'overlap': ov, 'step_text': r['text'],
                             'panels': [{'label': x.get('label'), 'crop': x.get('crop'),
                                         'definition': x.get('definition'),
                                         'use': x.get('use') or []}
                                        for x in f.get('panels', [])],
                             'property': r['property']}
    json.dump(cand, open(os.path.join(OUT, 'figlink_candidates.json'), 'w'), indent=1)
    json.dump(jobs, open(os.path.join(OUT, 'jobs_figlink.json'), 'w'), indent=1)
    print(f'{len(jobs)} figure-level link calls')
    return jobs


def figlinked():
    C = json.load(open(os.path.join(OUT, 'figlink_candidates.json')))
    keep, rej, tally = {}, [], collections.Counter()
    for jid, c in C.items():
        j = jload(rd(jid), 'verdict') or {}
        v = j.get('verdict') if j.get('verdict') in ('states', 'related', 'absent') else None
        q = (j.get('quote') or '').strip()
        tally[v or 'unruled'] += 1
        rec = {**c, 'verdict': v, 'quote': q}
        if v == 'states' and q: keep.setdefault(f"{c['doi']}|{c['step']}", []).append(rec)
        else: rej.append(rec)
    json.dump({'kept': keep, 'rejected': rej, 'tally': dict(tally)},
              open(os.path.join(OUT, 'figlinks.json'), 'w'), indent=1)
    print(json.dumps(dict(tally), indent=1))
    print(f'{len(keep)} observation steps linked at figure level; {len(rej)} rejected')
    return keep


if __name__ == '__main__':
    {'label': label, 'collect': collect, 'link': link, 'linked': linked, 'figlink': figlink, 'figlinked': figlinked}[sys.argv[1]]()
