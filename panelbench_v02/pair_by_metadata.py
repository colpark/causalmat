"""Pair lost v0.1 items with new v0.2 items on metadata only (paper, level, panels, page, key value). Prints ids, no text."""
import json
m=json.load(open('v02_to_v01_match.json'))
v1={x['id']:x for x in json.load(open('../ref/open_items_v01.json'))['items']}; v2={x['id']:x for x in json.load(open('open_items.json'))['items']}
L1=json.load(open('../ref/open_labels_v01.json'))
carried={v[0] for v in m.values() if v and v[0]}
lost=[i for i in v1 if i not in carried]; new=[i for i in v2 if not (m.get(i) and m[i][0])]
sig=lambda x:(x['paper'],x['level'],tuple(sorted(x['panels'])),x['page'],x.get('key_value'))
print('\nMetadata pairing of lost v0.1 items to new v0.2 items (same paper, level, panels, page, key value):')
used=set(); exact=part=0
for i in lost:
    c=[j for j in new if j not in used and sig(v2[j])==sig(v1[i])]
    c2=[j for j in new if j not in used and sig(v2[j])[:4]==sig(v1[i])[:4]]
    if c: used.add(c[0]); exact+=1; print(f'  {i} ({L1[i][0]}) -> {c[0]}  same metadata and key value')
    elif c2: used.add(c2[0]); part+=1; print(f'  {i} ({L1[i][0]}) -> {c2[0]}  same paper/level/panels/page, key value differs')
    else: print(f'  {i} ({L1[i][0]}) -> no counterpart')
print('pairs: exact', exact, 'partial', part, 'of', len(lost), 'lost | new items with no v0.1 counterpart:', [j for j in new if j not in used])
