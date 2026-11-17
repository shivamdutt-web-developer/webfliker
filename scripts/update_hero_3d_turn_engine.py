with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function initHero3dInteractiveTilt()')
# Find matching close brace
open_b = 0
found_first = False
end_idx = pos
for i in range(pos, len(text)):
    if text[i] == '{':
        open_b += 1
        found_first = True
    elif text[i] == '}':
        open_b -= 1
        if found_first and open_b == 0:
            end_idx = i + 1
            break

new_hero_engine = '''function initHero3dInteractiveTilt() {
  const stage = document.getElementById('hero3dStage');
  const scene = document.getElementById('hero3dScene');
  const phone = document.getElementById('phone3dChassis');
  const glow = document.getElementById('heroAmbientGlow');
  const heroSection = document.getElementById('hero') || document.querySelector('.hero-section');

  if (!stage || !scene || !phone) return;

  // 3 Primary Floating Layers with distinct depth multipliers
  const floatingLayers = [
    { el: document.getElementById('layerRankBadge'), depthX: -45, depthY: -35, tz: 120 },
    { el: document.getElementById('layerRevenueCard'), depthX: 55, depthY: 40, tz: 95 },
    { el: document.getElementById('layerAiCard'), depthX: -30, depthY: 35, tz: 140 }
  ];

  // Resting base angles
  const baseRotX = 5;
  const baseRotY = -8;

  let targetNormX = 0;
  let targetNormY = 0;
  let currentNormX = 0;
  let currentNormY = 0;
  
  // Drag-to-rotate state
  let isDragging = false;
  let dragStartX = 0;
  let dragStartY = 0;
  let dragRotX = 0;
  let dragRotY = 0;
  let dragVelX = 0;
  let dragVelY = 0;

  let isHeroHovered = false;
  let time = 0;

  // Track mouse across the ENTIRE HERO SECTION and WINDOW
  function onHeroMouseMove(e) {
    if (isDragging) return;
    
    // Calculate position relative to viewport center or hero center
    const rect = (heroSection || stage).getBoundingClientRect();
    const centerX = rect.left + rect.width * 0.5;
    const centerY = rect.top + rect.height * 0.5;
    
    // Normalized from -1.0 (far left) to +1.0 (far right)
    targetNormX = Math.max(-1, Math.min(1, (e.clientX - centerX) / (rect.width * 0.45)));
    targetNormY = Math.max(-1, Math.min(1, (e.clientY - centerY) / (rect.height * 0.45)));
    
    isHeroHovered = true;
  }

  // Drag to rotate / turn functionality
  stage.style.cursor = 'grab';

  function onDragStart(clientX, clientY) {
    isDragging = true;
    dragStartX = clientX;
    dragStartY = clientY;
    stage.style.cursor = 'grabbing';
  }

  function onDragMove(clientX, clientY) {
    if (!isDragging) return;
    const deltaX = clientX - dragStartX;
    const deltaY = clientY - dragStartY;
    dragStartX = clientX;
    dragStartY = clientY;

    dragRotY += deltaX * 0.45;
    dragRotX -= deltaY * 0.35;
    // Clamp vertical tilt
    dragRotX = Math.max(-35, Math.min(35, dragRotX));
    dragRotY = Math.max(-55, Math.min(55, dragRotY));

    dragVelX = deltaX * 0.45;
    dragVelY = deltaY * 0.35;
  }

  function onDragEnd() {
    isDragging = false;
    stage.style.cursor = 'grab';
  }

  // Mouse drag listeners
  stage.addEventListener('mousedown', (e) => {
    e.preventDefault();
    onDragStart(e.clientX, e.clientY);
  });
  window.addEventListener('mousemove', (e) => {
    if (isDragging) {
      onDragMove(e.clientX, e.clientY);
    }
  });
  window.addEventListener('mouseup', onDragEnd);

  // Touch drag listeners
  stage.addEventListener('touchstart', (e) => {
    if (e.touches.length === 1) {
      onDragStart(e.touches[0].clientX, e.touches[0].clientY);
    }
  }, { passive: true });
  window.addEventListener('touchmove', (e) => {
    if (isDragging && e.touches.length === 1) {
      onDragMove(e.touches[0].clientX, e.touches[0].clientY);
    }
  }, { passive: true });
  window.addEventListener('touchend', onDragEnd);

  // General Hero Mouse Move
  if (heroSection) {
    heroSection.addEventListener('mousemove', onHeroMouseMove, { passive: true });
    heroSection.addEventListener('mouseenter', () => { isHeroHovered = true; });
    heroSection.addEventListener('mouseleave', () => { 
      isHeroHovered = false;
      targetNormX = 0;
      targetNormY = 0;
    });
  } else {
    window.addEventListener('mousemove', onHeroMouseMove, { passive: true });
  }

  // Continuous animation loop: Smooth physics + Idle Breathing Turn
  function animateScene() {
    time += 0.018;

    // Smooth lerp towards target
    const lerpSpeed = isDragging ? 0.3 : 0.08;
    currentNormX += (targetNormX - currentNormX) * lerpSpeed;
    currentNormY += (targetNormY - currentNormY) * lerpSpeed;

    // Inertia decay on drag
    if (!isDragging) {
      dragRotX += (0 - dragRotX) * 0.05;
      dragRotY += (0 - dragRotY) * 0.05;
    }

    // Idle autonomous breathing oscillation (always keeps the phone gently turning)
    const idleTurnY = Math.sin(time * 0.9) * 4.5;
    const idleTurnX = Math.cos(time * 0.7) * 2.5;

    // Dynamic Turn Angle:
    // When moving mouse: up to ±28 degrees turn on Y, ±16 degrees on X!
    const dynamicTurnY = currentNormX * 26;
    const dynamicTurnX = -(currentNormY * 16);

    const finalRotY = baseRotY + dynamicTurnY + dragRotY + idleTurnY;
    const finalRotX = baseRotX + dynamicTurnX + dragRotX + idleTurnX;

    // Apply rotation to the 3D scene container
    scene.style.transform = `rotateY(${finalRotY.toFixed(2)}deg) rotateX(${finalRotX.toFixed(2)}deg)`;

    // Additional dynamic 3D turn directly on the phone chassis
    phone.style.transform = `rotateY(${(finalRotY * 0.15).toFixed(2)}deg) translateZ(${isHeroHovered ? 16 : 0}px)`;

    // Multi-plane parallax offset for floating cards
    floatingLayers.forEach(layer => {
      if (layer.el) {
        const tx = currentNormX * layer.depthX + (dragRotY * 0.6);
        const ty = currentNormY * layer.depthY - (dragRotX * 0.4);
        const tz = layer.tz + (isHeroHovered ? 15 : 0);
        layer.el.style.transform = `translate3d(${tx.toFixed(1)}px, ${ty.toFixed(1)}px, ${tz}px)`;
      }
    });

    // Dynamic ambient backlight follow
    if (glow) {
      const glowX = -50 + currentNormX * 12;
      const glowY = -50 + currentNormY * 12;
      glow.style.transform = `translate(${glowX.toFixed(1)}%, ${glowY.toFixed(1)}%) scale(${isHeroHovered ? 1.2 : 1})`;
    }

    requestAnimationFrame(animateScene);
  }

  requestAnimationFrame(animateScene);
}'''

html = text[:pos] + new_hero_engine + text[end_idx:]
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated initHero3dInteractiveTilt with high-range 3D turn and drag engine!")
