"""compare_v2.py: v3 against v2 on the same five papers.

  python3 trace_kit_v3/compare_v2.py

The two designs do not share a scale, and this does not pretend they do. v2 graded each step
against an expected support level derived from the graph, so it could report "steps correct". v3
has no key: the question "does this evidence warrant this step?" has no stored answer, so v3's arms
are compared with each other and with the majority-class baseline, never with a key.

What is comparable is what each design can detect, and how much of each paper it uses.

Every verdict is model against model.
"""
import json, os, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARMS3 = ['full', 'floor', 'oracle_complete', 'reordered', 'permute_image']


def main():
    v2 = json.load(open(os.path.join(ROOT, 'results/v2/v2_summary.json')))
    v3 = json.load(open(os.path.join(ROOT, 'results/v3/gate_scores.json')))
    byp2 = {c['paper']: c for c in v2['cases']}
    byp3 = collections.defaultdict(list)
    for c in v3['cases']: byp3[c['paper']].append(c)

    print("| paper | v2 case | v2 steps | v3 traces | v3 steps |")
    print("|---|---|---|---|---|")
    t2 = t3 = 0
    for p in sorted(set(byp2) | set(byp3)):
        a = byp2.get(p); b = byp3.get(p, [])
        n2 = a['n_steps'] if a else 0
        n3 = sum(c['n_steps'] for c in b)
        t2 += n2; t3 += n3
        print(f"| {p.split('__')[0].replace('_',' ')} | {a['case'] if a else '—'} | {n2} | "
              f"{len(b)} | {n3} |")
    print(f"| **total** | **{len(byp2)}** | **{t2}** | "
          f"**{sum(len(v) for v in byp3.values())}** | **{t3}** |")

    print("\n### what each design's step is")
    print("- v2: one evidence node under one claim. A step asks whether that observation is visible.")
    print("- v3: one MatMech causal hop. A step asks whether the evidence warrants moving from the")
    print("  previous hop's effect to this one's.")

    print("\n### v2 arm totals (graded against a key)")
    for a, v in v2['arm_totals'].items():
        print(f"  {a:16s} {v['steps_correct']}/{v['of']} steps, "
              f"{v['closings_correct']}/5 closings, parsed {v['parsed']}/5")
    print("\n  v2 stop rule `oracle_matches_full_in_2_or_more` fired on "
          f"{len(v2['stop_rules']['oracle_matches_full_in_2_or_more']['cases'])} of 5 cases: "
          "the text measurement matched or beat the picture everywhere.")
    exp = collections.Counter(c['closing'] for c in v2['cases'])
    print(f"  v2 expected closings: {dict(exp)} -- the key is degenerate, every case 'partial'.")

    print("\n### v3 arm levels (no key; arms compared with each other)")
    for a in ARMS3:
        lv = [c['arms'].get(a, {}).get('steps', {}).get(str(i)) or
              c['arms'].get(a, {}).get('steps', {}).get(i)
              for c in v3['cases'] for i in range(1, c['n_steps'] + 1)]
        lv = [x for x in lv if x]
        if not lv: print(f"  {a:16s} no parsed replies"); continue
        cc = collections.Counter(lv); top, n = cc.most_common(1)[0]
        print(f"  {a:16s} {len(lv)} rulings, majority '{top}' {n}/{len(lv)} = {n/len(lv):.0%}  {dict(cc)}")


if __name__ == '__main__': main()
