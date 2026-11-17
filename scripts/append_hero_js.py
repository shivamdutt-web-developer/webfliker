hero_3d_js = '''
/* ========================================================================= */
/* ADVANCED 3D MULTI-LAYER MOUSE PARALLAX & TILT ENGINE (REFERENCE 1 & 2)    */
/* ========================================================================= */
function initHero3dInteractiveTilt() {
  const stage = document.getElementById('hero3dStage');
  const scene = document.getElementById('hero3dScene');
  const phone = document.getElementById('phone3dChassis');
  const glow = document.getElementById('heroAmbientGlow');
  const sheen = document.getElementById('phoneLightSheen');

  if (!stage || !scene || !phone) return;

  const floatingLayers = [
    { el: document.getElementById('layerSearchBar'), depthX: 24, depthY: 20, tz: 50 },
    { el: document.getElementById('layerSalesCard'), depthX: -32, depthY: -26, tz: 85 },
    { el: document.getElementById('layerProductCard'), depthX: 36, depthY: 28, tz: 105 },
    { el: document.getElementById('layerRankBadge'), depthX: -42, depthY: -35, tz: 125 },
    { el: document.getElementById('layerRevenueCard'), depthX: 40, depthY: 34, tz: 110 }
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

  // Check if device is touch-primary
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
      sheen.style.setProperty('--sheen-x', `${px}%`);
      sheen.style.setProperty('--sheen-y', `${py}%`);
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
    // Smooth interpolation (spring damping)
    const lerpFactor = isHovered ? 0.08 : 0.05;
    currentX += (targetX - currentX) * lerpFactor;
    currentY += (targetY - currentY) * lerpFactor;

    // Calculate rotation angles
    const rotX = defaultRotX - (currentY * 20); // Moving down tilts up
    const rotY = defaultRotY + (currentX * 24); // Moving right tilts right

    // Apply 3D transform to overall scene
    scene.style.transform = `rotateY(${rotY.toFixed(2)}deg) rotateX(${rotX.toFixed(2)}deg)`;

    // Apply 3D transform to phone chassis (subtle internal depth)
    const phoneLift = isHovered ? 15 : 0;
    phone.style.transform = `translateZ(${phoneLift}px)`;

    // Apply independent parallax depth to each floating card
    floatingLayers.forEach(layer => {
      if (layer.el) {
        const tx = currentX * layer.depthX;
        const ty = currentY * layer.depthY;
        const extraLift = isHovered ? 12 : 0;
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
      // Snap to exact resting defaults
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
      const floatY = Math.cos(t * 0.8) * 4;
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

  // Initial render of resting 3D positions
  floatingLayers.forEach(layer => {
    if (layer.el) {
      layer.el.style.transform = `translate3d(0px, 0px, ${layer.tz}px)`;
    }
  });
}
'''

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add call in DOMContentLoaded if not present
if 'initHero3dInteractiveTilt()' not in js:
    # Append after initFaqAccordion()
    js = js.replace('initFaqAccordion();', 'initFaqAccordion();\n  initHero3dInteractiveTilt();')
    js += '\n' + hero_3d_js
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Successfully added initHero3dInteractiveTilt to app.js")
else:
    print("initHero3dInteractiveTilt already in app.js")
