"""segment.py (v2): PDF -> ordered body paragraphs. No model call.

S1  Body font = the most frequent character size in the PDF.
S2  Each page is cut into a left and a right column at the page middle.
S3  Body lines: characters of body size (+-0.3 pt) cluster into lines by their top (0.35 x body size tolerance;
    v2.1 after run 2: ligature glyphs sit 2.7 pt high in Nano Letters). Ligatures expand to letters.
    Every other character whose vertical middle lies within 0.45 x body size of a body line joins
    that line (subscripts, superscripts, symbols). Remaining characters (captions, headers, footers,
    tables, figure text) are dropped, except headings (S7).
S4  Spaces: a pdf space character, or a horizontal gap > 0.15 x body size between characters.
S5  A new paragraph starts when a line is indented >= 4 pt from the column's left edge, or the
    vertical gap to the previous body line exceeds 1.8x the median line pitch, or a heading intervenes.
    A paragraph not ending in . ? ! or : continues into the next column or page.
S6  Line-end hyphen + lowercase next word -> joined.
S7  Headings (v2.1: numbered headings need 'N. Title' with a period, after run 2 caught table cells): a non-body line of < 14 words whose characters are bold or larger than body, OR any line
    matching '<number>. Title' / 'Introduction|Results|Discussion|Conclusion|Experimental|Methods'.
S8  Body starts at the heading containing 'Introduction' (Nano Letters: first body paragraph after
    'KEYWORDS'), and ends at 'References', 'Acknowledg', 'Appendix', 'Supplementary', 'Declaration',
    'Conflict', 'ASSOCIATED CONTENT', 'Supporting Information'.
S5b (v2.3, after run 4): continuation across a column or page ignores the indent test, because a
    paragraph that stops mid-sentence cannot have ended.
S5c (v2.4, after run 5): no paragraph break at all (indent, gap, column, page) while the current
    paragraph is mid-sentence. A sentence end is . ? ! : optionally followed by a citation ([49] or 8-14).
S9  (v2.2) Lines repeating on >= 3 pages (digits masked) are running headers or footers and are dropped.
    Ligature glyphs never get a space before or after them.
S10 (v2.5) Drop caps rejoined; 'Figure 4 a' written as 'Figure 4a'. Back matter starting 'The Supporting
    Information' stops the body.
Output: <key>.paras.json  [{i, section, page, text}]
"""
import pdfplumber, json, re, statistics, collections, sys

HEADRE = re.compile(r'^(\d+(\.\d+)*\.\s+[A-Z][a-z][^.]{2,80}|(Introduction|Results( and [Dd]iscussions?)?|Discussion|Conclusions?|Experimental( [Ss]ection| details)?|Methods|Materials and [Mm]ethods|References|Acknowledg\w*))$')
STOP = re.compile(r'^(\d+\.?\s+)?(The Supporting Information|References|REFERENCES|Acknowledg|ACKNOWLEDG|Appendix|Supplementary|Declaration|Conflict|■?\s*ASSOCIATED CONTENT|Supporting Information|Notes)')

def text_of(chs, body):
    chs = sorted(chs, key=lambda c: c['x0'])
    s, prev = '', None
    for c in chs:
        lig = c['text'] in 'ﬁﬂﬀﬃﬄ' or (prev is not None and prev['text'] in 'ﬁﬂﬀﬃﬄ')
        if prev is not None and not lig and c['text'] != ' ' and not s.endswith(' ') and c['x0'] - prev['x1'] > 0.15 * body:
            s += ' '
        if c['text'] == ' ' and s.endswith(' '):
            continue
        s += c['text']
        prev = c
    for a, b in {'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬀ': 'ff', 'ﬃ': 'ffi', 'ﬄ': 'ffl'}.items():
        s = s.replace(a, b)
    return ' '.join(s.split())

def column_lines(chars, body):
    bodyc = [c for c in chars if abs(c['size'] - body) <= 0.3 and c['text'].strip()]
    bodyc.sort(key=lambda c: c['top'])
    lines = []
    for c in bodyc:
        if lines and abs(c['top'] - lines[-1]['top']) <= 0.35 * body:
            lines[-1]['chars'].append(c)
        else:
            lines.append({'top': c['top'], 'chars': [c]})
    for l in lines:
        l['bottom'] = max(c['bottom'] for c in l['chars'])
        l['mid'] = (l['top'] + l['bottom']) / 2
    used = {id(c) for l in lines for c in l['chars']}
    rest = []
    for c in chars:
        if id(c) in used:
            continue
        m = (c['top'] + c['bottom']) / 2
        best = min(lines, key=lambda l: abs(l['mid'] - m)) if lines else None
        if best and abs(best['mid'] - m) <= 0.45 * body and best['chars'][0]['x0'] - 2 <= c['x0'] <= max(x['x1'] for x in best['chars']) + 2:
            best['chars'].append(c)
        else:
            rest.append(c)
    out = []
    for l in lines:
        t = text_of(l['chars'], body)
        out.append({'kind': 'body', 'top': l['top'], 'x0': min(c['x0'] for c in l['chars'] if c['text'].strip()), 'text': t})
    # heading candidates from the rest
    rl = []
    for c in sorted(rest, key=lambda c: c['top']):
        if not c['text'].strip():
            continue
        if rl and abs(c['top'] - rl[-1]['top']) <= 2:
            rl[-1]['chars'].append(c)
        else:
            rl.append({'top': c['top'], 'chars': [c]})
    for l in rl:
        t = text_of(l['chars'], body)
        bold = sum('Bold' in c['fontname'] or 'bold' in c['fontname'] or c['size'] > body + 0.3 for c in l['chars']) / len(l['chars'])
        if len(t.split()) < 14 and (HEADRE.match(t) or (bold > 0.7 and len(t) > 3 and HEADRE.match(t))):
            out.append({'kind': 'head', 'top': l['top'], 'x0': min(c['x0'] for c in l['chars']), 'text': t})
    # body-size headings (e.g. bold body-size '3. Results and discussion')
    for o in out:
        if o['kind'] == 'body' and len(o['text'].split()) < 14 and HEADRE.match(o['text']):
            o['kind'] = 'head'
    return sorted(out, key=lambda o: o['top'])

