/**
 * WEBFLIKR.COM - Core Interactive Engine
 * 1. Three.js 3D WebGL Canvas (Desktop & Mobile Optimized)
 * 2. WordPress-Style Live In-Page Visual CMS Engine (Editable text & real-time updates)
 * 3. PageTraffic Mega-Menus & Mobile Accordion Navigation
 * 4. Multi-Step "Get a Proposal" Funnel
 * 5. Pricing Matrix Toggle (Monthly vs Annual)
 */

document.addEventListener('DOMContentLoaded', () => {
  initFaqAccordion();
  initHero3dInteractiveTilt();
  // Initialize Lucide Icons
  if (window.lucide) {
    lucide.createIcons();
  }

  // 0. Schbang Motion Suite (Lenis, Magnetic Cursor, Brand Morph, Particle Canvas)
  initLenisSmoothScroll();
  initSchbangMagneticCursor();
  initSchbangBrandMorph();
  initCtaParticleWave();
  init3dCardPhysics();

  // 1. Initialize Three.js 3D Canvas
  initBeforeAfterSlider();
  initKpiProgressBars();
  // initStudioTabs();
  initThreeJsHero();
  initThreeJsLab();

    init3dCardTilt();
  initMobikasaDeviceTilt();

  // 2. Initialize WordPress Live Visual CMS Editor
  initVisualCmsEditor();

  // 3. Initialize Mobile Navigation & Mega Menu Accordions
  initMobileNavigation();
  initFormAccessibility();

  // 4. Initialize Multi-Step Proposal Modal
  initProposalModal();

  // 5. Initialize Pricing Toggle (Monthly vs Annual -20%)
  initPricingToggle();

  // 6. Initialize Portfolio Filter Tabs
  initPortfolioFilters();

  // FAQ Accordion Interaction
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    if (questionBtn) {
      questionBtn.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        faqItems.forEach(i => {
          i.classList.remove('active');
          const a = i.querySelector('.faq-answer');
          if (a) a.style.display = 'none';
        });
        if (!isActive) {
          item.classList.add('active');
          if (answer) answer.style.display = 'block';
        }
      });
    }
  });

});

/* ==========================================================================
   1. THREE.JS 3D INTERACTIVE HERO ENGINE (SCHBANG & MOBIKASA STYLE)
   ========================================================================== */
/* ==========================================================================
   1. THREE.JS 3D INTERACTIVE AMBIENT ENGINE (WARM MOBIKASA & SCHBANG ATMOSPHERE)
   ========================================================================== */
/* ==========================================================================
   1. THREE.JS 3D INTERACTIVE QUANTUM HERO ENGINE
   ========================================================================== */
function initThreeJsHero() {
  const canvas = document.getElementById('hero3dCanvas');
  if (!canvas || !window.THREE) return;

  const wrapper = canvas.parentElement;
  let width = wrapper.clientWidth || window.innerWidth;
  let height = wrapper.clientHeight || window.innerHeight;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
  camera.position.z = 9.5;

  const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true,
    antialias: true,
    powerPreference: 'high-performance'
  });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Main 3D Container Group
  const heroGroup = new THREE.Group();
  heroGroup.position.set(0.4, 0.1, 0);
  heroGroup.scale.set(1.2, 1.2, 1.2);
  scene.add(heroGroup);

  // Outer Gyroscopic Ring 1
  const ring1Geo = new THREE.TorusGeometry(3.6, 0.07, 16, 120);
  const ring1Mat = new THREE.MeshStandardMaterial({
    color: 0xff5e1e,
    metalness: 0.85,
    roughness: 0.2,
    emissive: 0x331000,
    emissiveIntensity: 0.2
  });
  const ring1 = new THREE.Mesh(ring1Geo, ring1Mat);
  heroGroup.add(ring1);

  // Outer Gyroscopic Ring 2 (Perpendicular)
  const ring2Geo = new THREE.TorusGeometry(2.9, 0.06, 16, 100);
  const ring2Mat = new THREE.MeshStandardMaterial({
    color: 0xffaa40,
    metalness: 0.9,
    roughness: 0.15,
    emissive: 0x442200,
    emissiveIntensity: 0.2
  });
  const ring2 = new THREE.Mesh(ring2Geo, ring2Mat);
  ring2.rotation.x = Math.PI / 2;
  heroGroup.add(ring2);

  // Inner Faceted Core Jewel (Icosahedron)
  const coreGeo = new THREE.IcosahedronGeometry(1.6, 1);
  const coreMat = new THREE.MeshPhysicalMaterial({
    color: 0xff5e1e,
    metalness: 0.1,
    roughness: 0.1,
    transmission: 0.7,
    transparent: true,
    opacity: 0.85,
    reflectivity: 0.9,
    clearcoat: 1.0,
    clearcoatRoughness: 0.1
  });
  const coreMesh = new THREE.Mesh(coreGeo, coreMat);
  heroGroup.add(coreMesh);

  // Glowing Wireframe Cage for the Core
  const wireGeo = new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(1.68, 1));
  const wireMat = new THREE.LineBasicMaterial({
    color: 0xffffff,
    transparent: true,
    opacity: 0.65,
    blending: THREE.AdditiveBlending
  });
  const wireMesh = new THREE.LineSegments(wireGeo, wireMat);
  heroGroup.add(wireMesh);

  // Orbiting Golden Stardust Particles
  const particleCount = 380;
  const particleGeo = new THREE.BufferGeometry();
  const particlePos = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount * 3; i += 3) {
    const radius = 3.0 + Math.random() * 5.0;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos((Math.random() * 2) - 1);
    particlePos[i] = radius * Math.sin(phi) * Math.cos(theta);
    particlePos[i + 1] = radius * Math.sin(phi) * Math.sin(theta);
    particlePos[i + 2] = radius * Math.cos(phi);
  }
  particleGeo.setAttribute('position', new THREE.BufferAttribute(particlePos, 3));

  const particleMat = new THREE.PointsMaterial({
    size: 0.05,
    color: 0xff8c42,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
  });
  const particleSystem = new THREE.Points(particleGeo, particleMat);
  heroGroup.add(particleSystem);

  // Dynamic Lights
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
  scene.add(ambientLight);

  const orangePoint = new THREE.PointLight(0xff5e1e, 4, 30);
  orangePoint.position.set(4, 5, 5);
  scene.add(orangePoint);

  const cyanPoint = new THREE.PointLight(0x00f0ff, 2.5, 30);
  cyanPoint.position.set(-4, -4, 4);
  scene.add(cyanPoint);

  // Core Pulse Light
  const coreLight = new THREE.PointLight(0xff5e1e, 3, 10);
  coreMesh.add(coreLight);

  // Interactive Cursor Tracking & Drag Orbit
  let mouseX = 0, mouseY = 0;
  let targetRotationX = 0, targetRotationY = 0;
  let isDragging = false;
  let previousMouseX = 0, previousMouseY = 0;

  window.addEventListener('mousemove', (e) => {
    const normX = (e.clientX / window.innerWidth) * 2 - 1;
    const normY = -(e.clientY / window.innerHeight) * 2 + 1;
    if (!isDragging) {
      targetRotationY = normX * 0.45;
      targetRotationX = -normY * 0.35;
    }
  });

  canvas.addEventListener('mousedown', (e) => {
    isDragging = true;
    previousMouseX = e.clientX;
    previousMouseY = e.clientY;
  });

  window.addEventListener('mouseup', () => { isDragging = false; });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    const deltaX = e.clientX - previousMouseX;
    const deltaY = e.clientY - previousMouseY;
    heroGroup.rotation.y += deltaX * 0.008;
    heroGroup.rotation.x += deltaY * 0.008;
    previousMouseX = e.clientX;
    previousMouseY = e.clientY;
  });

  // Touch Support
  canvas.addEventListener('touchstart', (e) => {
    if (e.touches.length === 1) {
      isDragging = true;
      previousMouseX = e.touches[0].clientX;
      previousMouseY = e.touches[0].clientY;
    }
  });
  window.addEventListener('touchend', () => { isDragging = false; });
  window.addEventListener('touchmove', (e) => {
    if (!isDragging || e.touches.length !== 1) return;
    const deltaX = e.touches[0].clientX - previousMouseX;
    const deltaY = e.touches[0].clientY - previousMouseY;
    heroGroup.rotation.y += deltaX * 0.008;
    heroGroup.rotation.x += deltaY * 0.008;
    previousMouseX = e.touches[0].clientX;
    previousMouseY = e.touches[0].clientY;
  });

  // Animation Loop
  const clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);
    const time = clock.getElapsedTime();

    // Constant Gyroscopic Rotation
    ring1.rotation.y = time * 0.35;
    ring1.rotation.x = time * 0.2;

    ring2.rotation.z = time * 0.3;
    ring2.rotation.y = time * 0.25;

    coreMesh.rotation.y = -time * 0.4;
    wireMesh.rotation.y = -time * 0.4;

    particleSystem.rotation.y = time * 0.05;

    // Pulse core
    const pulse = 1 + Math.sin(time * 2.5) * 0.05;
    coreMesh.scale.set(pulse, pulse, pulse);
    wireMesh.scale.set(pulse, pulse, pulse);
    coreLight.intensity = 2.5 + Math.sin(time * 3) * 1.0;

    // Smooth Cursor Parallax Easing
    if (!isDragging) {
      heroGroup.rotation.x += (targetRotationX - heroGroup.rotation.x) * 0.05;
      heroGroup.rotation.y += (targetRotationY - heroGroup.rotation.y) * 0.05;
    }

    renderer.render(scene, camera);
  }
  animate();

  // Responsive Resize
  window.addEventListener('resize', () => {
    width = wrapper.clientWidth || window.innerWidth;
    height = wrapper.clientHeight || window.innerHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  });
}


/* ==========================================================================
   1C. 3D WEBGL CREATIVE MOTION STUDIO (DIGITAL MARKETING & SEO THEMED 3D LAB)
   ========================================================================== */
