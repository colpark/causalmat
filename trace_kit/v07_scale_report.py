"""v07_scale_report.py: the tables behind docs/V07_SCALE.md, computed from batch.csv and the paper trees.

  python3 trace_kit/v07_scale_report.py [--papers <file with one paper per line>]

Prints markdown. Every verdict is model against model.
"""
import csv, json, os, sys, glob, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
PAPERS = os.path.join(ROOT, 'results', 'v07', 'papers')
NOTE = "Every verdict is model against model."
I = lambda v: int(v) if str(v).strip().isdigit() else 0
F = lambda v: float(v) if str(v).replace('.', '', 1).replace('-', '', 1).strip().isdigit() else None


def load(only=None):
    rows = [r for r in csv.DictReader(open(os.path.join(ROOT, 'results', 'v07', 'batch.csv')))]
    if only: rows = [r for r in rows if r['paper'] in only]
    return rows


def gate_rows(p):
    f = os.path.join(PAPERS, p, 'gate.jsonl')
    return [json.loads(l) for l in open(f) if l.strip()] if os.path.exists(f) else []


def funnel(rows):
    k = ['traces_cut', 'open', 'written', 'passed_nets', 'valid', 'text_sufficient', 'inspect']
    t = {x: sum(I(r[x]) for r in rows) for x in k}
    t['valid_partial'] = sum(I(r['valid_partial']) for r in rows)
    out = ["| stage | traces | share of cut |", "|---|---|---|"]
    lab = [('cut by the cutter', 'traces_cut'), ('open after the cutter rules', 'open'),
           ('written', 'written'), ('passed the structural nets', 'passed_nets'),
           ('**valid**', 'valid'), ('text-sufficient', 'text_sufficient'), ('inspect', 'inspect')]
    for name, key in lab:
        out.append(f"| {name} | {t[key]} | {t[key] / t['traces_cut'] * 100:.0f}% |")
    out.append(f"\n{t['valid_partial']} of the {t['valid']} valid items are partial. "
               f"{len(rows)} papers, {t['valid'] / len(rows):.2f} valid per paper.")
    return "\n".join(out), t


def by(rows, keyfn, label):
    g = collections.defaultdict(list)
    for r in rows: g[keyfn(r)].append(r)
    out = [f"| {label} | papers | cut | valid | valid per paper |", "|---|---|---|---|---|"]
    for k in sorted(g, key=lambda x: (x is None, x)):
        rs = g[k]; v = sum(I(r['valid']) for r in rs); c = sum(I(r['traces_cut']) for r in rs)
        out.append(f"| {k if k is not None else '(unknown)'} | {len(rs)} | {c} | {v} | {v / len(rs):.2f} |")
    return "\n".join(out)


def annotated_bands(rows):
    def band(r):
        a = F(r['annotated_share'])
        if a is None: return None
        return '0.00-0.25' if a < .25 else '0.25-0.50' if a < .5 else '0.50-0.75' if a < .75 else '0.75-1.00'
    return by(rows, band, 'annotated share of crops')


def inspect_causes(rows):
    c = collections.Counter()
    for r in rows:
        for part in (r['inspect_cause'] or '').split('/'):
            if ':' in part:
                k, n = part.rsplit(':', 1); c[k] += I(n)
    tot = sum(c.values())
    out = ["| cause | items | share |", "|---|---|---|"]
    for k, n in c.most_common(): out.append(f"| {k} | {n} | {n / tot * 100:.0f}% |")
    return "\n".join(out), tot


def skip_rules(rows):
    c = collections.Counter()
    for r in rows:
        for part in (r['closed_by_rule'] or '').split('/'):
            if ':' in part:
                k, n = part.rsplit(':', 1); c[k] += I(n)
    tot = sum(c.values())
    out = ["| rule | traces closed | share of all closed |", "|---|---|---|"]
    for k, n in c.most_common(): out.append(f"| {k} | {n} | {n / tot * 100:.0f}%|" if tot else f"| {k} | {n} | |")
    return "\n".join(out), tot


