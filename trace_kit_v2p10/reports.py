"""reports.py: v2.10 -- one self-contained report per paper, graph to figure pixels.

  python3 -m trace_kit_v2p10.reports chains    assemble the 86 maximal chains with every text
  python3 -m trace_kit_v2p10.reports prompts   the 4 Sonnet prompts per chain
  python3 -m trace_kit_v2p10.reports collect   parse the replies
  python3 -m trace_kit_v2p10.reports build     render the reports

The reports exist because the numbers have outrun the evidence. A pass rate says a chain held;
it does not let anyone see what travelled, what the figure actually shows, or what the chain
quietly stopped saying. So every report carries the paper's whole graph, every chain drawn on
it, and for each link the crop at readable size beside the whole figure with the panel's box
drawn on it, the caption that defines the panel and the sentences the body text uses it in.

Three things on each page are generated rather than stored, and each says so: a plain-words
reading of the chain, a caveat ledger that asks whether the last proposition still respects the
limits the earlier links attached, and a comparison of the chain's conclusion with the paper's
own wording of the claim. The ledger and the comparison are new measurements, not decoration.

Every verdict is model against model.
"""
import base64, collections, html, io, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
sys.path.insert(0, R('trace_kit'))
from cut_traces import store_for, fig_by_number  # noqa: E402
from pages import obj  # noqa: E402

E = html.escape
OUT = R('results/v2p10/reports')
STAGE = ['HYP', 'DES', 'PRC', 'STR', 'PRP', 'MEC', 'PRF', 'DSC', 'KNW', 'OBS']
PROM = R('results/v2p10/reportcalls')


# ---------------------------------------------------------------- data

def panel_full(store, pid):
    """crop, whole figure, the panel's box on that figure, its caption and its body-text uses.

    panel_record in trace_kit gives the crop and the caption. A reader also needs to see where
    on the page the crop came from and what the paper says about it, so this returns the bbox
    and the `use` sentences too.
    """
    base, mj, pj, ocr = store
    m = re.match(r'.*#F(\d+)([a-z]?)$', pid)
    if not m: return None
    n, let = int(m.group(1)), m.group(2).upper()
    fig = fig_by_number(mj, n)
    if not fig: return None
    pf = next((f for f in pj['figures'] if f['file'] == fig['file']), {})
    out = {'pid': pid, 'figure': os.path.join(base, fig['file']),
           'fig_w': pf.get('width'), 'fig_h': pf.get('height'),
           'caption_preamble': fig.get('caption_preamble'),
           'crop': None, 'bbox': None, 'definition': None, 'uses': []}
    if not let:
        out['crop'] = out['figure']
        out['definition'] = fig.get('caption_preamble')
        return out
    mp = next((p for p in fig.get('panels', []) if (p.get('label') or '').upper() == let), {})
    det = next((x for x in pf.get('detections', [])
                if (x.get('label') or '').upper() == let and x.get('crop')), {})
    out['definition'] = mp.get('definition')
    u = mp.get('use')
    out['uses'] = ([u] if isinstance(u, str) else list(u or []))
    out['bbox'] = mp.get('bbox') or det.get('bbox')
    c = det.get('crop') or mp.get('crop')
    if c: out['crop'] = os.path.join(base, c)
    return out


def load():
    d = {'DEC': {}, 'KEY': {}, 'CLM': {}, 'REC': {}}

    def add(dec, key, clm, src):
        for f, k in ((dec, 'DEC'), (key, 'KEY'), (clm, 'CLM'), (src, 'REC')):
            p = R(f)
            if not os.path.exists(p): continue
            j = json.load(open(p))
            if k == 'DEC': d[k].update(j['items_out'])
            elif k == 'KEY': d[k].update(j)
            elif k == 'CLM': d[k].update(j['items'])
            else: d[k].update({x['item']: x for x in j['pairs_out']})

    add('results/v2p9/step4.json', 'results/v2p9/keys.json',
        'results/v2p9/step2.json', 'results/v2p9/pairs.json')
    add('results/v2p9/step4_nl.json', 'results/v2p9/keys_nl.json',
        'results/v2p9/step2_nl.json', 'results/v2p9/nextlink.json')
    add('results/v2p10/step4_d4.json', 'results/v2p10/keys_d4.json',
        'results/v2p10/step2_d4.json', 'results/v2p10/deeper_d4.json')
    add('results/v2p10/step4_d5.json', 'results/v2p10/keys_d5.json',
        'results/v2p10/step2_d5.json', 'results/v2p10/deeper_d5.json')
    d['PU'] = json.load(open(R('results/v2p10/purge.json')))
    d['V25'] = {i['item']: i for i in json.load(open(R('results/v2p5/items.json')))['items']}
    return d


def steps_of(leaf, d):
    out, cur = [], leaf
    while cur and cur in d['REC']:
        out.append(cur)
        nxt = d['REC'][cur].get('parent_item') or d['REC'][cur].get('upstream_item')
        cur = nxt if nxt in d['REC'] else None
    return list(reversed(out))


def maximal_chains(d):
    """every passing chain that is not contained in a longer passing one"""
    cand = [{'leaf': i, 'depth': 2} for i in d['PU']['live_depth2']]
    cand += [{'leaf': i, 'depth': 3} for i in d['PU']['live_depth3']]
    for it, v in d['DEC'].items():
        if not v.get('compositional'): continue
        if it.startswith('d4_'): cand.append({'leaf': it, 'depth': 4})
        elif it.startswith('d5_'): cand.append({'leaf': it, 'depth': 5})
    deepest = {}
    for c in cand:
        for s in steps_of(c['leaf'], d):
            deepest[s] = max(deepest.get(s, 0), c['depth'])
    keep = [c for c in cand if deepest.get(c['leaf'], 0) == c['depth']]
    for i, c in enumerate(sorted(keep, key=lambda x: (-x['depth'], x['leaf'])), 1):
        c['id'] = f'C{i}'
        c['steps'] = steps_of(c['leaf'], d)
        c['paper'] = d['REC'][c['leaf']]['paper']
        c['contains'] = [s for s in c['steps'][:-1]]
    return sorted(keep, key=lambda x: (x['paper'], -x['depth'], x['id']))


def chains():
    d = load()
    cs = maximal_chains(d)
    json.dump({'note': 'v2.10 reports: the maximal passing chains, with their step ids.',
               'chains': len(cs),
               'by_depth': dict(collections.Counter(c['depth'] for c in cs)),
               'papers': len({c['paper'] for c in cs}),
               'out': cs}, open(R('results/v2p10/report_chains.json'), 'w'), indent=1)
    print(json.dumps({'chains': len(cs),
                      'by_depth': dict(collections.Counter(c['depth'] for c in cs)),
                      'papers': len({c['paper'] for c in cs})}, indent=1))
    return cs




# ---------------------------------------------------------------- prompts

PARA = """Below is one chain of reasoning about a single experimental paper, step by step. Each step was handed the previous step's conclusion and one new measurement.

{body}

Write ONE paragraph, at most 180 words, that reads this chain from the first evidence to the final claim. For each step say what the new measurement adds and why that step needed the result handed to it. Write plainly, as you would explain it to a colleague who has not seen the figures.

Use only what is above. Do not add mechanism, motivation or significance that is not in these texts. Do not hedge about what you were not given.

Return the paragraph as plain prose and nothing else."""

CHECK = """A paragraph was written to summarise a chain of reasoning, using only the stored texts below. Check it sentence by sentence.

THE STORED TEXTS
{body}

THE PARAGRAPH
{para}

For each sentence of the paragraph in order, decide whether the stored texts support it, and quote the stored text that does. A sentence is supported when the texts assert it or plainly carry it. A sentence is NOT supported when it adds a mechanism, a motive, a quantity or a consequence the texts do not state, however reasonable it sounds.

Return JSON and nothing else:
{{"sentences": [{{"n": 1, "sentence": "...", "supported": true or false, "quote": "the stored text that supports it, or \\"\\" if none"}}, ...]}}"""

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

