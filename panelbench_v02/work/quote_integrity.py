"""quote_integrity.py: share of the verified sentences (ref/verified_quotes.json) that sit whole inside ONE
paragraph of <key>.paras.json. Same test as v0.1 (head and tail 30-char anchors after normalisation).
v0.1 pdfplumber score: 188 of 203 body sentences. Usage: python3 quote_integrity.py [paras_suffix]"""
import json, re, sys, unicodedata
suffix = sys.argv[1] if len(sys.argv) > 1 else '.paras.json'
LIG = {'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬀ': 'ff', 'ﬃ': 'ffi', 'ﬄ': 'ffl'}
GREEK = {'α':'alpha','β':'beta','γ':'gamma','μ':'mu','σ':'sigma','κ':'kappa','ρ':'rho','θ':'theta','λ':'lambda','Δ':'delta','δ':'delta','Ω':'omega','ω':'omega','π':'pi','τ':'tau','χ':'chi','ν':'nu','η':'eta','ε':'epsilon'}
def norm(s):
    for a, b in LIG.items(): s = s.replace(a, b)
    s = re.sub(r'\\(text|mathrm|mathbf|mathit|rm)\s*', ' ', s); s = re.sub(r'\\rightarrow|\\to', '', s)
    s = re.sub(r'\\(alpha|beta|gamma|mu|sigma|kappa|rho|theta|lambda|delta|Delta|omega|Omega|pi|tau|chi|nu|eta|epsilon)', lambda m: m.group(1).lower(), s)
    s = re.sub(r'\\(bar|equiv|sim|le|ge|pm)\b', '', s).replace('\\%', '')
    for a, b in GREEK.items(): s = s.replace(a, b)
    s = unicodedata.normalize('NFKD', s)
    return re.sub(r'[^a-z0-9]', '', s.lower())
Q = json.load(open('../ref/verified_quotes.json'))['quotes']
skip = ['###', '**NONE', 'Page Count', 'printed:', 'the entire paper']
T = {'one': 0, 'across': 0, 'missing': 0}
for k, qs in Q.items():
    P = [norm(p['text']) for p in json.load(open(k + suffix))['paras']]; allp = ''.join(P)
    c = {'one': 0, 'across': 0, 'missing': 0}
    for q in qs:
        if any(x in q for x in skip): continue
        n = norm(re.sub(r'\[UNCERTAIN\]', '', q).replace('**', ''))
        h, t = n[:30], n[-30:]
        if any(h in p and t in p for p in P): c['one'] += 1
        elif h in allp or t in allp: c['across'] += 1
        else: c['missing'] += 1
    for x in c: T[x] += c[x]
    print(k, c)
print('TOTAL', T, '(v0.1 pdfplumber: one 188, across 15, missing 8; the 8 missing are titles and headings)')
