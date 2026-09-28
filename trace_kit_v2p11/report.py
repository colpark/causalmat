"""report.py: the v2.11 report for Nano_Letters 10.1021/acs.nanolett.6b04294.

  python3 trace_kit_v2p11/report.py

No model call. Same layout as v2.10, with what v2.10 did not show: the seed tested like a link,
the six gates with their reasons, the evidence-validity rulings, what each arm was actually
handed, and every arm answer verbatim.

The panel renderer, the stage-column graph and the image handling come from
trace_kit_v2p10/reports.py unchanged, so a panel here is shown exactly as it is there.

Every verdict is model against model.
"""
import collections, html, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p10'))
sys.path.insert(0, R('trace_kit_v2p11'))
import reports as V10  # noqa: E402
import pilot as P  # noqa: E402

E = html.escape
OUT = P.OUT
PAGE = os.path.join(OUT, 'report.html')
MODEL = 'claude-sonnet-5 (every role: answerer, splitter, checker, grader, validity judge, ledger)'

CSS_EXTRA = """
.gate{width:100%;font-size:12.5px;margin:9px 0}
.gate td,.gate th{padding:5px 9px}
.gate .ok{color:#1d5a3c;font-weight:700}
.gate .no{color:#b3261e;font-weight:700}
.unit{border:1px solid var(--line);border-radius:11px;margin:14px 0;background:var(--card);overflow:hidden}
.unit.pass{border-color:var(--acc)}
.unit.fail{border-color:var(--bad)}
.uhead{padding:10px 14px;background:var(--chip);border-bottom:1px solid var(--line);
display:flex;flex-wrap:wrap;gap:9px;align-items:baseline}
.badge{display:inline-block;font:700 10.5px ui-monospace,Menlo,monospace;padding:2px 9px;
border-radius:11px;text-transform:uppercase;letter-spacing:.05em}
.b-pass{background:#dcefe4;color:#1d5a3c}.b-fail{background:#fadbd8;color:#8c1d18}
.b-seed{background:#e7e2f5;color:#4a3580}.b-link{background:#e2e7f5;color:#31427c}
.b-add{background:#fbe6c8;color:#7a4c00}
.fam{border:2px solid var(--acc);border-radius:13px;margin:22px 0;padding:0 0 8px;background:#fbfcfb}
.fam.none{border-color:var(--bad)}
.famhead{padding:11px 15px;background:var(--chip);border-bottom:1px solid var(--line)}
.arm{font:12.5px/1.55 ui-monospace,Menlo,monospace;white-space:pre-wrap;background:var(--bg);
border-left:3px solid var(--line);padding:9px 12px;margin:6px 0;max-height:420px;overflow:auto}
.rub{font-size:12.5px;background:var(--bg);border:1px solid var(--line);border-radius:9px;
padding:10px 13px;white-space:pre-wrap;font-family:ui-monospace,Menlo,monospace;max-height:300px;
overflow:auto}
.v-supported{background:#dcefe4;color:#1d5a3c}
.v-overreaches{background:#fbe6c8;color:#7a4c00}
.v-unsupported{background:#fadbd8;color:#8c1d18}
.v-unruled{background:var(--chip);color:var(--mut)}
.recv td:first-child{white-space:nowrap}
"""


def vd(v, cls=None):
    return f'<span class="badge {cls or "v-" + (v or "unruled")}">{E(str(v or "unruled"))}</span>'


def num(x, d=2):
    return '&mdash;' if x is None else f'{x:.{d}f}'


def received(it, d):
    """what each arm was handed, read back out of the prompt that was sent"""
    s1 = json.load(open(os.path.join(OUT, 'step1.json')))
    row = next((r for r in s1['per_link'] if r['link'] == it), None)
    H = ['<table class="recv"><tr><th>arm</th><th>observation text</th><th>cropped panels</th>'
         '<th>whole figures</th><th>captions</th><th>earlier result</th><th>its limits</th></tr>']
    if row:
        for a in ('A', 'B', 'C', 'N'):
            g = row[a]
            if not g: H.append(f'<tr><td><b>{a}</b></td><td colspan="6">no prompt on file</td></tr>'); continue
            H.append(f'<tr><td><b>{a}</b></td><td>{"yes" if g["observation_text"] else "no"}</td>'
                     f'<td>{g["crop_paths"]}</td><td>{g["whole_figures"]}</td>'
                     f'<td>{"yes" if g["captions"] else "no"}</td>'
                     f'<td>{"yes" if g["earlier_result"] else "no"}</td>'
                     f'<td>{g["limits_present"]}/{row["n_input_limits"]}</td></tr>')
    else:
        # a seed: the arms were built in this run, symmetric by construction
        x = d['V25'][it]
        pa = P.seed_panels(x, d, x['observation_a']['node'])
        pb = P.seed_panels(x, d, x['observation_b']['node'])
        for a, n, e in (('A', len(pa), 'observation A only'), ('B', len(pa) + len(pb), 'both observations'),
                        ('C', len(pb), 'observation B only'), ('N', 0, 'title and journal only')):
            H.append(f'<tr><td><b>{a}</b></td><td>{E(e)}</td><td>{n}</td><td>0</td>'
                     f'<td>{"yes" if n else "no"}</td><td>n/a (a seed has none)</td>'
                     f'<td>n/a</td></tr>')
    H.append('</table>')
    return '\n'.join(H)


