"""v3b.py: hide the effect. The step asks what the evidence establishes, not whether it warrants
a conclusion the prompt already stated.

  python3 trace_kit_v3/v3b.py prompts     answer prompts for every arm and removal, 3 repeats
  python3 trace_kit_v3/v3b.py gradejobs   one grader job per answer file
  python3 trace_kit_v3/v3b.py score       grade tallies, arm comparison, stop-rule check

v3's finding was that reordered equalled full and no hop's evidence was necessary. The cause was
the format: every step stated the paper's conclusion, so the model graded an assertion and the
evidence was optional. v3b removes the conclusion from the prompt.

**Naming the property without naming the finding.** The question has to say what the evidence is
about. `attrs.property_family` is set on only 4 of 24 effect claims, so the property is derived from
the claim's `type`, which is a controlled vocabulary: STR/microstructure/porosity becomes "the
porosity and pore structure". A type cannot leak a result; a label would.

**One deviation from the brief, and the reason.** The brief asks for the cause as our upstream claim
text. That works for step 1, whose cause is the setting. For a later step the upstream claim *is the
previous step's hidden effect*, so printing it would hand over the previous step's answer inside the
same prompt. Later steps therefore refer to "the previous step's result" without stating it. The
alternative -- one prompt per step -- would have made `reordered` undefined and broken comparability
with v3.

Every verdict is model against model.
"""
import json, os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit'))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v2'))
import leakguard as LG
from cut_traces import store_for, fig_preamble, unmath

REPEATS = 3
ARMS = ['full', 'floor', 'measurement', 'reordered', 'permute_image']

PROPERTY = {
    'STR/phase/identity':            'which phases are present and what they are',
    'STR/phase/fraction':            'how much of each phase is present',
    'STR/phase/lattice':             'the lattice parameters and how they change',
    'STR/microstructure/feature_size':  'the size of the microstructural features',
    'STR/microstructure/porosity':   'the porosity and pore structure',
    'STR/microstructure/distribution': 'how the microstructural features are distributed',
    'PRP/value':                     'the measured property value',
    'PRF/service_capability':        'how the material performs in service',
    'MEC/pathway':                   'the mechanism connecting the two',
    'MEC/identification':            'the mechanism responsible',
    'DSC/conclusion':                'what the results amount to overall',
}
FAMILY = {'mechanical': 'the mechanical property', 'optical': 'the optical property',
          'kinetic': 'the rate at which it happens',
          'ionic_electrochemical': 'the electrochemical property'}

# interpretive language stripped for the measurement arm: verbs of inference, hedges and
# attributions. Numbers, features and conditions stay.
INTERPRETIVE = [
    r'\bindicat\w+\b', r'\bsuggest\w+\b', r'\bconsistent with\b', r'\bconfirm\w+\b',
    r'\bdemonstrat\w+\b', r'\bshow\w+ that\b', r'\bimpl\w+\b', r'\bevidenc\w+\b',
    r'\battribut\w+ to\b', r'\bassign\w+ to\b', r'\breveal\w+\b',
    # NOT r'\breflect\w+\b': "reflection" is a diffraction peak, a measured feature, not an
    # inference verb. It stripped "one low-angle reflection" down to "one low-angle" -- the
    # stripper was deleting the measurement it was meant to preserve.
    r'\bproving\b', r'\bprov\w+ that\b', r'\bsuppor\w+ the\b', r'\bconsistent\b',
    r'\btherefore\b', r'\bthus\b', r'\bhence\b', r'\bmeaning\b', r'\bi\.e\.\b',
    r'\bwhich means\b', r'\bcharacteristic of\b', r'\btypical of\b', r'\bsignatur\w+ of\b',
]


def prop_of(claims, N):
    out = []
    for c in claims:
        n = N.get(c) or {}
        fam = (n.get('attrs') or {}).get('property_family')
        p = FAMILY.get(fam) if fam else None
        p = p or PROPERTY.get(n.get('type')) or PROPERTY.get(
            '/'.join((n.get('type') or '').split('/')[:2]))
        if p and p not in out: out.append(p)
    return ' and '.join(out) if out else 'what the sample is like'


def strip_interpretive(text):
    """measurement-only: numbers, features and conditions; no interpretive words"""
    t, removed = text or '', []
    for pat in INTERPRETIVE:
        for m in re.finditer(pat, t, re.I):
            if m.group(0) not in removed: removed.append(m.group(0))
        t = re.sub(pat, '', t, flags=re.I)
    t = re.sub(r'\s+([,.;:])', r'\1', t)
    t = re.sub(r'\s{2,}', ' ', t).strip(' ,;:')
    return t, removed


ASK = ("For each step, say what the evidence establishes about the property named, what it does "
       "not establish, and your confidence (high, medium or low).\n"
       "Reply as JSON only: {\"steps\": [{\"step\": 1, \"shows\": \"...\", "
       "\"does_not_show\": \"...\", \"confidence\": \"...\"}]}")


