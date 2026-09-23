"""export_items.py: standalone dataset export of the v07 gate items.

  python3 trace_kit/export_items.py [--include text_sufficient,inspect] [--out export]

Reads results/v07/papers/<P>/ (gate.jsonl, written.json, validation.json, gate/<T>.*), the graph, the spec and
the packet, and writes export/v07_items/<paper>/<TRACE>/ with question.pdf, answer.pdf, images/ and item.json.
Nothing under results/v07/papers/ is written. Every verdict in the export is model against model.
"""
import csv, datetime, json, os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
from cut_traces import store_for, panel_record, unmath
from PIL import Image as PILImage
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")

PAPERS = os.path.join(ROOT, 'results', 'v07', 'papers')
V06C = os.path.join(ROOT, 'results', 'v06c')
GRAPHS = os.path.join(ROOT, 'taxonomy', 'graphs_v07')
SPECS = os.path.join(ROOT, 'taxonomy', 'specs_v07')
PACKET_DIRS = [os.path.join(ROOT, 'taxonomy', 'v07', 'partB', 'packets'),
               os.path.join(ROOT, 'taxonomy', 'v07', 'partC', 'packets'),
               os.path.join(ROOT, 'taxonomy', 'v06b_pilot', 'packets'),
               os.path.join(ROOT, 'taxonomy', 'v06_pilot', 'packets')]
NOTE = "Every verdict is model against model."
ROOTS = {'valid': 'v07_items', 'text-sufficient': 'v07_text_sufficient', 'inspect': 'v07_inspect'}

INK = colors.HexColor("#1f2933"); MUTED = colors.HexColor("#5f6b7a"); RULE = colors.HexColor("#c9d1d9")
QBG = colors.HexColor("#e8f0f7"); ABG = colors.HexColor("#e7f3ec"); HBG = colors.HexColor("#fbeae8"); GBG = colors.HexColor("#f2f2ef")
ss = getSampleStyleSheet()
base = ParagraphStyle("b", parent=ss["Normal"], fontName="DV", fontSize=9.6, leading=13.4, textColor=INK)
small = ParagraphStyle("s", parent=base, fontSize=8.6, leading=11.8)
tiny = ParagraphStyle("t", parent=base, fontSize=7.8, leading=10.4, textColor=MUTED)
h1 = ParagraphStyle("h1", parent=base, fontName="DVB", fontSize=14.5, leading=18.5, spaceAfter=2)
h2 = ParagraphStyle("h2", parent=base, fontName="DVB", fontSize=10.6, leading=14, spaceBefore=11, spaceAfter=4)
lbl = ParagraphStyle("lbl", parent=tiny, fontName="DVB", textColor=MUTED, spaceAfter=2)
esc = lambda s: str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
P = lambda t, s=base: Paragraph(t, s)


def box(label, text, bg, accent, style=base):
    t = Table([[P(label, lbl)], [P(text, style)]], colWidths=[7.0 * inch])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 9),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LINEBEFORE", (0, 0), (0, -1), 3, accent)]))
    return t


