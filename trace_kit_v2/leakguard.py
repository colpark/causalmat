"""leakguard.py: keep the answer off the question sheet.

Two rules from the plan:
  section 1  "nothing from after the answer may appear on the sheet"
  section 4  oracle returns carry "measurements from observation nodes, never interpretations"

caption_for()  trims a panel's caption span to what does not give the step away, falling back to the
               figure preamble and then to nothing.
measurement()  cuts an observation label at the first interpretive hinge, so the oracle hands over the
               number and not the reading of it.
"""
import re

HINGE = re.compile(r'\s*[,;]?\s*\b(assigned to|attributed to|attributable to|indicating|indicative of|'
                   r'suggesting|suggestive of|consistent with|implying|which (?:indicates|shows|means|confirms)|'
                   r'identified as|corresponding to|due to|showing that|confirming)\b.*$', re.I)
WORD = re.compile(r"[A-Za-z][A-Za-z0-9_\-]{4,}|[A-Z][a-z]?\d+[A-Za-z0-9]*")


def terms(*texts):
    """distinctive tokens: words of 5+ characters and formula-like tokens (Al6Cu6La, NaZn13)"""
    out = set()
    for t in texts:
        for m in WORD.findall(t or ''):
            out.add(m.lower())
    return out


def measurement(label):
    """the measured part of an observation label, with the interpretation cut off"""
    s = (label or '').strip()
    cut = HINGE.sub('', s).strip().rstrip(',;')
    return cut if len(cut) >= 20 else s


def caption_for(span, preamble, forbidden):
    """a caption to print under a panel, or None. Drops any clause that shares a distinctive term
    with the claim or with the step's own answer."""
    def clean(t):
        if not t: return None
        parts = re.split(r'(?<=[.;])\s+|\s*\((?=arrow|inset)', t)
        keep = [p for p in parts if p.strip() and not (terms(p) & forbidden)]
        out = ' '.join(keep).strip().rstrip(' ,;(')
        return out if len(out) >= 12 else None
    return clean(span) or clean(preamble)


def check(sheet_text, forbidden):
    """tokens that leaked onto a rendered sheet; empty means clean"""
    return sorted(terms(sheet_text) & forbidden)