function initThreeJsLab() {
  const canvas = document.getElementById('webglLabCanvas');
  if (!canvas || !window.THREE) return;

  const wrapper = canvas.parentElement;
  let width = wrapper.clientWidth || 800;
  let height = wrapper.clientHeight || 540;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
  camera.position.z = 7.5;

  const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true,
    antialias: true,
    powerPreference: 'high-performance'
  });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Studio Lights
  const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
  scene.add(ambientLight);

  const mainDirLight = new THREE.DirectionalLight(0xffffff, 2.2);
  mainDirLight.position.set(6, 8, 6);
  scene.add(mainDirLight);

  const orangeSpot = new THREE.PointLight(0xff5e1e, 5, 40);
  orangeSpot.position.set(5, 5, 5);
  scene.add(orangeSpot);

  const cyanSpot = new THREE.PointLight(0x00f0ff, 4, 40);
  cyanSpot.position.set(-6, -5, 5);
  scene.add(cyanSpot);

  const goldRim = new THREE.PointLight(0xffb703, 3, 30);
  goldRim.position.set(0, -6, -4);
  scene.add(goldRim);

  // Background Ambient Stardust
  const pCount = 350;
  const pGeo = new THREE.BufferGeometry();
  const pPos = new Float32Array(pCount * 3);
  for (let i = 0; i < pCount * 3; i += 3) {
    pPos[i] = (Math.random() - 0.5) * 14;
    pPos[i + 1] = (Math.random() - 0.5) * 14;
    pPos[i + 2] = (Math.random() - 0.5) * 14;
  }
  pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
  const pMat = new THREE.PointsMaterial({
    size: 0.04,
    color: 0xff8c42,
    transparent: true,
    opacity: 0.7,
    blending: THREE.AdditiveBlending
  });
  const labParticles = new THREE.Points(pGeo, pMat);
  scene.add(labParticles);

  // Main 3D Container Group
  const labGroup = new THREE.Group();
  scene.add(labGroup);

  // --- BUILDERS FOR SEO & DIGITAL AGENCY 3D MODELS ---

  // Model 1: 🔍 3D Cyber Search Magnifier & SERP Keyword Cubes
  function buildSearchLens(matType) {
    const grp = new THREE.Group();
    const isWire = matType === 'neonWire';

    // Frame
    const frameGeo = new THREE.TorusGeometry(1.6, 0.1, 16, 80);
    const frameMat = new THREE.MeshStandardMaterial({
      color: matType === 'liquidGold' ? 0xffb703 : 0xff5e1e,
      metalness: 0.9,
      roughness: 0.15,
      wireframe: isWire
    });
    const frame = new THREE.Mesh(frameGeo, frameMat);
    grp.add(frame);

    // Handle
    const handleGeo = new THREE.CylinderGeometry(0.1, 0.14, 1.8, 16);
    const handleMat = new THREE.MeshStandardMaterial({
      color: 0x1e293b,
      metalness: 0.8,
      roughness: 0.25,
      wireframe: isWire
    });
    const handle = new THREE.Mesh(handleGeo, handleMat);
    handle.position.set(1.4, -1.4, 0);
    handle.rotation.z = -Math.PI / 4;
    grp.add(handle);

    // Lens Glass
    const lensGeo = new THREE.CylinderGeometry(1.58, 1.58, 0.04, 32);
    const lensMat = new THREE.MeshPhysicalMaterial({
      color: 0x00f0ff,
      transmission: 0.85,
      transparent: true,
      opacity: 0.7,
      roughness: 0.1,
      clearcoat: 1.0,
      wireframe: isWire
    });
    const lens = new THREE.Mesh(lensGeo, lensMat);
    lens.rotation.x = Math.PI / 2;
    grp.add(lens);

    // 3 Orbiting Keyword Data Cubes (#1 Rank, CTR, Keywords)
    const cubeMat = new THREE.MeshStandardMaterial({
      color: 0xffaa40,
      metalness: 0.7,
      roughness: 0.2,
      wireframe: isWire
    });
    const c1 = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.4, 0.4), cubeMat);
    c1.position.set(-0.7, 0.6, 0.4);
    grp.add(c1);

    const c2 = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.32, 0.32), cubeMat);
    c2.position.set(0.6, -0.5, -0.3);
    grp.add(c2);

    const c3 = new THREE.Mesh(new THREE.BoxGeometry(0.26, 0.26, 0.26), cubeMat);
    c3.position.set(0.2, 0.75, -0.2);
    grp.add(c3);

    // Laser Scan Beam Line
    const beamGeo = new THREE.CylinderGeometry(0.018, 0.018, 3.1, 8);
    const beamMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
    const beam = new THREE.Mesh(beamGeo, beamMat);
    beam.rotation.z = Math.PI / 2;
    grp.add(beam);

    grp.userData = { type: 'magnifier', c1, c2, c3, beam };
    return grp;
  }

  // Model 2: 🚀 3D Growth Velocity Rocket & Trajectory Spiral
  function buildGrowthRocket(matType) {
    const grp = new THREE.Group();
    const isWire = matType === 'neonWire';

    // Fuselage
    const bodyGeo = new THREE.CylinderGeometry(0.25, 0.65, 2.3, 20);
    const bodyMat = new THREE.MeshStandardMaterial({
      color: matType === 'liquidGold' ? 0xffb703 : 0xffffff,
      metalness: 0.9,
      roughness: 0.2,
      wireframe: isWire
    });
    const body = new THREE.Mesh(bodyGeo, bodyMat);
    grp.add(body);

    // Nose Cone
    const noseGeo = new THREE.ConeGeometry(0.25, 1.1, 20);
    const noseMat = new THREE.MeshStandardMaterial({
      color: 0xff5e1e,
      metalness: 0.9,
      roughness: 0.2,
      wireframe: isWire
    });
    const nose = new THREE.Mesh(noseGeo, noseMat);
    nose.position.y = 1.7;
    grp.add(nose);

    // 3 Fins
    for (let i = 0; i < 3; i++) {
      const finGeo = new THREE.BoxGeometry(0.08, 0.7, 0.55);
      const fin = new THREE.Mesh(finGeo, noseMat);
      const angle = (i * Math.PI * 2) / 3;
      fin.position.set(Math.cos(angle) * 0.65, -0.85, Math.sin(angle) * 0.65);
      fin.rotation.y = -angle;
      grp.add(fin);
    }

    // Flame Cone
    const flameGeo = new THREE.ConeGeometry(0.35, 1.0, 16);
    const flameMat = new THREE.MeshBasicMaterial({ color: 0xff8c42, wireframe: isWire });
    const flame = new THREE.Mesh(flameGeo, flameMat);
    flame.position.y = -1.65;
    flame.rotation.x = Math.PI;
    grp.add(flame);

    // Orbital Growth Rings
    const ring1Geo = new THREE.TorusGeometry(1.6, 0.04, 16, 80);
    const ring1Mat = new THREE.MeshBasicMaterial({ color: 0x00f0ff, transparent: true, opacity: 0.6 });
    const ring1 = new THREE.Mesh(ring1Geo, ring1Mat);
    ring1.rotation.x = Math.PI / 3;
    grp.add(ring1);

    grp.userData = { type: 'rocket', flame, ring1 };
    return grp;
  }

  // Model 3: 🧠 3D AI Search & Neural Entity Knowledge Graph (GEO / ChatGPT / Gemini)
  function buildNeuralGraph(matType) {
    const grp = new THREE.Group();
    const isWire = matType === 'neonWire';

    // Central Knowledge Jewel
    const centerGeo = new THREE.IcosahedronGeometry(0.8, 1);
    const centerMat = new THREE.MeshStandardMaterial({
      color: matType === 'liquidGold' ? 0xffb703 : 0xff5e1e,
      metalness: 0.9,
      roughness: 0.2,
      wireframe: isWire
    });
    const center = new THREE.Mesh(centerGeo, centerMat);
    grp.add(center);

    // 10 Outer Entity Nodes & Connecting Synapse Beams
    const nodeGeo = new THREE.SphereGeometry(0.14, 12, 12);
    const nodeMat = new THREE.MeshStandardMaterial({
      color: 0x00f0ff,
      metalness: 0.8,
      roughness: 0.2,
      wireframe: isWire
    });

    for (let i = 0; i < 10; i++) {
      const phi = Math.acos(1 - 2 * (i + 0.5) / 10);
      const theta = Math.PI * (1 + Math.sqrt(5)) * i;
      const x = 2.1 * Math.sin(phi) * Math.cos(theta);
      const y = 2.1 * Math.sin(phi) * Math.sin(theta);
      const z = 2.1 * Math.cos(phi);

      const node = new THREE.Mesh(nodeGeo, nodeMat);
      node.position.set(x, y, z);
      grp.add(node);

      const points = [new THREE.Vector3(0, 0, 0), new THREE.Vector3(x, y, z)];
      const lineGeo = new THREE.BufferGeometry().setFromPoints(points);
      const lineMat = new THREE.LineBasicMaterial({ color: 0xffaa40, transparent: true, opacity: 0.6 });
      const line = new THREE.Line(lineGeo, lineMat);
      grp.add(line);
    }

    // Outer Halo Ring
    const haloGeo = new THREE.TorusGeometry(2.4, 0.03, 16, 80);
    const haloMat = new THREE.MeshBasicMaterial({ color: 0xff5e1e, transparent: true, opacity: 0.5 });
    const halo = new THREE.Mesh(haloGeo, haloMat);
    grp.add(halo);

    grp.userData = { type: 'neural', halo, center };
    return grp;
  }

  // Model 4: 📊 3D Interactive ROI Performance Analytics Towers
  function buildAnalyticsTowers(matType) {
    const grp = new THREE.Group();
    const isWire = matType === 'neonWire';

    const heights = [0.9, 1.8, 2.7, 4.0];
    const colors = [0x475569, 0xf59e0b, 0xff5e1e, 0x10b981];
    const xOffsets = [-1.5, -0.5, 0.5, 1.5];

    for (let i = 0; i < 4; i++) {
      const h = heights[i];
      const boxGeo = new THREE.BoxGeometry(0.65, h, 0.65);
      const boxMat = new THREE.MeshStandardMaterial({
        color: matType === 'liquidGold' ? 0xffb703 : colors[i],
        metalness: 0.85,
        roughness: 0.2,
        wireframe: isWire
      });
      const tower = new THREE.Mesh(boxGeo, boxMat);
      tower.position.set(xOffsets[i], h / 2 - 1.5, 0);
      grp.add(tower);

      // Top Peak Node
      const peakGeo = new THREE.SphereGeometry(0.12, 12, 12);
      const peakMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
      const peak = new THREE.Mesh(peakGeo, peakMat);
      peak.position.set(xOffsets[i], h - 1.45, 0);
      grp.add(peak);
    }

    // Connecting Growth Trendline
    const pts = [];
    for (let i = 0; i < 4; i++) {
      pts.push(new THREE.Vector3(xOffsets[i], heights[i] - 1.45, 0));
    }
    const curveGeo = new THREE.BufferGeometry().setFromPoints(pts);
    const curveMat = new THREE.LineBasicMaterial({ color: 0x00f0ff, linewidth: 2 });
    const curveLine = new THREE.Line(curveGeo, curveMat);
    grp.add(curveLine);

    grp.userData = { type: 'towers' };
    return grp;
  }

  // State
  let currentModelKey = 'searchLens';
  let currentMatKey = 'liquidGold';
  let active3DObject = null;

  function setModel(modelKey, matKey) {
    if (active3DObject) {
      labGroup.remove(active3DObject);
    }
    currentModelKey = modelKey;
    currentMatKey = matKey;

    if (modelKey === 'searchLens') {
      active3DObject = buildSearchLens(matKey);
    } else if (modelKey === 'growthRocket') {
      active3DObject = buildGrowthRocket(matKey);
    } else if (modelKey === 'neuralGraph') {
      active3DObject = buildNeuralGraph(matKey);
    } else if (modelKey === 'analyticsTowers') {
      active3DObject = buildAnalyticsTowers(matKey);
    }
    labGroup.add(active3DObject);
  }

  // Initial setup
  setModel('searchLens', 'liquidGold');

  // UI Event Listeners
  document.querySelectorAll('[data-3d-model]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('[data-3d-model]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const model = btn.getAttribute('data-3d-model');
      setModel(model, currentMatKey);
    });
  });

  document.querySelectorAll('[data-3d-material]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('[data-3d-material]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const mat = btn.getAttribute('data-3d-material');
      setModel(currentModelKey, mat);
    });
  });

  // Drag to Orbit
  let isDragging = false;
  let prevX = 0, prevY = 0;
  let autoRotate = true;

  canvas.addEventListener('mousedown', (e) => {
    isDragging = true;
    autoRotate = false;
    prevX = e.clientX;
    prevY = e.clientY;
  });
  window.addEventListener('mouseup', () => { isDragging = false; });
  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    const deltaX = e.clientX - prevX;
    const deltaY = e.clientY - prevY;
    labGroup.rotation.y += deltaX * 0.008;
    labGroup.rotation.x += deltaY * 0.008;
    prevX = e.clientX;
    prevY = e.clientY;
  });

  // Touch Support
  canvas.addEventListener('touchstart', (e) => {
    if (e.touches.length === 1) {
      isDragging = true;
      autoRotate = false;
      prevX = e.touches[0].clientX;
      prevY = e.touches[0].clientY;
    }
  });
  window.addEventListener('touchend', () => { isDragging = false; });
  window.addEventListener('touchmove', (e) => {
    if (!isDragging || e.touches.length !== 1) return;
    const deltaX = e.touches[0].clientX - prevX;
    const deltaY = e.touches[0].clientY - prevY;
    labGroup.rotation.y += deltaX * 0.008;
    labGroup.rotation.x += deltaY * 0.008;
    prevX = e.touches[0].clientX;
    prevY = e.touches[0].clientY;
  });

  // Animation Loop
  const clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);
    const time = clock.getElapsedTime();

    if (autoRotate && !isDragging) {
      labGroup.rotation.y += 0.008;
      labGroup.rotation.x = Math.sin(time * 0.5) * 0.12;
    }

    labParticles.rotation.y = time * 0.03;

    // Sub-element animation
    if (active3DObject && active3DObject.userData) {
      const u = active3DObject.userData;
      if (u.type === 'magnifier') {
        u.c1.rotation.y += 0.02;
        u.c2.rotation.x += 0.02;
        u.c3.rotation.z += 0.02;
        u.beam.position.y = Math.sin(time * 3) * 1.1;
      } else if (u.type === 'rocket') {
        const pulse = 1 + Math.sin(time * 12) * 0.15;
        u.flame.scale.set(pulse, pulse, pulse);
        u.ring1.rotation.z = time * 0.8;
      } else if (u.type === 'neural') {
        u.center.rotation.y = -time * 0.4;
        u.halo.rotation.z = time * 0.3;
      }
    }

    renderer.render(scene, camera);
  }
  animate();

  // Resize
  window.addEventListener('resize', () => {
    width = wrapper.clientWidth || 800;
    height = wrapper.clientHeight || 540;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  });
}


