with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', text)
print("Defined functions in app.js:")
for fn in funcs:
    print(" -", fn)