def gate_table(u):
    names = {
        '1_dependency': 'dependency — B beats A and C by ≥ 0.25',
        '2_relation': 'relation — B beats the stacked baseline by ≥ 0.25',
        '3_absolute': 'absolute quality — B ≥ 0.60',
        '4_no_contradictions': 'no contradictions in arm B',
        '5_caveats': 'caveats — B’s limit score ≥ C’s',
        '6_validity': 'validity — no combined claim unsupported or overreaching',
    }
    H = ['<table class="gate"><tr><th>#</th><th>gate</th><th>result</th><th>why</th></tr>']
    for k in sorted(u['gates']):
        ok = u['gates'][k]
        H.append(f'<tr><td>{k[0]}</td><td>{names[k]}</td>'
                 f'<td class="{"ok" if ok else "no"}">{"pass" if ok else "FAIL"}</td>'
                 f'<td>{E(u["why"][k])}</td></tr>')
    H.append('</table>')
    return '\n'.join(H)


def score_table(u):
    s = u['scores']
    H = ['<table class="sc"><tr><th>arm</th><th>what it held</th><th>combined</th></tr>']
    for a, what in (('A', 'one side alone'), ('B', 'both sides'), ('C', 'the other side alone'),
                    ('N', 'the paper name only')):
        cls = ' class="hi"' if a == 'B' else ''
        H.append(f'<tr{cls}><td><b>{a}</b></td><td>{what}</td><td>{num(s.get(a))}</td></tr>')
    H.append(f'<tr><td><b>stacked</b></td><td>arm A’s answer and arm C’s, concatenated, '
             f'nothing added</td><td>{num(s.get("stacked"))}</td></tr>')
    H.append('</table>')
    H.append(f'<p class="sub">B&minus;A {num(u["B_minus_A"])} &middot; B&minus;C '
             f'{num(u["B_minus_C"])} &middot; <b>B&minus;stacked {num(u["B_minus_stacked"])}</b>'
             f' &middot; limits B {num(s.get("limit_B"))} vs C {num(s.get("limit_C"))}'
             f' &middot; contradictions in B {s.get("contradictions")}</p>')
    return '\n'.join(H)


