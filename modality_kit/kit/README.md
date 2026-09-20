# Modality graph kit

- `build_all.py`: renderer. `python3 build_all.py --specs specs/` renders every JSON spec in the folder to `/mnt/user-data/outputs/<file>`. Edit OUTDIR at the top for another location. `python3 build_all.py` rebuilds the four built-in examples.
- `page_template.html`: the HTML template the renderer fills. Self-contained output, no external scripts, Google Fonts with a system fallback.
- `specs/`: the four worked examples in the schema the prompt asks the agent to produce. `nico_spec.json` renders without figures here; the built-in example embeds them.
- Requires Python 3 only. No packages.

## Panel verification fields (optional, per lane node)
- `panel_ids`: canonical ids from the panel store, e.g. `10.1002/aenm.201401880#F2a`.
- `panel_check`: `{"status": "verified|partial|unverified", "id_exists": bool, "tier": "A|B|C", "ocr_agrees": bool, "modality_agrees": bool, "judge_opened": bool, "human": "correct|wrong|null"}`.
  `verified` requires id_exists, tier A or B, ocr_agrees, modality_agrees and judge_opened all true. `partial` when the chain is incomplete but nothing failed. Any failure gives `unverified`.
  The renderer prints the status at the node corner and the full chain in the panel.
