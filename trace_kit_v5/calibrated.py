"""calibrated.py: the hand-written keys the v5 brief specifies, item by item.

These override any model-drafted key. Everything else in v5 is drafted by a model and marked as a
draft (brief item 10: automated critique fields are drafts, not gold). At five papers the combining
propositions were hand-written; at thirty-two they cannot be, so the distinction between a
hand-calibrated key and a drafted one is recorded on every item and shown on every page.

The calibration principle, brief item 1: **a key states only the inference the evidence permits.**
Where two causes cannot be separated, that is the key, and "not identifiable" is a scorable answer
rather than a failure to answer.

Every verdict is model against model.
"""

# causal strength, weakest to strongest
STRENGTH = ['descriptive', 'associative', 'conditional mechanism', 'discriminating']

# quantity kinds that must be named rather than left implicit (brief item 6)
QUANTITY = ['rate', 'amount', 'cumulative', 'normalized']

HAND = {

 # ---- Acta Materialia, split into two items (brief item 5): depth counts derived conclusions,
 # and the density-yield covariation and the [0001] loading comparison are two conclusions.
 'acta_density_yield': {
   'paper': 'Acta_Materialia__10.1016_j.actamat.2021.116797', 'from_step': 2,
   'question': 'Across the three heat treatments, does the yield stress measured here move with the '
               'nanoplate number density from step 1? Give the comparison.',
   'quantity': {'kind': 'amount', 'what': 'nanoplate number density, per um; yield stress, MPa'},
   'key': 'Yield stress and nanoplate number density move together across the three heat '
          'treatments: 167 -> 113 -> 160 MPa against 9.8 -> 0.3 -> 9.0 per um, both dipping after '
          'the 520 C anneal and recovering after the further 400 C anneal. This is consistent with '
          'a strengthening contribution from the nanoplates.',
   'limits': ['Nanoplate THICKNESS moves the opposite way, 28 -> 84 -> 14 nm, so the two plate '
              'descriptors do not covary with each other and the comparison does not isolate which '
              'of them, if either, carries the strength.',
              'Three points, and the heat treatments differ in more than plate density, so a '
              'contribution is the most the data supports -- not that density is the cause.'],
   'permitted': 'consistent with a strengthening contribution from the nanoplates',
   'not_permitted': 'that nanoplate density causes the yield stress, or that the effect is '
                    'quantitatively attributable to density',
   'labels': {'dependency': 'real', 'inference_validity': 'follows, weakly',
              'causal_strength': 'associative'},
 },

 'acta_loading_asymmetry': {
   'paper': 'Acta_Materialia__10.1016_j.actamat.2021.116797', 'from_step': 3,
   'question': 'Compare the stress at which this evidence shows deformation along [0001] with the '
               'stress step 2 reported for that same orientation. Report both and say what the '
               'comparison implies about the deformation route.',
   'quantity': {'kind': 'amount', 'what': 'compressive fracture stress and tensile flow stress, MPa'},
   'key': 'The [0001] orientation fractures in compression at ~355 MPa without yielding, and flows '
          'in tension at ~72 MPa (serrated ~52-80) to ~45% plastic strain. The two numbers are a '
          'fracture stress and a flow stress, not two yield stresses, so they are not a yield '
          'ratio; what they show is that the orientation has a deformation route available in '
          'tension that is absent in compression, and the kink bands in F10b are what identifies '
          'it.',
   'limits': ['A fracture stress and a flow stress are different quantities; dividing them gives a '
              'number with no mechanical meaning.',
              'Whether kinking is also available in compression and merely pre-empted by fracture '
              'is not established here.'],
   'permitted': 'that a deformation route exists in tension which compression does not reach',
   'not_permitted': 'a yield-stress ratio, or a strength comparison between the two senses',
   'labels': {'dependency': 'real', 'inference_validity': 'follows',
              'causal_strength': 'discriminating'},
 },

 # ---- Biomaterials, branched (brief item 8) into a cobalt/biology item and an antibiotic item.
 'biomat_texture_inventory': {
   'paper': 'Biomaterials__j.biomaterials.2011.11.042', 'from_step': 2,
   'question': 'Order the three scaffolds by the cobalt released here and compare that order with '
               'the pore structure from step 1. What can be concluded about what sets the release?',
   'quantity': {'kind': 'cumulative', 'what': 'Co2+ in medium, mg/L, cumulative to the stated day; '
                                              'surface area m2/g and pore volume cm3/g'},
   'key': 'Release rises as surface area and pore volume fall -- 0 -> 16.9 -> 20.8 mg/L at 7 days '
          'against 290 -> 180 -> 127 m2/g -- so a texture-driven mechanism predicts the opposite '
          'order and is ruled out in that direction. It does NOT follow that cobalt content sets '
          'the release: **cobalt inventory and texture cannot be separated here**, because adding '
          'cobalt both lowers the texture and raises the inventory. The identifiable answer is that '
          'the two candidate causes are confounded by construction.',
   'limits': ['Three scaffolds, one varying composition: inventory and texture are collinear.',
              'Ruling out a direction is not ruling out a cause.'],
   'permitted': 'that texture does not act in the direction a texture mechanism predicts, and that '
                'inventory and texture are not separable in this series',
   'not_permitted': 'that cobalt content is the cause of the release rate',
   'labels': {'dependency': 'real', 'inference_validity': 'follows',
              'causal_strength': 'conditional mechanism'},
   'not_identifiable': 'which of cobalt inventory or mesoporous texture sets the release',
 },

 'biomat_dose_response': {
   'paper': 'Biomaterials__j.biomaterials.2011.11.042', 'from_step': 2,
   'question': 'Do the HIF-1alpha and VEGF results describe one dose response in cobalt content?',
   'quantity': {'kind': 'normalized', 'what': 'HIF-1alpha band intensity relative to the '
                                              'alpha-tubulin loading control; VEGF secretion at day 7'},
   'key': 'They do not. HIF-1alpha rises with cobalt, strongest for 5Co. VEGF is raised by 2Co and '
          'not by 5Co. A single monotonic dose response in cobalt cannot produce both, so the two '
          'readouts do not describe one dose response.',
   'limits': ['The HIF-1alpha comparison is a band intensity against a loading control, not a '
              'calibrated concentration.',
              'Non-monotonic VEGF may reflect cytotoxicity at 5Co, which is not measured here.'],
   'permitted': 'that the two readouts diverge and no single dose response covers both',
   'not_permitted': 'a HIF-1alpha -> VEGF pathway claim; nothing here shows one drives the other',
   'labels': {'dependency': 'real', 'inference_validity': 'follows',
              'causal_strength': 'discriminating'},
 },

 'biomat_antibiotic': {
   'paper': 'Biomaterials__j.biomaterials.2011.11.042', 'from_step': 3,
   'question': 'Does the ampicillin release profile account for the bacterial survival over 7 days?',
   'quantity': {'kind': 'cumulative', 'what': 'cumulative ampicillin released, ug; relative survival, '
                                              'percent of blank'},
   'key': 'Release is cumulative and plateaus near 795 ug by 72 h, while survival keeps falling to '
          '~52% at day 7. The drug is already delivered before most of the kill occurs, so the '
          'survival trend is not tracking the release rate over days 3-7.',
   'limits': ['Cumulative release and instantaneous survival are different quantity kinds and '
              'should not be read as a rate against a rate.',
              'Local concentration at the bacteria is not measured.'],
   'permitted': 'that the kill continues after release has plateaued',
   'not_permitted': 'that release rate drives survival',
   'labels': {'dependency': 'none', 'inference_validity': 'follows',
              'causal_strength': 'descriptive'},
 },

 # ---- Advanced Functional Materials: define the quantity (brief item 6)
 'afm_domain_emission': {
   'paper': 'Advanced_Functional_Materials__10.1002_adfm.202008088', 'from_step': 2,
   'question': 'Rank the three samples by emission complexity below 150 K, and compare that ranking '
               'with the domain sizes from step 1.',
   'quantity': {'kind': 'descriptive ordinal',
                'what': 'emission complexity = the number of resolved emission bands below 150 K, '
                        'counting a distinct IR tail as an additional feature; window 0-150 K, '
                        'excitation 50-370 uW at 80 K'},
   'key': 'The orderings correspond inversely across the same three samples: ~0.1 um PC shows two '
          'bands plus an IR tail, 1e2-1e3 um SC shows one band, HOC lies between on both axes.',
   'limits': ['Three samples made by three different growth routes, so domain size is confounded '
              'with synthesis route.',
              'Emission complexity is an ordinal count, not a continuous measure, so "inversely '
              'ranks" is the strongest form available -- no slope can be fitted.'],
   'permitted': 'an inverse rank correspondence across three samples',
   'not_permitted': 'that domain size causes the emission structure',
   'labels': {'dependency': 'real', 'inference_validity': 'follows, weakly',
              'causal_strength': 'associative'},
 },

 # ---- Rare Metals: tables in scope (brief item 7)
 'raremetals_strength': {
   'paper': 'Rare_Metals__s12598-012-0515-6', 'from_step': 2,
   'question': 'Compare the tensile strengths of the three alloys with the precipitate structure '
               'from step 1.',
   'quantity': {'kind': 'amount', 'what': 'ultimate tensile strength, MPa, from Table 3'},
   'key': 'Tensile strength rises 311 -> 376 -> 406 MPa across RE-free, Sm and La, in the same order '
          'as the refinement and number density of the theta-prime precipitates from step 1.',
   'limits': ['The three alloys differ in copper content as well as in rare-earth addition, so the '
              'strength ordering is confounded with Cu.',
              'Three alloys, one point each: an ordering, not a relationship.'],
   'permitted': 'that strength orders with precipitate refinement, confounded with Cu content',
   'not_permitted': 'that RE addition raises strength through precipitate refinement',
   'labels': {'dependency': 'real', 'inference_validity': 'follows, weakly',
              'causal_strength': 'associative'},
   'source_note': 'uses Table 3, not a figure panel',
 },
}
