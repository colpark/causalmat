"""audit.py: the v5 audit and the quantity-kind check, applied to v2.5 items.

  python3 trace_kit_v2p5/audit.py prompts [n_per_generator]
  python3 trace_kit_v2p5/audit.py collect

Two things carried over from v5b, both learned the hard way there.

**The quantity-kind check needs both sides' numbers.** In v5 it was shown one step's observations
and then called the other step's quantities absent. Here each item IS a pair, so both observations
go in the prompt.

**Its rulings are reviewed, not applied.** In v5 it ruled 14 of 26 mixed; hand review found 7
genuine, 2 borderline and 5 category errors, because it treats any proposition RELATING two
different quantities as a mismatch -- which is what a covariation item is for. So the prompt now
draws that distinction explicitly, and a mixed ruling is still recorded for review rather than
auto-applied to the key.

Sampling is stratified by generator so a rate can be quoted per generator, as the brief asks.

Every verdict is model against model.
"""
import json, os, re, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

CHECK_ASK = """You are auditing an answer key against the two observations it was written from.

For the proposition and for EACH limit separately, rule one of:

  holds       every quantity and direction it states is in the observations, and the inference it
              draws is available from them
  overreaches states something the observations support only weakly or in a weaker form -- a cause
              where only an association is available, a relationship where only an ordering is
  wrong       contradicts the observations, or cites a number or direction that is not there

Quote the observation you rule against. Where a statement fails, give corrected wording as close to
the original as the evidence allows.

Reply as JSON only:
{"proposition": {"verdict": "...", "evidence": "...", "fix": "..." or null},
 "limits": [{"index": 0, "verdict": "...", "evidence": "...", "fix": "..." or null}]}"""

QK_ASK = """Does this proposition compare quantities of different KINDS?

Be careful about one distinction, because getting it wrong is the common failure here:

  NOT a mismatch: a proposition that RELATES two different quantities -- a yield stress against a
  particle density, a domain size against a spectral feature count, a release rate against a surface
  area. Relating two different quantities across the same samples is what a covariation or a
  mechanism check IS. That is the item working, not an error.

  A mismatch: two quantities SET AGAINST EACH OTHER as if they were the same kind -- a charge
  capacity against a discharge capacity, a rate against an accumulated amount, a test temperature
  against a service temperature, a yield stress against a fracture or flow stress, an instantaneous
  value against a time-averaged one, a value at one cycle against a value at another.

Rule `same_kind` or `mixed`. If mixed, quote both quantities, name each kind, and say whether the
observations contain a same-kind pair that could be used instead. If they do not, the repair is to
state the mismatch as a limit, not to substitute numbers that are not there.

Reply as JSON only:
{"ruling": "same_kind" or "mixed", "quantity_a": "...", "kind_a": "...",
 "quantity_b": "...", "kind_b": "...", "same_kind_pair_available": true or false,
 "limit_to_add": "..." or null}"""


def packet(it):
    k = it['key']
    L = [f"Question: {it['question']}", "",
         f"Observation A ({it['observation_a']['technique']}): {it['observation_a']['text']}",
         f"Observation B ({it['observation_b']['technique']}): {it['observation_b']['text']}", "",
         f"Proposition: {k.get('proposition')}", "", "Limits:"]
    for n, l in enumerate(k.get('limits') or []): L.append(f"  [{n}] {l}")
    return "\n".join(L)


def prompts(n_per=25):
    D = json.load(open(os.path.join(ROOT, 'results/v2p5/items.json')))
    have = [i for i in D['items'] if i.get('key')]
    bygen = collections.defaultdict(list)
    for i in have: bygen[i['generator']].append(i)
    pick = []
    for gen, its in bygen.items():
        # stratify within a generator by paper so one paper cannot dominate a rate
        bypaper = collections.OrderedDict()
        for i in its: bypaper.setdefault(i['paper'], []).append(i)
        while len([p for p in pick if p['generator'] == gen]) < min(n_per, len(its)):
            moved = False
            for p in list(bypaper):
                if len([x for x in pick if x['generator'] == gen]) >= min(n_per, len(its)): break
                if bypaper[p]: pick.append(bypaper[p].pop(0)); moved = True
            if not moved: break
    d1 = os.path.join(ROOT, 'results/v2p5/check'); os.makedirs(d1, exist_ok=True)
    d2 = os.path.join(ROOT, 'results/v2p5/qkind'); os.makedirs(d2, exist_ok=True)
    a, b = [], []
    for it in pick:
        f = os.path.join(d1, it['item'] + '.txt')
        open(f, 'w').write(packet(it) + "\n\n" + CHECK_ASK)
        a.append({'id': it['item'], 'agent': 'net-judge', 'prompt': os.path.abspath(f),
                  'out': os.path.abspath(os.path.join(d1, it['item'] + '.out.txt'))})
        f = os.path.join(d2, it['item'] + '.txt')
        open(f, 'w').write(packet(it) + "\n\n" + QK_ASK)
        b.append({'id': it['item'], 'agent': 'net-judge', 'prompt': os.path.abspath(f),
                  'out': os.path.abspath(os.path.join(d2, it['item'] + '.out.txt'))})
    json.dump(a, open(os.path.join(ROOT, '.v07work/batch_v2p5_audit.json'), 'w'), indent=1)
    json.dump(b, open(os.path.join(ROOT, '.v07work/batch_v2p5_qk.json'), 'w'), indent=1)
    print(f"{len(a)} audit jobs and {len(b)} quantity-kind jobs over "
          f"{dict(collections.Counter(i['generator'] for i in pick))}")
    print(f"  papers represented: {len({i['paper'] for i in pick})}")


