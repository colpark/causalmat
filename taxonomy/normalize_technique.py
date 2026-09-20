"""Normalize attrs.technique to FAMILY:mode across the v05 graphs.

The subject is stripped: "SEM of worn surfaces" and "SEM after immersion" are both SEM; the subject
stays in the node label. A string naming two techniques maps to a list and is flagged. Nothing is
guessed: a string no rule matches becomes OTHER and is reported in technique_unmapped.json.

Usage: python taxonomy/normalize_technique.py --dir taxonomy/graphs_v05/first100 [--write]
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

FAMILIES = ["SEM", "TEM", "XRD", "XAS", "EBSD", "EDS", "XPS", "RAMAN", "IR", "UVVIS", "PL", "NMR", "AFM",
            "OPTICAL", "CT", "APT", "ECHEM", "MECH", "THERMAL", "TRANSPORT", "ATOM", "PROCESS", "DERIVED",
            "ASSAY", "PHYS", "OTHER"]
# modes are a fixed list per family; anything else in that family is the bare family name
MODES = {
    "SEM": ["BSE", "SE", "FEG", "crosssection", "imageanalysis"],
    "TEM": ["HRTEM", "SAED", "STEM", "HAADF", "brightfield", "EBSDtransmission"],
    "XRD": ["synchrotron", "insitu", "poleFigure", "CXD", "powder", "SAXS"],
    "XAS": ["EXAFS", "XANES", "operando"],
    "EBSD": ["IPF", "phasemap", "step"],
    "EDS": ["mapping", "linescan", "spectrum", "AES"],
    "XPS": ["depth", "region"],
    "RAMAN": [], "IR": ["DRIFTS"], "UVVIS": ["Tauc", "IPCE", "transmittance"], "PL": ["timeresolved"],
    "NMR": [], "AFM": ["phase", "height"], "OPTICAL": ["profilometry", "photograph", "fluorescence"],
    "CT": [], "APT": ["proximity"],
    "ECHEM": ["galvanostatic", "CV", "EIS", "LSV", "Tafel", "RDE", "chronoamperometry", "potentiodynamic"],
    "MECH": ["tensile", "hardness", "nanoindentation", "DMA", "wear", "scratch"],
    "THERMAL": ["TGA", "DSC", "laserflash", "transient", "IRcamera"],
    "TRANSPORT": ["Hall", "fourprobe", "Seebeck", "VNA", "dielectric"],
    "ATOM": ["DFT", "MD", "CALPHAD", "FEM"],
    "PROCESS": [], "DERIVED": [], "ASSAY": ["stain", "survival", "tumour", "catalysis"],
    # physical-property measurement: density, porosity, surface area, particle size
    "PHYS": ["density", "porosity", "surfacearea", "particlesize"], "OTHER": [],
}

# (regex, family, mode) — first match wins inside a family pass; order matters within each block
RULES = [
    # imaging
    (r"\bSEM[- ]?BSE\b|\bSEM BSE\b|\bBSE\b", "SEM", "BSE"),
    (r"\bSEM[- ]?SE\b|\bSE2\b|secondary electron", "SEM", "SE"),
    (r"image analysis of SEM", "SEM", "imageanalysis"),
    (r"\bFE-?SEM\b|\bFESEM\b", "SEM", "FEG"),
    (r"SEM cross-?section", "SEM", "crosssection"),
    (r"\bSEM\b", "SEM", None),
    (r"aberration-corrected HAADF|AC HAADF|HAADF", "TEM", "HAADF"),
    (r"\bHRTEM\b|high-?resolution TEM", "TEM", "HRTEM"),
    (r"\bSAED\b|selected area diffraction", "TEM", "SAED"),
    (r"transmission EBSD", "TEM", "EBSDtransmission"),
    (r"\bSTEM\b", "TEM", "STEM"),
    (r"TEM bright field|bright[- ]field TEM", "TEM", "brightfield"),
    (r"\bTEM\b", "TEM", None),
    # diffraction
    (r"\bCXD\b|coherent (?:x-?ray )?diffraction|phase retrieval of the 3-?D", "XRD", "CXD"),
    (r"synchrotron|HEXRD|\bSXRD\b", "XRD", "synchrotron"),
    (r"pole figure", "XRD", "poleFigure"),
    (r"\bSAXS\b", "XRD", "SAXS"),
    (r"powder XRD", "XRD", "powder"),
    (r"in[- ]?operando XRD|ex situ XRD|in[- ]?situ XRD", "XRD", "insitu"),
    (r"\bXRD\b|x-?ray diffraction|Rietveld", "XRD", None),
    # spectroscopy
    (r"\bEXAFS\b", "XAS", "EXAFS"),
    (r"\bXANES\b", "XAS", "XANES"),
    (r"\bXAS\b|x-?ray absorption", "XAS", None),
    (r"\bAES\b depth|Auger", "EDS", "AES"),
    (r"\bEDS\b mapping|\bEDX\b mapping|element(?:al)? map", "EDS", "mapping"),
    (r"line profile|line scan|linescan", "EDS", "linescan"),
    (r"\bEDS\b|\bEDX\b|\bEPMA\b", "EDS", "spectrum"),
    (r"\bXPS\b.*(?:4f|1s|2p|deconvolution)", "XPS", "region"),
    (r"\bXPS\b|photoelectron", "XPS", None),
    (r"\bRaman\b", "RAMAN", None),
    (r"\bDRIFTS\b", "IR", "DRIFTS"),
    (r"\bFTIR\b|FT-?IR|infrared spectro", "IR", None),
    (r"Tauc", "UVVIS", "Tauc"),
    (r"\bIPCE\b", "UVVIS", "IPCE"),
    (r"transmittance", "UVVIS", "transmittance"),
    (r"UV-?vis", "UVVIS", None),
    (r"time-?resolved photoluminescence", "PL", "timeresolved"),
    (r"photoluminescen|\bPL\b", "PL", None),
    (r"\bNMR\b", "NMR", None),
    # scanned probe, optical, tomography
    (r"AFM (?:height and )?phase", "AFM", "phase"),
    (r"AFM height", "AFM", "height"),
    (r"\bAFM\b|atomic force|\bSTM\b|scanning tunn", "AFM", None),
    (r"profilometry", "OPTICAL", "profilometry"),
    (r"photograph|photography", "OPTICAL", "photograph"),
    (r"fluorescence (?:staining|imaging)|AO/EB", "OPTICAL", "fluorescence"),
    (r"optical microscopy|light microscop|quantitative microscopy", "OPTICAL", None),
    (r"micro-?CT|\bCT\b|photoacoustic imaging", "CT", None),
    (r"proximity histogram", "APT", "proximity"),
    (r"atom probe", "APT", None),
    # orientation
    (r"\bIPF\b|inverse pole figure", "EBSD", "IPF"),
    (r"EBSD phase mapping", "EBSD", "phasemap"),
    (r"EBSD,? ?[<\d]", "EBSD", "step"),
    (r"\bEBSD\b|misorientation", "EBSD", None),
    # electrochemistry
    (r"galvanostatic|rate test|cycling test|charge[-–/ ]discharge", "ECHEM", "galvanostatic"),
    (r"cyclic voltamm|\bCV\b", "ECHEM", "CV"),
    (r"\bEIS\b|impedance|Nyquist", "ECHEM", "EIS"),
    (r"\bLSV\b|linear sweep", "ECHEM", "LSV"),
    (r"Tafel", "ECHEM", "Tafel"),
    (r"\bRDE\b|Koutecky|rotating disk", "ECHEM", "RDE"),
    (r"chronoamper", "ECHEM", "chronoamperometry"),
    (r"potentiodynamic|polarisation in SBF|polarization curve", "ECHEM", "potentiodynamic"),
    (r"turnover number|photocatalytic CO2|J-V under|ICP-OES of the electrolyte", "ECHEM", None),
    # mechanical
    (r"tensile|uniaxial tension", "MECH", "tensile"),
    (r"hardness|Vickers", "MECH", "hardness"),
    (r"nanoindent", "MECH", "nanoindentation"),
    (r"\bDMA\b", "MECH", "DMA"),
    (r"wear|pin-on-disc|height loss", "MECH", "wear"),
    (r"scratch", "MECH", "scratch"),
    (r"biaxial-modulus", "MECH", None),
    # thermal, transport
    (r"\bTGA\b|thermogravimetric", "THERMAL", "TGA"),
    (r"\bDSC\b|\bDTA\b", "THERMAL", "DSC"),
    (r"laser-?flash", "THERMAL", "laserflash"),
    (r"heating-?cooling transient|thermocouple", "THERMAL", "transient"),
    (r"IR thermal camera", "THERMAL", "IRcamera"),
    (r"Hall effect", "TRANSPORT", "Hall"),
    (r"four-?probe", "TRANSPORT", "fourprobe"),
    (r"Seebeck|Pisarenko", "TRANSPORT", "Seebeck"),
    (r"\bVNA\b", "TRANSPORT", "VNA"),
    (r"permittivity|permeability|dielectric", "TRANSPORT", "dielectric"),
    # computation
    (r"\bDFT\b|first[- ]principles|effective band structure", "ATOM", "DFT"),
    (r"molecular dynamics|\bMD\b", "ATOM", "MD"),
    (r"CALPHAD", "ATOM", "CALPHAD"),
    (r"finite element|\bFEM\b|thermo-elastic calculation|shape-only simulation", "ATOM", "FEM"),
    # assays
    (r"stain|vital ratio", "ASSAY", "stain"),
    (r"Kaplan-Meier|survival", "ASSAY", "survival"),
    (r"tumour|tumor", "ASSAY", "tumour"),
    (r"cell viability|CFU|antibacterial|immersion medium|mass loss during immersion|\bpH\b", "ASSAY", None),
    # processing filed as a technique
    (r"ball milling|hydrothermal|solvothermal|calcination|solid-state reaction|hot pressing|stir casting|"
     r"induction melting|VAR ?/ ?VIM|casting|\bSLM\b|\bECAP\b|\bFSP\b|\bPVD\b|spin coating|freeze[- ]drying|"
     r"freeze-thaw|sonication|polymerisation|meniscus-guided|direct writing|electropulsing|vapour reduction|"
     r"cutting and polishing|mixing \+|ligand substitution|coating tests", "PROCESS", None),
    # physical-property measurement, distinct from a quantity computed from other data
    (r"Archimedes|apparent density|bulk density|relative density", "PHYS", "density"),
    (r"porosity|pore size distribution|NLDFT", "PHYS", "porosity"),
    (r"N2 physisorption|\bBET\b|isotherm", "PHYS", "surfacearea"),
    (r"particle size distribution|\bDLS\b|zeta potential", "PHYS", "particlesize"),
    # quantities computed from other measurements
    (r"Scherrer|power factor|engineering ZT|ZT from|Wiedemann-Franz|derived from|computed from|"
     r"isosteric heat|transmission-line calculation|literature comparison|sessile drop", "DERIVED", None),
]
RULES = [(re.compile(p, re.I), f, m) for p, f, m in RULES]
MULTI = re.compile(r"\band\b|-EDS\b|\bwith\b|\bvs\b|\+", re.I)


# a computed quantity is DERIVED alone, whatever measurement it was computed from
PURE_DERIVED = re.compile(r"^(?:derived|computed) from|Wiedemann-Franz|transmission-line calculation", re.I)
IMAGING = {"SEM", "TEM", "OPTICAL", "AFM"}


def suppress(s, hits):
    """Drop second families that are the subject of an imaging string, or a synonym of the first."""
    if PURE_DERIVED.search(s):
        return ["DERIVED"]
    fams = [h.split(":")[0] for h in hits]
    out = list(hits)
    if "TEM:EBSDtransmission" in out and "EBSD" in out:
        out.remove("EBSD")                               # one technique, not two
    if "ASSAY:stain" in out and "OPTICAL:fluorescence" in out:
        out.remove("OPTICAL:fluorescence")               # the stain is the technique; optical is how it is read
    if "EBSD" in fams and "OPTICAL" in fams:
        out = [h for h in out if not h.startswith("OPTICAL")]
    if set(fams) & IMAGING and "MECH" in fams and re.search(r"\bof\b", s):
        out = [h for h in out if not h.startswith("MECH")]   # "SEM of worn surfaces": subject, not technique
    if "ASSAY" in fams and "DERIVED" in fams:
        out = [h for h in out if h != "DERIVED"]
    return out


def normalize(s):
    """Returns (list of FAMILY:mode, flags)."""
    hits, flags = [], []
    for rx, fam, mode in RULES:
        if rx.search(s):
            tag = f"{fam}:{mode}" if mode else fam
            if tag not in hits:
                hits.append(tag)
    hits = suppress(s, hits)
    fams = []
    for h in hits:
        f = h.split(":")[0]
        if f not in fams:
            fams.append(f)
    if len(fams) > 1:
        flags.append("multi_technique")
        # keep the first tag of each distinct family, in rule order
        seen, keep = set(), []
        for h in hits:
            f = h.split(":")[0]
            if f not in seen:
                seen.add(f)
                keep.append(h)
        hits = keep
    elif len(hits) > 1:
        hits = hits[:1]          # one family, several mode cues: the most specific rule fired first
    if not hits:
        hits, flags = ["OTHER"], flags + ["unmapped"]
    return hits, flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    D = Path(a.dir)

    uses, mapping, unmapped, multi = Counter(), {}, {}, {}
    SKIP = {"ab.json", "summary.json", "technique_map.json", "technique_unmapped.json"}
    files = [f for f in sorted(D.glob("*.json"))
             if not f.name.endswith(".build.json") and f.name not in SKIP]
    changed = 0
    for f in files:
        g = json.load(open(f))
        dirty = False
        for n in g.get("nodes", []):
            t = (n.get("attrs") or {}).get("technique")
            if not t:
                continue
            s = str(t)
            uses[s] += 1
            tags, flags = normalize(s)
            mapping[s] = tags
            if "unmapped" in flags:
                unmapped.setdefault(s, 0)
                unmapped[s] += 1
            if "multi_technique" in flags:
                multi.setdefault(s, tags)
            n["attrs"]["technique_norm"] = tags if len(tags) > 1 else tags[0]
            if flags:
                n["attrs"]["technique_flags"] = flags
            dirty = True
        if dirty and a.write:
            json.dump(g, open(f, "w"), ensure_ascii=False, indent=1)
            changed += 1

    fam_counts = Counter()
    for s, c in uses.items():
        for tag in mapping[s]:
            fam_counts[tag.split(":")[0]] += c
    json.dump({k: mapping[k] for k in sorted(mapping)}, open(D / "technique_map.json", "w"), indent=1)
    json.dump({"unmapped_strings": unmapped, "multi_technique": multi}, open(D / "technique_unmapped.json", "w"), indent=1)
    print(f"{len(uses)} distinct strings, {sum(uses.values())} uses, {len(files)} graphs"
          + (f", {changed} written" if a.write else " (dry run)"))
    print("by family:", dict(fam_counts.most_common()))
    print("multi-technique strings:", len(multi), list(multi.items())[:6])
    print("unmapped -> OTHER:", len(unmapped), list(unmapped)[:10])


if __name__ == "__main__":
    main()
