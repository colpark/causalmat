"""harvest.py: take a subagent's reply verbatim from its transcript, and check the prompt it received against the packet.

  python harvest.py <transcript.jsonl> <packet.txt> <out.txt>
Writes the handback message (or, failing that, the last assistant text) to <out.txt> unchanged.
Exits 2 if the delivered prompt differs from the packet file, so a relay error cannot pass silently.
"""
import json, sys

def read(path):
    L = [json.loads(l) for l in open(path)]
    prompt = next(x['message']['content'] for x in L if x.get('type') == 'user' and isinstance(x.get('message', {}).get('content'), str))
    reply = None
    for x in L:
        c = x.get('message', {}).get('content')
        if x.get('type') != 'assistant' or not isinstance(c, list): continue
        for b in c:
            # the harness accepts only the first handback; later calls are refused, so keep the first
            if b.get('type') == 'tool_use' and b.get('name') == 'SubagentHandback' and reply is None: reply = b['input'].get('message')
    if reply is None:
        texts = [b['text'] for x in L if x.get('type') == 'assistant' and isinstance(x['message'].get('content'), list)
                 for b in x['message']['content'] if b.get('type') == 'text']
        reply = texts[-1] if texts else ''
    return prompt, reply

if __name__ == '__main__':
    prompt, reply = read(sys.argv[1])
    packet = open(sys.argv[2]).read()
    open(sys.argv[3], 'w').write(reply)
    same = prompt.strip() == packet.strip()
    print(f"{sys.argv[3]}: relay {'exact' if same else 'DIFFERS'}")
    if not same:
        import difflib
        for l in list(difflib.unified_diff(packet.strip().splitlines(), prompt.strip().splitlines(), lineterm='', n=0))[:20]: print('  ', l)
        sys.exit(2)
