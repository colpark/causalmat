"""Checkpoint diff: script-collapsed spec against a hand-built spec, node by node.

Matches nodes across the two specs by (row, lane key, figure set); reports lane, target state,
verdict, necessity and panel set for each match, plus unmatched nodes on either side.

Usage: python taxonomy/diff_specs.py --auto <auto.json> --hand <hand.json>
"""
import argparse
import json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--auto", required=True)
ap.add_argument("--hand", required=True)
a = ap.parse_args()
A, H = json.load(open(a.auto)), json.load(open(a.hand))


def lane_key(spec, n):
    return spec["lanes"][n["lane"]]["key"]


def sig(spec, n):
    return (n["row"], lane_key(spec, n), tuple(sorted(n.get("figs") or [])))


def panels(n):
    p = n.get("panel_ids") or ([n["panel"]] if n.get("panel") else [])
    return tuple(sorted(x for x in p if x))


print(f"auto: {len(A['nodes'])} nodes, lanes {[l['key'] for l in A['lanes']]}, states {[s['id'] for s in A['states']]}")
print(f"hand: {len(H['nodes'])} nodes, lanes {[l['key'] for l in H['lanes']]}, states {[s['id'] for s in H['states']]}")
print()
hand_by_sig = {}
for n in H["nodes"]:
    hand_by_sig.setdefault(sig(H, n), []).append(n)

matched, only_auto = [], []
for n in A["nodes"]:
    s = sig(A, n)
    cands = hand_by_sig.get(s) or hand_by_sig.get((s[0], s[1], ()))
    if cands:
        matched.append((n, cands.pop(0)))
    else:
        only_auto.append(n)
only_hand = [n for v in hand_by_sig.values() for n in v]

fields = ["lane", "row", "verdict", "necessity"]
agree = {f: 0 for f in fields}
agree["panels"] = 0
for n, h in matched:
    print(f"— auto {n['id']} vs hand {h['id']}  row {n['row']}/{h['row']}  lane "
          f"{lane_key(A, n)}/{lane_key(H, h)}  figs {n.get('figs')}/{h.get('figs')}")
    for f in fields:
        av = lane_key(A, n) if f == "lane" else n.get(f)
        hv = lane_key(H, h) if f == "lane" else h.get(f)
        ok = av == hv
        agree[f] += ok
        if not ok:
            print(f"    {f}: auto={av!r}  hand={hv!r}")
    ap_, hp = panels(n), panels(h)
    if ap_ == hp:
        agree["panels"] += 1
    else:
        print(f"    panels: auto={list(ap_)}  hand={list(hp)}")

print()
print(f"matched {len(matched)} of auto {len(A['nodes'])} / hand {len(H['nodes'])}")
for k, v in agree.items():
    print(f"  {k} agrees on {v}/{len(matched)}")
if only_auto:
    print("only in auto:", [(n["id"], n["row"], lane_key(A, n), n.get("figs"), n.get("tech")) for n in only_auto])
if only_hand:
    print("only in hand:", [(n["id"], n["row"], lane_key(H, n), n.get("figs"), n.get("tech")) for n in only_hand])
