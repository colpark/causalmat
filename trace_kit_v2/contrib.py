"""contrib.py: the claim-contribution label over the chains' steps.

  python3 trace_kit_v2/contrib.py prompts   build one net-contrib prompt per step
  python3 trace_kit_v2/contrib.py collect   harvested replies -> results/v2/contrib_labels.jsonl
  python3 trace_kit_v2/contrib.py cross     results/v2/contrib_vs_image_support.md

The prompt carries the claim text, one observation text and the relation, and nothing else.
guard() enforces that before anything is dispatched: stop rule 3 of the brief.
"""
import json, os, re, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IN = os.path.join(ROOT, '.v07work/contrib_inputs.jsonl')
WORK = os.path.join(ROOT, '.v07work/contrib')
LAB = os.path.join(ROOT, 'results/v2/contrib_labels.jsonl')
MAP = {'establishes': 'shown', 'supports_part': 'partial',
       'cuts_against': 'contradicts', 'not_addressed': 'not addressed'}
BANNED = re.compile(r'\b(panel|figure|crop|F\d+[a-z]?\b|image|question|answer|arm|shown|partial|'
                    r'not addressed|contradicts|image_support|gate|png|jpg)\b', re.I)


def rows(): return [json.loads(l) for l in open(IN)]


PANEL = re.compile(r'\b(?:in|from|on|of)\s+F\d+[a-z]?(?:\s*[,/and]+\s*F\d+[a-z]?)*\b[,:]?\s*', re.I)
PANEL2 = re.compile(r'\bF\d+[a-z]?\b')


def scrub(o):
    """the label judges what an observation settles, not which panel it came from. Panel references
    are provenance, and naming one would tell the label it is looking at figure evidence."""
    t = PANEL.sub('', o or '')
    t = PANEL2.sub('the data', t)
    return ' '.join(t.split()).strip().lstrip(',;').strip()


def text(r):
    return (f"Claim: {r['claim_text']}\n\n"
            f"Observation: {scrub(r['observation'])}\n\n"
            f"Relation: the observation {r['relation']} the claim.")


def guard(t):
    """stop rule 3: the label must never see a panel, a question or anyone's answer"""
    return sorted({m.group(0).lower() for m in BANNED.finditer(t)})


def prompts():
    os.makedirs(WORK, exist_ok=True)
    jobs, leaks = [], []
    for r in rows():
        t = text(r)
        bad = guard(t)
        if bad: leaks.append((r['case'], r['step'], bad))
        p = os.path.join(WORK, f"{r['case']}.{r['step']}.txt"); open(p, 'w').write(t)
        jobs.append({'id': f"{r['case']}/{r['step']}/contrib", 'agent': 'net-contrib',
                     'prompt': p, 'out': os.path.join(WORK, f"{r['case']}.{r['step']}.out.txt")})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_contrib.json'), 'w'), indent=1)
    json.dump({'papers': ['v2'], 'stage': 'contrib'}, open(os.path.join(ROOT, '.v07work/batch_contrib.meta.json'), 'w'), indent=1)
    print(f"{len(jobs)} net-contrib prompts")
    if leaks:
        print("LEAK: a prompt mentions something the label must not see:")
        for c, s, b in leaks: print(f"   {c} step {s}: {b}")
        print("Refusing to dispatch. Fix the observation text or the guard.")
        sys.exit(2)
    print("guard: no prompt mentions a panel, figure, image, question, answer or support level")


def parse(t):
    m = re.search(r'\{.*\}', t or '', re.S)
    if not m: return None
    try: return json.loads(m.group(0))
    except Exception: return None


def collect():
    out = []
    for r in rows():
        f = os.path.join(WORK, f"{r['case']}.{r['step']}.out.txt")
        j = parse(open(f).read()) if os.path.exists(f) else None
        if not j: print('UNPARSED', r['case'], r['step']); continue
        c = (j.get('contribution') or '').strip().lower().replace(' ', '_')
        out.append({**{k: r[k] for k in ('case', 'paper', 'claim_id', 'step', 'node', 'relation',
                                         'technique', 'image_support', 'claim_text', 'observation')},
                    'observation_as_labelled': scrub(r['observation']),
                    'contribution': c, 'mapped_support': MAP.get(c),
                    'why': j.get('why'), 'unsettled': j.get('unsettled') or []})
    with open(LAB, 'w') as f:
        for o in out: f.write(json.dumps(o) + '\n')
    print(f"{len(out)}/21 labels -> {os.path.relpath(LAB, ROOT)}")
    import collections
    print(dict(collections.Counter(o['contribution'] for o in out)))


if __name__ == '__main__': {'prompts': prompts, 'collect': collect}[sys.argv[1]]()
