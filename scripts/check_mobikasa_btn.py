with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.mobikasa-arrow-btn[^{]*{[^}]+})', css)
for m in matches:
    print(m)
