"""shots.py: region screenshots of the v2.10 reports, straight from a headless browser.

  python3 trace_kit_v2p10/shots.py <outdir>

A fragment URL is not enough: the browser lays the page out but never rasterises a section far
below the fold, so `--screenshot` on `page.html#C1_ledger` returns blank paper. This drives the
DevTools protocol instead and asks for a clip around the element's own box, with
captureBeyondViewport, which rasterises it wherever it sits.

There is no websocket library here, so the client below is the minimum that speaks to CDP:
handshake, masked text frames out, unmasked frames in. No model call.
"""
import base64, json, os, re, socket, subprocess, sys, time, urllib.request

CH = os.path.expanduser('~/.cache/ms-playwright/chromium_headless_shell-1243/'
                        'chrome-headless-shell-linux-arm64/chrome-headless-shell')
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REP = os.path.join(ROOT, 'results/v2p10/reports')


class WS:
    def __init__(self, url):
        m = re.match(r'ws://([^:/]+):(\d+)(/.*)', url)
        host, port, path = m.group(1), int(m.group(2)), m.group(3)
        self.s = socket.create_connection((host, port)); self.s.settimeout(60)
        k = base64.b64encode(os.urandom(16)).decode()
        self.s.sendall((f'GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\n'
                        f'Connection: Upgrade\r\nSec-WebSocket-Key: {k}\r\n'
                        f'Sec-WebSocket-Version: 13\r\n\r\n').encode())
        buf = b''
        while b'\r\n\r\n' not in buf: buf += self.s.recv(4096)
        assert b'101' in buf.split(b'\r\n')[0], buf[:120]
        self.buf = buf.split(b'\r\n\r\n', 1)[1]
        self.n = 0

    def _read(self, k):
        while len(self.buf) < k: self.buf += self.s.recv(1 << 20)
        out, self.buf = self.buf[:k], self.buf[k:]
        return out

    def send(self, obj):
        p = json.dumps(obj).encode()
        h = b'\x81'
        n = len(p)
        if n < 126: h += bytes([0x80 | n])
        elif n < 1 << 16: h += bytes([0x80 | 126]) + n.to_bytes(2, 'big')
        else: h += bytes([0x80 | 127]) + n.to_bytes(8, 'big')
        m = os.urandom(4)
        self.s.sendall(h + m + bytes(b ^ m[i % 4] for i, b in enumerate(p)))

    def recv(self):
        b0, b1 = self._read(2)
        n = b1 & 127
        if n == 126: n = int.from_bytes(self._read(2), 'big')
        elif n == 127: n = int.from_bytes(self._read(8), 'big')
        return json.loads(self._read(n).decode())

    def call(self, method, **params):
        self.n += 1
        self.send({'id': self.n, 'method': method, 'params': params})
        while True:
            m = self.recv()
            if m.get('id') == self.n:
                if 'error' in m: raise RuntimeError(f'{method}: {m["error"]}')
                return m.get('result', {})


