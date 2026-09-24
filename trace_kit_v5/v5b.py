"""v5b.py: tighten the 30 survivors.

  python3 trace_kit_v5/v5b.py apply      scoring targets, dedup, panel cap, depth, FM lane
  python3 trace_kit_v5/v5b.py checks     12 key-checking jobs over the drafted keys
  python3 trace_kit_v5/v5b.py collect    apply the check verdicts

**Scoring the proposition, not the verdict.** 22 of 30 keys end in "not identifiable". If that
sentence alone scores, the item rewards recognising a confound without doing the comparison that
finds it. A key's scoring target is now the combining proposition AND each named limit, listed as
required elements; saying only that the causes cannot be separated earns nothing.

**Deduplication.** A step carrying several items is only a duplicate when the items land on the
same fact. Checked one by one against the claim labels rather than by counting: advanced_ene step 2
splits DFT adsorption energetics (n9) from measured nucleation overpotential (n16), and
bioactive_ma step 2 splits in-vitro platelet adhesion (n18) from in-vivo shunt occlusion (n20).
Those are branches and are kept. journal_of_m_M2_M4 step 2 is the real duplicate: its second item
lands on n20, "improved creep resistance at >=15 wt% SiCp", which restates n16 already carried by
the first item together with the yield-strength claim.

**Depth.** The old field counted how many items a step was split into, which is not depth and read 1
for 19 items at step 2 or later. Depth now counts **derived conclusions**: the number of steps at or
before this item whose key combines a previous result with new evidence. A first step that reads a
micrograph directly contributes nothing to depth. The old value is kept as `split_into`.

Every verdict is model against model.
"""
import json, os, re, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PANEL_CAP = 5
FM = {'SEM', 'TEM', 'STEM', 'XRD', 'XAS', 'ATOM', 'EBSD', 'AFM', 'CT', 'SAXS', 'LEED'}

# checked against the claim labels, not inferred from counts
MERGE = {'journal_of_m_M2_M4_s2_2': {'into': 'journal_of_m_M2_M4_s2_1',
         'why': 'lands on n20, "improved creep resistance at >=15 wt% SiCp", which restates n16 '
                'already carried by s2_1 alongside the yield-strength claim n13'}}


def fam(t):
    if isinstance(t, list): t = t[0] if t else None
    return (t or '').split(':')[0].upper()


def cap_panels(pans, cap=PANEL_CAP):
    """keep at most `cap`, covering as many distinct figures as possible before doubling up"""
    if len(pans) <= cap: return pans, []
    byfig = collections.OrderedDict()
    for p in pans: byfig.setdefault((p.get('figure') or p['suffix'][:2]), []).append(p)
    keep = []
    while len(keep) < cap and any(byfig.values()):
        for f in list(byfig):
            if len(keep) >= cap: break
            if byfig[f]: keep.append(byfig[f].pop(0))
    kept = {id(p) for p in keep}
    return keep, [p for p in pans if id(p) not in kept]


def apply():
    D = json.load(open(os.path.join(ROOT, 'results/v5/items.json')))
    I = {i['item']: i for i in D['items']}
    S = [r['item'] for r in json.load(open(os.path.join(ROOT, 'results/v5/survival.json')))['surviving']]

    # --- 3. dedup
    merged = []
    for a, spec in MERGE.items():
        if a in S:
            S.remove(a); I[a]['merged_into'] = spec['into']; I[a]['merge_why'] = spec['why']
            tgt = I[spec['into']]
            tgt.setdefault('absorbed', []).append({'item': a, 'why': spec['why'],
                                                   'claims': I[a]['claims']})
            for c in I[a]['claims']:
                if c not in tgt['claims']: tgt['claims'].append(c)
            merged.append(a)

    # --- 4. panel cap  --- 1. scoring target  --- 6. FM lane
    capped = []
    for iid in S:
        it = I[iid]
        keep, dropped = cap_panels(it['panels'])
        if dropped:
            it['panels'] = keep
            it['panels_dropped_by_cap'] = [p['suffix'] for p in dropped]
            capped.append((iid, len(keep) + len(dropped), len(keep)))
        k = it['key'] or {}
        req = [x for x in [k.get('proposition')] if x] + list(k.get('limits') or [])
        k['scoring'] = {
            'required_elements': req,
            'n_required': len(req),
            'insufficient_alone': (
                'Stating that the causes cannot be separated, or that the result is not '
                'identifiable, without giving the combining proposition and its limits, earns '
                'nothing. The confound is the conclusion of the comparison, not a substitute '
                'for it.'),
            'target': 'the combining proposition together with each named limit',
        }
        it['key'] = k
        it['fm_lane'] = fam(it['technique']) in FM

    # --- 5. depth
    bytrace = collections.defaultdict(list)
    for iid in S: bytrace[I[iid]['trace']].append(I[iid])
    for tr, its in bytrace.items():
        its.sort(key=lambda x: (x['step'], x['sub']))
        seen = 0
        for it in its:
            it['split_into'] = it.pop('depth', 1)
            if (it['key'] or {}).get('combines'): seen += 1
            it['depth'] = seen
            it['depth_means'] = ('number of derived conclusions at or before this item in its '
                                 'chain: steps whose key combines a previous result with new '
                                 'evidence. A step that reads its evidence directly adds nothing.')

    json.dump({'items': list(I.values()), 'note': D['note']},
              open(os.path.join(ROOT, 'results/v5/items.json'), 'w'), indent=1)
    json.dump({'surviving': [{'item': s} for s in S]},
              open(os.path.join(ROOT, 'results/v5/survival_v5b.json'), 'w'), indent=1)

    steps = {(I[s]['trace'], I[s]['step']) for s in S}
    fmn = [s for s in S if I[s]['fm_lane']]
    print(f"survivors {len(S)} (was {len(S)+len(merged)}), over {len(steps)} distinct steps "
          f"in {len({I[s]['trace'] for s in S})} traces")
    print(f"merged: {merged}")
    print(f"panel cap applied to {len(capped)}: " +
          ', '.join(f'{a} {b}->{c}' for a, b, c in capped))
    print(f"depth: {dict(collections.Counter(I[s]['depth'] for s in S))}")
    print(f"scoring targets: mean {sum(len(I[s]['key']['scoring']['required_elements']) for s in S)/len(S):.1f} "
          f"required elements per item")
    print(f"FM-lane survivors: {len(fmn)} of {len(S)}")
    for s in fmn: print(f"   {s:34s} {I[s]['technique']}")