/* ==========================================================================
   1D. REAL-TIME 3D PERSPECTIVE CARD TILT ENGINE (WITH LIGHT SHEEN)
   ========================================================================== */
function init3dCardTilt() {
  const cards = document.querySelectorAll('.service-card, .deliverable-box, .team-card, .price-card, .work-card, .portfolio-card');
  if (!cards.length) return;

  cards.forEach(card => {
    card.style.transformStyle = 'preserve-3d';
    card.style.transition = 'transform 0.15s ease-out, box-shadow 0.15s ease-out';

    // Add sheen reflection layer if not present
    let sheen = card.querySelector('.card-3d-sheen');
    if (!sheen) {
      sheen = document.createElement('div');
      sheen.className = 'card-3d-sheen';
      sheen.style.cssText = 'position:absolute; inset:0; border-radius:inherit; pointer-events:none; background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.15) 0%, transparent 60%); opacity:0; transition:opacity 0.2s ease; z-index:2;';
      card.style.position = 'relative';
      card.appendChild(sheen);
    }

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -10;
      const rotateY = ((x - centerX) / centerX) * 10;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
      card.style.boxShadow = `0 20px 40px rgba(0, 0, 0, 0.12), 0 0 25px rgba(255, 94, 30, 0.15)`;

      sheen.style.opacity = '1';
      sheen.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255,255,255,0.25) 0%, transparent 65%)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
      card.style.boxShadow = '';
      sheen.style.opacity = '0';
    });
  });
}


/* ==========================================================================
   1B. MOBIKASA 3D SMARTPHONE INTERACTIVE MOUSE INERTIA ENGINE
   ========================================================================== */
function initMobikasaDeviceTilt() {
  const stage = document.getElementById('phonePerspectiveStage');
  const phone = document.getElementById('phone3dBody');
  if (!stage || !phone) return;

  let mouseX = 0;
  let mouseY = 0;
  let currentTiltX = 8;
  let currentTiltY = -14;

  window.addEventListener('mousemove', (e) => {
    const rect = stage.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    // Strictly clamp normalized tilt between -1 and 1 to prevent flip
    mouseX = Math.max(-1, Math.min(1, (e.clientX - centerX) / 350));
    mouseY = Math.max(-1, Math.min(1, (e.clientY - centerY) / 350));
  });

  function renderTilt() {
    // Smooth interpolation (damping inertia)
    const targetTiltX = 8 - (mouseY * 16);
    const targetTiltY = -14 + (mouseX * 22);
    
    currentTiltX += (targetTiltX - currentTiltX) * 0.08;
    currentTiltY += (targetTiltY - currentTiltY) * 0.08;

    phone.style.transform = `perspective(1200px) rotateX(${currentTiltX.toFixed(2)}deg) rotateY(${currentTiltY.toFixed(2)}deg) rotateZ(-1deg)`;
    requestAnimationFrame(renderTilt);
  }
  renderTilt();
}

/* ==========================================================================
   2. WORDPRESS-STYLE AUTHENTICATED VISUAL CMS EDITOR ENGINE
   (Admin logs in via /admin-login.html or /wp-admin to unlock inline visual editing)
   ========================================================================== */
function initVisualCmsEditor() {
  const STORAGE_KEY = 'webflikr_cms_saved_edits';
  const AUTH_KEY = 'webflikr_cms_authenticated';

  // 1. Check if user passed ?admin=true or is already authenticated in localStorage
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.get('admin') === 'true' || urlParams.get('edit') === 'true') {
    localStorage.setItem(AUTH_KEY, 'true');
  }

  const isAuthenticated = localStorage.getItem(AUTH_KEY) === 'true';

  // 2. Load Saved Edits from LocalStorage (always apply saved content for all users)
  const savedEdits = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  Object.keys(savedEdits).forEach(cmsId => {
    const el = document.querySelector(`[data-cms-id="${cmsId}"]`);
    if (el) {
      el.innerText = savedEdits[cmsId];
    }
  });

  // Keyboard shortcut: Ctrl + Shift + A to open admin login
  window.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.shiftKey && (e.key === 'A' || e.key === 'a' || e.key === 'E' || e.key === 'e')) {
      e.preventDefault();
      window.location.href = 'admin-login.html';
    }
  });

  // IF NOT AUTHENTICATED, DO NOT SHOW ADMIN BAR OR CONTROLS
  if (!isAuthenticated) {
    // Ensure any leftover admin bar is removed
    const existingBar = document.getElementById('wpAdminBar');
    if (existingBar) existingBar.remove();
    document.body.classList.remove('admin-logged-in', 'cms-edit-active');
    return;
  }

  // 3. USER IS AUTHENTICATED: INJECT WORDPRESS-STYLE ADMIN BAR
  document.body.classList.add('admin-logged-in');

  let adminBar = document.getElementById('wpAdminBar');
  if (!adminBar) {
    adminBar = document.createElement('div');
    adminBar.id = 'wpAdminBar';
    adminBar.className = 'wp-admin-bar';
    adminBar.innerHTML = `
      <div class="wp-admin-bar-left">
        <a href="admin-login.html" class="wp-admin-brand">
          <span class="wp-icon">⚡</span>
          <strong>WEBFLIKR CMS</strong>
        </a>
        <span class="wp-admin-divider">|</span>
        <span class="wp-admin-user"><i data-lucide="user-check" style="width:14px; height:14px;"></i> Logged in as: <strong>Admin (Client Portal)</strong></span>
      </div>
      <div class="wp-admin-bar-center">
        <button class="wp-btn-toggle-edit" id="toggleCmsModeBtn">
          <i data-lucide="edit-3" style="width:14px; height:14px;"></i>
          <span id="cmsBtnText">Turn ON Live Visual Edit Mode</span>
        </button>
        <button class="wp-btn-reset-edits" id="resetCmsChangesBtn" title="Reset all edits to factory default">
          <i data-lucide="rotate-ccw" style="width:13px; height:13px;"></i> Reset
        </button>
      </div>
      <div class="wp-admin-bar-right">
        <div class="wp-status-indicator">
          <span class="wp-status-dot"></span>
          <span>CMS Session Active</span>
        </div>
        <button class="wp-btn-logout" id="wpLogoutBtn">
          <i data-lucide="log-out" style="width:13px; height:13px;"></i> Logout
        </button>
      </div>
    `;
    document.body.insertBefore(adminBar, document.body.firstChild);
    if (window.lucide) lucide.createIcons();
  }

  // 4. Ensure Floating Edit Toolbar Exists (Two-way live editing dialog)
  let toolbar = document.getElementById('cmsEditorToolbar');
  if (!toolbar) {
    toolbar = document.createElement('div');
    toolbar.id = 'cmsEditorToolbar';
    toolbar.className = 'cms-editor-toolbar';
    toolbar.style.display = 'none';
    toolbar.innerHTML = `
      <div class="toolbar-header">
        <div class="toolbar-title-wrap">
          <i data-lucide="edit-2" class="icon-sm" style="color:var(--brand-orange)"></i>
          <span id="cmsEditingItemTitle">Editing Content</span>
        </div>
        <button id="cmsToolbarClose" class="toolbar-close-btn">&times;</button>
      </div>
      <div class="toolbar-body">
        <textarea id="cmsLiveTextInput" class="toolbar-textarea" rows="4" placeholder="Edit copy here..."></textarea>
      </div>
      <div class="toolbar-footer">
        <button id="cmsCancelBtn" class="btn btn-secondary btn-sm">Cancel</button>
        <button id="cmsApplyBtn" class="btn btn-primary btn-sm">Save &amp; Publish</button>
      </div>
    `;
    document.body.appendChild(toolbar);
    if (window.lucide) lucide.createIcons();
  }

  const toggleBtn = document.getElementById('toggleCmsModeBtn');
  const btnText = document.getElementById('cmsBtnText');
  const resetBtn = document.getElementById('resetCmsChangesBtn');
  const logoutBtn = document.getElementById('wpLogoutBtn');
  const toolbarClose = document.getElementById('cmsToolbarClose');
  const liveTextInput = document.getElementById('cmsLiveTextInput');
  const applyBtn = document.getElementById('cmsApplyBtn');
  const cancelBtn = document.getElementById('cmsCancelBtn');
  const editingTitle = document.getElementById('cmsEditingItemTitle');

  let isCmsActive = false;
  let currentlyEditingElement = null;

  function setEditMode(active) {
    isCmsActive = active;
    if (isCmsActive) {
      document.body.classList.add('cms-edit-active');
      toggleBtn.classList.add('active-mode');
      btnText.innerText = '🔴 Edit Mode ACTIVE (Click Any Text to Edit)';
    } else {
      document.body.classList.remove('cms-edit-active');
      toggleBtn.classList.remove('active-mode');
      btnText.innerText = 'Turn ON Live Visual Edit Mode';
      toolbar.style.display = 'none';
      currentlyEditingElement = null;
    }
  }

  // Toggle Edit Mode ON/OFF
  toggleBtn.addEventListener('click', () => {
    setEditMode(!isCmsActive);
  });

  // Auto-activate edit mode if redirected from login
  if (localStorage.getItem('webflikr_cms_auto_edit') === 'true') {
    localStorage.removeItem('webflikr_cms_auto_edit');
    setEditMode(true);
    showToastNotification('🔓 Admin Authenticated: Visual Edit Mode is now ACTIVE!');
  }

  // Handle Clicking on Editable Elements
  document.addEventListener('click', (e) => {
    if (!isCmsActive) return;

    const editableEl = e.target.closest('.editable');
    if (editableEl) {
      e.preventDefault();
      e.stopPropagation();

      currentlyEditingElement = editableEl;
      const cmsId = editableEl.getAttribute('data-cms-id') || 'Item';
      editingTitle.innerText = `Editing: [${cmsId}]`;
      liveTextInput.value = editableEl.innerText.trim();
      toolbar.style.display = 'block';
      liveTextInput.focus();
    }
  });

  // Real-time Visual Two-Way Binding
  liveTextInput.addEventListener('input', () => {
    if (currentlyEditingElement) {
      currentlyEditingElement.innerText = liveTextInput.value;
    }
  });

  // Apply & Save to CMS Memory
  applyBtn.addEventListener('click', () => {
    if (currentlyEditingElement) {
      const cmsId = currentlyEditingElement.getAttribute('data-cms-id');
      if (cmsId) {
        savedEdits[cmsId] = liveTextInput.value;
        localStorage.setItem(STORAGE_KEY, JSON.stringify(savedEdits));
      }
      toolbar.style.display = 'none';
      showToastNotification('✅ Text updated and saved to CMS successfully!');
    }
  });

  // Cancel / Close
  cancelBtn.addEventListener('click', () => {
    toolbar.style.display = 'none';
  });
  toolbarClose.addEventListener('click', () => {
    toolbar.style.display = 'none';
  });

  // Reset all edits back to factory default
  resetBtn.addEventListener('click', () => {
    if (confirm('Reset all edited content back to default values?')) {
      localStorage.removeItem(STORAGE_KEY);
      location.reload();
    }
  });

  // Logout Admin
  logoutBtn.addEventListener('click', () => {
    localStorage.removeItem(AUTH_KEY);
    localStorage.removeItem('webflikr_cms_auto_edit');
    showToastNotification('🔒 Logged out of Admin Portal.');
    setTimeout(() => {
      location.reload();
    }, 600);
  });
}


