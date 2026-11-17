# 1. Update index.html for KPI section and Methodology section
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace KPI section
kpi_start = html.find('<section class="kpi-section">')
kpi_end = html.find('</section>', kpi_start) + 10

if kpi_start == -1:
    print("ERROR: kpi-section not found!")
    exit(1)

new_kpi = """<section class="kpi-section" id="kpi-section">
    <!-- Soft Ambient Warm Aura -->
    <div class="kpi-ambient-glow"></div>
    <div class="container">
      <div class="kpi-stage-wrapper">
        <!-- 3D Showroom Pedestal Surface -->
        <div class="kpi-stage-pedestal"></div>

        <div class="kpi-grid">
          <!-- KPI 1 -->
          <div class="kpi-ceramic-card">
            <div class="kpi-badge-top">
              <span class="kpi-badge-dot dot-emerald"></span>
              <span class="kpi-badge-text">VERIFIED RETENTION</span>
            </div>
            <div class="kpi-number-wrap">
              <span class="kpi-number-val val-slate">98.4%</span>
            </div>
            <h4 class="kpi-label-text">Client Retention Rate</h4>
            <p class="kpi-desc-text">Long-term retainer relationships based on compound organic search ROI and transparent attribution.</p>
            <div class="kpi-micro-footer">
              <span class="kpi-stars">★★★★★</span>
              <span class="kpi-pill-tag">Zero Attrition Model</span>
            </div>
          </div>

          <!-- KPI 2 -->
          <div class="kpi-ceramic-card featured-kpi">
            <div class="kpi-badge-top">
              <span class="kpi-badge-dot dot-orange"></span>
              <span class="kpi-badge-text">REVENUE VELOCITY</span>
            </div>
            <div class="kpi-number-wrap">
              <span class="kpi-number-val val-orange">+340%</span>
            </div>
            <h4 class="kpi-label-text">Avg. Organic Revenue Lift</h4>
            <p class="kpi-desc-text">Average revenue increase achieved for e-commerce and enterprise clients within the first 12 months.</p>
            <div class="kpi-micro-footer">
              <svg class="kpi-spark-svg" viewBox="0 0 100 24" fill="none">
                <path d="M 0 20 Q 25 22 50 12 T 100 4" stroke="#ff5e1e" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="100" cy="4" r="3" fill="#ff5e1e"/>
              </svg>
              <span class="kpi-pill-tag tag-emerald">Top 1% Benchmark</span>
            </div>
          </div>

          <!-- KPI 3 -->
          <div class="kpi-ceramic-card">
            <div class="kpi-badge-top">
              <span class="kpi-badge-dot dot-cyan"></span>
              <span class="kpi-badge-text">GLOBAL ENTERPRISE</span>
            </div>
            <div class="kpi-number-wrap">
              <span class="kpi-number-val val-slate">500+</span>
            </div>
            <h4 class="kpi-label-text">Enterprise Brands Scaled</h4>
            <p class="kpi-desc-text">Serving market leaders across India, North America, the UK, Europe, and Australia since 2002.</p>
            <div class="kpi-micro-footer">
              <span class="kpi-pill-tag">US • UK • IN • EU</span>
              <span class="kpi-pill-tag">Global Delivery</span>
            </div>
          </div>

          <!-- KPI 4 -->
          <div class="kpi-ceramic-card">
            <div class="kpi-badge-top">
              <span class="kpi-badge-dot dot-gold"></span>
              <span class="kpi-badge-text">HERITAGE AUTHORITY</span>
            </div>
            <div class="kpi-number-wrap">
              <span class="kpi-number-val val-gold">24+ Yrs</span>
            </div>
            <h4 class="kpi-label-text">Continuous Leadership</h4>
            <p class="kpi-desc-text">Navigating every major Google core update, mobile transition, and the generative AI search revolution.</p>
            <div class="kpi-micro-footer">
              <span class="kpi-pill-tag">Since 2002</span>
              <span class="kpi-pill-tag">Florida → SGE 2026</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""

html = html[:kpi_start] + new_kpi + html[kpi_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Updated KPI section in index.html with 3D tactile showroom ceramic cards!")
