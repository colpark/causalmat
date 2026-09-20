"""Modality statistics over accepted panels (tiers A and B) of the match run.

Each panel is classified from its own definition span (its caption sentence), falling back to the
figure's caption preamble. Two independent axes:
  technique  — what instrument/measurement produced it (SEM, TEM, XRD, XPS, ...)
  form       — what the panel looks like (micrograph, diffraction pattern, spectrum, curve, map, ...)
A panel can carry several technique cues; the first form cue wins, most specific first.

Usage: python panel_modalities.py --root ~/Documents/causalmat/matmech --out results.json [--workers 18]
"""
import argparse
import json
import re
import sys
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

TECH = {
    "SEM": r"\bSEM\b|scanning electron|FE-?SEM|BSE image|secondary electron",
    "TEM": r"\bTEM\b|HRTEM|HAADF|STEM|transmission electron|bright[- ]field|dark[- ]field|SAED|selected area",
    "AFM/STM": r"\bAFM\b|atomic force|\bSTM\b|scanning tunn|KPFM",
    "optical microscopy": r"optical micrograph|optical microscop|light microscop|confocal|CLSM|fluorescence (?:image|microscop)",
    "XRD": r"\bXRD\b|X-?ray diffraction|diffraction pattern|diffractogram|Rietveld|\bGIXD\b|\bWAXS\b|\bSAXS\b",
    "EBSD": r"\bEBSD\b|inverse pole figure|\bIPF\b|pole figure|misorientation",
    "EDS/EDX": r"\bEDS\b|\bEDX\b|\bEPMA\b|elemental mapping|element(?:al)? map",
    "XPS": r"\bXPS\b|photoelectron|binding energy",
    "Raman": r"\bRaman\b",
    "FTIR": r"\bFTIR\b|FT-?IR|infrared spectr",
    "NMR": r"\bNMR\b",
    "UV-vis/PL": r"UV-?vis|absorption spectr|absorbance spectr|photoluminescen|\bPL\b spectr|emission spectr|fluorescence spectr",
    "XAS": r"\bXANES\b|\bEXAFS\b|\bXAS\b|X-?ray absorption",
    "mass spec/chromatography": r"\bXRF\b|mass spectr|\bGPC\b|\bHPLC\b|chromatograph|\bICP\b",
    "mechanical test": r"stress[- ]strain|tensile|compress(?:ion|ive) (?:test|curve)|hardness|nanoindent|fracture toughness|fatigue|creep",
    "electrochemistry": r"voltammogram|\bCV\b curve|cyclic voltamm|\bEIS\b|Nyquist|impedance|galvanostatic|charge[-–/ ]discharge|polarization curve|Tafel|chronoamper|capacit(?:y|ance) retention|coulombic",
    "thermal analysis": r"\bTGA\b|\bDSC\b|\bDTA\b|thermogravimetric|thermal conductivit|heat flow",
    "magnetic/transport": r"hysteresis loop|\bM-?H\b curve|magnetization|resistivity|Seebeck|Hall (?:effect|measurement)|conductivity vs",
    "simulation/DFT": r"\bDFT\b|first[- ]principles|molecular dynamics|\bMD\b simulation|finite element|\bFEM\b|phase[- ]field|Monte Carlo|calculated (?:band|density of states)|\bDOS\b|band structure",
    "biological assay": r"cell viability|live/dead|immunostain|histolog|H&E|flow cytometr|CFU|antibacterial|in vivo|micro-?CT",
    "particle size/porosity": r"particle size distribution|\bDLS\b|zeta potential|\bBET\b|pore size distribution|isotherm",
}
FORM = [  # most specific first; first match wins
    ("diffraction_pattern", r"\bXRD\b|X-?ray diffraction|diffraction pattern|diffractogram|\bSAED\b|\bWAXS\b|\bSAXS\b"),
    ("orientation_distribution", r"pole figure|inverse pole figure|\bIPF\b map|orientation map|\bEBSD\b"),
    ("spatial_map", r"element(?:al)? map|mapping|\bmap\b|distribution image|line scan"),
    ("spectrum", r"spectr(?:um|a)|\bXPS\b|\bRaman\b|\bFTIR\b|FT-?IR|\bNMR\b|XANES|EXAFS|absorbance|photoluminescen"),
    ("micrograph", r"\bSEM\b|\bTEM\b|HRTEM|HAADF|STEM|micrograph|microscop|\bAFM\b|\bSTM\b|\bBSE\b|bright[- ]field|dark[- ]field|morpholog"),
    ("schematic", r"schematic|illustration|diagram|sketch|mechanism of|process flow|cartoon"),
    ("photograph", r"photograph|digital (?:photo|image)|optical (?:photo|image) of the sample|appearance of"),
    ("simulation_render", r"simulat|\bDFT\b|molecular dynamics|finite element|snapshot|atomistic model|band structure|\bDOS\b"),
    ("table", r"^table|\btable\b"),
    ("xy_curve", r"curve|plot|profile|vs\.?\s|versus|dependence|evolution of|variation of|isotherm|loop|histogram|distribution of"),
]
TECH = {k: re.compile(v, re.I) for k, v in TECH.items()}
FORM = [(k, re.compile(v, re.I)) for k, v in FORM]


