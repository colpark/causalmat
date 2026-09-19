"""Fill a prompt template. Usage: python taxonomy/fill.py <template> KEY=VALUE ...  (VALUE may contain \\n)"""
import os
import sys

TAX = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(TAX, "prompts", sys.argv[1] + ".md")).read()
for kv in sys.argv[2:]:
    k, v = kv.split("=", 1)
    s = s.replace("{" + k + "}", v.replace("\\n", "\n"))
print(s)