// Visual Toast feedback
function showToastNotification(message) {
  let toast = document.getElementById('webflikrToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'webflikrToast';
    toast.style.cssText = `
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      background: #00e676;
      color: #000;
      font-weight: 800;
      padding: 12px 24px;
      border-radius: 9999px;
      box-shadow: 0 10px 30px rgba(0, 230, 118, 0.5);
      z-index: 3000;
      font-size: 0.9rem;
      transition: opacity 0.3s;
    `;
    document.body.appendChild(toast);
  }
  toast.innerText = message;
  toast.style.opacity = '1';
  setTimeout(() => {
    toast.style.opacity = '0';
  }, 2500);
}

/* ==========================================================================
   3. MOBILE NAVIGATION & DRAWER
   ========================================================================== */
/* ========================================================================= */
/* UNIVERSAL MOBILE DRAWER, ACCORDION & A11Y ENGINE                         */
/* ========================================================================= */
function initMobileNavigation() {
  // 1. Ensure Mobile Menu Toggle Exists in Header
  let toggleBtn = document.getElementById('mobileMenuToggle');
  if (!toggleBtn) {
    const actions = document.querySelector('.header-actions');
    if (actions) {
      toggleBtn = document.createElement('button');
      toggleBtn.id = 'mobileMenuToggle';
      toggleBtn.className = 'mobile-menu-toggle';
      toggleBtn.setAttribute('aria-label', 'Open mobile navigation');
      toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
      actions.appendChild(toggleBtn);
    }
  }

  // 2. Ensure Luxury Light Mobile Drawer Exists
  let drawer = document.getElementById('mobileNavDrawer');
  let backdrop = document.getElementById('mobileDrawerBackdrop');

  if (!drawer) {
    drawer = document.createElement('div');
    drawer.id = 'mobileNavDrawer';
    drawer.className = 'mobile-nav-drawer';
    drawer.innerHTML = `
      <div class="mobile-drawer-header">
        <a href="index.html" style="display:flex; align-items:center; gap:8px; text-decoration:none;">
          <img src="logo.svg?v=2" alt="WEBFLIKR." style="height:26px;">
        </a>
        <button id="mobileDrawerClose" class="mobile-drawer-close" aria-label="Close Navigation Menu">&times;</button>
      </div>

      <div style="overflow-y:auto; flex:1; padding-right:4px;">
        <div class="mobile-drawer-category">Services</div>
        <ul class="mobile-drawer-links">
          <li><a href="services.html" class="mobile-drawer-link">All Services Overview <span>&rarr;</span></a></li>
          <li><a href="seo-services.html" class="mobile-drawer-link">SEO Services <span>&rarr;</span></a></li>
          <li><a href="website-designing.html" class="mobile-drawer-link">Website Designing <span>&rarr;</span></a></li>
          <li><a href="ecommerce-seo.html" class="mobile-drawer-link">Ecommerce SEO <span>&rarr;</span></a></li>
          <li><a href="enterprise-seo.html" class="mobile-drawer-link">Enterprise SEO <span>&rarr;</span></a></li>
          <li><a href="ai-seo.html" class="mobile-drawer-link">AI SEO & SGE <span>&rarr;</span></a></li>
          <li><a href="ppc-services.html" class="mobile-drawer-link">Paid Advertising (PPC) <span>&rarr;</span></a></li>
        </ul>

        <div class="mobile-drawer-category">Plans & Packages</div>
        <ul class="mobile-drawer-links">
          <li><a href="plans.html" class="mobile-drawer-link">All Plans Overview <span>&rarr;</span></a></li>
          <li><a href="seo-plans.html" class="mobile-drawer-link">SEO Plans <span>&rarr;</span></a></li>
          <li><a href="local-seo-plans.html" class="mobile-drawer-link">Google Map Local SEO <span>&rarr;</span></a></li>
          <li><a href="ecommerce-seo-plans.html" class="mobile-drawer-link">Ecommerce SEO Plans <span>&rarr;</span></a></li>
          <li><a href="ppc-plans.html" class="mobile-drawer-link">PPC Management Plans <span>&rarr;</span></a></li>
          <li><a href="social-media-plans.html" class="mobile-drawer-link">Social Media Plans <span>&rarr;</span></a></li>
        </ul>

        <div class="mobile-drawer-category">Who We Are</div>
        <ul class="mobile-drawer-links">
          <li><a href="about-us.html" class="mobile-drawer-link">About Webflikr <span>&rarr;</span></a></li>
          <li><a href="our-team.html" class="mobile-drawer-link">Our Team <span>&rarr;</span></a></li>
          <li><a href="case-studies.html" class="mobile-drawer-link">Case Studies <span>&rarr;</span></a></li>
          <li><a href="featured-clients.html" class="mobile-drawer-link">Featured Clients <span>&rarr;</span></a></li>
          <li><a href="testimonials.html" class="mobile-drawer-link">Reviews & Ratings <span>&rarr;</span></a></li>
          <li><a href="seo-awards.html" class="mobile-drawer-link">SEO Awards <span>&rarr;</span></a></li>
          <li><a href="our-locations.html" class="mobile-drawer-link">Global Office Hubs <span>&rarr;</span></a></li>
        </ul>

        <div class="mobile-drawer-category">Resources & Insights</div>
        <ul class="mobile-drawer-links">
          <li><a href="blog.html" class="mobile-drawer-link">Research Blog <span>&rarr;</span></a></li>
          <li><a href="free-guides.html" class="mobile-drawer-link">Free Guides & Ebooks <span>&rarr;</span></a></li>
          <li><a href="events.html" class="mobile-drawer-link">Summits & Events <span>&rarr;</span></a></li>
          <li><a href="webinars.html" class="mobile-drawer-link">Webinars & Masterclasses <span>&rarr;</span></a></li>
          <li><a href="presentations.html" class="mobile-drawer-link">Slide Decks & Keynotes <span>&rarr;</span></a></li>
        </ul>

        <div class="mobile-drawer-category">Careers & Culture</div>
        <ul class="mobile-drawer-links">
          <li><a href="current-openings.html" class="mobile-drawer-link">Current Openings (8 Roles) <span>&rarr;</span></a></li>
          <li><a href="career.html" class="mobile-drawer-link">Careers With Webflikr <span>&rarr;</span></a></li>
          <li><a href="benefits.html" class="mobile-drawer-link">Employee Benefits <span>&rarr;</span></a></li>
          <li><a href="life-at-webflikr.html" class="mobile-drawer-link">Life at Webflikr <span>&rarr;</span></a></li>
          <li><a href="our-values.html" class="mobile-drawer-link">Our Values <span>&rarr;</span></a></li>
          <li><a href="recruitment-process.html" class="mobile-drawer-link">Recruitment Process <span>&rarr;</span></a></li>
        </ul>
      </div>

      <div style="margin-top:auto; padding-top:16px; border-top:1px solid rgba(16,27,53,0.08);">
        <a href="tel:+919212521444" style="color:#475569; font-size:0.88rem; font-weight:700; text-decoration:none; display:flex; align-items:center; gap:8px; margin-bottom:12px;">
          <i class="fas fa-phone-alt" style="color:#FF5A1F;"></i> +91 92125 21444
        </a>
        <a href="get-a-proposal.html" class="btn-cta-main" style="width:100%; text-align:center; display:block; padding:12px 20px; font-weight:800; border-radius:9999px; text-decoration:none;">
          GET A PROPOSAL ↗
        </a>
      </div>
    `;
    document.body.appendChild(drawer);

    backdrop = document.createElement('div');
    backdrop.id = 'mobileDrawerBackdrop';
    backdrop.className = 'mobile-drawer-backdrop';
    document.body.appendChild(backdrop);
  }

  const closeBtn = document.getElementById('mobileDrawerClose');
  const toggleBtns = document.querySelectorAll('#mobileMenuToggle, .mobile-menu-toggle, #mobileMenuBtn, .mobile-nav-toggle, button[aria-label*="navigation"]');

  function openDrawer() {
    drawer.classList.add('active');
    if (backdrop) backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('active');
    if (backdrop) backdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  toggleBtns.forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      e.stopPropagation();
      openDrawer();
    };
  });

  if (closeBtn) closeBtn.onclick = closeDrawer;
  if (backdrop) backdrop.onclick = closeDrawer;

  drawer.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', closeDrawer);
  });
}