def unit_block(it, u, d, S, store, seen):
    is_seed = u['is_seed']
    cls = 'pass' if u['passed'] else 'fail'
    H = [f'<div class="unit {cls}" id="u_{E(it)}">',
         f'<div class="uhead">{vd("seed" if is_seed else "link", "b-seed" if is_seed else "b-link")}'
         f'{vd("passes all six" if u["passed"] else "fails " + str(u["first_failed"]), "b-pass" if u["passed"] else "b-fail")}'
         + (vd('additive, not relational', 'b-add') if u['additive_not_relational'] else '')
         + f'<code>{E(it)}</code></div>',
         '<div class="link">']

    if is_seed:
        x = d['V25'][it]
        for lab, k in (('A', 'observation_a'), ('B', 'observation_b')):
            o = x[k]
            H.append(f'<div class="obs"><b>observation {lab}</b> <code>{E(o["node"])}</code>'
                     f' &middot; <code>{E(str(o.get("technique")))}</code><br>{E(o["text"])}</div>')
        H.append(V10.pans_html(store, [p['panel_id'] for p in x['panels']], seen))
        H.append(f'<p class="qn">{E(x["question"])}</p>')
        H.append('<p class="sub"><b>the key this seed was written with</b></p>')
        H.append(f'<div class="cl">{E(x["key"]["proposition"])}</div>')
        for t in (x['key'].get('limits') or []):
            H.append(f'<div class="cl lim">{E(str(t))}</div>')
    else:
        r = d['REC'][it]; k = d['KEY'].get(it) or {}
        H.append(f'<div class="inp"><b>the earlier result handed in</b><br>{E(r["input_result"])}</div>')
        for t in (r.get('input_limits') or []):
            H.append(f'<div class="cl lim">{E(str(t))}</div>')
        o = r['new_observation']
        H.append(f'<div class="obs"><b>new measurement</b> <code>{E(o["node"])}</code>'
                 f' &middot; <code>{E(str(o.get("technique")))}</code><br>{E(o["text"])}</div>')
        H.append(V10.pans_html(store, [p['panel_id'] for p in (r.get('panels') or [])], seen))
        H.append(f'<p class="qn">{E(r.get("question") or "")}</p>')
        H.append('<p class="sub"><b>the key this link was written with</b></p>')
        H.append(f'<div class="cl">{E(k.get("proposition") or "")}</div>')
        for t in (k.get('limits') or []):
            H.append(f'<div class="cl lim">{E(str(t))}</div>')

    H.append('<h4>what each arm received</h4>')
    H.append(received(it, d))
    H.append('<h4>scores</h4>')
    H.append(score_table(u))
    H.append('<h4>the six gates</h4>')
    H.append(gate_table(u))

    H.append('<h4>can the evidence carry the combined claims?</h4>')
    if u['validity']:
        H.append('<table><tr><th>#</th><th>combined claim</th><th>ruling</th>'
                 '<th>what the evidence cannot show</th></tr>')
        for v in u['validity']:
            ex = ' <i>(excused: the key already states this limit)</i>' if v.get('excused') else ''
            H.append(f'<tr><td>{v["n"]}</td><td>{E(v["claim"])}</td>'
                     f'<td>{vd(v["verdict"])}{ex}</td><td>{E(v["cannot_show"])}'
                     + (f'<br><i>&ldquo;{E(v["quote"])}&rdquo;</i>' if v['quote'] else '')
                     + '</td></tr>')
        H.append('</table>')
    else:
        H.append('<p class="sub">No combined claims survived the split, so there was nothing '
                 'for the validity judge to rule on.</p>')

    H.append('<h4>the claims this unit was graded against</h4>')
    H.append('<table><tr><th>#</th><th>kind</th><th>claim</th></tr>')
    for i, c in enumerate(u['claims'], 1):
        H.append(f'<tr><td>{i}</td><td>{E(c["kind"])}</td><td>{E(c["claim"])}</td></tr>')
    H.append('</table>')

    H.append('<details><summary>every arm answer, verbatim</summary>')
    for arm in ('A', 'B', 'C', 'N'):
        a = P.arm_answer(it, arm, d)
        H.append(f'<p class="sub"><b>arm {arm}</b></p>')
        H.append(f'<div class="arm">{E(a) if a else "(no answer on file)"}</div>')
    sp = os.path.join(P.CALLS, f'{it}__stackedanswer.txt')
    if os.path.exists(sp):
        H.append('<p class="sub"><b>the stacked baseline, exactly as graded</b></p>')
        H.append(f'<div class="arm">{E(open(sp).read())}</div>')
    H.append('</details>')
    H.append('</div></div>')
    return '\n'.join(H)


RUBRIC = """The grader is shown one answer and a fixed, numbered list of claims. It rules each claim
"stated", "contradicted" or "absent", and must quote the answer's own words for every "stated"
and every "contradicted". A "stated" with no quote is counted "absent": a claim that cannot be
pointed to in the text is not stated, however plausible it is that the answerer believed it.
Hedging earns nothing -- "cannot be determined" is not a statement of the claim. The grader is
not told which arm produced the answer, and never sees another arm's answer.

  combined score  the fraction of COMBINED claims ruled stated
  limit score     the fraction of LIMIT claims ruled stated
  contradictions  the count of claims ruled contradicted"""


