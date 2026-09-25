"""partB.py: v2.8 Part B -- three arms, six samples each.

  python3 -m trace_kit_v2p8.partB build

  arm A  the new measurement alone, with its panels
  arm B  the new measurement plus the earlier result, as v2.7 ran it
  arm C  the earlier result alone, no measurement and no panels

Arm C is the one v2.7 never had, and it is why this pilot can say something v2.7 could not.
v2.7 compared B against A and called the difference necessity. But a difference there only shows
the earlier result added something; it cannot show the measurement was needed at all. If arm C
reaches the key on its own, the item is not composing, it is restating step 1. Necessity needs
B to beat BOTH.

Six samples per arm rather than three, because Part A of v2.7 measured how far a single sample
wanders and three was not enough to see past it.

Every verdict is model against model.
"""
import json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
ARMS = R('results/v2p8/arms')
SAMPLES = 6

TAIL = ("Answer in prose, at most 250 words. Say what conclusion this justifies and say plainly "
        "what it leaves uncertain. Claim nothing the evidence does not carry.")

ARM_A = """{q}

What the measurement says:

  {obs}

Figure panels. Open every one of these with the Read tool before you answer:
{pans}
{caps}
{tail}"""

ARM_B = """{q}

What the measurement says:

  {obs}

Figure panels. Open every one of these with the Read tool before you answer:
{pans}
{caps}
An earlier step in this work already established the following, and you may treat it as settled:

{inp}
{lims}

{tail}"""

ARM_C = """{q}

You have no new measurement and no figures for this step. What you have is a result an earlier step already established, which you may treat as settled:

{inp}
{lims}

{tail}"""


def items():
    S = json.load(open(R('results/v2p8/selected.json')))['items']
    DI = {x['item']: x for x in json.load(open(R('results/v2p7/derived_input.json')))['items_out']}
    return [(s, DI[s['item']]) for s in S]


def build(only=None):
    os.makedirs(ARMS, exist_ok=True)
    jobs, skipped = [], []
    for s, x in items():
        if only is not None and x['item'] not in only:
            skipped.append(x['item']); continue
        pans = '\n'.join(f"  {p['suffix']}   {os.path.realpath(p['crop'])}"
                         for p in x['panels'] if p.get('crop'))
        caps = ('\nPanel captions as printed:\n'
                + '\n'.join(f"  {p['suffix']}: {p['caption_span'].strip()}"
                            for p in x['panels'] if p.get('caption_span')) + '\n') \
            if any(p.get('caption_span') for p in x['panels']) else '\n'
        lims = ('\nThe qualifications recorded on that earlier result:\n'
                + '\n'.join('  - ' + t for t in x['input_limits'])) if x['input_limits'] \
            else '\nNo qualifications were recorded on that earlier result.'
        q = x['question']
        bodies = {
            'A': ARM_A.format(q=q, obs=x['new_observation']['text'], pans=pans, caps=caps,
                              tail=TAIL),
            'B': ARM_B.format(q=q, obs=x['new_observation']['text'], pans=pans, caps=caps,
                              inp=x['input_result'], lims=lims, tail=TAIL),
            'C': ARM_C.format(q=q, inp=x['input_result'], lims=lims, tail=TAIL),
        }
        for arm, body in bodies.items():
            f = os.path.join(ARMS, f"{x['item']}_{arm}.txt")
            open(f, 'w').write(body)
            # arm C has no images, so it does not need the image-reading agent
            ag = 'net-floor' if arm == 'C' else 'net-fullarm'
            for k in range(1, SAMPLES + 1):
                jobs.append({'id': f"{x['item']}_{arm}{k}", 'agent': ag, 'prompt': f,
                             'out': os.path.join(ARMS, f"{x['item']}_{arm}{k}.out.txt")})
    json.dump(jobs, open(R('results/v2p8/arm_jobs.json'), 'w'), indent=1)
    n = len({j['prompt'] for j in jobs})
    print(f'{len(jobs)} answers from {n} prompts '
          f'({n // 3} items x 3 arms x {SAMPLES} samples)'
          + (f', {len(skipped)} items skipped' if skipped else ''))
    return jobs


if __name__ == '__main__':
    build()