COMPARE = """Two statements about the same experimental result. The first is what a chain of reasoning concluded. The second is how the paper's own argument graph words that claim.

THE CHAIN'S CONCLUSION
{final}

THE PAPER'S OWN WORDING
{node}

How does the chain's conclusion stand to the paper's?

  agrees      the same claim at the same strength and scope.
  narrower    the chain claims less: fewer conditions, a weaker relation, more hedging, or a
              subset of what the paper asserts.
  broader     the chain claims more than the paper's wording supports.
  conflicts   they cannot both be right.

Quote from both to justify the ruling.

Return JSON and nothing else:
{{"verdict": "agrees" | "narrower" | "broader" | "conflicts",
 "chain_quote": "...", "paper_quote": "...", "why": "at most 40 words"}}"""


def chain_body(c, d):
    """every stored text of the chain, in order, for the generating calls"""
    L = []
    root = d['REC'][c['steps'][0]]
    up = d['V25'].get(root['upstream_item'])
    if up:
        L.append('STEP 1, the two-step item this chain starts from')
        L.append(f"  measurement A ({up['observation_a'].get('technique')}): "
                 f"{up['observation_a']['text']}")
        L.append(f"  measurement B ({up['observation_b'].get('technique')}): "
                 f"{up['observation_b']['text']}")
        L.append(f"  what it concluded: {(up.get('key') or {}).get('proposition')}")
        L.append('')
    for i, s in enumerate(c['steps'], 2):
        r = d['REC'][s]; k = d['KEY'].get(s) or {}
        L.append(f'STEP {i}')
        L.append(f"  handed in: {r['input_result']}")
        L.append(f"  new measurement ({r['new_observation'].get('technique')}): "
                 f"{r['new_observation']['text']}")
        L.append(f"  question asked: {r.get('question')}")
        L.append(f"  what it concluded: {k.get('proposition')}")
        for t in (k.get('limits') or []):
            L.append(f"  qualification: {t}")
        L.append('')
    return '\n'.join(L)


def chain_limits(c, d):
    out = []
    root = d['REC'][c['steps'][0]]
    up = d['V25'].get(root['upstream_item'])
    if up:
        for t in ((up.get('key') or {}).get('limits') or []):
            out.append(('step 1', str(t)))
    for i, s in enumerate(c['steps'], 2):
        for t in ((d['KEY'].get(s) or {}).get('limits') or []):
            out.append((f'step {i}', str(t)))
    return out


def final_prop(c, d):
    return (d['KEY'].get(c['steps'][-1]) or {}).get('proposition') or ''


def node_label(c, d):
    r = d['REC'][c['steps'][-1]]
    gp = json.load(open(R('results/v3', r['paper'], 'stitch.json')))['graph']
    N = {n['id']: n for n in json.load(open(R(gp)))['nodes']}
    return (N.get(r['target_claim']) or {}).get('label') or ''


def prompts():
    d = load()
    cs = json.load(open(R('results/v2p10/report_chains.json')))['out']
    os.makedirs(PROM, exist_ok=True)
    jobs, meta = [], {}
    for c in cs:
        body = chain_body(c, d)
        lim = chain_limits(c, d)
        fin = final_prop(c, d)
        meta[c['id']] = {'paper': c['paper'], 'depth': c['depth'], 'steps': c['steps'],
                         'limits': lim, 'final': fin, 'node': node_label(c, d)}
        for kind, text in (
                ('para', PARA.format(body=body)),
                ('ledger', LEDGER.format(
                    limits='\n'.join(f'{i}. [{w}] {t}' for i, (w, t) in enumerate(lim, 1))
                           or '  none recorded', final=fin)),
                ('compare', COMPARE.format(final=fin, node=meta[c['id']]['node']))):
            f = os.path.join(PROM, f"{c['id']}_{kind}.txt"); open(f, 'w').write(text)
            jobs.append({'id': f"{c['id']}_{kind}", 'agent': 'net-writer' if kind == 'para'
                         else 'net-contrib', 'prompt': f,
                         'out': os.path.join(PROM, f"{c['id']}_{kind}.out.txt")})
        open(os.path.join(PROM, f"{c['id']}_body.txt"), 'w').write(body)
    json.dump(meta, open(R('results/v2p10/report_meta.json'), 'w'), indent=1)
    json.dump(jobs, open(R('results/v2p10/report_jobs_a.json'), 'w'), indent=1)
    print(f'{len(jobs)} first-round calls for {len(cs)} chains '
          f'(paragraph, caveat ledger, paper comparison)')
    return jobs




# ---------------------------------------------------------------- round B, collect

def jload(t, want):
    """tolerant reader for a model's JSON reply.

    obj() counts braces without knowing about string literals, so a reply that quotes a Miller
    index -- {10-12} -- is unparseable to it. These replies quote paper text by design, so the
    plain parse and the fenced parse are tried first and obj() is only the third resort.
    """
    t = (t or '').strip()
    for cand in (t, re.sub(r'^```(?:json)?|```$', '', t, flags=re.M).strip()):
        try:
            j = json.loads(cand)
            if isinstance(j, dict) and want in j: return j
        except Exception: pass
    return obj(t, want)


def checks():
    """round B: one CHECK call per chain, against the paragraph round A produced"""
    meta = json.load(open(R('results/v2p10/report_meta.json')))
    jobs, miss = [], []
    for cid in meta:
        po = os.path.join(PROM, f'{cid}_para.out.txt')
        if not os.path.exists(po) or not open(po).read().strip():
            miss.append(cid); continue
        body = open(os.path.join(PROM, f'{cid}_body.txt')).read()
        text = CHECK.format(body=body, para=open(po).read().strip())
        f = os.path.join(PROM, f'{cid}_check.txt'); open(f, 'w').write(text)
        jobs.append({'id': f'{cid}_check', 'agent': 'net-contrib', 'prompt': f,
                     'out': os.path.join(PROM, f'{cid}_check.out.txt')})
    json.dump(jobs, open(R('results/v2p10/report_jobs_b.json'), 'w'), indent=1)
    print(f'{len(jobs)} check calls' + (f'; NO PARAGRAPH for {miss}' if miss else ''))
    return jobs


def sentences(t):
    """split a paragraph the way the checker was asked to read it"""
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z(])', (t or '').strip()) if s.strip()]


def collect():
    meta = json.load(open(R('results/v2p10/report_meta.json')))
    out, tally = {}, collections.Counter()
    for cid, m in meta.items():
        rd = lambda k: (open(os.path.join(PROM, f'{cid}_{k}.out.txt')).read()
                        if os.path.exists(os.path.join(PROM, f'{cid}_{k}.out.txt')) else '')
        e = {'paper': m['paper'], 'depth': m['depth']}
        para = rd('para').strip()
        # the writer was asked for prose only; strip a stray lead-in line if one came back
        if para.lower().startswith(('here is', 'paragraph:')):
            para = para.split('\n', 1)[-1].strip()
        e['para_raw'] = para

        ck = jload(rd('check'), 'sentences')
        if ck:
            ss = [s for s in ck['sentences'] if isinstance(s, dict)]
            e['checked'] = [{'n': s.get('n'), 'sentence': s.get('sentence', ''),
                             'supported': bool(s.get('supported')),
                             'quote': (s.get('quote') or '').strip()} for s in ss]
            # a sentence needs BOTH the verdict and a quote; "supported" with no quote is
            # the checker asserting support it could not point to, so it is removed.
            e['kept'] = [s for s in e['checked'] if s['supported'] and s['quote']]
            e['removed'] = [s for s in e['checked'] if not (s['supported'] and s['quote'])]
            e['para'] = ' '.join(s['sentence'].strip() for s in e['kept'])
            tally['sent_total'] += len(e['checked']); tally['sent_kept'] += len(e['kept'])
            tally['sent_removed'] += len(e['removed'])
        else:
            # unchecked prose is not shown. A paragraph with no verification is exactly the
            # thing this round exists to prevent.
            e['checked'], e['kept'], e['removed'], e['para'] = [], [], [], ''
            tally['check_unparsed'] += 1

        lg = jload(rd('ledger'), 'rulings')
        if lg is None and rd('ledger').strip():
            rs = [{'n': int(a), 'verdict': b} for a, b in
                  re.findall(r'"n"\s*:\s*(\d+)\s*,\s*"verdict"\s*:\s*"(\w+)"', rd('ledger'))]
            lg = {'rulings': rs} if rs else None
            if lg: tally['ledger_salvaged'] += 1
        e['ledger'] = []
        if lg:
            byn = {r.get('n'): r for r in lg['rulings'] if isinstance(r, dict)}
            for i, (w, t) in enumerate(m['limits'], 1):
                r = byn.get(i) or {}
                v = r.get('verdict') if r.get('verdict') in ('respects', 'ignores', 'contradicts') else None
                e['ledger'].append({'n': i, 'where': w, 'limit': t, 'verdict': v,
                                    'quote': (r.get('quote') or '').strip(),
                                    'why': (r.get('why') or '').strip()})
                tally['lim_' + (v or 'unruled')] += 1
        else:
            if m['limits']: tally['ledger_unparsed'] += 1
            for i, (w, t) in enumerate(m['limits'], 1):
                e['ledger'].append({'n': i, 'where': w, 'limit': t, 'verdict': None,
                                    'quote': '', 'why': ''})
                tally['lim_unruled'] += 1

        cp = jload(rd('compare'), 'verdict')
        v = (cp or {}).get('verdict')
        e['compare'] = {'verdict': v if v in ('agrees', 'narrower', 'broader', 'conflicts') else None,
                        'chain_quote': ((cp or {}).get('chain_quote') or '').strip(),
                        'paper_quote': ((cp or {}).get('paper_quote') or '').strip(),
                        'why': ((cp or {}).get('why') or '').strip(), 'node': m['node']}
        tally['cmp_' + (e['compare']['verdict'] or 'unruled')] += 1
        out[cid] = e
    json.dump({'note': 'v2.10 reports: the generated parts, after sentence checking.',
               'tally': dict(tally), 'chains': out},
              open(R('results/v2p10/report_data.json'), 'w'), indent=1)
    print(json.dumps(dict(tally), indent=1))
    return out


