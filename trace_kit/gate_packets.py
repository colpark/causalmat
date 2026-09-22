"""gate_packets.py: solving-gate packets for written v2.2 traces that pass the structural nets.

  python gate_packets.py <paper> <written.json> <validation.json> <out_dir> [<graph.json>]   (default graphs_v06b)
One JSON per trace: the full-arm prompt (context, condition labels, panel captions, question, image paths),
the floor prompt (the same text, no images) and, kept apart, the key with answer_scope for the grader.
Images are the masked crops where the cutter masked a panel, else the panel crop, else the whole figure.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from cut_traces import store_for, panel_record, unmath, fig_preamble

def main(paper, written, validation, out_dir, gp=None):
    gp = gp or os.path.join(HERE, '..', 'taxonomy', 'graphs_v06b', paper + '.json'); g = json.load(open(gp))
    N = {n['id']: n for n in g['nodes']}; st = store_for(gp)
    val = {v['id']: v for v in json.load(open(validation))}
    os.makedirs(out_dir, exist_ok=True); n = 0
    for t in json.load(open(written))['traces']:
        v = val.get(t['id'], {})
        if t['status'] != 'open' or v.get('fails'): continue
        hid = set(t.get('hidden', []))
        ctx = "\n".join(f"- {N[s['node']]['label']}" for s in t['walk'] if s['node'] not in hid and s['role'] != 'redacted')
        masked = {m['panel']: m['masked_crop'] for m in t.get('masked_panels') or []}
        labels = {l['panel']: l.get('text') for l in t.get('condition_labels') or [] if not l.get('withheld')}
        lines, imgs = [], []
        for pid in t.get('given_panels') or []:
            r = panel_record(st, pid) or {}
            cap = " ".join(unmath(r.get('span') or '').split())
            pre = " ".join(unmath(fig_preamble(st, pid) or '').split())
            lines.append(f"- {pid.split('#')[1]}: caption: {pre}{' ... ' + cap if cap and cap not in pre else ''}" + (f" | condition: {labels[pid]}" if labels.get(pid) else ''))
            img = masked.get(pid) or r.get('crop') or r.get('figure')
            imgs.append(os.path.abspath(os.path.join(HERE, '..', img)) if not os.path.isabs(img) else os.path.abspath(img))
        fmt = ("\n" + t['answer_format']) if t.get('answer_format') else ''
        text = f"Context from a materials paper:\n{ctx}\n\nPanels:\n" + "\n".join(lines) + f"\n\nQuestion: {t['question']}{fmt}"
        pk = {'paper': paper, 'trace': t['id'], 'root': t['root'], 'subtype': t['subtype'], 'v1_filter': t.get('v1_filter'),
              'fullarm': text + "\n\nImages (read each with Read):\n" + "\n".join(imgs) + "\nAnswer in at most six sentences.",
              'floor': text + "\nAnswer in at most five sentences.", 'images': imgs,
              'key': {'answer_key': t['answer_key'], 'answer_scope': t.get('answer_scope', 'full'), 'grading': t['grading'], 'answer_key_nodes': t.get('answer_key_nodes')}}
        json.dump(pk, open(os.path.join(out_dir, f"{t['id']}.gate.json"), 'w'), indent=1); n += 1
    print(paper, n, 'gate packets')

if __name__ == '__main__': main(*sys.argv[1:6])
