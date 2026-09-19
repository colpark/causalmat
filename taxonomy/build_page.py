"""Build the case-graph page: python taxonomy/build_page.py <vocab.json> <out.html> <graph.json> [graph.json ...]

Embeds each graph, its referenced figures (base64) and the vocabulary; the browser lays graphs out with dagre.
"""
import base64
import json
import os
import re
import sys

TAX = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(os.path.dirname(TAX), "matmech")
vocab_path, out, graph_paths = sys.argv[1], sys.argv[2], sys.argv[3:]
vocab = json.load(open(vocab_path))
metrics = [json.loads(l) for l in open(f"{TAX}/metrics.jsonl")]

cases = []
for gp in graph_paths:
    g = json.load(open(gp))
    pid = g["paper_id"]
    d = json.load(open(f"{ROOT}/{pid}/data.json"))
    figs = {}
    for i, im in enumerate(d.get("image_info") or [], 1):
        figs[f"F{i}"] = (im, os.path.join(ROOT, pid, im["image_path"]))
    used = sorted({f for n in g["nodes"] for f in (n.get("figs") or [])}, key=lambda s: int(re.sub(r"\D", "", s) or 0))
    fig_data = {}
    for f in used:
        if f in figs and os.path.exists(figs[f][1]):
            b = base64.b64encode(open(figs[f][1], "rb").read()).decode()
            cap = " ".join(figs[f][0].get("image_caption") or [])
            fig_data[f] = {"src": "data:image/jpeg;base64," + b, "caption": re.sub(r"\$[^$]*\$", "", cap)[:400]}
    cases.append({"paper_id": pid, "title": d.get("title"), "doi": d.get("doi"), "year": d.get("year"),
                  "material": d.get("material_object"), "chain": d.get("casual_chain"),
                  "graph": g, "figs": fig_data})

tpl = open(f"{TAX}/page_template.html").read()
data = {"vocab": vocab, "metrics": metrics, "cases": cases}
html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
open(out, "w").write(html)
print(out, f"{os.path.getsize(out) / 1e6:.2f} MB", [c["paper_id"] for c in cases])