def rows_table(rows, widths=None):
    t = Table(rows, colWidths=widths or [7.0 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.3, RULE),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    return t


# ---------------------------------------------------------------- packet metadata
_PACKETS = {}

def packet_meta(paper):
    """panel id -> {tier, letter, ocr_letter, ocr_agrees, span} parsed from the paper's packet"""
    if paper in _PACKETS: return _PACKETS[paper]
    path = next((os.path.join(d, paper + '.md') for d in PACKET_DIRS if os.path.exists(os.path.join(d, paper + '.md'))), None)
    out = {}
    if path:
        tier, cur = None, None
        for line in open(path):
            m = re.match(r'Figure .* \((F\d+)\), tier (\S+)', line.strip())
            if m: tier = m.group(2); continue
            m = re.match(r'\s+(\S+#F\d+[a-z]?)\s+crop\s', line)
            if m:
                cur = m.group(1); out[cur] = {'tier': tier, 'letter': cur.split('#')[1][re.match(r'F\d+', cur.split('#')[1]).end():],
                                              'ocr_letter': None, 'ocr_agrees': None, 'span': None}
                continue
            if cur is None: continue
            m = re.match(r'\s+caption span: "(.*)"\s*$', line)
            if m: out[cur]['span'] = m.group(1); continue
            m = re.match(r'\s+ocr letter: (\S+) \((\w+)\)', line)
            if m:
                out[cur]['ocr_letter'] = None if m.group(1) == 'None' else m.group(1)
                out[cur]['ocr_agrees'] = {'agrees': True, 'disagrees': False}.get(m.group(2))
    _PACKETS[paper] = out
    return out


# ---------------------------------------------------------------- gate prompt parsing
def split_fullarm(text):
    """the gate full-arm prompt, verbatim, split into its sections"""
    ctx, _, rest = text.partition("\n\nPanels:\n")
    panels, _, rest = rest.partition("\n\nQuestion: ")
    qblock, _, tail = rest.partition("\n\nImages (read each with Read):\n")
    tail_lines = tail.split("\n")
    limit = tail_lines[-1] if tail_lines else ""
    ctx_lines = [l[2:] for l in ctx.split("\n")[1:] if l.startswith("- ")]
    panel_lines = {}
    for l in panels.split("\n"):
        m = re.match(r'- (\S+?): (.*)$', l)
        if m: panel_lines[m.group(1)] = m.group(2)
    return ctx_lines, panel_lines, qblock.strip(), limit.strip()


def read(p):
    return open(p).read().strip() if os.path.exists(p) else None


# ---------------------------------------------------------------- image export
def to_png(src, dst):
    im = PILImage.open(src)
    if im.mode not in ("RGB", "RGBA", "L", "P"): im = im.convert("RGB")
    im.save(dst, "PNG")
    return im.size


def fit(path, maxw=2.25 * inch, maxh=2.1 * inch):
    w, h = PILImage.open(path).size
    iw, ih = maxw, maxw * h / w
    if ih > maxh: ih = maxh; iw = ih * w / h
    return RLImage(path, width=iw, height=ih)


def panel_grid(items, per_row=3):
    """items: (png_path or None, caption html)"""
    cells = []
    for png, cap in items:
        cells.append([fit(png), P(cap, tiny)] if png else P(cap, tiny))
    rows = [cells[i:i + per_row] for i in range(0, len(cells), per_row)]
    for r in rows:
        while len(r) < per_row: r.append("")
    t = Table([[(c if not isinstance(c, list) else Table([[c[0]], [c[1]]], colWidths=[2.3 * inch])) for c in r] for r in rows],
              colWidths=[7.0 * inch / per_row] * per_row)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 2), ("RIGHTPADDING", (0, 0), (-1, -1), 2)]))
    return t


# ---------------------------------------------------------------- PDFs
def footer_for(tid, paper, qonly):
    def footer(c, d):
        c.saveState(); c.setFont("DV", 7); c.setFillColor(MUTED)
        c.drawString(0.75 * inch, 0.5 * inch, f"causalmat v07 - item {tid} - {paper[:58]}" + (" - question only" if qonly else ""))
        c.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, f"page {d.page}")
        c.restoreState()
    return footer


def header(it, answered):
    bits = [it['journal'].replace('_', ' '), it['doi'], f"item {it['trace']}"]
    if it.get('year'): bits.insert(1, str(it['year']))
    line = " &middot; ".join(esc(b) for b in bits)
    if answered:
        line += f" &middot; <b>{esc(it['root'])}, {esc(it['subtype'])}</b> &middot; verdict {esc(it['verdict']).upper()}" \
                + (" (partial)" if it.get('partial') else "") + f" &middot; depth {it.get('depth')}"
    return [P(esc(it['title']), h1), P(line, tiny), Spacer(1, 8)]


