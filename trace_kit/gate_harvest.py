"""gate_harvest.py <map.txt> <tasks_dir>: for each 'agent paper trace arm' line, take the arm's reply from its transcript,
check the delivered prompt against results/v06c/gate/<paper>/<trace>.<arm>.txt, write <trace>.<arm>.out.txt; then write
<trace>.grader.<arm>.txt, the grader prompt (question, key with answer_scope, grading note, candidate)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harvest import read
G = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'results', 'v06c', 'gate')
def grader_prompt(pk, question, cand):
    k = pk['key']
    return (f"Question: {question}\n\nAnswer key (answer_scope: {k['answer_scope']}"
            + (" - the given panels support the whole answer" if k['answer_scope'] == 'full' else " - the given panels support only part; the key says what cannot be determined")
            + f"): {k['answer_key']}\n\nGrading note: {k['grading']}\n\nCandidate answer:\n{cand.strip()}")
if __name__ == '__main__':
    for line in open(sys.argv[1]):
        a, P, T, arm = line.split()[:4]
        if arm.startswith('grader'): continue
        tr = os.path.join(sys.argv[2], a + '.output')
        if not os.path.exists(tr): print('MISSING', P, T, arm); continue
        prompt, reply = read(tr); base = os.path.join(G, P, T)
        ok = prompt.strip() == open(f"{base}.{arm}.txt").read().strip()
        open(f"{base}.{arm}.out.txt", 'w').write(reply)
        pk = json.load(open(f"{base}.gate.json")); q = pk['fullarm'].split('Question: ', 1)[1].split('\n\nImages', 1)[0]
        open(f"{base}.grader.{arm}.txt", 'w').write(grader_prompt(pk, q, reply))
        print(P[:24], T, arm, 'prompt', 'exact' if ok else 'DIFFERS', '|', reply.strip()[:60].replace('\n', ' '))
