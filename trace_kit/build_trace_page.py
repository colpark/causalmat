"""build_trace_page.py: full argument graph + trace overlays in one self-contained page."""
import json, sys, html
from collections import defaultdict

SPINE_RELS = {"motivates", "realizes", "feeds_into", "produces", "causes", "explains", "supports"}
AUDIT_RELS = {"qualifies", "contrasts", "rules_out"}
STAGE_LABEL = {"HYP": "Hypothesis", "DES": "Design", "PRC": "Processing", "STR": "Structure", "MEC": "Mechanism",
               "PRP": "Property", "PRF": "Performance", "DSC": "Discussion", "OBS": "Observation", "KNW": "Knowledge"}


def build(graph_path, spec_path, traces_path, out_path):
    g = json.load(open(graph_path)); s = json.load(open(spec_path)); T = json.load(open(traces_path))
    N = {n["id"]: n for n in g["nodes"]}
    inn, out = defaultdict(list), defaultdict(list)
    for e in g["edges"]: inn[e["dst"]].append(e); out[e["src"]].append(e)
    nec = {}
    for ln in s["nodes"]:
        for m in str(ln.get("source", "")).replace(",", " ").split(): nec[m] = ln.get("necessity")

    spine = [n["id"] for n in g["nodes"] if n.get("spine")]
    spine_idx = {c: i for i, c in enumerate(spine)}
    # left: OBS nodes at the row of their first spine target; right: KNW premises and off-spine claims
    left, right = defaultdict(list), defaultdict(list)
    placed = set()
    for n in g["nodes"]:
        if n["id"] in placed or n.get("spine"): continue
        tg = [e["dst"] for e in out[n["id"]] if e["dst"] in spine_idx]
        if not tg:  # off-spine node pointing at an off-spine node (r2->q18): resolve via that node's target
            tg2 = [e2["dst"] for e in out[n["id"]] for e2 in out[e["dst"]] if e2["dst"] in spine_idx]
            tg = tg2
        if not tg:
            src = [e["src"] for e in inn[n["id"]] if e["src"] in spine_idx]
            if not src: continue
            row = max(src, key=lambda c: spine_idx[c])
        else:
            row = min(tg, key=lambda c: spine_idx[c])
        (left if n["type"].startswith("OBS") else right)[row].append(n["id"]); placed.add(n["id"])

    SX, SW, SH = 620, 250, 62
    EW, EH = 232, 58
    LH, STAGE_H, TOP = 70, 26, 28
    BUS, BUS2, RBUS = SX - SW/2 - 30, SX - SW/2 - 44, SX + SW/2 + 30
    COL1 = BUS - 24 - EW/2
    RCOL = RBUS + 24 + EW/2
    W = RCOL + EW/2 + 24
    pos, bands = {}, []
    y = TOP; prev = None
    for c in spine:
        st = N[c]["type"].split("/")[0]; key = "MEC/PRP" if st in ("MEC", "PRP") else st
        if key != prev:
            bands.append({"label": STAGE_LABEL.get(st, st) if key != "MEC/PRP" else "Mechanism and property", "y0": y}); y += STAGE_H; prev = key
        lines = max(1, len(left[c]), len(right[c]))
        y0 = y
        pos[c] = dict(x=SX, y=y0 + lines*LH/2, w=SW, h=SH)
        for i, nid in enumerate(left[c]): pos[nid] = dict(x=COL1, y=y0 + i*LH + LH/2, w=EW, h=EH)
        for i, nid in enumerate(right[c]): pos[nid] = dict(x=RCOL, y=y0 + i*LH + LH/2, w=EW, h=EH)
        y = y0 + lines*LH; bands[-1]["y1"] = y
    H = y + 24

    def box(i): p = pos[i]; return p["x"]-p["w"]/2, p["y"]-p["h"]/2, p["x"]+p["w"]/2, p["y"]+p["h"]/2
    lanes_busy = []
    def lane(y0, y1):
        for k in range(6):
            if all(not (l == k and not (y1 < a-6 or y0 > b+6)) for (l, a, b) in lanes_busy): lanes_busy.append((k, y0, y1)); return k
        lanes_busy.append((5, y0, y1)); return 5
    edges = []
    for e in g["edges"]:
        a, b = e["src"], e["dst"]
        if a not in pos or b not in pos: continue
        pa, pb = pos[a], pos[b]; ax0, ay0, ax1, ay1 = box(a); bx0, by0, bx1, by1 = box(b)
        kind = "audit" if e["rel"] in AUDIT_RELS else "premise" if e["rel"] == "premise_for" else "spine" if (a in spine_idx and b in spine_idx) else "evidence"
        if a in spine_idx and b in spine_idx:
            if spine_idx[b] == spine_idx[a] + 1: pts = [(pa["x"], ay1), (pb["x"], by0)]
            else:
                lx = RBUS + 10 + lane(pa["y"], pb["y"])*14
                pts = [(ax1, pa["y"]), (lx, pa["y"]), (lx, pb["y"]), (bx1, pb["y"])]
        elif pa["x"] < SX and pb["x"] == SX:
            bx = BUS2 if kind == "audit" else BUS
            pts = [(ax1, pa["y"]), (bx, pa["y"]), (bx, pb["y"]), (bx0, pb["y"])] if abs(pa["y"]-pb["y"]) > 1 else [(ax1, pa["y"]), (bx0, pb["y"])]
        elif pa["x"] > SX and pb["x"] == SX:
            pts = [(ax0, pa["y"]), (RBUS, pa["y"]), (RBUS, pb["y"]), (bx1, pb["y"])] if abs(pa["y"]-pb["y"]) > 1 else [(ax0, pa["y"]), (bx1, pb["y"])]
        elif pa["x"] == SX and pb["x"] > SX:
            pts = [(ax1, pa["y"]), (RBUS, pa["y"]), (RBUS, pb["y"]), (bx0, pb["y"])] if abs(pa["y"]-pb["y"]) > 1 else [(ax1, pa["y"]), (bx0, pb["y"])]
        else:  # same side (left->right, e.g. r2 -> q18)
            lx = RBUS + 10 + lane(pa["y"], pb["y"])*14
            pts = [(ax1, pa["y"]), (BUS2-14, pa["y"]), (BUS2-14, pb["y"]-EH/2-6), (lx, pb["y"]-EH/2-6), (lx, pb["y"]), (bx0, pb["y"])] if pa["x"] < pb["x"] else [(ax0, pa["y"]), (bx1, pb["y"])]
        edges.append(dict(src=a, dst=b, rel=e["rel"], op=e.get("mm_op"), kind=kind, pts=pts))

    nodes = []
    for n in g["nodes"]:
        if n["id"] not in pos: continue
        a = n.get("attrs") or {}
        nodes.append(dict(id=n["id"], type=n["type"], stage=n["type"].split("/")[0], label=n["label"], spine=bool(n.get("spine")),
                          panel_ids=n.get("panel_ids") or [], figs=n.get("figs") or [], modality=n.get("modality"),
                          support=n.get("image_support"), technique=a.get("technique_norm") or a.get("technique"),
                          text_silent=bool(a.get("text_silent")), necessity=nec.get(n["id"]),
                          conditions=a.get("panel_conditions"), **pos[n["id"]]))
    payload = dict(title=g["title"], paper_id=g["paper_id"], W=W, H=H, bands=bands, nodes=nodes, edges=edges,
                   traces=T["traces"], panels=s.get("panels", {}))
    open(out_path, "w", encoding="utf-8").write(PAGE.replace("__DATA__", json.dumps(payload).replace("</", "<\\/")))
    print("wrote", out_path, "nodes", len(nodes), "edges", len(edges), "traces", len(T["traces"]), "canvas", W, "x", H)


