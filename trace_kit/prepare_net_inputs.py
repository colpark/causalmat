"""prepare_net_inputs.py: write one packet per (trace, net). A packet holds exactly what the subagent may see.

  python prepare_net_inputs.py --graph G.json --traces traces.json --panels-dir <doi_folder> --out nets/<paper>

Writes
  nets/<paper>/<trace>.floor.json, .floor_masked.json, .reread.<panel>.json, .fullarm.json, .judge.json
  nets/<paper>/_keys.json          answer keys, kept OUT of the packet files; only the grader step reads it
Each packet: {"net", "trace", "system", "user", "images": [paths]}   (images empty for text nets)
"""
import argparse, json, os, re

MASK_TERMS = [r"ZrB2", r"ZrSi2", r"SiC", r"B4C", r"WSi2", r"ZrC", r"ZrO2", r"RZSZ-?\d*"]


def mask(text):
    for i, t in enumerate(MASK_TERMS): text = re.sub(t, f"MATERIAL_{chr(65 + i)}", text)
    return text


def crop_for(panels_dir, pid):
    """resolve a canonical panel id to a crop path via panels.json; returns None if absent."""
    pj_path = os.path.join(panels_dir, "panels", "panels.json")
    if not os.path.exists(pj_path): return None
    pj = json.load(open(pj_path))
    fig_no = re.sub(r"[a-z].*$", "", pid.split("#F")[1]); letter = re.sub(r"^\d+", "", pid.split("#F")[1]).upper()
    for fig in pj["figures"]:
        if not re.search(rf"fig{fig_no}\.(jpg|png|jpeg)$", fig["file"]): continue
        for d in fig.get("detections", []):
            if d.get("panel_id") == pid or (letter and d.get("label", "").upper() == letter):
                p = os.path.join(panels_dir, d.get("crop", "")); return p if d.get("crop") else None
        if not letter: return os.path.join(panels_dir, fig["file"])  # whole single figure
    return None


def given_text(N, t, masked=False):
    hid = set(t.get("hidden", []))
    lines = [f"- {N[s['node']]['label']}" for s in t["walk"] if s["node"] not in hid and s["role"] != "redacted"]
    txt = "\n".join(lines); q = t["question"]
    if masked: txt, q = mask(txt), mask(q)
    return txt, q


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", required=True); ap.add_argument("--traces", required=True)
    ap.add_argument("--panels-dir", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    g = json.load(open(a.graph)); N = {n["id"]: n for n in g["nodes"]}; T = json.load(open(a.traces))
    os.makedirs(a.out, exist_ok=True)
    keys, n_pk, unresolved = {}, 0, []
    for t in T["traces"]:
        if t["status"] == "closed": continue
        tid = t["id"]; keys[tid] = {"answer_key": t["answer_key"], "answer_key_fallback": t.get("answer_key_fallback"), "grading": t["grading"],
                                   "observations": {e: N[e]["label"] for e in t["evidence"]}}
        def write(name, system, user, images=()):
            nonlocal n_pk
            json.dump({"net": name.split(".")[0], "trace": tid, "system": system, "user": user, "images": list(images)},
                      open(os.path.join(a.out, f"{tid}.{name}.json"), "w"), indent=1); n_pk += 1
        # floor, twice
        for variant in ("floor", "floor_masked"):
            txt, q = given_text(N, t, masked=(variant == "floor_masked"))
            write(variant, "You answer from the provided text only. You have no images and no tools. If the text does not settle the question, reply exactly: CANNOT DETERMINE.",
                  f"Context from a materials paper:\n{txt}\n\nQuestion: {q}\nAnswer in at most five sentences.")
        # reread, one per cited panel
        for ev in t["evidence"]:
            for pid in N[ev].get("panel_ids", []):
                p = crop_for(a.panels_dir, pid)
                if not p or not os.path.exists(p): unresolved.append({"trace": tid, "panel": pid}); continue
                write(f"reread.{pid.split('#')[1]}", "Describe exactly what this scientific figure panel shows: technique, features, scale bar, trends. Read the image only; do not guess the paper.",
                      "Describe the panel in at most six sentences.", [p])
        # fullarm
        txt, q = given_text(N, t)
        withheld = set(t.get("hidden_panels", []))
        imgs = [crop_for(a.panels_dir, pid) for ev in t["evidence"] for pid in N[ev].get("panel_ids", []) if pid not in withheld]
        imgs = [p for p in imgs if p and os.path.exists(p)]
        write("fullarm", "You may use the images and the text. You have no other tools. If the images do not settle the question, reply exactly: CANNOT DETERMINE.",
              f"Context from a materials paper:\n{txt}\n\nQuestion: {q}\nThe images are the cited panels. Answer in at most six sentences.", imgs)
        # judge
        steps = "\n".join(f"{s['step']}. [{s['role']}{' HIDDEN' if s['hidden'] else ''}] (nodes {', '.join(s['nodes'])}) {s['text']}" for s in t["linear"])
        nodes = "\n".join(f"{i}: {N[i]['label']}" for s in t["linear"] for i in s["nodes"] if i in N)
        write("judge", "You are a strict reviewer of a reasoning trace. Reply with JSON only: {\"steps_follow\": [true/false per step], \"answerable_from_given\": true/false, \"issues\": [\"...\"]}",
              f"Question: {t['question']}\n\nSteps:\n{steps}\n\nNode texts:\n{nodes}\n\nFor each step: does its text follow from its cited nodes? Is the question answerable from the non-hidden steps plus the images those steps cite?")
    json.dump(keys, open(os.path.join(a.out, "_keys.json"), "w"), indent=1)
    json.dump(unresolved, open(os.path.join(a.out, "_unresolved_panels.json"), "w"), indent=1)
    print(f"wrote {n_pk} packets to {a.out}; unresolved panels: {len(unresolved)}")


if __name__ == "__main__":
    main()
