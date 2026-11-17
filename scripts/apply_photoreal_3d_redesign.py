import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the legacy visual pane with the photoreal 3D asset
legacy_pane_replacement = '''<div class="trans-3d-visual-pane legacy-visual-pane">
                <div class="photoreal-3d-wrap floating-3d-legacy">
                  <img src="assets/3d/legacy_server_3d_photoreal.png" alt="3D Legacy Server Stack" class="photoreal-3d-img legacy-3d-img">
                </div>
              </div>'''

modern_pane_replacement = '''<div class="trans-3d-visual-pane modern-visual-pane">
                <div class="photoreal-3d-wrap floating-3d-modern">
                  <img src="assets/3d/modern_tech_3d_photoreal.png" alt="3D Modernized Headless Architecture Stack" class="photoreal-3d-img modern-3d-img">
                </div>
              </div>'''

# Replace legacy pane
html = re.sub(
    r'<div class="trans-3d-visual-pane legacy-visual-pane">[\s\S]*?</div>\s*</div>\s*<!-- Right: Failure Items',
    f'{legacy_pane_replacement}\n\n              <!-- Right: Failure Items',
    html
)

# Replace modern pane
html = re.sub(
    r'<div class="trans-3d-visual-pane modern-visual-pane">[\s\S]*?</div>\s*</div>\s*<!-- Right: Success Items',
    f'{modern_pane_replacement}\n\n              <!-- Right: Success Items',
    html
)

# Also update the background torus elements to use the photoreal 3D assets
torus_left_replacement = '''<div class="trans-3d-bg-element torus-top-left" aria-hidden="true">
      <img src="assets/3d/torus_left_photoreal.png" alt="" class="bg-torus-img torus-img-left">
    </div>'''

torus_right_replacement = '''<div class="trans-3d-bg-element torus-top-right" aria-hidden="true">
      <img src="assets/3d/torus_right_photoreal.png" alt="" class="bg-torus-img torus-img-right">
    </div>'''

html = re.sub(
    r'<div class="trans-3d-bg-element torus-top-left"[^>]*>[\s\S]*?</div>\s*<div class="trans-3d-bg-element torus-top-right"',
    f'{torus_left_replacement}\n\n    <div class="trans-3d-bg-element torus-top-right"',
    html
)

html = re.sub(
    r'<div class="trans-3d-bg-element torus-top-right"[^>]*>[\s\S]*?</div>\s*<div class="container trans-content-container">',
    f'{torus_right_replacement}\n\n    <div class="container trans-content-container">',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated index.html with photoreal 3D elements!")