CHECK_ASK = """You are auditing an answer key against the evidence it was written from.

You are given the step's observations, the previous step's result, and a key: one combining
proposition and a list of limits. For EACH of them separately, rule one of:

  holds       every quantity and direction it states is in the observations above, and the
              inference it draws is available from them
  overreaches states something the observations support only weakly, or in a weaker form -- a cause
              where only an association is available, a relationship where only an ordering is,
              a magnitude the numbers do not pin down
  wrong       contradicts the observations, or cites a number or direction that is not there

Quote the observation you are ruling against. If a statement overreaches or is wrong, give the
corrected wording, keeping it as close to the original as the evidence allows.

Reply as JSON only:
{"proposition": {"verdict": "...", "evidence": "...", "fix": "..." or null},
 "limits": [{"index": 0, "verdict": "...", "evidence": "...", "fix": "..." or null}]}"""


def checks():
    I = {i['item']: i for i in json.load(open(os.path.join(ROOT, 'results/v5/items.json')))['items']}
    S = [r['item'] for r in json.load(open(os.path.join(ROOT, 'results/v5/survival_v5b.json')))['surviving']]
    drafted = [s for s in S if (I[s]['key'] or {}).get('drafted')]
    # sample across papers: round-robin over papers so no paper dominates
    bypaper = collections.OrderedDict()
    for s in drafted: bypaper.setdefault(I[s]['paper'], []).append(s)
    pick, i = [], 0
    while len(pick) < 12 and any(bypaper.values()):
        for p in list(bypaper):
            if len(pick) >= 12: break
            if bypaper[p]: pick.append(bypaper[p].pop(0))
        i += 1
        if i > 50: break
    d = os.path.join(ROOT, 'results/v5/check'); os.makedirs(d, exist_ok=True)
    jobs = []
    for s in pick:
        it = I[s]; k = it['key']
        L = [f"Property under test: {it['property']}", ""]
        if it['previous_output']:
            L += [f"Previous step established: {it['previous_output']}", ""]
        L.append(f"Observations available at this step ({it['technique']}):")
        for n, o in enumerate(it['observations'], 1): L.append(f"  [obs{n}] {o}")
        L += ["", "THE KEY UNDER AUDIT", "", f"Proposition: {k.get('proposition')}", "", "Limits:"]
        for n, lim in enumerate(k.get('limits') or []): L.append(f"  [{n}] {lim}")
        L += ["", CHECK_ASK]
        f = os.path.join(d, s + '.txt'); open(f, 'w').write("\n".join(L))
        jobs.append({'id': s, 'agent': 'net-judge', 'prompt': os.path.abspath(f),
                     'out': os.path.abspath(os.path.join(d, s + '.out.txt'))})
    json.dump(jobs, open(os.path.join(ROOT, '.v07work/batch_v5check.json'), 'w'), indent=1)
    print(f"{len(jobs)} key-check jobs over {len({I[j['id']]['paper'] for j in jobs})} papers "
          f"(of {len(drafted)} drafted survivors)")
    for j in jobs: print(f"   {j['id']}")


if __name__ == '__main__': {'apply': apply, 'checks': checks}[sys.argv[1]]()
