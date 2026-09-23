"""necessity.py: measure a panel's necessity by removing it and re-answering the claim.

  python3 trace_kit_v2/necessity.py prompts   build every configuration x 3 repeats
  python3 trace_kit_v2/necessity.py collect   -> results/v2/necessity/<case>.json

Ground truth becomes an experiment rather than another model's opinion: run net-claim with all panels,
then once per panel with that panel removed, and see whether the answer survives.

net-claim receives the claim text, the paper's setup context and panel images. It never receives an
observation text, a contribution label or the step structure -- guard() enforces that before dispatch.
"""
import json, os, re, sys, glob, statistics, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
WORK = os.path.join(ROOT, '.v07work/nec')
OUT = os.path.join(ROOT, 'results/v2/necessity')
REPEATS = 3
THRESHOLD = 0.15          # fixed in advance, per the brief
VERDICTS = ('supported', 'partly supported', 'cannot tell', 'contradicted')
STRENGTH = {'supported': 3, 'partly supported': 2, 'cannot tell': 1, 'contradicted': 0}
# the answerer must not be told what any panel shows, nor how the chain is built
BANNED = re.compile(r'\b(observation|contribution|establishes|supports_part|supports part|cuts_against|'
                    r'cuts against|not_addressed|image_support|step \d|shown|partial|contradicts|'
                    r'evidences|qualifies|chain)\b', re.I)


def cases():
    for f in sorted(glob.glob(os.path.join(ROOT, 'results/v2/cases/*/*/case.json'))):
        yield json.load(open(f)), os.path.dirname(f)


def context(ch):
    """the paper's setup: the non-evidence nodes upstream of the claim, by label. No observations."""
    g = json.load(open(os.path.join(ROOT, ch['graph'])))
    N = {n['id']: n for n in g['nodes']}
    ev = {s['node'] for s in ch['steps']}
    up = [e['src'] for e in g['edges'] if e['dst'] == ch['claim'] and e['src'] not in ev]
    out = []
    for nid in up:
        n = N.get(nid) or {}
        if (n.get('type') or '').startswith('OBS'): continue
        if n.get('label'): out.append(n['label'])
    return out[:4]


def channels(ch):
    """panels grouped by the step's technique family. Removing a channel pulls all its panels at once."""
    out = collections.OrderedDict()
    for s in ch['steps']:
        for p in s['panels']:
            if p.get('png'): out.setdefault(s['family'], []).append(p)
    for k in out:   # dedupe by suffix, keep order
        seen = set(); out[k] = [p for p in out[k] if not (p['suffix'] in seen or seen.add(p['suffix']))]
    return out


def panels(ch):
    seen, out = set(), []
    for s in ch['steps']:
        for p in s['panels']:
            if p.get('png') and p['suffix'] not in seen:
                seen.add(p['suffix']); out.append(p)
    return out


def text(ch, ctx, keep, cdir):
    L = [f"Claim: {ch['claim_text']}", ""]
    if ctx:
        L.append("Setup from the paper:")
        L += [f"- {c}" for c in ctx]
        L.append("")
    if keep:
        L.append(f"You are given {len(keep)} figure panel{'s' if len(keep) != 1 else ''} from this paper.")
        L.append("")
        L.append("Images (read each with Read):")
        L += [os.path.join(cdir, p['png']) for p in keep]
    else:
        L.append("You are given no figure panels: judge the claim from the setup alone.")
    return "\n".join(L)


def prompts():
    os.makedirs(WORK, exist_ok=True)
    jobs, leaks, plan = [], [], []
    for ch, cdir in cases():
        ctx = context(ch); ps = panels(ch)
        ch_map = channels(ch)
        configs = [('full', ps)] + [(f"drop_{p['suffix']}", [q for q in ps if q is not p]) for p in ps]
        for fam, fps in ch_map.items():
            keep = [q for q in ps if q['suffix'] not in {x['suffix'] for x in fps}]
            configs.append((f"dropchan_{fam}", keep))
        configs.append(('floor_nopanels', []))
        for name, keep in configs:
            t = text(ch, ctx, keep, cdir)
            bad = sorted({m.group(0).lower() for m in BANNED.finditer(t)})
            if bad: leaks.append((ch['case'], name, bad)); continue
            for r in range(1, REPEATS + 1):
                pth = os.path.join(WORK, f"{ch['case']}.{name}.r{r}.txt"); open(pth, 'w').write(t)
                jobs.append({'id': f"{ch['case']}/{name}/r{r}", 'agent': 'net-claim', 'prompt': pth,
                             'out': os.path.join(WORK, f"{ch['case']}.{name}.r{r}.out.txt")})
        plan.append((ch['case'], len(ps), len(configs)))
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_nec.json'), 'w'), indent=1)
    json.dump({'papers': ['nec'], 'stage': 'necessity'}, open(os.path.join(ROOT, '.v07work/batch_nec.meta.json'), 'w'), indent=1)
    for c, np_, nc in plan: print(f"  {c:22s} {np_:2d} panels -> {nc:2d} configs x {REPEATS} = {nc*REPEATS:3d} calls")
    print(f"{len(jobs)} calls total, threshold drop > {THRESHOLD} fixed in advance")
    if leaks:
        print("LEAK, refusing to dispatch:", leaks[:6]); sys.exit(2)
    print("guard: no prompt names an observation, a contribution label, a support level or a step")