def build_question_pdf(it, out, ctx_lines, obs_lines, panel_lines, qblock, limit, given_png):
    story = header(it, False)
    story.append(box("QUESTION", esc(qblock.split("\n")[0]), QBG, colors.HexColor("#1f6e9e")))
    if ctx_lines:
        story.append(P("Context you are given", h2))
        story.append(rows_table([[P(esc(l), small)] for l in ctx_lines]))
    if obs_lines:
        story.append(P("Observations already stated for you", h2))
        story.append(rows_table([[P(esc(l), small)] for l in obs_lines]))
    story.append(P("Data: the panels you open", h2))
    if given_png:
        items = []
        for suf, png, meta in given_png:
            cap = f"<b>{esc(suf)}</b> &middot; tier {esc(meta.get('tier') or '?')}"
            if meta.get('ocr_letter') is not None:
                cap += f" &middot; ocr {esc(meta['ocr_letter'])}" + (" ok" if meta.get('ocr_agrees') else (" (disagrees)" if meta.get('ocr_agrees') is False else ""))
            cap += "<br/>" + esc(panel_lines.get(suf, ""))
            items.append((png, cap))
        story.append(panel_grid(items))
    else:
        story.append(P("No panels are handed over for this item.", small))
    story.append(Spacer(1, 6))
    fmt = "\n".join(qblock.split("\n")[1:]).strip()
    story.append(box("ANSWER FORMAT", esc((fmt + "\n" + limit).strip()).replace("\n", "<br/>"), GBG, colors.HexColor("#8a8f98"), small))
    story.append(Spacer(1, 6))
    story.append(P("This sheet contains no answer. It is what the answering model receives. " + NOTE, tiny))
    SimpleDocTemplate(out, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch, topMargin=0.7 * inch,
                      bottomMargin=0.75 * inch, title=f"{it['trace']} - {it['title']}").build(
        story, onFirstPage=footer_for(it['trace'], it['paper'], True), onLaterPages=footer_for(it['trace'], it['paper'], True))


