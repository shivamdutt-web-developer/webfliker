stitch_css = """
/* ==========================================================================
   GOOGLE STITCH DESIGN SYSTEM & 3D INTERACTION OVERHAUL (FULL HOMEPAGE)
   ========================================================================== */

/* 1. Global Stitch Design Tokens & Atmosphere */
:root {
  --stitch-bg-dark: #070b14;
  --stitch-surface-card: rgba(13, 21, 39, 0.72);
  --stitch-surface-card-hover: rgba(18, 28, 52, 0.85);
  --stitch-border-glass: rgba(255, 255, 255, 0.08);
  --stitch-border-hover: rgba(255, 94, 30, 0.42);
  --stitch-accent-orange: #ff5e1e;
  --stitch-accent-glow: rgba(255, 94, 30, 0.28);
  --stitch-accent-emerald: #10b981;
  --stitch-text-primary: #ffffff;
  --stitch-text-secondary: #94a3b8;
  --stitch-text-muted: #64748b;
  --stitch-shadow-card: 0 16px 36px -10px rgba(0, 0, 0, 0.45);
  --stitch-shadow-glow: 0 0 35px rgba(255, 94, 30, 0.22);
  --stitch-bevel-inner: inset 0 1px 0 rgba(255, 255, 255, 0.12);
}

/* 2. Global Stitch 3D Card Behavior & Perspective */
.mobikasa-signature-card,
.kpi-card,
.process-step-card,
.phase-item-card,
.price-card,
.pricing-card,
.work-card,
.bento-card-square,
.lighthouse-benchmark-card,
.bento-perf-card,
.testimonial-card,
.review-card,
.blog-card,
.insight-card,
.office-card,
.global-office-card,
.stitch-3d-card {
  background: var(--stitch-surface-card) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border: 1px solid var(--stitch-border-glass) !important;
  box-shadow: var(--stitch-shadow-card), var(--stitch-bevel-inner) !important;
  border-radius: 20px !important;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), 
              box-shadow 0.25s cubic-bezier(0.16, 1, 0.3, 1), 
              border-color 0.25s ease !important;
  will-change: transform, box-shadow;
}

.mobikasa-signature-card:hover,
.kpi-card:hover,
.process-step-card:hover,
.phase-item-card:hover,
.price-card:hover,
.pricing-card:hover,
.work-card:hover,
.bento-card-square:hover,
.lighthouse-benchmark-card:hover,
.bento-perf-card:hover,
.testimonial-card:hover,
.review-card:hover,
.blog-card:hover,
.insight-card:hover,
.office-card:hover,
.global-office-card:hover,
.stitch-3d-card:hover {
  border-color: var(--stitch-border-hover) !important;
  box-shadow: 0 24px 55px -10px rgba(0, 0, 0, 0.65), 
              var(--stitch-shadow-glow), 
              var(--stitch-bevel-inner) !important;
}

/* 3. Hero Section Stitch 3D Spatial Aura */
.hero-section {
  position: relative;
  overflow: hidden;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: -15%;
  left: 50%;
  transform: translateX(-50%);
  width: 900px;
  height: 550px;
  background: radial-gradient(ellipse at center, rgba(255, 94, 30, 0.16) 0%, rgba(13, 21, 39, 0.05) 50%, transparent 75%);
  pointer-events: none;
  z-index: 0;
  filter: blur(60px);
}

.hero-title .gradient-text,
.hero-title strong {
  background: linear-gradient(135deg, #ffffff 30%, #ff8c42 75%, #ff5e1e 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  text-shadow: 0 0 30px rgba(255, 94, 30, 0.25);
}

/* 4. Floating 3D Micro-Animations */
@keyframes stitchFloatSoft {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-6px) rotate(0.8deg); }
}

@keyframes stitchPulseAura {
  0%, 100% { opacity: 0.4; transform: scale(1); }
  50% { opacity: 0.8; transform: scale(1.06); }
}

.stitch-floating {
  animation: stitchFloatSoft 5s ease-in-out infinite;
}

/* 5. KPI Section Glass & Counter Polish */
.kpi-section {
  position: relative;
  padding: 60px 0;
}

.kpi-card {
  padding: 28px 24px !important;
  text-align: center;
}

.kpi-card .kpi-num,
.kpi-card h3 {
  background: linear-gradient(135deg, #ffffff 40%, #ff7a00 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  font-weight: 900 !important;
  font-size: clamp(2rem, 3.5vw, 2.8rem) !important;
  letter-spacing: -0.03em;
}

/* 6. Services & Growth Modules 3D Hover Polish */
.mobikasa-signature-card {
  position: relative;
  overflow: hidden;
}

.mobikasa-signature-card .mobi-icon-box {
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
}

.mobikasa-signature-card:hover .mobi-icon-box {
  transform: scale(1.1) rotate(5deg) translateZ(10px);
  box-shadow: 0 10px 25px rgba(255, 94, 30, 0.35);
}

/* 7. Methodology 4-Stage Authority Framework */
.process-step-card,
.phase-item-card {
  position: relative;
  border-radius: 22px !important;
}

.process-step-card .step-num,
.phase-item-card .phase-badge {
  background: linear-gradient(135deg, #ff5e1e, #ff8c42) !important;
  color: #ffffff !important;
  font-weight: 800 !important;
  box-shadow: 0 4px 15px rgba(255, 94, 30, 0.4) !important;
}

/* 8. SERP Dominance Table Stitch Polish */
.serp-dominance-table,
.serp-table {
  background: rgba(13, 21, 39, 0.65) !important;
  backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 20px !important;
  overflow: hidden;
}

.serp-dominance-table tr:hover {
  background: rgba(255, 255, 255, 0.03) !important;
}

/* 9. Pricing Sprints 3D Elevation */
.price-card.featured,
.pricing-card.featured,
.price-card.recommended {
  border: 1px solid rgba(255, 94, 30, 0.55) !important;
  box-shadow: 0 25px 60px -10px rgba(0, 0, 0, 0.7), 0 0 35px rgba(255, 94, 30, 0.25) !important;
  transform: translateY(-8px);
}

.price-card .price-amount {
  background: linear-gradient(135deg, #ffffff 30%, #ff8c42 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}

/* 10. Instant Scanner & Bottom CTA High-Impact Glow */
.instant-scanner-section,
.cta-audit-section {
  position: relative;
  overflow: hidden;
}

.instant-scanner-section::before,
.cta-audit-section::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 700px;
  height: 400px;
  background: radial-gradient(ellipse at center, rgba(255, 94, 30, 0.14) 0%, transparent 70%);
  pointer-events: none;
  filter: blur(50px);
}

.instant-scanner-card,
.cta-audit-card {
  background: rgba(13, 21, 39, 0.8) !important;
  backdrop-filter: blur(20px) !important;
  border: 1px solid rgba(255, 94, 30, 0.3) !important;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 35px rgba(255, 94, 30, 0.2) !important;
}

.instant-scanner-input:focus {
  border-color: #ff5e1e !important;
  box-shadow: 0 0 20px rgba(255, 94, 30, 0.45) !important;
  outline: none;
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(stitch_css)

print("SUCCESS: Google Stitch design system & 3D styling appended to styles.css!")