END = re.compile(r'[.?!:]\s*(\[\s*[\d,\s–−-]+\]|[\d,–−-]+)?\s*$')
def ended(t):
    return bool(END.search(t))

def join(a, b):
    if re.search(r'[A-Za-z]-$', a) and re.match(r'[a-z]', b):
        return a[:-1] + b
    return a + ' ' + b

def run(key):
    pdf = pdfplumber.open(key + '.pdf')
    sizes = collections.Counter(round(c['size'], 1) for p in pdf.pages for c in p.chars if c['text'].strip())
    body = sizes.most_common(1)[0][0]
    stream = []
    for pn, p in enumerate(pdf.pages, 1):
        mid = p.width / 2
        for side in (0, 1):
            chs = [c for c in p.chars if ((c['x0'] + c['x1']) / 2 < mid) == (side == 0)]
            L = column_lines(chs, body)
            if L:
                stream.append((pn, L))
    # S9 (v2.2, after run 3 found running headers and page footers at body size splitting sentences):
    # a line whose text, digits masked, occurs on 3 or more pages is a running header/footer and is dropped.
    sig = lambda t: re.sub(r'\d+', '#', t.strip())
    pages_of = collections.defaultdict(set)
    for pn, L in stream:
        for l in L:
            pages_of[sig(l['text'])].add(pn)
    stream = [(pn, [l for l in L if len(pages_of[sig(l['text'])]) < 3]) for pn, L in stream]
    stream = [(pn, L) for pn, L in stream if L]
    items = []   # paragraphs and headings in order
    for pn, L in stream:
        B = [l for l in L if l['kind'] == 'body']
        if not B:
            for l in L:
                items.append({'head': l['text'], 'page': pn})
            continue
        left = statistics.median(sorted(l['x0'] for l in B)[:max(1, len(B) // 3)])
        pitch = statistics.median([B[i + 1]['top'] - B[i]['top'] for i in range(len(B) - 1)] or [12])
        first, prev_top = True, None
        for l in L:
            if l['kind'] == 'head':
                items.append({'head': l['text'], 'page': pn}); prev_top = None; first = False
                continue
            indent = l['x0'] - left >= 4
            gap = prev_top is not None and (l['top'] - prev_top) > 1.8 * pitch
            last = items[-1] if items else None
            if last and 'text' in last and not ended(last['text']):
                last['text'] = join(last['text'], l['text'])
            elif last is None or 'head' in last or indent or gap or first:
                items.append({'text': l['text'], 'page': pn})
            else:
                last['text'] = join(last['text'], l['text'])
            first, prev_top = False, l['top']
    out, section, started = [], None, False
    for k, it in enumerate(items):
        if 'head' in it:
            t = it['head']
            if STOP.match(t) and started:
                break
            if re.search(r'ntroduction|INTRODUCTION', t):
                started = True
            section = t
            continue
        t = ' '.join(it['text'].split())
        # S10 (v2.5): Wiley drop caps and link-font gaps: 'F igure 4 a' -> 'Figure 4a', paragraph-initial 'A s' -> 'As'
        t = re.sub(r'^([A-Z]) ([a-z])', r'\1\2', t)
        t = re.sub(r'\bF igure', 'Figure', t)
        t = re.sub(r'\b(Fig(?:ure|s)?\.?\s*\d+)\s+([a-h])(?=\s*[,)\s.;]|$)', r'\1\2', t)
        if STOP.match(t) and started:
            break
        if key == 'Xu17' and not started and any('KEYWORDS' in (x.get('text') or '') for x in items[:k]) and len(t.split()) > 40:
            started = True
        if started and len(t.split()) >= 5:
            out.append({'i': len(out), 'section': section, 'page': it['page'], 'text': t})
    json.dump({'key': key, 'body_size': body, 'paras': out}, open(key + '.paras.json', 'w'), indent=1, ensure_ascii=False)
    return body, out

if __name__ == '__main__':
    for k in sys.argv[1:]:
        body, out = run(k)
        secs = collections.Counter(p['section'] for p in out)
        print(k, 'body', body, 'paras', len(out), 'words', sum(len(p['text'].split()) for p in out))
        for s, n in secs.items():
            print('   ', n, '|', (s or '')[:70])
