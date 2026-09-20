import json, re, sys

KIT_VERSION = "modality-kit/v2"   # v2 = panel-crop support (D.panels); stamped into every spec and printed per run

OUTDIR = "/home/aid1/Documents/causalmat/site/modality"
try:   # only the built-in Ni-Co example needs this; --specs mode does not
    site = json.load(open("/home/claude/nico/case_site.json"))
    NICO_FIGS = {fid: {"src": f["src"], "caption": re.sub(r"\s+", " ", f["caption"]).strip()} for fid, f in site["figs"].items()}
except FileNotFoundError:
    site = {"figs": {}, "title": "Ni-Co example (not available here)", "doi": "", "journal": "", "year": 0}
    NICO_FIGS = {}

LANE_VARS = {"micro": "--micro", "atom": "--atom", "diff": "--atom", "spec": "--atom", "classic": "--classic"}

# =====================================================================================
# SPEC 1: Ni-Co hydroxide nanocages (Advanced Energy Materials 2015)
# =====================================================================================
NICO = dict(
 file="nico_modality_graph.html", short="Ni-Co hydroxide nanocages", journal="Advanced Energy Materials", year=2015,
 title=site["title"].replace("Ni–Co", "Ni-Co"), doi=site["doi"], figs=NICO_FIGS,
 lanes=[dict(key="micro", label="Microscopy: SEM, TEM", sub="foundation model in hand or candidate"),
        dict(key="atom", label="Atomistics: DFT to universal MLIP", sub="foundation model candidate"),
        dict(key="classic", label="Classical tools", sub="collapsed to one node per state")],
 states=[
  dict(id="S0", stage="HYP", title="Hypothesis and design", head="The Ni/Co ratio in amorphous Ni-Co hydroxide sets surface O* reactivity and thereby OER activity.",
       detail="Need: an efficient, stable, earth-abundant OER catalyst in alkaline media. Gap: why activity varies with metal ratio across double hydroxides is unexplained. Design: seven compositions from Ni(OH)2 to Co(OH)2, hollow nanocages templated on Cu2O by Na2S2O3 etching, and solid ~10 nm particles as the architecture control. Figure 1 is the synthesis schematic.", figs=["F1"], source="h1, h2, h3, d1, d2, d3, p1"),
  dict(id="S1", stage="STR", title="Structure state", head="Hollow ~80 nm cages with a ~15 nm rough amorphous shell, composition NiCo2.7(OH)x, both metals divalent.",
       detail="Three claims sit here: cage morphology (s1), amorphous state (s2), composition and valence (s3). Microscopy resolves the first. SAED, EDS, XPS and EXAFS resolve the second and third.", figs=[], source="s1, s2, s3"),
  dict(id="S2", stage="MEC", title="Reactivity state and mechanism", head="O* binding energy is non-monotonic in Co content and peaks near 67% Co. O* adsorption is rate-determining, so composition acts through reactivity.",
       detail="The computed descriptor (r1) and the paper's mechanism (m1). Premises: O* binding reported as the OER rate-determining step in earlier work (k3), with the Sabatier caveat that stronger binding can impede O-O bond making (k4). Figure 5 draws composition to reactivity to activity and labels the last link 'deduction'.", figs=["F5"], source="r1, m1, k3, k4"),
  dict(id="S3", stage="PRF", title="Activity and performance state", head="OER activity is a volcano in Co content peaking at 73% Co. eta10 = 0.35 V and 10 h stability at 10 mA cm-2 through the 4e- path.",
       detail="Property r2, performance f1 and f2, and the architecture claim m2 that cages add activity beyond composition (hollow eta10 0.36 V against solid 0.39 V, text only).", figs=[], source="r2, f1, f2, m2, o21"),
  dict(id="S4", stage="DSC", title="Conclusion", head="Amorphous NiCo2.7(OH)x cages are efficient and stable because the Ni/Co ratio maximizes O* binding.",
       detail="Supported by f1, f2 and m1. The comparison node x1 places the catalyst beside reported transition-metal catalysts, with NiFe-GO LDH still better at eta10 = 0.21 V.", figs=[], source="c1, x1"),
 ],
 nodes=[
  dict(id="M1", lane=0, row="S1", line=0, title="SEM, Figure 2a", tech="SEM", figs=["F2"], panel="F2a", head="Measures cage size and surface texture: rough spheroids 50 to 105 nm, mostly 70 to 85 nm.", solves="Size and roughness in the structure state.", op="measure feature metric", verdict="shown",
       fm="BNL SEM foundation model (ViT-L masked autoencoder with mixture of experts, 125k images). Needs a task head for size distribution and texture.", source="o1"),
  dict(id="M2", lane=0, row="S1", line=1, title="TEM, Figure 2b, c", tech="TEM", figs=["F2"], panel="F2b, F2c", head="Shows the shells are hollow: dark 12 to 15 nm rim around a light core, a ~40 nm cavity in a 70 nm cage.", solves="Hollowness in the structure state, which SEM cannot see.", op="inspect local feature", verdict="shown",
       fm="Candidates: EM-DINO (EM-5M), the EMCF corpus, SAM based zero-shot segmentation. Control arm: DINOv2 or DINOv3 with a linear probe.", note="Outlines are rounded or ovoid rather than the faceted rhombus drawn in Figure 1.", source="o1"),
  dict(id="M3", lane=0, row="S1", line=2, audit=True, title="TEM audit, Figure 2b", tech="TEM", figs=["F2"], panel="F2b", head="The field shows flaky sheet debris and dark collapsed particles between cages. The text says the product is exclusively high-quality nanocages.", solves="Qualifies the structure state. The figure contradicts the text.", op="assess spatial distribution", verdict="contradicts", text_silent=True,
       fm="Same candidates as TEM. A debris-present classifier on the embedding is the cleanest test item in this paper.", source="o2"),
  dict(id="M4", lane=0, row="S3", line=0, textonly=True, title="TEM after 10 h (text only)", tech="TEM", figs=[], panel=None, head="The paper says the cages keep shape, size and amorphous state after 10 h. The image sits in the supplement, outside the packet.", solves="Stability in the activity state, as a text claim only.", op=None, verdict="text only",
       fm="Becomes a TEM item once the supplementary image is pulled in.", source="o20"),
  dict(id="A1", lane=1, row="S2", line=0, title="DFT, Figure 4a, b", tech="DFT", figs=["F4"], panel="F4a, F4b", head="A NixCo(3-x)O6H6 cluster with an O* adsorbate. O* binding at 0, 33, 67, 100% Co: 4.21, 4.87, 6.17, 5.09 eV.", solves="The descriptor in the reactivity state.", op="read trend", verdict="shown",
       fm="A universal MLIP (UMA, MACE-MPA-0, MatterSim, Orb-v3) can re-relax the clusters and add the missing 50, 85 and 90% points, with a DFT single point as the check. A radical O* on a charged hydroxide cluster sits at the edge of their training data.", source="k2, o22"),
  dict(id="A2", lane=1, row="S2", line=1, audit=True, title="Bridge audit, Figure 3b x Figure 4b", tech="DFT + Electrochem", figs=["F3", "F4"], panel="F3b, F4b", head="The reactivity to activity link rests on a rank match over four shared compositions. DFT peaks at 67% Co, the measurement at 73%, and 50, 85, 90% have no DFT counterpart.", solves="Qualifies the mechanism. A four-point rank match cannot separate a monotonic from a volcano relation.", op="correlate across series", verdict="qualifies", text_silent=True,
       fm="Filling the DFT gap with a universal MLIP turns this audit into a counterfactual item: does the completed computed curve still rank the measured one?", source="o23, o11, o22"),
  dict(id="C1", lane=2, row="S1", line=3, title="Classical, Figure 2c to h", tech="SAED, EDS, XPS, EXAFS", figs=["F2"], panel="F2c inset, F2d, F2e, F2f to h", head="SAED: diffuse halo, no rings. EDS: Co 10.84, Ni 3.99 at% (1:2.72). XPS: 2p splittings 17.6 and 16.1 eV with satellites. EXAFS: N about 5, text only.",
       detail="SAED on the cages shows a diffuse halo and no Bragg rings, so the shells are amorphous. The EDS table gives Co 10.84 and Ni 3.99 at%, a 1:2.72 ratio, and the line scan shows Co and Ni rising at both walls with Co about twice Ni. XPS puts Ni 2p3/2 at 856.1 eV and Co 2p3/2 at 781.3 eV, with 17.6 and 16.1 eV splittings and strong satellites, so both metals are divalent. EXAFS coordination numbers near 5 against 6 in crystalline references appear only in the text.",
       solves="Phase, composition and valence in the structure state.", op="recognize signature, convert to quantity, assign features", verdict="shown", inner_audit="The EDS spectrum's tallest peak is Cu with S beside it. The formula names only Ni and Co, and the at% table omits Cu, S, O and C.",
       fm="No foundation model. Line-library lookup, NMF unmixing and reference splittings do this exactly.", source="o3, o4, o5, o6, o7, o8, o9, k1"),
  dict(id="C2", lane=2, row="S3", line=1, title="Electrochemistry, Figure 3", tech="LSV, Tafel, CA, CP, RRDE", figs=["F3"], panel="F3a to F3f", head="LSV: volcano in j at 1.60 V, 17.8 mA cm-2 at 73% Co. Tafel 65 mV/dec. eta10 0.35 V at 1.58 V. 10 h CA and CP. RRDE: FE 0.98 to 0.99, ~2% peroxide.",
       detail="The LSV curves and the current density at 1.60 V give the volcano in Co content, 17.8 mA cm-2 at 73% Co. Tafel slopes fall from 182 to 65 mV/dec at 73% Co. The NiCo2.7 curve crosses 10 mA cm-2 near 1.58 V, so eta10 is 0.35 V. Chronoamperometry and chronopotentiometry hold for 10 h with a slight improvement. The rotating ring-disk data give an O2 Faradaic efficiency of 0.98 to 0.99 with about 2% peroxide, which closes the charge balance for the 4e- path.",
       solves="The activity and performance state.", op="read trend, fit model, read characteristic point, compare coplotted quantities", verdict="shown", inner_audit="The stated 1.48 V onset is not resolvable on Figure 3a's 0 to 20 mA cm-2 axis. The curves leave the baseline gradually between 1.47 and 1.52 V.",
       fm="No foundation model for polarization curves. Tafel fits, characteristic points and the ring-disk charge balance are classical and verifiable.", source="o10 to o19"),
 ],
 edges=[("S0","S1","produces"),("S1","S2","causes"),("S2","S3","explains"),("S3","S4","supports"),("S2","S4","supports"),
        ("M1","S1","evidences"),("M2","S1","evidences"),("M3","S1","qualifies"),("M4","S3","evidences"),
        ("A1","S2","evidences"),("A2","S2","qualifies"),("A1","A2","derives"),("C2","A2","derives"),
        ("C1","S1","evidences"),("C2","S3","evidences")],
)

