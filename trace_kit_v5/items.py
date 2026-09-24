"""items.py: turn v4 spine steps into v5 items -- one property, one derived conclusion.

  python3 trace_kit_v5/items.py build      items.json per trace
  python3 trace_kit_v5/items.py prompts    one key-drafting job per item
  python3 trace_kit_v5/items.py collect

Changes from v4, following the brief.

**One property per question** (v4c fix). v4 concatenated every property a step's claims touched,
producing questions like "...about the mechanism connecting the two and how the material performs
in service and the rate at which it happens". An item now carries exactly one property. Where a
step touches several, that is not a long question -- it is several items, and `depth` counts them.

**Depth counts derived conclusions** (brief item 5). A step establishing two distinct derived
conclusions becomes two items. Acta is the worked case: the density-yield covariation and the
[0001] loading comparison are separate, and the second is a fracture stress against a flow stress,
not a yield ratio.

**Trimmed step 1** (v4c fix). A first step landing on several claims is trimmed to the claim the
next step actually uses, so the opening item is not a survey.

**Withheld panels** (v4c fix). Panels listed in WITHHOLD are dropped from the evidence: they carry
the answer directly and make the item recall rather than inference.

**Keys state only the permitted inference** (brief item 1). Every key carries `limits` and, where
two causes cannot be separated, `not_identifiable` -- a scorable answer, not a failure to answer.

**Three labels** (brief item 2): dependency, inference validity, causal strength.

**Handoffs carry their caveats** (brief item 4).

Hand-calibrated keys come from calibrated.py and override any draft. Every other key is drafted by
a model and carries `drafted: true` (brief item 10: drafts, not gold).

Every verdict is model against model.
"""
import json, os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'trace_kit_v3'))
from calibrated import HAND, STRENGTH, QUANTITY
from support import claim_support, supported
from v3b import PROPERTY, FAMILY

# panels withheld because they state the answer outright rather than evidence it
WITHHOLD = {('Acta_Materialia__10.1016_j.actamat.2021.116797', 1): ['F1f']}


def props_of(claims, N):
    """every distinct property the claims touch, as separate entries -- one per item"""
    out = []
    for c in claims:
        n = N.get(c) or {}
        fam = (n.get('attrs') or {}).get('property_family')
        p = (FAMILY.get(fam) if fam else None) or PROPERTY.get(n.get('type')) \
            or PROPERTY.get('/'.join((n.get('type') or '').split('/')[:2]))
        if p and not any(o['property'] == p for o in out):
            out.append({'property': p, 'claims': [c]})
        elif p:
            next(o for o in out if o['property'] == p)['claims'].append(c)
    return out or [{'property': 'what the sample is like', 'claims': list(claims)}]


DRAFT_ASK = """You are drafting an answer key, not answering a question.

Say what this evidence, together with the previous step's result, actually PERMITS someone to
conclude -- and no more. A key that overstates is worse than a key that says a thing cannot be
determined. "Not identifiable" is a correct and scorable answer whenever two candidate causes
cannot be separated by the data given.

Give:
1. the combining proposition: what follows from putting the previous step's result together with
   this evidence. If nothing does, say so and set `combines` false.
2. its limits: what this comparison does NOT establish, including any confound -- two variables
   that move together by construction, a quantity compared against a different kind of quantity,
   or too few points to support a relationship rather than an ordering.
3. `not_identifiable`: if two causes cannot be separated here, name them. Otherwise null.
4. the quantity kind on each side: one of rate, amount, cumulative, normalized -- and say what is
   being measured, with units and the window it covers.
5. three labels:
   dependency: real if the conclusion becomes unjustifiable without the previous step, none if not.
   inference_validity: "follows", "follows, weakly", or "does not follow".
   causal_strength: descriptive, associative, conditional mechanism, or discriminating.
6. the handoff to the next step, WITH the caveats it must carry.

Reply as JSON only:
{"combines": true or false,
 "proposition": "...", "limits": ["..."], "not_identifiable": "..." or null,
 "quantity": {"previous": {"kind": "...", "what": "..."}, "this": {"kind": "...", "what": "..."}},
 "labels": {"dependency": "...", "inference_validity": "...", "causal_strength": "..."},
 "handoff": "...", "handoff_caveats": ["..."]}"""


def build():
    items, bypaper = [], collections.Counter()
    for f in sorted(glob.glob(os.path.join(ROOT, 'results/v4x/*/trace.json'))):
        t = json.load(open(f))
        N = {n['id']: n for n in json.load(open(os.path.join(ROOT, t['graph'])))['nodes']}
        sup = claim_support(json.load(open(os.path.join(ROOT, t['graph']))))
        for i, s in enumerate(t['steps']):
            prev = t['steps'][i - 1] if i else None
            groups = props_of(s['claims'], N)
            if not prev and len(groups) > 1:
                groups = groups[:1]                       # trimmed step 1
            wh = WITHHOLD.get((t['paper'], s['step']), [])
            pans = [p for p in s['panels'] if p['suffix'] not in wh]
            for k, gr in enumerate(groups, 1):
                iid = f"{t['trace']}_s{s['step']}" + (f"_{k}" if len(groups) > 1 else '')
                items.append({
                    'item': iid, 'paper': t['paper'], 'trace': t['trace'], 'step': s['step'],
                    'sub': k, 'of': len(groups),
                    'property': gr['property'], 'claims': gr['claims'],
                    'hidden_key_claims': [N[c].get('label') for c in gr['claims']],
                    'previous_output': prev['output_short'] if prev else None,
                    'previous_step': prev['step'] if prev else None,
                    'technique': s['technique'], 'delivery': s['delivery'],
                    'observations': s['observations'],
                    'panels': pans, 'withheld_panels': wh,
                    'depth': len(groups),
                    'provenance_NOT_SOLVER_VISIBLE': s['provenance_NOT_SOLVER_VISIBLE'],
                })
                bypaper[t['paper']] += 1
    json.dump({'items': items, 'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v5/items.json'), 'w'), indent=1)
    print(f"{len(items)} items over {len(bypaper)} papers "
          f"(from {len(glob.glob(os.path.join(ROOT,'results/v4x/*/trace.json')))} traces)")
    split = sum(1 for i in items if i['of'] > 1)
    print(f"  {split} items came from splitting a step that carried more than one property")
    print(f"  {sum(1 for i in items if i['withheld_panels'])} items have a withheld panel")
    return items


if __name__ == '__main__': {'build': build}[sys.argv[1]]()
