#!/bin/bash
# finalize_writer_paper.sh <paper> <tasks_dir>: harvest replies listed in dispatch_map.txt, merge the writer's four fields
# into results/traces/<paper>.traces.json, run the structural nets -> <paper>.validation.json
set -e
P=$1; TK=$2; cd "$(dirname "$0")/.."
D=results/traces/writer/$P; G=taxonomy/graphs_v05/first100/$P.json
while read id t; do python3 trace_kit/harvest.py $TK/$id.output $D/$t.writer.txt $D/$t.writer.out.txt >/dev/null || { echo "RELAY DIFF $t"; exit 2; }; done < $D/dispatch_map.txt
python3 trace_kit/writer_packets.py merge results/traces/cut/$P.traces.json $D results/traces/$P.traces.json
python3 trace_kit/validate_traces.py $G results/traces/$P.traces.json results/traces/$P.validation.json