# =====================================================================================
# SPEC 2: Stretchable nanowire photodetector (Advanced Materials 2015)
# =====================================================================================
PHOTO = dict(
 file="photodetector_modality_graph.html", short="Stretchable QD-P3HT nanowire photodetector", journal="Advanced Materials", year=2015,
 title="A Stretchable Nanowire UV-Vis-NIR Photodetector with High Performance", doi="https://doi.org/10.1002/adma.201404945", figs={},
 lanes=[dict(key="micro", label="Microscopy: SEM, TEM, optical", sub="foundation model in hand or candidate"),
        dict(key="classic", label="Classical tools", sub="collapsed to one node per state")],
 states=[
  dict(id="S0", stage="HYP", title="Hypothesis and design", head="PbS quantum dots dispersed in P3HT nanowires sensitize the NIR response, and freestanding nanowire arches tolerate substrate stretching.",
       detail="Need: stretchable optoelectronics want broadband UV to NIR photodetectors, and prior UV-NIR nanowire detectors have low ON/OFF ratios. Design: a P3HT conjugated-polymer nanowire as the UV-vis photoconducting matrix, PbS quantum dots blended in as NIR sensitizers, QD loading swept 0 to 60 wt% at 4.4 nm and QD size swept 4.4 to 9.1 nm at 60 wt%, single freestanding arches bridging Au-Al electrodes and a 3x3 array embedded in PDMS. Processing: meniscus-guided direct writing from a toluene blend.", figs=[], source="a1 to a6, a8, a7, a9"),
  dict(id="S1", stage="STR", title="Structure state", head="A freestanding arched nanowire bridges the electrodes, with PbS quantum dots uniformly dispersed in the P3HT wire and still rock-salt PbS.",
       detail="Arch shape (a11), QD dispersion (a14) and QD phase identity (a15). The structure stage is thin: one SEM inset, one TEM field, one EDS spectrum.", figs=[], source="a11, a14, a15"),
  dict(id="S2", stage="PRP", title="Property state and mechanisms", head="Broadband UV to NIR response with ON/OFF up to ~600 and sub-0.2 s UV-vis response. ON/OFF rises with QD loading and falls with QD size.",
       detail="Two property strands (a20, a25) with three mechanisms: the NIR response comes from excitonic absorption of the PbS QDs (a21), more QDs raise absorbance and photocarrier generation (a26, correlational only), and photoinduced hole transfer from QD to P3HT is restricted for larger dots by band alignment (a28).", figs=[], source="a20, a21, a25, a26, a28"),
  dict(id="S3", stage="PRF", title="Performance state under stretch", head="The arch unfolds to absorb substrate strain, so the array keeps its UV-NIR photoresponse up to 100% stretch and through 100 cycles.",
       detail="Mechanism a30 (the nanowire itself is barely strained because the arch geometry changes) and performance a33.", figs=[], source="a30, a33"),
  dict(id="S4", stage="DSC", title="Conclusion", head="Direct-written QD-P3HT nanowire arches give stretchable broadband photodetectors with high, strain-insensitive photoresponse.",
       detail="The paper adds that the UV-vis ON/OFF sits two orders above previous UV-NIR nanowire detectors (a35) and points to wearable optoelectronics (a37).", figs=[], source="a36, a35, a37"),
 ],
 nodes=[
  dict(id="M1", lane=0, row="S1", line=0, title="SEM inset, Figure 1", tech="SEM", figs=["F1"], panel="F1 inset", head="A single nanowire arch spans the Au-Al electrode gap. The arch path is marked by a drawn curve, and the thin wire is barely resolved at the 10 um scale.", solves="Arch geometry in the structure state.", op="inspect local feature", verdict="partial",
       fm="SEM foundation model, but a weak item: the read depends on the drawn guide more than on the image.", source="a10"),
  dict(id="M2", lane=0, row="S1", line=1, title="TEM, Figure 1", tech="TEM", figs=["F1"], panel="F1", head="Dark QD dots of a few nanometres are scattered along the whole wire without visible aggregates. One wire, one field.", solves="QD dispersion in the structure state.", op="assess spatial distribution", verdict="shown",
       fm="TEM candidates: EM-DINO, EMCF, SAM based segmentation. A dispersed-versus-aggregated classifier on the embedding, with DINOv2 as the control. One field limits what any model can claim.", source="a12"),
  dict(id="M3", lane=0, row="S3", line=0, title="Optical microscopy, Figure 4", tech="Optical", figs=["F4"], panel="F4a, F4b", head="The arch straightens from curved at 0% to nearly flat at 100% stretch and stays attached. F4b is a photograph of the PDMS array bent by hand.", solves="Arch unfolding in the performance state.", op="compare across conditions", verdict="shown",
       fm="Not an SEM or TEM item. A generic vision model with a curvature read (arch height against strain) is the natural probe.", source="a29"),
  dict(id="C1", lane=1, row="S1", line=2, title="EDS, Figure 1", tech="EDS", figs=["F1"], panel="F1", head="The EDS spectrum shows Pb and S lines. Cu and most of the C come from the grid and mesh.", solves="QD identity in the structure state. Rock-salt PbS is asserted without a diffraction figure.", op="assign features", verdict="shown",
       fm="No foundation model. Line-library lookup.", source="a13, a15"),
  dict(id="C2", lane=1, row="S2", line=0, title="Optical spectroscopy, Figure 3", tech="Absorption, PL", figs=["F3"], panel="F3", head="An absorption band near 1150 nm appears in QD films and is absent in P3HT; clear at 60 and 40 wt%, barely visible at 20. Absorbance at 300 to 650 nm rises stepwise with wt%. QD PL is quenched in the blend, strongly at 4.4 nm and weakly at 5.5 nm.",
       detail="Three spectral reads carry the mechanisms. The 1150 nm band supports QD sensitization (a21). The stepwise absorbance rise across the same wt% series supports the absorbance explanation (a26), which is correlational only. The PL quenching ratios, about 0.67 at 4.4 nm, 0.8 at 4.7 and 0.9 at 5.5, support size-limited hole transfer (a28).",
       solves="The sensitization and charge-transfer mechanisms in the property state.", op="recognize signature, read trend", verdict="partial",
       fm="No foundation model for QD film spectra. Peak presence and quenching ratios are classical reads.", source="a19, a23, a27"),
  dict(id="C3", lane=1, row="S2", line=1, title="Photoresponse, Figs 2 to 4", tech="I-t curves", figs=["F2", "F3", "F4"], panel="F2, F3a, F3c, F4c to e", head="Single wire: ON/OFF ~300 at 365 nm, ~600 at 625 nm, ~15 at 850 nm; rise and fall below 0.16 and 0.11 s in the UV. ON/OFF rises with wt% and falls with QD size. Array: ~50/28/4 and flat over 0 to 100% stretch and 100 cycles.",
       detail="Single-wire ON/OFF over six cycles with the 625 nm ON level drifting from ~620 to ~480 (a16), response times of 0.16/0.11 s UV, 0.16/0.12 s visible, 0.58/0.48 s NIR (a17), no NIR response at 0 wt% (a18), ON/OFF rising with wt% at all nine wavelengths, 625 nm from ~9 to ~200 (a22), falling with QD size 4.4 to 9.1 nm (a24), and array ON/OFF and times flat across strain and cycles (a31, a32).",
       solves="The property state and the performance state.", op="read characteristic point, read trend", verdict="shown",
       fm="No foundation model for photocurrent transients. Peak ratios and rise times are classical and verifiable.", source="a16, a17, a18, a22, a24, a31, a32"),
  dict(id="C4", lane=1, row="S3", line=1, audit=True, title="Photoresponse audit, Figs 2 to 4", tech="I-t curves", figs=["F2", "F3", "F4"], panel="F2 vs F3a vs F4e", head="Array ON/OFF at 625 nm (~50) sits ~10x below the single-wire value in Figure 2 (~600), and Figure 3a gives ~200 for the same composition. Light intensities are similar. The text calls both 'high performance'.", solves="Qualifies both the property and the performance states.", op="cross check consistency", verdict="qualifies", text_silent=True,
       fm="A cross-figure consistency item. No model needed, only three reads and a ratio.", source="a34"),
 ],
 edges=[("S0","S1","produces"),("S1","S2","causes"),("S1","S3","causes"),("S2","S4","supports"),("S3","S4","supports"),
        ("M1","S1","evidences"),("M2","S1","evidences"),("M3","S3","evidences"),
        ("C1","S1","evidences"),("C2","S2","evidences"),("C3","S2","evidences"),("C3","S3","evidences"),
        ("C4","S2","qualifies"),("C4","S3","qualifies"),("C3","C4","derives")],
)

