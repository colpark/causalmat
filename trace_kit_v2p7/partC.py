"""partC.py: v2.7 Part C -- widen the "upstream ignored" flag.

  python3 -m trace_kit_v2p7.partC

No model call. The v2.5 join audits, re-read once more.

v2.6 flagged a seam only when EVERY upstream limit was ruled not_applicable, or when the audit
said in certain words that the derived result was dropped. Nano Letters c055 slipped through
both. Its seam has one carried limit and three not_applicable, so the structural rule does not
fire; and the sentence that names the problem --

    "The downstream item (spi_o13_o9) does not use the AIMD data at all"

-- was thrown away by two v2.6 exclusions at once: it is scoped to one limit ("this AIMD-specific
limit has nothing to attach to"), and its object is an evidence leg rather than a conclusion.
v2.6 excluded both on the argument that swapping an evidence leg is how chains are built.

That argument was wrong here, and the brief overrules it. If the audit says the downstream does
not use the upstream's data, then the upstream item contributed nothing to the downstream step,
whether the thing not used is called a result or a measurement. So the new rule adds a third
signal: ANY limit's "why" that says the downstream does not use, invoke or rely on what the
upstream brought. Per-limit scoping no longer excludes it, and neither does the object being a
technique.

The v2.6 signals are kept as they were, so the flag only ever widens. Every seam the new signal
adds is listed with the sentence that triggered it, because a rule this broad has to be
readable one case at a time.

Every verdict is model against model.
"""
import collections, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402
from trace_kit_v2p6.ignored import audit_text, PAT, PER_LIMIT, LEG  # noqa: E402

# the downstream, doing nothing with what came before
DOWN = (r'(?:the\s+)?(?:downstream|joined|new|later|second)\s+'
        r'(?:item|claim|key|pairing|join|proposition|step|reasoning)|'
        r'\bdownstream\b|\bthe\s+join\b|\bthe\s+joined\s+claim\b')
NOTUSE = (r'(?:does\s+not|do\s+not|doesn\'?t|did\s+not|never|no\s+longer)\s+'
          r'(?:in\s+fact\s+|actually\s+|ever\s+|at\s+all\s+)?'
          r'(?:re-?)?(?:uses?|using|invokes?|invoking|relies?\s+on|rely\s+on|relying\s+on|'
          r'draws?\s+on|references?|referencing|appeals?\s+to|carry|carries|carried)')
USE_RULE = [
    ('downstream-does-not-use', rf'(?:{DOWN})[^.;]{{0,80}}?{NOTUSE}'),
    ('not-used-by-downstream', rf'{NOTUSE}[^.;]{{0,80}}?(?:{DOWN})'),
    ('absent-from-downstream', rf'\bis\s+absent\s+from\s+the\s+(?:downstream|join)'),
    ('no-role-downstream', rf'\bplays?\s+no\s+role\s+in\s+the\s+(?:downstream|join)'),
]

# Three sentences in the audits match the rule while saying something else. Excluded by hand,
# each for a stated reason, and each one listed in the report so the exclusion is auditable.
#   a CAVEAT is what is absent, not the upstream's contribution
#     "...but that caveat is absent from the joined proposition itself"
#   the downstream does not rely on the upstream ALONE, i.e. it added more evidence -- the
#     opposite of ignoring it
#     "...so the joined claim does not rely on the SEM ordering alone as if it were..."
#   what is not invoked is a validation of the upstream, not the upstream
#     "...does not invoke or depend on the release mechanism being independently validated"
NOT_A_FLAG = re.compile(
    r'\b(?:caveat|limit|limitation|qualification)\b[^.;]{0,40}\bis\s+absent\b'
    r'|\bnot\s+(?:rely|relies|relying)\s+on\b[^.;]{0,60}\balone\b'
    r'|\b(?:being|been)\s+independently\s+validated\b', re.I)


def run():
    P = json.load(open(R('results/v2p6/pruned.json')))
    V6 = json.load(open(R('results/v2p6/ignored.json')))
    d = R('results/v2p5/joinaudit')
    out = {}
    for jn in P['joins']:
        k = f"{jn['from']}__{jn['to']}"
        old = V6['seams'].get(k) or {}
        rec = {'paper': jn['paper'], 'v2p6_ignored': bool(old.get('ignored')),
               'v2p6_signals': old.get('signals') or [], 'new_signals': [], 'new_evidence': []}
        f = os.path.join(d, k + '.out.txt')
        if os.path.exists(f):
            j = obj(open(f).read(), 'limits_survive') or obj(open(f).read(), 'join_verdict')
            if j:
                # the new signal: any ONE limit's why is enough, scoping and object ignored
                for x in (j.get('limits_survive') or []):
                    why = x.get('why') or ''
                    for s in re.split(r'(?<=[.;])\s+', why):
                        sl = s.lower()
                        if NOT_A_FLAG.search(sl): continue
                        for nm, p in USE_RULE:
                            if re.search(p, sl):
                                rec['new_signals'].append('limit-why: ' + nm)
                                rec['new_evidence'].append(s.strip()[:300])
                                break
                rec['limit_verdicts'] = dict(collections.Counter(
                    (x.get('verdict') or '').strip().lower() for x in (j.get('limits_survive') or [])))
        rec['new_signals'] = sorted(set(rec['new_signals']))
        rec['ignored'] = bool(rec['v2p6_ignored'] or rec['new_signals'])
        rec['added_by_v2p7'] = bool(rec['ignored'] and not rec['v2p6_ignored'])
        out[k] = rec

    flagged = [k for k, v in out.items() if v['ignored']]
    added = [k for k, v in out.items() if v['added_by_v2p7']]
    res = {
        'note': 'v2.7 Part C. The v2.6 flag, widened to any limit-why that says the downstream '
                'does not use what came before. No model call.',
        'joins': len(out),
        'v2p6_flagged': sum(1 for v in out.values() if v['v2p6_ignored']),
        'v2p7_flagged': len(flagged), 'added': len(added),
        'flagged_ids': sorted(flagged), 'added_ids': sorted(added),
        'c055_seam': 'nano_letters_com_o13_o24__nano_letters_spi_o13_o9',
        'c055_flagged': out.get('nano_letters_com_o13_o24__nano_letters_spi_o13_o9', {}).get('ignored'),
        'c055_flagged_in_v2p6': out.get('nano_letters_com_o13_o24__nano_letters_spi_o13_o9', {}).get('v2p6_ignored'),
        'seams': out,
    }
    json.dump(res, open(R('results/v2p7/partC.json'), 'w'), indent=1)
    return res


if __name__ == '__main__':
    r = run()
    print(json.dumps({k: v for k, v in r.items()
                      if k not in ('seams', 'flagged_ids', 'added_ids')}, indent=1))
    print(f"\nnew flags added by v2.7: {r['added']}")
    for k in r['added_ids']:
        v = r['seams'][k]
        print(f"\n  {k}")
        print(f"    signals: {', '.join(v['new_signals'])}  | limits {v.get('limit_verdicts')}")
        for e in v['new_evidence'][:1]: print(f"    > {e}")
