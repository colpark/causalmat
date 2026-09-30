#!/bin/bash
# Proves the kit reproduces v0.1 exactly from the v0.1 paragraphs. Run from work/. Expect: identical items,
# 0 new, 0 lost, 53 benchmark items, quote integrity 188.
set -e
for k in Xu17 Hag21 Ye14 Yan20 Mo21 Ahm15; do cp ../ref/$k.paras_v01.json $k.paras.json; done
python3 open.py > /dev/null
python3 - <<'PY'
import json
a=json.load(open('open_items.json'))['items']; b=json.load(open('../ref/open_items_v01.json'))['items']
same=len(a)==len(b) and all(x['id']==y['id'] and x['key']==y['key'] for x,y in zip(a,b))
print('open.py reproduces v0.1 items:', same, len(a))
PY
python3 carry_labels.py
PB_ROOT=selftest_bench python3 build_bench.py
python3 quote_integrity.py | tail -1
rm -rf selftest_bench
