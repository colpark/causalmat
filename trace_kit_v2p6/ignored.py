"""ignored.py: v2.6 step 3 -- flag seams where the downstream never uses the upstream result.

  python3 -m trace_kit_v2p6.ignored

No model call. Reads the v2.5 join audits that already exist and re-reads what they said.

The failure the external review found on the Nano Letters page: a seam can show "every limit
survives" while the downstream claim never touches what the upstream item concluded. No limit
is ruled dropped, because there is nothing downstream for an upstream limit to qualify. The
seam looks clean for the same reason it is empty.

Two signals, both the audit's own words:

  structural  Every upstream limit ruled not_applicable. not_applicable is the audit saying
              this qualification has no object in the downstream claim. When that is true of
              EVERY limit, the upstream result as qualified has no purchase at all -- the
              downstream is reusing a raw observation, not the conclusion drawn from it.

  prose       The audit states the downstream drops or ignores the upstream derived result.
              This needs care. "The downstream item drops HRTEM entirely" is normal: the
              downstream is a different pair of observations and swapping an evidence leg is
              how chains are built. What counts is the RESULT being dropped, as in "drops the
              XANES-derived metallic-Co-state claim entirely". Sentences scoped to a single
              limit -- "this limit has nothing to attach to", "this particular concern is not
              re-invoked" -- are excluded: that is not_applicable restated, not an ignored
              result. Of 17 tight-pattern matches, 13 were per-limit and were excluded.

A flagged seam cannot be told "every limit survives". It is labelled "upstream ignored".

Every verdict is model against model.
"""
import json, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, R('trace_kit_v2p5'))
from pages import obj  # noqa: E402

W = r"[a-z0-9\-'’/()]+"
PAT = [
    ('drops-the-result',
     rf"\b(?:drops?|dropped|discards?|abandons?)\s+(?:the|its|upstream'?s?)?\s*(?:{W}\s+){{0,4}}"
     r"(?:claim|conclusion|result|finding|inference|proposition)\b"),
    ('plays-no-role', r'\b(?:plays?|played)\s+no\s+(?:role|part)\b'),
    ('never-invoked',
     r'\b(?:claim|conclusion|result|finding|inference|proposition)\b[^.]{0,60}'
     r'\b(?:is|are|was|were)\s+(?:simply\s+|ever\s+)?(?:never|not)\s+invoked\b'),
    ('not-invoked-at-all',
     r'\b(?:never|not)\s+(?:re-?)?invoke[sd]?\b[^.]{0,40}\b(?:upstream|step\s?1|earlier|prior|previous)\b'),
    ('no-value-from-upstream', r'\bdoes not (?:in fact )?use any\b[^.]{0,60}\bfrom\b'),
    ('topic-mismatch', r'\btopic mismatch\b'),
    ('upstream-not-used',
     r'\bupstream\s+(?:claim|result|conclusion|key|finding|item)\b[^.]{0,90}\b(?:not|never)\b'
     r'[^.]{0,50}\b(?:used|invoked|carried|referenced|relied)\b'),
]
# A sentence that scopes itself to one limit is not_applicable in prose. Not an ignored result.
# "this limit", but also "this SIMS-specific limitation", "this particular circularity concern",
# "this upstream limit": up to two words may sit between the demonstrative and the noun.
PER_LIMIT = re.compile(
    r"\bthis\s+(?:[a-z0-9\-\u2019']+\s+){0,2}(?:limit|limits|limitation|caveat|concern|caution|"
    r"issue|worry|qualification|point|objection)\b|\bthe\s+limit\b|\blimit's\b")

# An evidence leg is not a result. "never invokes upstream Observation A" is the downstream
# using a different pair of observations, which is how every chain is built.
LEG = re.compile(r"\b(?:observation|evidence|panel|image|micrograph|spectrum|spectra|curve|"
                 r"dataset|data)\b\s*[ab]?\b")


def audit_text(j):
    t = [(j.get('proposition') or {}).get('evidence') or '']
    t += [x.get('why') or '' for x in (j.get('limits_survive') or [])]
    t += [j.get('note_for_caller') or '', j.get('fix') or '']
    return t


def run():
    P = json.load(open(R('results/v2p6/pruned.json')))
    joins = P['joins']
    d = R('results/v2p5/joinaudit')
    out, unparsed = {}, []
    for jn in joins:
        k = f"{jn['from']}__{jn['to']}"
        f = os.path.join(d, k + '.out.txt')
        if not os.path.exists(f):
            unparsed.append(k); out[k] = {'ignored': False, 'why': 'no audit file', 'signals': []}
            continue
        raw = open(f).read()
        j = obj(raw, 'limits_survive') or obj(raw, 'join_verdict')
        if not j:
            unparsed.append(k); out[k] = {'ignored': False, 'why': 'audit not parseable', 'signals': []}
            continue
        vs = [(x.get('verdict') or '').strip().lower() for x in (j.get('limits_survive') or [])]
        sig, ev = [], []
        if vs and all(v == 'not_applicable' for v in vs):
            sig.append('structural: every upstream limit not_applicable')
            ev.append(f'{len(vs)} of {len(vs)} limits ruled not_applicable')
        for t in audit_text(j):
            for s in re.split(r'(?<=[.;])\s+', t):
                sl = s.lower()
                if PER_LIMIT.search(sl): continue
                for nm, p in PAT:
                    m = re.search(p, sl)
                    if not m: continue
                    # what was said not to be used: skip if it is an evidence leg, not a result
                    if LEG.search(sl[m.start():m.end() + 30]): break
                    sig.append('prose: ' + nm); ev.append(s.strip()[:320]); break
        out[k] = {'ignored': bool(sig), 'signals': sorted(set(sig)), 'evidence': ev[:3],
                  'limit_verdicts': dict(collections.Counter(vs)),
                  'no_limit_dropped': bool(vs) and 'dropped' not in vs,
                  'paper': jn['paper']}
    flagged = [k for k, v in out.items() if v['ignored']]
    res = {
        'note': 'v2.6 step 3. No model call: the v2.5 join audits, re-read.',
        'joins': len(joins), 'flagged': len(flagged),
        'flagged_ids': sorted(flagged),
        'unparsed': unparsed,
        'by_signal': dict(collections.Counter(
            s.split(':')[0] for k in flagged for s in out[k]['signals'])),
        'both_signals': sum(1 for k in flagged
                            if len({s.split(':')[0] for s in out[k]['signals']}) > 1),
        'flagged_but_showed_every_limit_survives':
            sorted(k for k in flagged if out[k]['no_limit_dropped']),
        'seams': out,
    }
    json.dump(res, open(R('results/v2p6/ignored.json'), 'w'), indent=1)
    return res


if __name__ == '__main__':
    r = run()
    print(json.dumps({k: v for k, v in r.items() if k != 'seams'}, indent=1))
