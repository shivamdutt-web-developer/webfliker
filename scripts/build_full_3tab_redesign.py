# Build full 3-tab redesign matching the exact reference images

# 1. New Section HTML
refined_modern_svg_4layer = '''<svg class="trans-isometric-svg" viewBox="0 0 220 250" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <radialGradient id="baseOrangeGlow4L" cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stop-color="#ff7a18" stop-opacity="0.95"/>
                      <stop offset="50%" stop-color="#ff5e1e" stop-opacity="0.35"/>
                      <stop offset="100%" stop-color="#ff5e1e" stop-opacity="0"/>
                    </radialGradient>
                    <linearGradient id="llmTopG4L" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#361f1a"/>
                      <stop offset="100%" stop-color="#170d10"/>
                    </linearGradient>
                    <linearGradient id="webglTopG4L" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#132c4d"/>
                      <stop offset="100%" stop-color="#0a152e"/>
                    </linearGradient>
                    <linearGradient id="nextTopG4L" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#2d2d32"/>
                      <stop offset="100%" stop-color="#0d0d10"/>
                    </linearGradient>
                    <linearGradient id="shopifySlabG4L" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#234215"/>
                      <stop offset="100%" stop-color="#11220a"/>
                    </linearGradient>
                    <linearGradient id="shopifyBagGrad4L" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#9dd345"/>
                      <stop offset="50%" stop-color="#72aa29"/>
                      <stop offset="100%" stop-color="#4e7d17"/>
                    </linearGradient>
                    <filter id="shopifyShadow4L" x="-25%" y="-20%" width="150%" height="150%">
                      <feDropShadow dx="0" dy="8" stdDeviation="7" flood-color="#84cc16" flood-opacity="0.55"/>
                    </filter>
                  </defs>

                  <!-- Base Radiant Ground Glow Ring -->
                  <ellipse cx="110" cy="215" rx="80" ry="22" fill="url(#baseOrangeGlow4L)"/>

                  <!-- Layer 1: LLM Graph (Bottom Slab) -->
                  <g class="tech-slab slab-llm">
                    <polygon points="110,180 178,202 110,224 42,202" fill="url(#llmTopG4L)" stroke="#ff7a18" stroke-width="1.6"/>
                    <polygon points="42,202 110,224 110,235 42,213" fill="#24130f" stroke="#ea580c" stroke-width="1.2"/>
                    <polygon points="110,224 178,202 178,213 110,235" fill="#140a08" stroke="#c2410c" stroke-width="1.2"/>
                    <!-- Icon & Label -->
                    <g transform="translate(74, 208)">
                      <circle cx="6" cy="3" r="2" fill="#ff7a18"/>
                      <circle cx="13" cy="7" r="1.6" fill="#ff7a18"/>
                      <circle cx="18" cy="2" r="1.8" fill="#ff7a18"/>
                      <line x1="6" y1="3" x2="13" y2="7" stroke="#ff7a18" stroke-width="1"/>
                      <line x1="13" y1="7" x2="18" y2="2" stroke="#ff7a18" stroke-width="1"/>
                      <text x="26" y="5.5" font-size="9" font-weight="700" fill="#ffedd5" font-family="system-ui, sans-serif">LLM Graph</text>
                    </g>
                  </g>

                  <!-- Layer 2: WebGL 3D (Middle-Lower Slab) -->
                  <g class="tech-slab slab-webgl">
                    <polygon points="110,144 178,166 110,188 42,166" fill="url(#webglTopG4L)" stroke="#38bdf8" stroke-width="1.6"/>
                    <polygon points="42,166 110,188 110,199 42,177" fill="#0c223c" stroke="#0284c7" stroke-width="1.2"/>
                    <polygon points="110,188 178,166 178,177 110,199" fill="#071526" stroke="#0369a1" stroke-width="1.2"/>
                    <!-- Cube Icon & Label -->
                    <g transform="translate(72, 172)">
                      <polygon points="11,0 18,3.5 11,7 4,3.5" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
                      <polygon points="4,3.5 11,7 11,13 4,9.5" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
                      <polygon points="11,7 18,3.5 18,9.5 11,13" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
                      <text x="26" y="8" font-size="9" font-weight="700" fill="#e0f2fe" font-family="system-ui, sans-serif">WebGL 3D</text>
                    </g>
                  </g>

                  <!-- Layer 3: Next.js (Middle-Upper Slab) -->
                  <g class="tech-slab slab-nextjs">
                    <polygon points="110,108 178,130 110,152 42,130" fill="url(#nextTopG4L)" stroke="#e4e4e7" stroke-width="1.6"/>
                    <polygon points="42,130 110,152 110,163 42,141" fill="#1c1c20" stroke="#a1a1aa" stroke-width="1.2"/>
                    <polygon points="110,152 178,130 178,141 110,163" fill="#0b0b0e" stroke="#71717a" stroke-width="1.2"/>
                    <!-- Next.js N Logo Badge & Label -->
                    <g transform="translate(74, 136)">
                      <circle cx="8" cy="4.5" r="6" fill="#000000" stroke="#ffffff" stroke-width="0.8"/>
                      <text x="5.5" y="7.5" font-size="7.5" font-weight="900" fill="#ffffff" font-family="system-ui, sans-serif">N</text>
                      <text x="22" y="8" font-size="9.5" font-weight="800" fill="#ffffff" font-family="system-ui, sans-serif">Next.js</text>
                    </g>
                  </g>

                  <!-- Layer 4: Shopify Plus (Top Slab) -->
                  <g class="tech-slab slab-shopify">
                    <polygon points="110,72 178,94 110,116 42,94" fill="url(#shopifySlabG4L)" stroke="#4ade80" stroke-width="1.8"/>
                    <polygon points="42,94 110,116 110,127 42,105" fill="#17310d" stroke="#22c55e" stroke-width="1.2"/>
                    <polygon points="110,116 178,94 178,105 110,127" fill="#0c1d06" stroke="#16a34a" stroke-width="1.2"/>
                    <!-- Shopify Icon & Label -->
                    <g transform="translate(68, 100)">
                      <circle cx="8" cy="4.5" r="6" fill="#15803d" stroke="#86efac" stroke-width="0.8"/>
                      <path d="M 6 3.5 C 6 2.5, 9.5 2.5, 10 4 C 10.5 5.5, 6 6, 6 8 C 6 9.5, 10 9.5, 10 8" stroke="#ffffff" stroke-width="1.2" fill="none"/>
                      <text x="21" y="8" font-size="9.5" font-weight="800" fill="#dcfce7" font-family="system-ui, sans-serif">Shopify Plus</text>
                    </g>
                  </g>

                  <!-- Floating 3D Shopify Plus Shopping Bag on Top -->
                  <g class="floating-3d-node shopify-bag-node" filter="url(#shopifyShadow4L)">
                    <path d="M 103 26 C 103 16, 117 16, 117 26" stroke="#f1f5f9" stroke-width="3" fill="none" stroke-linecap="round"/>
                    <polygon points="94,26 126,26 131,56 89,56" fill="url(#shopifyBagGrad4L)" stroke="#bbf7d0" stroke-width="1.2"/>
                    <polygon points="89,56 131,56 127,61 93,61" fill="#3b5e11"/>
                    <path d="M 107 35 C 107 33, 113 33, 114 36 C 115 40, 107 41, 107 46 C 107 49, 114 49, 114 47" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>
                  </g>
                </svg>'''