def build(ch, arm, N, images_from=None, drop=None):
    st = store_for(os.path.join(ROOT, ch['graph']))
    forb = LG.terms(*[s['effect_text'] for s in ch['steps']],
                    *[o for s in ch['steps'] for o in s['observations'] if o])
    steps = list(reversed(ch['steps'])) if arm == 'reordered' else list(ch['steps'])
    L = [f"Setting: {ch['setup']}", "",
         "Below are steps in an experimental argument. For each you are given the evidence and the "
         "property it concerns. You are NOT told what the authors concluded.", ""]
    imgs, stripped = [], []
    for i, s in enumerate(steps, 1):
        src = ("the starting material and processing described above" if s['step'] == 1
               else "the previous step's result")
        L.append(f"- Step {i} [{s['stage_type']}]: starting from {src}, the evidence below bears on "
                 f"**{prop_of(s['claims'], N)}**.")
        if drop == s['step']:
            L.append("    evidence — withheld for this step: none is provided.")
            continue
        if arm == 'measurement':
            m, rem = strip_interpretive(LG.measurement(s['observation']))
            stripped += [r for r in rem if r not in stripped]
            L.append(f"    evidence — {s['technique']}, measurement: {m}")
        elif arm == 'floor':
            caps = '; '.join(
                ' '.join(unmath(fig_preamble(st, p['panel_id']) or '').split()) and
                LG.caption_for(p['caption_span'],
                               ' '.join(unmath(fig_preamble(st, p['panel_id']) or '').split()),
                               forb) or '' for p in s['panels']) or '(no caption)'
            L.append(f"    evidence — {s['technique']}, panel caption only: {caps}")
        elif s['delivery'] == 'oracle':
            L.append(f"    evidence — {s['technique']}, tool result: {LG.measurement(s['observation'])}")
        else:
            use = images_from['steps'][(i - 1) % len(images_from['steps'])] if images_from else s
            ps = [p for p in use['panels'] if p.get('png')]
            L.append(f"    evidence — {s['technique']}, panels {', '.join(p['suffix'] for p in ps)}")
            base = images_from if images_from else ch
            imgs += [os.path.join(ROOT, 'results/v3/traces', base['case'], p['png']) for p in ps]
    L += ["", ASK]
    t = "\n".join(L)
    if imgs and arm not in ('floor', 'measurement'): 
        t += "\n\nImages (read each with Read):\n" + "\n".join(imgs)
    return t, stripped


def prompts():
    jobs, allstripped = [], []
    cases = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(ROOT, 'results/v3/traces/*/case.json')))]
    for ch in cases:
        N = {n['id']: n for n in json.load(open(os.path.join(ROOT, ch['graph'])))['nodes']}
        d = os.path.join(ROOT, 'results/v3b', ch['case']); os.makedirs(d, exist_ok=True)
        others = [c for c in cases if c['case'] != ch['case']]
        for arm in ARMS:
            for r in range(1, REPEATS + 1):
                t, strp = build(ch, arm, N, others[0] if arm == 'permute_image' else None)
                allstripped += [x for x in strp if x not in allstripped]
                p = os.path.join(d, f'{arm}.r{r}.txt'); open(p, 'w').write(t)
                jobs.append({'id': f"{ch['case']}/{arm}/r{r}", 'prompt': os.path.abspath(p),
                             'agent': 'net-floor' if arm in ('floor', 'measurement') else 'net-fullarm',
                             'out': os.path.abspath(os.path.join(d, f'{arm}.r{r}.out.txt'))})
        for k in range(1, len(ch['steps']) + 1):
            for r in range(1, REPEATS + 1):
                t, _ = build(ch, 'full', N, None, drop=k)
                p = os.path.join(d, f'drop{k}.r{r}.txt'); open(p, 'w').write(t)
                jobs.append({'id': f"{ch['case']}/drop{k}/r{r}", 'prompt': os.path.abspath(p),
                             'agent': 'net-fullarm',
                             'out': os.path.abspath(os.path.join(d, f'drop{k}.r{r}.out.txt'))})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v3b.json'), 'w'), indent=1)
    json.dump({'stripped_terms': allstripped},
              open(os.path.join(ROOT, 'results/v3b/stripped.json'), 'w'), indent=1)
    print(f"{len(jobs)} answer jobs ({len(cases)} traces x {len(ARMS)} arms x {REPEATS} repeats, "
          f"plus removals)")
    print(f"interpretive terms stripped for the measurement arm: {allstripped}")


GRADE_ASK = (
    "You are grading what a reader concluded from evidence, against what the paper actually "
    "concluded.\n\nFor each step, compare the reader's statement with the answer key and rule one "
    "of: correct, partly correct, wrong, or cannot tell.\n"
    "  correct       the reader reached the key's finding, in their own words\n"
    "  partly correct the reader reached part of it, or reached it with the wrong magnitude, "
    "direction or sample\n"
    "  wrong         the reader reached something the key contradicts\n"
    "  cannot tell   the reader declined to conclude, or said only that the evidence is "
    "insufficient\n\n"
    "Judge the substance, not the wording, and do not reward a statement for merely repeating the "
    "measurement without reaching a finding -- that is `cannot tell`.\n"
    "Reply as JSON only: {\"steps\": [{\"step\": 1, \"verdict\": \"...\", \"why\": \"one sentence\"}]}")