PROSE_V = re.compile(r'\bverdict\b\W{0,4}(supported|partly supported|partially supported|cannot tell|contradicted)', re.I)
PROSE_C = re.compile(r'confidence\W{0,4}([01](?:\.\d+)?)', re.I)
PROSE_U = re.compile(r'unsettled\b\W{0,4}(.+?)(?:\n\n|\Z)', re.I | re.S)


def parse(t):
    """JSON first; then the prose form the answerer sometimes returns ("Verdict: partly supported,
    confidence 0.5"). Dropping those silently would make every drop None and every panel score
    not-necessary by default, which reads as all_redundant and is not a finding."""
    t = t or ''
    m = re.search(r'\{.*\}', t, re.S)
    if m:
        try: return json.loads(m.group(0))
        except Exception: pass
    v = PROSE_V.search(t)
    if not v: return None
    c = PROSE_C.search(t)
    u = PROSE_U.search(t)
    return {'verdict': v.group(1).lower().replace('partially', 'partly'),
            'confidence': float(c.group(1)) if c else None,
            'unsettled': [x.strip(' -*') for x in (u.group(1).split('\n') if u else []) if x.strip(' -*')][:6],
            '_from_prose': True}


def majority(rs):
    """majority verdict and median confidence over the repeats, plus whether they agreed"""
    vs = [r['verdict'] for r in rs if r]
    if not vs: return None, None, None
    top, n = collections.Counter(vs).most_common(1)[0]
    conf = [r['confidence'] for r in rs if r and r['verdict'] == top and isinstance(r.get('confidence'), (int, float))]
    return top, (round(statistics.median(conf), 3) if conf else None), n == len(vs)


