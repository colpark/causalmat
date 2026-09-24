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

# Claims pinned onto a step because a hand-calibrated key depends on them.
#
# net-decompose is not stable across runs. The v3 run that built v4 matched Acta M1 to n2, n8 and
# n9; re-running it for the 32-paper batch returned n8 alone, dropping n9 -- the nanoplate density
# series 9.8 -> 0.3 -> 9.0 per um that the whole density-versus-yield comparison rests on. The same
# instability cost Nano Letters M3 its n17 in 4 of 6 identical runs. Where the brief hand-specifies
# a key, the quantity that key cites must be present regardless of what the matcher returned that
# day, so it is pinned here and the pin is recorded on the item.
PIN = {('Acta_Materialia__10.1016_j.actamat.2021.116797', 1): ['n8', 'n9']}


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
            claims = PIN.get((t['paper'], s['step']), s['claims'])
            pinned = (t['paper'], s['step']) in PIN and claims != s['claims']
            groups = props_of(claims, N)
            if not prev and len(groups) > 1:
                # Trim step 1 to ONE property -- but to the one the next step actually uses, not
                # whichever sorts first. Trimming Acta step 1 to its first group kept the phase
                # identity (n8) and dropped the nanoplate density series (n9), which is the entire
                # quantity the density-yield comparison depends on. Prefer the group with a graph
                # edge into the next step's claims.
                nxt = set(t['steps'][1]['claims']) if len(t['steps']) > 1 else set()
                E = json.load(open(os.path.join(ROOT, t['graph'])))['edges']
                linked = {e['src'] for e in E if e['dst'] in nxt} | \
                         {e['dst'] for e in E if e['src'] in nxt}
                groups = sorted(groups, key=lambda g: -len(set(g['claims']) & linked))[:1]
            wh = WITHHOLD.get((t['paper'], s['step']), [])
            pans = [p for p in s['panels'] if p['suffix'] not in wh]
            for k, gr in enumerate(groups, 1):
                iid = f"{t['trace']}_s{s['step']}" + (f"_{k}" if len(groups) > 1 else '')
                items.append({
                    'item': iid, 'paper': t['paper'], 'trace': t['trace'], 'step': s['step'],
                    'sub': k, 'of': len(groups),
                    'property': gr['property'], 'claims': gr['claims'], 'claims_pinned': pinned,
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


def prompts():
    IT = json.load(open(os.path.join(ROOT, 'results/v5/items.json')))['items']
    jobs = []
    d = os.path.join(ROOT, 'results/v5/draft'); os.makedirs(d, exist_ok=True)
    for it in IT:
        L = [f"Property under test: {it['property']}", ""]
        if it['previous_output']:
            L += [f"The previous step (step {it['previous_step']}) established: {it['previous_output']}", ""]
        else:
            L += ["This is the first step of its chain; there is no previous result.", ""]
        L.append(f"Evidence available at this step ({it['technique']}):")
        for i, o in enumerate(it['observations'], 1): L.append(f"  [obs{i}] {o}")
        if it['panels']: L.append("Panels: " + ', '.join(p['suffix'] for p in it['panels']))
        if it['withheld_panels']:
            L.append(f"(withheld from the solver: {', '.join(it['withheld_panels'])})")
        L += ["", "What the paper concluded at this step, for your reference as the key's author:"]
        for c in it['hidden_key_claims']: L.append(f"  {c}")
        L += ["", DRAFT_ASK]
        f = os.path.join(d, it['item'] + '.txt'); open(f, 'w').write("\n".join(L))
        jobs.append({'id': it['item'], 'agent': 'net-writer', 'prompt': os.path.abspath(f),
                     'out': os.path.abspath(os.path.join(d, it['item'] + '.out.txt'))})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v5draft.json'), 'w'), indent=1)
    print(f"{len(jobs)} key-drafting jobs")


def _obj(txt):
    out, depth, start = [], 0, None
    for i, c in enumerate(txt or ''):
        if c == '{':
            if depth == 0: start = i
            depth += 1
        elif c == '}' and depth:
            depth -= 1
            if not depth: out.append(txt[start:i + 1])
    for o in sorted(out, key=len, reverse=True):
        for cand in (o, re.sub(r',(\s*[}\]])', r'\1', o)):
            # the second candidate strips trailing commas. One drafter reported having fixed a
            # stray trailing comma in its own JSON and had in fact left one in, so a reply that
            # says it is valid is not evidence that it is.
            try:
                j = json.loads(cand)
                if 'labels' in j or 'proposition' in j: return j
            except Exception: continue
    return None


def collect():
    IT = json.load(open(os.path.join(ROOT, 'results/v5/items.json')))['items']
    # several hand keys can target one (paper, step): Biomaterials step 2 carries both the
    # texture/inventory item and the dose-response item, because the brief branches that step.
    # A plain dict here kept only the last and silently dropped biomat_texture_inventory.
    byhand = collections.defaultdict(list)
    for k, v in HAND.items(): byhand[(v['paper'], v['from_step'])].append((k, v))
    n_hand = n_draft = n_fail = 0
    for it in IT:
        f = os.path.join(ROOT, 'results/v5/draft', it['item'] + '.out.txt')
        j = _obj(open(f).read()) if os.path.exists(f) else None
        if j:
            it['key'] = {'drafted': True, **j}; n_draft += 1
        else:
            it['key'] = None; n_fail += 1
    # hand keys replace the draft on their item, and are added where no item matched
    used = set()
    for it in IT:
        pool = [x for x in byhand.get((it['paper'], it['step']), []) if x[0] not in used]
        if pool:
            k, v = pool[0]
            it['key'] = {'drafted': False, 'hand_calibrated': k, 'proposition': v['key'],
                         'limits': v['limits'], 'not_identifiable': v.get('not_identifiable'),
                         'permitted': v['permitted'], 'not_permitted': v['not_permitted'],
                         'quantity': v['quantity'], 'labels': v['labels'],
                         'combines': v['labels']['dependency'] == 'real'}
            it['property'] = v.get('question', it['property'])
            used.add(k); n_hand += 1
    json.dump({'items': IT, 'note': 'Every verdict is model against model.'},
              open(os.path.join(ROOT, 'results/v5/items.json'), 'w'), indent=1)
    lab = collections.Counter()
    for it in IT:
        if it.get('key') and it['key'].get('labels'):
            lab[it['key']['labels'].get('causal_strength')] += 1
    print(f"{n_draft} drafted, {n_hand} replaced by a hand-calibrated key, {n_fail} unparsed")
    print(f"causal strength: {dict(lab)}")
    ni = sum(1 for it in IT if (it.get('key') or {}).get('not_identifiable'))
    print(f"items whose key says something is not identifiable: {ni}")
    unused = [k for k in HAND if k not in used]
    if unused: print(f"hand keys with no matching item: {unused}")


if __name__ == '__main__': {'build': build, 'prompts': prompts, 'collect': collect}[sys.argv[1]]()