def shots(outdir, jobs, width=1400, height=1100):
    os.makedirs(outdir, exist_ok=True)
    port = 9412
    p = subprocess.Popen([CH, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                          f'--remote-debugging-port={port}', f'--window-size={width},{height}',
                          'about:blank'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        url = None
        for _ in range(80):
            try:
                j = json.load(urllib.request.urlopen(f'http://127.0.0.1:{port}/json/list'))
                url = next((t['webSocketDebuggerUrl'] for t in j if t.get('type') == 'page'), None)
                if url: break
            except Exception: pass
            time.sleep(0.25)
        if not url: raise RuntimeError('no devtools target')
        ws = WS(url)
        ws.call('Page.enable'); ws.call('Runtime.enable')
        ws.call('Emulation.setDeviceMetricsOverride', width=width, height=height,
                deviceScaleFactor=1, mobile=False)
        done, cur = [], None
        for job in jobs:
            name, page, sel, w = job[:4]
            pre = job[4] if len(job) > 4 else None
            if w != width:
                ws.call('Emulation.setDeviceMetricsOverride', width=w, height=height,
                        deviceScaleFactor=1, mobile=False)
                width = w; cur = None
            if page != cur or pre:
                ws.call('Page.navigate', url=f'file://{os.path.join(REP, page)}')
                for _ in range(200):
                    r = ws.call('Runtime.evaluate',
                                expression='document.readyState+"|"+document.images.length+"|"'
                                           '+[...document.images].filter(i=>i.complete).length',
                                returnByValue=True)['result'].get('value', '')
                    a = r.split('|')
                    if a and a[0] == 'complete' and len(a) == 3 and a[1] == a[2]: break
                    time.sleep(0.15)
                time.sleep(0.6)
                cur = page
            if pre:
                ws.call('Runtime.evaluate', expression=pre, returnByValue=True)
                time.sleep(0.4)
            if sel:
                r = ws.call('Runtime.evaluate', returnByValue=True, expression=f"""
                  (function(){{var e=document.querySelector({json.dumps(sel)});if(!e)return null;
                   var b=e.getBoundingClientRect();
                   return {{x:b.x+scrollX,y:b.y+scrollY,w:b.width,h:b.height}};}})()""")['result']
                v = r.get('value')
                if not v: print(f'  {name}: selector {sel} not found'); continue
                clip = {'x': max(0, v['x'] - 10), 'y': max(0, v['y'] - 10),
                        'width': min(width, v['w'] + 20), 'height': min(2600, v['h'] + 20),
                        'scale': 1}
            else:
                clip = {'x': 0, 'y': 0, 'width': width, 'height': height, 'scale': 1}
            d = ws.call('Page.captureScreenshot', format='png', clip=clip,
                        captureBeyondViewport=True)['data']
            f = os.path.join(outdir, name + '.png')
            open(f, 'wb').write(base64.b64decode(d))
            done.append((name, os.path.getsize(f), round(clip['width']), round(clip['height'])))
            print(f'  {name}: {os.path.getsize(f)//1024} kB  '
                  f'{round(clip["width"])}x{round(clip["height"])}')
        return done
    finally:
        p.terminate()
        try: p.wait(10)
        except Exception: p.kill()


JOBS = [
    # name, page, css selector (None = the viewport at the top), viewport width
    ('deep_header',  'Advanced_Energy_Materials__aenm.202003419.html', None, 1400),
    ('deep_graph',   'Advanced_Energy_Materials__aenm.202003419.html', '#graph', 1400),
    ('deep_index',   'Advanced_Energy_Materials__aenm.202003419.html', 'h2 + .scroll table', 1400),
    ('deep_traj',    'Advanced_Energy_Materials__aenm.202003419.html', '#C1 .traj', 1400),
    ('deep_step1',   'Advanced_Energy_Materials__aenm.202003419.html', '#C1_step1', 1400),
    ('deep_seam',    'Advanced_Energy_Materials__aenm.202003419.html', '#C1_seam3', 1400),
    ('deep_step3',   'Advanced_Energy_Materials__aenm.202003419.html', '#C1_step3', 1400),
    ('deep_gen',     'Advanced_Energy_Materials__aenm.202003419.html', '#C1_gen', 1400),
    ('deep_narrow',  'Advanced_Energy_Materials__aenm.202003419.html', None, 390),
    ('d2_header',    'Journal_of_Magnesium_and_Alloys__j.jma.2020.09.027.html', None, 1400),
    ('d2_graph',     'Journal_of_Magnesium_and_Alloys__j.jma.2020.09.027.html', '#graph', 1400),
    ('d2_traj',      'Journal_of_Magnesium_and_Alloys__j.jma.2020.09.027.html', '#C67 .traj', 1400),
    ('d2_step1',     'Journal_of_Magnesium_and_Alloys__j.jma.2020.09.027.html', '#C67_step1', 1400),
    ('d2_seam',      'Journal_of_Magnesium_and_Alloys__j.jma.2020.09.027.html', '#C67_seam2', 1400),
    ('d2_gen',       'Journal_of_Magnesium_and_Alloys__j.jma.2020.09.027.html', '#C67_gen', 1400),
    ('d2_narrow',    'Journal_of_Magnesium_and_Alloys__j.jma.2020.09.027.html', '#C67_step1', 390),
]

if __name__ == '__main__':
    shots(sys.argv[1] if len(sys.argv) > 1 else '/tmp/v2p10shots', JOBS)