def build_answer_pdf(it, out, qblock, t, val, gate, arms, withheld_png):
    story = header(it, True)
    story.append(box("QUESTION THE MODEL GETS", esc(qblock.split("\n")[0]), QBG, colors.HexColor("#1f6e9e")))
    story.append(Spacer(1, 4))
    story.append(P("Reasoning: the single-direction walk (shaded steps are what the model must produce)", h2))
    rrows = []
    for s in t.get('linear') or []:
        tag = ' &middot; <font color="#b9312c"><b>MODEL MUST PRODUCE</b></font>' if s['hidden'] else ''
        dep = (' &middot; needs ' + ', '.join(map(str, s['depends_on']))) if s.get('depends_on') else ''
        rrows.append([P(f"<b>{s['step']}</b>", small),
                      P(f"<b>{esc(s['role'])}</b>{tag} <font color='#5f6b7a'>{esc(', '.join(s['nodes']))}{dep}</font><br/>{esc(s['text'])}", small)])
    if rrows:
        rt = Table(rrows, colWidths=[0.35 * inch, 6.65 * inch])
        st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.3, RULE),
              ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
        for i, s in enumerate(t['linear']):
            if s['hidden']: st.append(("BACKGROUND", (0, i), (-1, i), HBG))
        rt.setStyle(TableStyle(st)); story.append(rt)
    story.append(Spacer(1, 8))
    key = esc(it['answer_key'])
    if it.get('answer_key_nodes'):
        key += f"<br/><font color='#5f6b7a'>source nodes: {esc(', '.join(it['answer_key_nodes']))}</font>"
    story.append(box("ANSWER KEY", key, ABG, colors.HexColor("#2f8f5b")))
    story.append(Spacer(1, 5))
    fl = t.get('floor') or {}
    gr = esc(it['grading']) + f"<br/><font color='#5f6b7a'>answer scope: {esc(it.get('answer_scope'))}"
    gr += f" &middot; floor with the FM evidence removed: {'reaches the claim' if fl.get('reaches') else 'does not reach the claim'}"
    gr += f" &middot; leave-one-out depth {it.get('depth')} ({esc(', '.join(it.get('depth_families') or []))})"
    gr += f" &middot; channels {esc(', '.join(t.get('channels_involved') or []))}</font>"
    story.append(box("HOW IT IS GRADED", gr, GBG, colors.HexColor("#8a8f98"), small))
    story.append(P("Structural nets", h2))
    nrows = [[P(f"<b>{esc(k)}</b>", small), P("pass" if v.get('pass') else "FAIL", small),
              P(esc(v.get('why') or v.get('rule') or ''), tiny)] for k, v in (val.get('nets') or {}).items()]
    if nrows: story.append(rows_table(nrows, [1.4 * inch, 0.7 * inch, 4.9 * inch]))
    ws = val.get('warnings') or []
    story.append(P("Warnings: " + (esc(json.dumps(ws)) if ws else "none"), tiny))
    story.append(P("The gate: model against model", h2))
    grows = []
    for name, lab in (("fullarm", "Image arm (sees the panels)"), ("floor", "Text-only arm (no images)")):
        grows.append([P(f"<b>{lab}</b><br/><font color='#5f6b7a'>graded {esc(it['gate'][name + '_grade'])}</font>", small),
                      P(esc(arms.get(name) or "(no reply on file)"), small)])
        g = arms.get(name + "_grader")
        if g: grows.append([P("<font color='#5f6b7a'>grader</font>", tiny), P(esc(g), tiny)])
    story.append(rows_table(grows, [1.6 * inch, 5.4 * inch]))
    story.append(P(f"Gate verdict: <b>{esc(it['verdict'])}</b>" + (" (partial)" if it.get('partial') else "")
                   + (f" &middot; cause {esc(it['gate'].get('cause'))}" if it['gate'].get('cause') else ""), small))
    if withheld_png:
        story.append(P("Withheld from the answering model", h2))
        story.append(P("These panels are held back: they are the grading channel, or a condition the item stops before.", tiny))
        story.append(panel_grid([(png, f"<b>{esc(suf)}</b> &middot; withheld") for suf, png, _ in withheld_png]))
    story.append(Spacer(1, 8))
    story.append(P("Provenance. Every sentence in the context, the reasoning steps and the answer key is a node label from "
                   "the paper's argument graph, written by a model and reviewed by a second model. " + NOTE
                   + " No human has checked this item.", tiny))
    SimpleDocTemplate(out, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch, topMargin=0.7 * inch,
                      bottomMargin=0.75 * inch, title=f"{it['trace']} answer - {it['title']}").build(
        story, onFirstPage=footer_for(it['trace'], it['paper'], False), onLaterPages=footer_for(it['trace'], it['paper'], False))


# ---------------------------------------------------------------- the export
FIELDS = ['paper', 'doi', 'journal', 'year', 'trace', 'root', 'subtype', 'depth', 'depth_families', 'fm_family',
          'question', 'asks_for', 'answer_key', 'answer_key_nodes', 'answer_scope', 'grading', 'floor_result',
          'panel_ids_given', 'panel_ids_withheld', 'images', 'gate', 'nets', 'warnings', 'graph_file', 'spec_file',
          'pipeline_version', 'export_date', 'title', 'verdict', 'partial', 'note']


def years():
    p = os.path.join(ROOT, 'results', 'v07', 'batch.csv')
    if not os.path.exists(p): return {}
    return {r['paper']: (int(r['year']) if (r.get('year') or '').strip().isdigit() else None) for r in csv.DictReader(open(p))}


def grader_channel_nodes(t):
    """evidence nodes the grading text says are held back from the answering model"""
    txt = (t.get('grader') or '') + ' ' + (t.get('grading') or '')
    if not re.search(r'held out|held-out|independent channel|withheld', txt, re.I): return set()
    return {n for n in re.findall(r'\b[a-z]\d+\b', txt) if n in set(t.get('evidence') or []) | set(t.get('hidden') or [])}


