"""sheets.py: question.pdf and answer.pdf for one support chain.

  python3 trace_kit_v2/sheets.py <case_dir>

The question sheet states the claim in full, copied from the claim node (plan section 7), lists the
steps in the paper's argument order with the data each hands over, and asks for a four-level ruling per
step plus a closing profile. The answer sheet adds every step's expected level, the closing profile,
what is missing, the layer decisions and the necessity labels.
"""
import json, os, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leakguard as LG
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'trace_kit'))
from cut_traces import store_for, fig_preamble, unmath

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
INK = colors.HexColor("#1f2933"); MUTED = colors.HexColor("#5f6b7a"); RULE = colors.HexColor("#c9d1d9")
QBG = colors.HexColor("#e8f0f7"); ABG = colors.HexColor("#e7f3ec"); GBG = colors.HexColor("#f2f2ef")
OBG = colors.HexColor("#fdf3e3"); HBG = colors.HexColor("#fbeae8")
ss = getSampleStyleSheet()
base = ParagraphStyle("b", parent=ss["Normal"], fontName="DV", fontSize=9.6, leading=13.4, textColor=INK)
small = ParagraphStyle("s", parent=base, fontSize=8.6, leading=11.8)
tiny = ParagraphStyle("t", parent=base, fontSize=7.8, leading=10.4, textColor=MUTED)
h1 = ParagraphStyle("h1", parent=base, fontName="DVB", fontSize=14, leading=18, spaceAfter=2)
h2 = ParagraphStyle("h2", parent=base, fontName="DVB", fontSize=10.6, leading=14, spaceBefore=11, spaceAfter=4)
lbl = ParagraphStyle("lbl", parent=tiny, fontName="DVB", textColor=MUTED, spaceAfter=2)
esc = lambda s: str(s if s is not None else '').replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
P = lambda t, s=base: Paragraph(t, s)
SCALE = "shown · partial · not addressed · contradicts"


def box(label, text, bg, accent, style=base):
    t = Table([[P(label, lbl)], [P(text, style)]], colWidths=[7.0 * inch])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 9),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LINEBEFORE", (0, 0), (0, -1), 3, accent)]))
    return t


def rows_table(rows, widths=None):
    t = Table(rows, colWidths=widths or [7.0 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.3, RULE),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t


def fit(path, maxw=2.3 * inch, maxh=2.0 * inch):
    w, h = PILImage.open(path).size
    iw, ih = maxw, maxw * h / w
    if ih > maxh: ih = maxh; iw = ih * w / h
    return RLImage(path, width=iw, height=ih)


def oracle_text(step, answered=False):
    """plan section 4: an ordinary tool result in plain text, the MEASUREMENT from the observation node.
    The interpretation is cut off; on the answer sheet it is shown so a grader can see what was withheld."""
    m = LG.measurement(step['observation'])
    out = f"Tool: {esc(step['technique'])} readout.<br/>{esc(m)}"
    if answered and m != step['observation']:
        out += f"<br/><font color='#5f6b7a'>withheld as interpretation: {esc(step['observation'][len(m):].lstrip(' ,;'))}</font>"
    return out


def footer_for(ch, qonly):
    def f(c, d):
        c.saveState(); c.setFont("DV", 7); c.setFillColor(MUTED)
        c.drawString(0.75 * inch, 0.5 * inch, f"causalmat v2 · {ch['case']} · {ch['paper'][:50]} · claim {ch['claim']}"
                     + (" · question only" if qonly else ""))
        c.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, f"page {d.page}")
        c.restoreState()
    return f


def header(ch, answered):
    line = f"{esc(ch['paper'].split('__')[0].replace('_',' '))} &middot; claim {esc(ch['claim'])} ({esc(ch['claim_type'])}) &middot; {ch['n_steps']} steps &middot; {ch['n_channels']} channels: {esc(', '.join(ch['channels']))}"
    if answered: line += f" &middot; <b>closing {esc(ch['closing_support']).upper()}</b>"
    return [P(f"Support chain &middot; {esc(ch['case'])}", h1), P(line, tiny), Spacer(1, 8)]


