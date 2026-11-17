with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Replace hero-visual-col
old_visual_pattern = r'<!-- Hero Right: MULTI-LAYER 3D GLASSMORPHIC HERO STAGE -->[\s\S]*?</div>\s*</div>\s*</div>\s*</div>\s*</section>'

new_visual = '''<!-- Hero Right: POLISHED 3-ELEMENT 3D HERO SHOWCASE -->
      <div class="hero-visual-col">
        <div class="hero-3d-stage" id="hero3dStage" aria-label="Interactive 3D flagship smartphone and focused analytics showcase">
          
          <!-- Soft Ambient Orange Backlight Glow -->
          <div class="hero-3d-ambient-glow" id="heroAmbientGlow"></div>

          <!-- Main 3D Perspective Scene Container -->
          <div class="hero-3d-scene" id="hero3dScene">
            
            <!-- PRIMARY FOCAL POINT: 3D FLAGSHIP SMARTPHONE -->
            <div class="phone-3d-chassis" id="phone3dChassis">
              <!-- Polished Titanium Chamfered Bezel -->
              <div class="phone-titanium-bezel">
                
                <!-- Dynamic Island & Camera System -->
                <div class="phone-dynamic-island">
                  <span class="island-camera"></span>
                  <span class="island-sensor"></span>
                </div>

                <!-- Glass Screen & High-End Agency Storefront UI -->
                <div class="phone-screen-content">
                  <!-- App Header -->
                  <div class="screen-app-bar">
                    <span class="app-brand-title">AURA COMMERCE • LIVE</span>
                    <div class="app-bar-icons">
                      <span class="app-signal-dot"></span>
                      <span class="app-cart-pill">GROWTH ACTIVE</span>
                    </div>
                  </div>

                  <!-- Hero Showcase Base Artwork -->
                  <div class="screen-hero-art">
                    <img src="assets/3d/mobikasa-hero-showcase.png" alt="3D eCommerce and Search Engine Dominance App Interface" class="screen-base-img" loading="eager">
                    <!-- Subtle Glass Specular Light Sheen -->
                    <div class="glass-light-sheen" id="phoneLightSheen"></div>
                  </div>

                  <!-- Screen Status Ribbon -->
                  <div class="screen-status-ribbon">
                    <div class="status-kpi-item">
                      <span class="kpi-micro-label">ORGANIC GMV</span>
                      <span class="kpi-micro-val">$12.4M</span>
                    </div>
                    <div class="status-kpi-item border-both">
                      <span class="kpi-micro-label">TOP-3 RANK</span>
                      <span class="kpi-micro-val">94.8%</span>
                    </div>
                    <div class="status-kpi-item">
                      <span class="kpi-micro-label">AI CITATION</span>
                      <span class="kpi-micro-val">98.6%</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- ELEMENT 1: UPPER-LEFT GOOGLE RANK #1 SHIELD BADGE (translateZ: 110px) -->
            <div class="glass-card-3d polished-rank-badge" id="layerRankBadge" data-parallax-depth="0.08" data-tz="110">
              <div class="rank-shield-icon">#1</div>
              <div class="rank-shield-text">
                <div class="rank-main-title">Google Rank #1</div>
                <div class="rank-sub-title">Commercial Query • 48.2k Clicks</div>
              </div>
              <span class="live-pulse-dot"></span>
            </div>

            <!-- ELEMENT 2: UPPER-RIGHT ORGANIC REVENUE GROWTH CARD (translateZ: 90px) -->
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
                  <linearGradient id="revGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#ff5e1e" stop-opacity="0.3"/>
                    <stop offset="50%" stop-color="#ff7b39" stop-opacity="0.9"/>
                    <stop offset="100%" stop-color="#10b981" stop-opacity="1"/>
                  </linearGradient>
                </defs>
                <path d="M 0 38 Q 35 44 70 26 T 140 18 T 200 6" stroke="url(#revGrad)" stroke-width="3" stroke-linecap="round"/>
                <circle cx="200" cy="6" r="4" fill="#10b981"/>
              </svg>
            </div>

            <!-- ELEMENT 3: LOWER-RIGHT AI SEARCH VISIBILITY CARD (translateZ: 75px) -->
            <div class="glass-card-3d polished-ai-card" id="layerAiCard" data-parallax-depth="0.075" data-tz="75">
              <div class="polished-card-header">
                <div>
                  <div class="card-micro-label">AI SEARCH VISIBILITY</div>
                  <div class="card-macro-val">98.6% <span class="trend-badge-cyan">Active</span></div>
                </div>
                <span class="ai-live-pill">ChatGPT • Gemini</span>
              </div>
              <div class="ai-knowledge-meta">
                <span class="meta-dot-pulse"></span>
                <span>140+ Knowledge Graph Nodes Verified</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </section>'''

if re.search(old_visual_pattern, html):
    html = re.sub(old_visual_pattern, new_visual, html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced old multi-card layout with 3-element polished layout in index.html")
else:
    print("Regex match failed")
