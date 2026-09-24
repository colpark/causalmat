"""v4b.py: re-judge the dependency on the data, not on the question's wording.

  python3 trace_kit_v4/v4b.py apply      rewrite questions, re-judge, write dependency_v4b.json
  python3 trace_kit_v4/v4b.py prompts    regenerate the reference reasoning for the new questions
  python3 trace_kit_v4/v4b.py collect

v4 judged a step `real` when its question said "taking step 1 as given". That is wording, not
dependency. Acta step 2 is the case that exposed it: the question referred back, but its key --
"yield stress is strongly orientation dependent, ~145-165 MPa" -- is read entirely off F8a and F2a
and needs nothing from step 1. Meanwhile the actual cross-step link sits unused in the data:
nanoplate density 9.8 -> 0.3 -> 9.0 per um (step 1) against yield stress 167 -> 113 -> 160 MPa
(step 2), the same three heat treatments, dipping and recovering together.

**New criterion.** A step is `real` only when a proposition exists that COMBINES the previous step's
output with this step's evidence -- a covariation, a mechanism check, or a quantity needing both.
The question's wording counts for nothing.

The combining propositions below are judgements made by reading both steps' numbers. They are
written out in full, with the quantities from each side, so they can be checked rather than trusted.

Every verdict is model against model.
"""
import json, os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TR = sorted(glob.glob(os.path.join(ROOT, 'results/v4/*/trace.json')))

# (trace, step) -> the combining proposition, or None where the data supports none.
# `question` keeps the effect hidden: it names the property and asks whether the two covary; it
# never states which way.
COMBINE = {
 ('acta_materia_M1_M2_M3', 2): {
   'kind': 'covariation',
   'proposition': 'Yield stress tracks nanoplate number density across the three heat treatments: '
                  'both fall after the 520 C anneal and both recover after the further 400 C anneal, '
                  'so the strengthening follows plate density rather than the anneal itself.',
   'from_previous': 'nanoplate count 9.8 -> 0.3 -> 9.0 per um, mean thickness 28 -> 84 -> 14 nm '
                    '(as-grown / 520 C / 520->400 C) [n9]',
   'from_this': 'yield stress in [11-20] at RT 167 -> 113 -> 160 MPa across the same three '
                'heat treatments [n12]',
   'question': 'Across the three heat treatments (as-grown, 520 C, and the further 400 C anneal), '
               'does the mechanical property measured here move with the feature sizes you measured '
               'in step 1, or independently of them? Give the comparison and say what it implies '
               'about what carries the strength.'},
 ('acta_materia_M1_M2_M3', 3): {
   'kind': 'quantity needing both',
   'proposition': 'The [0001] orientation that step 2 found unable to yield in compression, '
                  'fracturing at ~355 MPa, deforms in tension at ~65-80 MPa to ~45% strain, a four- '
                  'to five-fold asymmetry that a slip mechanism cannot produce.',
   'from_previous': '[0001] fractures at ~355 MPa in compression without yielding; soft orientation '
                    '~9 MPa, [11-20] ~148-165 MPa [n12]',
   'from_this': 'tension along [0001] flows at ~72 MPa, serrated ~52-80 MPa, ~45% plastic strain [n18]',
   'question': 'Compare the stress at which this evidence shows deformation along [0001] with the '
               'property value you measured in step 2 for that same orientation. Report both numbers '
               'and say what their ratio implies about the deformation route.'},
 ('advanced_fun_M1_M2', 2): {
   'kind': 'covariation',
   'proposition': 'Emission complexity ranks inversely with domain size across the same three '
                  'samples: the ~0.1 um PC shows a dual peak with an IR tail, the 1e2-1e3 um SC a '
                  'single band, and HOC lies between on both axes.',
   'from_previous': 'domain size ~0.1 um (PC), 10-100 um (HOC), 1e2-1e3 um (SC) [n7]',
   'from_this': 'below 150 K, PC shows two branches plus an IR tail, HOC intermediate, SC one '
                'band [n13]',
   'question': 'Rank the three samples by what this evidence shows, and compare that ranking with '
               'the feature sizes you measured in step 1. Do the two orderings correspond, and what '
               'does that imply about the optical property?'},
 ('biomaterials_M1_M3_M4', 2): {
   'kind': 'mechanism check',
   'proposition': 'Release rises as surface area and pore volume fall, so it is set by Co content '
                  'and not by the mesoporous texture: the 5Co scaffold has the least surface area '
                  'and releases the most.',
   'from_previous': 'surface area 290 -> 180 -> 127 m2/g and pore volume 0.30 -> 0.19 -> 0.15 cm3/g '
                    'for 0Co / 2Co / 5Co [n9]',
   'from_this': 'Co2+ in medium at 7 days: 0 (0Co), ~16.9 (2Co), ~20.8 mg/L (5Co) [n11]',
   'question': 'Order the three scaffolds by the rate measured here, and compare that order with '
               'the pore structure you characterised in step 1. If the texture were controlling '
               'this rate, which scaffold would lead? Say what the comparison implies about the '
               'mechanism.'},
 ('biomaterials_M1_M3_M4', 3): None,
 ('biomaterials_M2_M4', 2): None,
 ('nano_letters_M1_M2', 2): None,
 ('rare_metals_M1_M2', 2): None,
}

