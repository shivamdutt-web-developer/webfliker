hero_3d_css = '''
/* ==========================================================================
   ADVANCED INTERACTIVE 3D GLASSMORPHISM & PARALLAX HERO STAGE
   ========================================================================== */
.hero-3d-stage {
  position: relative;
  width: 100%;
  max-width: 580px;
  min-height: 520px;
  margin: 0 auto;
  perspective: 1400px;
  perspective-origin: 50% 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  cursor: pointer;
}

.hero-3d-ambient-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 480px;
  height: 480px;
  background: radial-gradient(circle, rgba(255, 94, 30, 0.28) 0%, rgba(255, 123, 57, 0.12) 40%, transparent 70%);
  filter: blur(55px);
  pointer-events: none;
  z-index: 0;
  transition: transform 0.5s ease, opacity 0.5s ease;
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

/* 1. Base 3D Smartphone Hardware */
.phone-3d-chassis {
  position: relative;
  width: 320px;
  height: 480px;
  border-radius: 44px;
  background: linear-gradient(145deg, #1e2430 0%, #0d111a 100%);
  padding: 8px;
  box-shadow: 
    0 0 0 2px rgba(255, 255, 255, 0.1),
    0 25px 60px rgba(0, 0, 0, 0.55),
    0 0 40px rgba(255, 94, 30, 0.22);
  transform-style: preserve-3d;
  will-change: transform, box-shadow;
  transition: box-shadow 0.4s ease;
  z-index: 1;
}

.phone-titanium-bezel {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 38px;
  background: #090c14;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  flex-direction: column;
}

.phone-dynamic-island {
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  width: 90px;
  height: 22px;
  background: #000000;
  border-radius: 20px;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 10px;
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
  padding: 34px 18px 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.app-brand-title {
  font-size: 0.72rem;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 0.06em;
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
  font-size: 0.68rem;
  font-weight: 700;
  background: rgba(255, 94, 30, 0.18);
  color: #ff7b39;
  border: 1px solid rgba(255, 94, 30, 0.3);
  padding: 1px 6px;
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
  opacity: 0.9;
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

.kpi-micro-label {
  display: block;
  font-size: 0.6rem;
  font-weight: 700;
  color: #64748b;
  margin-bottom: 2px;
}

.kpi-micro-val {
  display: block;
  font-size: 0.85rem;
  font-weight: 800;
  color: #ffffff;
}

.border-both {
  border-left: 1px solid rgba(255, 255, 255, 0.08);
  border-right: 1px solid rgba(255, 255, 255, 0.08);
}

/* 2. Floating 3D Glassmorphism Cards */
.glass-card-3d {
  position: absolute;
  border-radius: 16px;
  background: rgba(15, 23, 42, 0.82);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 255, 255, 0.16);
  box-shadow: 
    0 16px 36px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(255, 94, 30, 0.12);
  transform-style: preserve-3d;
  will-change: transform;
  pointer-events: auto;
  transition: box-shadow 0.35s ease, border-color 0.35s ease;
}

.glass-card-3d:hover {
  border-color: rgba(255, 94, 30, 0.45);
  box-shadow: 
    0 22px 45px rgba(0, 0, 0, 0.45),
    0 0 28px rgba(255, 94, 30, 0.25);
}

/* Layer 1: Search Bar */
.layer-search-bar {
  top: 60px;
  left: -20px;
  width: 280px;
  padding: 8px 14px;
  border-radius: 999px;
  z-index: 5;
}

.glass-search-inner {
  display: flex;
  align-items: center;
  gap: 8px;
}

.search-lens-icon {
  font-size: 0.85rem;
}

.search-input-placeholder {
  flex: 1;
  font-size: 0.72rem;
  color: #cbd5e1;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.search-verified-pill {
  font-size: 0.62rem;
  font-weight: 800;
  color: #10b981;
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.3);
  padding: 2px 7px;
  border-radius: 999px;
  white-space: nowrap;
}

/* Layer 2: Sales & Revenue Card */
.layer-sales-card {
  top: 135px;
  right: -30px;
  width: 230px;
  padding: 12px 14px;
  z-index: 6;
}

.sales-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.card-micro-title {
  font-size: 0.62rem;
  color: #94a3b8;
  font-weight: 700;
  text-transform: uppercase;
}

.card-macro-val {
  font-size: 1.15rem;
  font-weight: 800;
  color: #ffffff;
}

.trend-badge {
  font-size: 0.7rem;
  font-weight: 700;
  color: #ff5e1e;
}

.circular-progress-badge {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2.5px solid #ff5e1e;
  border-top-color: #38bdf8;
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-num {
  font-size: 0.65rem;
  font-weight: 800;
  color: #ffffff;
}

.mini-bar-chart {
  display: flex;
  align-items: flex-end;
  gap: 6px;
  height: 40px;
  padding-top: 6px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.bar-col {
  flex: 1;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  gap: 3px;
}

.bar-fill {
  width: 100%;
  border-radius: 3px;
  background: linear-gradient(180deg, #ff7b39 0%, #ff5e1e 100%);
  display: block;
}

.bar-col .active-bar {
  background: linear-gradient(180deg, #38bdf8 0%, #0284c7 100%);
  box-shadow: 0 0 6px #38bdf8;
}

.bar-day {
  font-size: 0.55rem;
  color: #64748b;
  font-weight: 700;
}

/* Layer 3: Product Card */
.layer-product-card {
  bottom: 85px;
  left: -25px;
  width: 220px;
  padding: 10px 14px;
  z-index: 7;
}

.prod-card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}

.prod-badge {
  font-size: 0.58rem;
  font-weight: 800;
  color: #ff7b39;
  letter-spacing: 0.04em;
}

.prod-rating {
  font-size: 0.65rem;
  color: #f59e0b;
  font-weight: 700;
}

.prod-card-mid {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.prod-title {
  font-size: 0.78rem;
  font-weight: 800;
  color: #ffffff;
}

.prod-price {
  font-size: 0.72rem;
  color: #10b981;
  font-weight: 700;
}

.prod-stock {
  font-size: 0.6rem;
  color: #94a3b8;
  font-weight: 600;
}

.prod-quick-btn {
  background: linear-gradient(135deg, #ff5e1e, #ff3b00);
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 4px 10px;
  font-size: 0.68rem;
  font-weight: 800;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 3px;
  box-shadow: 0 3px 10px rgba(255, 94, 30, 0.35);
  transition: transform 0.2s ease;
}

.prod-quick-btn:hover {
  transform: scale(1.05);
}

/* Layer 4: Rank #1 Shield Badge */
.layer-rank-badge {
  top: -15px;
  left: 30px;
  padding: 8px 16px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  z-index: 8;
}

.rank-shield-icon {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  background: rgba(16, 185, 129, 0.18);
  color: #10b981;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 0.85rem;
}

.rank-main-title {
  font-size: 0.78rem;
  font-weight: 800;
  color: #ffffff;
}

.rank-sub-title {
  font-size: 0.64rem;
  color: #94a3b8;
}

.live-pulse-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
  animation: pulseLight 2s infinite;
}

@keyframes pulseLight {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}

/* Layer 5: Total Revenue Card */
.layer-revenue-card {
  bottom: 25px;
  right: -20px;
  width: 170px;
  padding: 10px 14px;
  z-index: 7;
}

.rev-card-label {
  font-size: 0.6rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
}

.rev-card-num {
  font-size: 1.15rem;
  font-weight: 800;
  color: #ffffff;
  margin: 2px 0;
}

.rev-trend-wave {
  width: 100%;
  height: 18px;
  display: block;
}

/* Mobile & Touch Fallbacks */
@media (max-width: 768px) {
  .hero-3d-stage {
    max-width: 100%;
    min-height: 460px;
    perspective: 1000px;
  }
  .phone-3d-chassis {
    width: 270px;
    height: 420px;
  }
  .layer-sales-card {
    right: -10px;
    width: 190px;
  }
  .layer-search-bar {
    left: -5px;
    width: 240px;
  }
  .layer-product-card {
    left: -10px;
    width: 190px;
  }
  .layer-revenue-card {
    right: -10px;
    width: 140px;
  }
  .layer-rank-badge {
    left: 10px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hero-3d-scene,
  .glass-card-3d,
  .phone-3d-chassis {
    transform: none !important;
    transition: none !important;
  }
}
'''

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.hero-3d-stage' not in css:
    css += '\n' + hero_3d_css
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Successfully added 3D glassmorphism hero CSS")
else:
    print("3D glassmorphism hero CSS already exists")