function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item, .faq-accordion-item, .accordion-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question, .accordion-header, .faq-header, button');
    const answer = item.querySelector('.faq-answer, .accordion-content, .faq-body');

    if (questionBtn) {
      questionBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const isActive = item.classList.contains('active');
        faqItems.forEach(i => {
          i.classList.remove('active');
          const a = i.querySelector('.faq-answer, .accordion-content, .faq-body');
          if (a) a.style.display = 'none';
        });

        if (!isActive) {
          item.classList.add('active');
          if (answer) answer.style.display = 'block';
        }
      });
    }
  });
}

function initFormAccessibility() {
  // Ensure favicon exists in head
  if (!document.querySelector('link[rel*="icon"]')) {
    const link = document.createElement('link');
    link.rel = 'icon';
    link.type = 'image/svg+xml';
    link.href = 'logo.svg';
    document.head.appendChild(link);
  }

  // Auto-label inputs for screen readers
  document.querySelectorAll('input:not([aria-label]), select:not([aria-label])').forEach(input => {
    const placeholder = input.getAttribute('placeholder') || input.name || input.id || 'Search & Form Field';
    input.setAttribute('aria-label', placeholder);
  });
}

function runInstantScan() {
  const urlInput = document.getElementById('scanUrlInput');
  const hud = document.getElementById('scannerResultsHud');
  const label = document.getElementById('scannedDomainLabel');
  const btn = document.getElementById('scanSubmitBtn');
  if (!urlInput || !hud) return;

  const url = urlInput.value.trim() || 'yourbrand.com';
  let cleanDomain = url.replace(/^https?:\/\//, '').replace(/\/.*$/, '');
  if (label) label.textContent = cleanDomain;

  btn.disabled = true;
  btn.innerHTML = '<span>ANALYZING SERP &amp; CWV...</span> <i data-lucide="loader-2" style="animation:spin 1s linear infinite;"></i>';
  if (window.lucide) lucide.createIcons();

  setTimeout(() => {
    hud.style.display = 'block';
    hud.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    btn.disabled = false;
    btn.innerHTML = '<span>RE-SCAN DOMAIN</span> <i data-lucide="refresh-cw"></i>';
    if (window.lucide) lucide.createIcons();
  }, 1000);
}

window.runInstantScan = runInstantScan;


/* ==========================================================================
   SCHBANG-STYLE MOTION, LENIS SMOOTH SCROLL, MAGNETIC CURSOR & PARTICLE CANVAS
   ========================================================================== */

// 1. Lenis Smooth Scroll Engine
function initLenisSmoothScroll() {
  if (typeof Lenis !== 'undefined') {
    try {
      const lenis = new Lenis({
        duration: 1.15,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        smoothWheel: true,
        wheelMultiplier: 1.0,
        touchMultiplier: 1.8,
      });

      function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
      }
      requestAnimationFrame(raf);
      window.lenisInstance = lenis;
    } catch (e) {
      console.warn('Lenis scroll initialization note:', e);
    }
  }
}

// 2. Schbang Magnetic Reactive Cursor System
function initSchbangMagneticCursor() {
  const dot = document.getElementById('cursorDot');
  const ring = document.getElementById('cursorRing');
  const label = document.getElementById('cursorLabel');
  if (!dot || !ring) return;

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let ringX = mouseX;
  let ringY = mouseY;
  let isHovering = false;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
  });

  // Smooth lerp loop for outer ring
  function renderCursor() {
    ringX += (mouseX - ringX) * 0.18;
    ringY += (mouseY - ringY) * 0.18;
    ring.style.transform = `translate3d(${ringX}px, ${ringY}px, 0)`;
    requestAnimationFrame(renderCursor);
  }
  renderCursor();

  // Hover triggers for cards, buttons, 3D canvases
  const interactiveTargets = [
    { selector: '.search-command-stage, #webglLabCanvas', text: '3D ORBIT' },
    { selector: '.deliverable-box, .pricing-card', text: 'EXPLORE' },
    { selector: '.btn-primary, .btn-proposal, .btn-proposal-header', text: 'CLAIM' },
    { selector: 'table tr', text: 'RANK #1' }
  ];

  interactiveTargets.forEach(target => {
    document.querySelectorAll(target.selector).forEach(el => {
      el.addEventListener('mouseenter', () => {
        ring.classList.add('active-hover');
        if (label) {
          label.textContent = target.text;
        }
      });
      el.addEventListener('mouseleave', () => {
        ring.classList.remove('active-hover');
      });
    });
  });
}

// 3. Dynamic Scroll-Driven Header Brand Morphing
function initSchbangBrandMorph() {
  const morphPill = document.getElementById('schbangMorphPill');
  if (!morphPill) return;

  const milestones = [
    { id: 'hero', text: '✦ Search Science' },
    { id: 'methodology', text: '✦ 9-Phase Delivery' },
    { id: 'webgl-studio', text: '✦ 3D WebGL Lab' },
    { id: 'rankings-proof', text: '✦ Verified #1 SERPs' },
    { id: 'pricing', text: '✦ Transparent Retainers' },
    { id: 'proposal', text: '✦ Growth Audit' }
  ];

  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY + 250;
    for (let i = milestones.length - 1; i >= 0; i--) {
      const section = document.getElementById(milestones[i].id);
      if (section && section.offsetTop <= scrollPos) {
        if (morphPill.textContent !== milestones[i].text) {
          morphPill.style.opacity = '0';
          morphPill.style.transform = 'translateY(-4px)';
          setTimeout(() => {
            morphPill.textContent = milestones[i].text;
            morphPill.style.opacity = '1';
            morphPill.style.transform = 'translateY(0)';
          }, 180);
        }
        break;
      }
    }
  }, { passive: true });
}

// 4. Schbang-Style Fluid Particle Wave Canvas in Proposal Section
function initCtaParticleWave() {
  const canvas = document.getElementById('ctaParticleCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  let width = canvas.width = canvas.parentElement.offsetWidth;
  let height = canvas.height = canvas.parentElement.offsetHeight;

  window.addEventListener('resize', () => {
    if (canvas.parentElement) {
      width = canvas.width = canvas.parentElement.offsetWidth;
      height = canvas.height = canvas.parentElement.offsetHeight;
    }
  });

  const particleCount = 85;
  const particles = [];
  let cursor = { x: -1000, y: -1000, radius: 140 };

  canvas.parentElement.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    cursor.x = e.clientX - rect.left;
    cursor.y = e.clientY - rect.top;
  });

  canvas.parentElement.addEventListener('mouseleave', () => {
    cursor.x = -1000;
    cursor.y = -1000;
  });

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 1.2,
      vy: (Math.random() - 0.5) * 1.2,
      radius: Math.random() * 2.5 + 1.2,
      color: Math.random() > 0.4 ? 'rgba(255, 94, 30, ' : 'rgba(56, 189, 248, '
    });
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];

      // Mouse repulsion physics
      const dx = cursor.x - p.x;
      const dy = cursor.y - p.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < cursor.radius) {
        const angle = Math.atan2(dy, dx);
        const force = (cursor.radius - dist) / cursor.radius;
        p.vx -= Math.cos(angle) * force * 1.8;
        p.vy -= Math.sin(angle) * force * 1.8;
      }

      p.x += p.vx;
      p.y += p.vy;

      // Friction damping
      p.vx *= 0.96;
      p.vy *= 0.96;

      // Natural subtle drift
      p.x += (Math.random() - 0.5) * 0.3;
      p.y += (Math.random() - 0.5) * 0.3;

      // Edge bounds
      if (p.x < 0) p.x = width;
      if (p.x > width) p.x = 0;
      if (p.y < 0) p.y = height;
      if (p.y > height) p.y = 0;

      // Draw particle
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fillStyle = p.color + '0.75)';
      ctx.fill();

      // Interconnect nodes
      for (let j = i + 1; j < particles.length; j++) {
        const p2 = particles[j];
        const linkDx = p.x - p2.x;
        const linkDy = p.y - p2.y;
        const linkDist = Math.sqrt(linkDx * linkDx + linkDy * linkDy);

        if (linkDist < 95) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = `rgba(255, 94, 30, ${0.25 * (1 - linkDist / 95)})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(draw);
  }
  draw();
}

// 5. Interactive 3D Card Physics with Gyroscopic Specular Glare (Mobikasa & Glassmorphism Spec)
function init3dCardPhysics() {
  const cards = document.querySelectorAll('.tilt-card, .kpi-card, .bento-card, .process-card, .phase-item-card, .mobikasa-case-card, .plan-card, .timeline-milestone-card, .hub-card, .testimonial-card, .pricing-card, .interactive-3d-card');
  const isTouch = window.matchMedia('(pointer: coarse)').matches;
  if (isTouch) return; // Non-blocking on touch/mobile

  cards.forEach(card => {
    card.classList.add('tilt-card');
    let rafId = null;

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      // Smooth subtle tilt (-6deg to +6deg)
      const rotateX = ((y - centerY) / centerY) * -6;
      const rotateY = ((x - centerX) / centerX) * 6;

      card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-5px)`;
      const pctX = `${((x / rect.width) * 100).toFixed(1)}%`;
      const pctY = `${((y / rect.height) * 100).toFixed(1)}%`;
      card.style.setProperty('--sheen-x', pctX);
      card.style.setProperty('--sheen-y', pctY);
      card.style.setProperty('--mouse-x', pctX);
      card.style.setProperty('--mouse-y', pctY);
    }, { passive: true });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
    });
  });
}


