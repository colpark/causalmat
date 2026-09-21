"""build_packets_v06.py: v06 paper packets for graph extraction.

  python taxonomy/build_packets_v06.py taxonomy/v06_pilot/papers.txt taxonomy/v06_pilot

Changes from v05 (build_packets.py + add_panel_sections.py):
  - no MatMech content in the packet: the "Extracted mechanisms (MatMech)" block, the tetrahedron summary, the MST chain,
    the material summary fields and every figure's image_description ("linked text") move to judge_only/<paper>.matmech.md
  - full text where the host can fetch publisher XML (MatMMExtract Elsevier/Springer fetchers, which need
    ELSEVIER_API_KEY/ELSEVIER_INST_TOKEN or SPRINGER_API_KEY); otherwise the header says text_source: captions_only
  - the panel section lists per crop its OCR cue classes, every OCR token with its box, and annotated: true when a token
    is a word or phrase written in the image (not a panel letter, tick, unit, scale bar or axis label); the annotation
    strings are listed
"""
import json, os, re, sys
ROOT = "matmech"
papers = [l.strip() for l in open(sys.argv[1]) if l.strip()]
out = sys.argv[2]; os.makedirs(f"{out}/packets", exist_ok=True); os.makedirs(f"{out}/judge_only", exist_ok=True)

UNIT = r"(?:nm|µm|μm|um|mm|cm|m|Å|A|s|min|h|°C|℃|C|K|eV|keV|kV|V|mV|mA|A|Hz|kHz|MHz|%|wt%|at%|a\.u\.|au|deg|°)"
LETTER = re.compile(r"^[\(\[]?[A-Za-z][\)\]]?[.,]?$")
NUMERIC = re.compile(r"^[\s\d.,:;+\-−–()\[\]<>{}/×x*~°]+$")          # ticks, hkl indices, numbers
SCALE = re.compile(rf"^[\s\d.,]*{UNIT}$", re.I)                        # 2um, 500 nm, 10%
AXIS = re.compile(r"(intensity|a\.?u\.?|counts?|degree|2\s*[θo0]|theta|wavenumber|cm-1|cm\^?-1|binding\s*energy|"
                  r"energy|time|temperature|current|potential|voltage|frequency|wavelength|absorbance|transmittance|"
                  r"reflectance|capacit|density|strain|stress|load|depth|distance|position|z['\"]?\s*\(|"
                  r"-?z''|z'|log|cycle|number|mass|weight|heat\s*flow|raman\s*shift|\(ohm|ω|ohm)", re.I)

def classify(tok):
    t = tok.strip()
    if not t: return "empty"
    if LETTER.match(t): return "letter"
    if NUMERIC.match(t): return "tick"
    if SCALE.match(t): return "scale"
    if sum(ch.isalpha() for ch in t) < 2: return "tick"
    if AXIS.search(t): return "axis"
    return "annotation"

def clip(s, k):
    s = " ".join((s or "").split()); return s if len(s) <= k else s[:k] + " …"

