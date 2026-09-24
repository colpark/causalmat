"""cost.py: record what each v2.6 stage actually cost, so the 99-paper estimate has a basis.

  python3 -m trace_kit_v2p6.cost start <stage>
  python3 -m trace_kit_v2p6.cost stop  <stage> <n_calls> [<n_relays>]

Wall time is measured on this session's clock from the moment the relays are dispatched to the
moment the last one is harvested, so it includes relay overhead and the concurrency cap. It is
wall time for THIS cap (20 agents), not a per-call cost.

Every verdict is model against model.
"""
import json, os, sys, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
F = os.path.join(ROOT, 'results/v2p6/cost.json')


def load():
    return json.load(open(F)) if os.path.exists(F) else {}


def save(d):
    os.makedirs(os.path.dirname(F), exist_ok=True)
    json.dump(d, open(F, 'w'), indent=1)


def main():
    d, cmd, stage = load(), sys.argv[1], sys.argv[2]
    r = d.setdefault(stage, {})
    if cmd == 'start':
        r['start'] = time.time()
    else:
        r['stop'] = time.time()
        r['calls'] = int(sys.argv[3])
        if len(sys.argv) > 4: r['relays'] = int(sys.argv[4])
        r['wall_s'] = round(r['stop'] - r['start'], 1)
        r['wall_min'] = round(r['wall_s'] / 60, 1)
        r['s_per_call'] = round(r['wall_s'] / r['calls'], 2) if r['calls'] else None
    save(d)
    print(stage, json.dumps(r))


if __name__ == '__main__': main()
