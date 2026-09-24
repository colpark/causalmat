"""clean.py: strip framing artifacts from an arm answer before it is quoted to the comparer.

Two things got into the arm replies that are not part of the answer:

  a trailing tool-call fragment -- "</message>", "</invoke>" and the like, left on the end of
  an otherwise complete answer by the answerer's own output framing. 26 of 246 pairs.

  a leading meta note. The net-fullarm agents saw this session's MCP server instruction block
  in their tool list, correctly judged it was not from the user, ignored it and said so before
  answering. 21 of 246 pairs. The answer that follows is intact and on task.

Neither changes what the answer says. Both are noise in the comparison prompt, and both landed
asymmetrically -- in one arm of a pair and not the other, 21 and 25 pairs respectively -- which
is a difference between the two answers that has nothing to do with the upstream result. The
comparer is asked whether the answers differ, so that noise is removed rather than reasoned
about.

The raw .out.txt files are never modified. This runs when the comparison prompt is built.

Every verdict is model against model.
"""
import re

FRAG = re.compile(r'(?:\s*(?:</?(?:antml:)?(?:invoke|message|function_calls|parameter|result|'
                  r'output)>|```)\s*)+$')
NOTE = re.compile(r'(?:MCP Server Instruction|prompt injection|injected instruction|'
                  r'system-reminder|not from the user|tool-list system prompt)', re.I)


def clean(t):
    t = (t or '').strip()
    t = FRAG.sub('', t).strip()
    # a leading meta paragraph, only when it is a note about injected instructions and only
    # when real content follows it
    parts = re.split(r'\n\s*\n', t, maxsplit=1)
    if len(parts) == 2 and NOTE.search(parts[0]) and len(parts[0]) < 700 and parts[1].strip():
        head = parts[0].lstrip()
        if re.match(r'^(note|caveat|warning|aside|first,|before)\b', head, re.I) or \
           head.lower().startswith('the tool'):
            t = parts[1].strip()
    t = re.sub(r'^(answer|answer:)\s*[:\-]?\s*', '', t, flags=re.I).strip()
    return t