_PILOT = None

def pilot_gate(paper):
    """the v07 pilot gate rows (results/v07/pilot/gate.jsonl) — the same source batch.csv counts"""
    global _PILOT
    if _PILOT is None:
        f = os.path.join(ROOT, 'results', 'v07', 'pilot', 'gate.jsonl')
        _PILOT = {}
        if os.path.exists(f):
            for l in open(f):
                if l.strip():
                    r = json.loads(l); _PILOT.setdefault(r['paper'], []).append(r)
    return _PILOT.get(paper, [])


def export_paper(paper, want, out_roots, YEARS, log):
    d = os.path.join(PAPERS, paper)
    gj = os.path.join(d, 'gate.jsonl')
    if os.path.exists(gj):
        rows = [json.loads(l) for l in open(gj) if l.strip()]
    else:
        rows = pilot_gate(paper)
        pd = os.path.join(V06C, 'writer', paper)
        if rows and os.path.exists(os.path.join(pd, 'written.json')): d = pd
        elif rows: log.append(f"{paper}: v06c gate rows but no v06c written.json, skipped"); return []
    rows = [r for r in rows if r['verdict'] in want]
    if not rows: return []
    gdir = os.path.join(d, 'gate') if os.path.exists(os.path.join(d, 'gate')) else os.path.join(V06C, 'gate', paper)
    wp = os.path.join(d, 'written_pass2.json')
    if not os.path.exists(wp): wp = os.path.join(d, 'written.json')
    vp = os.path.join(d, 'validation_pass2.json')
    if not os.path.exists(vp): vp = os.path.join(d, 'validation.json')
    W = {t['id']: t for t in json.load(open(wp))['traces']}
    VAL = {v['id']: v for v in json.load(open(vp))} if os.path.exists(vp) else {}
    gpath = os.path.join(GRAPHS, paper + '.json')
    if not os.path.exists(gpath):   # pilot papers were graphed under v06b
        gpath = next((os.path.join(ROOT, 'taxonomy', v, paper + '.json') for v in ('graphs_v06b', 'graphs_v06')
                      if os.path.exists(os.path.join(ROOT, 'taxonomy', v, paper + '.json'))), gpath)
    graph = json.load(open(gpath)); N = {n['id']: n for n in graph['nodes']}
    spec = json.load(open(os.path.join(SPECS, paper + '.json'))) if os.path.exists(os.path.join(SPECS, paper + '.json')) else {}
    st = store_for(gpath); meta = packet_meta(paper)
    made = []
    for r in rows:
        tid = r['trace']; t = W.get(tid)
        gate_file = os.path.join(gdir, tid + '.gate.json')
        if t is None or not os.path.exists(gate_file):
            log.append(f"{paper} {tid}: no written trace or gate packet, skipped"); continue
        gate = json.load(open(gate_file))
        ctx_lines, panel_lines, qblock, limit = split_fullarm(gate['fullarm'])
        hid = set(t.get('hidden') or [])
        obs_ids = [s['node'] for s in t['walk'] if s.get('role') == 'evidence' and s['node'] not in hid]
        obs_lines = [N[i]['label'] for i in obs_ids if i in N]
        ctx_only = [l for l in ctx_lines if l not in obs_lines]
        given = list(dict.fromkeys(t.get('given_panels') or []))
        gnodes = grader_channel_nodes(t)
        withheld = list(dict.fromkeys(list(t.get('hidden_panels') or [])
                                      + [p for n in gnodes for p in (N.get(n, {}).get('panel_ids') or [])]))
        withheld = [p for p in withheld if p not in given]
        doi = given[0].split('#')[0] if given else (withheld[0].split('#')[0] if withheld else paper.split('__', 1)[-1].replace('_', '/', 1))

        root_dir = os.path.join(out_roots[r['verdict']], paper, tid)
        img_dir = os.path.join(root_dir, 'images')
        os.makedirs(os.path.join(img_dir, 'withheld'), exist_ok=True)
        os.makedirs(os.path.join(img_dir, 'figures'), exist_ok=True)
        prows, given_png, withheld_png, figs = [], [], [], {}
        arm_imgs = {p: i for p, i in zip(t.get('given_panels') or [], gate.get('images') or [])}
        for pid in given:
            suf = pid.split('#')[1]; rec = panel_record(st, pid) or {}
            src = arm_imgs.get(pid) or rec.get('crop') or rec.get('figure')
            m = meta.get(pid, {})
            if src and os.path.exists(src):
                png = os.path.join(img_dir, suf + '.png'); to_png(src, png)
                given_png.append((suf, png, m))
                prows.append({'file': f"images/{suf}.png", 'panel_id': pid, 'kind': 'given', 'tier': m.get('tier'),
                              'letter': m.get('letter'), 'ocr_agrees': m.get('ocr_agrees'), 'caption_span': m.get('span'), 'reason': ''})
            else:
                prows.append({'file': '', 'panel_id': pid, 'kind': 'given', 'tier': m.get('tier'), 'letter': m.get('letter'),
                              'ocr_agrees': m.get('ocr_agrees'), 'caption_span': m.get('span'),
                              'reason': 'panel id does not resolve to a crop'})
            f = rec.get('figure')
            if f and os.path.exists(f):
                fn = 'fig' + re.match(r'F(\d+)', suf).group(1) + '.png'
                if fn not in figs:
                    fp = os.path.join(img_dir, 'figures', fn); to_png(f, fp); figs[fn] = True
                    prows.append({'file': f"images/figures/{fn}", 'panel_id': pid.split('#')[0] + '#' + re.match(r'F\d+', suf).group(0),
                                  'kind': 'figure', 'tier': m.get('tier'), 'letter': '', 'ocr_agrees': '', 'caption_span': '', 'reason': ''})
        for pid in withheld:
            suf = pid.split('#')[1]; rec = panel_record(st, pid) or {}
            src = rec.get('crop') or rec.get('figure'); m = meta.get(pid, {})
            if src and os.path.exists(src):
                png = os.path.join(img_dir, 'withheld', suf + '.png'); to_png(src, png)
                withheld_png.append((suf, png, m))
                prows.append({'file': f"images/withheld/{suf}.png", 'panel_id': pid, 'kind': 'withheld', 'tier': m.get('tier'),
                              'letter': m.get('letter'), 'ocr_agrees': m.get('ocr_agrees'), 'caption_span': m.get('span'), 'reason': ''})
            else:
                prows.append({'file': '', 'panel_id': pid, 'kind': 'withheld', 'tier': m.get('tier'), 'letter': m.get('letter'),
                              'ocr_agrees': m.get('ocr_agrees'), 'caption_span': m.get('span'),
                              'reason': 'panel id does not resolve to a crop'})
        with open(os.path.join(root_dir, 'panels.csv'), 'w', newline='') as fh:
            w = csv.DictWriter(fh, ['file', 'panel_id', 'kind', 'tier', 'letter', 'ocr_agrees', 'caption_span', 'reason'])
            w.writeheader(); w.writerows(prows)

        val = VAL.get(tid, {})
        arms = {'fullarm': read(os.path.join(gdir, tid + '.fullarm.out.txt')),
                'floor': read(os.path.join(gdir, tid + '.floor.out.txt')),
                'fullarm_grader': read(os.path.join(gdir, tid + '.grader.fullarm.out.txt')),
                'floor_grader': read(os.path.join(gdir, tid + '.grader.floor.out.txt'))}
        it = {'paper': paper, 'doi': doi, 'journal': spec.get('journal') or paper.split('__')[0], 'year': YEARS.get(paper),
              'trace': tid, 'root': r['root'], 'subtype': r['subtype'], 'depth': t.get('depth'),
              'depth_families': t.get('depth_families'), 'fm_family': t.get('fm_family'),
              'question': t.get('question'), 'asks_for': t.get('asks_for'), 'answer_key': t.get('answer_key'),
              'answer_key_nodes': t.get('answer_key_nodes'), 'answer_scope': r.get('answer_scope') or t.get('answer_scope'),
              'grading': t.get('grading'), 'floor_result': t.get('floor'),
              'panel_ids_given': given, 'panel_ids_withheld': withheld,
              'images': {'given': [f"images/{s}.png" for s, _, _ in given_png],
                         'withheld': [f"images/withheld/{s}.png" for s, _, _ in withheld_png],
                         'figures': [f"images/figures/{k}" for k in figs]},
              'gate': {'fullarm_grade': r.get('fullarm'), 'floor_grade': r.get('floor'), 'verdict': r['verdict'],
                       'partial': r.get('partial'), 'cause': r.get('cause'),
                       'fullarm_answer': arms['fullarm'], 'floor_answer': arms['floor'],
                       'fullarm_grader': arms['fullarm_grader'], 'floor_grader': arms['floor_grader']},
              'nets': {k: bool(v.get('pass')) for k, v in (val.get('nets') or {}).items()},
              'warnings': val.get('warnings') or [],
              'graph_file': os.path.relpath(gpath, ROOT), 'spec_file': os.path.relpath(os.path.join(SPECS, paper + '.json'), ROOT),
              'pipeline_version': 'v07', 'export_date': datetime.date.today().isoformat(),
              'title': graph.get('title') or spec.get('title') or paper, 'verdict': r['verdict'],
              'partial': bool(r.get('partial')), 'note': NOTE}
        json.dump(it, open(os.path.join(root_dir, 'item.json'), 'w'), indent=1)
        build_question_pdf(it, os.path.join(root_dir, 'question.pdf'), ctx_only, obs_lines, panel_lines, qblock, limit, given_png)
        build_answer_pdf(it, os.path.join(root_dir, 'answer.pdf'), qblock, t, val, gate, arms, withheld_png)
        made.append((it, root_dir, prows))
    return made


