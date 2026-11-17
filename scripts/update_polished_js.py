updated_hero_js = '''
/* ========================================================================= */
/* ADVANCED 3D MULTI-LAYER MOUSE PARALLAX & TILT ENGINE (POLISHED 3-ELEMENT) */
/* ========================================================================= */
function initHero3dInteractiveTilt() {
  const stage = document.getElementById('hero3dStage');
  const scene = document.getElementById('hero3dScene');
  const phone = document.getElementById('phone3dChassis');
  const glow = document.getElementById('heroAmbientGlow');
  const sheen = document.getElementById('phoneLightSheen');

  if (!stage || !scene || !phone) return;

  // 3 Focused Primary Floating Layers
  const floatingLayers = [
    { el: document.getElementById('layerRankBadge'), depthX: -36, depthY: -28, tz: 110 },
    { el: document.getElementById('layerRevenueCard'), depthX: 42, depthY: 32, tz: 90 },
    { el: document.getElementById('layerAiCard'), depthX: 35, depthY: 26, tz: 75 }
  ];

  // Resting defaults
  const defaultRotX = 4;
  const defaultRotY = -6;

  let targetX = 0;
  let targetY = 0;
  let currentX = 0;
  let currentY = 0;
  let isHovered = false;
  let isAnimating = false;
  let rafId = null;

  // Touch / Mobile check
  const isTouchDevice = window.matchMedia('(pointer: coarse)').matches;

  function onMouseMove(e) {
    const rect = stage.getBoundingClientRect();
    // Normalized coordinates from -0.5 to 0.5
    targetX = (e.clientX - rect.left) / rect.width - 0.5;
    targetY = (e.clientY - rect.top) / rect.height - 0.5;

    // Specular light sheen coordinates (0% to 100%)
    if (sheen) {
      const px = ((e.clientX - rect.left) / rect.width) * 100;
      const py = ((e.clientY - rect.top) / rect.height) * 100;
      sheen.style.setProperty('--sheen-x', `${px.toFixed(1)}%`);
      sheen.style.setProperty('--sheen-y', `${py.toFixed(1)}%`);
    }

    if (!isAnimating) {
      isAnimating = true;
      rafId = requestAnimationFrame(updatePhysics);
    }
  }

  function onMouseEnter() {
    isHovered = true;
    if (glow) {
      glow.style.transform = 'translate(-50%, -50%) scale(1.15)';
      glow.style.opacity = '1';
    }
  }

  function onMouseLeave() {
    isHovered = false;
    targetX = 0;
    targetY = 0;
    if (glow) {
      glow.style.transform = 'translate(-50%, -50%) scale(1)';
      glow.style.opacity = '0.85';
    }
  }

  function updatePhysics() {
    // Smooth spring interpolation (0.08 factor)
    const lerpFactor = isHovered ? 0.08 : 0.05;
    currentX += (targetX - currentX) * lerpFactor;
    currentY += (targetY - currentY) * lerpFactor;

    // Subtle 3D perspective tilt
    const rotX = defaultRotX - (currentY * 18);
    const rotY = defaultRotY + (currentX * 22);

    scene.style.transform = `rotateY(${rotY.toFixed(2)}deg) rotateX(${rotX.toFixed(2)}deg)`;

    // Phone subtle Z lift on hover
    const phoneLift = isHovered ? 12 : 0;
    phone.style.transform = `translateZ(${phoneLift}px)`;

    // Independent 3D parallax on each floating card
    floatingLayers.forEach(layer => {
      if (layer.el) {
        const tx = currentX * layer.depthX;
        const ty = currentY * layer.depthY;
        const extraLift = isHovered ? 10 : 0;
        const totalZ = layer.tz + extraLift;
        layer.el.style.transform = `translate3d(${tx.toFixed(1)}px, ${ty.toFixed(1)}px, ${totalZ}px)`;
      }
    });

    // Check if motion has settled
    const diff = Math.abs(targetX - currentX) + Math.abs(targetY - currentY);
    if (diff > 0.001 || isHovered) {
      rafId = requestAnimationFrame(updatePhysics);
    } else {
      isAnimating = false;
      scene.style.transform = `rotateY(${defaultRotY}deg) rotateX(${defaultRotX}deg)`;
      floatingLayers.forEach(layer => {
        if (layer.el) {
          layer.el.style.transform = `translate3d(0px, 0px, ${layer.tz}px)`;
        }
      });
      phone.style.transform = `translateZ(0px)`;
    }
  }

  // Mobile / Touch Auto-Float Logic
  if (isTouchDevice) {
    let t = 0;
    function autoFloat() {
      t += 0.02;
      const floatX = Math.sin(t) * 3;
      const floatY = Math.cos(t * 0.8) * 3;
      scene.style.transform = `rotateY(${defaultRotY + floatX}deg) rotateX(${defaultRotX + floatY}deg)`;
      requestAnimationFrame(autoFloat);
    }
    requestAnimationFrame(autoFloat);
    return;
  }

  // Desktop Mouse Events
  stage.addEventListener('mousemove', onMouseMove, { passive: true });
  stage.addEventListener('mouseenter', onMouseEnter, { passive: true });
  stage.addEventListener('mouseleave', onMouseLeave, { passive: true });

  // Initial resting 3D positions
  floatingLayers.forEach(layer => {
    if (layer.el) {
      layer.el.style.transform = `translate3d(0px, 0px, ${layer.tz}px)`;
    }
  });
}
'''

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

marker = '/* ========================================================================= */\n/* ADVANCED 3D MULTI-LAYER MOUSE PARALLAX & TILT ENGINE'
if marker in js:
    js = js[:js.find(marker)] + updated_hero_js
else:
    js += '\n' + updated_hero_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Successfully updated app.js with polished 3-element tilt logic")