# =====================================================================================
# SPEC 3: Scalable silicon nanoparticle anodes (Rare Metals 2017)
# =====================================================================================
SILICON = dict(
 file="silicon_anode_modality_graph.html", short="Scalable Si nanoparticle anode", journal="Rare Metals", year=2017,
 title="A scalable synthesis of silicon nanoparticles as high-performance anode material for lithium-ion batteries", doi="https://doi.org/10.1007/s12598-017-0936-3", figs={},
 lanes=[dict(key="micro", label="Microscopy: SEM, HRTEM", sub="foundation model in hand or candidate"),
        dict(key="diff", label="Diffraction: XRD", sub="foundation model candidate"),
        dict(key="classic", label="Classical tools", sub="collapsed to one node per state")],
 states=[
  dict(id="S0", stage="HYP", title="Hypothesis and design", head="Scalable wet milling plus centrifugation can bring Si below the ~150 nm fracture size, and removing the surface SiOx should raise capacity and first-cycle efficiency.",
       detail="Need: Si anodes offer high capacity but fracture on lithiation, and nano-Si routes do not scale. Design: commercial micrometre Si feedstock, wet bead milling with 0.3 mm YSZ beads in ethanol for up to 11 h at 1800 rpm, centrifugation at 11,000 rpm for 5 min, spray drying, then HF etching at 5 wt% for 30 min. Sweep: d50 = 628, 162, 126, 62 nm, and 62 nm as-received against HF-etched.", figs=[], source="s1 to s9, s6"),
  dict(id="S1", stage="STR", title="Size and phase state", head="Si nanoparticles with d50 = 62 nm and d99 = 147 nm, below the 150 nm fracture size, still single-phase fcc Si with broadened reflections from milling strain.",
       detail="Feature size (s10) rests on laser diffraction, the SEM count and the precedent that particles below ~150 nm do not fracture on lithiation (s16). Phase (s17) rests on XRD. No cycling-stability data test the fracture-size premise.", figs=[], source="s10, s16, s17"),
  dict(id="S2", stage="STR", title="Surface state", head="As-received particles carry a ~3 nm amorphous SiOx shell and Zr traces from the milling media. HF etching removes both.",
       detail="Composition claim s19, resolved by HRTEM and EDX. The EDX oxygen signal only partly supports the removal.", figs=[], source="s19"),
  dict(id="S3", stage="PRP", title="Size-effect property state", head="Smaller unetched particles give lower initial capacity and lower first-cycle efficiency (2980 to 1485 mAh/g, 82 to 55%), because they carry relatively more SiOx and far more surface area for SEI (16 to 198 m2/g).",
       detail="Property s22 with mechanism s27. Crystalline Li15Si4 formation is suppressed for d50 at or below 162 nm (s25), argued from a 0.45 V plateau and the self-limiting lithiation precedent (s26).", figs=[], source="s22, s27, s25, s26"),
  dict(id="S4", stage="PRF", title="Etching performance state", head="HF etching raises the 62 nm Si initial delithiation capacity from 1485 to 2801 mAh/g and first CE from 55.0 to 68.9%. The etched anode gives 2940/2801/2417 mAh/g at 0.01/0.05/0.10 C.",
       detail="Property s29, mechanism s32 (the SiOx shell slows Li+ and electron transport and consumes Li irreversibly), performance s33.", figs=[], source="s29, s32, s33"),
  dict(id="S5", stage="DSC", title="Conclusion", head="Scalable milling and centrifugation give 62 nm Si, and HF removal of SiOx makes it a high-capacity anode.",
       detail="The framing that small is good sits in tension with the paper's own size series, where smaller is worse until etched.", figs=[], source="s36"),
 ],
 nodes=[
  dict(id="M1", lane=0, row="S1", line=0, title="SEM, Figure 4", tech="SEM", figs=["F4"], panel="F4", head="Pristine Si is several-micrometre angular grains; milled Si is irregular platelets. A 150-particle SEM count gives 20 to 160 nm, mean ~80 nm, close to laser diffraction.", solves="Particle size and shape in the size state.", op="measure feature metric", verdict="shown",
       fm="SEM foundation model. Particle segmentation and a size histogram against the scale bar is the textbook task.", source="s13, s14"),
  dict(id="M2", lane=0, row="S1", line=1, audit=True, title="SEM audit, Figure 4", tech="SEM", figs=["F4"], panel="F4b", head="The platelets in the micrograph measure 0.3 to 0.7 um against the 2 um bar, inconsistent with the 20 to 160 nm histogram. Either the count came from another field or the bar is misreported. Nothing supports 'no agglomerates'.", solves="Qualifies the size state.", op="measure feature metric", verdict="contradicts", text_silent=True,
       fm="An SEM model size read against the scale bar is exactly this test, and the answer is a number.", source="s15"),
  dict(id="M3", lane=0, row="S2", line=0, title="HRTEM, Figure 5", tech="TEM", figs=["F5"], panel="F5", head="A ~3 nm amorphous rim on the as-received particle. The etched particle shows lattice fringes to the edge, with a ~1 nm disordered rim still visible.", solves="The surface state.", op="inspect local feature", verdict="shown",
       fm="TEM candidates (EM-DINO, EMCF). Shell-thickness measurement from a lattice-resolved edge, with the residual 1 nm rim as the hard case.", note="The residual rim means removal is partial, which the EDX oxygen also says.", source="s20"),
  dict(id="D1", lane=1, row="S1", line=2, title="XRD, Figure 3", tech="XRD", figs=["F3"], panel="F3", head="Nano-Si reflections are much weaker and broader than raw Si, with no extra phases.", solves="Phase in the size state: single fcc Si with lattice strain and reduced crystalline fraction.", op="recognize signature", verdict="shown",
       fm="XRD models (Dara for phase identification, XtalNet or DiffractGPT for structure) can confirm single-phase Si. Crystallite size from peak width is classical Scherrer.", source="s18, s17"),
  dict(id="C1", lane=2, row="S1", line=3, title="Laser PSD and BET, Fig 2, Table 1", tech="Laser diffraction, BET", figs=["F2"], panel="F2", head="d50 falls to 174 nm in 6 h, then plateaus near 126 nm by 11 h. Centrifugation narrows the PSD to a 0.1 um cut-off. BET rises from 16 to 198 m2/g as d50 falls to 62 nm.",
       detail="The milling-time trend (s11) was not opened and rests on caption and text. The PSD shift (s12) is shown in Figure 2. BET areas come from Table 1 (s28) and feed the surface-area mechanism in the size-effect state.",
       solves="Size in the size state and surface area in the size-effect state.", op="read trend, convert to quantity", verdict="shown",
       fm="No foundation model. Laser diffraction and BET are instrument outputs.", source="s11, s12, s28"),
  dict(id="C2", lane=2, row="S2", line=1, title="EDX, Figure 5", tech="EDS", figs=["F5"], panel="F5", head="Zr peaks (0.51 wt%) vanish after HF. Oxygen falls only from 6.42 to 4.55 wt%. Cu comes from the grid.", solves="The surface state.", op="assign features", verdict="partial", inner_audit="Oxygen largely persists after etching, so EDX does not support full SiOx removal. The text is silent on this.",
       fm="No foundation model. Line-library lookup and standardless quantification.", source="s21"),
  dict(id="C3", lane=2, row="S4", line=0, title="Electrochemistry, Figs 6 to 8", tech="Galvanostatic, CV", figs=["F6", "F7", "F8"], panel="F6, F7, F8", head="First-cycle curves rank delithiation capacity 628 > 162 > 126 > 62 nm. A 0.45 V Li15Si4 plateau is clean only for 628 nm. Rate curves at 0.01/0.05/0.10 C fall with rate. CV of as-received Si shows activation over cycles 1 to 3 and an extra anodic peak near 0.25 V.",
       detail="Capacity ranking by size (s23), the Li15Si4 plateau read (s24, partial: the 126 and 162 nm curves also flatten near 0.42 V), Table 2 for as-received against etched capacity and CE (s30), the CV activation and extra peak (s31), and the rate series (s34).",
       solves="The size-effect state and the etching performance state.", op="read trend, read characteristic point, recognize signature", verdict="shown",
       inner_audit="Every figure end point sits ~1.35x below the quoted delithiation capacity (for example 2050 against 2801 mAh/g). The constant factor suggests a different mass basis between figures and tables. Coulombic efficiency is unaffected. Text silent.",
       fm="No foundation model for charge-discharge curves at this scale. End points, plateaus and CV peaks are classical reads, and the 1.35x audit is a ratio.", source="s23, s24, s30, s31, s34, s35"),
 ],
 edges=[("S0","S1","produces"),("S1","S2","produces"),("S1","S3","causes"),("S2","S4","causes"),("S3","S4","supports"),("S4","S5","supports"),
        ("M1","S1","evidences"),("M2","S1","qualifies"),("M3","S2","evidences"),("D1","S1","evidences"),
        ("C1","S1","evidences"),("C1","S3","evidences"),("C2","S2","evidences"),("C3","S3","evidences"),("C3","S4","evidences")],
)