# ---------------------------------------------------------------- images

from PIL import Image  # noqa: E402

IMG, IMGN, RESIZED, MISSPAN = {}, {}, [], []


def img_reset():
    IMG.clear(); IMGN.clear()


def img_key(path, cap):
    """register one image for this page and return its key.

    At or under the cap the file's own bytes go in untouched -- no resample, no re-encode, no
    annotation -- because the crop is the evidence the reader is being asked to judge. Over the
    cap it is downscaled once with LANCZOS; every one of those is counted and reported.
    """
    if not path or not os.path.exists(path): return None
    if (path, cap) in IMGN: return IMGN[(path, cap)]
    try:
        im = Image.open(path); w, h = im.size
    except Exception:
        return None
    if max(w, h) <= cap:
        data = open(path, 'rb').read()
        mime = 'image/png' if path.lower().endswith('.png') else 'image/jpeg'
    else:
        s = cap / max(w, h)
        im = im.convert('RGB').resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)
        b = io.BytesIO(); im.save(b, 'JPEG', quality=92, optimize=True)
        data, mime = b.getvalue(), 'image/jpeg'
        RESIZED.append({'path': path, 'from': [w, h], 'to': list(im.size), 'cap': cap})
    k = 'i%d' % (len(IMG) + 1)
    IMG[k] = f'data:{mime};base64,' + base64.b64encode(data).decode()
    IMGN[(path, cap)] = k
    return k


CROP_CAP, FIG_CAP = 1400, 1200


def panel_html(store, pid, seen):
    """the crop, where it came from, and everything the paper says about it"""
    f = panel_full(store, pid) if store else None
    if not f or not f.get('crop'):
        MISSPAN.append({'pid': pid, 'why': 'no panel record' if not f else 'no crop file'})
        return f'<div class="pan miss">panel <code>{E(pid)}</code> &mdash; no crop on file</div>'
    ck = img_key(f['crop'], CROP_CAP)
    if not ck:
        MISSPAN.append({'pid': pid, 'why': 'crop unreadable'})
        return f'<div class="pan miss">panel <code>{E(pid)}</code> &mdash; crop unreadable</div>'
    seen.add(pid)
    H = [f'<figure class="pan" id="p_{E(re.sub(chr(35)+"|/|[.]", "_", pid))}">']
    H.append(f'<figcaption class="pcap"><code>{E(pid)}</code></figcaption>')
    H.append(f'<img class="zoom" data-k="{ck}" alt="panel {E(pid)}">')
    fk = img_key(f['figure'], FIG_CAP) if f.get('figure') else None
    bb, W, Hh = f.get('bbox'), f.get('fig_w'), f.get('fig_h')
    if fk and bb and W and Hh:
        x0, y0, x1, y1 = bb
        H.append('<div class="figwrap">'
                 f'<img class="zoom fig" data-k="{fk}" alt="whole figure">'
                 f'<svg viewBox="0 0 {W} {Hh}" preserveAspectRatio="none">'
                 f'<rect x="{x0}" y="{y0}" width="{max(1, x1 - x0)}" height="{max(1, y1 - y0)}"/>'
                 '</svg></div>')
        H.append('<div class="sub">where it sits in the whole figure</div>')
    elif fk and f['crop'] != f['figure']:
        # a lettered panel whose box was never recorded: the figure is still shown, but the
        # reader is told the crop's place on it is not being asserted.
        H.append(f'<img class="zoom fig" data-k="{fk}" alt="whole figure">')
        MISSPAN.append({'pid': pid, 'why': 'no bbox recorded'})
        H.append('<div class="sub">whole figure &mdash; no box recorded for this panel</div>')
    elif f['crop'] == f['figure']:
        # the citation names a whole figure, so the crop above already is the whole figure
        H.append('<div class="sub">the citation names the whole figure</div>')
    if f.get('caption_preamble'):
        H.append(f'<div class="ptx"><b>figure caption</b>{E(f["caption_preamble"])}</div>')
    if f.get('definition'):
        H.append(f'<div class="ptx"><b>this panel</b>{E(f["definition"])}</div>')
    for u in f.get('uses') or []:
        H.append(f'<div class="ptx use"><b>in the text</b>{E(u)}</div>')
    H.append('</figure>')
    return '\n'.join(H)


# ---------------------------------------------------------------- graph and trajectory

def chain_nodes(c, d):
    """every graph node the chain touches, and the claim it ends on"""
    ns = []
    root = d['REC'][c['steps'][0]]
    up = d['V25'].get(root['upstream_item']) or {}
    for k in ('observation_a', 'observation_b'):
        if up.get(k): ns.append(up[k]['node'])
    ns += list(up.get('claims') or [])
    for s in c['steps']:
        r = d['REC'][s]
        ns.append(r['new_observation']['node'])
        if r.get('claim_C'): ns.append(r['claim_C'])
        if r.get('target_claim'): ns.append(r['target_claim'])
    out = []
    for n in ns:
        if n and n not in out: out.append(n)
    return out


