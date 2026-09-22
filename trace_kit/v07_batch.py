"""v07_batch.py: one relay per stage across several papers.

  v07_batch.py merge <name> <stage> <P>...    concatenates results/v07/papers/<P>/jobs_<stage>.json -> .v07work/batch_<name>.json
  v07_batch.py harvest <name> <relay_id>      relay.py harvest on the merged file, then each paper gets its own
                                              jobs_<stage>.json.harvest.json (its jobs only) and the relay in its dispatch log
The relay is shared by the papers in the batch; each paper's log records it with the share 1/len(papers).
"""
import json, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
W = os.path.join(ROOT, '.v07work')
def D(P): return os.path.join(ROOT, 'results', 'v07', 'papers', P)

def merge(name, stage, papers):
    jobs, meta = [], {'stage': stage, 'papers': papers}
    for P in papers:
        for st in stage.split(','):   # several stages can share one relay
            f = os.path.join(D(P), f'jobs_{st}.json')
            if os.path.exists(f): jobs += json.load(open(f))
    json.dump(jobs, open(os.path.join(W, f'batch_{name}.json'), 'w'), indent=1)
    json.dump(meta, open(os.path.join(W, f'batch_{name}.meta.json'), 'w'), indent=1)
    print(f'batch_{name}: {len(jobs)} jobs from {len(papers)} papers')

def harvest(name, relay_id):
    f = os.path.join(W, f'batch_{name}.json'); meta = json.load(open(os.path.join(W, f'batch_{name}.meta.json')))
    r = subprocess.run([sys.executable, os.path.join(HERE, 'relay.py'), 'harvest', f, relay_id], cwd=ROOT)
    H = json.load(open(f + '.harvest.json')); jobs = json.load(open(f)); byid = {j['id']: j for j in jobs}
    for P in meta['papers']:
        for st in meta['stage'].split(','):
            mine = [h for h in H['jobs'] if byid[h['id']]['out'].startswith(D(P) + os.sep)
                    and (len(meta['stage'].split(',')) == 1 or byid[h['id']]['id'].endswith('/' + st) or (st == 'gate' and byid[h['id']]['id'].rsplit('/', 1)[1] in ('fullarm', 'floor')) or (st == 'grade' and '/grader.' in byid[h['id']]['id']))]
            hp = os.path.join(D(P), f"jobs_{st}.json.harvest.json")
            if mine and os.path.exists(hp):   # a paper split across relays keeps every relay's jobs
                old = json.load(open(hp)); ids = {x['id'] for x in mine}
                mine = [x for x in old.get('jobs', []) if x['id'] not in ids] + mine
                relay_id_s = ','.join(dict.fromkeys(str(old.get('relay', '')).split(',') + [relay_id]))
            else: relay_id_s = relay_id
            if mine: json.dump({'relay': relay_id_s, 'batch': name, 'jobs': mine}, open(hp, 'w'), indent=1)
        lp = os.path.join(D(P), 'dispatch_log.json'); L = json.load(open(lp)) if os.path.exists(lp) else []
        if not any(x['agent_id'] == relay_id for x in L):
            L.append({'kind': 'relay', 'agent_id': relay_id, 'share': round(1 / len(meta['papers']), 3), 't': time.time()})
            json.dump(L, open(lp, 'w'), indent=1)
    sys.exit(r.returncode)

if __name__ == '__main__':
    a = sys.argv
    if a[1] == 'merge': merge(a[2], a[3], a[4:])
    else: harvest(a[2], a[3])
