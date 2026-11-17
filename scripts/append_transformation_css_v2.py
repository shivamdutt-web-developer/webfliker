css_code = '''
/* ========================================================================= */
/* REDESIGNED TRANSFORMATION SHOWCASE (EXACT 3D REFERENCE FIDELITY)          */
/* ========================================================================= */
.transformation-showcase-section,
body.theme-light .transformation-showcase-section {
  position: relative !important;
  background: #fdfbf7 !important;
  color: #0f172a !important;
  padding: 100px 0 90px !important;
  overflow: hidden !important;
  border-top: 1px solid rgba(15, 23, 42, 0.05) !important;
  border-bottom: 1px solid rgba(15, 23, 42, 0.05) !important;
  width: 100% !important;
}

/* Ambient Radial Lighting on Canvas */
.transformation-showcase-section::before {
  content: "";
  position: absolute;
  top: 15%;
  left: 50%;
  transform: translateX(-50%);
  width: 900px;
  height: 600px;
  background: radial-gradient(ellipse at center, rgba(255, 140, 80, 0.12) 0%, rgba(255, 220, 200, 0.05) 50%, transparent 75%);
  pointer-events: none;
  z-index: 1;
}

/* Floating 3D Torus Rings in Background */
.trans-3d-bg-element {
  position: absolute;
  pointer-events: none;
  z-index: 1;
}
.torus-top-left {
  top: 50px;
  left: calc(50% - 620px);
  width: 140px;
  height: 140px;
  animation: floatTorusLeft 8s ease-in-out infinite;
}
.torus-top-right {
  top: 40px;
  right: calc(50% - 630px);
  width: 160px;
  height: 160px;
  animation: floatTorusRight 9s ease-in-out infinite;
}

@keyframes floatTorusLeft {
  0%, 100% { transform: translateY(0px) rotate(-15deg); }
  50% { transform: translateY(-16px) rotate(-8deg); }
}
@keyframes floatTorusRight {
  0%, 100% { transform: translateY(0px) rotate(25deg); }
  50% { transform: translateY(-18px) rotate(32deg); }
}

.trans-content-container {
  position: relative;
  z-index: 3;
}

/* Stage Wrapper & Center Connector */
.trans-stage-wrapper {
  position: relative;
  margin-bottom: 24px;
}

.trans-center-connector {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 15;
  pointer-events: none;
  display: flex;
  align-items: center;
  justify-content: center;
}
.trans-energy-trail-svg {
  position: absolute;
  width: 220px;
  height: 80px;
  top: -15px;
  left: -80px;
  overflow: visible;
  opacity: 0.95;
  pointer-events: none;
}
.trans-center-disc {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #ffffff 0%, #fff7ed 60%, #ffedd5 100%);
  border: 2.5px solid #ff7a18;
  box-shadow: 0 0 25px rgba(255, 122, 24, 0.45), 0 8px 20px rgba(15, 23, 42, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  animation: pulseCenterDisc 3s ease-in-out infinite;
  pointer-events: auto;
}
@keyframes pulseCenterDisc {
  0%, 100% { transform: scale(1); box-shadow: 0 0 25px rgba(255, 122, 24, 0.45), 0 8px 20px rgba(15, 23, 42, 0.12); }
  50% { transform: scale(1.06); box-shadow: 0 0 38px rgba(255, 122, 24, 0.75), 0 10px 25px rgba(15, 23, 42, 0.16); }
}

/* 3D Oval Podium Pedestal Underneath Cards */
.trans-stage-pedestal {
  position: absolute;
  bottom: -16px;
  left: 50%;
  transform: translateX(-50%);
  width: 98%;
  max-width: 1160px;
  height: 38px;
  pointer-events: none;
  z-index: 1;
}
.pedestal-disc-surface {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: linear-gradient(180deg, #fcefe9 0%, #f6ded5 100%);
  border: 1.5px solid rgba(255, 140, 100, 0.35);
  box-shadow: 0 25px 60px rgba(255, 94, 30, 0.15), 0 10px 30px rgba(15, 23, 42, 0.08);
}

/* 2-Column Inside Card Layout */
.trans-card-inner-split {
  display: grid;
  grid-template-columns: 190px 1fr;
  gap: 20px;
  align-items: center;
  margin-top: 18px;
}

.trans-3d-visual-pane {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
}
.trans-isometric-svg {
  width: 100%;
  height: auto;
  max-height: 215px;
  filter: drop-shadow(0 10px 15px rgba(0,0,0,0.06));
}

/* Floating Animations for SVG 3D Nodes */
.floating-3d-node.wp-node {
  animation: floatNodeWP 4s ease-in-out infinite;
}
@keyframes floatNodeWP {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-6px); }
}
.floating-3d-node.warn-node {
  animation: floatNodeWarn 3.5s ease-in-out infinite;
}
@keyframes floatNodeWarn {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-4px) scale(1.03); }
}
.floating-3d-node.shopify-bag-node {
  animation: floatNodeShopify 4.5s ease-in-out infinite;
}
@keyframes floatNodeShopify {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-7px); }
}
.tech-slab {
  transition: transform 0.35s cubic-bezier(0.2, 0, 0.2, 1);
}
.trans-card-modern:hover .slab-nextjs { transform: translateY(-4px); }
.trans-card-modern:hover .slab-webgl { transform: translateY(-2px); }

/* Breakdown Checklists */
.trans-breakdown-pane {
  display: flex;
  flex-direction: column;
}
.trans-check-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 16px;
}
.trans-check-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.82rem;
  font-weight: 700;
  line-height: 1.35;
}
.trans-check-item.item-fail {
  color: #1e293b;
}
.trans-check-item.item-pass {
  color: #f1f5f9;
}
.check-icon {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 900;
  flex-shrink: 0;
}
.icon-fail {
  background: #ef4444;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(239, 68, 68, 0.35);
}
.icon-pass {
  background: #10b981;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
}

/* 12-Month Mini Graph Cards */
.trans-graph-card {
  border-radius: 14px;
  padding: 12px 14px;
}
.graph-card-legacy {
  background: #ffffff;
  border: 1.5px solid #e2e8f0;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
}
.graph-card-modern {
  background: rgba(10, 16, 30, 0.9);
  border: 1.5px solid rgba(16, 185, 129, 0.5);
  box-shadow: inset 0 0 15px rgba(16, 185, 129, 0.08), 0 4px 14px rgba(0, 0, 0, 0.2);
}
.graph-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}
.graph-meta-title {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  color: #64748b;
  text-transform: uppercase;
}
.graph-card-modern .graph-meta-title {
  color: #94a3b8;
}
.graph-meta-badge {
  font-size: 0.76rem;
  font-weight: 800;
}
.badge-down { color: #ef4444; }
.badge-up { color: #10b981; }

.trans-mini-chart {
  width: 100%;
  height: 40px;
  display: block;
}

/* Symmetrical Bottom Metrics Bar */
.trans-bottom-metrics-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #ffffff;
  border: 1.5px solid #e2e8f0;
  border-radius: 20px;
  padding: 18px 30px;
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.05);
  margin-top: 24px;
  position: relative;
  z-index: 5;
}
.trans-metrics-col-group {
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex: 1;
  gap: 20px;
}
.trans-metrics-center-divider {
  width: 2px;
  height: 38px;
  background: linear-gradient(180deg, rgba(255, 94, 30, 0.2) 0%, rgba(255, 140, 50, 0.8) 50%, rgba(255, 94, 30, 0.2) 100%);
  margin: 0 24px;
}

/* Modern Card Custom Radiant Rim */
.trans-card-modern {
  background: #090e1a !important;
  border: 3px solid #ff7a18 !important;
  box-shadow: 0 0 45px rgba(255, 94, 30, 0.35), 0 25px 65px -10px rgba(0, 0, 0, 0.6) !important;
}
.highlight-orange {
  color: #ff7a18;
  background: linear-gradient(135deg, #ff7a18 0%, #ea580c 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Tablet & Mobile Responsiveness */
@media (max-width: 1200px) {
  .trans-card-inner-split {
    grid-template-columns: 160px 1fr;
    gap: 14px;
  }
}

@media (max-width: 991px) {
  .trans-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 40px !important;
  }
  .trans-center-connector {
    display: none !important;
  }
  .torus-top-left, .torus-top-right {
    display: none !important;
  }
  .trans-bottom-metrics-wrap {
    flex-direction: column !important;
    gap: 20px !important;
    padding: 20px !important;
  }
  .trans-metrics-col-group {
    width: 100% !important;
  }
  .trans-metrics-center-divider {
    width: 100% !important;
    height: 1px !important;
    margin: 8px 0 !important;
  }
}

@media (max-width: 580px) {
  .trans-card-inner-split {
    grid-template-columns: 1fr !important;
  }
  .trans-3d-visual-pane {
    max-width: 180px;
    margin: 0 auto 12px;
  }
  .trans-metrics-col-group {
    flex-direction: column !important;
    gap: 12px !important;
  }
  .trans-metric-box {
    width: 100% !important;
    text-align: center !important;
  }
}
'''

with open('styles.css', 'r', encoding='utf-8') as f:
    orig_css = f.read()

# Append to styles.css
with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_code)

print("Successfully appended updated CSS to styles.css!")
