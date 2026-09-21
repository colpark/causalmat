"""build_sheets_v06c.py: question-only and answered PDFs, with the panel images, for every valid item in results/v06c/solving_gate.jsonl
(layout from build_sheets_with_images.py)."""
import json, subprocess, os, re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")); pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.join(HERE,"..")
INK=colors.HexColor("#1f2933"); MUTED=colors.HexColor("#5f6b7a"); RULE=colors.HexColor("#c9d1d9"); QBG=colors.HexColor("#e8f0f7"); ABG=colors.HexColor("#e7f3ec"); HBG=colors.HexColor("#fbeae8"); GBG=colors.HexColor("#f2f2ef")
ss=getSampleStyleSheet(); base=ParagraphStyle("b",parent=ss["Normal"],fontName="DV",fontSize=9.6,leading=13.4,textColor=INK)
small=ParagraphStyle("s",parent=base,fontSize=8.6,leading=11.8); tiny=ParagraphStyle("t",parent=base,fontSize=7.8,leading=10.4,textColor=MUTED)
h1=ParagraphStyle("h1",parent=base,fontName="DVB",fontSize=14.5,leading=18.5,spaceAfter=2); h2=ParagraphStyle("h2",parent=base,fontName="DVB",fontSize=10.6,leading=14,spaceBefore=11,spaceAfter=4)
lbl=ParagraphStyle("lbl",parent=tiny,fontName="DVB",textColor=MUTED,spaceAfter=2)
P=lambda t,s=base: Paragraph(t,s); esc=lambda s: str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def box(label,text,bg,accent,style=base):
    t=Table([[P(label,lbl)],[P(text,style)]],colWidths=[7.0*inch]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),6),("LINEBEFORE",(0,0),(0,-1),3,accent)])); return t
FORMAT={("infer","rank"):"Give the ranking as one ordered list, most to least, naming each sample as it is labelled in the panels. If the panels do not settle the order, write exactly: CANNOT DETERMINE.",
        ("infer","estimate"):"Give the value with its unit and a range you are confident in. If the panels do not settle it, write exactly: CANNOT DETERMINE.",
        ("infer","classify"):"Name the class, and the feature in the panels that decides it. If the panels do not settle it, write exactly: CANNOT DETERMINE.",
        ("explain","competing causes"):"Name the cause you choose, the mechanism by which it acts, and for each alternative the specific reason it fails to account for the observation. If the evidence cannot separate the candidates, say which it cannot separate and why.",
        ("explain","mechanism"):"List the mechanisms you can identify from the panel, and for each the feature that shows it. If the panel does not settle it, write exactly: CANNOT DETERMINE.",
        ("explain","rejection"):"Answer SUPPORTED or NOT SUPPORTED, and name the feature of the figure that decides it.",
        ("intervene","next condition"):"Name the next condition to test, as one value, and state what result you expect from it and why. If the results so far do not point to a next condition, say so."}

def grid(imgs, labels, per_row=3, maxw=2.25*inch):
    cells=[]
    for path,lab in zip(imgs,labels):
        w,h=PILImage.open(path).size; iw=maxw; ih=iw*h/w
        if ih>2.2*inch: ih=2.2*inch; iw=ih*w/h
        cells.append(Table([[RLImage(path,width=iw,height=ih)],[P(esc(lab),tiny)]],colWidths=[maxw]))
    rows=[cells[i:i+per_row] for i in range(0,len(cells),per_row)]
    for r in rows:
        while len(r)<per_row: r.append("")
    t=Table(rows,colWidths=[7.0*inch/per_row]*per_row); t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),2),("RIGHTPADDING",(0,0),(-1,-1),2)])); return t