def classify(text):
    techs = [k for k, rx in TECH.items() if rx.search(text)]
    form = next((k for k, rx in FORM if rx.search(text)), None)
    return techs, form


def do_folder(folder):
    folder = Path(folder)
    mj = folder / "panels" / "match.json"
    if not mj.exists():
        return None
    try:
        m = json.load(open(mj))
    except Exception:
        return None
    tech_c, form_c, pair_c, n = Counter(), Counter(), Counter(), Counter()
    per_tier_tech = {"A": Counter(), "B": Counter()}
    per_tier_form = {"A": Counter(), "B": Counter()}
    multi = Counter()
    for f in m.get("figures", []):
        if f["tier"] == "C":
            continue
        forms_here = set()
        pre = f.get("caption_preamble") or ""
        for p in f["panels"]:
            own = p.get("definition") or ""
            # the technique is usually named once in the preamble; the panel span names its condition
            text = f"{own} {pre}".strip()
            if len(text) < 3:
                text = " ".join(p.get("use") or [])[:400]
            techs, form = classify(text)
            if not techs and p.get("use"):
                techs, form2 = classify(" ".join(p["use"])[:400])
                form = form or form2
            n[f["tier"]] += 1
            if not techs:
                tech_c["(none detected)"] += 1
                per_tier_tech[f["tier"]]["(none detected)"] += 1
            for t in techs:
                tech_c[t] += 1
                per_tier_tech[f["tier"]][t] += 1
            key = form or "(unclassified)"
            form_c[key] += 1
            per_tier_form[f["tier"]][key] += 1
            forms_here.add(key)
            if techs:
                pair_c[(techs[0], key)] += 1
        if len(forms_here - {"(unclassified)"}) > 1:
            multi[f["tier"]] += 1
    return n, tech_c, form_c, pair_c, per_tier_tech, per_tier_form, multi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=18)
    a = ap.parse_args()
    root = Path(a.root).expanduser()
    folders = sorted(p.parent for p in root.glob("*/*/data.json"))
    N, T, F, P = Counter(), Counter(), Counter(), Counter()
    TT = {"A": Counter(), "B": Counter()}
    FF = {"A": Counter(), "B": Counter()}
    M = Counter()
    with Pool(a.workers) as pool:
        for res in pool.imap_unordered(do_folder, (str(f) for f in folders), chunksize=64):
            if not res:
                continue
            n, t, f, p, tt, ff, m = res
            N += n; T += t; F += f; P += p; M += m
            for k in ("A", "B"):
                TT[k] += tt[k]; FF[k] += ff[k]
    tot = sum(N.values())
    out = {
        "panels_by_tier": dict(N), "panels_total_AB": tot,
        "form_overall": {k: [v, round(v / tot, 4)] for k, v in F.most_common()},
        "form_tier_A": dict(FF["A"].most_common()), "form_tier_B": dict(FF["B"].most_common()),
        "technique_overall": {k: [v, round(v / tot, 4)] for k, v in T.most_common()},
        "technique_tier_A": dict(TT["A"].most_common()), "technique_tier_B": dict(TT["B"].most_common()),
        "top_technique_form_pairs": {f"{a_}|{b}": c for (a_, b), c in P.most_common(25)},
        "figures_mixing_forms": dict(M),
    }
    json.dump(out, open(a.out, "w"), indent=1)
    print(json.dumps({k: out[k] for k in ("panels_by_tier", "panels_total_AB", "form_overall", "figures_mixing_forms")}, indent=1))


if __name__ == "__main__":
    sys.exit(main())