def modality(rows):
    c = collections.Counter(); v = collections.Counter()
    for r in rows:
        for g in gate_rows(r['paper']):
            fam = None
            w = os.path.join(PAPERS, r['paper'], 'written.json')
            c[g['verdict']] += 0
    fam_all = collections.Counter(); fam_valid = collections.Counter()
    for r in rows:
        w = os.path.join(PAPERS, r['paper'], 'written.json')
        if not os.path.exists(w): continue
        T = {t['id']: t for t in json.load(open(w))['traces']}
        for g in gate_rows(r['paper']):
            fam = (T.get(g['trace']) or {}).get('fm_family') or '(none)'
            fam_all[fam] += 1
            if g['verdict'] == 'valid': fam_valid[fam] += 1
    out = ["| figure-modality family | gate items | valid | rate |", "|---|---|---|---|"]
    for k, n in fam_all.most_common():
        out.append(f"| {k} | {n} | {fam_valid[k]} | {fam_valid[k] / n * 100:.0f}% |")
    return "\n".join(out)


def knowledge(rows):
    n = 0; papers = 0
    for r in rows:
        w = os.path.join(PAPERS, r['paper'], 'written.json')
        if not os.path.exists(w): continue
        kp = json.load(open(w)).get('knowledge_pile') or []
        if kp: papers += 1
        n += len(kp)
    return n, papers


def panel_check(rows):
    ck = sum(I(r['reread_checks']) for r in rows); fl = sum(I(r['reread_flags']) for r in rows)
    pj = sum(I(r['paneljudge_real']) for r in rows)
    return ck, fl, pj


def cost(rows):
    d = [I(r['subagent_dispatches']) for r in rows]
    w = [F(r['wall_minutes']) for r in rows if F(r['wall_minutes'])]
    return sum(d), sum(d) / len(rows), (sum(w) / len(w) if w else None)


def main(argv):
    only = None
    if '--papers' in argv:
        only = {l.strip() for l in open(argv[argv.index('--papers') + 1]) if l.strip()}
    rows = load(only)
    fn, t = funnel(rows)
    ic, itot = inspect_causes(rows)
    sk, stot = skip_rules(rows)
    kn, kp = knowledge(rows)
    ck, fl, pj = panel_check(rows)
    disp, per, wall = cost(rows)
    P = print
    P(f"# v07 scale: {len(rows)} papers\n")
    P(f"**{NOTE}**\n")
    P("## Funnel\n"); P(fn); P("")
    P("## Yield by journal\n"); P(by(rows, lambda r: r['journal'], 'journal')); P("")
    P("## Yield by year\n"); P(by(rows, lambda r: r['year'] or None, 'year')); P("")
    P("## Yield by annotated share of crops\n"); P(annotated_bands(rows)); P("")
    P("## Yield by figure-modality family\n"); P(modality(rows)); P("")
    P(f"## Inspect causes ({itot} items)\n"); P(ic); P("")
    P(f"## What the cutter closed ({stot} traces)\n"); P(sk); P("")
    P(f"## Knowledge pile\n\n{kn} text-only facts recorded across {kp} papers.\n")
    P(f"## The panel check\n\n{ck} node-panel units checked, {fl} flagged, {pj} ruled a real citation error by the panel judge.")
    if fl: P(f"Panel-judge precision on the flags: {pj / fl * 100:.0f}%.")
    P("")
    P(f"## Cost\n\n{disp} subagent dispatches, {per:.1f} per paper."
      + (f" Median wall time per paper {wall:.0f} min." if wall else ""))
    P(f"\nAt {per:.1f} dispatches per paper, the 16,487-paper corpus projects to {per * 16487 / 1000:.0f}k dispatches "
      f"and {t['valid'] / len(rows) * 16487:,.0f} valid items.")
    P(f"\n{NOTE}")


if __name__ == '__main__': main(sys.argv[1:])
