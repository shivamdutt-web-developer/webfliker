with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

pricing_css = '''
/* ==========================================================================
   MOBIKASA & STITCH ELEVATED PRICING MATRIX (3-TIER + DEDICATED SQUAD)
   ========================================================================== */
.pricing-matrix-section {
  padding: 110px 0 100px;
  background: #fbf9f5;
  position: relative;
}

.pricing-toggle-wrap {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  background: #ffffff;
  padding: 8px 18px;
  border-radius: 999px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
  margin-top: 30px;
}

.pricing-toggle-label {
  font-size: 0.88rem;
  font-weight: 700;
  color: #64748b;
  cursor: pointer;
  transition: all 0.2s ease;
  user-select: none;
}

.pricing-toggle-label.active {
  color: #0f172a;
  font-weight: 800;
}

.pricing-discount-pill {
  display: inline-block;
  background: #fff7ed;
  color: #ea580c;
  border: 1px solid #fed7aa;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 999px;
  margin-left: 4px;
}

.pricing-toggle-switch {
  width: 52px;
  height: 28px;
  background: #cbd5e1;
  border-radius: 999px;
  border: none;
  cursor: pointer;
  position: relative;
  transition: background 0.25s ease;
  padding: 2px;
  display: flex;
  align-items: center;
}

.pricing-toggle-switch.active {
  background: #ff5e1e;
}

.pricing-toggle-knob {
  width: 24px;
  height: 24px;
  background: #ffffff;
  border-radius: 50%;
  display: block;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  transform: translateX(0);
}

.pricing-toggle-switch.active .pricing-toggle-knob {
  transform: translateX(24px);
}

.luxury-pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
  margin-top: 50px;
  align-items: stretch;
}

.luxury-price-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 28px;
  padding: 40px 32px;
  box-shadow: 0 10px 35px rgba(15, 23, 42, 0.04);
  display: flex;
  flex-direction: column;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: hidden;
}

.luxury-price-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 24px 50px rgba(15, 23, 42, 0.09);
  border-color: #cbd5e1;
}

.luxury-price-card.featured {
  border: 2px solid #ff5e1e;
  box-shadow: 0 20px 50px rgba(255, 94, 30, 0.12), 0 0 0 1px #ff5e1e;
  transform: translateY(-4px);
}

.luxury-price-card.featured:hover {
  transform: translateY(-12px);
  box-shadow: 0 30px 60px rgba(255, 94, 30, 0.2);
}

.featured-top-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: linear-gradient(90deg, #ff5e1e, #ff8c42);
}

.price-card-header {
  margin-bottom: 24px;
}

.featured-badge-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.tier-pill {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  padding: 4px 12px;
  border-radius: 999px;
  margin-bottom: 14px;
}

.tier-pill-slate {
  background: #f1f5f9;
  color: #475569;
}

.tier-pill-orange {
  background: #fff7ed;
  color: #ea580c;
  border: 1px solid #fed7aa;
}

.live-pulse-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.7rem;
  font-weight: 800;
  color: #10b981;
  background: #ecfdf5;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid #a7f3d0;
}

.pulse-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 6px #10b981;
}

.tier-name {
  font-size: 1.5rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 8px;
  line-height: 1.25;
}

.tier-summary {
  font-size: 0.88rem;
  color: #64748b;
  line-height: 1.55;
  margin: 0;
  min-height: 44px;
}

.price-figure-row {
  display: flex;
  align-items: baseline;
  gap: 4px;
  padding-bottom: 24px;
  margin-bottom: 24px;
  border-bottom: 1px solid #f1f5f9;
}

.currency-symbol {
  font-size: 1.5rem;
  font-weight: 800;
  color: #0f172a;
}

.price-amount {
  font-size: 2.8rem;
  font-weight: 900;
  color: #0f172a;
  letter-spacing: -0.03em;
  line-height: 1;
}

.price-cadence {
  font-size: 0.88rem;
  font-weight: 600;
  color: #94a3b8;
  margin-left: 4px;
}

.color-orange {
  color: #ff5e1e !important;
}

.price-deliverables-title {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: #94a3b8;
  margin-bottom: 16px;
  text-transform: uppercase;
}

.luxury-features-list {
  list-style: none;
  padding: 0;
  margin: 0 0 32px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  flex-grow: 1;
}

.luxury-features-list li {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 0.88rem;
  color: #334155;
  line-height: 1.5;
}

.feat-icon {
  width: 17px;
  height: 17px;
  color: #10b981;
  flex-shrink: 0;
  margin-top: 2px;
}

.feat-orange {
  color: #ff5e1e !important;
}

.btn-price-tier {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  padding: 16px;
  border-radius: 999px;
  font-weight: 800;
  font-size: 0.92rem;
  text-decoration: none;
  transition: all 0.25s ease;
  cursor: pointer;
}

.btn-tier-secondary {
  background: #f8fafc;
  color: #0f172a;
  border: 1px solid #e2e8f0;
}

.btn-tier-secondary:hover {
  background: #0f172a;
  color: #ffffff;
  border-color: #0f172a;
}

.btn-tier-primary {
  background: linear-gradient(135deg, #ff5e1e, #ff7a00);
  color: #ffffff;
  box-shadow: 0 8px 24px rgba(255, 94, 30, 0.35);
  border: none;
}

.btn-tier-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(255, 94, 30, 0.5);
}

.enterprise-squad-banner {
  margin-top: 48px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 24px;
  padding: 32px 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  box-shadow: 0 8px 25px rgba(15, 23, 42, 0.04);
  flex-wrap: wrap;
}

.squad-info {
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
}

.squad-avatars {
  display: flex;
  align-items: center;
}

.squad-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 3px solid #ffffff;
  object-fit: cover;
  margin-left: -12px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

.squad-avatars img:first-child {
  margin-left: 0;
}

.squad-avatar-more {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #ff5e1e;
  color: #ffffff;
  border: 3px solid #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 800;
  margin-left: -12px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

.squad-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 6px;
}

.squad-desc {
  font-size: 0.88rem;
  color: #64748b;
  margin: 0;
  max-width: 620px;
  line-height: 1.5;
}

.btn-squad-action {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  background: #0f172a;
  color: #ffffff;
  border-radius: 999px;
  font-weight: 800;
  font-size: 0.88rem;
  text-decoration: none;
  white-space: nowrap;
  transition: all 0.25s ease;
}

.btn-squad-action:hover {
  background: #ff5e1e;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(255, 94, 30, 0.3);
}

@media (max-width: 1024px) {
  .luxury-pricing-grid {
    grid-template-columns: 1fr;
    max-width: 540px;
    margin-left: auto;
    margin-right: auto;
  }
  .enterprise-squad-banner {
    flex-direction: column;
    text-align: center;
  }
  .squad-info {
    flex-direction: column;
    justify-content: center;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(pricing_css)

print('Appended pricing CSS successfully!')
