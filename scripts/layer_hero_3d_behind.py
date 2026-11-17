# 1. Update CSS in styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_canvas_css = """.hero-3d-canvas {
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
}"""

new_canvas_css = """.hero-3d-canvas {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 680px !important;
  height: 680px !important;
  max-width: none !important;
  pointer-events: none;
  z-index: 0 !important;
  opacity: 0.85;
}
.hero-3d-scene {
  position: relative;
  z-index: 2 !important;
}"""

if old_canvas_css in css:
    css = css.replace(old_canvas_css, new_canvas_css)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("SUCCESS: Updated hero-3d-canvas CSS to layer behind phone!")
else:
    print("old_canvas_css not found, appending clean override.")
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write("\n" + new_canvas_css + "\n")

# 2. Adjust Three.js group scale and position in app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

target_group = "const heroGroup = new THREE.Group();\n  scene.add(heroGroup);"
new_group = "const heroGroup = new THREE.Group();\n  heroGroup.position.set(0.4, 0.1, 0);\n  heroGroup.scale.set(1.2, 1.2, 1.2);\n  scene.add(heroGroup);"

if target_group in js:
    js = js.replace(target_group, new_group)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("SUCCESS: Adjusted heroGroup position and scale in app.js!")
else:
    print("target_group not found in app.js")
