"""Papers with SEM and more than two FM-addressable modalities.

"FM-addressable" means a modality for which a pretrained encoder, predictor, generator or simulator
exists today that takes this kind of input (or, for composition, this kind of object). The map is
declared below and is the assumption the counts rest on; change it and rerun.

Evidence per paper is pooled from three independent sources:
  panels   - modality/technique cues on accepted (tier A/B) panel definitions + caption preambles
  flags    - MatMech's own microscopic_image flag per figure
  methods  - experiment `type`/`name` strings in MatMech's extracted mechanisms

Usage: python fm_supply.py --root ~/Documents/causalmat/matmech --out fm_supply.json [--workers 18]
"""
import argparse
import json
import re
import sys
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from panel_modalities import TECH, FORM, classify  # noqa: E402

# modality -> tools that take this input today, with the availability tier from the operator's list:
#   immediate   = open license, pip/git, no registration
#   gated       = click-through or registration (hours to days)
#   procurement = commercial/site licence (weeks+)
#   unclear     = repository carries no usable licence statement; ask the authors
FM_MODALITIES = {
    "electron micrograph": {
        "encoder": ("SAM, DINOv2", "immediate"), "encoder_alt": ("DINOv3", "gated"),
        "simulator": ("abTEM / Prismatic multislice (TEM), CASINO (SEM)", "immediate"),
        "unclear": "EM-DINO, EMCF weights", "tier": "immediate"},
    "scanned-probe micrograph": {"encoder": ("SAM, DINOv2", "immediate"), "tier": "immediate"},
    "optical/fluorescence micrograph": {"encoder": ("SAM, DINOv2", "immediate"), "tier": "immediate"},
    "diffraction pattern": {
        "simulator": ("pymatgen XRD calculator, GSAS-II refinement", "immediate"),
        "generator": ("XtalNet, deCIFer, DiffractGPT", "unclear"),
        "refiner_alt": ("TOPAS", "procurement"), "tier": "immediate"},
    "elemental map": {"simulator": ("DTSA-II, CASINO", "immediate"), "encoder": ("SAM, DINOv2", "immediate"),
                      "alt": ("PENELOPE", "gated"), "tier": "immediate"},
    "orientation map": {"simulator": ("EMsoft pattern simulation/indexing", "immediate"),
                        "encoder": ("SAM, DINOv2", "immediate"), "tier": "immediate"},
    "core-level spectrum": {"simulator": ("SESSA (XPS, NIST)", "immediate"),
                            "simulator_alt": ("FEFF10 (XAS)", "gated"),
                            "predictor": ("OmniXAS", "unclear"), "tier": "immediate"},
    "vibrational/optical spectrum": {"simulator": ("Quantum ESPRESSO + Phonopy (IR/Raman modes)", "immediate"),
                                     "tier": "immediate"},
    "electrochemical response": {"simulator": ("PyBaMM", "immediate"), "tier": "immediate"},
    "composition/structure": {
        "predictor": ("MACE-MP-0/MPA-0, MatterSim, Orb-v3, SevenNet", "immediate"),
        "predictor_alt": ("UMA", "gated"), "predictor_academic": ("MACE-OMAT-0/MH-1/POLAR-1, GRACE", "ASL academic"),
        "generator": ("MatterGen, DiffCSP, CDVAE", "immediate"),
        "simulator": ("LAMMPS + MLIP, Quantum ESPRESSO", "immediate"),
        "simulator_alt": ("VASP", "procurement"), "tier": "immediate"},
    "atomistic simulation": {"simulator": ("LAMMPS + MLIP surrogates, Quantum ESPRESSO", "immediate"),
                             "tier": "immediate"},
    "thermal/phase response": {"simulator": ("Phonopy (thermal properties)", "immediate"),
                               "simulator_alt": ("Thermo-Calc", "procurement"), "tier": "immediate"},
    "mechanical response": {"simulator": ("LAMMPS + MLIP (atomistic)", "immediate"),
                            "simulator_alt": ("Abaqus (continuum)", "procurement"), "tier": "immediate"},
}

