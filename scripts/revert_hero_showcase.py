# 1. Restore index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- Hero Right: POLISHED 3-ELEMENT 3D HERO SHOWCASE -->'
end_marker = '<!-- ========================================================================= -->\n  <!-- 2. TRUSTED ACCREDITATIONS & AUTHORITY MEDIA STRIP'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    orig_hero_right = """<!-- Hero Right: POLISHED 3-ELEMENT 3D HERO SHOWCASE -->
      <div class="hero-visual-col">
        <div class="hero-3d-stage" id="hero3dStage" aria-label="Interactive 3D flagship smartphone and focused analytics showcase">
          
          <!-- Soft Ambient Orange Backlight Glow -->
          <div class="hero-3d-ambient-glow" id="heroAmbientGlow"></div>

          <!-- Main 3D Perspective Scene Container -->
          <div class="hero-3d-scene" id="hero3dScene">
            
            <!-- PRIMARY FOCAL POINT: SEAMLESS 3D FLAGSHIP SMARTPHONE (ZERO RECTANGULAR EDGES) -->
            <div class="phone-3d-chassis-seamless" id="phone3dChassis">
              <img src="assets/3d/mobikasa-flagship-phone.png" alt="Mobikasa-Inspired 3D Headless eCommerce Flagship Smartphone" class="mobikasa-flagship-phone-img" loading="eager">
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

            <!-- ELEMENT 3: MOBIKASA SIGNATURE FROSTED GLASS CARD (BOTTOM-LEFT, OVERLAPPING PHONE) -->
            <div class="glass-card-3d mobikasa-signature-card" id="layerAiCard" data-parallax-depth="0.075" data-tz="125">
              <div class="mobi-card-header">
                <div class="mobi-icon-box">
                  <i data-lucide="sparkles" style="width: 18px; height: 18px; color: #ff5e1e;"></i>
                </div>
                <div class="mobi-arrow-btn">
                  <i data-lucide="arrow-up-right" style="width: 16px; height: 16px; color: #ffffff;"></i>
                </div>
              </div>
              <div class="mobi-card-content">
                <h4 class="mobi-card-title">Headless 3D Commerce</h4>
                <p class="mobi-card-desc">Sub-second Shopify Plus speed &amp; 98.6% AI citation authority.</p>
              </div>
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
    html = html[:start_idx] + orig_hero_right + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS: index.html reverted!")
else:
    print(f"Warning: markers not found, start: {start_idx}, end: {end_idx}")

# 2. Restore styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

marker = "/* ==========================================================================\n   HERO 3D SPATIAL SHOWCASE & MODEL SWITCHER"
idx = css.find(marker)
if idx != -1:
    css = css[:idx].rstrip() + "\n"
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("SUCCESS: styles.css reverted!")
else:
    print("styles.css marker not found.")

# 3. Restore app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# remove btnHeroPhone wiring
idx_js = js.find('// Hero 3D Spatial View Switcher Wiring')
if idx_js != -1:
    end_js = js.find('  init3dCardTilt();', idx_js)
    if end_js != -1:
        js = js[:idx_js] + js[end_js:]
        print("SUCCESS: Removed hero switcher wiring from app.js!")

# reset camera distance to 7.5
js = js.replace('camera.position.z = 8.8;', 'camera.position.z = 7.5;')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("COMPLETE REVERT DONE!")