PAGE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Argument graph and reasoning-trace cuts</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);
 --bg:#f6f4ee;--panel:#fffdf8;--ink:#1e2126;--ink-2:#5a6270;--line:#d9d4c8;--line-2:#c2bcae;--spine:#2b2f36;--ev:#6f7a8a;--audit:#b9312c;--premise:#7a5fb3;
 --hyp:#4a6da7;--des:#2c8a86;--prc:#b9861a;--str:#6a5cb8;--mec:#6a8b2a;--prp:#2f7d52;--prf:#1f6e9e;--dsc:#4b4f57;--knw:#7a5fb3;--obs:#3b4250;
 --shown:#2f8f5b;--partial:#d29a2b;--none:#9aa1ab;--focus:#1f6e9e;--open:#2f8f5b;--control:#d29a2b;--closed:#9aa1ab;
 --t-claim:#1f6e9e;--t-ev:#2f8f5b;--t-hidden:#b9312c;--t-cause:#7a5fb3;--t-ctx:#9aa1ab;
 --font:"Instrument Sans","Segoe UI",Roboto,Helvetica,Arial,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15171b;--panel:#1d2026;--ink:#e8e6df;--ink-2:#a3a9b3;--line:#2e323a;--line-2:#444a54;--spine:#d8dbe0;--ev:#8f98a6;--audit:#e0645d;--premise:#a894d8;--hyp:#8aa8dd;--des:#5fbdb8;--prc:#d9a83c;--str:#a397e0;--mec:#a2c05a;--prp:#5fb58a;--prf:#63a9d8;--dsc:#b3b8c2;--knw:#a894d8;--obs:#c3c9d3;--shown:#5fbf85;--partial:#e0b04a;--none:#6c737d;--focus:#63a9d8;--open:#5fbf85;--control:#e0b04a;--closed:#6c737d;--t-claim:#63a9d8;--t-ev:#5fbf85;--t-hidden:#e0645d;--t-cause:#a894d8;--t-ctx:#6c737d}}
