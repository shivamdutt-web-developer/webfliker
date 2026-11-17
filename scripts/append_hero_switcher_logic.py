# 1. Append CSS to styles.css
css_rules = """
/* ==========================================================================
   HERO 3D SPATIAL SHOWCASE & MODEL SWITCHER
   ========================================================================== */
.hero-3d-switcher-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 16px;
  position: relative;
  z-index: 10;
  flex-wrap: wrap;
}

.hero-switcher-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: 999px;
  background: rgba(13, 21, 39, 0.72);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #94a3b8;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-switcher-pill:hover {
  color: #ffffff;
  border-color: rgba(255, 94, 30, 0.4);
  transform: translateY(-2px);
}

.hero-switcher-pill.active {
  background: linear-gradient(135deg, #ff5e1e, #ff7a00) !important;
  color: #ffffff !important;
  border-color: transparent !important;
  box-shadow: 0 4px 18px rgba(255, 94, 30, 0.38) !important;
}

.webgl-lab-viewport {
  position: relative;
  width: 100%;
  height: 480px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
}

.webgl-lab-canvas {
  width: 100% !important;
  height: 100% !important;
  cursor: grab;
  outline: none;
}

.webgl-lab-canvas:active {
  cursor: grabbing;
}

.webgl-drag-hint {
  position: absolute;
  bottom: 8px;
  left: 50%;
  transform: translateX(-50%);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(13, 21, 39, 0.75);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: #94a3b8;
  font-size: 0.74rem;
  font-weight: 700;
  border: 1px solid rgba(255, 255, 255, 0.08);
  pointer-events: none;
  z-index: 5;
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.hero-3d-switcher-bar' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write("\n" + css_rules + "\n")
    print("SUCCESS: Appended hero switcher CSS to styles.css!")
else:
    print(".hero-3d-switcher-bar already in styles.css")

# 2. Add hero switcher event listener logic to app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_addition = """
  // Hero 3D Spatial View Switcher Wiring
  const btnHeroPhone = document.getElementById('btnHeroPhone');
  const heroWebglViewport = document.getElementById('heroWebglViewport');
  const hero3dScene = document.getElementById('hero3dScene');

  if (btnHeroPhone && heroWebglViewport && hero3dScene) {
    btnHeroPhone.addEventListener('click', () => {
      document.querySelectorAll('.hero-switcher-pill').forEach(b => b.classList.remove('active'));
      btnHeroPhone.classList.add('active');
      heroWebglViewport.style.display = 'none';
      hero3dScene.style.display = 'flex';
    });

    document.querySelectorAll('.hero-switcher-pill[data-3d-model]').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.hero-switcher-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        hero3dScene.style.display = 'none';
        heroWebglViewport.style.display = 'flex';
        window.dispatchEvent(new Event('resize'));
      });
    });
  }
"""

if 'btnHeroPhone' not in js:
    # insert inside DOMContentLoaded or initThreeJsLab
    idx = js.find('initThreeJsLab();')
    if idx != -1:
        js = js[:idx+17] + "\n" + js_addition + "\n" + js[idx+17:]
        with open('app.js', 'w', encoding='utf-8') as f:
            f.write(js)
        print("SUCCESS: Added hero switcher JS to app.js!")
    else:
        print("initThreeJsLab() call not found in app.js")
else:
    print("btnHeroPhone already in app.js")
