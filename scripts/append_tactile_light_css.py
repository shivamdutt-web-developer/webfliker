css_tactile = """
/* ==========================================================================
   WARM LUXURY 3D TACTILE CERAMIC UPGRADES (LIGHT THEME SHOWROOM QUALITY)
   ========================================================================== */

/* 1. KPI Section Showroom Pedestal & Ceramic Cards */
.kpi-section {
  position: relative;
  padding: 80px 0 100px;
  background: transparent;
  overflow: visible;
}

.kpi-ambient-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 950px;
  height: 400px;
  background: radial-gradient(ellipse at center, rgba(255, 94, 30, 0.08) 0%, rgba(255, 122, 0, 0.03) 50%, transparent 75%);
  filter: blur(60px);
  pointer-events: none;
  z-index: 0;
}

.kpi-stage-wrapper {
  position: relative;
  z-index: 1;
}

/* 3D Showroom Platform Pedestal */
.kpi-stage-pedestal {
  position: absolute;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  width: 104%;
  height: 48px;
  background: radial-gradient(ellipse at center, #ffdcd1 0%, #ffece4 60%, rgba(255, 245, 240, 0) 80%);
  border-radius: 999px;
  box-shadow: 0 16px 35px rgba(255, 94, 30, 0.16);
  z-index: 0;
  pointer-events: none;
}

.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  position: relative;
  z-index: 1;
}

@media (max-width: 1100px) {
  .kpi-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
}

@media (max-width: 640px) {
  .kpi-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}

.kpi-ceramic-card {
  position: relative;
  background: #ffffff !important;
  border: 1px solid rgba(255, 230, 218, 0.95) !important;
  border-radius: 24px !important;
  padding: 32px 26px 28px !important;
  box-shadow: 0 20px 45px -12px rgba(255, 94, 30, 0.12), 
              0 8px 24px -6px rgba(15, 23, 42, 0.05),
              inset 0 1px 0 #ffffff !important;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1),
              box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1),
              border-color 0.3s ease !important;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.kpi-ceramic-card:hover {
  transform: translateY(-8px) scale(1.015) !important;
  border-color: rgba(255, 94, 30, 0.45) !important;
  box-shadow: 0 28px 60px -12px rgba(255, 94, 30, 0.24), 
              0 12px 30px -8px rgba(15, 23, 42, 0.08),
              inset 0 1px 0 #ffffff !important;
}

.kpi-ceramic-card.featured-kpi {
  border: 1.5px solid rgba(255, 94, 30, 0.45) !important;
  box-shadow: 0 24px 50px -10px rgba(255, 94, 30, 0.18), 
              0 10px 26px -6px rgba(15, 23, 42, 0.06),
              inset 0 1px 0 #ffffff !important;
}

/* KPI Card Interior Elements */
.kpi-badge-top {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 5px 12px;
  border-radius: 999px;
  background: #fff8f5;
  border: 1px solid rgba(255, 94, 30, 0.18);
  margin-bottom: 18px;
  width: fit-content;
}

.kpi-badge-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.dot-emerald { background: #10b981; box-shadow: 0 0 8px rgba(16, 185, 129, 0.6); }
.dot-orange { background: #ff5e1e; box-shadow: 0 0 8px rgba(255, 94, 30, 0.6); }
.dot-cyan { background: #0284c7; box-shadow: 0 0 8px rgba(2, 132, 199, 0.6); }
.dot-gold { background: #f59e0b; box-shadow: 0 0 8px rgba(245, 158, 11, 0.6); }

.kpi-badge-text {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: #ff5e1e;
}

.kpi-number-wrap {
  margin-bottom: 12px;
}

.kpi-number-val {
  font-size: clamp(2.4rem, 4vw, 3.2rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 1;
  display: block;
}

.val-slate {
  background: linear-gradient(135deg, #0f172a 40%, #ea580c 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.val-orange {
  background: linear-gradient(135deg, #ff5e1e 0%, #ff8c42 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.val-gold {
  background: linear-gradient(135deg, #0f172a 40%, #d97706 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.kpi-label-text {
  font-size: 1.15rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 8px;
  letter-spacing: -0.01em;
}

.kpi-desc-text {
  font-size: 0.92rem;
  line-height: 1.55;
  color: #64748b;
  margin-bottom: 22px;
}

.kpi-micro-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 16px;
  border-top: 1px solid rgba(241, 245, 249, 0.9);
  gap: 10px;
}

.kpi-stars {
  color: #f59e0b;
  font-size: 0.95rem;
  letter-spacing: 2px;
}

.kpi-pill-tag {
  display: inline-block;
  font-size: 0.74rem;
  font-weight: 700;
  color: #64748b;
  background: #f8fafc;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid #e2e8f0;
}

.kpi-pill-tag.tag-emerald {
  color: #059669;
  background: #ecfdf5;
  border-color: #a7f3d0;
}

.kpi-spark-svg {
  width: 80px;
  height: 20px;
}

/* 2. Methodology Section Tactile Upgrades */
.process-step-card {
  background: #ffffff !important;
  border: 1px solid rgba(255, 230, 218, 0.9) !important;
  border-radius: 22px !important;
  padding: 32px 26px !important;
  box-shadow: 0 18px 40px -10px rgba(255, 94, 30, 0.1),
              0 8px 20px -6px rgba(15, 23, 42, 0.04),
              inset 0 1px 0 #ffffff !important;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1),
              box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1),
              border-color 0.3s ease !important;
}

.process-step-card:hover {
  transform: translateY(-8px) !important;
  border-color: rgba(255, 94, 30, 0.4) !important;
  box-shadow: 0 26px 55px -10px rgba(255, 94, 30, 0.22),
              0 10px 25px -6px rgba(15, 23, 42, 0.06),
              inset 0 1px 0 #ffffff !important;
}

.step-num-pill {
  background: linear-gradient(135deg, #fff5f0, #ffeae0) !important;
  color: #ff5e1e !important;
  font-weight: 800 !important;
  font-size: 0.76rem !important;
  padding: 6px 14px !important;
  border-radius: 999px !important;
  border: 1px solid rgba(255, 94, 30, 0.25) !important;
  box-shadow: 0 2px 8px rgba(255, 94, 30, 0.12) !important;
}

.step-icon-wrap {
  width: 44px !important;
  height: 44px !important;
  border-radius: 14px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.06) !important;
}

.step-icon-wrap.icon-orange { background: #fff5ed !important; color: #ff5e1e !important; border: 1px solid #ffd8c4 !important; }
.step-icon-wrap.icon-cyan { background: #f0f9ff !important; color: #0284c7 !important; border: 1px solid #bae6fd !important; }
.step-icon-wrap.icon-purple { background: #faf5ff !important; color: #7c3aed !important; border: 1px solid #e9d5ff !important; }
.step-icon-wrap.icon-emerald { background: #ecfdf5 !important; color: #059669 !important; border: 1px solid #a7f3d0 !important; }

.step-deliverables span {
  display: block;
  font-size: 0.84rem;
  font-weight: 600;
  color: #0f172a;
  background: #f8fafc;
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  margin-top: 6px;
}

/* 3. 9-Phase Lifecycle Tactile Cards */
.phase-item-card {
  background: #ffffff !important;
  border: 1px solid rgba(255, 235, 225, 0.85) !important;
  border-radius: 20px !important;
  padding: 26px 22px !important;
  box-shadow: 0 14px 32px -8px rgba(255, 94, 30, 0.08),
              0 6px 16px -4px rgba(15, 23, 42, 0.03),
              inset 0 1px 0 #ffffff !important;
  position: relative !important;
  overflow: hidden !important;
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease !important;
}

.phase-item-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #ff5e1e, #ffaa40);
  opacity: 0;
  transition: opacity 0.25s ease;
}

.phase-item-card:hover {
  transform: translateY(-6px) !important;
  border-color: rgba(255, 94, 30, 0.35) !important;
  box-shadow: 0 22px 48px -10px rgba(255, 94, 30, 0.18),
              inset 0 1px 0 #ffffff !important;
}

.phase-item-card:hover::before {
  opacity: 1;
}

.phase-item-card h4 {
  font-size: 1.1rem !important;
  font-weight: 800 !important;
  color: #0f172a !important;
  margin: 10px 0 6px !important;
}

.phase-item-card p {
  color: #64748b !important;
  font-size: 0.88rem !important;
  line-height: 1.55 !important;
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write("\n" + css_tactile + "\n")

print("SUCCESS: Appended warm luxury 3D tactile CSS to styles.css!")
