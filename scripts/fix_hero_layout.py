# 1. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

override = """
/* Hero Visual Column & Switcher Bar Fix */
.hero-visual-col {
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start !important;
}

.hero-3d-switcher-bar {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  width: 100% !important;
  margin-bottom: 20px !important;
  z-index: 10 !important;
}

.hero-switcher-pill {
  white-space: nowrap !important;
}

.webgl-lab-viewport {
  width: 100% !important;
  max-width: 500px !important;
  height: 500px !important;
  margin: 0 auto !important;
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write("\n" + override + "\n")

print("SUCCESS: Appended flex column and switcher override to styles.css!")

# 2. Update app.js camera distance
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = "const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);\n  camera.position.z = 7.5;"
replacement = "const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);\n  camera.position.z = 8.8;"

if target in js:
    js = js.replace(target, replacement, 1)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("SUCCESS: Updated Three.js camera distance in app.js!")
else:
    print("Camera target not found in app.js")