# technique cue -> modality bucket
TECH2MOD = {
    "SEM": "electron micrograph", "TEM": "electron micrograph",
    "AFM/STM": "scanned-probe micrograph", "optical microscopy": "optical/fluorescence micrograph",
    "XRD": "diffraction pattern",
    "Raman": "vibrational/optical spectrum", "FTIR": "vibrational/optical spectrum",
    "UV-vis/PL": "vibrational/optical spectrum",
    "XPS": "core-level spectrum", "XAS": "core-level spectrum", "NMR": "core-level spectrum",
    "EDS/EDX": "elemental map", "EBSD": "orientation map",
    "simulation/DFT": "atomistic simulation",
    "electrochemistry": "electrochemical response",
    "mechanical test": "mechanical response",
    "thermal analysis": "thermal/phase response",
    "magnetic/transport": None, "biological assay": None, "particle size/porosity": None,
    "mass spec/chromatography": None,
}
TECH2MOD = {k: v for k, v in TECH2MOD.items() if v}
FORM2MOD = {"micrograph": "electron micrograph", "diffraction_pattern": "diffraction pattern",
            "spectrum": "vibrational/optical spectrum", "spatial_map": "elemental map",
            "orientation_distribution": "orientation map", "simulation_render": "atomistic simulation"}

ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os
Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am""".split())
TOKEN = re.compile(r"([A-Z][a-z]?)(\d*(?:\.\d+)?)")
SEM_RX = TECH["SEM"]


def is_formula(s):
    s = re.sub(r"[₀-₉]", lambda m: str(ord(m.group()) - 0x2080), s or "").replace(" ", "")
    s = re.sub(r"[()\[\]·.\-+δxyz]", "", s)
    toks = TOKEN.findall(s)
    return bool(toks) and "".join(a + b for a, b in toks) == s and all(a in ELEMENTS for a, _ in toks)


def do_folder(folder):
    folder = Path(folder)
    try:
        rec = json.load(open(folder / "data.json", encoding="utf-8"))
    except Exception:
        return None
    mods, src = {}, {}

    def add(mod, source):
        mods[mod] = mods.get(mod, 0) + 1
        src.setdefault(mod, set()).add(source)

    sem_src = set()
    # 1. panels from the match run
    mj = folder / "panels" / "match.json"
    n_panels = n_fig_AB = 0
    if mj.exists():
        try:
            m = json.load(open(mj))
        except Exception:
            m = {"figures": []}
        for f in m.get("figures", []):
            if f["tier"] == "C":
                continue
            n_fig_AB += 1
            pre = f.get("caption_preamble") or ""
            for p in f["panels"]:
                n_panels += 1
                text = f"{p.get('definition') or ''} {pre}"
                techs, form = classify(text)
                for t in techs:
                    if t in TECH2MOD:
                        add(TECH2MOD[t], "panels")
                    if t == "SEM":
                        sem_src.add("panels")
                if form in FORM2MOD and not techs:
                    add(FORM2MOD[form], "panels")
    # 2. MatMech microscopy flag
    imgs = rec.get("image_info") or []
    if any(i.get("microscopic_image") for i in imgs):
        add("electron micrograph", "flag")
    for i in imgs:
        cap = " ".join(i.get("image_caption") or [])
        if SEM_RX.search(cap):
            sem_src.add("caption")
    # 3. experiment strings in the extracted mechanisms
    for mech in rec.get("mechanism") or []:
        e = mech.get("experiment") or {}
        blob = f"{e.get('type', '')} {e.get('name', '')} {e.get('parameters', '')}"
        techs, _ = classify(blob)
        for t in techs:
            if t in TECH2MOD:
                add(TECH2MOD[t], "methods")
            if t == "SEM":
                sem_src.add("methods")
    mo = rec.get("material_object") or ""
    formula = is_formula(mo)
    if formula:
        add("composition/structure", "formula")
    return {"doi": folder.name, "journal": folder.parent.name, "year": rec.get("year"),
            "has_sem": bool(sem_src), "sem_sources": sorted(sem_src),
            "modalities": sorted(mods), "n_modalities": len(mods),
            "modality_sources": {k: sorted(v) for k, v in src.items()},
            "formula_joinable": formula, "panels_AB": n_panels, "figures_AB": n_fig_AB,
            "n_figures": len(imgs), "material": mo}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=18)
    a = ap.parse_args()
    root = Path(a.root).expanduser()
    folders = sorted(p.parent for p in root.glob("*/*/data.json"))
    rows = []
    with Pool(a.workers) as pool:
        for r in pool.imap_unordered(do_folder, (str(f) for f in folders), chunksize=64):
            if r:
                rows.append(r)
    sem = [r for r in rows if r["has_sem"]]
    target = [r for r in sem if r["n_modalities"] >= 3]
    strict = [r for r in target if r["formula_joinable"]]
    hist = Counter(r["n_modalities"] for r in sem)
    combos = Counter(" + ".join(r["modalities"]) for r in target)
    permod = Counter(m for r in target for m in r["modalities"])
    out = {
        "fm_modality_map": FM_MODALITIES,
        "papers_total": len(rows),
        "papers_with_sem": len(sem),
        "papers_sem_and_3plus_fm_modalities": len(target),
        "papers_sem_3plus_and_formula_joinable": len(strict),
        "modality_count_histogram_over_sem_papers": dict(sorted(hist.items())),
        "modality_presence_in_target": dict(permod.most_common()),
        "top_modality_combinations_in_target": dict(combos.most_common(15)),
        "target_by_year": dict(sorted(Counter(r["year"] for r in target if isinstance(r["year"], int)).items())),
        "target_by_journal": dict(Counter(r["journal"] for r in target).most_common()),
        "sem_evidence_sources": {"+".join(k): v for k, v in Counter(tuple(r["sem_sources"]) for r in sem).most_common()},
        "target_figure_totals": {"figures": sum(r["n_figures"] for r in target),
                                 "figures_tier_AB": sum(r["figures_AB"] for r in target),
                                 "panels_tier_AB": sum(r["panels_AB"] for r in target)},
    }
    json.dump(out, open(a.out, "w"), indent=1)
    json.dump([r for r in target], open(str(a.out).replace(".json", "_papers.json"), "w"), indent=1)
    print(json.dumps({k: out[k] for k in ("papers_total", "papers_with_sem", "papers_sem_and_3plus_fm_modalities",
                                          "papers_sem_3plus_and_formula_joinable",
                                          "modality_count_histogram_over_sem_papers",
                                          "modality_presence_in_target", "target_figure_totals")}, indent=1))


if __name__ == "__main__":
    sys.exit(main())