/* ========================================================================= */
/* NATIVE INTERACTIVE 3D WEBGL SEARCH & AI SIMULATOR (ZERO VIDEOS, 60FPS)     */
/* ========================================================================= */
function initStudioTabs() {
  const canvas = document.getElementById('studioInteractiveCanvas');
  const tabs = document.querySelectorAll('.studio-tab-btn');
  const stageTitle = document.getElementById('studioStageTitle');
  const stageTag = document.getElementById('studioStageTag');
  const hudVal1 = document.getElementById('hudVal1');
  const hudSub1 = document.getElementById('hudSub1');
  const hudLabel1 = document.getElementById('hudLabel1');
  const hudVal2 = document.getElementById('hudVal2');
  const hudSub2 = document.getElementById('hudSub2');
  const hudLabel2 = document.getElementById('hudLabel2');
  const hudVal3 = document.getElementById('hudVal3');
  const hudSub3 = document.getElementById('hudSub3');
  const hudLabel3 = document.getElementById('hudLabel3');
  const hudActionBtn = document.getElementById('hudActionBtn');
  const liveIndicator = document.getElementById('studioModeLiveIndicator');

  if (!canvas || !window.THREE) return;

  const wrap = canvas.parentElement;
  let width = wrap.clientWidth || 800;
  let height = wrap.clientHeight || 500;

  // 1. Scene, Camera, Renderer
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
  camera.position.set(0, 1.2, 7.8);
  camera.lookAt(0, 0, 0);

  const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true,
    antialias: true,
    powerPreference: 'high-performance'
  });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
  scene.add(ambientLight);

  const orangeLight = new THREE.PointLight(0xff5e1e, 3, 30);
  orangeLight.position.set(4, 5, 4);
  scene.add(orangeLight);

  const cyanLight = new THREE.PointLight(0x38bdf8, 3, 30);
  cyanLight.position.set(-4, -3, 3);
  scene.add(cyanLight);

  // Root interactive container for 3D orbit
  const studioRoot = new THREE.Group();
  scene.add(studioRoot);

  // =========================================================================
  // MODEL 1: GENERATIVE AI & GEO NEURAL CITATION GRAPH (geo)
  // =========================================================================
  const geoGroup = new THREE.Group();
  studioRoot.add(geoGroup);

  // Central AI Core: Wireframe Icosahedron + Inner Pulsing Core
  const icosaGeom = new THREE.IcosahedronGeometry(1.3, 1);
  const icosaMat = new THREE.MeshStandardMaterial({
    color: 0xff5e1e,
    wireframe: true,
    emissive: 0xff3b00,
    emissiveIntensity: 0.6
  });
  const icosaMesh = new THREE.Mesh(icosaGeom, icosaMat);
  geoGroup.add(icosaMesh);

  const innerCoreGeom = new THREE.SphereGeometry(0.7, 24, 24);
  const innerCoreMat = new THREE.MeshStandardMaterial({
    color: 0x38bdf8,
    roughness: 0.2,
    metalness: 0.8,
    emissive: 0x0284c7,
    emissiveIntensity: 0.4
  });
  const innerCoreMesh = new THREE.Mesh(innerCoreGeom, innerCoreMat);
  geoGroup.add(innerCoreMesh);

  // 14 Orbiting Entity Knowledge Graph Nodes
  const nodeCount = 14;
  const nodes = [];
  const nodeGeom = new THREE.SphereGeometry(0.12, 16, 16);
  const nodeMat = new THREE.MeshStandardMaterial({
    color: 0xffffff,
    emissive: 0x38bdf8,
    emissiveIntensity: 0.9,
    roughness: 0.1
  });

  const linePositions = [];
  for (let i = 0; i < nodeCount; i++) {
    const phi = Math.acos(-1 + (2 * i) / nodeCount);
    const theta = Math.sqrt(nodeCount * Math.PI) * phi;
    const r = 2.4 + (i % 3) * 0.4;
    const x = r * Math.cos(theta) * Math.sin(phi);
    const y = r * Math.sin(theta) * Math.sin(phi);
    const z = r * Math.cos(phi);

    const node = new THREE.Mesh(nodeGeom, nodeMat.clone());
    node.position.set(x, y, z);
    if (i % 2 === 0) {
      node.material.emissive.setHex(0xff5e1e);
    } else if (i % 3 === 0) {
      node.material.emissive.setHex(0x10b981);
    }
    geoGroup.add(node);
    nodes.push({ mesh: node, basePos: new THREE.Vector3(x, y, z), speed: 0.005 + (i % 5) * 0.002 });

    // Connect node to center
    linePositions.push(0, 0, 0, x, y, z);
    // Connect to adjacent node
    if (i > 0) {
      const prev = nodes[i - 1].basePos;
      linePositions.push(prev.x, prev.y, prev.z, x, y, z);
    }
  }

  const lineGeom = new THREE.BufferGeometry();
  lineGeom.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
  const lineMat = new THREE.LineBasicMaterial({
    color: 0x38bdf8,
    transparent: true,
    opacity: 0.35
  });
  const linesMesh = new THREE.LineSegments(lineGeom, lineMat);
  geoGroup.add(linesMesh);

  // Ambient Floating Data Particles
  const partCount = 200;
  const partGeom = new THREE.BufferGeometry();
  const partPos = new Float32Array(partCount * 3);
  for (let i = 0; i < partCount * 3; i += 3) {
    partPos[i] = (Math.random() - 0.5) * 10;
    partPos[i + 1] = (Math.random() - 0.5) * 6;
    partPos[i + 2] = (Math.random() - 0.5) * 8;
  }
  partGeom.setAttribute('position', new THREE.BufferAttribute(partPos, 3));
  const partMat = new THREE.PointsMaterial({
    color: 0xff7b39,
    size: 0.045,
    transparent: true,
    opacity: 0.7
  });
  const particles = new THREE.Points(partGeom, partMat);
  geoGroup.add(particles);

  // =========================================================================
  // MODEL 2: ECOMMERCE HEADLESS 3D GMV MATRIX (ecom)
  // =========================================================================
  const ecomGroup = new THREE.Group();
  ecomGroup.visible = false;
  studioRoot.add(ecomGroup);

  // 3-Tiered Architectural Hexagonal Base Platforms
  for (let i = 0; i < 3; i++) {
    const tierGeom = new THREE.CylinderGeometry(2.4 - i * 0.6, 2.6 - i * 0.6, 0.25, 6);
    const tierMat = new THREE.MeshStandardMaterial({
      color: 0x0f172a,
      roughness: 0.4,
      metalness: 0.8,
      wireframe: i === 1
    });
    const tierMesh = new THREE.Mesh(tierGeom, tierMat);
    tierMesh.position.y = -1.2 + i * 0.5;
    ecomGroup.add(tierMesh);
  }

  // Central Rising Revenue Crystal
  const crystalGeom = new THREE.OctahedronGeometry(1.2, 0);
  const crystalMat = new THREE.MeshStandardMaterial({
    color: 0x10b981,
    emissive: 0x059669,
    emissiveIntensity: 0.7,
    roughness: 0.1,
    metalness: 0.9
  });
  const crystalMesh = new THREE.Mesh(crystalGeom, crystalMat);
  crystalMesh.position.y = 0.8;
  ecomGroup.add(crystalMesh);

  // 6 Floating Transaction Cubes
  const transCubes = [];
  for (let i = 0; i < 6; i++) {
    const boxGeom = new THREE.BoxGeometry(0.35, 0.35, 0.35);
    const boxMat = new THREE.MeshStandardMaterial({
      color: 0xff5e1e,
      emissive: 0xff5e1e,
      emissiveIntensity: 0.6
    });
    const boxMesh = new THREE.Mesh(boxGeom, boxMat);
    const angle = (i / 6) * Math.PI * 2;
    boxMesh.position.set(Math.cos(angle) * 2.2, 0.2 + (i % 2) * 0.4, Math.sin(angle) * 2.2);
    ecomGroup.add(boxMesh);
    transCubes.push(boxMesh);
  }

  // =========================================================================
  // MODEL 3: GLOBAL GOOGLE SERP COMMAND RADAR (serp)
  // =========================================================================
  const serpGroup = new THREE.Group();
  serpGroup.visible = false;
  studioRoot.add(serpGroup);

  // Concentric Coordinate Radar Rings
  for (let i = 1; i <= 3; i++) {
    const ringGeom = new THREE.RingGeometry(i * 1.0, i * 1.0 + 0.03, 64);
    const ringMat = new THREE.MeshBasicMaterial({
      color: i === 1 ? 0xff5e1e : (i === 2 ? 0x10b981 : 0x38bdf8),
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.6
    });
    const ringMesh = new THREE.Mesh(ringGeom, ringMat);
    ringMesh.rotation.x = Math.PI / 2.4;
    serpGroup.add(ringMesh);
  }

  // Rotating Radar Scanner Plane
  const radarSweepGeom = new THREE.CircleGeometry(3.1, 32, 0, Math.PI / 3);
  const radarSweepMat = new THREE.MeshBasicMaterial({
    color: 0x10b981,
    side: THREE.DoubleSide,
    transparent: true,
    opacity: 0.25
  });
  const radarSweepMesh = new THREE.Mesh(radarSweepGeom, radarSweepMat);
  radarSweepMesh.rotation.x = Math.PI / 2.4;
  serpGroup.add(radarSweepMesh);

  // 16 Real Google SERP Rank Badges plotted across the radar
  const rankPins = [];
  for (let i = 0; i < 16; i++) {
    const pinGeom = new THREE.SphereGeometry(0.1, 16, 16);
    const pinMat = new THREE.MeshStandardMaterial({
      color: 0xffffff,
      emissive: i < 5 ? 0xff5e1e : (i < 10 ? 0x10b981 : 0x38bdf8),
      emissiveIntensity: 0.95
    });
    const pin = new THREE.Mesh(pinGeom, pinMat);
    const r = 0.6 + (i * 0.16);
    const theta = (i * 1.35);
    pin.position.set(r * Math.cos(theta), (Math.sin(theta) * r) * 0.35, r * Math.sin(theta) * 0.7);
    serpGroup.add(pin);
    rankPins.push(pin);
  }

  // =========================================================================
  // INTERACTIVE 3D ORBIT MOUSE DRAG PHYSICS
  // =========================================================================
  let isDragging = false;
  let prevMouseX = 0;
  let prevMouseY = 0;
  let targetRotX = 0;
  let targetRotY = 0;

  canvas.addEventListener('mousedown', (e) => {
    isDragging = true;
    prevMouseX = e.clientX;
    prevMouseY = e.clientY;
    canvas.style.cursor = 'grabbing';
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
    canvas.style.cursor = 'grab';
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    const deltaX = e.clientX - prevMouseX;
    const deltaY = e.clientY - prevMouseY;
    prevMouseX = e.clientX;
    prevMouseY = e.clientY;

    targetRotY += deltaX * 0.006;
    targetRotX += deltaY * 0.006;
  });

  // Touch support for mobile
  canvas.addEventListener('touchstart', (e) => {
    if (e.touches.length === 1) {
      isDragging = true;
      prevMouseX = e.touches[0].clientX;
      prevMouseY = e.touches[0].clientY;
    }
  }, { passive: true });

  window.addEventListener('touchend', () => { isDragging = false; });

  canvas.addEventListener('touchmove', (e) => {
    if (!isDragging || e.touches.length !== 1) return;
    const deltaX = e.touches[0].clientX - prevMouseX;
    const deltaY = e.touches[0].clientY - prevMouseY;
    prevMouseX = e.touches[0].clientX;
    prevMouseY = e.touches[0].clientY;

    targetRotY += deltaX * 0.008;
    targetRotX += deltaY * 0.008;
  }, { passive: true });

  // =========================================================================
  // TAB SWITCHER LOGIC
  // =========================================================================
  const studioData = {
    geo: {
      title: '3D GENERATIVE ENGINE CITATION CORE (GEO)',
      tag: 'CHATGPT • GEMINI • PERPLEXITY',
      indicator: 'Live 3D Neural Knowledge Graph • Active AI Citations',
      l1: 'AI MODEL CITATION RATE', v1: '98.6%', s1: '↑ 3.4x vs Category Competitors',
      l2: 'STRUCTURED ENTITY GRAPH', v2: '140+ Nodes', s2: 'Verified JSON-LD Knowledge Base',
      l3: 'AI OVERVIEWS IMPRESSIONS', v3: '84.2%', s3: 'Google SGE Featured Snippets',
      actionText: 'Explore AI Architecture →', actionHref: 'ai-seo.html'
    },
    ecom: {
      title: '3D ECOMMERCE ORGANIC GMV ENGINE',
      tag: 'SHOPIFY PLUS • HEADLESS • BIGCOMMERCE',
      indicator: 'Live 3D eCommerce GMV Matrix • Real-Time SKU Pipelines',
      l1: 'ORGANIC REVENUE LIFT', v1: '+240%', s1: 'Average 12-Month GMV Growth',
      l2: 'CATALOG INDEXATION', v2: '99.4%', s2: 'Faceted Navigation Clean Architecture',
      l3: 'CORE WEB VITALS SCORE', v3: '98/100', s3: 'Sub-second Headless LCP Performance',
      actionText: 'Explore eCommerce SEO →', actionHref: 'ecommerce-seo.html'
    },
    serp: {
      title: '3D GLOBAL GOOGLE SERP COMMAND CENTER',
      tag: 'COMMERCIAL HIGH-INTENT #1 POSITIONS',
      indicator: 'Live 3D Google SERP Radar • #1 Commercial Rankings Active',
      l1: 'VERIFIED #1 RANKINGS', v1: '4,820+', s1: 'High-Commercial Value Keywords',
      l2: 'ANNUAL ORGANIC CLICKS', v2: '12.4M', s2: 'Direct Transactional Search Traffic',
      l3: 'BLENDED CTR GAIN', v3: '+340%', s3: 'Rich Schema & Knowledge Panel CTR',
      actionText: 'Explore Enterprise SERPs →', actionHref: 'enterprise-seo.html'
    }
  };

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => {
        t.classList.remove('active');
        t.style.background = 'rgba(255, 255, 255, 0.05)';
        t.style.color = '#cbd5e1';
        t.style.borderColor = 'rgba(255, 255, 255, 0.12)';
        t.style.boxShadow = 'none';
      });
      tab.classList.add('active');
      tab.style.background = 'linear-gradient(135deg, #ff5e1e, #ff3b00)';
      tab.style.color = '#ffffff';
      tab.style.borderColor = '#ff5e1e';
      tab.style.boxShadow = '0 4px 18px rgba(255, 94, 30, 0.4)';

      const mode = tab.getAttribute('data-studio-mode');
      const data = studioData[mode];
      if (!data) return;

      // Switch 3D Model
      geoGroup.visible = (mode === 'geo');
      ecomGroup.visible = (mode === 'ecom');
      serpGroup.visible = (mode === 'serp');

      // Update HUD
      if (stageTitle) stageTitle.innerText = data.title;
      if (stageTag) stageTag.innerText = data.tag;
      if (liveIndicator) liveIndicator.innerText = data.indicator;
      if (hudLabel1) hudLabel1.innerText = data.l1;
      if (hudVal1) hudVal1.innerText = data.v1;
      if (hudSub1) hudSub1.innerText = data.s1;
      if (hudLabel2) hudLabel2.innerText = data.l2;
      if (hudVal2) hudVal2.innerText = data.v2;
      if (hudSub2) hudSub2.innerText = data.s2;
      if (hudLabel3) hudLabel3.innerText = data.l3;
      if (hudVal3) hudVal3.innerText = data.v3;
      if (hudSub3) hudSub3.innerText = data.s3;
      if (hudActionBtn) {
        hudActionBtn.innerText = data.actionText;
        hudActionBtn.href = data.actionHref;
      }
    });
  });

  // Resize handler
  window.addEventListener('resize', () => {
    width = wrap.clientWidth;
    height = wrap.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  });

  // =========================================================================
  // ANIMATION 60FPS LOOP
  // =========================================================================
  let clock = new THREE.Clock();
  function animate() {
    requestAnimationFrame(animate);
    const delta = clock.getDelta();
    const elapsed = clock.getElapsedTime();

    // Smooth inertia rotation
    studioRoot.rotation.y += (targetRotY - studioRoot.rotation.y) * 0.08;
    studioRoot.rotation.x += (targetRotX - studioRoot.rotation.x) * 0.08;
    targetRotY += 0.002; // Gentle continuous auto-spin

    // Animate Mode 1 (geo)
    if (geoGroup.visible) {
      icosaMesh.rotation.x += 0.008;
      icosaMesh.rotation.y += 0.012;
      innerCoreMesh.rotation.y -= 0.006;
      innerCoreMesh.scale.setScalar(1 + Math.sin(elapsed * 2) * 0.08);

      nodes.forEach((n, idx) => {
        n.mesh.position.y = n.basePos.y + Math.sin(elapsed * 1.5 + idx) * 0.15;
      });
      particles.rotation.y += 0.001;
    }

    // Animate Mode 2 (ecom)
    if (ecomGroup.visible) {
      crystalMesh.rotation.y += 0.015;
      crystalMesh.position.y = 0.8 + Math.sin(elapsed * 2) * 0.1;
      transCubes.forEach((c, idx) => {
        c.rotation.x += 0.01;
        c.rotation.y += 0.02;
        const angle = (idx / 6) * Math.PI * 2 + elapsed * 0.5;
        c.position.x = Math.cos(angle) * 2.2;
        c.position.z = Math.sin(angle) * 2.2;
      });
    }

    // Animate Mode 3 (serp)
    if (serpGroup.visible) {
      radarSweepMesh.rotation.z -= 0.025;
      rankPins.forEach((p, idx) => {
        p.scale.setScalar(1 + Math.sin(elapsed * 3 + idx) * 0.2);
      });
    }

    renderer.render(scene, camera);
  }

  animate();
}