def build():
    d = P.load()
    D = json.load(open(os.path.join(OUT, 'decide.json')))
    S = json.load(open(os.path.join(OUT, 'seed_claims.json')))
    LG = json.load(open(os.path.join(OUT, 'ledger.json')))
    s1 = json.load(open(os.path.join(OUT, 'step1.json')))
    st = json.load(open(R('results/v3', P.PAPER, 'stitch.json')))
    g = json.load(open(R(st['graph'])))
    store = V10.store_for(st['graph'])
    V10.img_reset(); V10.RESIZED.clear(); V10.MISSPAN.clear()
    seen = set()
    U, CH, FAM = D['units'], D['chains'], D['families']

    H = ['<!doctype html><html lang="en"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{E((g.get("title") or P.PAPER)[:80])}</title>',
         f'<style>{V10.RCSS}{CSS_EXTRA}</style></head><body><div class="wrap">',
         f'<h1>{E(g.get("title") or P.PAPER)}</h1>',
         f'<p class="sub"><code>{E(g.get("paper_id") or P.PAPER)}</code> &middot; '
         f'v2.11 stricter acceptance, one paper &middot; {len(g["nodes"])} nodes, '
         f'{len(g["edges"])} edges</p>',
         '<div class="banner">Every chain on this page must now clear six gates at <i>every</i> '
         'step, including the seed it grows from, which v2.10 never tested. '
         '<b>Every verdict is model against model.</b> No step of this was reviewed by a person.'
         '</div>',
         '<div class="card"><p class="sub"><b>model</b></p>'
         f'<p><code>{E(MODEL)}</code> &middot; 1 sample per arm, with the v2.9 borderline rule '
         f'(a margin in [0.10, 0.40] buys one more sample of A, B and C).</p>'
         '<p class="sub"><b>the grading rubric, as the grader sees it</b></p>'
         f'<div class="rub">{E(RUBRIC)}</div></div>']

    # ---- step 1
    f1 = s1['finding']
    H += ['<h2>What each arm actually received</h2>',
          f'<p>Read out of the prompt files that were sent, not the generator that wrote them. '
          f'Across all {f1["links"]} links on this paper: '
          f'<b>{E(f1["verdict"])}</b>.</p>',
          '<p class="sub">Every panel reached the arms as a crop with its printed caption. '
          '<b>No arm was ever shown a whole figure.</b> Arm C held the earlier result and its '
          'qualifications but no image at all; arm A held the measurement and its crops but no '
          'earlier result.</p>']

    # ---- the graph
    H += ['<h2>The paper’s argument</h2>',
          '<div class="card scroll">' + V10.graph_sel(g) + '</div>']

    # ---- headline
    acc = [c for c in CH if CH[c]['gates_passed'] and not LG.get(c, {}).get('ledger_rejects')]
    rej = [c for c in CH if c not in acc]
    famacc = [f for f, v in FAM.items()
              if any(c in acc for c in v['chains'])]
    H += ['<h2>What survives</h2>',
          f'<p>v2.10 accepted all <b>{len(CH)}</b> of these chains. Under the v2.11 rule '
          f'<b>{len(acc)}</b> survive, across <b>{len(famacc)}</b> of <b>{len(FAM)}</b> '
          f'families.</p>',
          '<div class="scroll"><table><tr><th>chain</th><th>family</th><th>depth</th>'
          '<th>v2.10</th><th>v2.11</th><th>first gate that failed</th></tr>']
    fam_of = {c: f for f, v in FAM.items() for c in v['chains']}
    for cid in sorted(CH):
        c = CH[cid]
        led = LG.get(cid, {})
        ok = cid in acc
        why = ''
        if not c['gates_passed']:
            why = (f'{c["first_failed_gate"]} on '
                   f'<code>{E(str(c["first_failing_unit"]))}</code>')
        elif led.get('ledger_rejects'):
            why = f'caveat ledger: {led["bad"]} earlier limit(s) ignored or contradicted'
        H.append(f'<tr><td><a href="#{cid}"><b>{cid}</b></a></td><td>{fam_of.get(cid,"")}</td>'
                 f'<td>{c["depth"]}</td><td>accepted</td>'
                 f'<td>{vd("accepted" if ok else "rejected", "b-pass" if ok else "b-fail")}</td>'
                 f'<td>{why}</td></tr>')
    H.append('</table></div>')

    # ---- stacked baseline
    H += ['<h2>Does the answer relate the evidence, or only list it?</h2>',
          '<p>Arm B holds everything arm A and arm C hold, so B beating each of them separately '
          'is a low bar — stapling the two answers together clears it. The stacked baseline '
          'is that staple: arm A’s answer and arm C’s, concatenated with nothing added, '
          'graded against the same claims by the same grader.</p>',
          '<div class="scroll"><table><tr><th>unit</th><th>kind</th><th>A</th><th>C</th>'
          '<th>stacked</th><th>B</th><th>B&minus;stacked</th></tr>']
    for r in D['stacked_table']:
        u = U[r['unit']]
        bs = u['B_minus_stacked']
        H.append(f'<tr><td><code>{E(r["unit"])}</code></td>'
                 f'<td>{"seed" if r["seed"] else "link"}</td><td>{num(r["A"])}</td>'
                 f'<td>{num(r["C"])}</td><td>{num(r["stacked"])}</td><td>{num(r["B"])}</td>'
                 f'<td class="{"ok" if (bs is not None and bs >= P.MARGIN) else "no"}">'
                 f'{num(bs)}</td></tr>')
    H.append('</table></div>')

    # ---- families
    H.append('<h2>The chains, by family</h2>')
    order = sorted(FAM, key=lambda f: (not any(c in acc for c in FAM[f]['chains']), f))
    for f in order:
        v = FAM[f]
        any_acc = any(c in acc for c in v['chains'])
        H.append(f'<section class="fam {"" if any_acc else "none"}">')
        H.append(f'<div class="famhead"><b>{f}</b> &middot; {len(v["chains"])} chain(s): '
                 + ', '.join(f'<a href="#{c}">{c}</a>' for c in v['chains'])
                 + f' &middot; share the seed <code>{E(v["seed"])}</code>'
                 + (f' and {len(v["shared_links"])} link(s)' if v['shared_links'] else '')
                 + f' &middot; {len([c for c in v["chains"] if c in acc])} accepted</div>')
        for cid in sorted(v['chains'], key=lambda c: (c not in acc, c)):
            c = CH[cid]; led = LG.get(cid, {})
            ok = cid in acc
            H.append(f'<div class="chain" id="{cid}">')
            H.append(f'<div class="chead"><b>{cid}</b> '
                     f'{vd("accepted" if ok else "rejected", "b-pass" if ok else "b-fail")}'
                     f'<span class="sub">depth {c["depth"]} &middot; {len(c["units"])} units'
                     + (f' &middot; first failure: {c["first_failed_gate"]} on '
                        f'<code>{E(str(c["first_failing_unit"]))}</code>'
                        if c['first_failing_unit'] else '')
                     + '</span></div>')
            for uid in c['units']:
                H.append(unit_block(uid, U[uid], d, S, store, seen))
            if led.get('rows'):
                cnt = led['counts']
                H.append('<div class="gen"><h4>the caveat ledger across the whole chain</h4>')
                H.append('<p class="sub">' + ' &middot; '.join(f'{n} {k}' for k, n in sorted(cnt.items()))
                         + '</p>')
                H.append('<div class="scroll"><table><tr><th>#</th><th>from</th>'
                         '<th>qualification</th><th>ruling</th><th>on these words</th></tr>')
                for x in led['rows']:
                    H.append(f'<tr><td>{x["n"]}</td><td>{E(x["where"])}</td><td>{E(x["limit"])}</td>'
                             f'<td>{vd(x["verdict"], "v-supported" if x["verdict"] == "respects" else ("v-overreaches" if x["verdict"] == "ignores" else "v-unsupported"))}</td>'
                             f'<td>{E(x["quote"])}'
                             + (f'<br><i>{E(x["why"])}</i>' if x['why'] else '') + '</td></tr>')
                H.append('</table></div></div>')
            H.append('</div>')
        H.append('</section>')

    H.append('<div id="zv"><span class="x">&times;</span><img alt="full size"></div>')
    H.append('</div><script>'
             + (V10.JS % (json.dumps(V10.IMG),
                          json.dumps({cid: V10.chain_nodes(
                              {'steps': CH[cid]['steps']}, d) for cid in CH})))
             + '</script></body></html>')
    open(PAGE, 'w').write('\n'.join(H))
    mb = os.path.getsize(PAGE) / 1e6
    rep = {'page': os.path.relpath(PAGE, ROOT), 'mb': round(mb, 2),
           'panels_shown': len(seen), 'images_resized': len(V10.RESIZED),
           'panel_misses': V10.MISSPAN,
           'chains_accepted': sorted(acc), 'chains_rejected': sorted(rej),
           'families_with_an_accepted_chain': sorted(famacc), 'families': len(FAM)}
    json.dump(rep, open(os.path.join(OUT, 'report_build.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in rep.items() if k != 'panel_misses'}, indent=1))
    if V10.MISSPAN: print('panel misses:', V10.MISSPAN)


if __name__ == '__main__':
    build()