# =====================================================================================
# SPEC 4: Self-toughening ZrB2-SiC composites (Journal of Advanced Ceramics 2019)
# =====================================================================================
CERAMIC = dict(
 file="zrb2_sic_modality_graph.html", short="Self-toughening ZrB2-SiC composites", journal="Journal of Advanced Ceramics", year=2019,
 title="Fabrication and mechanical properties of self-toughening ZrB2-SiC composites from in-situ reaction", doi="https://doi.org/10.1007/s40145-019-0334-4", figs={},
 lanes=[dict(key="micro", label="Microscopy: SEM (BSE, fracture, crack)", sub="foundation model in hand"),
        dict(key="diff", label="Diffraction: XRD", sub="foundation model candidate"),
        dict(key="classic", label="Classical tools", sub="collapsed to one node per state")],
 states=[
  dict(id="S0", stage="HYP", title="Hypothesis and design", head="In-situ reaction of ZrSi2 + B4C + C with excess ZrSi2 should densify the composite and grow platelet ZrB2 for self-toughening.",
       detail="Need: ZrB2-SiC ultra-high-temperature ceramics densify poorly because of covalent bonding and have low fracture toughness. Design: Reaction (1), 2ZrSi2 + B4C + 3C = 2ZrB2 + 4SiC, with excess ZrSi2 at 0, 10, 15, 20, 25 vol% as a liquid-forming sintering additive (samples RZSZ-0 to RZSZ-25). Processing: high-energy ball milling with WC media, then reactive hot pressing at 1550 C, 30 min, 40 MPa in vacuum.", figs=[], source="c1 to c6, c5"),
  dict(id="S1", stage="STR", title="Phase state", head="Reaction (1) runs to completion: ZrB2 and SiC are the main phases, with WSi2 from WC milling debris, ZrC at 20 vol% excess and above, and residual ZrSi2.",
       detail="Phase identity c12 with the reaction-sequence mechanism c11: B4C is consumed preferentially by Reaction (1), so ZrC formed from ZrSi2 and WC survives at high ZrSi2 loading.", figs=[], source="c12, c11"),
  dict(id="S2", stage="STR", title="Microstructure state", head="Excess ZrSi2 raises relative density from 91.8 to 98.5% at 15 vol%, then slightly down. ZrB2 grows into interlocking platelets, most developed at 20 vol%, and SiC refines to nano size.",
       detail="Porosity c15, platelet shape c19 and SiC refinement c16, with mechanism c21: the exothermic reaction locally melts ZrSi2, and the liquid plus oxide impurities promote anisotropic ZrB2 growth and particle sliding. Premise c20: hexagonal ZrB2 grows fastest on the {010} and {110} faces.", figs=[], source="c15, c16, c19, c21, c20"),
  dict(id="S3", stage="PRP", title="Property and toughening state", head="Hardness, flexural strength and fracture toughness all peak at 20 vol% excess ZrSi2 (17.1 GPa, 655 MPa, 6.08 MPa m1/2). Interlocked platelets and SiC-rich regions toughen by pull-out, bridging, deflection and branching.",
       detail="Property c23 and mechanism c28, with mixed intergranular and transgranular fracture (c29) and the CTE-mismatch residual stress around SiC (c27) as a premise.", figs=[], source="c23, c28, c29, c27"),
  dict(id="S4", stage="DSC", title="Conclusion", head="Reactive hot pressing with 20 vol% excess ZrSi2 gives dense, self-toughened ZrB2-SiC with interlocking platelets and the best mechanical properties.",
       detail="Not covered in the packet: the RZSZ-25 degradation detail, the RZSZ-15 fracture surface in Figure 6, the toughening schematic in Figure 9, and the origin of the ZrO2 and WC impurities.", figs=[], source="c30"),
 ],
 nodes=[
  dict(id="M1", lane=0, row="S2", line=0, title="BSE SEM, Figure 5", tech="SEM (BSE)", figs=["F5"], panel="F5a to d", head="Grey elongated ZrB2 grains among black SiC, with white WSi2. An interlocking cluster and non-uniform ZrB2 size in RZSZ-20. Elongation is clear at the 1 um bar in (c) but weak at the 2 um bar in (a, b, d).", solves="Platelet shape in the microstructure state.", op="assess spatial distribution", verdict="partial",
       fm="SEM foundation model. Grain aspect ratio from BSE contrast across the series. The partial verdict makes this a good discrimination item: is anisotropy real or a magnification effect?", source="c17"),
  dict(id="M2", lane=0, row="S2", line=1, title="Fracture-surface SEM, Figure 8", tech="SEM", figs=["F8"], panel="F8", head="RZSZ-0 shows open pores and submicron SiC; RZSZ-10 and 15 tiny pores and nano-sized SiC; RZSZ-20 a dense cluster of interlocked ZrB2 platelets; RZSZ-25 coarse ZrB2 with secondary phases.", solves="Porosity, SiC refinement and platelet interlocking in the microstructure state, and the fracture mode in the property state.", op="compare across conditions", verdict="shown",
       fm="SEM foundation model. Pore fraction and grain size per sample, then the trend across five loadings.", source="c14, c18"),
  dict(id="M3", lane=0, row="S3", line=0, title="Indentation crack SEM, Figure 8", tech="SEM", figs=["F8"], panel="F8", head="An indentation crack in RZSZ-20 shows deflection, bridging, grain pull-out and branching into a SiC-rich region.", solves="The toughening mechanism in the property state.", op="inspect local feature", verdict="shown",
       fm="SEM foundation model. Crack-path segmentation and event counting (deflections, bridges, pull-outs) along the crack.", note="Figure 6 (RZSZ-15 fracture surface) and Figure 9 (toughening schematic) were not opened.", source="c26"),
  dict(id="D1", lane=1, row="S1", line=0, title="XRD, Figures 1 and 2", tech="XRD", figs=["F1", "F2"], panel="F1, F2a to d", head="RZSZ-0: ZrSi2 and B4C reflections vanish, ZrB2 and SiC dominate, new WSi2 and trace ZrO2. Across the series the WSi2 peak grows with excess ZrSi2, ZrC reflections appear, and weak residual ZrSi2 remains.", solves="The phase state.", op="assign features, recognize signature", verdict="partial",
       inner_audit="ZrC markers are labelled only on RZSZ-25. On RZSZ-20 the ~38.5 degree ZrC (200) peak is barely above noise, so 'at 20 vol% and above' is shown only for 25.",
       fm="XRD phase-identification models (Dara, multi-hypothesis) can put a number on the ZrC-at-20 claim. Peak assignment itself is a library match.", source="c7, c8"),
  dict(id="C1", lane=2, row="S1", line=1, title="EDS, Figure 5", tech="EDS", figs=["F5"], panel="F5 zones A, B", head="Zone A: W 21.4 and Si 59.5 at%, a WSi2 grain. Zone B: a SiC-rich region.", solves="Secondary-phase identity in the phase state.", op="convert to quantity", verdict="shown",
       inner_audit="Zone B reads C 58.9 at% against Si 34.5, far beyond SiC stoichiometry. Light-element EDS quantification is unreliable, and the text is silent.",
       fm="No foundation model. Standardless quantification with its known light-element limits.", source="c9"),
  dict(id="C2", lane=2, row="S1", line=2, title="Thermodynamics, Figure 3", tech="Computed dG(T)", figs=["F3"], panel="F3", head="Computed dG(T): Reactions (1) to (3) are all negative. Reaction (1) sits near -500 kJ/mol, far below (2) near -85 and (3).", solves="The reaction-sequence mechanism in the phase state.", op="read trend", verdict="shown",
       note="dG is per mole of reaction as written. The reactions have different stoichiometries, and a dG ranking says nothing about kinetics.",
       fm="No model. Thermochemical tables.", source="c10, c11"),
  dict(id="C3", lane=2, row="S2", line=2, title="Density and mechanics, Figs 4, 7", tech="Archimedes, indentation, bending, SEVNB", figs=["F4", "F7"], panel="F4, F7", head="Relative density 91.8, 94.9, 98.5 (RZSZ-15), 97.6, 96.4%. Hardness, strength and KIC rise to maxima at RZSZ-20 (17.1 GPa, 655 MPa, 6.08 MPa m1/2), then fall.", solves="Porosity in the microstructure state and the property state.", op="read trend", verdict="shown",
       inner_audit="The density optimum (RZSZ-15) and the property optimum (RZSZ-20) do not coincide, so densification alone cannot set the property optimum. This is a derived cross-check of Figures 4 and 7.",
       fm="No foundation model. Instrument outputs and a two-figure comparison.", source="c13, c22, c24, c25"),
 ],
 edges=[("S0","S1","produces"),("S1","S2","produces"),("S2","S3","causes"),("S3","S4","supports"),
        ("M1","S2","evidences"),("M2","S2","evidences"),("M2","S3","evidences"),("M3","S3","evidences"),
        ("D1","S1","evidences"),("C1","S1","evidences"),("C2","S1","evidences"),("C3","S2","evidences"),("C3","S3","evidences")],
)