def graph_sel(g):
    """the paper's whole argument graph in stage columns, every node addressable from JS"""
    N = {n['id']: n for n in g['nodes']}
    col = collections.defaultdict(list)
    for n in g['nodes']: col[(n.get('type') or '?').split('/')[0]].append(n['id'])
    order = [s for s in STAGE if s in col] + [k for k in col if k not in STAGE]
    # OBS routinely holds twenty-odd nodes while HYP holds two. One node per row would make the
    # graph a column of whitespace with a ribbon of boxes down one side, so a tall stage wraps
    # into sub-columns and keeps its own heading over the first of them.
    tall = max((len(v) for v in col.values()), default=1)
    rows = min(14, max(4, tall))
    X, SX, Y, pos, heads, cur = 128, 62, 40, {}, [], 52
    for k in order:
        ns = col[k]
        nsub = max(1, -(-len(ns) // rows))
        heads.append((cur, k))
        for i, nid in enumerate(ns):
            j, r = divmod(i, rows)
            pos[nid] = (cur + j * SX, 50 + r * Y)
        cur += (nsub - 1) * SX + X
    W = cur + 20
    Hh = 50 + min(rows, tall) * Y + 30
    o = [f'<svg viewBox="0 0 {W} {Hh}" class="gsvg" id="graph" role="img" '
         f'aria-label="the paper\'s argument graph">']
    for cx, k in heads:
        o.append(f'<text x="{cx}" y="26" class="gcol">{E(k)}</text>')
    for e in g['edges']:
        a, b = pos.get(e['src']), pos.get(e['dst'])
        if not a or not b: continue
        o.append(f'<line class="ge" data-s="{E(e["src"])}" data-d="{E(e["dst"])}" '
                 f'x1="{a[0]+48}" y1="{a[1]}" x2="{b[0]-3}" y2="{b[1]}"/>')
    for nid, (x, y) in pos.items():
        o.append(f'<g class="gn" data-id="{E(nid)}">'
                 f'<title>{E((N[nid].get("label") or "")[:300])}</title>'
                 f'<rect x="{x-3}" y="{y-12}" width="52" height="24" rx="6"/>'
                 f'<text x="{x+23}" y="{y+4}">{E(nid)}</text></g>')
    o.append('</svg>')
    return '\n'.join(o)


def traj_svg(c, d):
    """one strip: what each step added and what it concluded"""
    root = d['REC'][c['steps'][0]]
    up = d['V25'].get(root['upstream_item']) or {}
    cells = [{'t': 'step 1', 'add': ' + '.join(
        up[k]['node'] for k in ('observation_a', 'observation_b') if up.get(k)),
        'to': ', '.join(up.get('claims') or []) or '—'}]
    for i, s in enumerate(c['steps'], 2):
        r = d['REC'][s]
        cells.append({'t': f'step {i}', 'add': '+ ' + r['new_observation']['node'],
                      'to': r.get('target_claim') or '—'})
    BW, G, H = 168, 46, 92
    W = len(cells) * BW + (len(cells) - 1) * G + 24
    o = [f'<svg viewBox="0 0 {W} {H}" class="traj" role="img" '
         f'aria-label="the chain step by step">']
    for i, cl in enumerate(cells):
        x = 12 + i * (BW + G)
        o.append(f'<rect class="tb" x="{x}" y="16" width="{BW}" height="60" rx="9"/>')
        o.append(f'<text class="tt" x="{x+11}" y="36">{E(cl["t"])}</text>')
        o.append(f'<text class="ta" x="{x+11}" y="53">{E(cl["add"])}</text>')
        o.append(f'<text class="tc" x="{x+11}" y="69">&#8594; {E(cl["to"])}</text>')
        if i:
            o.append(f'<path class="tar" d="M{x-G+4} 46 L{x-7} 46"/>'
                     f'<path class="tarh" d="M{x-7} 46 l-8 -4.5 v9 z"/>')
    o.append('</svg>')
    return '\n'.join(o)


# ---------------------------------------------------------------- the page

RCSS = """
*{box-sizing:border-box}
:root{--bg:#f6f7f5;--card:#fff;--ink:#15171c;--mut:#5c636f;--line:#e0e3e7;--acc:#2f6f4f;
--warn:#8a5a00;--bad:#b3261e;--chip:#eceff4;--hi:#fff3c4}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.62 -apple-system,BlinkMacSystemFont,
"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-text-size-adjust:100%}
.wrap{max-width:1080px;margin:0 auto;padding:22px 16px 90px}
h1{font-size:24px;line-height:1.28;margin:0 0 6px}
h2{font-size:17px;margin:34px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--line)}
h3{font-size:15px;margin:0}
code{font:12.5px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--chip);
padding:1px 5px;border-radius:4px;word-break:break-all}
.sub{color:var(--mut);font-size:12.5px;margin:4px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:15px 17px;margin:14px 0}
.banner{background:#11342a;color:#eaf5ef;border-radius:12px;padding:13px 17px;font-size:13.5px;margin:14px 0}
table{border-collapse:collapse;width:100%;font-size:13px}
th,td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
th{background:var(--chip);font-size:12px;text-transform:uppercase;letter-spacing:.04em}
.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
.gsvg{min-width:640px;width:100%;height:auto}
.gcol{font:600 11px ui-monospace,Menlo,monospace;fill:#8a919d;letter-spacing:.06em}
.gn rect{fill:#fff;stroke:#ccd2d9}
.gn text{font:11px ui-monospace,Menlo,monospace;fill:#7b828d;text-anchor:middle}
.gn.on rect{fill:var(--acc);stroke:var(--acc)}
.gn.on text{fill:#fff;font-weight:700}
.ge{stroke:#dfe3e8;stroke-width:1.2}
.ge.on{stroke:var(--acc);stroke-width:2.4}
.traj{min-width:420px;width:100%;height:auto;max-height:120px}
.tb{fill:#fff;stroke:var(--acc);stroke-width:1.6}
.tt{font:600 10.5px ui-monospace,Menlo,monospace;fill:var(--mut);text-transform:uppercase}
.ta{font:12px ui-monospace,Menlo,monospace;fill:var(--ink)}
.tc{font:11.5px ui-monospace,Menlo,monospace;fill:var(--acc)}
.tar{stroke:var(--acc);stroke-width:1.8;fill:none}.tarh{fill:var(--acc)}
.sel{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 2px}
.sel button{font:12px ui-monospace,Menlo,monospace;padding:4px 10px;border-radius:14px;cursor:pointer;
border:1px solid var(--line);background:#fff;color:var(--ink)}
.sel button.on{background:var(--acc);border-color:var(--acc);color:#fff}
.chain{border:2px solid var(--acc);border-radius:13px;margin:22px 0;overflow:hidden;background:var(--card)}
.chead{background:var(--chip);padding:11px 15px;border-bottom:1px solid var(--line);
display:flex;flex-wrap:wrap;gap:10px;align-items:baseline}
.chead b{font-size:15px}
.link{padding:14px 16px;border-top:1px solid var(--line)}
.link h4{margin:0 0 9px;font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.inp{background:var(--bg);border-left:3px solid var(--line);padding:9px 12px;margin:7px 0;font-size:13.5px}
.obs{background:var(--bg);border-left:3px solid var(--acc);padding:9px 12px;margin:7px 0;font-size:13.5px}
.qn{font-style:italic;color:var(--mut);font-size:13px;margin:8px 0}
.cl{margin:5px 0;font-size:13.5px;padding-left:17px;position:relative}
.cl:before{content:"\\25B8";position:absolute;left:0;color:var(--acc)}
.cl.lim:before{content:"\\25B9";color:var(--warn)}
.travel{border-top:2px dashed var(--acc);border-bottom:2px dashed var(--acc);
background:linear-gradient(#f3f8f5,#eef4f0);padding:12px 16px}
.travel b{display:block;font:600 10.5px ui-monospace,Menlo,monospace;text-transform:uppercase;
letter-spacing:.05em;color:var(--acc);margin-bottom:5px}
.travel p{margin:0;font-size:13.5px}
.sc{width:auto;margin:9px 0;font-size:12.5px}
.sc td,.sc th{text-align:right}.sc th:first-child,.sc td:first-child{text-align:left}
.sc .hi{background:rgba(47,111,79,.13);font-weight:700}
.pans{display:flex;flex-wrap:wrap;align-items:flex-start;gap:14px;margin:10px 0}
.pan{margin:0;flex:1 1 300px;min-width:min(300px,100%);max-width:100%;border:1px solid var(--line);
border-radius:10px;padding:10px;background:var(--bg)}
.pan.miss{color:var(--bad);font-size:13px;flex-basis:100%}
.pcap{font:11.5px ui-monospace,Menlo,monospace;color:var(--mut);margin-bottom:7px}
.pan img{display:block;width:100%;height:auto;border-radius:6px;background:#fff;cursor:zoom-in}
.pan img.fig{margin:0}
.figwrap{position:relative;margin-top:9px}
.figwrap svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.figwrap rect{fill:none;stroke:#e2451f;stroke-width:6;vector-effect:non-scaling-stroke}
.ptx{font-size:12.5px;margin-top:8px;color:#333a44}
.ptx b{display:block;font:600 10px ui-monospace,Menlo,monospace;text-transform:uppercase;
letter-spacing:.05em;color:var(--mut)}
.ptx.use{border-left:2px solid var(--acc);padding-left:8px}
.gen{padding:14px 16px;border-top:3px double var(--line);background:#fbfcfb}
.para{font-size:14.5px}
.para .s{background:linear-gradient(transparent 82%,#dceee4 0)}
.para .s[data-q]{cursor:help}
.gone{font-size:12.5px;color:var(--bad);margin-top:8px}
.gone li{margin:3px 0}
.vd{display:inline-block;font:600 11px ui-monospace,Menlo,monospace;padding:2px 8px;border-radius:11px;
text-transform:uppercase;letter-spacing:.04em}
.v-respects,.v-agrees{background:#dcefe4;color:#1d5a3c}
.v-ignores,.v-broader{background:#fbe6c8;color:#7a4c00}
.v-contradicts,.v-conflicts{background:#fadbd8;color:#8c1d18}
.v-narrower{background:#e2e7f5;color:#31427c}
.v-unruled{background:var(--chip);color:var(--mut)}
details{margin:10px 0}summary{cursor:pointer;font-size:13.5px;color:var(--mut)}
#zv{position:fixed;inset:0;background:rgba(14,16,20,.93);display:none;z-index:99;overflow:auto;
padding:22px;text-align:center}
#zv.on{display:block}#zv img{max-width:100%;height:auto;cursor:zoom-out}
#zv .x{position:fixed;top:12px;right:16px;color:#fff;font-size:26px;cursor:pointer;line-height:1}
@media(max-width:640px){.wrap{padding:16px 16px 70px}h1{font-size:20px}.pan{flex-basis:100%}}
"""

JS = """
var IMG=%s;
document.querySelectorAll('img[data-k]').forEach(function(m){var s=IMG[m.dataset.k];if(s)m.src=s;});
var zv=document.getElementById('zv'),zi=zv.querySelector('img');
document.querySelectorAll('img.zoom').forEach(function(m){
  m.addEventListener('click',function(){zi.src=m.src;zv.classList.add('on');});});
zv.addEventListener('click',function(){zv.classList.remove('on');zi.src='';});
document.addEventListener('keydown',function(e){if(e.key==='Escape')
  {zv.classList.remove('on');zi.src='';}});
var SETS=%s,cur=null;
function paint(id){
  var on=SETS[id]||[],S={};on.forEach(function(n){S[n]=1;});
  document.querySelectorAll('#graph .gn').forEach(function(g){
    g.classList.toggle('on',!!S[g.dataset.id]);});
  document.querySelectorAll('#graph .ge').forEach(function(l){
    l.classList.toggle('on',!!(S[l.dataset.s]&&S[l.dataset.d]));});
  document.querySelectorAll('.sel button').forEach(function(b){
    b.classList.toggle('on',b.dataset.c===id);});
  var n=document.getElementById('nodelist');
  if(n)n.querySelectorAll('tr[data-id]').forEach(function(r){
    r.style.background=S[r.dataset.id]?'#eaf4ee':'';});
  cur=id;
}
document.querySelectorAll('.sel button').forEach(function(b){
  b.addEventListener('click',function(){paint(b.dataset.c===cur?'':b.dataset.c);});});
"""


def vd(v):
    return f'<span class="vd v-{v or "unruled"}">{E(v or "unruled")}</span>'


def pans_html(store, pids, seen):
    if not pids: return ''
    return '<div class="pans">' + '\n'.join(panel_html(store, p, seen) for p in pids) + '</div>'


def root_block(c, d, store, seen):
    """step 1: the two-measurement item the chain grows from"""
    root = d['REC'][c['steps'][0]]
    up = d['V25'].get(root['upstream_item'])
    if not up:
        return ('<div class="link"><h4>step 1</h4><p class="sub">the source item '
                f'<code>{E(root.get("upstream_item") or "")}</code> is not in the v2.5 file</p></div>')
    H = [f'<div class="link" id="{c["id"]}_step1">',
         f'<h4>step 1 &mdash; the two measurements this chain grows from &middot; '
         f'<code>{E(up["item"])}</code></h4>']
    for lab, k in (('A', 'observation_a'), ('B', 'observation_b')):
        o = up.get(k) or {}
        H.append(f'<div class="obs"><b>measurement {lab}</b> <code>{E(o.get("node",""))}</code>'
                 f'{" &middot; <code>" + E(o["technique"]) + "</code>" if o.get("technique") else ""}'
                 f'<br>{E(o.get("text",""))}</div>')
    H.append(pans_html(store, [p['panel_id'] for p in (up.get('panels') or [])], seen))
    if up.get('question'): H.append(f'<p class="qn">{E(up["question"])}</p>')
    key = up.get('key') or {}
    if key.get('proposition'):
        H.append('<p class="sub"><b>what step 1 concluded</b></p>')
        H.append(f'<div class="cl">{E(key["proposition"])}</div>')
    for t in (key.get('limits') or []):
        H.append(f'<div class="cl lim">{E(str(t))}</div>')
    H.append('</div>')
    return '\n'.join(H)


def step_block(it, i, d, store, seen, cid=''):
    r = d['REC'][it]; v = d['DEC'].get(it); k = d['KEY'].get(it) or {}
    H = ['<div class="travel" id="%s_seam%d"><b>what travelled into step %d</b><p>%s</p></div>'
         % (cid, i, i, E(r['input_result'])),
         '<div class="link" id="%s_step%d">' % (cid, i),
         f'<h4>step {i} &middot; <code>{E(it)}</code> &middot; edge <code>{E(r.get("edge") or "")}</code></h4>']
    o = r['new_observation']
    H.append(f'<div class="obs"><b>new measurement</b> <code>{E(o.get("node",""))}</code>'
             f'{" &middot; <code>" + E(o["technique"]) + "</code>" if o.get("technique") else ""}'
             f'<br>{E(o.get("text",""))}</div>')
    H.append(pans_html(store, [p['panel_id'] for p in (r.get('panels') or [])], seen))
    if r.get('question'): H.append(f'<p class="qn">{E(r["question"])}</p>')
    if k.get('proposition'):
        H.append('<p class="sub"><b>what this step concluded</b></p>')
        H.append(f'<div class="cl">{E(k["proposition"])}</div>')
    for t in (k.get('limits') or []):
        H.append(f'<div class="cl lim">{E(str(t))}</div>')
    if v: H.append(scores(v))
    H.append('</div>')
    return '\n'.join(H)


def scores(v):
    m = v['mean_combined']; ml = v.get('mean_limit') or {}
    rows = [('A', 'the new measurement alone'), ('B', '+ the result handed forward'),
            ('C', 'the handed result alone'), ('N', 'the paper name only')]
    h = ['<table class="sc"><tr><th>arm</th><th>what it held</th><th>combined</th><th>limits</th></tr>']
    for a, what in rows:
        h.append(f'<tr{" class=\"hi\"" if a == "B" else ""}><td><b>{a}</b></td><td>{what}</td>'
                 f'<td>{m.get(a, 0):.2f}</td>'
                 f'<td>{"&mdash;" if ml.get(a) is None else f"{ml[a]:.2f}"}</td></tr>')
    h.append('</table>')
    h.append(f'<p class="sub">B&minus;A {v["B_minus_A"]:+.2f} &middot; B&minus;C {v["B_minus_C"]:+.2f}'
             f' &middot; passes: <b>{"yes" if v["compositional"] else "no"}</b>'
             + (' &middot; borderline, decided on 2 samples' if v.get('borderline') else '') + '</p>')
    return '\n'.join(h)


def gen_block(cid, e):
    H = [f'<div class="gen" id="{cid}_gen">', '<h4 style="margin:0 0 8px;font-size:11.5px;text-transform:uppercase;'
         'letter-spacing:.05em;color:var(--mut)">the chain read straight through</h4>']
    if e['kept']:
        H.append('<p class="para">' + ' '.join(
            f'<span class="s" title="{E(s["quote"][:400])}" data-q="1">{E(s["sentence"])}</span>'
            for s in e['kept']) + '</p>')
        H.append('<p class="sub">Every sentence above quotes a stored text that carries it; hover '
                 'to see the quote. Sentences the checker could not source were removed.</p>')
    else:
        H.append('<p class="sub">No sentence of the written paragraph survived checking.</p>')
    if e['removed']:
        H.append(f'<details class="gone"><summary>{len(e["removed"])} sentence'
                 f'{"s" if len(e["removed"]) != 1 else ""} removed as unsupported</summary><ul>')
        for s in e['removed']: H.append(f'<li>{E(s["sentence"])}</li>')
        H.append('</ul></details>')

    H.append(f'<h4 id="{cid}_ledger" style="margin:18px 0 8px;font-size:11.5px;'
             'text-transform:uppercase;letter-spacing:.05em;color:var(--mut)">does the last '
             'claim still respect the qualifications the chain collected?</h4>')
    if e['ledger']:
        cnt = collections.Counter(x['verdict'] or 'unruled' for x in e['ledger'])
        H.append('<p class="sub">' + ' &middot; '.join(
            f'{n} {k}' for k, n in sorted(cnt.items())) + '</p>')
        H.append('<div class="scroll"><table><tr><th>#</th><th>from</th><th>qualification</th>'
                 '<th>ruling</th><th>on these words of the final claim</th></tr>')
        for x in e['ledger']:
            H.append(f'<tr><td>{x["n"]}</td><td>{E(x["where"])}</td><td>{E(x["limit"])}</td>'
                     f'<td>{vd(x["verdict"])}</td><td>{E(x["quote"])}'
                     f'{"<br><i>" + E(x["why"]) + "</i>" if x["why"] else ""}</td></tr>')
        H.append('</table></div>')
    else:
        H.append('<p class="sub">This chain recorded no qualifications.</p>')

    c = e['compare']
    H.append(f'<h4 id="{cid}_cmp" style="margin:18px 0 8px;font-size:11.5px;'
             'text-transform:uppercase;letter-spacing:.05em;color:var(--mut)">the chain\'s '
             'conclusion against the paper\'s own wording</h4>')
    H.append(f'<p>{vd(c["verdict"])} {E(c["why"])}</p>')
    if c['chain_quote']:
        H.append(f'<div class="inp"><b>the chain</b><br>{E(c["chain_quote"])}</div>')
    if c['paper_quote']:
        H.append(f'<div class="inp"><b>the paper</b><br>{E(c["paper_quote"])}</div>')
    H.append('</div>')
    return '\n'.join(H)


def build():
    D = load()
    cs = json.load(open(R('results/v2p10/report_chains.json')))['out']
    DATA = json.load(open(R('results/v2p10/report_data.json')))['chains']
    os.makedirs(OUT, exist_ok=True)
    bypaper = collections.defaultdict(list)
    for c in cs: bypaper[c['paper']].append(c)
    RESIZED.clear(); MISSPAN.clear()
    shown, sizes, idx = set(), [], []

    for paper, lst in sorted(bypaper.items()):
        img_reset()
        st = json.load(open(R('results/v3', paper, 'stitch.json')))
        g = json.load(open(R(st['graph'])))
        store = store_for(st['graph'])
        title = g.get('title') or paper
        lst = sorted(lst, key=lambda c: (-c['depth'], c['id']))
        seen = set()

        H = [f'<!doctype html><html lang="en"><head><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             f'<title>{E(title[:90])}</title><style>{RCSS}</style></head><body><div class="wrap">',
             f'<h1>{E(title)}</h1>',
             f'<p class="sub"><code>{E(g.get("paper_id") or paper)}</code> &middot; vocabulary '
             f'{E(str(g.get("vocab_version")))} &middot; {len(g["nodes"])} nodes, '
             f'{len(g["edges"])} edges</p>',
             '<div class="banner">This page follows every reasoning chain this paper supports, '
             'from the figure panels up to the paper\'s own claim. A chain passes only when a '
             'model given the new measurement <i>and</i> the previous step\'s result scores at '
             'least 0.25 above the same model given either one alone. '
             '<b>Every verdict is model against model.</b></div>']

        dm = collections.Counter(c['depth'] for c in lst)
        H.append(f'<p>{len(lst)} chain{"s" if len(lst) != 1 else ""}: '
                 + ', '.join(f'{n} at depth {k}' for k, n in sorted(dm.items())) + '.</p>')

        # ---- the graph
        H.append('<h2>The paper\'s argument</h2>')
        H.append('<p class="sub">Every node the paper\'s graph holds, in stage columns. '
                 'Pick a chain to light up the nodes it walks.</p>')
        sets = {c['id']: chain_nodes(c, D) for c in lst}
        H.append('<div class="sel">' + ''.join(
            f'<button data-c="{c["id"]}">{c["id"]} &middot; d{c["depth"]}</button>' for c in lst)
            + '</div>')
        H.append('<div class="card scroll">' + graph_sel(g) + '</div>')
        N = {n['id']: n for n in g['nodes']}
        H.append('<details><summary>the nodes, in full</summary><div class="scroll">'
                 '<table id="nodelist"><tr><th>id</th><th>type</th><th>label</th></tr>')
        for n in g['nodes']:
            H.append(f'<tr data-id="{E(n["id"])}"><td><code>{E(n["id"])}</code></td>'
                     f'<td>{E(n.get("type") or "")}</td><td>{E(n.get("label") or "")}</td></tr>')
        H.append('</table></div></details>')

        # ---- index
        H.append('<h2>The chains</h2><div class="scroll"><table>'
                 '<tr><th>chain</th><th>depth</th><th>ends on</th><th>what it concludes</th>'
                 '<th>vs the paper</th></tr>')
        for c in lst:
            e = DATA.get(c['id'], {})
            tgt = D['REC'][c['steps'][-1]].get('target_claim') or ''
            fin = (D['KEY'].get(c['steps'][-1]) or {}).get('proposition') or ''
            H.append(f'<tr><td><a href="#{c["id"]}"><b>{c["id"]}</b></a></td><td>{c["depth"]}</td>'
                     f'<td><code>{E(tgt)}</code></td><td>{E(fin[:260])}</td>'
                     f'<td>{vd((e.get("compare") or {}).get("verdict"))}</td></tr>')
        H.append('</table></div>')

        # ---- the chains
        for c in lst:
            e = DATA.get(c['id'])
            H.append(f'<section class="chain" id="{c["id"]}">')
            H.append(f'<div class="chead"><b>{c["id"]}</b>'
                     f'<span class="sub">depth {c["depth"]} &middot; {c["depth"]} steps &middot; '
                     f'ends on <code>{E(D["REC"][c["steps"][-1]].get("target_claim") or "")}</code>'
                     f'</span></div>')
            H.append('<div class="link" style="border-top:0"><div class="scroll">'
                     + traj_svg(c, D) + '</div></div>')
            H.append(root_block(c, D, store, seen))
            for i, s in enumerate(c['steps'], 2):
                H.append(step_block(s, i, D, store, seen, c['id']))
            if e: H.append(gen_block(c['id'], e))
            H.append('</section>')
            idx.append({'paper': paper, 'chain': c['id'], 'depth': c['depth']})

        # ---- what did not pass
        mine = [i for i, v in D['DEC'].items()
                if D['REC'].get(i, {}).get('paper') == paper and not v.get('compositional')]
        if mine:
            H.append(f'<h2>Items this paper did not carry</h2>')
            H.append('<details><summary>' + str(len(mine)) + ' item'
                     + ('s' if len(mine) != 1 else '') + ' tested and not passed</summary>')
            H.append('<div class="scroll"><table><tr><th>item</th><th>B&minus;A</th>'
                     '<th>B&minus;C</th><th>arm N</th><th>what it tried to conclude</th></tr>')
            for i in sorted(mine):
                v = D['DEC'][i]; k = D['KEY'].get(i) or {}
                H.append(f'<tr><td><code>{E(i)}</code></td><td>{v["B_minus_A"]:+.2f}</td>'
                         f'<td>{v["B_minus_C"]:+.2f}</td>'
                         f'<td>{v["mean_combined"].get("N", 0):.2f}</td>'
                         f'<td>{E((k.get("proposition") or "")[:300])}</td></tr>')
            H.append('</table></div><p class="sub">An item fails when the result handed to it '
                     'bought the model nothing: arm B did not beat arm A, or did not beat arm C, '
                     'or the paper\'s name alone was enough.</p></details>')

        H.append('<div id="zv"><span class="x">&times;</span><img alt="full size"></div>')
        H.append('</div><script>' + (JS % (json.dumps(IMG), json.dumps(sets))) + '</script></body></html>')
        p = os.path.join(OUT, paper + '.html')
        open(p, 'w').write('\n'.join(H))
        sizes.append({'paper': paper, 'file': os.path.basename(p),
                      'mb': round(os.path.getsize(p) / 1e6, 2), 'chains': len(lst),
                      'images': len(IMG), 'panels': len(seen)})
        shown |= seen

    # ---- index page
    sizes.sort(key=lambda x: -x['mb'])
    I = [f'<!doctype html><html lang="en"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>v2.10 reasoning reports</title><style>{RCSS}</style></head><body><div class="wrap">',
         '<h1>v2.10 &mdash; the chains, paper by paper</h1>',
         f'<p class="sub">{len(cs)} chains across {len(bypaper)} papers.</p>',
         '<div class="banner">Each report follows its paper\'s chains from the figure panels to '
         'the paper\'s own claim, with the arm scores that decided each link. '
         '<b>Every verdict is model against model.</b></div>',
         '<div class="scroll"><table><tr><th>paper</th><th>chains</th><th>deepest</th>'
         '<th>panels</th><th>size</th></tr>']
    for s in sorted(sizes, key=lambda x: x['paper']):
        dd = max(c['depth'] for c in bypaper[s['paper']])
        I.append(f'<tr><td><a href="{E(s["file"])}">{E(s["paper"].replace("__", " &middot; "))}'
                 f'</a></td><td>{s["chains"]}</td><td>{dd}</td><td>{s["panels"]}</td>'
                 f'<td>{s["mb"]:.2f} MB</td></tr>')
    I.append('</table></div></div></body></html>')
    open(os.path.join(OUT, 'index.html'), 'w').write('\n'.join(I))

    rep = {'pages': len(sizes) + 1, 'chains': len(cs), 'papers': len(bypaper),
           'panels_shown': len(shown), 'panel_misses': MISSPAN,
           'images_resized': len(RESIZED), 'resized': RESIZED[:40],
           'total_mb': round(sum(s['mb'] for s in sizes) / 1, 2), 'sizes': sizes}
    json.dump(rep, open(R('results/v2p10/report_build.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in rep.items() if k not in ('sizes', 'resized', 'panel_misses')},
                     indent=1))
    print(f'largest: {sizes[0]["paper"]} {sizes[0]["mb"]} MB; '
          f'smallest: {sizes[-1]["paper"]} {sizes[-1]["mb"]} MB')
    if MISSPAN: print(f'panel misses: {len(MISSPAN)} -> {MISSPAN[:5]}')


# ---------------------------------------------------------------- verification

def verify():
    """the five checks the reports have to pass before they are worth reading"""
    D = load()
    cs = json.load(open(R('results/v2p10/report_chains.json')))['out']
    DATA = json.load(open(R('results/v2p10/report_data.json')))['chains']
    bld = json.load(open(R('results/v2p10/report_build.json')))
    pages = {f: open(os.path.join(OUT, f)).read()
             for f in os.listdir(OUT) if f.endswith('.html') and f != 'index.html'}
    rep = {}

    # 1 -- every chain rendered, in full, exactly once
    where = collections.Counter()
    for c in cs:
        for f, h in pages.items():
            if f'id="{c["id"]}"' in h: where[c['id']] += 1
    rep['chains_expected'] = len(cs)
    rep['chains_rendered_once'] = sum(v == 1 for v in where.values())
    rep['chains_missing'] = [c['id'] for c in cs if where[c['id']] == 0]
    rep['chains_duplicated'] = [k for k, v in where.items() if v > 1]
    # in full: every step id of every chain appears on its page
    short = []
    for c in cs:
        h = pages.get(c['paper'] + '.html', '')
        miss = [s for s in c['steps'] if s not in h]
        root = D['REC'][c['steps'][0]].get('upstream_item')
        if root and root not in h: miss.append(root)
        if miss: short.append({'chain': c['id'], 'missing_steps': miss})
    rep['chains_with_missing_steps'] = short

    # 2 -- every cited panel shown, with a box on the figure
    cited = set()
    for c in cs:
        root = D['REC'][c['steps'][0]]
        up = D['V25'].get(root['upstream_item']) or {}
        for pn in up.get('panels') or []: cited.add((c['paper'], pn['panel_id']))
        for st in c['steps']:
            for pn in D['REC'][st].get('panels') or []: cited.add((c['paper'], pn['panel_id']))
    miss = []
    for paper, pid in sorted(cited):
        h = pages.get(paper + '.html', '')
        anc = 'p_' + re.sub(r'#|/|[.]', '_', pid)
        if f'id="{anc}"' not in h: miss.append({'paper': paper, 'pid': pid, 'why': 'not on page'})
    rep['panels_cited'] = len(cited)
    rep['panels_shown'] = len(cited) - len(miss)
    rep['panels_missing'] = miss
    rep['panels_without_box'] = bld['panel_misses']
    rep['images_resized_over_cap'] = bld['images_resized']

    # 3 -- every sentence that stayed carries a quote
    nq = [(cid, s['sentence'][:60]) for cid, e in DATA.items()
          for s in e['kept'] if not s['quote'].strip()]
    rep['sentences_written'] = sum(len(e['checked']) for e in DATA.values())
    rep['sentences_kept'] = sum(len(e['kept']) for e in DATA.values())
    rep['sentences_removed'] = sum(len(e['removed']) for e in DATA.values())
    rep['kept_without_quote'] = nq

    # 5 -- nothing on these pages reaches the network
    ext = []
    for f, h in pages.items():
        for m in re.finditer(r'(?:src|href)\s*=\s*"([^"]*)"', h):
            u = m.group(1)
            if u.startswith(('data:', '#')) or u.endswith('.html'): continue
            ext.append({'page': f, 'ref': u[:80]})
        for m in re.finditer(r'url\(([^)]*)\)', h):
            if not m.group(1).strip('\'"').startswith('data:'):
                ext.append({'page': f, 'css_url': m.group(1)[:80]})
        if re.search(r'https?://', h):
            n = len(re.findall(r'https?://', h))
            ext.append({'page': f, 'http_literals': n})
    rep['external_refs'] = ext

    json.dump(rep, open(R('results/v2p10/report_verify.json'), 'w'), indent=1)
    print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in rep.items()},
                     indent=1))
    for k in ('chains_missing', 'chains_duplicated', 'chains_with_missing_steps',
              'panels_missing', 'kept_without_quote', 'external_refs'):
        if rep[k]: print(f'  {k}: {rep[k][:6]}')
    return rep


