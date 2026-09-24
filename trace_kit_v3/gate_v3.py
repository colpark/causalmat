"""gate_v3.py: four arms and one control for a hop chain.

  python3 trace_kit_v3/gate_v3.py prompts <case_dir>
  python3 trace_kit_v3/gate_v3.py score   <case_dir>

v2 asked "does this evidence support the claim?". v3 asks, for each **hop**, whether the evidence
warrants the step from the previous hop's effect to this one's. The hop is the step.

Arms:
  full             crops for FM-lane steps, plain-text tool results for oracle steps
  floor            captions only: no images and no measurements
  oracle_complete  every step served as a plain-text tool result
  reordered        the full evidence, but the steps out of the paper's order and with the link
                   sentences removed. If the chain's order carries nothing, this scores like `full`.
Control:
  permute_image    this chain, another case's panels, so the pictures are certainly wrong

MatMech's cause and effect spans never appear. Every word here is our own claim text.

Every verdict is model against model.
"""
import json, os, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v2'))
import leakguard as LG
from cut_traces import store_for, fig_preamble, unmath

SCALE = "warrants, partly warrants, does not address, or contradicts"
ASK = (f"For each step say one of: {SCALE}, and one sentence of why. "
       "Then close with whether the chain as a whole is warranted and what is still missing. "
       "Partial rulings are expected; do not force a yes or no.\n"
       "Reply as JSON only: {\"steps\": [{\"step\": 1, \"level\": \"...\", \"why\": \"...\"}], "
       "\"closing\": {\"level\": \"...\", \"missing\": \"...\"}}")


def caption(st, p, forbidden):
    pre = ' '.join(unmath(fig_preamble(st, p['panel_id']) or '').split())
    return LG.caption_for(p['caption_span'], pre, forbidden) or pre or ''


def prompt(ch, arm, images_from=None):
    st = store_for(os.path.join(ROOT, ch['graph']))
    forb = LG.terms(*[s['effect_text'] for s in ch['steps']],
                    *[o for s in ch['steps'] for o in s['observations'] if o])
    steps = list(ch['steps'])
    if arm == 'reordered': steps = list(reversed(steps))
    L = [f"Setting: {ch['setup']}", "",
         "A chain of steps. For each, judge whether the evidence given warrants that step."]
    if arm != 'reordered':
        L.append("The steps are in the paper's own order.")
    L.append("")
    imgs = []
    for i, s in enumerate(steps):
        prior = ("the previous step's result" if i else "the starting material and processing")
        head = (f"- Step {i + 1} [{s['stage_type']}]: from {prior}, the paper concludes: "
                f"{s['effect_text']}")
        if arm != 'reordered' and s.get('link_from_previous'):
            head += f"  (linked to the previous step by: {s['link_from_previous']})"
        L.append(head)
        if s['delivery'] == 'oracle' or arm in ('floor', 'oracle_complete'):
            if arm == 'floor':
                caps = '; '.join(caption(st, p, forb) for p in s['panels']) or '(no caption)'
                L.append(f"    evidence — {s['technique']}, panel caption only: {caps}")
            else:
                L.append(f"    evidence — {s['technique']}, tool result: "
                         f"{LG.measurement(s['observation'])}")
        else:
            use = images_from['steps'][i % len(images_from['steps'])] if images_from else s
            ps = [p for p in use['panels'] if p.get('png')]
            caps = '; '.join(caption(st, p, forb) for p in s['panels']) or '(no caption)'
            L.append(f"    evidence — {s['technique']}, panels "
                     f"{', '.join(p['suffix'] for p in ps)}: {caps}")
            base = images_from if images_from else ch
            imgs += [os.path.join(ROOT, 'results/v3/traces', base['case'], p['png']) for p in ps]
    L += ["", ASK]
    text = "\n".join(L)
    if imgs and arm not in ('floor', 'oracle_complete'):
        text += "\n\nImages (read each with Read):\n" + "\n".join(imgs)
    return text, imgs


def main(cmd, case_dir):
    ch = json.load(open(os.path.join(case_dir, 'case.json')))
    gd = os.path.join(case_dir, 'gate'); os.makedirs(gd, exist_ok=True)
    others = [json.load(open(f)) for f in
              sorted(glob.glob(os.path.join(ROOT, 'results/v3/traces/*/case.json')))
              if json.load(open(f))['case'] != ch['case']]
    plan = [('full', None), ('floor', None), ('oracle_complete', None), ('reordered', None)]
    if others: plan += [('permute_image', others[0])]
    jobs = []
    for arm, imf in plan:
        t, _ = prompt(ch, arm, imf)
        p = os.path.join(gd, f'{arm}.txt'); open(p, 'w').write(t)
        jobs.append({'id': f"{ch['case']}/{arm}", 'prompt': p,
                     'agent': 'net-floor' if arm in ('floor', 'oracle_complete') else 'net-fullarm',
                     'out': os.path.join(gd, f'{arm}.out.txt')})
    json.dump(jobs, open(os.path.join(case_dir, 'jobs_gate.json'), 'w'), indent=1)
    print(f"{ch['case']}: {len(jobs)} prompts, {len(ch['steps'])} steps")


if __name__ == '__main__': main(sys.argv[1], sys.argv[2])
