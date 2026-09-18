"""Mechanical text-only floor for two MatMech task templates (skill stages P2/I1, zero model calls).

The BioReason-KEGG lesson: a text lookup reached ~97% of the task before any FM ran. This measures the
same thing here with TF-IDF cosine and no model:

  T1 mechanism selection  query = cause + effect         candidates = mechanism descriptions (1 true + 4 rivals)
  T2 effect prediction    query = cause (+ link type)    candidates = effects (1 true + 4 rivals)

Rivals come from other papers with the same link type, drawn two ways:
  random  uniformly
  hard    the 4 mechanisms whose own query is nearest to this query, which is the rival a mechanical
          composition would itself select (shape.md refusal 13)

One item per paper, so items are independent at the paper level. Chance is 0.2.
Usage: .venv/bin/python scripts/text_floor.py matmech [results/text_floor.json]
"""
import glob
import json
import math
import random
import re
import sys

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else "results/text_floor.json"
N, K, SEED = 3000, 5, 0
MAIN = {"Processing → Structure", "Structure → Property", "Property → Performance",
        "Structure → Performance", "Processing → Performance", "Processing → Property"}

rows = []
for f in glob.glob(f"{ROOT}/*/*/data.json"):
    d = json.load(open(f, encoding="utf-8"))
    for m in d.get("mechanism") or []:
        link = re.sub("Properties", "Property", m.get("link") or "")
        mm = m.get("mechanism") or {}
        conf = mm.get("confidence")
        if link in MAIN and isinstance(conf, (int, float)) and conf >= 0.8 and mm.get("description"):
            rows.append(dict(doi=d["doi"], year=d.get("year"), link=link, cause=m.get("cause") or "",
                             effect=m.get("effect") or "", desc=mm["description"]))
print(f"{len(rows)} mechanisms with confidence >= 0.8 on the six main links")

rng = random.Random(SEED)
by_paper = {}
for i, r in enumerate(rows):
    by_paper.setdefault(r["doi"], []).append(i)
items = [rng.choice(v) for v in by_paper.values()]
rng.shuffle(items)
items = items[:N]
by_link = {}
for i, r in enumerate(rows):
    by_link.setdefault(r["link"], []).append(i)

vec = TfidfVectorizer(sublinear_tf=True, min_df=2, stop_words="english", ngram_range=(1, 2), max_features=400000)
vec.fit([r["cause"] + " " + r["effect"] + " " + r["desc"] for r in rows])


def enc(texts):
    return vec.transform(texts)


def run(task, rival_mode):
    if task == "T1":
        qtext = [rows[i]["cause"] + " " + rows[i]["effect"] for i in range(len(rows))]
        ctext = [r["desc"] for r in rows]
    else:
        qtext = [rows[i]["link"] + " " + rows[i]["cause"] for i in range(len(rows))]
        ctext = [r["effect"] for r in rows]
    Q = enc([qtext[i] for i in items])
    hits = []
    if rival_mode == "hard":
        allQ = enc(qtext)
    for n, i in enumerate(items):
        pool = by_link[rows[i]["link"]]
        if rival_mode == "random":
            riv = []
            while len(riv) < K - 1:
                j = rng.choice(pool)
                if rows[j]["doi"] != rows[i]["doi"] and j not in riv:
                    riv.append(j)
        else:
            sims = (allQ[pool] @ Q[n].T).toarray().ravel()
            order = np.argsort(-sims)
            riv = [pool[o] for o in order if rows[pool[o]]["doi"] != rows[i]["doi"]][:K - 1]
        cands = [i] + riv
        C = enc([ctext[c] for c in cands])
        score = (C @ Q[n].T).toarray().ravel()
        hits.append(int(np.argmax(score) == 0))
    p = sum(hits) / len(hits)
    half = 1.96 * math.sqrt(p * (1 - p) / len(hits))
    return dict(task=task, rivals=rival_mode, n=len(hits), accuracy=round(p, 4),
                ci95=[round(p - half, 4), round(p + half, 4)], chance=1 / K)


res = [run(t, m) for t in ("T1", "T2") for m in ("random", "hard")]
out = dict(source="scripts/text_floor.py", seed=SEED, n_mechanisms=len(rows), n_papers=len(by_paper),
           items_one_per_paper=len(items), k=K, results=res)
json.dump(out, open(OUT, "w"), indent=1)
print(json.dumps(res, indent=1))
