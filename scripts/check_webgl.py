with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# check webgl-lab-section
lab_match = re.search(r'<section[^>]*id="webgl-studio"[^>]*>([\s\S]*?)</section>', text)
if lab_match:
    print("Found #webgl-studio, length:", len(lab_match.group(0)))
    print("Preview:\n", lab_match.group(0)[:500])
else:
    print("No #webgl-studio section found")
