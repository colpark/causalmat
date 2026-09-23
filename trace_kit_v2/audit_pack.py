"""audit_pack.py: the human audit pack. One page per step, unfilled.

  python3 trace_kit_v2/audit_pack.py

The brief asks for 30 steps across four contribution values. The five cases carry 21 steps and fewer
than four values, so the pack takes what exists and says so rather than padding.
"""
import csv, json, os, collections
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
ss = getSampleStyleSheet()
base = ParagraphStyle("b", parent=ss["Normal"], fontName="DV", fontSize=10, leading=14)
small = ParagraphStyle("s", parent=base, fontSize=8.8, leading=12)
tiny = ParagraphStyle("t", parent=base, fontSize=7.8, leading=10.6, textColor=colors.HexColor("#5f6b7a"))
h1 = ParagraphStyle("h1", parent=base, fontName="DVB", fontSize=13, leading=17, spaceAfter=3)
lbl = ParagraphStyle("lbl", parent=tiny, fontName="DVB")
esc = lambda s: str(s if s is not None else '').replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
P = lambda t, s=base: Paragraph(t, s)


def field(label, text, bg, style=base):
    t = Table([[P(label, lbl)], [P(text, style)]], colWidths=[6.9 * inch])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 8),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return t


def main():
    out = os.path.join(ROOT, 'results/v2/audit_pack'); os.makedirs(out, exist_ok=True)
    lab = [json.loads(l) for l in open(os.path.join(ROOT, 'results/v2/contrib_labels.jsonl'))]
    img = {}
    for f in os.listdir(os.path.join(ROOT, 'results/v2/cases')):
        pass
    # expected_support_image from each case.json
    import glob
    for f in glob.glob(os.path.join(ROOT, 'results/v2/cases/*/*/case.json')):
        ch = json.load(open(f))
        for s in ch['steps']:
            img[(ch['case'], s['step'])] = s.get('expected_support_image') or s.get('image_support')
    vals = collections.Counter(l['contribution'] for l in lab)
    story, rows = [], []
    story.append(P("Human audit pack: the claim-contribution label", h1))
    story.append(P(f"{len(lab)} steps from the five v2 cases. The brief asks for 30 across four contribution "
                   f"values; these steps carry {len(vals)} values ({', '.join(f'{k} {v}' for k, v in vals.most_common())}), "
                   f"so every step is included and nothing is padded.", small))
    story.append(Spacer(1, 6))
    story.append(P("For each page: does the contribution label describe what the observation settles about the "
                   "claim? Mark AGREE or DISAGREE and give a reason. You are judging the label, not the panel: "
                   "assume the observation is true and was read correctly.", small))
    story.append(Spacer(1, 4))
    story.append(P("Nothing in this pipeline has been checked by a person. This is the step that requires one.", tiny))
    story.append(PageBreak())
    for i, l in enumerate(sorted(lab, key=lambda x: (x['case'], x['step'])), 1):
        iv = img.get((l['case'], l['step']))
        story.append(P(f"{i}. {l['case']} &middot; step {l['step']} &middot; node {l['node']} &middot; {l['technique']}", h1))
        story.append(Spacer(1, 3))
        story.append(field("CLAIM", esc(l['claim_text']), colors.HexColor("#e8f0f7")))
        story.append(Spacer(1, 3))
        story.append(field("OBSERVATION (as the label saw it)", esc(l['observation_as_labelled']), colors.HexColor("#f2f2ef")))
        story.append(Spacer(1, 3))
        story.append(field("RELATION", f"the observation <b>{esc(l['relation'])}</b> the claim", colors.HexColor("#f2f2ef"), small))
        story.append(Spacer(1, 3))
        story.append(field("GRAPH'S image_support", esc(iv), colors.HexColor("#f2f2ef"), small))
        story.append(Spacer(1, 3))
        story.append(field("CONTRIBUTION LABEL", f"<b>{esc(l['contribution'])}</b><br/>{esc(l['why'])}"
                           + (f"<br/><font color='#5f6b7a'>leaves open: {esc('; '.join(l['unsettled']))}</font>" if l['unsettled'] else ""),
                           colors.HexColor("#e7f3ec")))
        story.append(Spacer(1, 10))
        box = Table([[P("AGREE  &#9744;", base), P("DISAGREE  &#9744;", base)],
                     [P("reason:", lbl), ""], [P(" ", base), ""], [P(" ", base), ""], [P(" ", base), ""]],
                    colWidths=[3.45 * inch, 3.45 * inch])
        box.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#5f6b7a")),
                                 ("SPAN", (0, 1), (1, 1)), ("SPAN", (0, 2), (1, 4)),
                                 ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                                 ("LEFTPADDING", (0, 0), (-1, -1), 8)]))
        story.append(box)
        story.append(PageBreak())
        rows.append({'n': i, 'case': l['case'], 'step': l['step'], 'node': l['node'],
                     'technique': l['technique'], 'relation': l['relation'], 'image_support': iv,
                     'contribution': l['contribution'], 'why': l['why'],
                     'unsettled': '; '.join(l['unsettled']),
                     'claim_text': l['claim_text'], 'observation': l['observation_as_labelled'],
                     'agree_disagree': '', 'reason': ''})
    SimpleDocTemplate(os.path.join(out, 'audit_pack.pdf'), pagesize=letter, leftMargin=0.8 * inch,
                      rightMargin=0.8 * inch, topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                      title="causalmat v2 human audit pack").build(story)
    with open(os.path.join(out, 'audit_sheet.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
    json.dump({'steps': len(rows), 'requested': 30, 'values_present': dict(vals),
               'values_requested': 4, 'padded': False,
               'note': 'Fewer than four contribution values are present in the five cases, so the pack takes '
                       'every step that exists rather than padding. Unfilled: no person has audited it.'},
              open(os.path.join(out, 'pack.json'), 'w'), indent=1)
    print(f"audit_pack: {len(rows)} pages (30 requested), values present {dict(vals)}, not padded")


if __name__ == '__main__': main()
