"""necessity_v3.py: hop-level necessity by removal.

  python3 trace_kit_v3/necessity_v3.py prompts
  python3 trace_kit_v3/necessity_v3.py score

For each step in each chain, withhold that step's evidence and ask again. The step's evidence is
necessary if the chain's ruling weakens without it -- strictly weaker, not merely different, which
is the rule v2 arrived at after a first version that could only fire "from warranted" and so could
never fire on a chain that started partial.

The step itself stays in the prompt, so the model is told what the paper concluded at that point
and simply has nothing to check it against. That isolates the evidence rather than the step.

Every verdict is model against model.
"""
import json, os, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v2'))
import leakguard as LG
from cut_traces import store_for, fig_preamble, unmath
from gate_v3 import ASK, caption
from score_v3 import parse, RANK


def prompt_without(ch, drop):
    st = store_for(os.path.join(ROOT, ch['graph']))
    forb = LG.terms(*[s['effect_text'] for s in ch['steps']],
                    *[o for s in ch['steps'] for o in s['observations'] if o])
    L = [f"Setting: {ch['setup']}", "",
         "A chain of steps. For each, judge whether the evidence given warrants that step.",
         "The steps are in the paper's own order.", ""]
    imgs = []
    for i, s in enumerate(ch['steps'], 1):
        head = (f"- Step {i} [{s['stage_type']}]: from "
                f"{'the previous step&apos;s result' if i > 1 else 'the starting material and processing'}"
                f", the paper concludes: {s['effect_text']}")
        head = head.replace('&apos;', "'")
        if s.get('link_from_previous'):
            head += f"  (linked to the previous step by: {s['link_from_previous']})"
        L.append(head)
        if i == drop:
            L.append("    evidence — withheld for this step: nothing is provided to check it against.")
            continue
        if s['delivery'] == 'oracle':
            L.append(f"    evidence — {s['technique']}, tool result: {LG.measurement(s['observation'])}")
        else:
            ps = [p for p in s['panels'] if p.get('png')]
            caps = '; '.join(caption(st, p, forb) for p in s['panels']) or '(no caption)'
            L.append(f"    evidence — {s['technique']}, panels "
                     f"{', '.join(p['suffix'] for p in ps)}: {caps}")
            imgs += [os.path.join(ROOT, 'results/v3/traces', ch['case'], p['png']) for p in ps]
    L += ["", ASK]
    t = "\n".join(L)
    if imgs: t += "\n\nImages (read each with Read):\n" + "\n".join(imgs)
    return t


def prompts():
    jobs = []
    for cj in sorted(glob.glob(os.path.join(ROOT, 'results/v3/traces/*/case.json'))):
        ch = json.load(open(cj)); d = os.path.dirname(cj)
        nd = os.path.join(d, 'necessity'); os.makedirs(nd, exist_ok=True)
        for k in range(1, len(ch['steps']) + 1):
            p = os.path.join(nd, f'drop{k}.txt')
            open(p, 'w').write(prompt_without(ch, k))
            jobs.append({'id': f"{ch['case']}/drop{k}", 'agent': 'net-fullarm',
                         'prompt': os.path.abspath(p),
                         'out': os.path.abspath(os.path.join(nd, f'drop{k}.out.txt'))})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v3nec.json'), 'w'), indent=1)
    print(f"{len(jobs)} removal prompts over "
          f"{len(glob.glob(os.path.join(ROOT, 'results/v3/traces/*/case.json')))} chains")


def score():
    gs = json.load(open(os.path.join(ROOT, 'results/v3/gate_scores.json')))
    base = {c['case']: c for c in gs['cases']}
    rows = []
    for cj in sorted(glob.glob(os.path.join(ROOT, 'results/v3/traces/*/case.json'))):
        ch = json.load(open(cj)); d = os.path.dirname(cj)
        full = base.get(ch['case'], {}).get('arms', {}).get('full', {})
        fcl = full.get('closing')
        for k in range(1, len(ch['steps']) + 1):
            f = os.path.join(d, 'necessity', f'drop{k}.out.txt')
            if not os.path.exists(f): continue
            st, cl, how = parse(open(f).read(), len(ch['steps']))
            weaker = (RANK.get(cl, 1) < RANK.get(fcl, 1)) if (cl and fcl) else None
            rows.append({'case': ch['case'], 'step': k, 'hop': ch['steps'][k - 1]['hop'],
                         'technique': ch['steps'][k - 1]['technique'],
                         'delivery': ch['steps'][k - 1]['delivery'],
                         'full_closing': fcl, 'without_closing': cl,
                         'step_level_without': st.get(k), 'necessary': weaker, 'parsed': how})
    json.dump({'rows': rows, 'rule': 'necessary = the closing ruling is strictly weaker without it',
               'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v3/necessity.json'), 'w'), indent=1)
    n = sum(1 for r in rows if r['necessary'])
    print(f"{len(rows)} removals, {n} necessary\n")
    print(f"{'case':24s} {'step':>4s} {'hop':>4s} {'technique':22s} {'full':>16s} {'without':>16s}  nec")
    for r in rows:
        print(f"{r['case'][:24]:24s} {r['step']:4d} {r['hop']:>4s} {str(r['technique'])[:22]:22s} "
              f"{str(r['full_closing'])[:16]:>16s} {str(r['without_closing'])[:16]:>16s}  "
              f"{'YES' if r['necessary'] else ('no' if r['necessary'] is False else '?')}")
    by = collections.Counter(r['delivery'] for r in rows if r['necessary'])
    print(f"\nnecessary by delivery: {dict(by)}")


if __name__ == '__main__': {'prompts': prompts, 'score': score}[sys.argv[1]]()
