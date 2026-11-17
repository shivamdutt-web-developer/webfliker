with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [(m.start(), m.group(0)) for m in re.finditer(r'initProposalModal', text)]
print("In index.html:", len(matches))
for pos, m in matches:
    print(text[max(0, pos-50):min(len(text), pos+100)])

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()
matches_js = [(m.start(), m.group(0)) for m in re.finditer(r'initProposalModal', js)]
print("In app.js:", len(matches_js))
