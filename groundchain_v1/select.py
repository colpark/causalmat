"""select.py: Stage 1, pick 20 papers plus 10 reserves from the M2M csv.

  python3 groundchain_v1/select.py local      the csv-only filter, no network
  python3 groundchain_v1/select.py crossref   year, licence and publisher, from Crossref
  python3 groundchain_v1/select.py pick       the final 20 + 10, with the funnel

No model call at any stage. Every number the report gives for the funnel comes from
results/groundchain_v1/select_*.json, which these write.

The csv's text is silver: an LLM wrote it and almost no step cites a figure. It is used here
only to find candidate papers and to carry the 6-step chain forward. Nothing in it is ever
used as an answer key -- the keys come from the authors' own spans, in Stage 3.
"""
import collections, csv, json, os, re, sys, time, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (CSV, OUT, TECHNIQUES, STRONG, OFFDOMAIN, REVIEWISH,
                    MIN_YEAR, MAX_PER_PUBLISHER, N_PICK, N_RESERVE)

csv.field_size_limit(10 ** 7)
UA = 'groundchain/1.0 (mailto:dpark2129@gmail.com)'
STEP = re.compile(r'\[Begin Step (\d+)\](.*?)\[End Step \1\]', re.S)


def rows():
    return list(csv.DictReader(open(CSV)))


def steps_of(r):
    out = [(int(n), t.strip()) for n, t in STEP.findall(r.get('reasoning_process') or '')]
    return [t for _, t in sorted(out)]


def blob(r):
    return ' '.join(str(r.get(k) or '') for k in
                    ('problem_statement', 'hypothesis', 'problem_core', 'battery_system',
                     'component', 'intervention_or_solution', 'target_property',
                     'keywords', 'keywords_compact', 'reasoning_process')).lower()


def techniques(t):
    """which technique FAMILIES this paper names -- two different families, not two methods"""
    hit = set()
    for fam, words in TECHNIQUES.items():
        for w in words:
            # a short acronym must stand alone, or "cv" matches "convection"
            pat = rf'\b{re.escape(w)}\b' if len(w) <= 4 else re.escape(w)
            if re.search(pat, t):
                hit.add(fam); break
    return sorted(hit)


def local():
    R = rows()
    funnel = collections.OrderedDict()
    funnel['csv_rows'] = len(R)
    out, why = [], collections.Counter()
    for r in R:
        t = blob(r)
        rec = {'sample_id': r['sample_id'], 'doi': r['doi'].strip(),
               'battery_system': r.get('battery_system'),
               'problem_type_broad': r.get('problem_type_broad'),
               'evidence_strength': r.get('evidence_strength'),
               'n_steps': len(steps_of(r)),
               'techniques': techniques(t)}
        if not rec['doi'] or not rec['doi'].startswith('10.'):
            why['no doi'] += 1; continue
        off = [w for w in OFFDOMAIN if w in t]
        on = [w for w in STRONG if w in t]
        rev = [w for w in REVIEWISH if w in t]
        # A storage device has to be named. "electrode" and "electrolyte" are not enough --
        # that is what let six fuel-cell and environmental papers into the first pick list.
        if not on:
            why['no storage device named'] += 1; continue
        if off:
            why['names another device class'] += 1; continue
        if rev:
            why['reads as a review'] += 1; continue
        if len(rec['techniques']) < 2:
            why['fewer than 2 technique families'] += 1; continue
        if rec['n_steps'] < 5:
            why['chain shorter than 5 steps'] += 1; continue
        rec['on_terms'] = on[:6]
        out.append(rec)
    funnel['dropped'] = dict(why)
    funnel['passed_local_filter'] = len(out)
    funnel['by_publisher'] = dict(collections.Counter(x['doi'].split('/')[0] for x in out))
    funnel['technique_families'] = dict(collections.Counter(
        len(x['techniques']) for x in out))
    os.makedirs(OUT, exist_ok=True)
    json.dump({'note': 'Stage 1 local filter, csv only, no network.',
               'funnel': funnel, 'candidates': out},
              open(os.path.join(OUT, 'select_local.json'), 'w'), indent=1)
    print(json.dumps(funnel, indent=1))
    return out


def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=30) as f:
                return json.load(f)
        except Exception as e:
            if i == tries - 1: return {'_error': str(e)[:120]}
            time.sleep(1.5 * (i + 1))
    return None


def crossref():
    cand = json.load(open(os.path.join(OUT, 'select_local.json')))['candidates']
    done = {}
    p = os.path.join(OUT, 'select_crossref.json')
    if os.path.exists(p): done = json.load(open(p)).get('works', {})
    todo = [c for c in cand if c['doi'] not in done]
    print(f'{len(todo)} to query, {len(done)} cached')
    for i, c in enumerate(todo, 1):
        j = get('https://api.crossref.org/works/' + urllib.parse.quote(c['doi']))
        m = (j or {}).get('message') or {}
        dp = (m.get('published') or m.get('issued') or {}).get('date-parts') or [[None]]
        lic = m.get('license') or []
        done[c['doi']] = {
            'ok': '_error' not in (j or {}) and bool(m),
            'error': (j or {}).get('_error'),
            'year': dp[0][0] if dp and dp[0] else None,
            'type': m.get('type'), 'publisher': m.get('publisher'),
            'container': (m.get('container-title') or [None])[0],
            'title': (m.get('title') or [None])[0],
            'licenses': [{'url': L.get('URL'), 'start': ((L.get('start') or {})
                          .get('date-parts') or [[None]])[0][0],
                          'content_version': L.get('content-version')} for L in lic],
            'is_cc': any('creativecommons.org' in (L.get('URL') or '') for L in lic),
        }
        if i % 25 == 0 or i == len(todo):
            json.dump({'works': done}, open(p, 'w'), indent=1)
            print(f'  {i}/{len(todo)}', flush=True)
        time.sleep(0.06)
    json.dump({'works': done}, open(p, 'w'), indent=1)
    ok = sum(1 for v in done.values() if v['ok'])
    print(f'{ok} resolved, {len(done)-ok} failed')
    return done




