# trace_kit

Pipeline: full v05 graph -> traces -> structural nets -> packets -> Sonnet subagents (no tools) -> verdicts.

- `cut_traces.py`            graph + collapsed spec -> traces.json (root, subtype, lift, floor, depth, hidden set, redactions, linear steps)
- `validate_traces.py`       structural nets, no model -> validation.json
- `build_trace_page.py`      graph + traces -> self-contained HTML with trace overlays
- `prepare_net_inputs.py`    traces + panel store -> one packet per (trace, net); keys kept apart in _keys.json
- `collect_net_outputs.py`   subagent replies -> grader packets -> verdicts.json + summary
- `agents/`                  Claude Code subagent definitions (copy to .claude/agents/): net-floor, net-reread, net-fullarm, net-judge, net-grader; all model: sonnet, tools removed except Read for the two image nets
- `fixtures/`                the 12 ceramic traces and their structural verdicts: the regression reference

No API key is used. The model is the Claude Code subagent.
