"""normalize.py: the one text normaliser for v3.

Twice a Unicode/ASCII mismatch silently turned a real match into a null result: MatMech writes
`Al₆Cu₆La`, `α-Al`, `θ′` where our graphs write `Al6Cu6La`, `alpha-Al`, `theta'`. Every v3 matcher
routes through `fold()` so the class of bug is fixed rather than the instance.

  fold(s)      ASCII-folded, whitespace-collapsed, lowercased. For MATCHING ONLY, never for display.
  tokens(s)    distinctive tokens of the folded text, for leak guards.
"""
import re, unicodedata

SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜ', '0123456789+-=()aeoxhklmnpst')
SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ', '0123456789+-=()n')
GREEK = {'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta', 'ε': 'epsilon', 'ζ': 'zeta',
         'η': 'eta', 'θ': 'theta', 'ι': 'iota', 'κ': 'kappa', 'λ': 'lambda', 'μ': 'mu', 'ν': 'nu',
         'ξ': 'xi', 'π': 'pi', 'ρ': 'rho', 'σ': 'sigma', 'τ': 'tau', 'υ': 'upsilon', 'φ': 'phi',
         'χ': 'chi', 'ψ': 'psi', 'ω': 'omega'}
PRIME = {'′': "'", '″': "''", '’': "'", '‘': "'", '´': "'",
         '“': '"', '”': '"'}
DASH = {'‐': '-', '‑': '-', '‒': '-', '–': '-', '—': '-', '−': '-'}


def fold(s):
    """ASCII-folded, collapsed, lowercased. Matching only; never render this to a human or a solver."""
    t = (s or '')
    t = t.translate(SUB).translate(SUP)
    for k, v in {**GREEK, **PRIME, **DASH}.items():
        t = t.replace(k, v); t = t.replace(k.upper(), v)
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = t.replace('×', 'x').replace('·', ' ').replace('…', ' ')
    return re.sub(r'\s+', ' ', t).strip().lower()


WORD = re.compile(r"[a-z][a-z0-9_\-']{3,}|[a-z]{1,2}\d+[a-z0-9]*")


def tokens(*texts):
    """distinctive folded tokens, for leak guards"""
    out = set()
    for t in texts:
        out |= set(WORD.findall(fold(t)))
    return out
