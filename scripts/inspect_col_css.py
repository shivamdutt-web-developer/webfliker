with open('styles.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.(hero-visual-col|hero-container)\s*\{[^}]*\})', text)
for m in matches[:6]:
    print(m[0])
    print('---')
