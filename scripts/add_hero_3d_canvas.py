# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<div class="hero-3d-ambient-glow" id="heroAmbientGlow"></div>'
replacement = '<div class="hero-3d-ambient-glow" id="heroAmbientGlow"></div>\n          <canvas id="hero3dCanvas" class="hero-3d-canvas"></canvas>'

if 'hero3dCanvas' not in html and target in html:
    html = html.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS: Added hero3dCanvas to index.html!")
else:
    print("hero3dCanvas already present or target not found.")

# 2. Add CSS to styles.css
css_rule = """
/* Hero 3D WebGL Canvas Layer */
.hero-3d-canvas {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100% !important;
  height: 100% !important;
  max-width: 580px;
  max-height: 580px;
  pointer-events: none;
  z-index: 1;
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.hero-3d-canvas' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(css_rule)
    print("SUCCESS: Added .hero-3d-canvas rule to styles.css!")
else:
    print(".hero-3d-canvas already present in styles.css.")
