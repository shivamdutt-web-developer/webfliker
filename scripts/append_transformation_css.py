css_content = '''
/* ========================================================================= */
/* LUXURY 3D ARCHITECTURAL TRANSFORMATION SHOWCASE (MOBIKASA + LUMERIXA)      */
/* ========================================================================= */
.transformation-showcase-section,
body.theme-light .transformation-showcase-section {
  position: relative !important;
  background: #060911 !important;
  color: #ffffff !important;
  padding: 110px 0 !important;
  overflow: hidden !important;
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
}

/* Multi-layer Ambient Backlight Glow */
.trans-ambient-glow {
  position: absolute;
  pointer-events: none;
  filter: blur(80px);
  border-radius: 50%;
  opacity: 0.65;
}
.trans-glow-orange {
  top: 15%;
  left: 20%;
  width: 500px;
  height: 350px;
  background: radial-gradient(circle, rgba(255, 94, 30, 0.16) 0%, transparent 70%);
}
.trans-glow-cyan {
  bottom: 10%;
  right: 15%;
  width: 550px;
  height: 400px;
  background: radial-gradient(circle, rgba(56, 189, 248, 0.12) 0%, transparent 70%);
}

/* Header Styles with 100% Contrast Immunity */
.trans-header {
  text-align: center;
  max-width: 820px;
  margin: 0 auto 50px;
  position: relative;
  z-index: 2;
}
.trans-pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 20px;
  border-radius: 999px;
  background: rgba(255, 94, 30, 0.12);
  border: 1px solid rgba(255, 94, 30, 0.35);
  color: #ff8c42 !important;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 18px;
  box-shadow: 0 0 20px rgba(255, 94, 30, 0.15);
}
.badge-sparkle-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #ff5e1e;
  box-shadow: 0 0 8px #ff5e1e;
}

.trans-title,
body.theme-light .trans-title {
  font-size: clamp(2.2rem, 3.8vw, 3.2rem) !important;
  font-weight: 800 !important;
  color: #ffffff !important;
  line-height: 1.22 !important;
  margin: 0 0 16px !important;
  letter-spacing: -0.02em !important;
}
.trans-gradient-text {
  background: linear-gradient(135deg, #ffffff 30%, #ff7b39 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}

.trans-subtitle,
body.theme-light .trans-subtitle {
  font-size: 1.1rem !important;
  color: #94a3b8 !important;
  line-height: 1.7 !important;
  max-width: 680px;
  margin: 0 auto 32px !important;
}

/* Interactive Switch Dock */
.trans-switch-dock {
  display: inline-flex;
  align-items: center;
  background: rgba(15, 23, 42, 0.85);
  padding: 6px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  gap: 6px;
}
.trans-tab-btn {
  background: transparent;
  border: none;
  color: #94a3b8;
  padding: 10px 22px;
  border-radius: 999px;
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.25s ease;
}
.trans-tab-btn:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.05);
}
.trans-tab-btn.active {
  background: linear-gradient(135deg, #ff5e1e 0%, #ea580c 100%);
  color: #ffffff !important;
  box-shadow: 0 4px 18px rgba(255, 94, 30, 0.45);
}
.dot-red {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ef4444;
}
.dot-green {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10b981;
}

/* Cards Grid */
.trans-cards-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 32px;
  position: relative;
  z-index: 2;
}

/* Individual Transformation Card */
.trans-card {
  border-radius: 26px;
  padding: 38px 34px;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: all 0.35s ease;
}
.trans-card-legacy {
  background: linear-gradient(150deg, #130f14 0%, #0d0c11 100%);
  border: 1px solid rgba(239, 68, 68, 0.25);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 35px rgba(239, 68, 68, 0.06);
}
.trans-card-legacy:hover {
  border-color: rgba(239, 68, 68, 0.45);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 40px rgba(239, 68, 68, 0.12);
}

.trans-card-modern {
  background: linear-gradient(150deg, #0b151f 0%, #080f16 100%);
  border: 1px solid rgba(16, 185, 129, 0.35);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 45px rgba(16, 185, 129, 0.12);
}
.trans-card-modern:hover {
  border-color: rgba(16, 185, 129, 0.55);
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.7), 0 0 55px rgba(16, 185, 129, 0.2);
}

/* Topbar */
.trans-card-topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 22px;
}
.trans-status-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.tag-legacy {
  background: rgba(239, 68, 68, 0.12);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #fca5a5;
}
.tag-modern {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.35);
  color: #6ee7b7;
}

.pulse-indicator {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}
.pulse-red {
  background: #ef4444;
  box-shadow: 0 0 8px #ef4444;
}
.pulse-green {
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
}

.trans-impact-badge {
  padding: 7px 16px;
  border-radius: 999px;
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.04em;
}
.badge-red-glow {
  background: rgba(239, 68, 68, 0.18);
  border: 1px solid rgba(239, 68, 68, 0.4);
  color: #ef4444;
  box-shadow: 0 0 16px rgba(239, 68, 68, 0.25);
}
.badge-green-glow {
  background: rgba(16, 185, 129, 0.18);
  border: 1px solid rgba(16, 185, 129, 0.45);
  color: #10b981;
  box-shadow: 0 0 20px rgba(16, 185, 129, 0.35);
}

/* Card Metadata */
.trans-card-title,
body.theme-light .trans-card-title {
  font-size: 1.55rem !important;
  font-weight: 800 !important;
  line-height: 1.3 !important;
  margin: 0 0 10px !important;
}
.text-legacy-title {
  color: #ffffff !important;
}
.text-modern-title {
  color: #ffffff !important;
}

.trans-card-desc,
body.theme-light .trans-card-desc {
  font-size: 0.94rem !important;
  color: #94a3b8 !important;
  line-height: 1.6 !important;
  margin: 0 0 26px !important;
}

/* Simulated Console Terminal */
.trans-mockup-console {
  border-radius: 16px;
  padding: 18px;
  margin-bottom: 26px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.console-legacy {
  background: rgba(10, 8, 12, 0.85);
  border-color: rgba(239, 68, 68, 0.2);
}
.console-modern {
  background: rgba(8, 14, 22, 0.85);
  border-color: rgba(16, 185, 129, 0.2);
}

.console-header {
  display: flex;
  align-items: center;
  gap: 6px;
  padding-bottom: 12px;
  margin-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.mac-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
}
.mac-dot.red { background: #ef4444; }
.mac-dot.yellow { background: #f59e0b; }
.mac-dot.green { background: #10b981; }

.console-title {
  font-family: monospace;
  font-size: 0.72rem;
  color: #64748b;
  margin-left: 8px;
}

.console-body {
  font-family: monospace;
  font-size: 0.78rem;
  line-height: 1.7;
}
.console-line {
  margin-bottom: 4px;
}
.err-tag { color: #ef4444; font-weight: 700; margin-right: 6px; }
.warn-tag { color: #f59e0b; font-weight: 700; margin-right: 6px; }
.succ-tag { color: #10b981; font-weight: 700; margin-right: 6px; }
.line-err { color: #fca5a5; }
.line-warn { color: #fcd34d; }
.line-succ { color: #a7f3d0; }

/* Console Chart Wrap */
.console-chart-wrap {
  margin-top: 16px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}
.chart-label-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}
.chart-lbl {
  font-size: 0.74rem;
  color: #94a3b8;
  font-weight: 600;
  text-transform: uppercase;
}
.chart-stat {
  font-size: 0.8rem;
  font-weight: 800;
}
.stat-down { color: #ef4444; }
.stat-up { color: #10b981; }

.trans-chart-svg {
  width: 100%;
  height: 55px;
  display: block;
}

/* 3 Metrics Grid */
.trans-metrics-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
  margin-top: auto;
}
.trans-metric-box {
  padding: 14px 16px;
  border-radius: 14px;
  display: flex;
  flex-direction: column;
}
.box-legacy {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
}
.box-modern {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(16, 185, 129, 0.15);
}

.metric-label {
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: #94a3b8;
  margin-bottom: 6px;
}
.metric-val {
  font-size: 1.45rem;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 4px;
}
.text-red { color: #ef4444 !important; }
.text-amber { color: #f59e0b !important; }
.text-muted { color: #64748b !important; }
.text-emerald { color: #10b981 !important; }
.text-cyan { color: #38bdf8 !important; }
.text-orange { color: #ff5e1e !important; }

.metric-sub {
  font-size: 0.74rem;
  color: #94a3b8;
  line-height: 1.35;
}

/* Responsive Overrides */
@media (max-width: 900px) {
  .trans-cards-grid {
    grid-template-columns: 1fr !important;
  }
  .trans-metrics-grid {
    grid-template-columns: 1fr !important;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

print("Appended luxury transformation CSS to styles.css")
