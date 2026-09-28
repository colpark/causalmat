"""step1.py: what each arm actually received, read out of the stored prompt files.

  python3 trace_kit_v2p11/step1.py

No model call. The question this answers is narrow and load-bearing: when arm B and arm C were
handed "the earlier result", were the qualifications recorded on that result handed over with
it, or only the bare proposition? If only the proposition, then arm B was asked to build on a
claim stripped of its own caveats, and every score downstream of that is measuring the wrong
thing.

The generator's source is not the evidence -- it has been edited since those runs. The prompt
files that were actually sent are, so this reads them.

Every verdict is model against model.
"""
import glob, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
OUT = R('results/v2p11/nanolett.6b04294')
DIRS = ['results/v2p9/arms', 'results/v2p9/arms_nl', 'results/v2p10/arms_d4',
        'results/v2p10/arms_d5']

LIMHDR = 'The qualifications recorded on that earlier result:'
NOLIM = 'No qualifications were recorded on that earlier result.'


def recs():
    D = {}
    for f in ('results/v2p9/pairs.json', 'results/v2p9/nextlink.json',
              'results/v2p10/deeper_d4.json', 'results/v2p10/deeper_d5.json'):
        for x in json.load(open(R(f)))['pairs_out']: D[x['item']] = x
    return D


def find(item, arm):
    """the prompt actually sent for this item and arm, first sample"""
    for d in DIRS:
        p = R(d, f'{item}_{arm}1.txt')
        if os.path.exists(p): return p
    return None


def main():
    sc = json.load(open(os.path.join(OUT, 'scope.json')))
    D = recs()
    rows, missing = [], []
    for it in sc['links']:
        x = D[it]
        r = {'link': it, 'n_input_limits': len(x.get('input_limits') or [])}
        for arm in ('A', 'B', 'C', 'N'):
            f = find(it, arm)
            if not f:
                missing.append(f'{it}_{arm}'); r[arm] = None; continue
            t = open(f).read()
            got = {
                'file': os.path.relpath(f, ROOT),
                'bytes': len(t),
                'observation_text': x['new_observation']['text'][:60] in t,
                'earlier_result': bool(x.get('input_result')) and x['input_result'][:60] in t,
                'limits_header': LIMHDR in t,
                'limits_absent_note': NOLIM in t,
                # every limit, not just the header: a truncated list is the same failure
                'limits_present': sum(1 for L in (x.get('input_limits') or [])
                                      if L[:70] in t),
                'crop_paths': len(re.findall(r'^\s{2}\S+\s+/\S+\.(?:jpg|png)$', t, re.M)),
                'captions': 'Panel captions as printed:' in t,
                'whole_figures': len(re.findall(r'figures?/\S+\.(?:jpg|png)', t)),
            }
            r[arm] = got
        rows.append(r)

    # the finding, stated as a single boolean over every link
    need = [(r['link'], a) for r in rows for a in ('B', 'C')
            if r[r'%s' % a] and r['n_input_limits']
            and r[a]['limits_present'] < r['n_input_limits']]
    fin = {
        'links': len(rows),
        'links_with_recorded_limits': sum(1 for r in rows if r['n_input_limits']),
        'arm_B_carried_all_limits': all(
            r['B'] and (r['B']['limits_present'] == r['n_input_limits']) for r in rows),
        'arm_C_carried_all_limits': all(
            r['C'] and (r['C']['limits_present'] == r['n_input_limits']) for r in rows),
        'incomplete': need,
        'missing_prompt_files': missing,
        'verdict': None,
    }
    fin['verdict'] = ('limits were in the handoff to both arm B and arm C; no rerun needed'
                      if fin['arm_B_carried_all_limits'] and fin['arm_C_carried_all_limits']
                      else 'limits were NOT fully in the handoff; arms B and C must be rerun')
    json.dump({'note': 'v2.11 Step 1: what each arm received, read from the sent prompts.',
               'finding': fin, 'per_link': rows},
              open(os.path.join(OUT, 'step1.json'), 'w'), indent=1)
    print(json.dumps(fin, indent=1))
    print()
    for r in rows:
        b, c, a = r['B'], r['C'], r['A']
        print(f"{r['link'][:58]:58s} limits {r['n_input_limits']:2d} | "
              f"B {b['limits_present'] if b else '-'}/{r['n_input_limits']} "
              f"crops {b['crop_paths'] if b else '-'} caps {int(b['captions']) if b else '-'} | "
              f"C {c['limits_present'] if c else '-'}/{r['n_input_limits']} "
              f"crops {c['crop_paths'] if c else '-'} | "
              f"A crops {a['crop_paths'] if a else '-'} earlier {int(a['earlier_result']) if a else '-'}")


if __name__ == '__main__':
    main()