SPECS = {"nico": NICO, "photo": PHOTO, "silicon": SILICON, "ceramic": CERAMIC}
NECESSITY = {'nico': {'M1': ('necessary', 'Only figure evidence for cage size and roughness, but the structure state is off the path to the conclusion. The composition line never touches morphology.'), 'M2': ('necessary', 'Only evidence for hollowness. Feeds the architecture branch alone, whose hollow-versus-solid data are text only.'), 'M3': ('corrective', 'Dormant. Activity is per geometric area with no ECSA, so debris could change the intrinsic-activity claim. The paper never makes that link.'), 'M4': ('decorative', 'Text only. Stability stands on the CA and CP curves.'), 'A1': ('necessary', "Only support for the reactivity state, and the conclusion's 'because' clause cannot be stated without it."), 'A2': ('corrective', 'Shows the necessary DFT link is a four-point rank match, so it is necessary but not sufficient.'), 'C1': ('necessary', 'Composition and valence carry the whole composition line.'), 'C2': ('necessary', 'All headline numbers live here.')}, 'photo': {'M1': ('redundant', 'The optical images at 0% strain show the same arch, and this read is partial.'), 'M2': ('decorative', 'Uniform dispersion feeds nothing. Sensitization needs QDs present, which absorption and EDS show.'), 'M3': ('necessary', 'Only support for the arch-unfolding mechanism. The performance numbers stand on electrical data regardless. Generic vision, not SEM or TEM.'), 'C1': ('necessary', 'Confirms PbS is present.'), 'C2': ('necessary', 'Carries the sensitization and charge-transfer mechanisms.'), 'C3': ('necessary', 'Carries both property and performance states.'), 'C4': ('corrective', 'Ten-fold gap between single-wire and array ON/OFF that the text does not acknowledge.')}, 'silicon': {'M1': ('redundant', 'Laser diffraction alone gives d50 = 62 nm.'), 'M2': ('corrective', 'Puts the 62 nm claim itself in doubt, and that claim is the premise of the fracture-size argument.'), 'M3': ('necessary', 'Only strong evidence for the shell and its removal. EDX oxygen barely drops.'), 'D1': ('decorative', 'No downstream node uses single-phase Si.'), 'C1': ('necessary', 'Size series and BET carry the size-effect state.'), 'C2': ('redundant', 'HRTEM carries the surface state. EDX adds the Zr removal and the oxygen caveat.'), 'C3': ('necessary', 'All capacity and CE numbers live here.')}, 'ceramic': {'M1': ('necessary', 'No non-SEM evidence for platelet shape, and the toughening mechanism runs through it. Partial read, so it needs M2.'), 'M2': ('necessary', 'Only evidence for platelet interlocking and SiC refinement. Porosity alone is redundant with the density curve.'), 'M3': ('necessary', 'Only evidence for the toughening events. Property values stand on the mechanical tests without it.'), 'D1': ('necessary', 'Only evidence that the in situ reaction ran to completion. EDS confirms one grain.'), 'C1': ('redundant', 'XRD carries the phase state. EDS confirms WSi2 and adds the light-element caveat.'), 'C2': ('decorative', 'Ranks driving forces but the phase state stands on XRD.'), 'C3': ('necessary', 'Density and property values. Its cross-check makes the SEM platelet story more necessary.')}}
for k, spec in SPECS.items():
    for n in spec["nodes"]:
        if n["id"] in NECESSITY[k]:
            n["necessity"], n["necessity_reason"] = NECESSITY[k][n["id"]]


