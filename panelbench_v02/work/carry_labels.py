"""carry_labels.py: give v0.2 items the v0.1 hand label when the item is the same question.
Same question = same paper, same level, and the same signature (normalised key + its source sentence or
paragraph): exact first, then the best fuzzy pairs with difflib ratio >= 0.90 (extraction noise such as
'Cu2 S' vs 'Cu2S'). Every other v0.2 item gets 'unreviewed' and stays OUT of the
benchmark until Claude reviews it (NEW_ITEMS.md lists them). Also reports v0.1 items that v0.2 lost."""
import json, re, difflib
n = lambda s: re.sub(r'[^a-z0-9]', '', (s or '').lower())
v1 = json.load(open('../ref/open_items_v01.json'))['items']; L1 = json.load(open('../ref/open_labels_v01.json'))
v2 = json.load(open('open_items.json'))['items']
labels, match, used = {}, {}, set()
sig = lambda it: n(it['key']) + '|' + n(it.get('source') or it.get('paragraph') or '')
# pass 1: exact signature (key AND its source sentence or paragraph)
for it in v2:
    for o in v1:
        if o['id'] not in used and o['paper'] == it['paper'] and o['level'] == it['level'] and sig(o) == sig(it):
            used.add(o['id']); match[it['id']] = (o['id'], 1.0); break
# pass 2: fuzzy on the same signature, best pair first, ratio >= 0.90
cand = []
for it in v2:
    if it['id'] in match: continue
    for o in v1:
        if o['id'] in used or o['paper'] != it['paper'] or o['level'] != it['level']: continue
        cand.append((difflib.SequenceMatcher(None, sig(o), sig(it)).ratio(), it['id'], o['id']))
for r, iid, oid in sorted(cand, reverse=True):
    if r < 0.90: break
    if iid in match or oid in used: continue
    used.add(oid); match[iid] = (oid, round(r, 3))
for it in v2:
    if it['id'] in match:
        oid = match[it['id']][0]
        labels[it['id']] = [L1[oid][0], L1[oid][1] + ' (carried from v0.1 %s)' % oid]
    else:
        labels[it['id']] = ['unreviewed', 'new in v0.2, needs review before entering the benchmark']
json.dump(labels, open('open_labels.json', 'w'), indent=1, ensure_ascii=False)
json.dump(match, open('v02_to_v01_match.json', 'w'), indent=1)
lost = [o['id'] for o in v1 if o['id'] not in used]
new = [it for it in v2 if labels[it['id']][0] == 'unreviewed']
with open('NEW_ITEMS.md', 'w') as f:
    f.write('# v0.2 items without a v0.1 match (%d)\n\n' % len(new))
    for it in new:
        f.write('## %s (%s, L%d, panels %s, p.%s)\n\nKey: %s\n\nSource: %s\n\n' % (it['id'], it['paper'], it['level'], ', '.join(it['panels']), it['page'], it['key'], it.get('source') or it.get('paragraph', '')[:600]))
    f.write('# v0.1 items with no v0.2 match (%d)\n\n%s\n' % (len(lost), ', '.join(lost)))
import collections
print('carried', collections.Counter(v[0] for v in labels.values()), 'new', len(new), 'lost from v0.1', len(lost))
