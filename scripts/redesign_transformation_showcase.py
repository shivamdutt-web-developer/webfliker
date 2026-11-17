import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new showstopper transformation showcase HTML
new_section_html = '''  <!-- ========================================================================= -->
  <!-- LUXURY 3D ARCHITECTURAL TRANSFORMATION SHOWCASE (MOBIKASA + LUMERIXA GRADE)-->
  <!-- ========================================================================= -->
  <section class="transformation-showcase-section" id="transformation-showcase">
    <!-- Radiant Multi-Layer Ambient Glow -->
    <div class="trans-ambient-glow trans-glow-orange"></div>
    <div class="trans-ambient-glow trans-glow-cyan"></div>

    <div class="container" style="position: relative; z-index: 2;">
      <!-- Section Header with High-Contrast Typography -->
      <div class="trans-header">
        <div class="trans-pill-badge">
          <span class="badge-sparkle-dot"></span> ARCHITECTURAL TRANSFORMATION • 2026 BENCHMARK
        </div>
        <h2 class="trans-title">
          The Anatomy of an <span class="trans-gradient-text">Enterprise Growth Overhaul</span>
        </h2>
        <p class="trans-subtitle">
          Inspect the quantifiable performance gap: slow monolithic legacy platforms vs. Webflikr's high-speed 3D headless search architecture.
        </p>

        <!-- Interactive View Switcher Tabs -->
        <div class="trans-switch-dock">
          <button class="trans-tab-btn active" data-view="split" id="btnViewSplit">
            <i data-lucide="columns" style="width: 15px; height: 15px;"></i> Side-by-Side Dual View
          </button>
          <button class="trans-tab-btn" data-view="legacy" id="btnViewLegacy">
            <span class="dot-red"></span> Legacy Monolith
          </button>
          <button class="trans-tab-btn" data-view="modern" id="btnViewModern">
            <span class="dot-green"></span> Modernized 3D Headless
          </button>
        </div>
      </div>

      <!-- DUAL SHOWCASE CARDS CONTAINER -->
      <div class="trans-cards-grid" id="transCardsGrid">
        
        <!-- CARD 1: THE LEGACY MONOLITH (PRE-WEBFLIKR) -->
        <div class="trans-card trans-card-legacy tilt-card" id="cardLegacy">
          <!-- Card Top Bar -->
          <div class="trans-card-topbar">
            <div class="trans-status-tag tag-legacy">
              <span class="pulse-indicator pulse-red"></span> PRE-WEBFLIKR • LEGACY PLATFORM
            </div>
            <div class="trans-impact-badge badge-red-glow">
              -42% TRAFFIC LOSS
            </div>
          </div>

          <!-- Card Header Info -->
          <div class="trans-card-meta">
            <h3 class="trans-card-title text-legacy-title">Monolithic Bloated Infrastructure</h3>
            <p class="trans-card-desc">Legacy multi-plugin CMS with fragmented indexing, severe crawl budget waste, and failing Core Web Vitals.</p>
          </div>

          <!-- Diagnostic Console Mockup -->
          <div class="trans-mockup-console console-legacy">
            <div class="console-header">
              <span class="mac-dot red"></span>
              <span class="mac-dot yellow"></span>
              <span class="mac-dot green"></span>
              <span class="console-title">diagnostic-terminal://lighthouse-audit-fail.log</span>
            </div>
            <div class="console-body">
              <div class="console-line line-err"><span class="err-tag">[CRITICAL]</span> LCP: 4.8s (Exceeds Google 2.5s Good Threshold)</div>
              <div class="console-line line-warn"><span class="warn-tag">[WARN]</span> 4.2 MB Payload • 38 Uncompressed JavaScript scripts</div>
              <div class="console-line line-err"><span class="err-tag">[PENALTY]</span> AI Knowledge Graph: 0 Schema Entities Validated</div>
            </div>

            <!-- Falling Traffic Mini Chart SVG -->
            <div class="console-chart-wrap">
              <div class="chart-label-row">
                <span class="chart-lbl">12-Month Organic Visibility</span>
                <span class="chart-stat stat-down">📉 -42% Downward Slope</span>
              </div>
              <svg class="trans-chart-svg" viewBox="0 0 400 60" fill="none">
                <path d="M 0 15 Q 100 20 200 35 T 320 48 T 400 55" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
                <circle cx="400" cy="55" r="4" fill="#ef4444"/>
              </svg>
            </div>
          </div>

          <!-- 3 Quantitative Failure Metrics -->
          <div class="trans-metrics-grid">
            <div class="trans-metric-box box-legacy">
              <span class="metric-label">CORE WEB VITALS</span>
              <span class="metric-val text-red">4.8s LCP</span>
              <span class="metric-sub">74% Mobile bounce rate</span>
            </div>
            <div class="trans-metric-box box-legacy">
              <span class="metric-label">AI OVERVIEWS</span>
              <span class="metric-val text-muted">0 Citations</span>
              <span class="metric-sub">Invisible to LLMs</span>
            </div>
            <div class="trans-metric-box box-legacy">
              <span class="metric-label">ALGORITHM RISK</span>
              <span class="metric-val text-amber">Penalized</span>
              <span class="metric-sub">Faceted URL bloat</span>
            </div>
          </div>
        </div>

        <!-- CARD 2: THE MODERNIZED 3D HEADLESS ARCHITECTURE (POST-WEBFLIKR) -->
        <div class="trans-card trans-card-modern tilt-card" id="cardModern">
          <!-- Card Top Bar -->
          <div class="trans-card-topbar">
            <div class="trans-status-tag tag-modern">
              <span class="pulse-indicator pulse-green"></span> WEBFLIKR MODERNIZED ARCHITECTURE
            </div>
            <div class="trans-impact-badge badge-green-glow">
              +340% COMPOUND GMV
            </div>
          </div>

          <!-- Card Header Info -->
          <div class="trans-card-meta">
            <h3 class="trans-card-title text-modern-title">High-Performance 3D Headless Growth</h3>
            <p class="trans-card-desc">Sub-second Shopify Plus / Next.js edge storefront with programmatic JSON-LD entity graphs and interactive 3D WebGL.</p>
          </div>

          <!-- Diagnostic Console Mockup -->
          <div class="trans-mockup-console console-modern">
            <div class="console-header">
              <span class="mac-dot red"></span>
              <span class="mac-dot yellow"></span>
              <span class="mac-dot green"></span>
              <span class="console-title">edge-radar://lighthouse-audit-100.verified</span>
            </div>
            <div class="console-body">
              <div class="console-line line-succ"><span class="succ-tag">[VERIFIED]</span> LCP: 0.6s Instant Edge Delivery (Top 1% Global)</div>
              <div class="console-line line-succ"><span class="succ-tag">[CITATION]</span> 140+ Knowledge Graph Nodes Fed to SGE & Gemini</div>
              <div class="console-line line-succ"><span class="succ-tag">[CONVERSION]</span> Interactive 3D Product Visualizer: +38% AOV Lift</div>
            </div>

            <!-- Surging Traffic Mini Chart SVG -->
            <div class="console-chart-wrap">
              <div class="chart-label-row">
                <span class="chart-lbl">12-Month Organic Revenue Velocity</span>
                <span class="chart-stat stat-up">🚀 +340% Compound Curve</span>
              </div>
              <svg class="trans-chart-svg" viewBox="0 0 400 60" fill="none">
                <defs>
                  <linearGradient id="chartGradModern" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#ff5e1e"/>
                    <stop offset="60%" stop-color="#10b981"/>
                    <stop offset="100%" stop-color="#38bdf8"/>
                  </linearGradient>
                </defs>
                <path d="M 0 52 Q 90 48 180 32 T 300 16 T 400 6" stroke="url(#chartGradModern)" stroke-width="3" stroke-linecap="round"/>
                <circle cx="400" cy="6" r="5" fill="#10b981" filter="drop-shadow(0 0 6px #10b981)"/>
              </svg>
            </div>
          </div>

          <!-- 3 Quantitative Success Metrics -->
          <div class="trans-metrics-grid">
            <div class="trans-metric-box box-modern">
              <span class="metric-label">CORE WEB VITALS</span>
              <span class="metric-val text-emerald">0.6s LCP</span>
              <span class="metric-sub">99/100 Mobile Score</span>
            </div>
            <div class="trans-metric-box box-modern">
              <span class="metric-label">AI ANSWER ENGINE</span>
              <span class="metric-val text-cyan">98.6% Rate</span>
              <span class="metric-sub">Top citation source</span>
            </div>
            <div class="trans-metric-box box-modern">
              <span class="metric-label">GOOGLE SERP #1s</span>
              <span class="metric-val text-orange">4,820+ #1s</span>
              <span class="metric-sub">Commercial keywords</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>'''

# Replace the old section
pattern = r'<!-- =+ -->\s*<!-- MOBIKASA-INSPIRED INTERACTIVE BEFORE / AFTER TRANSFORMATION SLIDER -->\s*<!-- =+ -->\s*<section class="before-after-section" id="transformation-showcase">.*?</section>'
match = re.search(pattern, html, flags=re.DOTALL)
if match:
    html = html[:match.start()] + new_section_html + html[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced transformation section in index.html")
else:
    print("Could not match old transformation section with regex, trying alternate slice")
    start = html.find('id="transformation-showcase"')
    if start != -1:
        sec_start = html.rfind('<section', 0, start)
        sec_end = html.find('</section>', start) + len('</section>')
        html = html[:sec_start] + new_section_html + html[sec_end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Replaced via slice method successfully")