README = """# v07 items

These items come from published figures in subscription journals: every PNG in this export is a copy of a figure or
figure panel from the paper named in the item record, reproduced here only so an item can be answered, and the export
is for internal evaluation and is not redistributable. Each item was cut from an argument graph a model built from the
paper, the question and answer key were written by a model, and the gate result was produced by one model answering and
another grading it. Every verdict in it was produced by a model, with no human check.

Every verdict is model against model.
"""


def pdf_text(path):
    """the PDF's text layer, via pdftotext, else pypdf"""
    import shutil, subprocess
    if shutil.which('pdftotext'):
        r = subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True)
        if r.returncode == 0: return r.stdout
    try:
        from pypdf import PdfReader
        return "\n".join((p.extract_text() or '') for p in PdfReader(path).pages)
    except Exception:
        return None


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()


def checks(items, out_root):
    fails, missing_panel, leaks = [], 0, []
    for it, dirp, prows in items:
        for f in ('question.pdf', 'answer.pdf', 'item.json'):
            if not os.path.exists(os.path.join(dirp, f)): fails.append(f"{it['paper']} {it['trace']}: no {f}")
        pngs = glob.glob(os.path.join(dirp, 'images', '*.png'))
        if not pngs and not any(r['reason'] for r in prows if r['kind'] == 'given'):
            fails.append(f"{it['paper']} {it['trace']}: no PNG in images/ and no reason recorded")
        if any(r['reason'] for r in prows): missing_panel += 1
        for p in glob.glob(os.path.join(dirp, 'images', '**', '*.png'), recursive=True):
            try:
                w, h = PILImage.open(p).size
                if w <= 80 or h <= 80: fails.append(f"{it['paper']} {it['trace']}: {os.path.basename(p)} is {w}x{h}")
            except Exception as e:
                fails.append(f"{it['paper']} {it['trace']}: {os.path.basename(p)} will not open ({e})")
        txt = pdf_text(os.path.join(dirp, 'question.pdf'))
        if txt is None:
            leaks.append('no pdf text extractor available'); continue
        n = norm(txt)
        key = norm(it['answer_key'])
        probe = ' '.join(key.split()[:8])
        if probe and probe in n: leaks.append(f"{it['paper']} {it['trace']}: answer-key sentence in question.pdf")
        for nid in (it.get('answer_key_nodes') or []):
            if re.search(r'\b' + re.escape(nid) + r'\b', txt): leaks.append(f"{it['paper']} {it['trace']}: hidden node id {nid} in question.pdf")
    return fails, missing_panel, sorted(set(leaks))


