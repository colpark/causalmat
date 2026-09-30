"""selftest_adapter.py: builds a synthetic MinerU content_list from each v0.1 paragraph file (headings as
text_level 1, every paragraph broken mid-sentence around an image block) and checks that mineru_paras.py
returns exactly the same body text. Run after any change to mineru_paras.py. Expect 'same text: True' x6."""
import json, re, subprocess, os
os.makedirs('_syn', exist_ok=True)
allok = True
for k in ['Xu17', 'Hag21', 'Ye14', 'Yan20', 'Mo21', 'Ahm15']:
    P = json.load(open('../ref/%s.paras_v01.json' % k))['paras']
    blocks = [{'type': 'text', 'text': 'KEYWORDS: test', 'page_idx': 0}] if k == 'Xu17' else [{'type': 'text', 'text': '1. Introduction', 'text_level': 1, 'page_idx': 0}]
    sec = None
    for p in P:
        if p['section'] != sec and p['section']:
            blocks.append({'type': 'text', 'text': p['section'], 'text_level': 1, 'page_idx': p['page'] - 1}); sec = p['section']
        w = p['text'].split(); h = len(w) // 2
        blocks += [{'type': 'text', 'text': ' '.join(w[:h]), 'page_idx': p['page'] - 1}, {'type': 'image', 'img_path': 'x.jpg', 'page_idx': p['page'] - 1},
                   {'type': 'text', 'text': ' '.join(w[h:]), 'page_idx': p['page'] - 1}]
    blocks.append({'type': 'text', 'text': 'References', 'text_level': 1, 'page_idx': 99})
    json.dump(blocks, open('_syn/%s.json' % k, 'w'))
    subprocess.run(['python3', 'mineru_paras.py', k, '_syn/%s.json' % k, '_syn/%s.paras.json' % k], check=True, capture_output=True)
    Q = json.load(open('_syn/%s.paras.json' % k))['paras']
    same = re.sub(r'\s', '', ' '.join(x['text'] for x in P)) == re.sub(r'\s', '', ' '.join(x['text'] for x in Q))
    allok &= same
    print(k, 'v0.1 paras', len(P), 'adapter paras', len(Q), 'same text:', same)
print('ADAPTER SELF-TEST', 'PASS' if allok else 'FAIL')