# why a pair supports none, recorded so a `none` is as auditable as a `real`
NO_COMBINE = {
 ('biomaterials_M1_M3_M4', 3): 'restatement: lands only on n12 and n16, which step 2 already '
                               'established, with the same two observations. Nothing to combine.',
 ('biomaterials_M2_M4', 2):    'the only content this step adds is n16, the ampicillin antibacterial '
                               'result. That is a separate arm of the paper from step 1\'s Co2+ '
                               'release dose, and the HIF-1alpha observation it shares with step 1 '
                               'is already step 1 evidence. Antibacterial survival does not combine '
                               'with Co2+ dose. Under v4 this scored `real` on wording alone.',
 ('nano_letters_M1_M2', 2):    'one material, two cells: the pore structure is a single constant '
                               'across the Li and Na measurements, so no covariation exists. The '
                               'only cross-step inference available -- that porosity cannot be what '
                               'differentiates Li from Na -- uses no quantity from step 1.',
 ('rare_metals_M1_M2', 2):     'restatement: lands only on s6, which step 1 already established, '
                               'from the same observation. Nothing to combine.',
}


def apply():
    rows, tally = [], collections.Counter()
    for f in TR:
        t = json.load(open(f)); d = os.path.dirname(f)
        old = {r['step']: r for r in json.load(open(os.path.join(d, 'dependency.json')))['steps']}
        for i, s in enumerate(t['steps']):
            if not i:
                s['combining'] = None; continue
            key = (t['trace'], s['step'])
            c = COMBINE.get(key)
            s['combining'] = c
            s['question_v4'] = s.get('question_v4') or s['question']
            if c:
                s['question'] = c['question']
            new = 'real' if c else 'none'
            tally[new] += 1
            rows.append({'trace': t['trace'], 'step': s['step'],
                         'old': old.get(s['step'], {}).get('dependency'),
                         'old_why': old.get(s['step'], {}).get('why'),
                         'new': new,
                         'proposition': (c or {}).get('proposition'),
                         'kind': (c or {}).get('kind'),
                         'from_previous': (c or {}).get('from_previous'),
                         'from_this': (c or {}).get('from_this'),
                         'why_none': NO_COMBINE.get(key)})
        json.dump(t, open(f, 'w'), indent=1)
    json.dump({'rows': rows, 'criterion': 'real only if a proposition combines the previous step\'s '
               'output with this step\'s evidence; wording counts for nothing.',
               'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v4/dependency_v4b.json'), 'w'), indent=1)
    print(f"re-judged {sum(tally.values())} steps with a predecessor: {dict(tally)}\n")
    print(f"{'trace':24s} {'step':>4s}  {'v4':>5s} -> {'v4b':<5s}  kind")
    ch = 0
    for r in rows:
        flag = '  CHANGED' if r['old'] != r['new'] else ''
        ch += r['old'] != r['new']
        print(f"{r['trace'][:24]:24s} {r['step']:4d}  {str(r['old']):>5s} -> {r['new']:<5s}  "
              f"{str(r['kind'] or '-'):22s}{flag}")
    print(f"\n{ch} of {len(rows)} labels changed")
    if not tally['real']:
        print("STOP RULE FIRED: no step supports a combining proposition.")
    else:
        print(f"STOP RULE not fired: {tally['real']} steps support one.")


if __name__ == '__main__': {'apply': apply}[sys.argv[1]]()
