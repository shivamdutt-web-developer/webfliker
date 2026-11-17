# Script to upgrade hero visual to multi-layer 3D glassmorphic interactive stage

# 1. Update HTML in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_html = '''      <!-- Hero Right: MOBIKASA SIGNATURE 3D DEVICE SHOWCASE -->
      <div class="hero-visual-col">
        <div class="search-command-stage" style="position: relative; perspective: 1200px; max-width: 560px; margin: 0 auto;">
          <!-- Ambient Radiant Orange Backlight Spotlight (Mobikasa Aesthetic) -->
          <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 440px; height: 440px; background: radial-gradient(circle, rgba(255, 94, 30, 0.28) 0%, rgba(255, 123, 57, 0.12) 40%, transparent 70%); filter: blur(50px); pointer-events: none; z-index: 0;"></div>

          <!-- Luxury 3D Holographic Showcase Card -->
          <div class="search-terminal-card" style="position: relative; z-index: 1; border-radius: 28px; overflow: hidden; border: 1px solid rgba(255, 94, 30, 0.35); box-shadow: 0 30px 70px rgba(0, 0, 0, 0.45), 0 0 50px rgba(255, 94, 30, 0.2); background: #0c0f17; transform: rotateY(-5deg) rotateX(3deg); transition: transform 0.4s ease, box-shadow 0.4s ease;">
            
            <!-- Terminal Top Window Header -->
            <div style="padding: 13px 20px; background: rgba(18, 23, 34, 0.9); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); display: flex; align-items: center; justify-content: space-between;">
              <div style="display: flex; gap: 8px;">
                <span style="width: 10px; height: 10px; border-radius: 50%; background: #ef4444; display: inline-block;"></span>
                <span style="width: 10px; height: 10px; border-radius: 50%; background: #f59e0b; display: inline-block;"></span>
                <span style="width: 10px; height: 10px; border-radius: 50%; background: #10b981; display: inline-block;"></span>
              </div>
              <div style="font-size: 0.78rem; font-weight: 700; color: #cbd5e1; display: flex; align-items: center; gap: 7px; letter-spacing: 0.03em;">
                <span style="width: 7px; height: 7px; border-radius: 50%; background: #10b981; box-shadow: 0 0 10px #10b981;"></span>
                <span>MOBIKASA-INSPIRED 3D HARDWARE SHOWCASE</span>
              </div>
              <div style="font-size: 0.72rem; color: #ff5e1e; font-weight: 800; background: rgba(255, 94, 30, 0.15); border: 1px solid rgba(255, 94, 30, 0.3); padding: 3px 10px; border-radius: 999px;">GROWTH ENGINE</div>
            </div>

            <!-- Photorealistic 3D Mobikasa Flagship Device Showcase Image -->
            <div style="position: relative; width: 100%; aspect-ratio: 16/10; overflow: hidden; background: #07090e;">
              <img src="assets/3d/mobikasa-hero-showcase.png" alt="3D Mobikasa Flagship Smartphone Luxury eCommerce Showcase" style="width: 100%; height: 100%; object-fit: cover; display: block; filter: contrast(1.03);">
              
              <!-- Subtle Scanning Glow Line -->
              <div style="position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, #ff5e1e, #10b981, transparent); box-shadow: 0 0 15px #ff5e1e; animation: scanLine 3.5s infinite linear;"></div>

              <!-- Animated Real-Time Organic Growth Wave (SVG) -->
              <svg viewBox="0 0 500 140" style="position: absolute; bottom: 8px; left: 0; width: 100%; height: 75px; pointer-events: none; opacity: 0.85;">
                <defs>
                  <linearGradient id="heroWaveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#ff5e1e" stop-opacity="0.2"/>
                    <stop offset="45%" stop-color="#ff7b39" stop-opacity="0.9"/>
                    <stop offset="75%" stop-color="#38bdf8" stop-opacity="0.9"/>
                    <stop offset="100%" stop-color="#10b981" stop-opacity="1"/>
                  </linearGradient>
                </defs>
                <path d="M 10 110 Q 70 125 130 85 T 250 55 T 370 35 T 490 12" fill="none" stroke="url(#heroWaveGrad)" stroke-width="3.5" stroke-linecap="round" class="animated-wave-line"/>
              </svg>
            </div>

            <!-- Terminal Bottom HUD Stats Strip -->
            <div style="padding: 16px 20px; background: rgba(12, 16, 26, 0.95); border-top: 1px solid rgba(255, 255, 255, 0.08); display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; text-align: center;">
              <div>
                <div style="font-size: 0.72rem; color: #64748b; font-weight: 700; text-transform: uppercase;">ACTIVE KEYWORDS</div>
                <div style="font-size: 1.15rem; font-weight: 800; color: #ffffff;">4,820+</div>
                <div style="font-size: 0.7rem; color: #10b981; font-weight: 700;">↑ 94% Top-3</div>
              </div>
              <div style="border-left: 1px solid rgba(255,255,255,0.06); border-right: 1px solid rgba(255,255,255,0.06);">
                <div style="font-size: 0.72rem; color: #64748b; font-weight: 700; text-transform: uppercase;">ORGANIC REVENUE</div>
                <div style="font-size: 1.15rem; font-weight: 800; color: #ff5e1e;">$12.4M</div>
                <div style="font-size: 0.7rem; color: #10b981; font-weight: 700;">+340% YoY</div>
              </div>
              <div>
                <div style="font-size: 0.72rem; color: #64748b; font-weight: 700; text-transform: uppercase;">AI CITATIONS</div>
                <div style="font-size: 1.15rem; font-weight: 800; color: #38bdf8;">98.6%</div>
                <div style="font-size: 0.7rem; color: #38bdf8; font-weight: 700;">ChatGPT &amp; Gemini</div>
              </div>
            </div>
          </div>

          <!-- 4 Floating 3D Frosted Glass Badges -->
          <div style="position: absolute; top: -16px; left: -20px; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 14px; padding: 10px 18px; display: flex; align-items: center; gap: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.35); animation: floatBadge 4s ease-in-out infinite;">
            <div style="width: 32px; height: 32px; border-radius: 8px; background: rgba(16, 185, 129, 0.15); color: #10b981; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.9rem;">#1</div>
            <div>
              <div style="font-size: 0.82rem; font-weight: 800; color: #ffffff;">Google Rank #1</div>
              <div style="font-size: 0.7rem; color: #94a3b8;">Commercial Search Query</div>
            </div>
          </div>

          <div style="position: absolute; bottom: 40px; right: -24px; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 14px; padding: 10px 18px; display: flex; align-items: center; gap: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.35); animation: floatBadge 5s ease-in-out infinite reverse;">
            <div style="width: 32px; height: 32px; border-radius: 8px; background: rgba(255, 94, 30, 0.15); color: #ff5e1e; display: flex; align-items: center; justify-content: center;"><i data-lucide="trending-up" style="width: 18px; height: 18px;"></i></div>
            <div>
              <div style="font-size: 0.82rem; font-weight: 800; color: #ffffff;">+340% Traffic Surge</div>
              <div style="font-size: 0.7rem; color: #10b981;">Verified Search Console</div>
            </div>
          </div>
        </div>
      </div>'''

replacement_html = '''      <!-- Hero Right: MULTI-LAYER 3D GLASSMORPHIC HERO STAGE -->
      <div class="hero-visual-col">
        <div class="hero-3d-stage" id="hero3dStage" aria-label="Interactive 3D flagship smartphone and floating analytics showcase">
          
          <!-- Ambient Radiant Backlight Bloom -->
          <div class="hero-3d-ambient-glow" id="heroAmbientGlow"></div>

          <!-- Main 3D Perspective Scene Container -->
          <div class="hero-3d-scene" id="hero3dScene">
            
            <!-- LAYER 0: BASE 3D SMARTPHONE HARDWARE -->
            <div class="phone-3d-chassis" id="phone3dChassis">
              <!-- Metallic Rim & Titanium Bezel -->
              <div class="phone-titanium-bezel">
                
                <!-- Dynamic Island / Speaker Notch -->
                <div class="phone-dynamic-island">
                  <span class="island-camera"></span>
                  <span class="island-sensor"></span>
                </div>

                <!-- Glass Screen & UI Base -->
                <div class="phone-screen-content">
                  <!-- App Header -->
                  <div class="screen-app-bar">
                    <span class="app-brand-title">AURA COMMERCE</span>
                    <div class="app-bar-icons">
                      <span class="app-signal-dot"></span>
                      <span class="app-cart-pill">🛒 2</span>
                    </div>
                  </div>

                  <!-- Hero Showcase Base Artwork -->
                  <div class="screen-hero-art">
                    <img src="assets/3d/mobikasa-hero-showcase.png" alt="3D eCommerce and Search Engine Dominance App Interface" class="screen-base-img" loading="eager">
                    <!-- Subtle Glass Sheen Tracking Mouse -->
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

            <!-- LAYER 1: FLOATING GLASS SEARCH COMMAND BAR (translateZ: 50px) -->
            <div class="glass-card-3d layer-search-bar" id="layerSearchBar" data-parallax-depth="0.045" data-tz="50">
              <div class="glass-search-inner">
                <span class="search-lens-icon">🔍</span>
                <span class="search-input-placeholder">luxury scandinavian lounge</span>
                <span class="search-verified-pill">#1 TOP RESULT</span>
              </div>
            </div>

            <!-- LAYER 2: FLOATING SALES & REVENUE OVERVIEW GRAPH (translateZ: 85px) -->
            <div class="glass-card-3d layer-sales-card" id="layerSalesCard" data-parallax-depth="0.075" data-tz="85">
              <div class="sales-card-header">
                <div>
                  <div class="card-micro-title">SALES &amp; REVENUE OVERVIEW</div>
                  <div class="card-macro-val">+340% <span class="trend-badge">↑ YoY</span></div>
                </div>
                <div class="circular-progress-badge">
                  <span class="progress-num">98%</span>
                </div>
              </div>
              <!-- Mini Bar Chart (Orange & Cyan) -->
              <div class="mini-bar-chart">
                <div class="bar-col"><span class="bar-fill" style="height: 38%;"></span><span class="bar-day">M</span></div>
                <div class="bar-col"><span class="bar-fill" style="height: 52%;"></span><span class="bar-day">T</span></div>
                <div class="bar-col"><span class="bar-fill" style="height: 48%;"></span><span class="bar-day">W</span></div>
                <div class="bar-col"><span class="bar-fill" style="height: 70%;"></span><span class="bar-day">T</span></div>
                <div class="bar-col"><span class="bar-fill" style="height: 64%;"></span><span class="bar-day">F</span></div>
                <div class="bar-col"><span class="bar-fill" style="height: 88%;"></span><span class="bar-day">S</span></div>
                <div class="bar-col"><span class="bar-fill active-bar" style="height: 100%;"></span><span class="bar-day">S</span></div>
              </div>
            </div>

            <!-- LAYER 3: FLOATING ECOMMERCE PRODUCT CONVERSION CARD (translateZ: 105px) -->
            <div class="glass-card-3d layer-product-card" id="layerProductCard" data-parallax-depth="0.09" data-tz="105">
              <div class="prod-card-top">
                <span class="prod-badge">PERFORMANCE RUNNER</span>
                <span class="prod-rating">★ 4.9</span>
              </div>
              <div class="prod-card-mid">
                <div class="prod-info-block">
                  <div class="prod-title">Aura Carbon Sneaker</div>
                  <div class="prod-price">$129 <span class="prod-stock">In Stock</span></div>
                </div>
                <button type="button" class="prod-quick-btn" aria-label="Quick Add to Cart">
                  <span>ADD</span>
                  <span class="btn-plus">+</span>
                </button>
              </div>
            </div>

            <!-- LAYER 4: FLOATING GOOGLE RANK #1 SHIELD BADGE (translateZ: 125px) -->
            <div class="glass-card-3d layer-rank-badge" id="layerRankBadge" data-parallax-depth="0.12" data-tz="125">
              <div class="rank-shield-icon">#1</div>
              <div class="rank-shield-text">
                <div class="rank-main-title">Google Rank #1</div>
                <div class="rank-sub-title">Commercial Query • 48.2k Clicks</div>
              </div>
              <span class="live-pulse-dot"></span>
            </div>

            <!-- LAYER 5: FLOATING TOTAL REVENUE HUD CARD (translateZ: 110px) -->
            <div class="glass-card-3d layer-revenue-card" id="layerRevenueCard" data-parallax-depth="0.1" data-tz="110">
              <div class="rev-card-label">TOTAL REVENUE</div>
              <div class="rev-card-num">$24,560</div>
              <svg class="rev-trend-wave" viewBox="0 0 100 24" fill="none">
                <path d="M 0 18 Q 25 22 50 10 T 100 4" stroke="#ff5e1e" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>

          </div>
        </div>
      </div>'''

if target_html in html:
    html = html.replace(target_html, replacement_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated hero visual in index.html")
else:
    print("Target HTML not found directly, checking partial replacement")
