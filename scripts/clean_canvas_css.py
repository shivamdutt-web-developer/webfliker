with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
css = re.sub(r'/\* Hero 3D WebGL Canvas Layer \*/\s*\.hero-3d-canvas\s*\{[^}]*\}', '', css)
css = re.sub(r'\.hero-3d-canvas\s*\{[^}]*\}', '', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Cleaned up .hero-3d-canvas from styles.css!")
