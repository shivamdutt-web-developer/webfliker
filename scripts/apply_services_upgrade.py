import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_services_html = '''<!-- ========================================================================= -->
  <!-- 3. MOBIKASA ASYMMETRIC BENTO SHOWCASE (DIGITAL SOLUTIONS & GROWTH)        -->
  <!-- ========================================================================= -->
  <section class="services-section" id="services">
    <div class="container">
      <div class="services-stage-panel">
        <!-- Section Header -->
        <div class="services-header-row">
          <div>
            <div class="section-pill" style="margin-bottom: 14px;">WE OFFER • FULL-STACK CAPABILITIES</div>
            <h2 class="services-main-title">
              Digital Solutions &amp; <span style="font-family: 'Playfair Display', Georgia, serif; font-style: italic; color: #ff5e1e;">Growth Strategy</span>
            </h2>
          </div>
          <div class="services-header-right">
            <p class="services-intro-text">
              Engineered to capture high-intent search market share, maximize conversion rates, and dominate Generative AI answers.
            </p>
            <a href="get-a-proposal.html" class="btn-services-explore">
              <span>Explore All Capabilities</span>
              <i data-lucide="arrow-up-right" style="width: 16px; height: 16px;"></i>
            </a>
          </div>
        </div>

        <!-- Asymmetric Bento Showcase Grid (Mobikasa & Stitch Standard) -->
        <div class="mobikasa-bento-grid">
          
          <!-- Bento 1: Wide Featured Headless E-Commerce & 3D WebGL -->
          <div class="bento-feature-wide tilt-card">
            <div class="bento-content-col">
              <span class="bento-badge badge-orange">FLAGSHIP ECOMMERCE</span>
              <h3 class="bento-heading">Headless E-Commerce &amp; 3D Storefronts</h3>
              <p class="bento-sub">Bespoke Shopify Plus, BigCommerce &amp; Next.js platforms engineered with sub-second speeds, 3D interactive visualizers, and seamless checkout optimization.</p>
              <div class="bento-tags-row">
                <span class="bento-tag">⚡ 0.6s LCP Speed</span>
                <span class="bento-tag">🛍️ Shopify Plus Elite</span>
                <span class="bento-tag">✨ 3D WebGL Configurator</span>
              </div>
              <a href="headless-ecommerce.html" class="bento-cta-link">
                <span>View E-Commerce Architecture</span>
                <i data-lucide="arrow-right" style="width: 15px; height: 15px;"></i>
              </a>
            </div>
            <div class="bento-visual-preview">
              <div class="storefront-preview-card">
                <div class="preview-browser-bar">
                  <span class="p-dot"></span><span class="p-dot"></span><span class="p-dot"></span>
                  <span class="p-url">danetti.com/3d-commerce</span>
                </div>
                <div class="preview-store-body">
                  <div class="preview-metric-pill">
                    <span class="p-green-dot"></span> +38% Conversion Lift
                  </div>
                  <div class="preview-phone-cutout">
                    <img src="assets/3d/mobikasa-flagship-phone.png" alt="Danetti 3D Storefront" class="preview-thumb-img">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Bento 2: AI & Generative Engine Optimization (GEO) -->
          <div class="bento-card-square tilt-card">
            <div class="bento-square-top">
              <span class="bento-badge badge-purple">AEO / GEO 2026</span>
              <div class="bento-icon-glow icon-glow-purple">
                <i data-lucide="sparkles" style="width: 22px; height: 22px;"></i>
              </div>
            </div>
            <h3 class="bento-heading">AI Search &amp; LLM Citations</h3>
            <p class="bento-sub">Optimizing brand knowledge graphs and entity footprints so ChatGPT, Google Gemini, and Perplexity actively cite and recommend your products.</p>
            <div class="ai-citation-pills">
              <span class="ai-pill">ChatGPT Active</span>
              <span class="ai-pill">Gemini Knowledge</span>
              <span class="ai-pill">Perplexity #1</span>
            </div>
            <a href="ai-seo.html" class="bento-cta-link" style="margin-top: auto;">
              <span>Explore AI Search Engine Optimization</span>
              <i data-lucide="arrow-right" style="width: 15px; height: 15px;"></i>
            </a>
          </div>

          <!-- Bento 3: Enterprise Technical SEO & Core Web Vitals -->
          <div class="bento-card-square tilt-card">
            <div class="bento-square-top">
              <span class="bento-badge badge-cyan">TECHNICAL AUDIT</span>
              <div class="bento-icon-glow icon-glow-cyan">
                <i data-lucide="cpu" style="width: 22px; height: 22px;"></i>
              </div>
            </div>
            <h3 class="bento-heading">Core Web Vitals &amp; Architecture</h3>
            <p class="bento-sub">Eliminating crawl budget bottlenecks, unindexed faceted URLs, and JavaScript payload bloat on catalogs with 100k+ to 1M+ URLs.</p>
            <div class="lighthouse-benchmark-card">
              <div class="lh-score-circle">100</div>
              <div class="lh-score-info">
                <strong>Google Lighthouse Score</strong>
                <span>Sub-0.8s LCP • 0 CLS</span>
              </div>
            </div>
            <a href="enterprise-seo.html" class="bento-cta-link" style="margin-top: auto;">
              <span>Inspect Technical Auditing</span>
              <i data-lucide="arrow-right" style="width: 15px; height: 15px;"></i>
            </a>
          </div>

          <!-- Bento 4: High-DA Editorial Authority & Digital PR -->
          <div class="bento-card-square tilt-card">
            <div class="bento-square-top">
              <span class="bento-badge badge-emerald">EDITORIAL PR</span>
              <div class="bento-icon-glow icon-glow-emerald">
                <i data-lucide="award" style="width: 22px; height: 22px;"></i>
              </div>
            </div>
            <h3 class="bento-heading">Digital PR &amp; Authority Ingestion</h3>
            <p class="bento-sub">Data-driven editorial campaigns earning permanent contextual backlinks in top-tier tier-1 publications (Forbes, Business Insider, TechCrunch).</p>
            <div class="pr-publication-strip">
              <span class="pub-tag">Forbes</span>
              <span class="pub-tag">TechCrunch</span>
              <span class="pub-tag">Bloomberg</span>
              <span class="pub-tag">Vogue</span>
            </div>
            <a href="link-building.html" class="bento-cta-link" style="margin-top: auto;">
              <span>View Authority Campaigns</span>
              <i data-lucide="arrow-right" style="width: 15px; height: 15px;"></i>
            </a>
          </div>

          <!-- Bento 5: High-ROAS Performance Marketing & CRO -->
          <div class="bento-feature-wide tilt-card bento-perf-card">
            <div class="bento-content-col">
              <span class="bento-badge badge-orange">CONVERSION ENGINE</span>
              <h3 class="bento-heading">CRO &amp; High-ROAS Paid Growth</h3>
              <p class="bento-sub">Relentless full-funnel CRO experimentation, heatmaps, and Google Performance Max campaigns generating 4.8x average verified return on ad spend.</p>
              <div class="bento-tags-row">
                <span class="bento-tag">📈 4.8x Verified ROAS</span>
                <span class="bento-tag">🎯 Multi-Touch Attribution</span>
                <span class="bento-tag">🧪 Bi-Weekly A/B Split Tests</span>
              </div>
              <a href="ppc.html" class="bento-cta-link">
                <span>View Performance Marketing</span>
                <i data-lucide="arrow-right" style="width: 15px; height: 15px;"></i>
              </a>
            </div>
            <div class="bento-visual-preview perf-visual-preview">
              <div class="perf-metric-chart-box">
                <div class="chart-header-row">
                  <span class="chart-label">VERIFIED ROAS ACCELERATION</span>
                  <span class="chart-roi-stat">+340% YoY</span>
                </div>
                <svg class="chart-svg-line" viewBox="0 0 300 100" fill="none">
                  <path d="M0 80 Q 75 75, 150 45 T 300 15" stroke="url(#perfGrad)" stroke-width="4" stroke-linecap="round"/>
                  <circle cx="300" cy="15" r="6" fill="#ff5e1e"/>
                  <defs>
                    <linearGradient id="perfGrad" x1="0" y1="0" x2="300" y2="0" gradientUnits="userSpaceOnUse">
                      <stop stop-color="#fdba74"/>
                      <stop offset="1" stop-color="#ff5e1e"/>
                    </linearGradient>
                  </defs>
                </svg>
                <div class="chart-footer-row">
                  <span>Baseline Q1</span>
                  <span>Sprint Q2</span>
                  <span style="color: #ff5e1e; font-weight: 800;">Scale Q4 Dominance</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>'''

m_serv = re.search(r'<section[^>]*id="services".*?</section>', html, re.DOTALL)
if m_serv:
    html = html[:m_serv.start()] + new_services_html + html[m_serv.end():]
    print("Replaced services section successfully!")
else:
    print("Could not find services section")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with new services!")
