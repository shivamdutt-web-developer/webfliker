# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define new seamless 3D hero stage HTML
new_stage_html = '''        <div class="hero-3d-stage" id="hero3dStage" aria-label="Interactive 3D flagship smartphone and focused analytics showcase">
          
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
                <p class="mobi-card-desc">Sub-second Shopify Plus speed & 98.6% AI citation authority.</p>
              </div>
              <div class="mobi-card-tags">
                <span class="mobi-tag tag-cyan">ChatGPT</span>
                <span class="mobi-tag tag-emerald">Gemini Active</span>
              </div>
            </div>

          </div>
        </div>'''

# Find hero-3d-stage in index.html
start = html.find('<div class="hero-3d-stage" id="hero3dStage"')
if start != -1:
    end = html.find('</div>\n      </div>\n\n      <!-- Mobile Quick CTA Bar', start)
    if end == -1:
        # Fallback end search
        end = html.find('</div>\n      </div>\n\n      <!-- Mobile', start)
    if end == -1:
        end = html.find('<!-- Mobile Quick CTA Bar', start)
        # Search backwards for closing div
        end = html.rfind('</div>', 0, end)
        end = html.rfind('</div>', 0, end)
        
    # Let's cleanly replace from start of hero-3d-stage to the closing tag of hero-3d-stage
    stage_close = html.find('<!-- Mobile Quick CTA Bar', start)
    # The stage ends right before the parent column ends
    col_end = html.rfind('</div>', 0, stage_close)
    stage_end = html.rfind('</div>', 0, col_end) + len('</div>')
    
    html = html[:start] + new_stage_html + html[stage_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced hero-3d-stage with seamless Mobikasa phone!")
else:
    print("Could not find hero-3d-stage in index.html")
