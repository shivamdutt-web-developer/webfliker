with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

founder_css = '''
/* ==========================================================================
   MOBIKASA ELEVATED FOUNDER SPOTLIGHT & BULLETPROOF BUTTON HOVERS
   ========================================================================== */
.founder-spotlight-section {
  padding: 100px 0;
  background: #ffffff;
  position: relative;
}

.founder-stage-panel {
  background: #121316;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 40px;
  padding: 70px 56px;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.25);
  position: relative;
  overflow: hidden;
}

.founder-ambient-glow {
  position: absolute;
  top: -100px;
  right: -100px;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(255, 94, 30, 0.15) 0%, transparent 70%);
  filter: blur(60px);
  pointer-events: none;
}

.founder-grid-row {
  display: grid;
  grid-template-columns: 0.85fr 1.15fr;
  gap: 50px;
  align-items: center;
  position: relative;
  z-index: 2;
}

.founder-card-chassis {
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 25px 60px rgba(0,0,0,0.5), 0 0 40px rgba(255, 94, 30, 0.12);
  background: #0c0d10;
}

.founder-img-wrapper {
  position: relative;
  overflow: hidden;
  height: 480px;
}

.founder-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: contrast(1.05);
}

.founder-badge-floating {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #ffffff;
  font-size: 0.76rem;
  font-weight: 800;
  padding: 6px 14px;
  border-radius: 999px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

.badge-dot-green {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
}

.founder-meta-bar {
  padding: 22px 26px;
  background: #0e0f12;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.founder-name {
  font-size: 1.25rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 4px;
}

.founder-role {
  font-size: 0.82rem;
  color: #ff8c42;
  font-weight: 700;
}

.founder-icon-seal {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: rgba(255, 94, 30, 0.12);
  border: 1px solid rgba(255, 94, 30, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
}

.pill-warm-dark {
  background: rgba(255, 94, 30, 0.12);
  border: 1px solid rgba(255, 94, 30, 0.3);
  color: #ff8c42;
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  padding: 6px 16px;
  border-radius: 999px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 20px;
}

.founder-headline {
  font-size: clamp(2rem, 3.4vw, 2.9rem);
  font-weight: 800;
  line-height: 1.25;
  margin: 0 0 24px;
  color: #ffffff !important;
  letter-spacing: -0.02em;
}

.founder-quote-box {
  font-size: 1.15rem;
  font-style: italic;
  color: #e2e8f0;
  line-height: 1.7;
  margin-bottom: 24px;
  border-left: 3px solid #ff5e1e;
  background: rgba(255, 255, 255, 0.02);
  border-radius: 0 16px 16px 0;
  padding: 18px 24px;
}

.founder-body-p {
  color: #94a3b8;
  font-size: 1rem;
  line-height: 1.7;
  margin: 0 0 36px;
}

.founder-btn-group {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  align-items: center;
}

.founder-btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: linear-gradient(135deg, #ff5e1e, #ff7a00);
  color: #ffffff !important;
  padding: 16px 32px;
  border-radius: 999px;
  font-weight: 800;
  font-size: 0.94rem;
  text-decoration: none;
  box-shadow: 0 8px 25px rgba(255, 94, 30, 0.38);
  transition: all 0.25s ease;
  border: none;
  cursor: pointer;
}

.founder-btn-primary:hover {
  background: linear-gradient(135deg, #ea580c, #f97316);
  color: #ffffff !important;
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(255, 94, 30, 0.5);
}

.founder-btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.08);
  border: 1.5px solid rgba(255, 255, 255, 0.25);
  color: #ffffff !important;
  padding: 16px 28px;
  border-radius: 999px;
  font-weight: 800;
  font-size: 0.94rem;
  text-decoration: none;
  transition: all 0.25s ease;
  cursor: pointer;
}

.founder-btn-secondary:hover {
  background: #ffffff !important;
  color: #0f172a !important;
  border-color: #ffffff !important;
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(255, 255, 255, 0.2);
}

@media (max-width: 992px) {
  .founder-grid-row {
    grid-template-columns: 1fr;
  }
  .founder-stage-panel {
    padding: 40px 24px;
  }
  .founder-img-wrapper {
    height: 380px;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(founder_css)

print('Appended founder CSS successfully!')
