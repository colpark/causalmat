"""Zero-cost corpus counts over MatMech for the fm-advantage-benchmark discovery/supply stages.

Usage: python scripts/corpus_stats.py <extracted matmech root> [out.json]

Counts only; no model calls. Every number is over papers or mechanisms, stated per key.
"""
import json
import os
import re
import sys
from collections import Counter

ROOT = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else "results/corpus_stats.json"

NUM = re.compile(r"[-+]?\d+(?:\.\d+)?\s*(?:°C|K|nm|µm|μm|mm|eV|meV|MPa|GPa|%|mA|V|S/cm|mAh|h|min|wt|at|Å|°)")
CHAR = {
    "XRD": r"\bXRD\b|X-ray diffraction",
    "SEM": r"\bSEM\b|scanning electron",
    "TEM": r"\bTEM\b|HRTEM|transmission electron",
    "XPS": r"\bXPS\b|photoelectron",
    "Raman": r"Raman",
    "FTIR": r"FTIR|FT-IR|infrared",
    "XAS": r"\bXAS\b|XANES|EXAFS|absorption fine",
    "EBSD": r"EBSD",
    "DFT": r"\bDFT\b|density functional|first-principles|first principles",
    "tensile": r"tensile",
    "hardness": r"hardness",
    "electrochem": r"voltammetry|impedance|EIS\b|galvanostatic|charge.discharge",
    "UV-vis": r"UV.vis|absorbance|band ?gap",
    "TGA/DSC": r"\bTGA\b|\bDSC\b|thermogravimetric",
}
CHAR = {k: re.compile(v, re.I) for k, v in CHAR.items()}


def records(root):
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if fn.endswith(".json"):
                p = os.path.join(dp, fn)
                try:
                    yield p, json.load(open(p, encoding="utf-8"))
                except Exception as e:  # unprocessable unit: counted, never repaired
                    yield p, e


c = Counter()
link, chain_types, depth, years, cats, chars, conf_bins, conflict_kinds = (Counter() for _ in range(8))
# joint supply per candidate task family (mechanism-level, see docs/ANALYSIS.md section 5)
supply = Counter()
formula_ok = 0
ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os
Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am""".split())
TOKEN = re.compile(r"([A-Z][a-z]?)(\d*(?:\.\d+)?)")


def is_formula(s):
    """True when s is a bare stoichiometric formula (joinable to Materials Project / OQMD by composition)."""
    s = re.sub(r"[₀-₉]", lambda m: str(ord(m.group()) - 0x2080), s).replace(" ", "")
    s = re.sub(r"[()\[\]·.\-+δxyz]", "", s)
    toks = TOKEN.findall(s)
    return bool(toks) and "".join(a + b for a, b in toks) == s and all(a in ELEMENTS for a, _ in toks)


def norm_link(l):
    return re.sub(r"Properties", "Property", l or "").replace("->", "→")

for path, d in records(ROOT):
    if isinstance(d, Exception) or not isinstance(d, dict) or "mechanism" not in d:
        c["unprocessable_files"] += 1
        continue
    c["papers"] += 1
    years[d.get("year")] += 1
    for cat in d.get("material_category") or []:
        cats[cat] += 1
    imgs = d.get("image_info") or []
    c["images"] += len(imgs)
    c["images_microscopic"] += sum(1 for i in imgs if i.get("microscopic_image"))
    mo = d.get("material_object") or ""
    formula_ok += bool(mo) and is_formula(mo)
    mechs = d.get("mechanism") or []
    c["papers_with_mechanism"] += bool(mechs)
    for m in mechs:
        c["mechanisms"] += 1
        link[norm_link(m.get("link"))] += 1
        mm = m.get("mechanism") or {}
        chain = mm.get("reasoning_chain") or []
        types = {s.get("type", "").replace("_", " ").strip() for s in chain}
        for t in types:
            chain_types[t] += 1
        evid = types - {"deductive reasoning", "inductive reasoning"}
        depth[len(evid)] += 1
        c["mech_with_image"] += bool(m.get("images"))
        c["mech_with_microscopic_image"] += any(i.get("microscopic") for i in m.get("images") or [])
        exp = m.get("experiment") or {}
        res = f"{exp.get('result', '')}"
        c["mech_result_has_number_with_unit"] += bool(NUM.search(res))
        blob = f"{exp.get('type', '')} {exp.get('name', '')}"
        for k, rx in CHAR.items():
            if rx.search(blob):
                chars[k] += 1
        conf = mm.get("confidence")
        if isinstance(conf, (int, float)):
            conf_bins["<0.5" if conf < 0.5 else "0.5-0.8" if conf < 0.8 else ">=0.8"] += 1
        has_conflict = bool(mm.get("conflict_detection"))
        for ek in m.get("external_knowledge") or []:
            if ek.get("conflict_detection"):
                has_conflict = True
                conflict_kinds[ek.get("type")] += 1
        c["mech_with_conflict_flag"] += has_conflict

        has_num = bool(NUM.search(res))
        has_img = bool(m.get("images"))
        has_micro = any(i.get("microscopic") for i in m.get("images") or [])
        is_formula_mat = bool(mo) and is_formula(mo)
        hi_conf = isinstance(conf, (int, float)) and conf >= 0.8
        post = isinstance(d.get("year"), int) and d["year"] >= 2025
        diffraction = bool(CHAR["XRD"].search(blob))
        # C1 mechanism discrimination under evidence acquisition: >=3 evidence kinds, an image, grounded
        supply["C1_depth3_image_hiconf"] += len(evid) >= 3 and has_img and hi_conf
        # C2 anomaly / conflict diagnosis: a cross-paper conflict flag
        supply["C2_conflict_flag"] += has_conflict
        # C3 structure-from-pattern: diffraction experiment, formula-joinable material, numeric result
        supply["C3_xrd_formula_number"] += diffraction and is_formula_mat and has_num
        supply["C3_xrd_formula_number_Processing->Structure"] += (
            diffraction and is_formula_mat and has_num and norm_link(m.get("link")).startswith("Processing → Structure"))
        # C4 quantitative effect prediction: numeric result on a Processing/Structure -> Property link
        supply["C4_numeric_to_property"] += has_num and norm_link(m.get("link")).endswith("Property")
        # microscopy-grounded structure claims
        supply["micro_image_Processing->Structure"] += has_micro and norm_link(m.get("link")) == "Processing → Structure"
        # contamination: published 2025 or later (closest to subject cutoffs; still pre-cutoff for recent models)
        supply["any_published_2025plus"] += post
        supply["C1_supply_published_2025plus"] += post and len(evid) >= 3 and has_img and hi_conf

out = {
    "root": ROOT,
    "counts": dict(c),
    "papers_material_object_is_formula": formula_ok,
    "link_types": dict(link.most_common()),
    "reasoning_step_types_per_mechanism": dict(chain_types.most_common()),
    "claimed_depth_distinct_evidence_types": dict(sorted(depth.items())),
    "characterization_in_experiment": dict(chars.most_common()),
    "mechanism_confidence": dict(conf_bins),
    "conflict_flags_by_knowledge_type": dict(conflict_kinds),
    "candidate_supply_mechanisms": dict(supply),
    "material_category": dict(cats.most_common(20)),
    "year": dict(sorted((k, v) for k, v in years.items() if isinstance(k, int))),
}
os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
json.dump(out, open(OUT, "w"), indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False))