def build(case_dir, answered):
    ch = json.load(open(os.path.join(case_dir, 'case.json')))
    st = store_for(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', ch['graph']))
    forbidden = LG.terms(ch['claim_text'], *[x['observation'] for x in ch['steps']])
    story = header(ch, answered)
    story.append(box("THE CLAIM UNDER TEST", esc(ch['claim_text']), QBG, colors.HexColor("#1f6e9e")))
    story.append(Spacer(1, 4))
    story.append(P("What to do", h2))
    story.append(P(f"The evidence below is presented in the paper's own argument order, one step per measurement. "
                   f"For <b>each step</b>, say what that data contributes to the claim on this four-level scale: "
                   f"<b>{SCALE}</b>, and why in one sentence. Then close: give the <b>overall support level</b> for the "
                   f"claim and state <b>what is still missing</b>. Partial rulings are expected; do not force a yes or no.", small))
    for s in ch['steps']:
        story.append(P(f"Step {s['step']} &middot; {esc(s['technique'])} &middot; {esc(s['delivery'])}", h2))
        if s['delivery'] == 'oracle':
            story.append(box("TOOL RESULT (text)", oracle_text(s, answered), OBG, colors.HexColor("#c08a2e"), small))
        else:
            cells = []
            for p in s['panels']:
                if not p.get('png'): continue
                cap = f"<b>{esc(p['suffix'])}</b>"
                if p['layer_decision'] == 'hidden':
                    cap += f" &middot; <font color='#b9312c'>annotation layer hidden, {p['masked_fraction']:.1%} masked</font>"
                pre = ' '.join(unmath(fig_preamble(st, p['panel_id']) or '').split())
                shown_cap = LG.caption_for(p['caption_span'], pre, forbidden)
                if shown_cap: cap += "<br/>" + esc(shown_cap[:150])
                cells.append([fit(os.path.join(case_dir, p['png'])), P(cap, tiny)])
            if cells:
                t = Table([[Table([[c[0]], [c[1]]], colWidths=[2.35 * inch]) for c in cells[i:i + 3]]
                           for i in range(0, len(cells), 3)], colWidths=[7.0 * inch / 3] * min(3, len(cells)))
                t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")])); story.append(t)
        if answered:
            story.append(Spacer(1, 3))
            story.append(box("EXPECTED", f"<b>{esc(s['expected_support']).upper()}</b> &middot; "
                             f"{esc(s['observation'])}<br/><font color='#5f6b7a'>relation {esc(s['relation'])} &middot; "
                             f"operation {esc(s['mm_op'])} &middot; tests {esc(s['tests'])} &middot; lane {esc(s['lane'])}"
                             + (f" &middot; read from {esc(s['read_from'])}" if s['read_from'] else "")
                             + (f"<br/>needs, not on the panel: {esc('; '.join(s['requires_unseen']))}" if s['requires_unseen'] else "")
                             + "</font>", ABG, colors.HexColor("#2f8f5b"), small))
    story.append(Spacer(1, 6))
    if answered:
        story.append(P("Closing profile", h2))
        story.append(box("OVERALL SUPPORT", f"<b>{esc(ch['closing_support']).upper()}</b>", ABG, colors.HexColor("#2f8f5b")))
        story.append(Spacer(1, 4))
        story.append(box("WHAT IS MISSING", "<br/>".join("&bull; " + esc(m) for m in ch['closing_missing']) or "nothing recorded",
                         HBG, colors.HexColor("#b9312c"), small))
        if ch['dropped_panels']:
            story.append(P("Panels dropped from this chain", h2))
            story.append(rows_table([[P(f"<b>{esc(d['node'])}</b>", small), P(esc(d['reason']), small)] for d in ch['dropped_panels']],
                                    [0.8 * inch, 6.2 * inch]))
        story.append(P("Necessity (structural leave-one-out, channel level, no model calls)", h2))
        story.append(rows_table([[P(f"<b>{esc(k)}</b>", small), P(esc(v['structural']), small),
                                  P(esc(v['why']), tiny), P(esc(v['confidence']), tiny)]
                                 for k, v in ch['necessity'].items()], [0.9 * inch, 1.6 * inch, 3.8 * inch, 0.7 * inch]))
        story.append(P("Layer decisions", h2))
        story.append(rows_table([[P(f"<b>{esc(p['suffix'])}</b>", small), P(esc(p['layer_decision']), small), P(esc(p['layer_why']), tiny)]
                                 for s in ch['steps'] for p in s['panels']], [0.7 * inch, 1.0 * inch, 5.3 * inch]))
        story.append(Spacer(1, 8))
        story.append(P("Provenance. Every sentence here is a node label from the paper's argument graph; the four-level "
                       "supports are the graph's own image_support fields. " + ch['note'] + " No human has checked this item.", tiny))
    else:
        story.append(box("ANSWER FORMAT",
                         f"For each step: one of {SCALE}, and one sentence of why.<br/>"
                         "Then: the overall support level for the claim, and what is still missing.<br/>"
                         "If a step's data does not bear on the claim at all, say <b>not addressed</b>. "
                         "If it cuts against the claim, say <b>contradicts</b>.", GBG, colors.HexColor("#8a8f98"), small))
        story.append(Spacer(1, 6))
        story.append(P("This sheet contains no answer. It is what the answering model receives.", tiny))
    out = os.path.join(case_dir, 'answer.pdf' if answered else 'question.pdf')
    SimpleDocTemplate(out, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch, topMargin=0.7 * inch,
                      bottomMargin=0.75 * inch, title=f"{ch['case']} {ch['claim']}").build(
        story, onFirstPage=footer_for(ch, not answered), onLaterPages=footer_for(ch, not answered))
    return out


if __name__ == '__main__':
    d = sys.argv[1]
    for a in (False, True): print(os.path.relpath(build(d, a)))