new_section_html = f'''<section class="transformation-showcase-section" id="transformation-showcase">
    <!-- Floating 3D Background Torus Rings -->
    <div class="trans-3d-bg-element torus-top-left" aria-hidden="true">
      <svg viewBox="0 0 140 140" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="torusGradL" x1="15%" y1="10%" x2="85%" y2="90%">
            <stop offset="0%" stop-color="#ffcaa8"/>
            <stop offset="40%" stop-color="#ff8a4c"/>
            <stop offset="80%" stop-color="#ea580c"/>
            <stop offset="100%" stop-color="#9a3412"/>
          </linearGradient>
          <filter id="torusShadowL" x="-20%" y="-20%" width="150%" height="150%">
            <feDropShadow dx="8" dy="16" stdDeviation="14" flood-color="#ea580c" flood-opacity="0.25"/>
          </filter>
        </defs>
        <path d="M 70 20 C 100 20 120 38 120 70 C 120 102 100 120 70 120 C 40 120 20 102 20 70 C 20 38 40 20 70 20 Z M 70 42 C 53 42 42 54 42 70 C 42 86 53 98 70 98 C 87 98 98 86 98 70 C 98 54 87 42 70 42 Z" fill="url(#torusGradL)" filter="url(#torusShadowL)" transform="rotate(-25 70 70)"/>
      </svg>
    </div>

    <div class="trans-3d-bg-element torus-top-right" aria-hidden="true">
      <svg viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="torusGradR" x1="10%" y1="15%" x2="90%" y2="85%">
            <stop offset="0%" stop-color="#ffd5be"/>
            <stop offset="35%" stop-color="#ff955c"/>
            <stop offset="75%" stop-color="#ea580c"/>
            <stop offset="100%" stop-color="#7c2d12"/>
          </linearGradient>
          <filter id="torusShadowR" x="-20%" y="-20%" width="150%" height="150%">
            <feDropShadow dx="-10" dy="18" stdDeviation="16" flood-color="#ea580c" flood-opacity="0.22"/>
          </filter>
        </defs>
        <path d="M 80 24 C 114 24 136 44 136 80 C 136 116 114 136 80 136 C 46 136 24 116 24 80 C 24 44 46 24 80 24 Z M 80 48 C 61 48 48 62 48 80 C 48 98 61 112 80 112 C 99 112 112 98 112 80 C 112 62 99 48 80 48 Z" fill="url(#torusGradR)" filter="url(#torusShadowR)" transform="rotate(35 80 80)"/>
      </svg>
    </div>

    <div class="container trans-content-container">
      <!-- Section Header with High-Contrast Typography -->
      <div class="trans-header">
        <div class="trans-pill-badge">
          <span class="badge-sparkle-dot"></span> ARCHITECTURAL TRANSFORMATION • 2026 BENCHMARK
        </div>
        <h2 class="trans-title">
          The Anatomy of an <span class="trans-gradient-text">Enterprise Growth Overhaul</span>
        </h2>
        <p class="trans-subtitle">
          Compare the quantifiable performance gap: slow monolithic legacy platforms vs. Webflikr's high-speed 3D headless search architecture.
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

      <!-- DUAL SHOWCASE CARDS CONTAINER WITH 3D PEDESTAL STAGE -->
      <div class="trans-stage-wrapper">
        
        <!-- Center Connecting Energy Trail & Double Chevrons -->
        <div class="trans-center-connector" id="transCenterConnector" aria-hidden="true">
          <svg class="trans-energy-trail-svg" viewBox="0 0 200 80" fill="none">
            <defs>
              <linearGradient id="energyTrailGradRef" x1="0%" y1="50%" x2="100%" y2="50%">
                <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.3"/>
                <stop offset="50%" stop-color="#ff7a18" stop-opacity="0.95"/>
                <stop offset="100%" stop-color="#34d399" stop-opacity="0.8"/>
              </linearGradient>
              <filter id="energyGlowRef" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="4" result="blur"/>
                <feMerge>
                  <feMergeNode in="blur"/>
                  <feMergeNode in="SourceGraphic"/>
                </feMerge>
              </filter>
            </defs>
            <path d="M 0 50 C 60 50, 70 20, 130 35 S 180 15, 200 15" stroke="url(#energyTrailGradRef)" stroke-width="3.5" fill="none" filter="url(#energyGlowRef)"/>
          </svg>
          <div class="trans-center-disc">
            <i data-lucide="chevrons-right" style="width: 22px; height: 22px; color: #ff5e1e;"></i>
          </div>
        </div>

        <div class="trans-cards-grid" id="transCardsGrid">
          
          <!-- ========================================== -->
          <!-- CARD 1: THE LEGACY MONOLITH (PRE-WEBFLIKR) -->
          <!-- ========================================== -->
          <div class="trans-card trans-card-legacy tilt-card" id="cardLegacy">
            <div class="trans-card-reflection"></div>
            <!-- Card Top Bar -->
            <div class="trans-card-topbar">
              <div class="trans-status-tag tag-legacy">
                <span class="pulse-indicator pulse-red"></span> PRE-WEBFLIKR • LEGACY CMS
              </div>
              <div class="trans-impact-badge badge-red-glow">
                -42% TRAFFIC LOSS
              </div>
            </div>

            <!-- Card Header Info -->
            <div class="trans-card-meta">
              <h3 class="trans-card-title text-legacy-title">Monolithic Bloated Infrastructure</h3>
              <p class="trans-card-desc">Legacy multi-plugin CMS with fragmented indexing, 4.8MB uncompressed payloads, and 0 structured AI schemas.</p>
            </div>

            <!-- 2-Column Split: 3D Visual Architecture Stack (Left) + Breakdown Checklist (Right) -->
            <div class="trans-card-inner-split">
              <!-- Left: 3D Legacy Server Architecture Illustration -->
              <div class="trans-3d-visual-pane legacy-visual-pane">
                <svg class="trans-isometric-svg" viewBox="0 0 220 230" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="srvTopG" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#edf2f7"/>
                    </linearGradient>
                    <linearGradient id="srvFrontG" x1="0%" y1="0%" x2="0%" y2="100%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#e2e8f0"/>
                    </linearGradient>
                    <linearGradient id="srvSideG" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#cbd5e1"/>
                      <stop offset="100%" stop-color="#94a3b8"/>
                    </linearGradient>
                    <filter id="srvShadowRef" x="-20%" y="-10%" width="140%" height="140%">
                      <feDropShadow dx="0" dy="10" stdDeviation="7" flood-color="#0f172a" flood-opacity="0.14"/>
                    </filter>
                    <linearGradient id="warnTriGradRef" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#ff733b"/>
                      <stop offset="100%" stop-color="#ea3b16"/>
                    </linearGradient>
                    <filter id="warnGlowRef" x="-30%" y="-30%" width="160%" height="160%">
                      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#ea3b16" flood-opacity="0.55"/>
                    </filter>
                    <radialGradient id="wpSphereGradRef" cx="35%" cy="35%" r="65%">
                      <stop offset="0%" stop-color="#38a5df"/>
                      <stop offset="55%" stop-color="#21759b"/>
                      <stop offset="100%" stop-color="#11435d"/>
                    </radialGradient>
                    <filter id="wpShadowRef" x="-20%" y="-20%" width="140%" height="140%">
                      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#11435d" flood-opacity="0.4"/>
                    </filter>
                  </defs>

                  <!-- Server Blade 3 (Top) -->
                  <g filter="url(#srvShadowRef)">
                    <polygon points="105,75 170,100 105,124 40,100" fill="url(#srvTopG)" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="40,100 105,124 105,142 40,118" fill="url(#srvFrontG)" stroke="#cbd5e1" stroke-width="1"/>
                    <polygon points="105,124 170,100 170,118 105,142" fill="url(#srvSideG)" stroke="#94a3b8" stroke-width="1"/>
                    <circle cx="62" cy="112" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="72" cy="116" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="82" cy="120" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                  </g>

                  <!-- Server Blade 2 (Middle) -->
                  <g filter="url(#srvShadowRef)">
                    <polygon points="105,118 170,143 105,167 40,143" fill="url(#srvTopG)" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="40,143 105,167 105,185 40,161" fill="url(#srvFrontG)" stroke="#cbd5e1" stroke-width="1"/>
                    <polygon points="105,167 170,143 170,161 105,185" fill="url(#srvSideG)" stroke="#94a3b8" stroke-width="1"/>
                    <circle cx="62" cy="155" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="72" cy="159" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="82" cy="163" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                  </g>

                  <!-- Server Blade 1 (Bottom) -->
                  <g filter="url(#srvShadowRef)">
                    <polygon points="105,161 170,186 105,210 40,186" fill="url(#srvTopG)" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="40,186 105,210 105,226 40,202" fill="url(#srvFrontG)" stroke="#cbd5e1" stroke-width="1"/>
                    <polygon points="105,210 170,186 170,202 105,226" fill="url(#srvSideG)" stroke="#94a3b8" stroke-width="1"/>
                    <circle cx="62" cy="197" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="72" cy="201" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="82" cy="205" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                  </g>

                  <!-- Floating 3D WordPress Logo Sphere on Top -->
                  <g class="floating-3d-node wp-node" filter="url(#wpShadowRef)">
                    <circle cx="105" cy="40" r="26" fill="url(#wpSphereGradRef)"/>
                    <ellipse cx="98" cy="27" rx="10" ry="5" fill="#ffffff" opacity="0.45" transform="rotate(-20 98 27)"/>
                    <circle cx="105" cy="40" r="19" stroke="#ffffff" stroke-width="2.2" fill="none" opacity="0.9"/>
                    <path d="M 94 33 L 100 50 L 105 38 L 110 50 L 116 33" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  </g>

                  <!-- 3D Red Warning Triangle Badge in Front -->
                  <g class="floating-3d-node warn-node" filter="url(#warnGlowRef)">
                    <polygon points="152,156 190,218 114,218" fill="url(#warnTriGradRef)" stroke="#ffffff" stroke-width="3" stroke-linejoin="round"/>
                    <text x="152" y="210" font-size="24" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="system-ui, sans-serif">!</text>
                  </g>
                </svg>
              </div>

              <!-- Right: Failure Items Checklist + Decline Chart -->
              <div class="trans-breakdown-pane">
                <div class="trans-check-list">
                  <div class="trans-check-item item-fail">
                    <span class="check-icon icon-fail">✕</span>
                    <span class="check-text">Slow Core Web Vitals (LCP: 4.8s)</span>
                  </div>
                  <div class="trans-check-item item-fail">
                    <span class="check-icon icon-fail">✕</span>
                    <span class="check-text">Blocked Rendering (INP: 420ms)</span>
                  </div>
                  <div class="trans-check-item item-fail">
                    <span class="check-icon icon-fail">✕</span>
                    <span class="check-text">No AI Schema / Structured Data</span>
                  </div>
                  <div class="trans-check-item item-fail">
                    <span class="check-icon icon-fail">✕</span>
                    <span class="check-text">Fragmented Indexing</span>
                  </div>
                </div>

                <!-- 12-Month Visibility Box -->
                <div class="trans-graph-card graph-card-legacy">
                  <div class="graph-card-header">
                    <span class="graph-meta-title">12-MONTH ORGANIC VISIBILITY</span>
                    <span class="graph-meta-badge badge-down">-42% Downward Trend</span>
                  </div>
                  <svg class="trans-mini-chart" viewBox="0 0 280 44" fill="none">
                    <path d="M 10 10 L 70 18 L 130 26 L 190 32 L 270 40" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round"/>
                    <circle cx="10" cy="10" r="3" fill="#ef4444"/>
                    <circle cx="70" cy="18" r="3" fill="#ef4444"/>
                    <circle cx="130" cy="26" r="3" fill="#ef4444"/>
                    <circle cx="190" cy="32" r="3" fill="#ef4444"/>
                    <circle cx="270" cy="40" r="4" fill="#ef4444"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- ======================================================== -->
          <!-- CARD 2: THE MODERNIZED 3D HEADLESS (POST-WEBFLIKR)      -->
          <!-- ======================================================== -->
          <div class="trans-card trans-card-modern tilt-card" id="cardModern">
            <div class="trans-card-reflection"></div>
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
              <h3 class="trans-card-title text-modern-title">High-Performance 3D Headless <span class="highlight-orange">Growth</span></h3>
              <p class="trans-card-desc">Sub-second Shopify Plus / Next.js edge storefront with dynamic 3D WebGL spatial viewer and 100% LLM entity graph ingestion.</p>
            </div>

            <!-- 2-Column Split: 3D Modern Architecture Stack (Left) + Breakdown Checklist (Right) -->
            <div class="trans-card-inner-split">
              <!-- Left: 4-Layered 3D Modern Architecture Stack -->
              <div class="trans-3d-visual-pane modern-visual-pane">
                {refined_modern_svg_4layer}
              </div>

              <!-- Right: Success Items Checklist + Revenue Curve -->
              <div class="trans-breakdown-pane">
                <div class="trans-check-list">
                  <div class="trans-check-item item-pass">
                    <span class="check-icon icon-pass">✓</span>
                    <span class="check-text">Top 1% Global Core Web Vitals (LCP: 0.4s)</span>
                  </div>
                  <div class="trans-check-item item-pass">
                    <span class="check-icon icon-pass">✓</span>
                    <span class="check-text">Instant Edge Rendering (INP: 24ms)</span>
                  </div>
                  <div class="trans-check-item item-pass">
                    <span class="check-icon icon-pass">✓</span>
                    <span class="check-text">100% LLM Entity Graph Ingestion</span>
                  </div>
                  <div class="trans-check-item item-pass">
                    <span class="check-icon icon-pass">✓</span>
                    <span class="check-text">Interactive 3D Product Experience</span>
                  </div>
                </div>

                <!-- 12-Month Revenue Curve Box -->
                <div class="trans-graph-card graph-card-modern">
                  <div class="graph-card-header">
                    <span class="graph-meta-title">12-MONTH ORGANIC REVENUE</span>
                    <span class="graph-meta-badge badge-up">+340% Compound Curve</span>
                  </div>
                  <svg class="trans-mini-chart" viewBox="0 0 280 44" fill="none">
                    <defs>
                      <linearGradient id="chartGradModernLine" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#ff7a18"/>
                        <stop offset="50%" stop-color="#f59e0b"/>
                        <stop offset="100%" stop-color="#10b981"/>
                      </linearGradient>
                      <filter id="nodeGlowModern" x="-30%" y="-30%" width="160%" height="160%">
                        <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="#10b981" flood-opacity="0.9"/>
                      </filter>
                    </defs>
                    <path d="M 10 38 Q 90 34 160 22 T 270 8" stroke="url(#chartGradModernLine)" stroke-width="3" stroke-linecap="round"/>
                    <circle cx="270" cy="8" r="4.5" fill="#10b981" filter="url(#nodeGlowModern)"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- 3D Podium Pedestal Platform Beneath Cards -->
        <div class="trans-stage-pedestal" id="transStagePedestal" aria-hidden="true">
          <div class="pedestal-disc-surface"></div>
          <div class="pedestal-disc-bevel"></div>
        </div>
      </div>

      <!-- BOTTOM METRICS BAR (SYMMETRICALLY SPLIT UNDER PEDESTAL) -->
      <div class="trans-bottom-metrics-wrap" id="transBottomMetrics">
        <!-- Legacy Metrics Left -->
        <div class="trans-metrics-col-group group-legacy">
          <div class="trans-metric-box box-legacy">
            <span class="metric-label">CORE WEB VITALS</span>
            <span class="metric-val text-red">4.8s LCP</span>
          </div>
          <div class="trans-metric-box box-legacy">
            <span class="metric-label">AI OVERVIEWS</span>
            <span class="metric-val text-muted">0 Citations</span>
          </div>
          <div class="trans-metric-box box-legacy">
            <span class="metric-label">ALGORITHM RISK</span>
            <span class="metric-val text-amber">Penalized</span>
          </div>
        </div>

        <!-- Center Golden Divider Line -->
        <div class="trans-metrics-center-divider" id="transMetricsDivider"></div>

        <!-- Modern Metrics Right -->
        <div class="trans-metrics-col-group group-modern">
          <div class="trans-metric-box box-modern">
            <span class="metric-label">CORE WEB VITALS</span>
            <span class="metric-val text-emerald">0.4s LCP</span>
          </div>
          <div class="trans-metric-box box-modern">
            <span class="metric-label">AI ANSWER ENGINE</span>
            <span class="metric-val text-cyan">98.6% Rate</span>
          </div>
          <div class="trans-metric-box box-modern">
            <span class="metric-label">GOOGLE SERP #1s</span>
            <span class="metric-val text-orange">4,820+ #1s</span>
          </div>
        </div>
      </div>

    </div>
  </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
pattern = re.compile(r'<section\s+class=["\']transformation-showcase-section["\']\s+id=["\']transformation-showcase["\']>.*?</section>', re.DOTALL)
m = pattern.search(html)
if m:
    html = html[:m.start()] + new_section_html + html[m.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html successfully!")
else:
    print("Section not found in index.html!")
