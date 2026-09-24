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
REPO="/home/claude/causalmat"; B="origin/trace-validation/2026-09-20"; FIVE="/home/claude/five"
def show(p, ref=B): return subprocess.run(["git","-C",REPO,"show",f"{ref}:{p}"],capture_output=True,text=True).stdout
PICKS=[("Journal_of_Advanced_Ceramics__s40145-019-0334-4","T5"),("Acta_Materialia__10.1016_j.actamat.2014.06.008","T10"),
       ("Advanced_Energy_Materials__aenm.201301564","T4"),("Advanced_Energy_Materials__aenm.201501833","T1"),("Advanced_Functional_Materials__10.1002_adfm.202005093","T3")]
MAN={x["id"]:x for x in json.load(open(f"{FIVE}/manifest_resolved.json"))["ids"]}
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
def panel_grid(paper, pids, folder, panels_meta, per_row=3, maxw=2.25*inch):
    cells=[]
    for p in pids:
        suf=p.split("#")[1]; path=f"{FIVE}/{paper}/{folder}/{suf}.jpg"
        if not os.path.exists(path): path=f"{FIVE}/{paper}/withheld/{suf}.jpg" if folder=="given" else path
        if not os.path.exists(path): cells.append(P(f"<b>{esc(suf)}</b><br/>(crop not in the zip)",tiny)); continue
        w,h=PILImage.open(path).size; iw=maxw; ih=iw*h/w
        if ih>2.0*inch: ih=2.0*inch; iw=ih*w/h
        m=MAN.get(p,{}); meta=panels_meta.get(p,{})
        cap=f"<b>{esc(suf)}</b> · tier {esc(m.get('tier','?'))} · ocr {esc(str(m.get('ocr_letter')))}{' ✓' if m.get('ocr_letter_agrees') else (' ✗' if m.get('ocr_letter_agrees') is False else '')}<br/>{esc((meta.get('definition') or '')[:110])}"
        cells.append([RLImage(path,width=iw,height=ih), P(cap,tiny)])
    rows=[cells[i:i+per_row] for i in range(0,len(cells),per_row)]
    for r in rows:
        while len(r)<per_row: r.append("")
    t=Table([[ (c if isinstance(c,str) else Table([[c[0]],[c[1]]],colWidths=[maxw]) ) for c in r] for r in rows], colWidths=[7.0*inch/per_row]*per_row)
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),2),("RIGHTPADDING",(0,0),(-1,-1),2)])); return t
def build(paper,tid,answered):
    T=json.loads(show(f"results/traces/{paper}.traces.json")); t=next(x for x in T["traces"] if x["id"]==tid)
    g=json.loads(show(f"taxonomy/graphs_v05/first100/{paper}.json","origin/main")); N={n["id"]:n for n in g["nodes"]}
    try: panels=json.loads(show(f"taxonomy/specs_v05/{paper}.json","origin/main")).get("panels",{})
    except Exception: panels={}
    hid=set(t.get("hidden",[])); hp=set(t.get("hidden_panels",[]))
    gtxt=(t.get("grader") or "")+" "+(t.get("grading") or ""); grader_nodes=set(re.findall(r"\b[a-z]\d+\b",gtxt)) if re.search(r"held out|held-out|independent channel",gtxt,re.I) else set()
    given=[]; withheld=[]
    for e in t["evidence"]:
        for p in (N[e].get("panel_ids") or []):
            (withheld if (p in hp or e in grader_nodes) else given).append(p)
    given=list(dict.fromkeys(given)); withheld=list(dict.fromkeys(withheld))
    story=[P(esc(g["title"]),h1), P(f"{esc(paper.split('__')[0].replace('_',' '))} · {esc(g['paper_id'])} · item {esc(tid)}"+(f" · <b>{esc(t['root'])}, {esc(t['subtype'])}</b> · status {esc(t['status']).upper()} · depth {t.get('depth')}" if answered else ""),tiny), Spacer(1,8)]
    story.append(box("QUESTION" if not answered else "QUESTION THE MODEL GETS",esc(t["question"]),QBG,colors.HexColor("#1f6e9e"))); story.append(Spacer(1,4))
    story.append(P("Context you are given",h2))
    rows=[[P(esc(N[s["node"]]["label"]),small)] for s in t["walk"] if s["node"] not in hid and s["role"] not in ("redacted","evidence","audit")]
    if rows:
        tb=Table(rows,colWidths=[7.0*inch]); tb.setStyle(TableStyle([("LINEBELOW",(0,0),(-1,-1),0.3,RULE),("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2)])); story.append(tb)
    ev_given=[e for e in t["evidence"] if e not in hid and e not in grader_nodes and t["root"]!="intervene"]
    if ev_given:
        story.append(P("Observations already stated for you",h2))
        tb=Table([[P(esc(N[e]["label"]),small)] for e in ev_given],colWidths=[7.0*inch]); tb.setStyle(TableStyle([("LINEBELOW",(0,0),(-1,-1),0.3,RULE),("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2)])); story.append(tb)
    story.append(P("Data: the panels you open",h2))
    if given: story.append(panel_grid(paper,given,"given",panels))
    else: story.append(P("No panels are handed over for this item.",small))
    story.append(Spacer(1,6)); story.append(box("ANSWER FORMAT",esc(FORMAT.get((t["root"],t["subtype"]),"Answer in at most six sentences. If it cannot be answered from what is given, write exactly: CANNOT DETERMINE.")),GBG,colors.HexColor("#8a8f98"),small))
    if answered:
        story.append(P("Reasoning: the single-direction walk (shaded steps are what the model must produce)",h2))
        rrows=[[P(f"<b>{s['step']}</b>",small),P(f"<b>{esc(s['role'])}</b>{' · <font color=\"#b9312c\"><b>HIDDEN</b></font>' if s['hidden'] else ''} <font color='#5f6b7a'>{esc(', '.join(s['nodes']))}{(' · needs '+', '.join(map(str,s['depends_on']))) if s['depends_on'] else ''}</font><br/>{esc(s['text'])}",small)] for s in t["linear"]]
        rt=Table(rrows,colWidths=[0.35*inch,6.65*inch]); st=[("VALIGN",(0,0),(-1,-1),"TOP"),("LINEBELOW",(0,0),(-1,-1),0.3,RULE),("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),4)]
        for i,s in enumerate(t["linear"]):
            if s["hidden"]: st.append(("BACKGROUND",(0,i),(-1,i),HBG))
        rt.setStyle(TableStyle(st)); story.append(rt); story.append(Spacer(1,8))
        story.append(box("ANSWER KEY",esc(t["answer_key"])+(f"<br/><font color='#5f6b7a'>nodes: {esc(', '.join(t.get('answer_key_nodes') or []))}</font>" if t.get("answer_key_nodes") else ""),ABG,colors.HexColor("#2f8f5b")))
        story.append(Spacer(1,5)); story.append(box("GRADED BY",esc(t["grading"])+f"<br/><font color='#5f6b7a'>floor with FM evidence removed: {'reaches' if t['floor'].get('reaches') else 'fails'} · leave-one-out depth {t.get('depth')} ({esc(', '.join(t.get('depth_families') or []))})</font>",GBG,colors.HexColor("#8a8f98"),small))
        if withheld:
            story.append(P("Withheld from the model (grading channel or hidden condition)",h2)); story.append(panel_grid(paper,withheld,"withheld",panels))
        story.append(Spacer(1,8)); story.append(P("Provenance. Every sentence in the context, the reasoning steps and the answer key is a node label from the paper's argument graph; the question was written by a Sonnet subagent from those labels (ceramic: hand-written, then rewritten). Every check is model against model; no human has checked this item.",tiny))
    else:
        story.append(Spacer(1,6)); story.append(P("This sheet contains no answer. It is what the answering model receives.",tiny))
    out="/mnt/user-data/outputs/"+("qra_with_data" if answered else "questions_with_data"); os.makedirs(out,exist_ok=True)
    fn=f"{out}/{'QRA' if answered else 'Q'}_{paper[:40]}_{tid}.pdf"
    def footer(c,d): c.saveState(); c.setFont("DV",7); c.setFillColor(MUTED); c.drawString(0.75*inch,0.5*inch,f"causalmat · item {tid} · {paper[:60]}"+("" if answered else " · question only")); c.drawRightString(letter[0]-0.75*inch,0.5*inch,f"page {d.page}"); c.restoreState()
    SimpleDocTemplate(fn,pagesize=letter,leftMargin=0.75*inch,rightMargin=0.75*inch,topMargin=0.7*inch,bottomMargin=0.75*inch,title=f"{tid} · {g['title']}").build(story,onFirstPage=footer,onLaterPages=footer)
    return fn
for paper,tid in PICKS:
    for a in (False,True): print(os.path.basename(build(paper,tid,a)))
