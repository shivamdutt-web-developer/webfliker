with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
old_visual = re.search(r'<!-- Hero Right: MULTI-LAYER 3D GLASSMORPHIC HERO STAGE -->[\s\S]*?</div>\s*</div>\s*</div>\s*</div>\s*</section>', text)
if old_visual:
    print("Found old visual, length:", len(old_visual.group(0)))
else:
    print("Old visual not matched with exact regex")
