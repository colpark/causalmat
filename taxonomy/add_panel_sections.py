"""Append the panel section to packets built by build_packets.py.

Per figure: Tier A/B panels with their canonical id, crop path, OCR letter (or detector-only),
definition span, number of use sentences and OCR cues. A Tier C figure gets one line saying so.

Usage: python taxonomy/add_panel_sections.py --root <matmech> --packets <dir> --papers first100.jsonl
"""
import argparse
import json
import re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
ap.add_argument("--packets", required=True)
ap.add_argument("--papers", required=True)
a = ap.parse_args()
root, pk = Path(a.root).expanduser(), Path(a.packets).expanduser()

SCALE_RX = re.compile(r"\b\d+(?:\.\d+)?\s*(?:nm|µm|μm|um|mm|Å)\b", re.I)


def clip(s, n):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[:n] + "…"


stats = []
for line in open(a.papers):
    r = json.loads(line)
    folder = root / r["journal"] / r["doi"]
    pkt = pk / f"{r['journal']}__{r['doi']}.md".replace("/", "_")
    if not pkt.exists():
        print("! no packet for", r["doi"])
        continue
    mj, oj = folder / "panels" / "match.json", folder / "panels" / "ocr.json"
    if not mj.exists():
        continue
    match = json.load(open(mj))
    ocr = {}
    if oj.exists():
        for c in json.load(open(oj)).get("crops", []):
            ocr[c["crop"]] = c
    rec = json.load(open(folder / "data.json", encoding="utf-8"))
    order = {im.get("image_path"): i for i, im in enumerate(rec.get("image_info") or [], 1)}
    doi_pretty = (rec.get("doi") or r["doi"]).replace("https://doi.org/", "")
    L = ["", "## Panels (match/v4" + (", ocr/v1" if ocr else "") + " where present)",
         "Canonical id = <doi>#F<figure><panel>. Cite these ids in `panel_ids`; never invent one.", ""]
    offered = cited_possible = 0
    for f in match.get("figures", []):
        fi = order.get(f["file"], "?")
        if f["tier"] == "C":
            L.append(f"Figure {fi} (packet F{fi}), tier C ({f['reason']}): no panels offered")
            continue
        L.append(f"Figure {fi} (packet F{fi}), tier {f['tier']} ({f['reason']})")
        if not f["panels"]:
            L.append("   (no panel records)")
        for p in f["panels"]:
            offered += 1
            lab = p["label"]
            pid = f"{doi_pretty}#F{fi}{lab if lab != 'single' else ''}"
            crop = p.get("crop")
            o = ocr.get(crop) if crop else None
            if o and o.get("letter"):
                letter = f"letter {o['letter']} ({'ocr agrees' if o.get('letter_agrees') else 'OCR DISAGREES with detector ' + lab})"
            elif o:
                letter = f"letter {lab} (detector only; ocr read no label)"
            else:
                letter = f"letter {lab} (detector only)"
            cues = []
            if o:
                cues = list(o.get("cues") or [])
                sc = SCALE_RX.search(" ".join(t["text"] for t in o.get("tokens") or []))
                if sc:
                    cues.append(f"scale bar {sc.group(0)}")
            L.append(f"  {pid}  crop {crop or '(whole figure)'}  {letter}")
            L.append(f"     definition: \"{clip(p.get('definition'), 200)}\"   use: {len(p.get('use') or [])} sentences"
                     + (f"   cues: {', '.join(cues)}" if cues else ""))
            if o and o.get("tokens"):
                labels = [t["text"] for t in o["tokens"][:6]]
                L.append(f"     image_labels: {labels}")
    with open(pkt, "a") as fh:
        fh.write("\n".join(L) + "\n")
    stats.append({"doi": r["doi"], "rank": r["rank"], "panels_offered": offered, "ocr_present": bool(ocr),
                  "figures": len(match.get("figures", [])),
                  "tier_C_figures": sum(1 for f in match["figures"] if f["tier"] == "C")})

json.dump(stats, open(pk.parent / "panel_sections.json", "w"), indent=1)
print(f"appended panel sections to {len(stats)} packets; "
      f"{sum(s['ocr_present'] for s in stats)} with OCR; "
      f"{sum(s['panels_offered'] for s in stats)} panels offered in total")
