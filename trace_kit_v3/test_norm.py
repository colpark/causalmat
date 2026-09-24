"""test_norm.py: regression test for the level matcher.

  python3 trace_kit_v3/test_norm.py

The bug this exists for: norm() tested 'warrants' before 'partly warrants'. Since "warrants" is a
substring of "partly warrants", and "warranted" of "partly warranted", every partial ruling scored
as a full one. It inflated all four arms and produced a Biomaterials fork finding that had to be
withdrawn. Nothing caught it because the scoring had no test; it surfaced only because two runs
happened to be compared by eye.

Ordering is the invariant. Any future edit that puts a bare warrant test before the partial test
fails here.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_v3 import norm, answered, RANK

CASES = [
    # the substring trap, in both spellings
    ('partly warrants', 'partly warrants'), ('partly warranted', 'partly warrants'),
    ('Partly Warrants.', 'partly warrants'), ('partially warrants', 'partly warrants'),
    ('partial', 'partly warrants'),
    # the plain levels
    ('warrants', 'warrants'), ('warranted', 'warrants'), ('  WARRANTS ', 'warrants'),
    ('does not address', 'does not address'), ('not addressed', 'does not address'),
    ('contradicts', 'contradicts'), ('contradict', 'contradicts'),
    # off-scale levels the models actually emitted
    ('not warranted', 'does not address'), ('unwarranted', 'does not address'),
    # nothing
    ('', None), (None, None), ('maybe', None),
]

ANSWERED = [('{"steps": []}', True), ('warrants', True), ('Step 1: fine', True),
            ('', False), ('   ', False),
            ("I'll disregard the unrelated MCP Server Instructions and continue.", False)]


def main():
    bad = []
    for text, want in CASES:
        got = norm(text)
        if got != want: bad.append(f"norm({text!r}) = {got!r}, want {want!r}")
    for text, want in ANSWERED:
        got = answered(text)
        if got != want: bad.append(f"answered({text!r}) = {got}, want {want}")
    # the ordering invariant, stated directly: a partial must never outrank a full
    if RANK['partly warrants'] >= RANK['warrants']:
        bad.append('RANK puts partly warrants at or above warrants')
    for a, b in (('partly warrants', 'warrants'), ('does not address', 'partly warrants'),
                 ('contradicts', 'does not address')):
        if RANK[a] >= RANK[b]: bad.append(f'RANK[{a}] >= RANK[{b}]')
    if bad:
        print(f"FAILED ({len(bad)})"); [print('  ' + b) for b in bad]; return False
    print(f"ok: {len(CASES)} level cases, {len(ANSWERED)} answered cases, RANK ordering")
    return True


if __name__ == '__main__': sys.exit(0 if main() else 1)