def collect():
    os.makedirs(OUT, exist_ok=True)
    allrows, unstable, tot_cfg = [], 0, 0
    for ch, cdir in cases():
        ps = panels(ch); ch_map = channels(ch)
        res = {}
        names = ['full'] + [f"drop_{p['suffix']}" for p in ps] \
                + [f"dropchan_{f}" for f in ch_map] + ['floor_nopanels']
        for name in names:
            rs = []
            for r in range(1, REPEATS + 1):
                f = os.path.join(WORK, f"{ch['case']}.{name}.r{r}.out.txt")
                j = parse(open(f).read()) if os.path.exists(f) else None
                if j:
                    v = (j.get('verdict') or '').strip().lower()
                    rs.append({'verdict': v if v in VERDICTS else 'unparsed',
                               'confidence': j.get('confidence'), 'unsettled': j.get('unsettled') or []})
            v, c, agreed = majority(rs)
            confs = [r['confidence'] for r in rs if isinstance(r.get('confidence'), (int, float))]
            res[name] = {'verdict': v, 'confidence': c, 'repeats': len(rs), 'repeats_agreed': agreed,
                         'conf_spread': round(max(confs) - min(confs), 3) if len(confs) > 1 else 0.0,
                         'unsettled': (rs[0]['unsettled'] if rs else [])}
            tot_cfg += 1
            if agreed is False: unstable += 1
        full = res['full']
        rows = []
        for p in ps:
            d = res[f"drop_{p['suffix']}"]
            drop = (full['confidence'] - d['confidence']) if (full['confidence'] is not None and d['confidence'] is not None) else None
            flip = d['verdict'] != full['verdict']
            # the brief's wording assumes the full run reads "supported". Three of five cases start at
            # "partly supported", where the only weaker verdict is "cannot tell" -- so a rule keyed on
            # "from supported" can never fire for them and reports all_redundant by construction.
            # Necessity is removal STRICTLY WEAKENING the verdict, wherever it started.
            weaker = STRENGTH.get(d['verdict'], 1) < STRENGTH.get(full['verdict'], 1)
            nec = bool(weaker or (drop is not None and drop > THRESHOLD))
            new_uns = [u for u in d['unsettled'] if u not in full['unsettled']]
            rows.append({'panel': p['suffix'], 'panel_id': p['panel_id'], 'flip': flip,
                         'verdict_without': d['verdict'], 'confidence_without': d['confidence'],
                         'drop': round(drop, 3) if drop is not None else None,
                         'unsettled_delta': new_uns[:4], 'necessary': nec})
        def rank_in_place(rs):
            rk = sorted([r for r in rs if r['drop'] is not None], key=lambda x: -x['drop'])
            i = 0
            while i < len(rk):
                j = i
                while j + 1 < len(rk) and rk[j + 1]['drop'] == rk[i]['drop']: j += 1
                for k in range(i, j + 1): rk[k]['rank'] = i + 1; rk[k]['tied'] = j > i
                i = j + 1
        rank_in_place(rows)

        chrows = []
        for fam, fps in ch_map.items():
            d = res[f"dropchan_{fam}"]
            drop = (full['confidence'] - d['confidence']) if (full['confidence'] is not None and d['confidence'] is not None) else None
            weaker = STRENGTH.get(d['verdict'], 1) < STRENGTH.get(full['verdict'], 1)
            chrows.append({'channel': fam, 'n_panels': len(fps),
                           'panels': [p['suffix'] for p in fps],
                           'verdict_without': d['verdict'], 'confidence_without': d['confidence'],
                           'drop': round(drop, 3) if drop is not None else None,
                           'flip': d['verdict'] != full['verdict'],
                           'necessary': bool(weaker or (drop is not None and drop > THRESHOLD)),
                           'same_as_panel_level': len(fps) == 1})
        rank_in_place(chrows)
        cnn = sum(1 for r in chrows if r['necessary'])
        csplit = 'all_necessary' if cnn == len(chrows) else ('all_redundant' if cnn == 0 else 'mixed')
        # an ordering inside the repeat-to-repeat spread is not an ordering
        spread = max([res[n]['conf_spread'] for n in names] or [0.0])
        drops = [abs(r['drop']) for r in rows if r['drop'] is not None]
        ordering_real = bool(drops) and max(drops) > spread
        nn = sum(1 for r in rows if r['necessary'])
        split = 'all_necessary' if nn == len(rows) else ('all_redundant' if nn == 0 else 'mixed')
        obj = {'case': ch['case'], 'paper': ch['paper'], 'claim': ch['claim'],
               'channels': chrows, 'n_channels': len(chrows), 'n_necessary_channels': cnn,
               'channel_split': csplit, 'one_panel_per_channel': all(r['same_as_panel_level'] for r in chrows),
               'repeat_conf_spread': spread, 'ordering_outside_noise': ordering_real,
               'claim_text': ch['claim_text'], 'answerer': 'net-claim (sonnet), tools: Read',
               'threshold': THRESHOLD, 'repeats': REPEATS,
               'full_verdict': full['verdict'], 'full_confidence': full['confidence'],
               'confidence_floor': res['floor_nopanels'],
               'n_panels': len(ps), 'panels': rows, 'split': split, 'n_necessary': nn,
               'note': 'Every verdict is model against model. Necessity is relative to this answerer and prompt.'}
        json.dump(obj, open(os.path.join(OUT, ch['case'] + '.json'), 'w'), indent=1)
        allrows.append(obj)
        print(f"  {ch['case']:22s} full={full['verdict']}({full['confidence']}) "
              f"floor={res['floor_nopanels']['verdict']}({res['floor_nopanels']['confidence']}) "
              f"panel {nn}/{len(rows)} {split}  |  channel {cnn}/{len(chrows)} {csplit}"
              + ("  [1 panel per channel: same measurement twice]" if obj['one_panel_per_channel'] else "")
              + ("" if ordering_real else "  [all drops inside the repeat spread: no ordering]"))
    print(f"\nrepeat instability: {unstable}/{tot_cfg} configurations disagreed across the 3 repeats "
          f"({unstable/tot_cfg:.0%}); the stop rule is one third")
    mixed = sum(1 for o in allrows if o['split'] == 'mixed')
    print(f"mixed splits (the only case where the measurement discriminates): {mixed}/5")
    floor_sup = [o['case'] for o in allrows if o['confidence_floor']['verdict'] == 'supported']
    print(f"confidence floor says supported with no panels on {len(floor_sup)}/5: {floor_sup}")


if __name__ == '__main__': {'prompts': prompts, 'collect': collect}[sys.argv[1]]()