def build(rec, answered, outdir):
    paper, tid = rec["paper"], rec["trace"]; G=os.path.join(ROOT,"results","v06c","gate",paper)
    pk=json.load(open(f"{G}/{tid}.gate.json")); W=os.path.join(ROOT,"results","v06c","writer",paper)
    wf=f"{W}/written_pass2.json" if os.path.exists(f"{W}/written_pass2.json") else f"{W}/written.json"
    t=next(x for x in json.load(open(wf))["traces"] if x["id"]==tid)
    g=json.load(open(os.path.join(ROOT,"taxonomy","graphs_v06b",paper+".json")))
    text=pk["fullarm"]; ctx=text.split("Context from a materials paper:\n",1)[1].split("\n\nPanels:",1)[0]
    panels=text.split("\n\nPanels:\n",1)[1].split("\n\nQuestion:",1)[0].split("\n")
    story=[P(esc(g["title"]),h1), P(f"{esc(paper.split('__')[0].replace('_',' '))} · {esc(g['paper_id'])} · item {esc(tid)}"+(f" · <b>{esc(t['root'])}, {esc(t['subtype'])}</b> · gate verdict <b>{esc(rec['verdict'].upper())}</b>" if answered else ""),tiny), Spacer(1,8)]
    story.append(box("QUESTION",esc(t["question"])+(f"<br/><font color='#5f6b7a'>{esc(t['answer_format'])}</font>" if t.get("answer_format") else ""),QBG,colors.HexColor("#1f6e9e"))); story.append(Spacer(1,4))
    story.append(P("Context you are given",h2))
    tb=Table([[P(esc(l[2:]),small)] for l in ctx.split("\n") if l.strip()],colWidths=[7.0*inch]); tb.setStyle(TableStyle([("LINEBELOW",(0,0),(-1,-1),0.3,RULE),("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2)])); story.append(tb)
    story.append(P("Panels, with their captions and condition labels",h2))
    story.append(grid(pk["images"], [l[2:] for l in panels][:len(pk["images"])]))
    story.append(Spacer(1,6)); story.append(box("ANSWER FORMAT",(lambda f: esc(f if "CANNOT DETERMINE" in f else f+" If the panels do not settle it, write exactly: CANNOT DETERMINE."))(FORMAT.get((t["root"],t["subtype"]),"Answer in at most six sentences.")),GBG,colors.HexColor("#8a8f98"),small))
    if answered:
        story.append(P("Reasoning walk (shaded steps are what the model must produce)",h2))
        rrows=[[P(f"<b>{s['step']}</b>",small),P(f"<b>{esc(s['role'])}</b>{' · <font color=\"#b9312c\"><b>HIDDEN</b></font>' if s['hidden'] else ''} <font color='#5f6b7a'>{esc(', '.join(s['nodes']))}</font><br/>{esc(s['text'])}",small)] for s in t["linear"]]
        rt=Table(rrows,colWidths=[0.35*inch,6.65*inch]); st=[("VALIGN",(0,0),(-1,-1),"TOP"),("LINEBELOW",(0,0),(-1,-1),0.3,RULE),("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),4)]
        for i,s in enumerate(t["linear"]):
            if s["hidden"]: st.append(("BACKGROUND",(0,i),(-1,i),HBG))
        rt.setStyle(TableStyle(st)); story.append(rt); story.append(Spacer(1,8))
        story.append(box("ANSWER KEY (scope: "+esc(t.get("answer_scope","full"))+")",esc(t["answer_key"])+f"<br/><font color='#5f6b7a'>key nodes: {esc(', '.join(t.get('answer_key_nodes') or []))} · graded targets: {esc(', '.join(t.get('graded_targets') or []))}</font>",ABG,colors.HexColor("#2f8f5b")))
        story.append(Spacer(1,5)); story.append(box("GRADED BY",esc(t["grading"]),GBG,colors.HexColor("#8a8f98"),small))
        story.append(Spacer(1,5)); story.append(box("SOLVING GATE",f"full arm (images): <b>{esc(rec['fullarm'])}</b> · floor (text only): <b>{esc(rec['floor'])}</b> · verdict <b>{esc(rec['verdict'])}</b>"+(" (full arm partial)" if rec.get('partial') else "")+(f"<br/>v1 filter would have ruled: {esc(rec['v1_filter']['status'])}, {esc(rec['v1_filter']['ruling'])}" if rec.get('v1_filter') else ""),GBG,colors.HexColor("#8a8f98"),small))
        story.append(Spacer(1,8)); story.append(P("Provenance. Context, walk and key come from the paper's argument graph (staff and judge subagents); the question was written by net-writer; the gate arms and grader are Sonnet subagents. Every verdict is model against model; no human has checked this item.",tiny))
    else:
        story.append(Spacer(1,6)); story.append(P("This sheet contains no answer. It is what the answering model receives.",tiny))
    os.makedirs(outdir,exist_ok=True); fn=f"{outdir}/{'QRA' if answered else 'Q'}_{paper[:40]}_{tid}.pdf"
    def footer(c,d): c.saveState(); c.setFont("DV",7); c.setFillColor(MUTED); c.drawString(0.75*inch,0.5*inch,f"causalmat v06c · item {tid} · {paper[:60]}"+("" if answered else " · question only")); c.drawRightString(letter[0]-0.75*inch,0.5*inch,f"page {d.page}"); c.restoreState()
    SimpleDocTemplate(fn,pagesize=letter,leftMargin=0.75*inch,rightMargin=0.75*inch,topMargin=0.7*inch,bottomMargin=0.75*inch,title=f"{tid} · {g['title']}").build(story,onFirstPage=footer,onLaterPages=footer)
    return fn
if __name__=="__main__":
    out=os.path.join(ROOT,"results","v06c","sheets")
    for l in open(os.path.join(ROOT,"results","v06c","solving_gate.jsonl")):
        r=json.loads(l)
        if r["verdict"]!="valid": continue
        for a in (False,True): print(os.path.basename(build(r,a,out)))
