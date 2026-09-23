"""cross.py: results/v2/contrib_vs_image_support.md -- the cross-table and the dispute resolution."""
import json, os, collections, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LV = ['shown', 'partial', 'not addressed', 'contradicts']
CB = ['establishes', 'supports_part', 'not_addressed', 'cuts_against']


def main():
    lab = {(l['case'], l['step']): l for l in map(json.loads, open(os.path.join(ROOT, 'results/v2/contrib_labels.jsonl')))}
    disp = {(d['case'], d['step']): d for d in map(json.loads, open(os.path.join(ROOT, 'results/v2/gt_disputes.jsonl')))}
    ct = collections.Counter((l['image_support'], l['contribution']) for l in lab.values())
    resolved, neither, kept = [], [], []
    for k, d in disp.items():
        l = lab.get(k)
        if not l: continue
        if l['mapped_support'] == d['arm_label']: resolved.append((d, l))
        elif l['mapped_support'] == d['graph_label']: kept.append((d, l))
        else: neither.append((d, l))
    P = print
    P("# The claim-contribution label against `image_support`")
    P("")
    P("**Every verdict is model against model.** `net-contrib` saw only the claim text, one observation")
    P("text and the relation between them: no panel, no question, no arm answer, no `gt_disputes.jsonl`,")
    P("and no tools. Panel references were scrubbed from the observation text before dispatch, because")
    P("naming a panel would itself tell the label it is looking at figure evidence.")
    P("")
    P(f"21 steps across the five cases. {len(lab)} labelled.")
    P("")
    P("## Cross-table: `image_support` (rows) against `contribution` (columns)")
    P("")
    P("| image_support | " + " | ".join(f"`{c}`" for c in CB) + " | total |")
    P("|---|" + "---|" * (len(CB) + 1))
    for r in LV:
        row = [ct.get((r, c), 0) for c in CB]
        if not sum(row): continue
        P(f"| **{r}** | " + " | ".join(str(x) for x in row) + f" | {sum(row)} |")
    tot = [sum(ct.get((r, c), 0) for r in LV) for c in CB]
    P("| **total** | " + " | ".join(str(x) for x in tot) + f" | {sum(tot)} |")
    P("")
    agree = sum(ct.get((r, c), 0) for r, c in zip(LV, CB))
    P(f"The two fields agree on **{agree} of {sum(tot)}** steps when `establishes`/`supports_part`/")
    P(f"`not_addressed`/`cuts_against` are read as shown/partial/not addressed/contradicts.")
    P("")
    P("## What it does to the 14 disputes")
    P("")
    P(f"- **{len(resolved)} resolved**: the new label agrees with what the full arm said.")
    P(f"- **{len(kept)} unchanged**: the new label agrees with the graph, against the arm.")
    P(f"- **{len(neither)} agree with neither**.")
    P("")
    if resolved:
        P("### Resolved")
        P("")
        P("| case | step | node | claim needs | graph | arm | contribution |")
        P("|---|---|---|---|---|---|---|")
        for d, l in resolved:
            u = '; '.join(l['unsettled'])[:70] or '-'
            P(f"| {d['case']} | {d['step']} | `{d['node']}` | {u} | {d['graph_label']} | {d['arm_label']} | `{l['contribution']}` |")
        P("")
    if kept:
        P("### Unchanged (label sides with the graph)")
        P("")
        for d, l in kept:
            P(f"- **{d['case']} step {d['step']} (`{d['node']}`)** graph `{d['graph_label']}`, arm `{d['arm_label']}`, contribution `{l['contribution']}`")
            P(f"  - why: {l['why']}")
        P("")
    if neither:
        P("### Agrees with neither, listed in full")
        P("")
        for d, l in neither:
            P(f"**{d['case']} step {d['step']} (`{d['node']}`, {d['technique']})**")
            P("")
            P(f"- claim: {l['claim_text'][:200]}")
            P(f"- observation: {l['observation_as_labelled'][:200]}")
            P(f"- graph `{d['graph_label']}` / arm `{d['arm_label']}` / contribution `{l['contribution']}` -> {l['mapped_support']}")
            P(f"- why: {l['why']}")
            P(f"- unsettled: {'; '.join(l['unsettled']) or '-'}")
            P("")
    rate = len(neither) / len(lab) if lab else 0
    P("## Stop rule")
    P("")
    P(f"Agrees with neither on **{len(neither)} of {len(lab)} steps = {rate:.0%}**; the threshold is one third.")
    P(f"**{'FIRED: the definition is unstable.' if rate > 1/3 else 'Not fired.'}**")
    P("")
    P("Every verdict is model against model.")


if __name__ == '__main__': main()
