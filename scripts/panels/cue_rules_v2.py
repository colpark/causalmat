"""Cue patterns v2: the tightenings docs/CUE_PRECISION.md specifies, applied to stored OCR tokens.

No OCR re-run is needed. ocr.json holds every token with its box and score, so a pattern change is
re-derived offline from those tokens. `assign(tokens)` returns the v2 cue list for one crop.

Thermal-transport decision (the open question in CUE_PRECISION.md): a conductivity-versus-temperature
panel is a TRANSPORT measurement, not a calorimetry trace. `thermal` stays TGA/DSC/heat-flow only, and
transport panels get their own `thermal transport` cue rather than being folded into `thermal` or left
in `none`. That keeps `thermal` at 1.000 and stops the miss being invisible.
"""
import re

NUM_UNIT = re.compile(r"(\d+(?:\.\d+)?)\s*(nm|µm|μm|um|mm|Å)\b", re.I)
ELEMENTS = r"(?:H|He|Li|Be|B|C|N|O|F|Ne|Na|Mg|Al|Si|P|S|Cl|Ar|K|Ca|Sc|Ti|V|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Zr|Nb|Mo|Ru|Rh|Pd|Ag|Cd|In|Sn|Sb|Te|I|Ba|La|Ce|Pr|Nd|Sm|Eu|Gd|Tb|Dy|Er|Yb|Hf|Ta|W|Re|Os|Ir|Pt|Au|Hg|Pb|Bi)"


def _joined(tokens):
    return " ".join(t["text"] for t in tokens)


def _num_before(text, rx, lo=None, hi=None):
    """True when a number adjacent to a matching unit falls in [lo, hi]."""
    for m in re.finditer(rx, text, re.I):
        seg = text[max(0, m.start() - 12):m.end() + 12]
        for n in re.finditer(r"[-+]?\d+(?:\.\d+)?", seg):
            v = float(n.group())
            if (lo is None or v >= lo) and (hi is None or v <= hi):
                return True
    return False


def assign(tokens):
    """v2 cue classes for one crop, from its stored OCR tokens."""
    txt = _joined(tokens)
    cues = []

    def add(c):
        if c not in cues:
            cues.append(c)

    # 1. XAS: a real absorption edge sits above ~100 eV, or the words say so outright.
    #    The old pattern matched 1.5-3.5 eV photoluminescence panels through "photon energy (eV)".
    if re.search(r"XANES|EXAFS|K-?edge|L-?edge", txt, re.I):
        add("XAS")
    elif re.search(r"photon\s*energy|absorption", txt, re.I) and _num_before(txt, r"\beV\b", lo=100):
        add("XAS")
    elif _num_before(txt, r"\bkeV\b", lo=3) and re.search(r"XANES|EXAFS|edge|absorption", txt, re.I):
        add("XAS")

    # 2. EDS line scan: distance alone is not a line scan; a composition axis must be present too.
    if re.search(r"distance|position|\bµm\b|\bum\b", txt, re.I) and \
       re.search(rf"\bat\.?\s*%|\bwt\.?\s*%|counts|{ELEMENTS}\s*[KL]\b", txt):
        add("EDS line scan")

    # 3. FTIR: a wavenumber axis is shared with Raman, so require a transmittance/absorbance y-axis.
    if re.search(r"wavenumber", txt, re.I) and re.search(r"transmittance|absorbance|\bT\s*%|reflectance", txt, re.I):
        add("FTIR")
    # Raman keeps its own explicit axis name
    if re.search(r"raman\s*shift", txt, re.I):
        add("Raman")

    # 4. XRD: require 2-theta adjacency, not a bare "20" tick beside "(deg)".
    if re.search(r"2\s*θ|2\s*theta|2-?theta", txt, re.I) or \
       re.search(r"2\s*0\s*\(?\s*(?:°|deg)", txt, re.I) and re.search(r"intensity|counts|a\.?\s*u", txt, re.I):
        add("XRD")

    # 5. XPS: binding energy in eV; an axis running into keV is an EDX spectrum.
    if re.search(r"binding\s*energy", txt, re.I) and not _num_before(txt, r"\bkeV\b", lo=1):
        add("XPS")

    # 6. EDS: a keV energy axis, but not a hard X-ray absorption edge.
    if re.search(r"energy\s*\(?\s*keV", txt, re.I) and not re.search(r"XANES|EXAFS|K-?edge|L-?edge", txt, re.I):
        add("EDS")

    # 7. mechanical: strain alone fires on piezoresistive curves and strain colourbars.
    if re.search(r"stress\s*\(?\s*(?:MPa|GPa|N)", txt, re.I) or \
       (re.search(r"strain", txt, re.I) and re.search(r"\bload\b|\bforce\b|\bstress\b", txt, re.I)):
        add("mechanical")

    # unchanged classes, all at or above 0.90 in the eye check
    if re.search(r"heat\s*flow|\bTGA\b|\bDSC\b|weight\s*(?:loss|\(%)", txt, re.I):
        add("thermal")
    if re.search(r"thermal\s*conductivit|\bκ\b|\bkappa\b.*temperature", txt, re.I):
        add("thermal transport")          # its own class, see the module docstring
    if re.search(r"vs\.?\s*RHE|potential\s*\(V|mA\s*cm|mAh|voltage\s*\(V|capacity", txt, re.I):
        add("electrochemistry")
    if re.search(r"wavelength\s*\(?\s*nm", txt, re.I):
        add("optical spectroscopy")
    sem_banner = re.search(r"\bkV\b|\bWD\b|SE2|InLens|\bBSE\b|\bSEI\b|mag\b", txt, re.I)

    # 8. micrograph: the scale-bar token must not be an axis tick or a data label.
    scale = None
    for t in tokens:
        m = NUM_UNIT.search(t["text"])
        if not m:
            continue
        near_axis = any(
            o is not t and re.fullmatch(r"[-+]?\d+(?:\.\d+)?", o["text"].strip()) and
            abs((o["box"][1] + o["box"][3]) / 2 - (t["box"][1] + t["box"][3]) / 2) < 12
            for o in tokens)
        if not near_axis:
            scale = m.group(0)
            break
    if sem_banner and scale:
        add("SEM")
    elif scale and not cues:
        add("micrograph")
    return cues, scale