html{height:100%}body{margin:0;height:100%;background:var(--bg);color:var(--ink);font-family:var(--font);font-size:14px;line-height:1.45;display:flex;flex-direction:column;overflow:hidden}*{box-sizing:inherit}
header{padding:12px 18px 10px;border-bottom:1px solid var(--line);background:var(--panel);flex:0 0 auto}
header h1{font-size:16px;font-weight:600;margin:0 0 2px}header .meta{color:var(--ink-2);font-size:12.5px;margin:0}
.controls{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-top:8px}
.chip{border:1px solid var(--line-2);background:transparent;color:var(--ink);border-radius:999px;padding:4px 10px;font:inherit;font-size:12px;cursor:pointer;line-height:1.2;display:inline-flex;gap:6px;align-items:center}
.chip b{width:8px;height:8px;border-radius:50%;display:inline-block}
.chip[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
main{flex:1 1 auto;display:flex;min-height:0;position:relative}
#stage{flex:1 1 auto;min-width:0;position:relative;overflow:hidden;touch-action:none;cursor:grab}#stage svg{width:100%;height:100%;display:block}
.zoom{position:absolute;left:12px;bottom:12px;display:flex;gap:4px;z-index:2}.zoom button{width:34px;height:34px;border-radius:8px;border:1px solid var(--line-2);background:var(--panel);color:var(--ink);font:inherit;font-size:16px;cursor:pointer}.zoom button.fit{width:auto;padding:0 10px;font-size:12.5px}
.legend{position:absolute;right:12px;bottom:12px;background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:11.5px;color:var(--ink-2);display:grid;grid-template-columns:auto auto;gap:3px 10px;z-index:2}
.legend span{display:inline-flex;align-items:center;gap:6px}.legend i{width:14px;height:14px;border-radius:3px;display:inline-block;border:2px solid}
aside{flex:0 0 420px;max-width:46vw;border-left:1px solid var(--line);background:var(--panel);overflow:auto;padding:14px 18px 24px;display:none}aside.open{display:block}
aside .close{float:right;border:0;background:transparent;color:var(--ink-2);font:inherit;font-size:20px;cursor:pointer}
aside .kicker{font-size:12px;color:var(--ink-2);margin:0 0 4px}aside h2{font-size:15px;font-weight:600;margin:0 0 8px;line-height:1.35}
aside dl{display:grid;grid-template-columns:auto 1fr;gap:3px 12px;margin:0 0 10px;font-size:13px}aside dt{color:var(--ink-2)}aside dd{margin:0}
aside .note{background:var(--bg);border-left:3px solid var(--line-2);padding:7px 10px;font-size:12.5px;margin:0 0 10px}
aside .note.audit{border-left-color:var(--audit)}aside .note.hidden{border-left-color:var(--t-hidden)}
aside h3{font-size:12.5px;color:var(--ink-2);font-weight:500;margin:12px 0 4px}
.step{display:grid;grid-template-columns:22px 1fr;gap:8px;padding:6px 0;border-top:1px solid var(--line);font-size:13px}
.step .n{color:var(--ink-2);font-size:11.5px;padding-top:2px}.step .role{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.step.claim .role{color:var(--t-claim)}.step.evidence .role{color:var(--t-ev)}.step.audit .role{color:var(--audit)}.step.cause .role,.step.mechanism .role{color:var(--t-cause)}.step.redacted .role{color:var(--t-hidden)}.step.context .role,.step.downstream .role{color:var(--t-ctx)}
.step.hidden{background:repeating-linear-gradient(135deg,transparent 0 6px,rgba(185,49,44,.07) 6px 12px);border-left:3px solid var(--t-hidden);padding-left:8px}
.step .meta{color:var(--ink-2);font-size:11.5px}
.tag{display:inline-block;border:1px solid var(--line-2);border-radius:4px;padding:0 5px;font-size:11px;margin-right:4px}
.status{display:inline-block;padding:1px 8px;border-radius:999px;font-size:11.5px;font-weight:600;color:#fff}.status.big{display:block;border-radius:6px;padding:6px 10px;font-size:12.5px;letter-spacing:.02em;margin:0 0 10px}
.qa{border-radius:6px;padding:9px 11px;margin:0 0 8px;font-size:13.5px;line-height:1.5}.qa .lbl{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-2);margin-bottom:3px}.qa.q{background:rgba(31,110,158,.08);border-left:3px solid var(--t-claim)}.qa.a{background:rgba(47,143,91,.08);border-left:3px solid var(--t-ev)}.qa.g{background:var(--bg);border-left:3px solid var(--line-2)}
.node{cursor:pointer}.node rect.body{fill:var(--panel);stroke:var(--line-2);stroke-width:1}.node.spine rect.body{stroke-width:1.4}
.node text{font-family:var(--font);fill:var(--ink);font-size:11px}.node text.kind{fill:var(--ink-2);font-size:9.5px}
.node.audit rect.body{stroke:var(--audit);stroke-width:1.5}.node.dim{opacity:.12}
.node.t-claim rect.body{stroke:var(--t-claim);stroke-width:3}.node.t-evidence rect.body{stroke:var(--t-ev);stroke-width:2.6}.node.t-audit rect.body{stroke:var(--audit);stroke-width:2.6}
.node.t-cause rect.body,.node.t-mechanism rect.body{stroke:var(--t-cause);stroke-width:2.6}.node.t-hidden rect.body{stroke:var(--t-hidden);stroke-width:3;stroke-dasharray:6 3}
.node.t-context rect.body,.node.t-downstream rect.body{stroke:var(--t-ctx);stroke-width:1.6}
.node text.hide{fill:var(--t-hidden);font-size:9.5px;font-weight:600}
.edge{fill:none;stroke:var(--ev);stroke-width:1.3}.edge.spine{stroke:var(--spine);stroke-width:1.7}.edge.audit{stroke:var(--audit);stroke-dasharray:5 4}.edge.premise{stroke:var(--premise);stroke-dasharray:2 3}
.edge.dim{opacity:.06}.edge.hot{stroke:var(--focus);stroke-width:2.4;opacity:1}
.band{fill:var(--ink);opacity:.035}.band-label{font-family:var(--font);font-size:11px;fill:var(--ink-2);font-weight:500}
@media (max-width:760px){main{flex-direction:column}aside{flex:0 0 48%;max-width:none;border-left:0;border-top:1px solid var(--line)}.legend{display:none}}
</style></head><body>
<header><h1 id="title"></h1><p class="meta" id="meta"></p><div class="controls" id="controls"></div></header>
<main><div id="stage"><svg id="svg" xmlns="http://www.w3.org/2000/svg"></svg>
<div class="zoom"><button class="fit" id="fit">Fit</button><button id="zin">+</button><button id="zout">−</button></div>
<div class="legend"><span><i style="border-color:var(--t-claim)"></i>seed claim</span><span><i style="border-color:var(--t-ev)"></i>evidence used</span>
<span><i style="border-color:var(--t-hidden);border-style:dashed"></i>hidden from the model</span><span><i style="border-color:var(--t-cause)"></i>competing cause</span>
<span><i style="border-color:var(--audit)"></i>audit</span><span><i style="border-color:var(--t-ctx)"></i>context and downstream</span></div></div>
<aside id="panel"></aside></main>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);const svg=document.getElementById('svg');const NS='http://www.w3.org/2000/svg';
const byId=Object.fromEntries(D.nodes.map(n=>[n.id,n]));const el=(t,a={},p)=>{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e;};
const SV={HYP:'--hyp',DES:'--des',PRC:'--prc',STR:'--str',MEC:'--mec',PRP:'--prp',PRF:'--prf',DSC:'--dsc',KNW:'--knw',OBS:'--obs'};
const open=D.traces.filter(t=>t.status==='open').length,ctrl=D.traces.filter(t=>t.status==='control').length,closed=D.traces.filter(t=>t.status==='closed').length;
document.getElementById('title').textContent=D.title;
document.getElementById('meta').textContent=`${D.nodes.length} nodes, ${D.edges.length} edges. ${D.traces.length} candidate traces cut from the graph: ${open} open, ${ctrl} negative controls, ${closed} closed. Pick a trace to see which nodes it uses and what it hides; click any node for its evidence.`;
const root=el('g',{},svg),gB=el('g',{},root),gE=el('g',{},root),gN=el('g',{},root);const defs=el('defs',{},svg);
for(const [id,col] of [['arr','var(--spine)'],['arr-ev','var(--ev)'],['arr-au','var(--audit)'],['arr-pr','var(--premise)']]){const m=el('marker',{id,viewBox:'0 0 10 10',refX:'9',refY:'5',markerWidth:'7',markerHeight:'7',orient:'auto-start-reverse'},defs);el('path',{d:'M0,1 L9,5 L0,9 z',fill:col},m);}
for(const b of D.bands){el('rect',{class:'band',x:0,y:b.y0,width:D.W,height:b.y1-b.y0},gB);const t=el('text',{class:'band-label',x:12,y:b.y0+17},gB);t.textContent=b.label;}
function pathD(p){if(p.length===2)return `M${p[0][0]},${p[0][1]} L${p[1][0]},${p[1][1]}`;let d=`M${p[0][0]},${p[0][1]}`;const r=9;for(let i=1;i<p.length-1;i++){const [px,py]=p[i-1],[cx,cy]=p[i],[nx,ny]=p[i+1];const dx1=Math.sign(cx-px),dy1=Math.sign(cy-py),dx2=Math.sign(nx-cx),dy2=Math.sign(ny-cy);const l1=Math.min(r,Math.hypot(cx-px,cy-py)/2),l2=Math.min(r,Math.hypot(nx-cx,ny-cy)/2);d+=` L${cx-dx1*l1},${cy-dy1*l1} Q${cx},${cy} ${cx+dx2*l2},${cy+dy2*l2}`;}const L=p[p.length-1];return d+` L${L[0]},${L[1]}`;}
const edgeEls=[];for(const e of D.edges){const mk=e.kind==='spine'?'arr':e.kind==='audit'?'arr-au':e.kind==='premise'?'arr-pr':'arr-ev';const p=el('path',{class:'edge '+e.kind,d:pathD(e.pts),'marker-end':`url(#${mk})`},gE);p.dataset.src=e.src;p.dataset.dst=e.dst;edgeEls.push(p);}
function wrap(t,m){const w=t.split(' ');const L=[];let c='';for(const x of w){if((c+' '+x).trim().length>m){L.push(c.trim());c=x;}else c+=' '+x;}if(c.trim())L.push(c.trim());return L;}
const nodeEls={};
for(const n of D.nodes){const g=el('g',{class:'node'+(n.spine?' spine':'')+(n.text_silent?' audit':''),transform:`translate(${n.x-n.w/2},${n.y-n.h/2})`},gN);g.dataset.id=n.id;nodeEls[n.id]=g;
 el('rect',{class:'body',width:n.w,height:n.h,rx:5},g);el('rect',{x:0,y:0,width:5,height:n.h,rx:2,fill:`var(${SV[n.stage]||'--obs'})`},g);
 const k=el('text',{class:'kind',x:11,y:11},g);k.textContent=`${n.id} ${n.stage}${n.technique?' · '+n.technique:''}${n.panel_ids.length?' · '+n.panel_ids.map(p=>p.split('#')[1]).join(','):n.figs.length?' · '+n.figs.join(','):''}`;
 wrap(n.label,n.spine?42:38).slice(0,3).forEach((ln,i)=>{const t=el('text',{x:11,y:24+i*12},g);t.textContent=ln;});
 if(n.support){el('circle',{cx:n.w-9,cy:9,r:3.5,fill:{shown:'var(--shown)',partial:'var(--partial)'}[n.support]||'var(--none)'},g);}
 if(n.necessity){const t=el('text',{x:n.w-9,y:n.h-5,'text-anchor':'end','font-size':'9',fill:{necessary:'var(--shown)',corrective:'var(--audit)',redundant:'var(--partial)',decorative:'var(--none)'}[n.necessity]},g);t.textContent=n.necessity;}
 const ht=el('text',{class:'hide',x:n.w-9,y:n.h-5,'text-anchor':'end',display:'none'},g);ht.textContent='hidden';ht.dataset.hide='1';
 const tt=el('title',{},g);tt.textContent=n.label;g.addEventListener('click',ev=>{ev.stopPropagation();if(moved)return;selectNode(n.id);});
 g.addEventListener('mouseenter',()=>hot(n.id,true));g.addEventListener('mouseleave',()=>hot(n.id,false));}
let vb={x:0,y:0,w:D.W,h:D.H};function apply(){svg.setAttribute('viewBox',`${vb.x} ${vb.y} ${vb.w} ${vb.h}`);}
function fit(){const r=svg.getBoundingClientRect();const s=Math.max(D.W/r.width,D.H/r.height);vb={x:-6,y:-6,w:r.width*s+12,h:r.height*s+12};apply();}
function fitWidth(){const r=svg.getBoundingClientRect();vb={x:-6,y:-6,w:D.W+12,h:r.height*(D.W+12)/r.width};apply();}
function zoomAt(f,cx,cy){const r=svg.getBoundingClientRect();const px=vb.x+(cx-r.left)/r.width*vb.w,py=vb.y+(cy-r.top)/r.height*vb.h;vb.w*=f;vb.h*=f;vb.x=px-(cx-r.left)/r.width*vb.w;vb.y=py-(cy-r.top)/r.height*vb.h;apply();}
const stage=document.getElementById('stage');document.getElementById('fit').onclick=fit;
document.getElementById('zin').onclick=()=>{const r=svg.getBoundingClientRect();zoomAt(0.8,r.left+r.width/2,r.top+r.height/2);};document.getElementById('zout').onclick=()=>{const r=svg.getBoundingClientRect();zoomAt(1.25,r.left+r.width/2,r.top+r.height/2);};
stage.addEventListener('wheel',ev=>{ev.preventDefault();if(ev.ctrlKey||ev.metaKey){zoomAt(ev.deltaY>0?1.1:0.9,ev.clientX,ev.clientY);}else{const r=svg.getBoundingClientRect();vb.x+=ev.deltaX*vb.w/r.width;vb.y+=ev.deltaY*vb.h/r.height;apply();}},{passive:false});
let drag=null,moved=false;stage.addEventListener('pointerdown',ev=>{if(ev.target.closest('.zoom'))return;drag={x:ev.clientX,y:ev.clientY,vx:vb.x,vy:vb.y};moved=false;});
window.addEventListener('pointermove',ev=>{if(!drag)return;const r=svg.getBoundingClientRect();if(Math.hypot(ev.clientX-drag.x,ev.clientY-drag.y)>4)moved=true;if(moved){vb.x=drag.vx-(ev.clientX-drag.x)*vb.w/r.width;vb.y=drag.vy-(ev.clientY-drag.y)*vb.h/r.height;apply();}});
window.addEventListener('pointerup',()=>{drag=null;});
function hot(id,on){nodeEls[id].classList.toggle('hot',on);for(const p of edgeEls){if(p.dataset.src===id||p.dataset.dst===id)p.classList.toggle('hot',on);}}
function esc(s){return String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
const panel=document.getElementById('panel');let current=null;
// ---- traces
const C=document.getElementById('controls');const chips=[];
function chip(label,col,fn,pressed){const b=document.createElement('button');b.className='chip';b.innerHTML=`<b style="background:${col}"></b>${esc(label)}`;b.setAttribute('aria-pressed',String(!!pressed));b.onclick=fn;C.appendChild(b);chips.push(b);return b;}
chip('Whole graph','var(--ink-2)',()=>showTrace(null),true);
for(const t of D.traces){const col=`var(--${t.status})`;chip(`${t.id} ${t.root}${t.subtype?' · '+t.subtype:''} · ${t.status}`,col,()=>showTrace(t.id));}
function hiddenNodes(t){ if(t.root==='infer')return t.evidence; if(t.subtype==='rejection')return t.evidence; if(t.subtype==='competing causes'){return D.edges.filter(e=>e.rel==='explains'&&e.dst===t.seed_claim).map(e=>e.src);} if(t.subtype==='mechanism')return [t.seed_claim]; if(t.root==='intervene')return [t.seed_claim]; return [];}
function showTrace(id){current=id;for(const b of chips)b.setAttribute('aria-pressed','false');
 const idx=id?D.traces.findIndex(t=>t.id===id)+1:0;chips[idx].setAttribute('aria-pressed','true');
 for(const n of D.nodes){const g=nodeEls[n.id];g.className.baseVal=g.className.baseVal.replace(/ t-\S+|\bdim\b/g,'');g.querySelector('[data-hide]').setAttribute('display','none');}
 for(const p of edgeEls)p.classList.remove('dim');
 if(!id){panel.classList.remove('open');return;}
 const t=D.traces.find(x=>x.id===id);const roles={};for(const s of t.walk)roles[s.node]=roles[s.node]||s.role;
 for(const c of (t.rival||[]))roles[c]='cause';for(const c of t.walk.filter(s=>s.role==='cause'||s.role==='mechanism'))roles[c.node]=c.role;
 const hid=new Set(t.hidden||hiddenNodes(t));const used=new Set(Object.keys(roles));
 for(const n of D.nodes){const g=nodeEls[n.id];if(!used.has(n.id)){g.classList.add('dim');continue;}g.classList.add('t-'+(hid.has(n.id)?'hidden':roles[n.id]));if(hid.has(n.id))g.querySelector('[data-hide]').setAttribute('display','');}
 for(const p of edgeEls){if(!(used.has(p.dataset.src)&&used.has(p.dataset.dst)))p.classList.add('dim');}
 renderTrace(t,hid);}
function renderTrace(t,hid){let h=`<button class="close" onclick="showTrace(null)">×</button>`;
 const badge={open:'OPEN · a training item',control:'NEGATIVE CONTROL · no domain model needed',closed:'CLOSED · no trace produced'}[t.status];
 h+=`<p class="kicker">${esc(t.id)} · ${esc(t.root)}${t.subtype?' · '+esc(t.subtype):''}</p>`;
 h+=`<div class="status big" style="background:var(--${t.status})">${esc(badge)}</div>`;
 if(t.question)h+=`<div class="qa q"><div class="lbl">Question the model gets</div>${esc(t.question)}</div>`;
 if(t.answer_key)h+=`<div class="qa a"><div class="lbl">${t.status==='closed'?'What the graph says, and why no item':'Answer key'}</div>${esc(t.answer_key)}</div>`;
 if(t.grading)h+=`<div class="qa g"><div class="lbl">${t.status==='closed'?'Why closed':'Graded by'}</div>${esc(t.grading)}</div>`;
 if(t.validation&&t.status!=='closed'){const nets=t.validation.nets||{};const rows=Object.entries(nets).map(([k,r])=>`<span class="tag" style="border-color:${r.pass?'var(--shown)':'var(--audit)'};color:${r.pass?'var(--shown)':'var(--audit)'}">${esc(k)} ${r.pass?'✓':'✗'}</span>`).join(' ');
  h+=`<div class="qa g"><div class="lbl">Safety nets · ${esc(t.validation.verdict)}</div>${rows}${t.redactions?'<div class="meta" style="margin-top:6px">Redacted from the prompt: '+t.redactions.map(r=>esc(r.node)+' ('+esc(r.why)+')').join('; ')+'</div>':''}</div>`;}
 h+=`<h3>Seed claim</h3><h2>${esc(byId[t.seed_claim]?byId[t.seed_claim].label:t.seed_claim)}</h2>`;
 if(t.ruling&&t.status!=='closed')h+=`<div class="note audit"><b>Ruling.</b> ${esc(t.ruling)}</div>`;
 h+=`<dl><dt>Branch</dt><dd>${esc(t.branch)}</dd>`;
 if(t.rival&&t.rival.length)h+=`<dt>Rival</dt><dd>${t.rival.map(r=>esc(byId[r]?byId[r].label:r)).join('<br>')}</dd>`;
 h+=`<dt>FM lane</dt><dd>${esc(t.fm_family)}</dd>`;if(t.lift)h+=`<dt>Lift</dt><dd>${esc(t.lift)}</dd>`;
 h+=`<dt>Floor</dt><dd>${t.floor.reaches===null?'not applicable':t.floor.reaches?'reaches the claim via '+esc((t.floor.support||[]).join(', ')):'fails'}${t.floor.note?'. '+esc(t.floor.note):''}</dd>`;
 h+=`<dt>Depth</dt><dd>${t.depth??'n/a'}${t.depth_families&&t.depth_families.length?' (leave-one-out: '+esc(t.depth_families.join(', '))+')':''}${t.channels_involved?' · channels involved: '+esc(t.channels_involved.join(', ')):''}</dd>`;
 h+=`<dt>Grader</dt><dd>${esc(t.grader)}</dd></dl>`;
 h+=`<div class="note hidden"><b>Hidden from the model.</b> ${esc(t.mask)}</div>`;
 if(t.linear&&t.linear.length){h+=`<h3>Single-direction reasoning (one legal walk through the DAG)</h3>`;
  for(const s of t.linear){h+=`<div class="step ${s.hidden?'hidden':''} lin"><div class="n">${s.step}</div><div><span class="role" style="color:${s.hidden?'var(--t-hidden)':'var(--ink-2)'}">${esc(s.role)}${s.hidden?' · hidden, model must produce':''}</span> <span class="meta">${s.depends_on.length?'needs step '+s.depends_on.join(', '):''} · ${esc(s.nodes.join(', '))}</span><br>${esc(s.text)}</div></div>`;}}
 if(t.walk.length){h+=`<h3>Graph walk (all nodes the trace touches)</h3>`;let i=0;for(const s of t.walk){const n=byId[s.node];if(!n)continue;i++;const isH=hid.has(s.node);
  h+=`<div class="step ${esc(s.role)}${isH?' hidden':''}"><div class="n">${i}</div><div><span class="role">${esc(s.role)}${isH?' · hidden':''}</span> <span class="meta">${esc(n.id)} ${esc(n.stage)}</span><br>${esc(n.label)}`;
  if(s.role==='evidence'||s.role==='audit'){h+=`<div class="meta">${s.op?'<span class="tag">'+esc(String(s.op).replace(/_/g,' '))+'</span>':''}${s.verdict?'<span class="tag">'+esc(s.verdict)+'</span>':''}${n.technique?'<span class="tag">'+esc(n.technique)+'</span>':''}${n.panel_ids.length?' panels: '+esc(n.panel_ids.map(p=>p.split('#')[1]).join(', ')):''}</div>`;
   if(n.conditions)h+=`<div class="meta">conditions: ${esc(n.conditions.map(c=>c.condition).join(' / '))}</div>`;}
  h+=`</div></div>`;}}
 if(t.siblings)h+=`<h3>Siblings from the same read</h3><div class="meta">${esc(t.siblings.join(', '))} share evidence node ${esc(t.evidence[0])}; one group id, never split across train and test.</div>`;
 panel.innerHTML=h;panel.classList.add('open');}
function selectNode(id){const n=byId[id];let h=`<button class="close" onclick="panel.classList.remove('open')">×</button><p class="kicker">${esc(n.id)} · ${esc(n.type)}${n.spine?' · on the spine':''}</p><h2>${esc(n.label)}</h2><dl>`;
 if(n.technique)h+=`<dt>Technique</dt><dd>${esc(n.technique)}</dd>`;if(n.modality)h+=`<dt>Modality</dt><dd>${esc(n.modality)}</dd>`;
 if(n.panel_ids.length)h+=`<dt>Panels</dt><dd>${n.panel_ids.map(p=>esc(p.split('#')[1])).join(', ')}</dd>`;else if(n.figs.length)h+=`<dt>Figure</dt><dd>${esc(n.figs.join(', '))} (whole figure, no crop)</dd>`;
 if(n.support)h+=`<dt>Image check</dt><dd>${esc(n.support)}</dd>`;if(n.necessity)h+=`<dt>Necessity</dt><dd>${esc(n.necessity)}</dd>`;h+=`</dl>`;
 if(n.text_silent)h+=`<div class="note audit"><b>Text silent.</b> The paper's text never states this; the figure does.</div>`;
 if(n.conditions)h+=`<div class="note">Conditions: ${esc(n.conditions.map(c=>c.condition+' ['+c.source+']').join(' / '))}</div>`;
 for(const pid of n.panel_ids){const P=D.panels[pid];if(P&&P.src)h+=`<figure><img src="${P.src}" style="max-width:100%"><figcaption class="meta">${esc(pid.split('#')[1])} ${P.definition?'· '+esc(P.definition):''}</figcaption></figure>`;}
 const ins=D.edges.filter(e=>e.dst===id),outs=D.edges.filter(e=>e.src===id);
 if(ins.length)h+=`<h3>Supported by</h3>`+ins.map(e=>`<div class="meta">${esc(e.rel)} ← ${esc(e.src)} ${esc(byId[e.src].label.slice(0,80))}</div>`).join('');
 if(outs.length)h+=`<h3>Leads to</h3>`+outs.map(e=>`<div class="meta">${esc(e.rel)} → ${esc(e.dst)} ${esc(byId[e.dst].label.slice(0,80))}</div>`).join('');
 panel.innerHTML=h;panel.classList.add('open');}
requestAnimationFrame(()=>{const r=svg.getBoundingClientRect();if(r.width<700){const w=760;vb={x:620-w/2,y:-6,w:w,h:r.height*w/r.width};apply();}else fitWidth();});
</script></body></html>"""

if __name__ == "__main__":
    build(*sys.argv[1:5])
