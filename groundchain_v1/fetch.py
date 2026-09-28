"""fetch.py: Stage 1 fetch. Europe PMC JATS first, then publisher HTML.

  python3 groundchain_v1/fetch.py probe <doi> [...]   can we get figures? no files written
  python3 groundchain_v1/fetch.py get <doi> [...]     write m2m_corpus/<folder>/

Writes the MatMech layout exactly -- data.json with image_info[{image_path, image_caption,
image_description}] and images/<sha256>.jpg -- so scripts/panels/detect_panels.py and
match_panels.py run over m2m_corpus unchanged.

No model call.
"""
import hashlib, io, json, os, re, sys, time, urllib.parse, urllib.request, zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CORPUS, OUT

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/124.0 Safari/537.36 groundchain/1.0 (mailto:dpark2129@gmail.com)')
EPMC = 'https://www.ebi.ac.uk/europepmc/webservices/rest'


def folder_for(doi):
    return doi.replace('/', '_')


def fetch(url, binary=False, tries=3, timeout=45):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': UA, 'Accept': '*/*', 'Accept-Language': 'en'})
            with urllib.request.urlopen(req, timeout=timeout) as f:
                b = f.read()
                return b if binary else b.decode('utf-8', 'replace')
        except Exception as e:
            if i == tries - 1: return None
            time.sleep(1.2 * (i + 1))
    return None


def strip(x):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', x or '')).strip()


# ---------------------------------------------------------------- Europe PMC JATS

def epmc_figs(pmcid):
    """(caption, [graphic hrefs]) per figure, from the JATS full text"""
    xml = fetch(f'{EPMC}/{pmcid}/fullTextXML')
    if not xml or '<fig' not in xml: return None, None
    figs = []
    for m in re.finditer(r'<fig\b.*?</fig>', xml, re.S):
        blk = m.group(0)
        cap = strip(re.search(r'<caption>.*?</caption>', blk, re.S).group(0)
                    if re.search(r'<caption>.*?</caption>', blk, re.S) else '')
        lbl = strip(re.search(r'<label>(.*?)</label>', blk, re.S).group(1)
                    if re.search(r'<label>(.*?)</label>', blk, re.S) else '')
        hrefs = re.findall(r'xlink:href="([^"]+)"', blk) or re.findall(r'href="([^"]+)"', blk)
        figs.append({'label': lbl, 'caption': (lbl + '. ' + cap).strip('. '), 'hrefs': hrefs})
    # body text, for the "use" sentences match_panels needs
    body = re.search(r'<body>.*?</body>', xml, re.S)
    return figs, strip(body.group(0) if body else '')


_ZIP = {}


def epmc_zip(pmcid):
    """Europe PMC's supplementaryFiles zip, which is where the figure images actually live.

    The obvious routes all fail: europepmc.org/articles/<pmc>/bin/<file> returns 403, this
    article is not in NCBI's OA subset (oa.fcgi 404s) and Unpaywall has no pdf for it. The
    supplementaryFiles endpoint returns 200 and the zip holds the figure jpgs under exactly the
    filenames the JATS xlink:href gives. One download per paper, cached.
    """
    if pmcid in _ZIP: return _ZIP[pmcid]
    b = fetch(f'{EPMC}/{pmcid}/supplementaryFiles', binary=True, timeout=180)
    z = None
    if b and len(b) > 1000:
        try:
            z = zipfile.ZipFile(io.BytesIO(b))
        except Exception:
            z = None
    _ZIP[pmcid] = z
    return z


def epmc_image(pmcid, href):
    z = epmc_zip(pmcid)
    if not z: return None
    want = href.rsplit('/', 1)[-1]
    stem = re.sub(r'\.(gif|tif|tiff|jpg|jpeg|png)$', '', want, flags=re.I).lower()
    names = z.namelist()
    # exact name first, then the same stem with a raster extension, preferring jpg over gif
    order = ([n for n in names if n.rsplit('/', 1)[-1].lower() == want.lower()]
             + [n for n in names
                if re.sub(r'\.(gif|tif|tiff|jpg|jpeg|png)$', '', n.rsplit('/', 1)[-1], flags=re.I)
                .lower() == stem and n.lower().endswith(('.jpg', '.jpeg', '.png'))]
             + [n for n in names
                if re.sub(r'\.(gif|tif|tiff|jpg|jpeg|png)$', '', n.rsplit('/', 1)[-1], flags=re.I)
                .lower() == stem])
    for n in order:
        try:
            blob = z.read(n)
        except Exception:
            continue
        if len(blob) > 8000 and blob[:3] in (b'\xff\xd8\xff', b'\x89PN'):
            return blob
    return None


# ---------------------------------------------------------------- publisher HTML

FIGPAT = [
    # RSC, ACS, Springer, IOP, ECS all expose <figure> with an <img> and a caption block
    (re.compile(r'<figure\b.*?</figure>', re.S), None),
    (re.compile(r'<div[^>]+class="[^"]*(?:figure|fig-item|article-figure)[^"]*".*?</div>', re.S), None),
]
IMGSRC = re.compile(r'<img[^>]+(?:data-src|src)="([^"]+)"', re.I)
CAPTXT = re.compile(r'<(?:figcaption|div[^>]+class="[^"]*caption[^"]*")\b.*?</(?:figcaption|div)>', re.S)


def html_figs(url, base):
    html = fetch(url)
    if not html: return None, None, 'fetch failed'
    figs = []
    for pat, _ in FIGPAT:
        for m in pat.finditer(html):
            blk = m.group(0)
            srcs = [s for s in IMGSRC.findall(blk)
                    if re.search(r'\.(jpe?g|png|gif)(\?|$)', s, re.I)
                    or '/image/' in s or 'graphic' in s.lower()]
            cap = strip(CAPTXT.search(blk).group(0) if CAPTXT.search(blk) else '')
            if srcs:
                figs.append({'label': '', 'caption': cap,
                             'hrefs': [urllib.parse.urljoin(base, s) for s in srcs]})
        if figs: break
    body = strip(re.sub(r'<(script|style)\b.*?</\1>', ' ', html, flags=re.S))
    return figs, body, None


def landing(doi):
    """follow the DOI to wherever the publisher puts the article"""
    try:
        req = urllib.request.Request('https://doi.org/' + urllib.parse.quote(doi),
                                     headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=40) as f:
            return f.geturl(), f.read().decode('utf-8', 'replace')
    except Exception as e:
        return None, None


def probe(dois):
    E = json.load(open(os.path.join(OUT, 'select_epmc.json')))['recs']
    res = {}
    for doi in dois:
        r = {'doi': doi, 'route': None, 'n_figs': 0, 'n_images_ok': 0, 'note': None}
        pm = (E.get(doi) or {}).get('pmcid')
        if pm:
            figs, body = epmc_figs(pm)
            if figs:
                r.update(route='epmc', n_figs=len(figs), body_chars=len(body or ''))
                got = 0
                for f in figs[:3]:
                    for h in f['hrefs'][:2]:
                        if epmc_image(pm, h): got += 1; break
                r['n_images_ok'] = got
                r['sampled'] = min(3, len(figs))
        if not r['route'] or r['n_images_ok'] == 0:
            url, html = landing(doi)
            r['landing'] = (url or '')[:90]
            if url:
                figs, body, err = html_figs(url, url)
                if figs:
                    got = 0
                    for f in figs[:3]:
                        b = fetch(f['hrefs'][0], binary=True)
                        if b and len(b) > 8000: got += 1
                    r.update(route='html', n_figs=len(figs), n_images_ok=got,
                             sampled=min(3, len(figs)), body_chars=len(body or ''))
                else:
                    r['note'] = err or 'no figure blocks found'
            else:
                r['note'] = 'doi did not resolve'
        res[doi] = r
        print(f"  {doi[:42]:42s} route={str(r['route']):5s} figs={r['n_figs']:3d} "
              f"img_ok={r['n_images_ok']}/{r.get('sampled', 0)} {r['note'] or ''}")
        time.sleep(0.4)
    return res

# ---------------------------------------------------------------- write the MatMech layout

def write_paper(doi, figs, body, route, pmcid=None, title=None, year=None):
    """m2m_corpus/<doi folder>/{data.json,images/} -- byte-identical in shape to MatMech."""
    fold = os.path.join(CORPUS, folder_for(doi))
    imgs = os.path.join(fold, 'images')
    os.makedirs(imgs, exist_ok=True)
    info, kept, dropped = [], 0, []
    for f in figs:
        blob = None
        for h in f['hrefs']:
            blob = epmc_image(pmcid, h) if route == 'epmc' else fetch(h, binary=True)
            if blob and len(blob) > 8000 and blob[:3] in (b'\xff\xd8\xff', b'\x89PN'):
                break
            blob = None
        if not blob:
            dropped.append(f.get('label') or f['caption'][:40]); continue
        ext = '.png' if blob[:3] == b'\x89PN' else '.jpg'
        name = hashlib.sha256(blob).hexdigest() + ext
        open(os.path.join(imgs, name), 'wb').write(blob)
        info.append({'image_path': f'images/{name}',
                     'image_caption': [f['caption']],
                     'image_description': [body[:4000]] if body else []})
        kept += 1
    data = {'doi': doi, 'title': title, 'year': year,
            'source': {'route': route, 'pmcid': pmcid},
            'body_text': body or '',
            'image_info': info}
    json.dump(data, open(os.path.join(fold, 'data.json'), 'w'), indent=1)
    return {'doi': doi, 'folder': folder_for(doi), 'figures': kept,
            'figures_dropped': len(dropped), 'route': route}


def get(dois):
    E = json.load(open(os.path.join(OUT, 'select_epmc.json')))['recs']
    W = json.load(open(os.path.join(OUT, 'select_crossref.json')))['works']
    res = []
    for doi in dois:
        w = W.get(doi) or {}
        pm = (E.get(doi) or {}).get('pmcid')
        figs = body = None; route = None
        if pm:
            figs, body = epmc_figs(pm)
            route = 'epmc' if figs else None
        if not figs:
            url, _ = landing(doi)
            if url:
                figs, body, _ = html_figs(url, url)
                route = 'html' if figs else None
        if not figs:
            res.append({'doi': doi, 'figures': 0, 'route': None, 'note': 'no figures found'})
            print(f'  {doi}: NO FIGURES'); continue
        r = write_paper(doi, figs, body, route, pm, w.get('title'), w.get('year'))
        res.append(r)
        print(f"  {doi}: {r['figures']} figures via {route} "
              f"({r['figures_dropped']} image downloads failed)")
        time.sleep(0.5)
    p = os.path.join(OUT, 'fetch_log.json')
    old = json.load(open(p))['papers'] if os.path.exists(p) else []
    old = [x for x in old if x['doi'] not in {y['doi'] for y in res}] + res
    json.dump({'papers': old}, open(p, 'w'), indent=1)
    return res


if __name__ == '__main__':
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == 'probe':
        out = probe(args)
        p = os.path.join(OUT, 'fetch_probe.json')
        old = json.load(open(p))['probes'] if os.path.exists(p) else {}
        old.update(out)
        json.dump({'probes': old}, open(p, 'w'), indent=1)
    elif cmd == 'get':
        get(args)
