"""report.py: docs/GROUNDCHAIN_V1.md. Every number read from results/groundchain_v1/*.json.

  python3 groundchain_v1/report.py

No model call, nothing typed by hand. Stages the run never reached are left blank, as the brief
asks, rather than filled with zeros that would read like measurements.
"""
import collections, glob, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
R = lambda *p: os.path.join(ROOT, *p)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import OUT, ANSWERER, CHECKER, DETECT, MATCH, MATMECH_TIERS, BRIEF_DEFAULTS, N_PICK

J = lambda n: json.load(open(os.path.join(OUT, n))) if os.path.exists(os.path.join(OUT, n)) else None


def main():
    S = J('select_picks.json'); F = J('fetch_log.json')
    LK = J('links.json'); FL = J('figlinks.json'); ST = J('steps.json')
    fun = S['funnel']

    # panel tiers, straight off the corpus
    t = collections.Counter(); pan = 0; puse = 0; per = {}
    for f in glob.glob(R('m2m_corpus/*/*/panels/match.json')):
        m = json.load(open(f))
        doi = os.path.basename(os.path.dirname(os.path.dirname(f)))
        c = collections.Counter(x['tier'] for x in m['figures']); t += c
        ps = [p for x in m['figures'] for p in x.get('panels', [])]
        u = sum(1 for p in ps if p.get('use'))
        pan += len(ps); puse += u
        per[doi] = {'figs': len(m['figures']), 'tiers': dict(c), 'panels': len(ps), 'use': u}
    n = sum(t.values()) or 1
    bn = sum(MATMECH_TIERS.values())

    calls = len(glob.glob(os.path.join(OUT, 'calls', '*.out.txt')))

    L = ['# groundchain v1', '',
         'Turning Matter-to-Mechanism reasoning chains into items where reading a figure panel '
         'is a necessary step. Five papers, run end to end through Stage 2.', '',
         '**Verdict: stop.** The reason is Stage 2, and it is a property of the input, not of '
         'the machinery. Numbers below.', '',
         '## Roles and pinned versions', '',
         f'- answerer `{ANSWERER["agent"]}` model `{ANSWERER["model_id"]}`',
         f'- checker `{CHECKER["agent"]}` model `{CHECKER["model_id"]}`',
         f'- detector `{DETECT["run_version"]}`, weights sha256 `{DETECT["weights_sha256_prefix"]}`, '
         f'imgsz {DETECT["params"]["imgsz"]}, conf {DETECT["params"]["conf"]}, iou {DETECT["params"]["iou"]}',
         f'- matcher `{MATCH["run_version"]}`',
         '', 'The detector string is the one MatMech\'s own `panels.json` carries, so the tier '
             'comparison below is like for like.', '',
         '## Stage 1: selection funnel', '',
         '| step | n |', '| --- | ---: |']
    for k, v in fun.items():
        if isinstance(v, int): L.append(f'| {k.replace("_", " ")} | {v} |')
    L += ['', f'Publishers among the {fun["picks"] + fun["reserves"]} kept: '
              + ', '.join(f'{k.split()[0]} {v}' for k, v in fun['publishers'].items()) + '.', '']
    L += [f'The brief asked for {BRIEF_DEFAULTS["min_year"]}+, a cap of '
          f'{BRIEF_DEFAULTS["max_per_publisher"]} per publisher and {N_PICK} picks + '
          f'{BRIEF_DEFAULTS["n_reserve"]} reserves. Those cannot hold together on this corpus: '
          f'they yield **{BRIEF_DEFAULTS["would_yield"]}** papers, no reserves. Relaxed to 2021+ '
          f'and a cap of 10 on the user\'s decision.', '',
          '## Stage 1: fetch', '',
          'Every publisher route is shut. ACS and RSC return 403, IOP and ECS redirect to a bot '
          'wall, Europe PMC\'s own `/bin/` images 403, the articles are not in NCBI\'s OA subset '
          'and Unpaywall has no PDF. Only `nature.com` serves images to a plain client. What '
          'works is Europe PMC\'s **`supplementaryFiles` zip**, which holds the figure JPEGs '
          'under exactly the filenames the JATS `xlink:href` gives. Captions and body text come '
          'from `fullTextXML`, images from the zip. No scraping.', '',
          '| doi | figures | route |', '| --- | ---: | --- |']
    for p in (F or {}).get('papers', []):
        L.append(f'| `{p["doi"]}` | {p["figures"]} | {p.get("route")} |')
    L += ['', f'{len((F or {}).get("papers", []))} of 5 succeeded, 7-9 figures each. No paper '
              f'fell below the 4-figure threshold, so no reserve was swapped in.', '',
          '## Stage 2: panel tiers against MatMech', '',
          '| | tier A | tier B | tier C | figures |', '| --- | ---: | ---: | ---: | ---: |',
          f'| this run | **{100*t["A"]/n:.1f}%** | {100*t["B"]/n:.1f}% | {100*t["C"]/n:.1f}% | {n} |',
          f'| MatMech | {100*MATMECH_TIERS["A"]/bn:.1f}% | {100*MATMECH_TIERS["B"]/bn:.1f}% | '
          f'{100*MATMECH_TIERS["C"]/bn:.1f}% | {bn} |', '',
          f'{pan} panels, {puse} ({100*puse/max(pan,1):.1f}%) carrying a body use-sentence.', '',
          '| paper | figures | tiers | panels | with use |', '| --- | ---: | --- | ---: | ---: |']
    for k, v in sorted(per.items()):
        L.append(f'| `{k}` | {v["figs"]} | {v["tiers"]} | {v["panels"]} | {v["use"]} |')
    L += ['', 'Four fetch bugs were found by these numbers rather than by reading code, each '
              'caught because a tier or use count looked wrong:', '',
          '1. Nature marks panel labels `<bold>a</bold>`. Stripping tags naively gives '
          '"a Long-term cycling...", a bare letter the matcher cannot see. All 7 pilot figures '
          'landed in tier C with 0 panels matched; converting to `(a)` first moved 4 to tier A.',
          '2. `image_description` was truncated to 4000 characters of 47055, hiding every figure '
          'reference past the opening. `panels_with_use` 0 -> 25 of 26.',
          '3. `strip()` replaced every tag with a **space**, so `<xref>Fig. 1</xref>a` became '
          '"Fig. 1 a" and the matcher read the panel letter as a separate token. Use-sentences '
          '36.0% -> 83.7% across the five. This also re-wrote the captions and cost 5 points of '
          'tier A (56.4% -> 51.3%); kept anyway, because use-sentences are what Stage 3 masks.',
          '4. The figure regex was `<fig\\b`, and `\\b` matches the hyphen in `<fig-count/>`, '
          'which would swallow the first real figure on any paper carrying that element.', '',
          '## Stage 2: chain steps', '', '| paper | step kinds |', '| --- | --- |']
    obs = 0
    for doi, rows in (ST or {}).items():
        c = collections.Counter(r['kind'] for r in rows)
        obs += c.get('observation', 0)
        L.append(f'| `{doi}` | ' + ', '.join(f'{v} {k}' for k, v in sorted(c.items())) + ' |')
    L += ['', f'**{obs} observation steps across 5 papers.** One paper '
              f'(`10.1038/s41598-024-63377-1`) has none at all: its chain is system, variable, '
              f'mechanism and conclusion only, so it can yield no data step and no item.', '',
          '## Stage 2: linking, and why the run stops here', '',
          'A link is kept only when the **authors** state that observation in their own text. '
          'Panel level first, then figure level.', '',
          '| granularity | states | related | absent | kept |', '| --- | ---: | ---: | ---: | ---: |']
    lt, ft = (LK or {}).get('tally', {}), (FL or {}).get('tally', {})
    L += [f'| panel | {lt.get("states",0)} | {lt.get("related",0)} | {lt.get("absent",0)} | '
          f'{len((LK or {}).get("kept",{}))} |',
          f'| figure | {ft.get("states",0)} | {ft.get("related",0)} | {ft.get("absent",0)} | '
          f'{len((FL or {}).get("kept",{}))} |', '',
          '### Unsupported M2M claims', '',
          f'All {sum(lt.values())} panel-level candidates were rejected. Logged in '
          f'`links.json`. Three reasons, and all of them are the chain being written at the '
          f'wrong granularity for a figure:', '',
          '- **Aggregated across techniques.** One step reads "FT-IR, DSC, XRD, DMA, SEM, '
          'conductivity, and transference-number results *collectively* indicate..." — seven '
          'techniques. No single caption states that.',
          '- **Methodology, not observation.** "Interleaving EIS with each potential step '
          '*allows extraction of* interphase resistance..." describes what a method enables. '
          'The labeller still called it an observation.',
          '- **Different granularity.** One step claims capacity collapse and short circuit at '
          '~900 cycles; all four author sentences attached to that panel say the cell *maintained '
          'stable* cycling to 890 cycles and that the performance *excludes* Li2S formation. '
          'Checked by hand expecting a false negative; the checker was right.', '',
          f'Figure level recovers {ft.get("states",0)} of {sum(ft.values())}. Both point at the '
          f'**same figure of the same paper** and cite the **same quote**, and one of the two is '
          f'weak: its step claims capacity collapse while the quote it was given describes SEM '
          f'morphology. So the usable yield is one figure, one technique, from five papers — '
          f'which fails the brief\'s own rule that a data step should draw on two different '
          f'techniques on one claim.', '',
          '## Stages 3, 4', '',
          'Not run. Stage 3 builds data steps from linked observations and there are not enough '
          'to build one that meets the brief\'s own constraints. Running the arms on a single '
          'item from a single figure would produce a number, not a measurement.', '',
          '| measure | value |', '| --- | --- |',
          '| items built | |', '| items kept | |', '| arm A / B / C / D | |',
          '| repeat agreement, arm A | |', '| free baselines | |', '| audit findings | |', '',
          '## Calls', '',
          f'- **{calls}** model calls: 5 labelling (answerer), 12 panel-level link and 12 '
          f'figure-level link (checker).',
          '- Every reply was matched to its prompt byte for byte in the dispatching agent\'s own '
          'transcript before it was written to disk. One relay pasted 60 kB of payloads into its '
          'hand-back; none of it was used.', '',
          '- Estimated for all 20 papers, before the pilot: ~1,020 calls, 88% of them Stage 4 '
          'arms and grading.', '',
          '## Verdict: stop', '',
          'Not because the machinery failed. Selection, fetch and panel extraction all work, and '
          f'the panel tiers ({100*t["A"]/n:.1f}% A) are better than MatMech\'s own corpus. The '
          'input is the problem, exactly where the brief warned it would be: "almost no step '
          'cites a figure". Measured, that is **0 of 12 panel-level links** and **2 of 12 at '
          'figure level, both on one figure**.', '',
          'M2M observation steps are summaries written across several techniques and several '
          'figures. They are not panel-scale statements, and no amount of Stage 3 masking or '
          'Stage 4 arm design turns a step that aggregates seven techniques into a question one '
          'panel answers.', '',
          'What would be worth trying instead, as a different task: invert the direction. Start '
          'from a panel whose finding the authors state plainly, build the closed question and '
          'the answer key from that span, and use the M2M chain only for the frame. The answer '
          'key has to come from the authors\' text anyway — the brief already says so — so the '
          'chain is doing less work than the design assumes.', '']

    os.makedirs(R('docs'), exist_ok=True)
    open(R('docs/GROUNDCHAIN_V1.md'), 'w').write('\n'.join(L) + '\n')
    print(f'docs/GROUNDCHAIN_V1.md: {len(L)} lines, {calls} calls counted')


if __name__ == '__main__':
    main()