def parse_answer(txt, nsteps):
    m = re.search(r'\{.*\}', txt or '', re.S)
    if not m: return {}
    try: j = json.loads(m.group(0))
    except Exception: return {}
    return {int(s['step']): s for s in j.get('steps', []) if str(s.get('step', '')).isdigit()}


def gradejobs():
    jobs = []
    for cj in sorted(glob.glob(os.path.join(ROOT, 'results/v3/traces/*/case.json'))):
        ch = json.load(open(cj))
        N = {n['id']: n for n in json.load(open(os.path.join(ROOT, ch['graph'])))['nodes']}
        d = os.path.join(ROOT, 'results/v3b', ch['case'])
        gd = os.path.join(d, 'grade'); os.makedirs(gd, exist_ok=True)
        for f in sorted(glob.glob(os.path.join(d, '*.out.txt'))):
            tag = os.path.basename(f)[:-len('.out.txt')]
            ans = parse_answer(open(f).read(), len(ch['steps']))
            if not ans: continue
            rev = tag.startswith('reordered')
            L = ["Answer key, one entry per step:"]
            for i, st in enumerate(reversed(ch['steps']) if rev else ch['steps'], 1):
                key = '; '.join(x for x in (st['all_effect_text'] or []) if x)
                L.append(f"  Step {i}: {key}")
            L += ["", "What the reader said each step establishes:"]
            for i in range(1, len(ch['steps']) + 1):
                a = ans.get(i) or {}
                L.append(f"  Step {i}: {a.get('shows') or '(no statement)'}")
            L += ["", GRADE_ASK]
            p = os.path.join(gd, f'{tag}.txt'); open(p, 'w').write("\n".join(L))
            jobs.append({'id': f"{ch['case']}/{tag}", 'agent': 'net-grader',
                         'prompt': os.path.abspath(p),
                         'out': os.path.abspath(os.path.join(gd, f'{tag}.out.txt'))})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v3bgrade.json'), 'w'), indent=1)
    print(f"{len(jobs)} grader jobs")


VERD = ['correct', 'partly correct', 'wrong', 'cannot tell']


def gnorm(s):
    s = (s or '').strip().lower()
    for v in ('partly correct', 'partially correct'):
        if v in s: return 'partly correct'
    for v in ('cannot tell', "can't tell", 'cannot determine', 'unclear'):
        if v in s: return 'cannot tell'
    if 'wrong' in s or 'incorrect' in s: return 'wrong'
    if 'correct' in s: return 'correct'
    return None


def score():
    rows = []
    for cj in sorted(glob.glob(os.path.join(ROOT, 'results/v3/traces/*/case.json'))):
        ch = json.load(open(cj))
        gd = os.path.join(ROOT, 'results/v3b', ch['case'], 'grade')
        for f in sorted(glob.glob(os.path.join(gd, '*.out.txt'))):
            tag = os.path.basename(f)[:-len('.out.txt')]
            arm, _, rep = tag.rpartition('.')
            m = re.search(r'\{.*\}', open(f).read(), re.S)
            if not m: continue
            try: j = json.loads(m.group(0))
            except Exception: continue
            for st in j.get('steps', []):
                v = gnorm(st.get('verdict'))
                if not v: continue
                i = int(st['step'])
                # reordered was graded against a reversed key; map back to the real step number
                real = (len(ch['steps']) - i + 1) if arm == 'reordered' else i
                rows.append({'case': ch['case'], 'arm': arm, 'repeat': rep, 'step': real,
                             'hop': ch['steps'][real - 1]['hop'], 'verdict': v})
    json.dump({'rows': rows, 'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v3b/scores.json'), 'w'), indent=1)
    by = collections.defaultdict(collections.Counter)
    for r in rows: by[r['arm']][r['verdict']] += 1
    print(f"{len(rows)} graded step-rulings\n")
    print(f"{'arm':14s} {'n':>4s} {'correct':>8s} {'partly':>7s} {'wrong':>6s} {'cannot':>7s}  hit-rate")
    for a in ARMS + sorted({r['arm'] for r in rows} - set(ARMS)):
        c = by.get(a)
        if not c: continue
        n = sum(c.values())
        print(f"{a:14s} {n:4d} {c['correct']:8d} {c['partly correct']:7d} {c['wrong']:6d} "
              f"{c['cannot tell']:7d}  {c['correct']/n:.0%}")
    # stop rule
    fl = by.get('floor', collections.Counter()); nf = sum(fl.values())
    if nf:
        print(f"\nSTOP RULE -- floor produces the hidden effect correctly on "
              f"{fl['correct']}/{nf} = {fl['correct']/nf:.0%} of hop-rulings "
              f"(limit: more than half)")
        print(f"  correct+partly would be {(fl['correct']+fl['partly correct'])/nf:.0%}")
        if fl['correct'] / nf > 0.5: print("  FIRED: the effect is readable from captions.")
        else: print("  not fired.")


if __name__ == '__main__': {'prompts': prompts, 'gradejobs': gradejobs, 'score': score}[sys.argv[1]]()