def _obj(t, want):
    out, d, s = [], 0, None
    for i, c in enumerate(t or ''):
        if c == '{':
            if d == 0: s = i
            d += 1
        elif c == '}' and d:
            d -= 1
            if not d: out.append(t[s:i + 1])
    for o in sorted(out, key=len, reverse=True):
        for cand in (o, re.sub(r',(\s*[}\]])', r'\1', o)):
            try:
                j = json.loads(cand)
                if want in j: return j
            except Exception: continue
    return None


def vnorm(v):
    v = (v or '').strip().lower()
    for k in ('overreach', 'wrong', 'holds'):
        if k in v: return {'overreach': 'overreaches'}.get(k, k)
    return None


def collect():
    D = json.load(open(os.path.join(ROOT, 'results/v2p5/items.json')))
    I = {i['item']: i for i in D['items']}
    tally = collections.Counter(); qk = collections.Counter()
    for j in json.load(open(os.path.join(ROOT, '.v07work/batch_v2p5_audit.json'))):
        r = _obj(open(j['out']).read(), 'proposition') if os.path.exists(j['out']) else None
        if not r: tally['unparsed'] += 1; continue
        it = I[j['id']]; gen = it['generator']
        pv = vnorm((r.get('proposition') or {}).get('verdict'))
        tally[f'{gen}|proposition|{pv}'] += 1
        st = [{'what': 'proposition', 'verdict': pv,
               'evidence': (r.get('proposition') or {}).get('evidence'),
               'fix': (r.get('proposition') or {}).get('fix')}]
        for L in (r.get('limits') or []):
            lv = vnorm(L.get('verdict'))
            tally[f'{gen}|limit|{lv}'] += 1
            st.append({'what': f"limit[{L.get('index')}]", 'verdict': lv,
                       'evidence': L.get('evidence'), 'fix': L.get('fix')})
        it['audit'] = {'checked': True, 'statements': st}
    for j in json.load(open(os.path.join(ROOT, '.v07work/batch_v2p5_qk.json'))):
        r = _obj(open(j['out']).read(), 'ruling') if os.path.exists(j['out']) else None
        if not r: qk['unparsed'] += 1; continue
        it = I[j['id']]
        rule = 'mixed' if str(r.get('ruling', '')).lower().startswith('mix') else 'same_kind'
        qk[f"{it['generator']}|{rule}"] += 1
        it['quantity_kind'] = {'ruling': rule, 'a': r.get('quantity_a'), 'kind_a': r.get('kind_a'),
                               'b': r.get('quantity_b'), 'kind_b': r.get('kind_b'),
                               'same_kind_pair_available': r.get('same_kind_pair_available'),
                               'limit_to_add': r.get('limit_to_add'),
                               'applied': False,
                               'note': 'recorded for review, not applied: in v5b this checker '
                                       'produced 5 category errors in 14 mixed rulings'}
    json.dump(D, open(os.path.join(ROOT, 'results/v2p5/items.json'), 'w'), indent=1)
    print("audit, per generator:")
    for gen in ('covariation', 'complementary', 'spine_edge'):
        pr = {k.split('|')[-1]: v for k, v in tally.items() if k.startswith(f'{gen}|proposition|')}
        li = {k.split('|')[-1]: v for k, v in tally.items() if k.startswith(f'{gen}|limit|')}
        if not pr: continue
        pt = sum(pr.values()); lt = sum(li.values())
        print(f"  {gen:14s} propositions {pr.get('holds',0)}/{pt} hold {pr}   "
              f"limits {li.get('holds',0)}/{lt} hold {li}")
    print(f"\nquantity-kind (recorded, not applied): "
          f"{ {k: v for k, v in qk.items()} }")


if __name__ == '__main__': {'prompts': lambda: prompts(int(sys.argv[2]) if len(sys.argv) > 2 else 25),
                            'collect': collect}[sys.argv[1]]()