/* ========================================================================= */
/* MOBIKASA-STYLE BEFORE / AFTER TRANSFORMATION SLIDER & KPI ANIMATION       */
/* ========================================================================= */
function initBeforeAfterSlider() {
  const container = document.getElementById('beforeAfterSlider');
  const beforeLayer = document.getElementById('baBeforeLayer');
  const handle = document.getElementById('baHandle');

  if (!container || !beforeLayer || !handle) return;

  let isSliding = false;

  function setSliderPosition(x) {
    const rect = container.getBoundingClientRect();
    let pos = (x - rect.left) / rect.width;
    pos = Math.max(0.05, Math.min(0.95, pos));
    const percentage = pos * 100;
    beforeLayer.style.width = percentage + '%';
    handle.style.left = percentage + '%';
  }

  container.addEventListener('mousedown', (e) => {
    isSliding = true;
    setSliderPosition(e.clientX);
  });

  window.addEventListener('mouseup', () => { isSliding = false; });

  window.addEventListener('mousemove', (e) => {
    if (!isSliding) return;
    setSliderPosition(e.clientX);
  });

  // Touch support for mobile devices
  container.addEventListener('touchstart', (e) => {
    if (e.touches.length === 1) {
      isSliding = true;
      setSliderPosition(e.touches[0].clientX);
    }
  }, { passive: true });

  window.addEventListener('touchend', () => { isSliding = false; });

  container.addEventListener('touchmove', (e) => {
    if (!isSliding || e.touches.length !== 1) return;
    setSliderPosition(e.touches[0].clientX);
  }, { passive: true });
}

function initKpiProgressBars() {
  const fills = document.querySelectorAll('.kpi-progress-fill');
  if (!fills.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const fill = entry.target;
        const targetWidth = fill.getAttribute('data-progress') || '85%';
        fill.style.width = targetWidth;
      }
    });
  }, { threshold: 0.2 });

  fills.forEach(f => observer.observe(f));
}


/* ========================================================================= */
/* MULTI-STEP PROPOSAL MODAL, PRICING TOGGLE, & PORTFOLIO FILTER HANDLERS    */
/* ========================================================================= */
function initProposalModal() {
  const modal = document.getElementById('proposalModal');
  const triggers = document.querySelectorAll('[data-open-proposal], .open-proposal-btn, a[href="#proposalModal"]');
  const closeBtns = document.querySelectorAll('.close-modal-btn, [data-close-modal]');

  if (!modal) return;

  triggers.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.add('active');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    });
  });

  closeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    });
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  });
}

function initPricingToggle() {
  const toggle = document.getElementById('billingToggle') || document.querySelector('.pricing-billing-toggle');
  const priceElements = document.querySelectorAll('[data-monthly-price][data-annual-price]');
  if (!toggle) return;

  toggle.addEventListener('change', () => {
    const isAnnual = toggle.checked;
    priceElements.forEach(el => {
      const price = isAnnual ? el.getAttribute('data-annual-price') : el.getAttribute('data-monthly-price');
      if (price) el.textContent = price;
    });
  });
}

