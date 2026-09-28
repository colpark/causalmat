"""config.py: everything groundchain v1 pins, in one place.

Two model roles only, one pinned version each. The panel pipeline is MatMech's, unchanged:
the same YOLO checkpoint and the same match run version, so panel tiers here are comparable
with MatMech's numbers rather than merely similar.
"""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)

CSV = R('data/m2m/matter_to_mechanism.csv')
CORPUS = R('m2m_corpus')
OUT = R('results/groundchain_v1')

# --- the two model roles -------------------------------------------------------------------
# One version each, recorded so the report can name it. gc-answerer holds Read (it must open
# panel crops); gc-checker holds no tools at all.
ANSWERER = {'agent': 'gc-answerer', 'model': 'sonnet', 'model_id': 'claude-sonnet-5'}
CHECKER = {'agent': 'gc-checker', 'model': 'sonnet', 'model_id': 'claude-sonnet-5'}
REPEATS = 3

# --- the panel pipeline, pinned to MatMech's own run ----------------------------------------
DETECT = {
    'script': 'scripts/panels/detect_panels.py',
    'weights': '/home/aid1/matmmextract/examples/.weights_cache/'
               '10garsNWEdgzMGX9nyDE8dMABkU_3BYp9.pt',
    'weights_sha256_prefix': '7a92fbc6571e',
    'run_version': 'matmmextract-yolo12m/7a92fbc6571e/imgsz640/v1',
    'params': {'imgsz': 640, 'conf': 0.25, 'iou': 0.5},
}
MATCH = {'script': 'scripts/panels/match_panels.py', 'run_version': 'match/v4'}

# MatMech's own tier split, for the comparison the report has to make (per figure)
MATMECH_TIERS = {'A': 146836, 'B': 159254, 'C': 119205}

# --- selection -----------------------------------------------------------------------------
# The brief asked for 2023+, a cap of 6 per publisher, and 20 picks + 10 reserves. Those three
# cannot hold together on this corpus: Europe PMC is the only route by which figures actually
# come down (every publisher site except Nature returns 403 or a bot wall), which leaves 29
# papers at 2023+, and ACS is 18 of them, so a cap of 6 yields 16 -- no reserves and short of
# the 20. Relaxed to 2021+ and a cap of 10 on the user's decision, which yields 28 = 20 + 8.
N_PICK, N_RESERVE, MIN_YEAR, MAX_PER_PUBLISHER, MIN_FIGURES = 20, 8, 2021, 10, 4
BRIEF_DEFAULTS = {'min_year': 2023, 'max_per_publisher': 6, 'n_reserve': 10,
                  'would_yield': 16, 'relaxed_by': 'user decision after the pool was measured'}

# Characterization techniques. A paper needs two DIFFERENT families to qualify, so that
# "XRD and SAXS" counts as two routes and "CV and CV at another rate" does not.
TECHNIQUES = {
    'XRD': ['xrd', 'x-ray diffraction', 'sxrd', 'hexrd', 'operando xrd', 'rietveld',
            'neutron diffraction', 'selected area electron diffraction', 'saed'],
    'XPS': ['xps', 'x-ray photoelectron'],
    'XAS': ['xas', 'xanes', 'exafs', 'x-ray absorption', 'nexafs', 'soft xas'],
    'EM': ['sem', 'tem', 'hrtem', 'stem', 'haadf', 'cryo-em', 'scanning electron',
           'transmission electron', 'fib'],
    'SPM': ['afm', 'atomic force', 'kpfm', 'stm'],
    'SPECTRO': ['raman', 'ftir', 'infrared', 'uv-vis', 'photoluminescence', 'ellipsometry'],
    'NMR': ['nmr', 'magic angle', 'mas nmr', 'epr', 'esr'],
    'ECHEM': ['cyclic voltammetry', 'cv', 'eis', 'impedance', 'gitt', 'pitt',
              'galvanostatic', 'chronoamperometry', 'linear sweep', 'rate capability'],
    'THERMAL': ['tga', 'dsc', 'thermogravimetric', 'calorimetry', 'arc'],
    'SCATTER': ['saxs', 'sans', 'small-angle', 'usaxs'],
    'SURFACE': ['bet', 'bjh', 'adsorption isotherm', 'porosimetry'],
    'COMP': ['icp', 'eds', 'edx', 'edxs', 'elemental mapping', 'tof-sims', 'sims'],
}

# Domain: battery or electrochemical storage.
#
# Split deliberately. The first pass used one flat list and let six off-domain papers through
# to the picks -- arsenate dissolution, arsenic bioaccessibility, a solid oxide fuel cell, PEM
# fuel cell ORR, alkaline water splitting, PEM water electrolysis -- because every one of them
# says "electrode" and "electrolyte". Those words do not name a storage device. A paper now
# qualifies only on a STRONG term, which names a storage device or a storage-specific process.
STRONG = ['batter', 'supercapacitor', 'supercapattery', 'li-ion', 'lithium-ion', 'na-ion',
          'sodium-ion', 'k-ion', 'potassium-ion', 'zinc-ion', 'zn-ion', 'zinc ion',
          'lithium-sulfur', 'li-s batter', 'lithium metal anode', 'solid-state batter',
          'all-solid-state', 'redox flow', 'flow batter', 'intercalation', 'deintercalation',
          'solid electrolyte interphase', ' sei ', 'cathode material', 'anode material',
          'coulombic efficiency', 'state of charge', 'charge-discharge', 'cycling stability',
          'specific capacity', 'rate capability', 'electrochemical storage', 'energy storage']
# Present in storage papers but equally in fuel cells and electrolysers; never qualifying alone.
WEAK = ['electrode', 'electrolyte', 'anode', 'cathode', 'lithium', 'sodium', 'potassium']
DOMAIN = STRONG + WEAK
# A different device class. Vetoes unless a STRONG term is also present.
OFFDOMAIN = ['fuel cell', 'electrolyzer', 'electrolyser', 'water splitting', 'water electrolysis',
             'photocatal', 'electrocatal', 'solar cell', 'photovoltaic', 'thermoelectric',
             'co2 reduction', 'co2r', 'oxygen evolution', 'hydrogen evolution', 'oxygen reduction',
             ' oer', ' her ', ' orr', 'perovskite solar', 'bioaccessibility', 'bioavailability',
             'soil', 'groundwater', 'remediation', 'toxicity', 'drinking water',
             'desalination', 'membrane distillation', 'sensor', 'biosensor']
REVIEWISH = ['review', 'perspective', 'roadmap', 'outlook', 'survey', 'tutorial',
             'meta-analysis', 'policy', 'commentary', 'editorial']
