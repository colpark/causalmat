"""Select papers for a sweep round and write one compact markdown packet per paper.

Usage: .venv/bin/python taxonomy/build_packets.py <round> <n_papers> [seed]
Papers are stratified over journals, exclude ones used in earlier rounds, and need >= 3 figures and >= 2 mechanisms.
"""
import glob
import json
import os
import random
import sys

ROOT = os.path.abspath("matmech")
TAX = os.path.abspath("taxonomy")
rnd, n = int(sys.argv[1]), int(sys.argv[2])
seed = int(sys.argv[3]) if len(sys.argv) > 3 else rnd
rng = random.Random(seed)

used = set()
for f in glob.glob(f"{TAX}/rounds/*/papers.txt"):
    used |= set(open(f).read().split())

by_j = {}
for f in sorted(glob.glob(f"{ROOT}/*/*/data.json")):
    pid = os.path.relpath(os.path.dirname(f), ROOT)
    if pid not in used:
        by_j.setdefault(pid.split("/")[0], []).append(pid)
for v in by_j.values():
    rng.shuffle(v)

picked, journals = [], sorted(by_j)
while len(picked) < n:
    rng.shuffle(journals)
    for j in journals:
        while by_j[j]:
            pid = by_j[j].pop()
            d = json.load(open(f"{ROOT}/{pid}/data.json"))
            if len(d.get("image_info") or []) >= 3 and len(d.get("mechanism") or []) >= 2:
                picked.append(pid)
                break
        if len(picked) == n:
            break

out = f"{TAX}/rounds/r{rnd:02d}"
os.makedirs(f"{out}/packets", exist_ok=True)
os.makedirs(f"{out}/graphs", exist_ok=True)
open(f"{out}/papers.txt", "w").write("\n".join(picked) + "\n")


def clip(s, k):
    s = " ".join((s or "").split())
    return s if len(s) <= k else s[:k] + " …"


for pid in picked:
    d = json.load(open(f"{ROOT}/{pid}/data.json"))
    L = [f"# {d.get('title')}", f"- paper_id: `{pid}`", f"- doi: {d.get('doi')}  year: {d.get('year')}",
         f"- material: {d.get('material_object')}  elements: {d.get('material_element')}  category: {d.get('material_category')}",
         f"- MST chain: {d.get('casual_chain')}", "## Tetrahedron elements"]
    for k, v in (d.get("tetrahedron_element") or {}).items():
        L.append(f"- **{k}**: {v}")
    fid = {os.path.basename(im.get("image_path") or ""): f"F{i}" for i, im in enumerate(d.get("image_info") or [], 1)}
    L.append("## Figures (in paper order). Open an image with the Read tool on its absolute path.")
    for i, im in enumerate(d.get("image_info") or [], 1):
        L += [f"### F{i}  [{im.get('image_function')}; microscopic={im.get('microscopic_image')}]",
              f"- path: {ROOT}/{pid}/{im.get('image_path')}",
              f"- caption: {clip(' '.join(im.get('image_caption') or []), 700)}",
              f"- linked text: {clip(' '.join(im.get('image_description') or []), 1800)}"]
    L.append("## Extracted mechanisms (MatMech)")
    for i, m in enumerate(d.get("mechanism") or [], 1):
        e = m.get("experiment") or {}
        L += [f"### M{i}  {m.get('link')}", f"- cause: {m.get('cause')}", f"- effect: {m.get('effect')}",
              f"- experiment: {e.get('name')} | {e.get('type')} | params: {clip(e.get('parameters'), 300)} | result: {clip(e.get('result'), 400)}",
              f"- figures: {[fid.get(os.path.basename(x.get('image_path') or ''), '?') for x in m.get('images') or []]}"]
        for s in (m.get("mechanism") or {}).get("reasoning_chain") or []:
            L.append(f"  - [{s.get('type')}] {s.get('statement')}")
    open(f"{out}/packets/{pid.replace('/', '__')}.md", "w").write("\n".join(L) + "\n")

print(out, len(picked))
print("\n".join(picked))