stats = []
for pid in papers:
    base = f"{ROOT}/{pid}"; name = pid.replace("/", "__")
    d = json.load(open(f"{base}/data.json"))
    mj = json.load(open(f"{base}/panels/match.json"))
    ocr = {c["crop"]: c for c in json.load(open(f"{base}/panels/ocr.json"))["crops"]} if os.path.exists(f"{base}/panels/ocr.json") else {}
    order = {im.get("image_path"): i for i, im in enumerate(d.get("image_info") or [], 1)}
    doi = (d.get("doi") or "").replace("https://doi.org/", "")
    text_source = "captions_only"   # no ELSEVIER_API_KEY / SPRINGER_API_KEY on this host; Wiley titles have no fetcher
    L = [f"# {d.get('title')}", f"- paper_id: `{pid}`", f"- doi: {doi}  year: {d.get('year')}",
         f"- text_source: {text_source}",
         "## Figures (in paper order). Open an image with the Read tool on its absolute path."]
    for i, im in enumerate(d.get("image_info") or [], 1):
        L += [f"### F{i}", f"- path: {os.path.abspath(base)}/{im.get('image_path')}",
              f"- caption: {clip(' '.join(im.get('image_caption') or []), 900)}"]
    L += ["", "## Panels (match/v4" + (", ocr/v1" if ocr else ", no OCR") + ")",
          "Canonical id = <doi>#F<figure><panel>. Cite these ids in `panel_ids`; never invent one.",
          "Per crop: OCR cue classes, OCR tokens with boxes [x0,y0,x1,y1] in crop pixels, and annotated: true when a",
          "token is a word or phrase written inside the image; those strings are listed under annotations.", ""]
    n_ann = n_crops = 0
    for f in mj["figures"]:
        fi = order.get(f["file"], "?")
        if f["tier"] == "C":
            L.append(f"Figure {fi} (F{fi}), tier C ({f['reason']}): no panels offered; whole figure {os.path.abspath(base)}/{f['file']}"); continue
        L.append(f"Figure {fi} (F{fi}), tier {f['tier']} ({f['reason']})")
        if not f["panels"]: L.append("   (no panel records)")
        for p in f["panels"]:
            lab = p["label"]; cid = f"{doi}#F{fi}{lab if lab != 'single' else ''}"; crop = p.get("crop")
            o = ocr.get(crop) if crop else None
            L.append(f"  {cid}  crop {os.path.abspath(base) + '/' + crop if crop else '(whole figure)'}")
            L.append(f"     caption span: \"{clip(p.get('definition'), 200)}\"")
            if o:
                n_crops += 1
                toks = o.get("tokens") or []
                ann = [t["text"] for t in toks if classify(t["text"]) == "annotation"]
                axis = [t["text"] for t in toks if classify(t["text"]) == "axis"]
                n_ann += bool(ann)
                L.append(f"     ocr letter: {o.get('letter')} ({'agrees' if o.get('letter_agrees') else 'disagrees' if o.get('letter') else 'none'})"
                         f"   cue classes: {o.get('cues') or []}   scale bar: {bool(o.get('has_scale_bar'))}")
                L.append(f"     annotated: {'true' if ann else 'false'}" + (f"   annotations: {ann}" if ann else "") + (f"   axis labels: {axis}" if axis else ""))
                L.append("     tokens: " + json.dumps([[t["text"], t["box"]] for t in toks], ensure_ascii=False))
            else:
                L.append("     ocr: none for this crop")
    open(f"{out}/packets/{name}.md", "w").write("\n".join(L) + "\n")
    # everything MatMech removed from the packet goes to the judge-only file
    J = [f"# MatMech content for {pid} (judge only; not shown to staff)", f"- material: {d.get('material_object')}  elements: {d.get('material_element')}  category: {d.get('material_category')}",
         f"- MST chain: {d.get('casual_chain')}", "## Tetrahedron elements"] + [f"- **{k}**: {v}" for k, v in (d.get("tetrahedron_element") or {}).items()]
    J.append("## Figure image_description (MatMech linked text)")
    for i, im in enumerate(d.get("image_info") or [], 1):
        J.append(f"### F{i} [{im.get('image_function')}; microscopic={im.get('microscopic_image')}]\n{' '.join(im.get('image_description') or [])}")
    J.append("## Extracted mechanisms (MatMech)")
    for i, m in enumerate(d.get("mechanism") or [], 1):
        e = m.get("experiment") or {}
        J += [f"### M{i}  {m.get('link')}", f"- cause: {m.get('cause')}", f"- effect: {m.get('effect')}",
              f"- experiment: {e.get('name')} | {e.get('type')} | params: {e.get('parameters')} | result: {e.get('result')}"]
        for s in (m.get("mechanism") or {}).get("reasoning_chain") or []:
            J.append(f"  - [{s.get('type')}] {s.get('statement')}")
    open(f"{out}/judge_only/{name}.matmech.md", "w").write("\n".join(J) + "\n")
    stats.append({"paper": pid, "text_source": text_source, "figures": len(d.get("image_info") or []), "ocr_crops": n_crops,
                  "annotated_crops": n_ann, "matmech_mechanisms": len(d.get("mechanism") or [])})
json.dump(stats, open(f"{out}/packets_v06.json", "w"), indent=1)
for s in stats: print(s)
