/**
 * WEBFLIKR.COM - Real Interactive 3D & Smooth Animations (Vanilla JS)
 * - Three.js Floating Glossy 3D Geometric Scene reacting to mouse movement
 * - Smooth 3D Card Tilt Hover (perspective 1000px)
 * - GSAP ScrollTrigger Scroll-Reveal & Numerical Counters
 */

(function () {
  'use strict';

  // =========================================================================
  // 1. THREE.JS INTERACTIVE 3D FLOATING GEOMETRIC CANVAS
  // =========================================================================
  function initHeroThreeJS() {
    const stage = document.getElementById('hero3dStage') || document.querySelector('.hero-visual-col');
    if (!stage || typeof THREE === 'undefined') return;

    // Create Canvas if not already present
    let canvas = document.getElementById('heroInteractive3DCanvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'heroInteractive3DCanvas';
      canvas.className = 'hero-interactive-3d-canvas';
      stage.insertBefore(canvas, stage.firstChild);
    }

    const scene = new THREE.Scene();

    const getWidth = () => stage.clientWidth || 550;
    const getHeight = () => stage.clientHeight || 550;

    const camera = new THREE.PerspectiveCamera(45, getWidth() / getHeight(), 0.1, 1000);
    camera.position.z = 9;

    const renderer = new THREE.WebGLRenderer({
      canvas: canvas,
      alpha: true,
      antialias: true,
      powerPreference: 'high-performance'
    });
    renderer.setSize(getWidth(), getHeight());
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Studio Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
    scene.add(ambientLight);

    const keyLightOrange = new THREE.DirectionalLight(0xff5a1f, 1.8);
    keyLightOrange.position.set(5, 5, 4);
    scene.add(keyLightOrange);

    const fillLightSky = new THREE.DirectionalLight(0x0284c7, 1.2);
    fillLightSky.position.set(-5, -4, 3);
    scene.add(fillLightSky);

    const rimLightMint = new THREE.PointLight(0x10b981, 1.4, 25);
    rimLightMint.position.set(0, 4, -2);
    scene.add(rimLightMint);

    const goldPoint = new THREE.PointLight(0xfbbf24, 1.2, 20);
    goldPoint.position.set(-3, 3, 2);
    scene.add(goldPoint);

    // Group for mouse rotation
    const shapesGroup = new THREE.Group();
    scene.add(shapesGroup);

    // Shape 1: Main Glossy Brand Orange Torus Knot
    const knotGeo = new THREE.TorusKnotGeometry(1.35, 0.38, 120, 24);
    const knotMat = new THREE.MeshPhysicalMaterial({
      color: 0xff5a1f,
      roughness: 0.14,
      metalness: 0.1,
      clearcoat: 1.0,
      clearcoatRoughness: 0.08,
      reflectivity: 0.9,
      transmission: 0.15,
      ior: 1.5
    });
    const mainKnot = new THREE.Mesh(knotGeo, knotMat);
    mainKnot.position.set(0.2, 0.1, -1.0);
    shapesGroup.add(mainKnot);

    // Shape 2: Pastel Sky Blue Floating Glossy Sphere
    const sphereGeo = new THREE.SphereGeometry(0.65, 32, 32);
    const sphereMat = new THREE.MeshPhysicalMaterial({
      color: 0x38bdf8,
      roughness: 0.12,
      metalness: 0.05,
      clearcoat: 1.0,
      clearcoatRoughness: 0.05
    });
    const sphere = new THREE.Mesh(sphereGeo, sphereMat);
    sphere.position.set(-2.4, 1.8, 0.5);
    shapesGroup.add(sphere);

    // Shape 3: Pastel Mint Green Floating Torus Ring
    const torusGeo = new THREE.TorusGeometry(0.7, 0.22, 16, 40);
    const torusMat = new THREE.MeshPhysicalMaterial({
      color: 0x34d399,
      roughness: 0.15,
      metalness: 0.1,
      clearcoat: 1.0
    });
    const torus = new THREE.Mesh(torusGeo, torusMat);
    torus.position.set(2.5, -1.6, 0.8);
    torus.rotation.x = Math.PI / 3;
    shapesGroup.add(torus);

    // Shape 4: Warm Yellow / Gold Octahedron
    const octaGeo = new THREE.OctahedronGeometry(0.55, 0);
    const octaMat = new THREE.MeshPhysicalMaterial({
      color: 0xfbbf24,
      roughness: 0.1,
      metalness: 0.15,
      clearcoat: 1.0
    });
    const octa = new THREE.Mesh(octaGeo, octaMat);
    octa.position.set(2.4, 1.9, -0.2);
    shapesGroup.add(octa);

    // Shape 5: Soft Coral Satellite Sphere
    const coralGeo = new THREE.SphereGeometry(0.4, 28, 28);
    const coralMat = new THREE.MeshPhysicalMaterial({
      color: 0xff8c66,
      roughness: 0.18,
      clearcoat: 0.9
    });
    const coralSphere = new THREE.Mesh(coralGeo, coralMat);
    coralSphere.position.set(-2.0, -1.9, 0.4);
    shapesGroup.add(coralSphere);

    // Mouse Interaction
    let mouseX = 0;
    let mouseY = 0;
    let targetRotX = 0;
    let targetRotY = 0;

    window.addEventListener('mousemove', (e) => {
      const halfW = window.innerWidth / 2;
      const halfH = window.innerHeight / 2;
      mouseX = (e.clientX - halfW) / halfW;
      mouseY = (e.clientY - halfH) / halfH;
    });

    // Resize
    window.addEventListener('resize', () => {
      const w = getWidth();
      const h = getHeight();
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });

    // Animation Loop
    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const time = clock.getElapsedTime();

      // Smooth mouse damping
      targetRotX += (mouseY * 0.45 - targetRotX) * 0.05;
      targetRotY += (mouseX * 0.55 - targetRotY) * 0.05;

      shapesGroup.rotation.x = targetRotX;
      shapesGroup.rotation.y = targetRotY;

      // Idle floating oscillations
      mainKnot.rotation.x = time * 0.35;
      mainKnot.rotation.y = time * 0.45;
      mainKnot.position.y = 0.1 + Math.sin(time * 1.5) * 0.12;

      sphere.position.y = 1.8 + Math.cos(time * 1.8) * 0.18;
      sphere.rotation.y = time * 0.3;

      torus.position.y = -1.6 + Math.sin(time * 1.6) * 0.15;
      torus.rotation.z = time * 0.4;

      octa.position.y = 1.9 + Math.sin(time * 2.0) * 0.14;
      octa.rotation.x = time * 0.6;
      octa.rotation.y = time * 0.5;

      coralSphere.position.y = -1.9 + Math.cos(time * 1.4) * 0.12;

      renderer.render(scene, camera);
    }

    animate();
  }

  // =========================================================================
  // 2. SMOOTH 3D TILT HOVER EFFECT ON CARDS
  // =========================================================================
  function init3DCardTilt() {
    const tiltCards = document.querySelectorAll(
      '.tilt-card, .glass-card-3d, .kpi-cockpit-card, .modern-bento-card, .framework-step-card, .showcase-stat-pill, .tech-standard-card'
    );

    tiltCards.forEach((card) => {
      card.style.transition = 'transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease';

      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const cardX = e.clientX - rect.left;
        const cardY = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = -((cardY - centerY) / centerY) * 8; // max 8 deg
        const rotateY = ((cardX - centerX) / centerX) * 8;

        card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) scale3d(1.02, 1.02, 1.02)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
      });
    });
  }

  // =========================================================================
  // 3. GSAP SCROLLTRIGGER SCROLL-REVEAL & NUMERICAL COUNTERS
  // =========================================================================
  function initGSAPAnimations() {
    if (typeof gsap === 'undefined') return;

    if (typeof ScrollTrigger !== 'undefined') {
      gsap.registerPlugin(ScrollTrigger);
    }

    // Scroll reveal on modern cards
    const revealTargets = document.querySelectorAll(
      '.modern-bento-card, .framework-step-card, .tech-standard-card, .kpi-cockpit-card, .portfolio-showcase-canvas'
    );

    revealTargets.forEach((el, index) => {
      if (typeof ScrollTrigger !== 'undefined') {
        gsap.from(el, {
          scrollTrigger: {
            trigger: el,
            start: 'top 88%',
            toggleActions: 'play none none none'
          },
          y: 35,
          opacity: 0,
          duration: 0.75,
          ease: 'power2.out',
          delay: (index % 4) * 0.08
        });
      }
    });

    // Numerical counter animations
    const counterElements = document.querySelectorAll(
      '.modern-stat-num, .cockpit-main-val, .showcase-stat-val'
    );

    counterElements.forEach((el) => {
      const text = el.innerText.trim();
      const numMatch = text.match(/([0-9]+(?:\.[0-9]+)?)/);
      if (!numMatch) return;

      const targetNum = parseFloat(numMatch[1]);
      const prefix = text.startsWith('+') ? '+' : text.startsWith('$') ? '$' : '';
      const suffix = text.includes('%') ? '%' : text.includes('+') && !text.startsWith('+') ? '+' : text.includes('s') ? 's' : text.includes('x') ? 'x' : text.includes('M') ? 'M' : '';
      const decimals = numMatch[1].includes('.') ? numMatch[1].split('.')[1].length : 0;

      if (typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.create({
          trigger: el,
          start: 'top 90%',
          once: true,
          onEnter: () => {
            let obj = { val: 0 };
            gsap.to(obj, {
              val: targetNum,
              duration: 1.6,
              ease: 'power2.out',
              onUpdate: () => {
                el.innerText = `${prefix}${obj.val.toFixed(decimals)}${suffix}`;
              }
            });
          }
        });
      }
    });
  }

  // Initialize on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initHeroThreeJS();
      init3DCardTilt();
      initGSAPAnimations();
    });
  } else {
    initHeroThreeJS();
    init3DCardTilt();
    initGSAPAnimations();
  }
})();
