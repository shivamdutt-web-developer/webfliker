with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

services_bento_css = '''
/* ==========================================================================
   MOBIKASA ASYMMETRIC BENTO SHOWCASE (DIGITAL SOLUTIONS & GROWTH)
   ========================================================================== */
.services-section {
  padding: 100px 0 90px;
  background: #ffffff;
}

.services-stage-panel {
  background: #fbf9f5;
  border: 1px solid #e8e5df;
  border-radius: 40px;
  padding: 60px 48px;
  box-shadow: 0 15px 45px rgba(28, 25, 23, 0.04);
}

.services-header-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 44px;
  gap: 32px;
  flex-wrap: wrap;
}

.services-main-title {
  font-size: clamp(2rem, 3.5vw, 3rem);
  font-weight: 800;
  color: #0f172a;
  margin: 0;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.services-header-right {
  max-width: 480px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 16px;
}

.services-intro-text {
  font-size: 1rem;
  color: #64748b;
  margin: 0;
  line-height: 1.6;
}

.btn-services-explore {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #ff5e1e;
  color: #ffffff;
  padding: 12px 24px;
  border-radius: 999px;
  font-weight: 800;
  font-size: 0.88rem;
  text-decoration: none;
  transition: all 0.25s ease;
  box-shadow: 0 6px 20px rgba(255, 94, 30, 0.35);
}

.btn-services-explore:hover {
  background: #ea580c;
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(255, 94, 30, 0.5);
}

.mobikasa-bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.bento-feature-wide {
  grid-column: span 3;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 28px;
  padding: 40px 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  box-shadow: 0 8px 30px rgba(15, 23, 42, 0.04);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.bento-feature-wide:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.08);
  border-color: #cbd5e1;
}

.bento-content-col {
  flex: 1;
  max-width: 580px;
}

.bento-badge {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  padding: 4px 12px;
  border-radius: 999px;
  margin-bottom: 14px;
}

.bento-heading {
  font-size: 1.5rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 12px;
  line-height: 1.3;
}

.bento-sub {
  font-size: 0.92rem;
  color: #64748b;
  line-height: 1.6;
  margin: 0 0 22px;
}

.bento-tags-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
}

.bento-tag {
  font-size: 0.78rem;
  font-weight: 700;
  color: #475569;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 5px 12px;
  border-radius: 999px;
}

.bento-cta-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.88rem;
  font-weight: 800;
  color: #ff5e1e;
  text-decoration: none;
  transition: all 0.2s ease;
}

.bento-cta-link:hover {
  color: #ea580c;
  text-decoration: underline;
}

.bento-visual-preview {
  flex: 1;
  max-width: 440px;
  display: flex;
  justify-content: center;
}

.storefront-preview-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0,0,0,0.06);
  width: 100%;
}

.preview-browser-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #ffffff;
  padding: 10px 16px;
  border-bottom: 1px solid #e2e8f0;
}

.p-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #cbd5e1;
}

.p-url {
  font-size: 0.72rem;
  color: #94a3b8;
  font-family: monospace;
  margin-left: 8px;
}

.preview-store-body {
  padding: 24px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 180px;
  background: linear-gradient(135deg, #fff7ed 0%, #ffffff 100%);
}

.preview-metric-pill {
  position: absolute;
  top: 14px;
  right: 14px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.72rem;
  font-weight: 800;
  color: #059669;
  background: #ffffff;
  padding: 4px 10px;
  border-radius: 999px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

.p-green-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
}

.preview-thumb-img {
  height: 140px;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 12px 24px rgba(0,0,0,0.12));
}

.bento-card-square {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 28px;
  padding: 36px 30px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 25px rgba(15, 23, 42, 0.04);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.bento-card-square:hover {
  transform: translateY(-6px);
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
  border-color: #cbd5e1;
}

.bento-square-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.bento-icon-glow {
  width: 44px;
  height: 44px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-glow-purple {
  background: #faf5ff;
  color: #7e22ce;
  box-shadow: 0 4px 14px rgba(126, 34, 206, 0.15);
}

.icon-glow-cyan {
  background: #f0f9ff;
  color: #0284c7;
  box-shadow: 0 4px 14px rgba(2, 132, 199, 0.15);
}

.icon-glow-emerald {
  background: #ecfdf5;
  color: #059669;
  box-shadow: 0 4px 14px rgba(5, 150, 105, 0.15);
}

.ai-citation-pills {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 24px;
}

.ai-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 700;
  color: #475569;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 6px 12px;
  border-radius: 8px;
}

.lighthouse-benchmark-card {
  display: flex;
  align-items: center;
  gap: 14px;
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  padding: 12px 16px;
  border-radius: 14px;
  margin-bottom: 24px;
}

.lh-score-circle {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: #16a34a;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 1.05rem;
  box-shadow: 0 4px 10px rgba(22, 163, 74, 0.3);
}

.lh-score-info strong {
  display: block;
  font-size: 0.82rem;
  color: #14532d;
  font-weight: 800;
}

.lh-score-info span {
  display: block;
  font-size: 0.74rem;
  color: #166534;
}

.pr-publication-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
}

.pub-tag {
  font-size: 0.76rem;
  font-weight: 800;
  color: #334155;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 5px 12px;
  border-radius: 8px;
  font-style: italic;
}

.perf-metric-chart-box {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  padding: 20px 24px;
  width: 100%;
  box-shadow: 0 8px 20px rgba(0,0,0,0.04);
}

.chart-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.chart-label {
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: #94a3b8;
}

.chart-roi-stat {
  font-size: 0.88rem;
  font-weight: 900;
  color: #ff5e1e;
  background: #fff7ed;
  padding: 3px 10px;
  border-radius: 999px;
}

.chart-footer-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.72rem;
  color: #94a3b8;
  margin-top: 8px;
}

@media (max-width: 1024px) {
  .bento-feature-wide {
    flex-direction: column;
    padding: 32px 24px;
  }
  .mobikasa-bento-grid {
    grid-template-columns: 1fr;
  }
  .bento-feature-wide {
    grid-column: span 1;
  }
  .services-stage-panel {
    padding: 40px 24px;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(services_bento_css)

print('Appended Mobikasa Bento CSS successfully!')
