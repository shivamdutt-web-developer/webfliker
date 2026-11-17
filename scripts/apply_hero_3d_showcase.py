# Update index.html hero section
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- Hero Right: POLISHED 3-ELEMENT 3D HERO SHOWCASE -->'
end_marker = '<!-- 2. TRUSTED ACCREDITATIONS & AUTHORITY MEDIA STRIP'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: Markers not found! start: {start_idx}, end: {end_idx}")
    exit(1)

# Find the start of the comment before end_marker
prev_comment = html.rfind('<!-- ===', start_idx, end_idx)
if prev_comment != -1:
    end_idx = prev_comment

new_hero_right = """<!-- Hero Right: POLISHED 3-ELEMENT 3D HERO SHOWCASE -->
      <div class="hero-visual-col">
        <!-- 3D Interactive Spatial Switcher -->
        <div class="hero-3d-switcher-bar">
          <button type="button" class="hero-switcher-pill active" data-3d-model="searchLens" id="btnHeroLens">
            <i data-lucide="search" style="width: 14px; height: 14px;"></i>
            <span>3D Search Lens</span>
          </button>
          <button type="button" class="hero-switcher-pill" data-3d-model="neuralGraph" id="btnHeroNeural">
            <i data-lucide="network" style="width: 14px; height: 14px;"></i>
            <span>3D AI Entity Graph</span>
          </button>
          <button type="button" class="hero-switcher-pill" id="btnHeroPhone" data-hero-view="phone">
            <i data-lucide="smartphone" style="width: 14px; height: 14px;"></i>
            <span>3D Storefront</span>
          </button>
        </div>

        <div class="hero-3d-stage" id="hero3dStage" aria-label="Interactive 3D search and headless commerce showcase">
          <!-- Soft Ambient Orange Backlight Glow -->
          <div class="hero-3d-ambient-glow" id="heroAmbientGlow"></div>

          <!-- Interactive 3D WebGL Canvas Viewport -->
          <div class="webgl-lab-viewport" id="heroWebglViewport">
            <canvas id="webglLabCanvas" class="webgl-lab-canvas"></canvas>
            <div class="webgl-drag-hint">
              <i data-lucide="rotate-3d" style="width: 13px; height: 13px; color: #ff5e1e;"></i>
              <span>360° Drag to Rotate</span>
            </div>
          </div>

          <!-- Phone Viewport (shown when Storefront is clicked) -->
          <div class="hero-3d-scene" id="hero3dScene" style="display: none;">
            <div class="phone-3d-chassis-seamless" id="phone3dChassis">
              <img src="assets/3d/mobikasa-flagship-phone.png" alt="Mobikasa-Inspired 3D Headless eCommerce Flagship Smartphone" class="mobikasa-flagship-phone-img" loading="eager">
            </div>
          </div>

          <!-- ELEMENT 1: UPPER-LEFT GOOGLE RANK #1 SHIELD BADGE -->
          <div class="glass-card-3d polished-rank-badge" id="layerRankBadge" data-parallax-depth="0.08" data-tz="110">
            <div class="rank-shield-icon">#1</div>
            <div class="rank-shield-text">
              <div class="rank-main-title">Google Rank #1</div>
              <div class="rank-sub-title">Commercial Query • 48.2k Clicks</div>
            </div>
            <span class="live-pulse-dot"></span>
          </div>

          <!-- ELEMENT 2: UPPER-RIGHT ORGANIC REVENUE GROWTH CARD -->
          <div class="glass-card-3d polished-revenue-card" id="layerRevenueCard" data-parallax-depth="0.065" data-tz="90">
            <div class="polished-card-header">
              <div>
                <div class="card-micro-label">ORGANIC REVENUE GROWTH</div>
                <div class="card-macro-val">$12.4M <span class="trend-badge-orange">+340% YoY</span></div>
              </div>
              <div class="spark-icon-wrap">
                <i data-lucide="trending-up" style="width: 16px; height: 16px; color: #ff5e1e;"></i>
              </div>
            </div>
            <!-- Real Organic Curve SVG -->
            <svg class="revenue-sparkline-svg" viewBox="0 0 200 48" fill="none">
              <defs>
                <linearGradient id="revGradHero" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#ff5e1e" stop-opacity="0.3"/>
                  <stop offset="50%" stop-color="#ff7b39" stop-opacity="0.9"/>
                  <stop offset="100%" stop-color="#10b981" stop-opacity="1"/>
                </linearGradient>
              </defs>
              <path d="M 0 38 Q 35 44 70 26 T 140 18 T 200 6" stroke="url(#revGradHero)" stroke-width="3" stroke-linecap="round"/>
              <circle cx="200" cy="6" r="4" fill="#10b981"/>
            </svg>
          </div>

          <!-- ELEMENT 3: MOBIKASA SIGNATURE FROSTED GLASS CARD -->
          <div class="glass-card-3d mobikasa-signature-card hero-ai-card" id="layerAiCard" data-parallax-depth="0.075" data-tz="125">
            <div class="mobi-card-header">
              <div class="mobi-icon-box">
                <i data-lucide="sparkles" style="width: 18px; height: 18px; color: #ff5e1e;"></i>
              </div>
              <a href="ai-seo.html" class="mobi-arrow-btn" aria-label="Explore AI SEO Architecture">
                <i data-lucide="arrow-up-right" style="width: 15px; height: 15px;"></i>
              </a>
            </div>
            <div class="mobi-card-content">
              <h4 class="mobi-card-title">Headless 3D Commerce</h4>
              <p class="mobi-card-desc">Sub-second Shopify Plus speed &amp; 98.6% AI citation authority.</p>
              <div class="mobi-card-tags">
                <span class="mobi-tag tag-cyan">ChatGPT</span>
                <span class="mobi-tag tag-emerald">Gemini Active</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  """

html = html[:start_idx] + new_hero_right + html[end_idx:]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Updated hero section in index.html!")