# =====================================================================================
# layout + render
# =====================================================================================
def build(spec):
    STATE_X, STATE_W, STATE_H = 250, 340, 104
    LANE_W, LANE_H = 280, 94
    LANE_X = [665 + i*320 for i in range(len(spec["lanes"]))]
    LINE_H, STAGE_H, TOP = 108, 30, 60
    BUS = STATE_X + STATE_W/2 + 30
    BUS_A = BUS + 12
    W = LANE_X[-1] + LANE_W/2 + 24
    pos, bands = {}, []
    y = TOP
    for s in spec["states"]:
        here = [n for n in spec["nodes"] if n["row"] == s["id"]]
        lines = max(1, max([n["line"] for n in here], default=-1) + 1)
        bands.append({"id": s["id"], "label": s["title"], "y0": y, "y1": y + STAGE_H + lines*LINE_H})
        y += STAGE_H
        pos[s["id"]] = dict(x=STATE_X, y=y + lines*LINE_H/2, w=STATE_W, h=STATE_H)
        for n in here:
            pos[n["id"]] = dict(x=LANE_X[n["lane"]], y=y + n["line"]*LINE_H + LINE_H/2, w=LANE_W, h=LANE_H)
        y += lines*LINE_H
    H = y + 24
    def box(nid):
        p = pos[nid]; return p["x"]-p["w"]/2, p["y"]-p["h"]/2, p["x"]+p["w"]/2, p["y"]+p["h"]/2
    order = [s["id"] for s in spec["states"]]
    skip_busy = []
    def skip_lane(y0, y1):
        for k in range(4):
            if all(not (l == k and not (y1 < a-6 or y0 > b+6)) for (l, a, b) in skip_busy):
                skip_busy.append((k, y0, y1)); return k
        skip_busy.append((3, y0, y1)); return 3
    routed = []
    for s, d, rel in spec["edges"]:
        ps, pd = pos[s], pos[d]
        sx0, sy0, sx1, sy1 = box(s); dx0, dy0, dx1, dy1 = box(d)
        if s in order and d in order:
            if order.index(d) == order.index(s) + 1:
                pts = [(ps["x"], sy1), (pd["x"], dy0)]
            else:
                k = skip_lane(ps["y"], pd["y"]); sx = STATE_X - STATE_W/2 - 26 - 14*k
                pts = [(sx0, ps["y"]), (sx, ps["y"]), (sx, pd["y"]), (dx0, pd["y"])]
            kind = "spine"
        elif d in order:
            bx = BUS_A if rel == "qualifies" else BUS
            pts = [(sx0, ps["y"]), (bx, ps["y"]), (bx, pd["y"]), (dx1, pd["y"])] if abs(ps["y"]-pd["y"]) > 1 else [(sx0, ps["y"]), (dx1, pd["y"])]
            kind = "audit" if rel == "qualifies" else "evidence"
        else:
            if abs(ps["x"]-pd["x"]) < 1:
                pts = [(ps["x"], sy1), (pd["x"], dy0)] if pd["y"] > ps["y"] else [(ps["x"], sy0), (pd["x"], dy1)]
            else:
                pts = [(ps["x"], sy0 if pd["y"] < ps["y"] else sy1), (ps["x"], pd["y"]), (dx1 if pd["x"] < ps["x"] else dx0, pd["y"])]
            kind = "derive"
        routed.append(dict(src=s, dst=d, rel=rel, kind=kind, pts=pts))
    nodes_out = [{**s, "kind": "state", **pos[s["id"]]} for s in spec["states"]]
    for n in spec["nodes"]:
        kind = "classic" if spec["lanes"][n["lane"]]["key"] == "classic" else "fm"
        nodes_out.append({**n, "kind": kind, **pos[n["id"]]})
    lanes = [dict(x=LANE_X[i], label=l["label"], sub=l["sub"], var=LANE_VARS[l["key"]]) for i, l in enumerate(spec["lanes"])]
    n_fm = sum(1 for l in spec["lanes"] if l["key"] != "classic")
    payload = dict(title=spec["title"], journal=spec["journal"], year=spec["year"], doi=spec["doi"], W=W, H=H, bands=bands, lanes=lanes,
                   state_x=STATE_X, nodes=nodes_out, edges=routed, figs=spec["figs"], n_fm=n_fm,
                   panels=spec.get("panels", {}),
                   figs_note=("" if (spec["figs"] or spec.get("panels")) else "Figures for this paper are not in the repo, so the panel shows evidence text without thumbnails."))
    spec["kit_version"] = KIT_VERSION
    out = f"{OUTDIR}/{spec['file']}"
    open(out, "w", encoding="utf-8").write(PAGE.replace("__DATA__", json.dumps(payload).replace("</", "<\\/")).replace("__TITLE__", spec["short"]))
    print("wrote", out, "canvas", W, "x", H)
    return out

PAGE = open(__file__.rsplit("/",1)[0] + "/page_template.html", encoding="utf-8").read()

if __name__ == "__main__":
    import glob, os
    args = sys.argv[1:]
    if args and args[0] == "--specs":
        # render every JSON spec in a directory (machine output)
        for f in sorted(glob.glob(os.path.join(args[1], "*.json"))):
            spec = json.load(open(f, encoding="utf-8")); spec.setdefault("figs", {})
            build(spec)
    elif args and args[0] == "--export":
        os.makedirs(args[1], exist_ok=True)
        for k, spec in SPECS.items():
            out = {kk: vv for kk, vv in spec.items() if kk != "figs"}; out["figs"] = {}
            json.dump(out, open(os.path.join(args[1], f"{k}_spec.json"), "w", encoding="utf-8"), indent=1)
            print("exported", k)
    else:
        for k in (args or list(SPECS)):
            build(SPECS[k])