def du(path):
    tot = 0
    for r, _, fs in os.walk(path):
        for f in fs: tot += os.path.getsize(os.path.join(r, f))
    return tot


def main(argv):
    include = set()
    out = os.path.join(ROOT, 'export')
    for i, a in enumerate(argv):
        if a == '--include': include = {x.strip().replace('_', '-') for x in argv[i + 1].split(',')}
        if a == '--out': out = os.path.abspath(argv[i + 1])
    want = {'valid'} | {v for v in include if v in ROOTS}
    out_roots = {v: os.path.join(out, ROOTS[v]) for v in want}
    for p in out_roots.values(): os.makedirs(p, exist_ok=True)
    YEARS = years(); log = []
    by_verdict = {}
    for paper in sorted(os.listdir(PAPERS)):
        if not os.path.isdir(os.path.join(PAPERS, paper)): continue
        try:
            for it, dirp, prows in export_paper(paper, want, out_roots, YEARS, log):
                by_verdict.setdefault(it['verdict'], []).append((it, dirp, prows))
        except Exception as e:
            log.append(f"{paper}: {type(e).__name__}: {e}")
    report = {'export_date': datetime.date.today().isoformat(), 'note': NOTE, 'roots': {}, 'log': log}
    for verdict, items in by_verdict.items():
        root = out_roots[verdict]
        with open(os.path.join(root, 'items.jsonl'), 'w') as fh:
            for it, _, _ in items: fh.write(json.dumps({k: it.get(k) for k in FIELDS}) + "\n")
        with open(os.path.join(root, 'index.csv'), 'w', newline='') as fh:
            w = csv.writer(fh)
            w.writerow(['paper', 'trace', 'root', 'subtype', 'verdict', 'depth', 'n_given_panels', 'n_withheld_panels',
                        'fm_family', 'journal', 'year', 'question_pdf', 'answer_pdf'])
            for it, dirp, _ in items:
                rel = os.path.relpath(dirp, root)
                w.writerow([it['paper'], it['trace'], it['root'], it['subtype'], it['verdict'], it['depth'],
                            len(it['images']['given']), len(it['images']['withheld']), it['fm_family'], it['journal'],
                            it['year'] or '', os.path.join(rel, 'question.pdf'), os.path.join(rel, 'answer.pdf')])
        open(os.path.join(root, 'README.md'), 'w').write(README)
        fails, missing, leaks = checks(items, root)
        folders = sum(len(os.listdir(os.path.join(root, p))) for p in os.listdir(root)
                      if os.path.isdir(os.path.join(root, p)))
        pngs = len(glob.glob(os.path.join(root, '**', '*.png'), recursive=True))
        report['roots'][ROOTS[verdict]] = {
            'items': len(items), 'folders': folders, 'index_rows': len(items),
            'jsonl_lines': sum(1 for _ in open(os.path.join(root, 'items.jsonl'))),
            'pngs': pngs, 'items_missing_a_panel': missing, 'bytes': du(root),
            'counts_agree': folders == len(items) == sum(1 for _ in open(os.path.join(root, 'items.jsonl'))),
            'failed_checks': fails, 'answer_leaks_into_question_pdf': leaks}
    json.dump(report, open(os.path.join(out, 'export_report.json'), 'w'), indent=1)
    print(json.dumps(report, indent=1)[:4000])


if __name__ == '__main__':
    main(sys.argv[1:])
