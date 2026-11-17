with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [(m.start(), m.group(0)) for m in re.finditer(r'webgl-studio|3D WebGL Lab', text)]
print("References found in index.html:", len(matches))
for pos, m in matches:
    print(text[max(0, pos-40):min(len(text), pos+60)].replace('\n', ' '))
