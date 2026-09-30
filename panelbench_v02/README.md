# PanelBench v0.2 (MinerU extraction), for review

Branch for review; do not merge. Start with `V02_REPORT.md`, then `NEW_ITEMS.md`. Command log: `LOG.md`.

Left out of this public repository on purpose:
- PDFs, all panel crops (`work/panelbench_v02/tasks-*/*/environment/panels/`), so the image-arm Dockerfiles need the crops restored before a Harbor run;
- MinerU output (`mineru_out/`, full paper text) and the paragraph files (`work/*.paras.json`, `work/_syn/`), because four of the six papers are subscription-journal articles.
They stay on host A under `/home/aid1/Documents/harbor/v02/`. Hashes of all of them are in `hashes_v02.txt`.
