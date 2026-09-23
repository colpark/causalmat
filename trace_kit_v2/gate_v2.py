"""gate_v2.py: the three arms and the three alignment controls for one support chain.

  python3 trace_kit_v2/gate_v2.py prompts <case_dir>     build every arm and control prompt
  python3 trace_kit_v2/gate_v2.py score   <case_dir>     grade the replies per step and for the close

Arms (plan sections 4 and 6):
  full             crops for FM-lane steps, plain-text tool results for oracle steps
  floor            every step as text, no images, and no measurement either: captions only
  oracle_complete  every step served as a plain-text tool result -- the generalized floor
Controls:
  permute_answer   the chain of another case, this case's images
  permute_image    this case's chain, another case's images, across task types so it is certainly wrong
  no_image         this case's chain with the images removed
"""
import json, os, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
import leakguard as LG
from cut_traces import store_for, fig_preamble, unmath

SCALE = "shown, partial, not addressed, or contradicts"
ASK = (f"For each step say one of: {SCALE}, and one sentence of why. "
       "Then close with the overall support level for the claim and what is still missing. "
       "Partial rulings are expected; do not force a yes or no.\n"
       "Reply as JSON only: {\"steps\": [{\"step\": 1, \"level\": \"...\", \"why\": \"...\"}], "
       "\"closing\": {\"level\": \"...\", \"missing\": \"...\"}}")


def caption(st, p, forbidden):
    pre = ' '.join(unmath(fig_preamble(st, p['panel_id']) or '').split())
    return LG.caption_for(p['caption_span'], pre, forbidden) or pre or ''


def prompt(ch, arm, images_from=None, chain_from=None):
    src = chain_from or ch
    st = store_for(os.path.join(ROOT, src['graph']))
    forb = LG.terms(src['claim_text'], *[s['observation'] for s in src['steps']])
    L = [f"Claim under test: {src['claim_text']}", "",
         "Evidence, in the paper's own argument order:"]
    imgs = []
    img_ch = images_from or ch
    for i, s in enumerate(src['steps']):
        head = f"- Step {s['step']}: {s['technique']}"
        if s['delivery'] == 'oracle' or arm in ('floor', 'oracle_complete'):
            if arm == 'floor':
                caps = '; '.join(caption(st, p, forb) for p in s['panels']) or '(no caption)'
                L.append(f"{head} — panel caption only: {caps}")
            else:
                L.append(f"{head} — tool result: {LG.measurement(s['observation'])}")
        else:
            use = img_ch['steps'][i % len(img_ch['steps'])] if images_from else s
            ps = [p for p in use['panels'] if p.get('png')]
            caps = '; '.join(caption(st, p, forb) for p in s['panels']) or '(no caption)'
            L.append(f"{head} — panels {', '.join(p['suffix'] for p in ps)}: {caps}")
            imgs += [os.path.join(ROOT, 'results/v2/cases', img_ch['paper'], img_ch['claim'], p['png']) for p in ps]
    L += ["", ASK]
    text = "\n".join(L)
    if imgs and arm not in ('floor', 'oracle_complete', 'no_image'):
        text += "\n\nImages (read each with Read):\n" + "\n".join(imgs)
    return text, imgs


def main(cmd, case_dir):
    ch = json.load(open(os.path.join(case_dir, 'case.json')))
    gd = os.path.join(case_dir, 'gate'); os.makedirs(gd, exist_ok=True)
    others = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(ROOT, 'results/v2/cases/*/*/case.json')))
              if json.load(open(f))['case'] != ch['case']]
    jobs = []
    plan = [('full', None, None), ('floor', None, None), ('oracle_complete', None, None), ('no_image', None, None)]
    if others:
        plan += [('permute_answer', None, others[0]), ('permute_image', others[0], None)]
    for arm, imf, chf in plan:
        t, _ = prompt(ch, arm, imf, chf)
        p = os.path.join(gd, f'{arm}.txt'); open(p, 'w').write(t)
        jobs.append({'id': f"{ch['case']}/{arm}", 'agent': 'net-floor' if arm in ('floor', 'oracle_complete', 'no_image') else 'net-fullarm',
                     'prompt': p, 'out': os.path.join(gd, f'{arm}.out.txt')})
    json.dump(jobs, open(os.path.join(case_dir, 'jobs_gate.json'), 'w'), indent=1)
    print(f"{ch['case']}: {len(jobs)} arm/control prompts -> {os.path.relpath(gd, ROOT)}")
    for j in jobs: print(f"   {j['id'].split('/')[1]:16s} {j['agent']}")
    if not others: print("   (controls need a second case; re-run after another case exists)")


if __name__ == '__main__': main(sys.argv[1], sys.argv[2])
