css_patch = '''
/* ==========================================================================
   POLISHED 3-ELEMENT 3D HERO COMPOSITION (REFERENCE 1 & 2 PARITY)
   ========================================================================== */
.hero-section {
  position: relative;
  min-height: 88vh;
  display: flex;
  align-items: center;
  overflow: hidden;
  padding: 60px 0 80px;
  background: 
    radial-gradient(circle at 82% 38%, rgba(255, 94, 30, 0.09) 0%, transparent 60%),
    radial-gradient(circle at 18% 60%, rgba(255, 123, 57, 0.05) 0%, transparent 50%),
    #fafaf9;
}

.hero-title {
  font-family: var(--font-display, "Plus Jakarta Sans", sans-serif);
  font-size: clamp(2.7rem, 4.8vw, 4.1rem);
  font-weight: 800;
  line-height: 1.14;
  letter-spacing: -0.035em;
  color: #0f172a;
  margin-bottom: 24px;
}

.hero-title .serif-italic {
  font-family: var(--font-serif, "Playfair Display", Georgia, serif);
  font-style: italic;
  font-weight: 700;
  color: #ff5e1e;
  letter-spacing: -0.01em;
}

.hero-subtitle {
  font-size: 1.12rem;
  line-height: 1.72;
  color: #475569;
  max-width: 620px;
  margin-bottom: 30px;
}

.hero-pillars-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px 24px;
  margin-bottom: 36px;
}

.hero-pillar-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.95rem;
  font-weight: 600;
  color: #1e293b;
}

.hero-actions {
  display: flex;
  gap: 16px;
  align-items: center;
  flex-wrap: wrap;
}

.hero-actions .btn-primary {
  padding: 16px 36px;
  font-size: 0.96rem;
  font-weight: 800;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(255, 94, 30, 0.35);
}

.hero-actions .btn-secondary {
  padding: 16px 32px;
  font-size: 0.96rem;
  font-weight: 700;
  border-radius: 12px;
}

/* 3D Stage & Lighting */
.hero-3d-stage {
  position: relative;
  width: 100%;
  max-width: 540px;
  min-height: 540px;
  margin: 0 auto;
  perspective: 1400px;
  perspective-origin: 50% 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  cursor: pointer;
  pointer-events: auto;
}

.hero-3d-ambient-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 440px;
  height: 440px;
  background: radial-gradient(circle, rgba(255, 94, 30, 0.22) 0%, rgba(255, 123, 57, 0.08) 45%, transparent 70%);
  filter: blur(50px);
  pointer-events: none;
  z-index: 0;
  transition: transform 0.4s ease, opacity 0.4s ease;
}

.hero-3d-scene {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transform-style: preserve-3d;
  will-change: transform;
  transform: rotateY(-6deg) rotateX(4deg);
}

/* 3D Smartphone Hardware */
.phone-3d-chassis {
  position: relative;
  width: 335px;
  height: 510px;
  border-radius: 46px;
  background: linear-gradient(145deg, #2b3345 0%, #111622 100%);
  padding: 9px;
  box-shadow: 
    0 0 0 1px rgba(255, 255, 255, 0.15),
    0 35px 80px -15px rgba(15, 23, 42, 0.48),
    0 0 45px rgba(255, 94, 30, 0.16);
  transform-style: preserve-3d;
  will-change: transform, box-shadow;
  transition: box-shadow 0.4s ease;
  z-index: 1;
}

.phone-titanium-bezel {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 39px;
  background: #090c14;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  flex-direction: column;
}

.phone-dynamic-island {
  position: absolute;
  top: 11px;
  left: 50%;
  transform: translateX(-50%);
  width: 94px;
  height: 23px;
  background: #000000;
  border-radius: 20px;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 11px;
}

.island-camera {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #111827;
  border: 1.5px solid #1f2937;
}

.island-sensor {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #064e3b;
  box-shadow: 0 0 4px #10b981;
}

.phone-screen-content {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: radial-gradient(circle at 50% 30%, #151b28 0%, #080b12 100%);
}

.screen-app-bar {
  padding: 36px 18px 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.app-brand-title {
  font-size: 0.72rem;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 0.05em;
}

.app-bar-icons {
  display: flex;
  align-items: center;
  gap: 8px;
}

.app-signal-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 6px #10b981;
}

.app-cart-pill {
  font-size: 0.65rem;
  font-weight: 700;
  background: rgba(255, 94, 30, 0.16);
  color: #ff7b39;
  border: 1px solid rgba(255, 94, 30, 0.3);
  padding: 2px 7px;
  border-radius: 999px;
}

.screen-hero-art {
  position: relative;
  flex: 1;
  overflow: hidden;
}

.screen-base-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: 0.92;
}

.glass-light-sheen {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(circle at var(--sheen-x, 50%) var(--sheen-y, 50%), rgba(255, 255, 255, 0.22) 0%, transparent 60%);
  mix-blend-mode: overlay;
  transition: opacity 0.3s ease;
}

.screen-status-ribbon {
  padding: 10px 14px;
  background: rgba(12, 16, 26, 0.95);
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  text-align: center;
}

/* Focused 3 Floating Cards (Consistent Dark Luxury Glass) */
.glass-card-3d {
  position: absolute;
  border-radius: 18px;
  background: rgba(11, 16, 29, 0.88);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.4),
    0 0 24px rgba(255, 94, 30, 0.12);
  transform-style: preserve-3d;
  will-change: transform;
  pointer-events: auto;
  transition: box-shadow 0.35s ease, border-color 0.35s ease;
}

.glass-card-3d:hover {
  border-color: rgba(255, 94, 30, 0.45);
  box-shadow: 
    0 26px 50px rgba(0, 0, 0, 0.5),
    0 0 32px rgba(255, 94, 30, 0.25);
}

/* Element 1: Upper-Left Rank Badge */
.polished-rank-badge {
  top: 15px;
  left: -20px;
  padding: 10px 18px;
  display: flex;
  align-items: center;
  gap: 12px;
  z-index: 6;
}

.rank-shield-icon {
  width: 32px;
  height: 32px;
  border-radius: 9px;
  background: rgba(16, 185, 129, 0.18);
  border: 1px solid rgba(16, 185, 129, 0.35);
  color: #10b981;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 0.95rem;
}

.rank-main-title {
  font-size: 0.84rem;
  font-weight: 800;
  color: #ffffff;
}

.rank-sub-title {
  font-size: 0.68rem;
  color: #94a3b8;
  font-weight: 600;
}

.live-pulse-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
  animation: pulseLight 2s infinite;
}

/* Element 2: Upper-Right Revenue Card */
.polished-revenue-card {
  top: 75px;
  right: -30px;
  width: 240px;
  padding: 14px 18px;
  z-index: 7;
}

.polished-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.card-micro-label {
  font-size: 0.64rem;
  font-weight: 700;
  color: #94a3b8;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.card-macro-val {
  font-size: 1.25rem;
  font-weight: 800;
  color: #ffffff;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 3px;
}

.trend-badge-orange {
  font-size: 0.7rem;
  font-weight: 700;
  color: #ff5e1e;
  background: rgba(255, 94, 30, 0.15);
  border: 1px solid rgba(255, 94, 30, 0.3);
  padding: 1px 7px;
  border-radius: 999px;
}

.trend-badge-cyan {
  font-size: 0.68rem;
  font-weight: 700;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.15);
  border: 1px solid rgba(56, 189, 248, 0.3);
  padding: 1px 7px;
  border-radius: 999px;
}

.spark-icon-wrap {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  background: rgba(255, 94, 30, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
}

.revenue-sparkline-svg {
  width: 100%;
  height: 38px;
  display: block;
}

/* Element 3: Lower-Right AI Visibility Card */
.polished-ai-card {
  bottom: 50px;
  right: -25px;
  width: 235px;
  padding: 14px 18px;
  z-index: 6;
}

.ai-live-pill {
  font-size: 0.65rem;
  font-weight: 700;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.14);
  padding: 2px 8px;
  border-radius: 999px;
}

.ai-knowledge-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.72rem;
  font-weight: 600;
  color: #cbd5e1;
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.meta-dot-pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #38bdf8;
  box-shadow: 0 0 6px #38bdf8;
}

/* Responsive Rules */
@media (max-width: 1024px) {
  .hero-3d-stage {
    max-width: 480px;
  }
  .phone-3d-chassis {
    width: 300px;
    height: 470px;
  }
  .polished-revenue-card {
    right: -10px;
    width: 210px;
  }
  .polished-ai-card {
    right: -10px;
    width: 210px;
  }
  .polished-rank-badge {
    left: -5px;
  }
}

@media (max-width: 768px) {
  .hero-3d-stage {
    max-width: 100%;
    min-height: 480px;
    perspective: 1000px;
  }
  .phone-3d-chassis {
    width: 280px;
    height: 440px;
  }
  .polished-revenue-card {
    right: 0px;
    top: 50px;
    width: 190px;
  }
  .polished-ai-card {
    right: 0px;
    bottom: 25px;
    width: 190px;
  }
  .polished-rank-badge {
    left: 0px;
    top: 5px;
  }
}
'''

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace or append
marker = '/* ==========================================================================\n   ADVANCED INTERACTIVE 3D GLASSMORPHISM & PARALLAX HERO STAGE'
if marker in css:
    css = css[:css.find(marker)] + css_patch
else:
    css += '\n' + css_patch

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Successfully updated styles.css with polished 3-element composition styles")
