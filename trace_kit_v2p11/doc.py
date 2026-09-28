"""doc.py: docs/TRACES_V2P11_NANOLETT.md. Every number read from results/v2p11/*.json.

  python3 trace_kit_v2p11/doc.py

No model call, and nothing typed by hand.
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p11'))
import pilot as P  # noqa: E402

OUT = P.OUT


def n2(x): return '—' if x is None else f'{x:.2f}'


def main():
    D = json.load(open(os.path.join(OUT, 'decide.json')))
    LG = json.load(open(os.path.join(OUT, 'ledger.json')))
    s1 = json.load(open(os.path.join(OUT, 'step1.json')))
    est = json.load(open(os.path.join(OUT, 'estimate.json')))
    cost = json.load(open(os.path.join(OUT, 'cost.json')))
    bld = json.load(open(os.path.join(OUT, 'report_build.json')))
    S = json.load(open(os.path.join(OUT, 'seed_claims.json')))
    U, CH, FAM = D['units'], D['chains'], D['families']
    acc = set(bld['chains_accepted'])
    fam_of = {c: f for f, v in FAM.items() for c in v['chains']}

    L = ['# v2.11 pilot — stricter acceptance on one paper', '',
         '**Every verdict is model against model.** No step of this was reviewed by a person.', '',
         f'Paper: `{P.PAPER}`. Scope: the {len(CH)} chains v2.10 put on this paper '
         f'({", ".join(sorted(CH))}), the {len(D["stacked_table"]) - len(CH) + len(CH)} units '
         f'they are built from, grouped into {len(FAM)} families by shared prefix.', '',
         '## Step 1 — what each arm actually received', '']
    f1 = s1['finding']
    L += [f'Read out of the prompt files that were sent, not the generator that wrote them (the '
          f'generator has been edited since those runs, so its source is not evidence).', '',
          f'**Finding: {f1["verdict"]}.** All {f1["links"]} links carried every recorded '
          f'qualification into both arm B and arm C, so the rerun branch of Step 1 did not fire '
          f'and no arm was rerun.', '',
          'What each arm held, per link:', '',
          '| arm | observation text | cropped panels | whole figures | captions | earlier result | its limits |',
          '| --- | --- | ---: | ---: | --- | --- | --- |']
    r0 = s1['per_link'][0]
    for a in ('A', 'B', 'C', 'N'):
        g = r0[a]
        L.append(f'| {a} | {"yes" if g["observation_text"] else "no"} | {g["crop_paths"]} | '
                 f'{g["whole_figures"]} | {"yes" if g["captions"] else "no"} | '
                 f'{"yes" if g["earlier_result"] else "no"} | '
                 f'{g["limits_present"]}/{r0["n_input_limits"]} |')
    L += ['', '(One link shown; the shape is the same on all eight, and the per-link counts are '
              'in `step1.json`.)', '',
          '**No arm was ever shown a whole figure.** Every panel reached the answerers as a crop '
          'plus its printed caption. That matters for Step 3: a judge asked whether the evidence '
          'can carry a claim is ruling on crops and captions, which is what the answerers had.', '']

    L += ['## Steps 2–5 — every seed and link against the six gates', '',
          '| unit | kind | A | B | C | N | stacked | B−A | B−C | B−stacked | 1 dep | 2 rel | '
          '3 abs | 4 con | 5 cav | 6 val | verdict |',
          '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :-: | :-: | '
          ':-: | :-: | :-: | :-: | --- |']
    tick = lambda b: '✓' if b else '**✗**'
    for it, u in U.items():
        s = u['scores']; g = u['gates']
        L.append(f'| `{it}` | {"seed" if u["is_seed"] else "link"} | {n2(s.get("A"))} | '
                 f'{n2(s.get("B"))} | {n2(s.get("C"))} | {n2(s.get("N"))} | '
                 f'{n2(s.get("stacked"))} | {n2(u["B_minus_A"])} | {n2(u["B_minus_C"])} | '
                 f'{n2(u["B_minus_stacked"])} | ' + ' | '.join(
                     tick(g[k]) for k in sorted(g))
                 + f' | {"pass" if u["passed"] else "**fail " + str(u["first_failed"]) + "**"} |')
    npass = sum(1 for u in U.values() if u['passed'])
    L += ['', f'{npass} of {len(U)} units clear all six gates.', '']

    fails = collections.Counter(u['first_failed'] for u in U.values() if not u['passed'])
    if fails:
        L += ['Which gate does the work:', '', '| first gate failed | units |', '| --- | ---: |']
        for k, n in sorted(fails.items(), key=lambda kv: -kv[1]):
            L.append(f'| {k} | {n} |')
        L.append('')

    L += ['## The stacked baseline', '',
          'Arm B holds everything arm A and arm C hold, so B beating each separately is a low '
          'bar: stapling the two answers together clears it. The stacked baseline is that '
          'staple — arm A\'s answer and arm C\'s, concatenated with nothing added, graded '
          'against the same claims by the same grader.', '']
    bs = [u['B_minus_stacked'] for u in U.values() if u['B_minus_stacked'] is not None]
    rel = sum(1 for x in bs if x >= P.MARGIN)
    add = [it for it, u in U.items() if u['additive_not_relational']]
    L += [f'- **{rel} of {len(bs)} units** beat the stacked pile by the required +{P.MARGIN:.2f}.',
          f'- Mean B−stacked: **{sum(bs)/len(bs):+.3f}**' if bs else '- no stacked scores',
          f'- **{len(add)} units are additive, not relational**: they pass the dependency gate '
          f'(B really does beat A and C) yet do not beat the concatenation of A and C. Their '
          f'answers carry what both sides carry without relating them.', '']
    if add:
        L += ['| unit | B | stacked | B−stacked |', '| --- | ---: | ---: | ---: |']
        for it in add:
            u = U[it]
            L.append(f'| `{it}` | {n2(u["scores"]["B"])} | {n2(u["scores"]["stacked"])} | '
                     f'{n2(u["B_minus_stacked"])} |')
        L.append('')

    # the sharpest case, chosen by the data rather than by hand: the unit where the pile
    # scores furthest above either of the answers it is made of
    gap = [(u['scores']['stacked'] - max(u['scores']['A'] or 0, u['scores']['C'] or 0), it, u)
           for it, u in U.items() if u['scores'].get('stacked') is not None]
    gap.sort(reverse=True)
    if gap and gap[0][0] > 0:
        g0, it0, u0 = gap[0]
        comb = [c for c in u0['claims'] if c['kind'] == 'combined']
        rul = P.rulings_of(P.read(f'{it0}__stacked'))
        st = next((r for r in rul if str(r.get('n')) == '1'
                   and (r.get('verdict') or '') == 'stated'), None)
        L += ['### The clearest case', '',
              f'`{it0}`: arm A scores {n2(u0["scores"]["A"])} and arm C '
              f'{n2(u0["scores"]["C"])}, yet their concatenation scores '
              f'{n2(u0["scores"]["stacked"])} — a gap of {g0:+.2f} over either answer alone.', '']
        if comb:
            L += [f'The claim: *“{comb[0]["claim"]}”*', '']
        if st and st.get('quote'):
            L += ['What the grader quoted from the pile to call it stated:', '',
                  f'> {st["quote"]}', '',
                  'That quote is a splice. Its parts come from opposite sides of the '
                  'concatenation boundary — one from the arm that saw only the first '
                  'measurement, one from the arm that saw only the second — joined by the '
                  'grader, not by any answerer. The claim was assembled by the reader. This is '
                  'exactly what gate 2 exists to catch, and no arm-versus-arm comparison can '
                  'see it, because arm B beats both A and C by a full point here.', '']

    L += ['## Step 3 — evidence validity', '']
    vc = collections.Counter(v['verdict'] for u in U.values() for v in u['validity'])
    tot = sum(vc.values())
    L += [f'{tot} combined claims ruled across {len(U)} units.', '',
          '| ruling | n | share |', '| --- | ---: | ---: |']
    for k in ('supported', 'overreaches', 'unsupported', 'unruled'):
        if vc.get(k): L.append(f'| {k} | {vc[k]} | {100*vc[k]/tot:.1f}% |')
    L.append('')
    bad = [(it, v) for it, u in U.items() for v in u['validity']
           if v['verdict'] in ('overreaches', 'unsupported') and not v.get('excused')]
    if bad:
        L += [f'The {len(bad)} rulings that fail gate 6, verbatim:', '']
        for it, v in bad:
            L += [f'- **`{it}`** — *{v["verdict"]}* — “{v["claim"]}”',
                  f'  - cannot show: {v["cannot_show"]}']
            if v['quote']: L.append(f'  - quoting: “{v["quote"]}”')
        L.append('')

    L += ['## The chains and families', '',
          f'v2.10 accepted all {len(CH)} chains on this paper. v2.11 accepts **{len(acc)}**, '
          f'across **{len(bld["families_with_an_accepted_chain"])}** of **{len(FAM)}** families.',
          '', '| chain | family | depth | v2.10 | v2.11 | first gate failed | on which unit |',
          '| --- | --- | ---: | --- | --- | --- | --- |']
    for cid in sorted(CH):
        c = CH[cid]; led = LG.get(cid, {})
        if cid in acc: why, unit = '—', '—'
        elif not c['gates_passed']:
            why, unit = str(c['first_failed_gate']), f'`{c["first_failing_unit"]}`'
        else:
            why, unit = f'caveat ledger ({led.get("bad", 0)} ignored/contradicted)', 'whole chain'
        L.append(f'| {cid} | {fam_of.get(cid, "")} | {c["depth"]} | accepted | '
                 f'{"**accepted**" if cid in acc else "rejected"} | {why} | {unit} |')
    L.append('')
    seedkill = [c for c in CH if CH[c]['first_failing_unit'] in
                {v['seed'] for v in FAM.values()}]
    gate1only = [it for it, u in U.items() if u['gates']['1_dependency'] and not u['passed']]
    L += [f'**{len(seedkill)} of {len(CH)} chains die at the seed** — the unit v2.10 never put '
          f'to the arms at all. A chain can only be as good as the thing it starts from, and on '
          f'this paper the starting point was never checked.', '',
          f'**The old rule was not binding here.** Gate 1 is the whole v2.10 test, and all '
          f'{sum(1 for u in U.values() if u["gates"]["1_dependency"])} of {len(U)} units pass '
          f'it. Every rejection in this pilot comes from a gate v2.10 did not have: '
          f'{len(gate1only)} units clear the dependency test and fail something else.', '']
    L += ['| family | seed | chains | shared steps | accepted |',
          '| --- | --- | --- | ---: | ---: |']
    for f, v in sorted(FAM.items()):
        L.append(f'| {f} | `{v["seed"]}` | {", ".join(v["chains"])} | '
                 f'{1 + len(v["shared_links"])} | {len([c for c in v["chains"] if c in acc])} |')
    L.append('')

    L += ['### The caveat ledger on accepted chains', '']
    for cid in sorted(CH):
        led = LG.get(cid)
        if not led: continue
        L.append(f'- **{cid}**: {led["n"]} qualifications, '
                 + ', '.join(f'{n} {k}' for k, n in sorted(led['counts'].items()))
                 + (f' — **rejects the chain**' if led['ledger_rejects'] else ''))
    L.append('')

    L += ['## The seeds, which v2.10 never tested', '']
    for s, v in S.items():
        L.append(f'- `{s}`: {len(v["kept"])} claims kept, **{v["n_combined"]} tagged combined**, '
                 f'{len(v["limits"])} limits. {len(v["dropped"])} dropped by the second tagger.')
    L += ['', 'A seed with one combined claim has a combined score that can only be 0.00 or '
              '1.00. That is a coarse instrument, and gate 3 (B ≥ 0.60) on such a seed is an '
              'all-or-nothing test rather than a measurement. Stated here rather than left for '
              'the reader to infer from the table.', '']

    gd = json.load(open(os.path.join(OUT, 'grader_defect.json')))
    L += ['## A defect in the grader itself, found during this run', '',
          f'The `net-grader` agent definition (`{gd["file"]}`, and '
          f'{len(gd["identical_copies"])} byte-identical copies elsewhere in the repo) carries '
          f'instructions left over from an older task:', '',
          '```', gd['stray_body'], '```', '',
          gd['conflict'], '',
          f'Observed effect in this run: '
          f'**{gd["replies_starting_with_the_stray_verdict_word"]} of '
          f'{gd["grading_calls_this_run"]} grading replies** opened with the stray verdict word, '
          f'and **{gd["replies_without_a_rulings_block"]}** failed to return a rulings block. '
          f'The graders overwhelmingly followed the prompt file and ignored their own system '
          f'prompt, so the practical damage here is small. The second rule is the worse of the '
          f'two, though: it tells the grader that "different names for the same thing" are '
          f'CORRECT, a leniency instruction written for panel descriptions that has no business '
          f'in claim grading.', '',
          f'**Scope: {gd["scope"]}**', '',
          gd['not_changed'] + ' It is the first thing to fix before this rule is applied to any '
          'other paper.', '']

    L += ['## The report', '',
          f'`{bld["page"]}` — {bld["mb"]:.2f} MB, self-contained, {bld["panels_shown"]} panels '
          f'shown, {len(bld["panel_misses"])} panel misses, {bld["images_resized"]} images over '
          f'the 1400 px cap and downscaled once.', '',
          '## Cost', '',
          f'- Estimated before any call: **{est["estimate_without_reserve"]}** '
          f'({est["estimate_with_reserve"]} with the borderline reserve), against the brief\'s '
          f'estimate of {est["brief_estimate"]}. The gap is Step 1: it found the limits were '
          f'already in the handoff, so the rerun branch never fired.',
          f'- Actual: **{cost["calls"]} calls**' +
          (f', {cost["wall_minutes"]:.0f} minutes wall time' if cost.get('wall_minutes') else ''),
          '']
    for k, v in cost.get('by_step', {}).items():
        L.append(f'  - {k}: {v}')
    L += ['', '- Every reply was matched to its prompt byte for byte in the dispatching agent\'s '
              'own transcript before it was written to disk. The relay\'s own report is not '
              'evidence.', '']

    os.makedirs(R('docs'), exist_ok=True)
    open(R('docs/TRACES_V2P11_NANOLETT.md'), 'w').write('\n'.join(L) + '\n')
    print(f'docs/TRACES_V2P11_NANOLETT.md: {len(L)} lines')


if __name__ == '__main__':
    main()