def epmc():
    """Europe PMC: is there a JATS full text we can pull figures and captions out of?"""
    cand = {c['doi']: c for c in
            json.load(open(os.path.join(OUT, 'select_local.json')))['candidates']}
    W = json.load(open(os.path.join(OUT, 'select_crossref.json')))['works']
    # Probe every candidate, not just those Crossref calls CC. Crossref's licence field is
    # patchy, and Europe PMC records its own licence and OA status, which is the one that
    # actually predicts whether the figures come down.
    elig = [d for d, v in W.items() if v['ok']]
    p = os.path.join(OUT, 'select_epmc.json')
    done = json.load(open(p))['recs'] if os.path.exists(p) else {}
    todo = [d for d in elig if d not in done]
    print(f'{len(elig)} eligible on year+licence; {len(todo)} to probe, {len(done)} cached')
    base = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search'
    for i, doi in enumerate(todo, 1):
        q = urllib.parse.urlencode({'query': f'DOI:"{doi}"', 'format': 'json',
                                    'resultType': 'core', 'pageSize': 1})
        j = get(f'{base}?{q}')
        res = ((j or {}).get('resultList') or {}).get('result') or []
        r = res[0] if res else {}
        done[doi] = {
            'found': bool(res),
            'pmcid': r.get('pmcid'),
            'is_oa': r.get('isOpenAccess') == 'Y',
            'in_epmc': r.get('inEPMC') == 'Y',
            'has_fulltext_xml': r.get('hasFullTextXML') == 'Y' or r.get('inEPMC') == 'Y',
            'licence': r.get('license'),
            'journal': ((r.get('journalInfo') or {}).get('journal') or {}).get('title'),
        }
        if i % 20 == 0 or i == len(todo):
            json.dump({'recs': done}, open(p, 'w'), indent=1); print(f'  {i}/{len(todo)}', flush=True)
        time.sleep(0.08)
    json.dump({'recs': done}, open(p, 'w'), indent=1)
    n = sum(1 for v in done.values() if v['has_fulltext_xml'])
    print(f'{n} of {len(done)} have a Europe PMC full text')
    return done




def pick():
    """the final 20 + reserves, with the funnel the report has to print"""
    import importlib
    import config as _c
    importlib.reload(_c)
    L = {c['doi']: c for c in
         json.load(open(os.path.join(OUT, 'select_local.json')))['candidates']}
    W = json.load(open(os.path.join(OUT, 'select_crossref.json')))['works']
    E = json.load(open(os.path.join(OUT, 'select_epmc.json')))['recs']

    fun = collections.OrderedDict()
    fun['csv_rows'] = len(rows())
    fun['passed_local_filter'] = len(L)
    # count only over the CURRENT candidate set, not every doi ever queried
    fun['crossref_resolved'] = sum(1 for d in L if (W.get(d) or {}).get('ok'))
    fun['in_europe_pmc_full_text'] = sum(1 for d in L if (E.get(d) or {}).get('has_fulltext_xml'))

    elig = []
    for d, c in L.items():
        w, e = W.get(d) or {}, E.get(d) or {}
        if not w.get('ok'): continue
        if not e.get('has_fulltext_xml'): continue
        if (w.get('year') or 0) < _c.MIN_YEAR: continue
        lic = (e.get('licence') or '')
        if not (w.get('is_cc') or lic.startswith('cc')): continue
        elig.append({**c, 'year': w['year'], 'publisher': w['publisher'],
                     'container': w['container'], 'title': w['title'],
                     'pmcid': e.get('pmcid'), 'licence': lic or 'crossref-cc',
                     'n_tech': len(c['techniques'])})
    fun[f'and_year_ge_{_c.MIN_YEAR}_and_cc'] = len(elig)

    # rank: more technique families first (more routes to one claim), then permissive licence,
    # then more recent. Nothing here looks at the paper's content.
    elig.sort(key=lambda x: (-x['n_tech'], x['licence'] != 'cc by', -(x['year'] or 0), x['doi']))
    per, chosen = collections.Counter(), []
    for x in elig:
        if per[x['publisher']] >= _c.MAX_PER_PUBLISHER: continue
        per[x['publisher']] += 1
        chosen.append(x)
    fun[f'after_cap_{_c.MAX_PER_PUBLISHER}_per_publisher'] = len(chosen)
    picks, reserves = chosen[:_c.N_PICK], chosen[_c.N_PICK:_c.N_PICK + _c.N_RESERVE]
    fun['picks'] = len(picks)
    fun['reserves'] = len(reserves)
    fun['publishers'] = dict(collections.Counter(x['publisher'] for x in chosen))
    fun['brief_defaults_would_have_yielded'] = _c.BRIEF_DEFAULTS

    json.dump({'note': 'Stage 1 selection. No model call; every count is reproducible.',
               'funnel': fun, 'picks': picks, 'reserves': reserves},
              open(os.path.join(OUT, 'select_picks.json'), 'w'), indent=1)
    print(json.dumps(fun, indent=1))
    print('\nPILOT (first pick):', picks[0]['doi'], '|', (picks[0]['title'] or '')[:70])
    return picks, reserves


if __name__ == '__main__':
    {'local': local, 'crossref': crossref, 'epmc': epmc, 'pick': pick}[sys.argv[1]]()