function initPortfolioFilters() {
  const filterBtns = document.querySelectorAll('.portfolio-filter-btn, .work-filter-btn');
  const projectCards = document.querySelectorAll('.project-card, .case-study-card');

  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter') || 'all';
      projectCards.forEach(card => {
        const cat = card.getAttribute('data-category') || '';
        if (filter === 'all' || cat.includes(filter)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}



/* ========================================================================= */
/* ADVANCED 3D MULTI-LAYER MOUSE PARALLAX & TILT ENGINE (POLISHED 3-ELEMENT) */
/* ========================================================================= */
function initHero3dInteractiveTilt() {
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
}

/* ========================================================================= */
/* TRANSFORMATION SHOWCASE INTERACTIVE SWITCHER                              */
/* ========================================================================= */
function initTransformationSwitcher() {
  const btnSplit = document.getElementById('btnViewSplit');
  const btnLegacy = document.getElementById('btnViewLegacy');
  const btnModern = document.getElementById('btnViewModern');
  const cardLegacy = document.getElementById('cardLegacy');
  const cardModern = document.getElementById('cardModern');
  const grid = document.getElementById('transCardsGrid');
  const connector = document.getElementById('transCenterConnector');
  const pedestal = document.getElementById('transStagePedestal');
  const metricsWrap = document.getElementById('transBottomMetrics');
  const groupLegacy = document.querySelector('.trans-metrics-col-group.group-legacy');
  const groupModern = document.querySelector('.trans-metrics-col-group.group-modern');
  const centerDivider = document.querySelector('.trans-metrics-center-divider');

  if (!btnSplit || !btnLegacy || !btnModern || !cardLegacy || !cardModern || !grid) return;

  function setActiveTab(activeBtn) {
    [btnSplit, btnLegacy, btnModern].forEach(b => b.classList.remove('active'));
    activeBtn.classList.add('active');
  }

  btnSplit.addEventListener('click', () => {
    setActiveTab(btnSplit);
    cardLegacy.style.display = 'flex';
    cardModern.style.display = 'flex';
    grid.style.gridTemplateColumns = 'repeat(2, minmax(0, 1fr))';
    grid.style.maxWidth = '100%';
    grid.style.margin = '0';
    if (connector) connector.style.display = 'flex';
    if (pedestal) {
      pedestal.style.maxWidth = '1180px';
      pedestal.style.width = '98%';
    }
    if (metricsWrap) {
      metricsWrap.style.maxWidth = '100%';
      metricsWrap.style.margin = '24px 0 0';
    }
    if (groupLegacy) groupLegacy.style.display = 'flex';
    if (groupModern) groupModern.style.display = 'flex';
    if (centerDivider) centerDivider.style.display = 'block';
  });

  btnLegacy.addEventListener('click', () => {
    setActiveTab(btnLegacy);
    cardLegacy.style.display = 'flex';
    cardModern.style.display = 'none';
    grid.style.gridTemplateColumns = '1fr';
    grid.style.maxWidth = '960px';
    grid.style.margin = '0 auto';
    if (connector) connector.style.display = 'none';
    if (pedestal) {
      pedestal.style.maxWidth = '960px';
      pedestal.style.width = '100%';
    }
    if (metricsWrap) {
      metricsWrap.style.maxWidth = '960px';
      metricsWrap.style.margin = '24px auto 0';
    }
    if (groupLegacy) groupLegacy.style.display = 'flex';
    if (groupModern) groupModern.style.display = 'none';
    if (centerDivider) centerDivider.style.display = 'none';
  });

  btnModern.addEventListener('click', () => {
    setActiveTab(btnModern);
    cardLegacy.style.display = 'none';
    cardModern.style.display = 'flex';
    grid.style.gridTemplateColumns = '1fr';
    grid.style.maxWidth = '960px';
    grid.style.margin = '0 auto';
    if (connector) connector.style.display = 'none';
    if (pedestal) {
      pedestal.style.maxWidth = '960px';
      pedestal.style.width = '100%';
    }
    if (metricsWrap) {
      metricsWrap.style.maxWidth = '960px';
      metricsWrap.style.margin = '24px auto 0';
    }
    if (groupLegacy) groupLegacy.style.display = 'none';
    if (groupModern) groupModern.style.display = 'flex';
    if (centerDivider) centerDivider.style.display = 'none';
  });
}

/* ========================================================================= */
/* 3D INTERACTIVE WEBGL SPATIAL STOREFRONT CANVAS (THREE.JS)                 */
/* ========================================================================= */
function initTransformation3DCanvas() {
  // Retained as no-op for backward compatibility
}

/* ========================================================================= */
/* 3D TILT PHYSICS & DYNAMIC SPECULAR LIGHT ON TRANSFORMATION CARDS          */
/* ========================================================================= */
function initTransformation3DTilt() {
  const cards = document.querySelectorAll('.trans-card');
  if (!cards.length) return;

  cards.forEach(card => {
    const reflection = card.querySelector('.trans-card-reflection');

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      // Subtle tilt: 6 degrees max
      const rotateX = ((centerY - y) / centerY) * 6;
      const rotateY = ((x - centerX) / centerX) * 6;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;

      if (reflection) {
        reflection.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255, 255, 255, 0.45) 0%, transparent 60%)`;
      }
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initTransformationSwitcher();
  initTransformation3DCanvas();
  initTransformation3DTilt();
});
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  initTransformationSwitcher();
  initTransformation3DCanvas();
  initTransformation3DTilt();
}

// Interactive Pricing Billing Switcher (Monthly vs Quarterly Retainer)
function initPricingBillingToggle() {
  const toggleBtn = document.getElementById('pricingToggleBtn');
  const labelMonthly = document.getElementById('labelMonthly');
  const labelQuarterly = document.getElementById('labelQuarterly');
  const priceElements = document.querySelectorAll('.price-amount');
  if (!toggleBtn || !priceElements.length) return;

  let isQuarterly = false;

  function updatePrices(quarterly) {
    isQuarterly = quarterly;
    toggleBtn.classList.toggle('active', isQuarterly);
    if (labelMonthly) labelMonthly.classList.toggle('active', !isQuarterly);
    if (labelQuarterly) labelQuarterly.classList.toggle('active', isQuarterly);

    priceElements.forEach(el => {
      const val = isQuarterly ? el.getAttribute('data-quarterly') : el.getAttribute('data-monthly');
      if (val) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(-4px)';
        setTimeout(() => {
          el.textContent = val;
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        }, 150);
      }
    });
  }

  toggleBtn.addEventListener('click', () => updatePrices(!isQuarterly));
  if (labelMonthly) labelMonthly.addEventListener('click', () => updatePrices(false));
  if (labelQuarterly) labelQuarterly.addEventListener('click', () => updatePrices(true));
}

// Call on DOMContentLoaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPricingBillingToggle);
} else {
  initPricingBillingToggle();
}

/* ========================================================================== */
/* AWWWARDS-GRADE MOTION & INTERACTION SUITE (WEBFLIKR 2026)                 */
/* ========================================================================== */

// 1. Dynamic Rolling Counter Engine
function initAnimatedCounters() {
  const counterElements = document.querySelectorAll('[data-counter-target]');
  if (!counterElements.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        obs.unobserve(el);

        const target = parseFloat(el.getAttribute('data-counter-target') || '0');
        const prefix = el.getAttribute('data-counter-prefix') || '';
        const suffix = el.getAttribute('data-counter-suffix') || '';
        const decimals = parseInt(el.getAttribute('data-counter-decimals') || '0', 10);
        const duration = parseInt(el.getAttribute('data-counter-duration') || '1800', 10);

        let startTime = null;

        function animate(currentTime) {
          if (!startTime) startTime = currentTime;
          const progress = Math.min((currentTime - startTime) / duration, 1);
          // Ease out cubic
          const easeProgress = 1 - Math.pow(1 - progress, 3);
          const currentVal = target * easeProgress;

          el.textContent = `${prefix}${currentVal.toFixed(decimals)}${suffix}`;

          if (progress < 1) {
            requestAnimationFrame(animate);
          } else {
            el.textContent = `${prefix}${target.toFixed(decimals)}${suffix}`;
          }
        }

        requestAnimationFrame(animate);
      }
    });
  }, { threshold: 0.2 });

  counterElements.forEach(el => observer.observe(el));
}

// 2. Cursor Spotlight Sheen Engine
function initCardSpotlight() {
  const cards = document.querySelectorAll('.tilt-card, .kpi-card, .kpi-tactile-card, .bento-feature-wide, .bento-card-square, .work-card, .methodology-card, .bento-card, .scanner-terminal, .pricing-card');
  
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });
}

// 3. Magnetic CTA Button Proximity Suction
function initMagneticButtons() {
  const magneticBtns = document.querySelectorAll('.btn-primary, .btn-magnetic, .btn-audit-cta, .hero-btn-primary');
  
  magneticBtns.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      btn.style.transform = `translate(${x * 0.22}px, ${y * 0.22}px)`;
    });

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0px, 0px)';
      btn.style.transition = 'transform 0.4s cubic-bezier(0.25, 1, 0.5, 1)';
    });

    btn.addEventListener('mouseenter', () => {
      btn.style.transition = 'none';
    });
  });
}

// 4. Live Global Hub Clocks (New Delhi, London, Chicago, Singapore)
function initGlobalClocks() {
  const clockNodes = {
    'delhi-clock': 'Asia/Kolkata',
    'mumbai-clock': 'Asia/Kolkata',
    'london-clock': 'Europe/London',
    'chicago-clock': 'America/Chicago',
    'singapore-clock': 'Asia/Singapore'
  };

  function updateClocks() {
    const now = new Date();
    for (const [id, timeZone] of Object.entries(clockNodes)) {
      const el = document.getElementById(id);
      if (el) {
        try {
          const timeStr = now.toLocaleTimeString('en-US', {
            timeZone,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: true
          });
          el.textContent = timeStr;
        } catch (e) {
          // Fallback if timezone not supported
          el.textContent = now.toLocaleTimeString();
        }
      }
    }
  }

  updateClocks();
  setInterval(updateClocks, 1000);
}

// 5. Interactive SERP Diagnostic Terminal Simulation
function initInstantScannerSimulation() {
  const form = document.getElementById('scannerForm');
  const terminalLogs = document.getElementById('scannerTerminalLogs');
  const resultsCard = document.getElementById('scannerResultsCard');
  const scanBtn = document.getElementById('scannerSubmitBtn');
  const domainInput = document.getElementById('scannerDomainInput');

  if (!form || !scanBtn) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const domain = (domainInput && domainInput.value.trim()) || 'yourbrand.com';

    scanBtn.disabled = true;
    scanBtn.innerHTML = '<span>SCANNING IN REAL-TIME...</span> <i data-lucide="loader-2" class="spin-icon"></i>';
    if (window.lucide) lucide.createIcons();

    if (terminalLogs) {
      terminalLogs.style.display = 'block';
      terminalLogs.innerHTML = '';
    }
    if (resultsCard) {
      resultsCard.style.display = 'none';
    }

    const steps = [
      `[0.12s] Connecting to HTTP/3 edge nodes for https://${domain}...`,
      `[0.45s] DNS resolved. SSL certificate verified (TLS 1.3 encryption valid).`,
      `[0.82s] Measuring Core Web Vitals: LCP = 0.68s, INP = 18ms, CLS = 0.002. [PASS]`,
      `[1.24s] Parsing Semantic Schema Graphs: Organization, Product, FAQPage detected.`,
      `[1.65s] Evaluating AI Citation Index: 98.4% brand entity resonance in ChatGPT & Gemini.`,
      `[1.98s] Crawl Budget Efficiency: 99.6% indexation rate with zero 404 redirect chains.`,
      `[2.20s] Diagnostic complete! Rendering enterprise growth blueprint...`
    ];

    let stepIdx = 0;
    const interval = setInterval(() => {
      if (stepIdx < steps.length) {
        if (terminalLogs) {
          const logLine = document.createElement('div');
          logLine.className = 'terminal-log-line';
          logLine.textContent = steps[stepIdx];
          terminalLogs.appendChild(logLine);
          terminalLogs.scrollTop = terminalLogs.scrollHeight;
        }
        stepIdx++;
      } else {
        clearInterval(interval);
        scanBtn.disabled = false;
        scanBtn.innerHTML = '<span>DIAGNOSTIC COMPLETED</span> <i data-lucide="check-circle"></i>';
        if (window.lucide) lucide.createIcons();

        if (resultsCard) {
          resultsCard.style.display = 'block';
          resultsCard.style.animation = 'fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards';
          resultsCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }
    }, 320);
  });
}

// 6. Methodology Connected Circuit Stage Switcher
function initMethodologyCircuit() {
  const stageCards = document.querySelectorAll('.methodology-stage-card');
  if (!stageCards.length) return;

  stageCards.forEach((card, idx) => {
    card.addEventListener('mouseenter', () => {
      stageCards.forEach(c => c.classList.remove('active-stage'));
      card.classList.add('active-stage');

      const circuitSvg = document.getElementById('methodologyCircuitSvg');
      if (circuitSvg) {
        circuitSvg.setAttribute('data-active-stage', idx + 1);
      }
    });
  });
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
  initAnimatedCounters();
  initCardSpotlight();
  initMagneticButtons();
  initGlobalClocks();
  initInstantScannerSimulation();
  initMethodologyCircuit();
});

if (document.readyState === 'complete' || document.readyState === 'interactive') {
  initAnimatedCounters();
  initCardSpotlight();
  initMagneticButtons();
  initGlobalClocks();
  initInstantScannerSimulation();
  initMethodologyCircuit();
}