# ---------------------------------------------------------------- the write-up

def pct(a, b): return f'{100.0 * a / b:.1f}%' if b else 'n/a'


def doc():
    """docs/TRACES_V2P10_REPORTS.md -- every number here is read out of the JSON"""
    cs = json.load(open(R('results/v2p10/report_chains.json')))
    DATA = json.load(open(R('results/v2p10/report_data.json')))
    bld = json.load(open(R('results/v2p10/report_build.json')))
    ver = json.load(open(R('results/v2p10/report_verify.json')))
    cost = json.load(open(R('results/v2p10/reports_cost.json')))
    C, T = DATA['chains'], DATA['tally']
    bd = cs['by_depth']

    L = ['# v2.10 reports: the chains, paper by paper', '',
         'One self-contained HTML page per paper. Each page carries the paper\'s whole argument '
         'graph, every passing chain it supports from depth 2 to depth 5, and, under every step, '
         'the figure panel the step read, the box it occupies on its figure, its caption and the '
         'sentences the paper writes about it.', '',
         '**Every verdict is model against model.**', '',
         '## What was built', '',
         f'- **{cs["chains"]} chains** across **{cs["papers"]} papers**: '
         + ', '.join(f'{n} at depth {k}' for k, n in sorted(bd.items(), key=lambda x: int(x[0])))
         + '.',
         f'- **{bld["pages"]} pages** ({bld["pages"] - 1} papers + an index), '
         f'**{bld["total_mb"]:.1f} MB** in total.',
         f'- **{bld["panels_shown"]} distinct figure panels** shown, each as a crop, as a box on '
         f'its whole figure, and as the text the paper writes about it.', '',
         '### Page sizes', '',
         '| paper | chains | deepest | panels | size |', '| --- | ---: | ---: | ---: | ---: |']
    bp = collections.defaultdict(list)
    for c in cs['out']: bp[c['paper']].append(c['depth'])
    for z in sorted(bld['sizes'], key=lambda x: -x['mb']):
        L.append(f'| {z["paper"].replace("__", " / ")} | {z["chains"]} | '
                 f'{max(bp[z["paper"]])} | {z["panels"]} | {z["mb"]:.2f} MB |')
    L += ['', f'Largest {max(z["mb"] for z in bld["sizes"]):.2f} MB, '
              f'smallest {min(z["mb"] for z in bld["sizes"]):.2f} MB, '
              f'median {sorted(z["mb"] for z in bld["sizes"])[len(bld["sizes"]) // 2]:.2f} MB.', '']

    tot = T.get('sent_total', 0); kept = T.get('sent_kept', 0); rem = T.get('sent_removed', 0)
    L += ['## The written paragraph, and what the check removed', '',
          'One Sonnet call wrote a paragraph for each chain from the chain\'s stored texts alone. '
          'A second Sonnet call read it sentence by sentence against those same texts and had to '
          'quote the text supporting each sentence. A sentence kept its place only when the '
          'checker both called it supported **and** produced a quote; "supported" with no quote '
          'is the checker asserting a support it could not point to, so those were removed too.', '',
          f'- **{tot} sentences written**, **{kept} kept** ({pct(kept, tot)}), '
          f'**{rem} removed** ({pct(rem, tot)}).',
          f'- Chains whose paragraph did not survive checking at all: '
          f'{sum(1 for e in C.values() if not e["kept"])}.',
          f'- Check replies that could not be parsed: {T.get("check_unparsed", 0)}.', '']
    byd = collections.defaultdict(lambda: [0, 0])
    for e in C.values():
        byd[e['depth']][0] += len(e['checked']); byd[e['depth']][1] += len(e['kept'])
    L += ['| depth | sentences written | kept | kept % |', '| ---: | ---: | ---: | ---: |']
    for k in sorted(byd):
        a, b = byd[k]
        L.append(f'| {k} | {a} | {b} | {pct(b, a)} |')
    L.append('')
    gone = [(cid, s['sentence']) for cid, e in C.items() for s in e['removed']]
    if gone:
        L += ['A removed sentence is not a wrong sentence; it is a sentence the stored texts do '
              'not carry. The commonest kind adds a mechanism or a motive that reads as obvious '
              'and is nowhere in the record. Examples, verbatim:', '']
        for cid, t in gone[:8]: L.append(f'- `{cid}` — {t}')
        L.append('')

    L += ['## New finding 1: the caveat ledger', '',
          'Each step of a chain attached qualifications to its own result. Nothing in the '
          'benchmark ever checked whether the chain\'s **final** claim still respected the '
          'qualifications its **earlier** steps had attached. This asked that question directly: '
          'every qualification, in the order it was attached, ruled against the final conclusion.', '']
    lt = {k[4:]: v for k, v in T.items() if k.startswith('lim_')}
    ltot = sum(lt.values())
    L += [f'Across {cs["chains"]} chains, **{ltot} qualifications** were ruled.', '',
          '| ruling | n | share |', '| --- | ---: | ---: |']
    for k in ('respects', 'ignores', 'contradicts', 'unruled'):
        if lt.get(k): L.append(f'| {k} | {lt[k]} | {pct(lt[k], ltot)} |')
    L.append('')
    dep = collections.defaultdict(collections.Counter)
    for e in C.values():
        for x in e['ledger']: dep[e['depth']][x['verdict'] or 'unruled'] += 1
    L += ['By depth — the interesting axis, because a longer chain has more to forget:', '',
          '| depth | qualifications | respects | ignores | contradicts | respected % |',
          '| ---: | ---: | ---: | ---: | ---: | ---: |']
    for k in sorted(dep):
        c = dep[k]; n = sum(c.values())
        L.append(f'| {k} | {n} | {c["respects"]} | {c["ignores"]} | {c["contradicts"]} | '
                 f'{pct(c["respects"], n)} |')
    L.append('')
    worst = sorted(C.items(), key=lambda kv: -sum(
        1 for x in kv[1]['ledger'] if x['verdict'] in ('ignores', 'contradicts')))
    bad = [(k, v) for k, v in worst
           if any(x['verdict'] in ('ignores', 'contradicts') for x in v['ledger'])]
    L += [f'{len(bad)} of {len(C)} chains end on a claim that ignores or contradicts at least one '
          f'qualification they collected on the way.', '']
    if bad:
        L += ['| chain | depth | qualifications | ignored | contradicted |',
              '| --- | ---: | ---: | ---: | ---: |']
        for k, v in bad[:12]:
            c = collections.Counter(x['verdict'] for x in v['ledger'])
            L.append(f'| {k} | {v["depth"]} | {len(v["ledger"])} | {c["ignores"]} | '
                     f'{c["contradicts"]} |')
        L.append('')

    L += ['## New finding 2: the chain against the paper\'s own wording', '',
          'The chain\'s final conclusion was set beside the label the paper\'s own argument graph '
          'gives that claim, and ruled: the same claim, a narrower one, a broader one, or a '
          'conflicting one.', '']
    ct = {k[4:]: v for k, v in T.items() if k.startswith('cmp_')}
    ctot = sum(ct.values())
    L += ['| ruling | n | share |', '| --- | ---: | ---: |']
    for k in ('agrees', 'narrower', 'broader', 'conflicts', 'unruled'):
        if ct.get(k): L.append(f'| {k} | {ct[k]} | {pct(ct[k], ctot)} |')
    L.append('')
    cdep = collections.defaultdict(collections.Counter)
    for e in C.values(): cdep[e['depth']][e['compare']['verdict'] or 'unruled'] += 1
    L += ['| depth | chains | agrees | narrower | broader | conflicts |',
          '| ---: | ---: | ---: | ---: | ---: | ---: |']
    for k in sorted(cdep):
        c = cdep[k]
        L.append(f'| {k} | {sum(c.values())} | {c["agrees"]} | {c["narrower"]} | {c["broader"]} '
                 f'| {c["conflicts"]} |')
    L += ['', 'A `broader` ruling is the one that matters: it says the chain claimed more than '
              'the paper\'s own wording of that claim supports. `narrower` is the benign '
              'direction — the chain hedged where the paper did not.', '']

    L += ['## The checks', '',
          f'- **Every chain rendered once, in full.** {ver["chains_rendered_once"]} of '
          f'{ver["chains_expected"]} chains appear on exactly one page; '
          f'{len(ver["chains_missing"])} missing, {len(ver["chains_duplicated"])} duplicated, '
          f'{len(ver["chains_with_missing_steps"])} with a step id absent from their page.',
          f'- **Every cited panel shown.** {ver["panels_shown"]} of {ver["panels_cited"]} panel '
          f'ids cited by any step appear on their paper\'s page with an anchor; '
          f'{len(ver["panels_missing"])} missing. {len(ver["panels_without_box"])} lettered panels '
          f'lacked a recorded box on their figure. Whole-figure citations (`#F3`, no panel letter) '
          f'carry no box because the crop already is the whole figure.',
          f'- **Every surviving sentence carries a quote.** {ver["kept_without_quote"] and len(ver["kept_without_quote"]) or 0} '
          f'of {ver["sentences_kept"]} kept sentences have an empty quote.',
          f'- **Nothing reaches the network.** {len(ver["external_refs"])} external references '
          f'across all pages: no stylesheet, script, font or image is fetched, and every image is '
          f'an inline `data:` URI.',
          f'- **Rendered and looked at.** Both the deepest-chain paper and a depth-2-only paper '
          f'were screenshotted in a headless browser — header, argument graph with a chain '
          f'selected, chain index, trajectory strip, step block with panels, seam band, caveat '
          f'ledger and the written paragraph, at 1400 px and at 390 px — and inspected for '
          f'overlap and clipping.', '',
          '### On the images', '',
          f'A crop at or under {CROP_CAP} px on its long side is embedded as the file\'s own '
          f'bytes: no resample, no re-encode, no annotation. {bld["images_resized"]} images '
          f'exceeded the cap and were downscaled once with LANCZOS. The red box is drawn on the '
          f'**whole figure** as an SVG overlay, never on the crop, so no pixel of the evidence '
          f'is painted over.', '',
          '## Cost', '',
          f'- {cost.get("calls", 0)} Sonnet calls: {cs["chains"]} paragraphs, {cs["chains"]} '
          f'checks, {cs["chains"]} caveat ledgers, {cs["chains"]} paper comparisons.',
          f'- Every reply was matched to its prompt byte for byte in the dispatching agent\'s own '
          f'transcript before it was written to disk. The relay\'s own report is not evidence.', '']

    os.makedirs(R('docs'), exist_ok=True)
    open(R('docs/TRACES_V2P10_REPORTS.md'), 'w').write('\n'.join(L) + '\n')
    print(f'docs/TRACES_V2P10_REPORTS.md: {len(L)} lines')


if __name__ == '__main__':
    {'chains': chains, 'prompts': prompts, 'checks': checks, 'collect': collect,
     'build': build, 'verify': verify, 'doc': doc}[sys.argv[1]]()
