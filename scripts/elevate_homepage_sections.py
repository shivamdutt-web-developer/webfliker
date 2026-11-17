import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. UPGRADE METHODOLOGY SECTION
# Replace methodology section with an interactive connected roadmap and 3x3 engineering matrix
new_methodology_html = '''  <!-- ========================================================================= -->
  <!-- 4. SEARCH AUTHORITY FRAMEWORK & 9-PHASE LIFECYCLE (CONNECTED ROADMAP)     -->
  <!-- ========================================================================= -->
  <section class="methodology-section" id="methodology">
    <div class="container">
      <div class="section-header-center">
        <div class="section-pill">SYSTEMATIC METHODOLOGY</div>
        <h2 class="section-title">The 4-Stage Search Authority Framework</h2>
        <p class="section-desc">
          Tested over 24 years across 5,000+ campaigns, our systematic methodology eliminates guesswork and delivers predictable, compounding organic market equity.
        </p>
      </div>

      <!-- Connected 4-Stage Process Track -->
      <div class="process-roadmap-wrap">
        <div class="process-roadmap-line"></div>
        <div class="process-grid-4">
          
          <!-- Stage 1 -->
          <div class="process-step-card tilt-card">
            <div class="step-badge-row">
              <span class="step-num-pill">STAGE 01</span>
              <div class="step-icon-wrap icon-orange">
                <i data-lucide="search" style="width: 20px; height: 20px;"></i>
              </div>
            </div>
            <h4 class="step-title">Architectural &amp; Algorithmic Audit</h4>
            <p class="step-desc">Deconstruct your full technical stack, indexability, crawl tree, and backlink topology to expose structural growth blockers.</p>
            <div class="step-deliverables">
              <span>✓ Crawl budget modeling</span>
              <span>✓ Core Web Vitals profiling</span>
            </div>
          </div>

          <!-- Stage 2 -->
          <div class="process-step-card tilt-card">
            <div class="step-badge-row">
              <span class="step-num-pill">STAGE 02</span>
              <div class="step-icon-wrap icon-cyan">
                <i data-lucide="network" style="width: 20px; height: 20px;"></i>
              </div>
            </div>
            <h4 class="step-title">Intent Mapping &amp; Content Graph</h4>
            <p class="step-desc">Map the full universe of high-intent search queries and conversational AI prompts to architect authoritative topic clusters.</p>
            <div class="step-deliverables">
              <span>✓ Semantic entity schemas</span>
              <span>✓ Keyword intent clustering</span>
            </div>
          </div>

          <!-- Stage 3 -->
          <div class="process-step-card tilt-card">
            <div class="step-badge-row">
              <span class="step-num-pill">STAGE 03</span>
              <div class="step-icon-wrap icon-purple">
                <i data-lucide="award" style="width: 20px; height: 20px;"></i>
              </div>
            </div>
            <h4 class="step-title">Authority &amp; Digital PR Ingestion</h4>
            <p class="step-desc">Execute data-driven editorial digital PR to earn permanent contextual tier-1 backlinks that establish enduring domain authority.</p>
            <div class="step-deliverables">
              <span>✓ DA 60+ editorial links</span>
              <span>✓ Thought leadership newsroom</span>
            </div>
          </div>

          <!-- Stage 4 -->
          <div class="process-step-card tilt-card">
            <div class="step-badge-row">
              <span class="step-num-pill">STAGE 04</span>
              <div class="step-icon-wrap icon-emerald">
                <i data-lucide="trending-up" style="width: 20px; height: 20px;"></i>
              </div>
            </div>
            <h4 class="step-title">AI Citations &amp; Revenue Scaling</h4>
            <p class="step-desc">Optimize entity footprints for LLM citation dominance across ChatGPT, Gemini, and SGE while driving compounding revenue.</p>
            <div class="step-deliverables">
              <span>✓ SGE featured source</span>
              <span>✓ Multi-touch attribution</span>
            </div>
          </div>

        </div>
      </div>

      <!-- 9-Phase Execution Matrix Header -->
      <div style="margin-top: 80px; text-align: center;">
        <div class="section-pill">9-PHASE LIFECYCLE</div>
        <h3 style="font-size: clamp(1.8rem, 2.8vw, 2.4rem); font-weight: 800; color: #0f172a; margin: 12px 0;">From Baseline Audit to Global SERP Monopoly</h3>
        <p style="color: #64748b; font-size: 1.05rem; max-width: 650px; margin: 0 auto 40px;">
          Our battle-tested 9-phase search engineering sprints executed by dedicated senior delivery pods.
        </p>
      </div>

      <!-- 3x3 Phase Matrix -->
      <div class="phase-matrix-grid">
        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-orange">PHASE 01</span>
            <i data-lucide="file-search" style="width: 18px; height: 18px; color: #ff5e1e;"></i>
          </div>
          <h4 class="phase-title">Discovery &amp; Baseline Modeling</h4>
          <p class="phase-desc">Stakeholder alignment, revenue funnel mapping, KPI baseline setting, and historical penalty screening.</p>
        </div>

        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-cyan">PHASE 02</span>
            <i data-lucide="cpu" style="width: 18px; height: 18px; color: #0284c7;"></i>
          </div>
          <h4 class="phase-title">Technical Architecture Audit</h4>
          <p class="phase-desc">Crawl budget verification, Core Web Vitals optimization, sitemap overhauls, and canonical routing.</p>
        </div>

        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-emerald">PHASE 03</span>
            <i data-lucide="git-branch" style="width: 18px; height: 18px; color: #059669;"></i>
          </div>
          <h4 class="phase-title">Competitor Gap &amp; Entity Analysis</h4>
          <p class="phase-desc">Reverse-engineering domain velocity, content depth, and conversational AI citation presence of market leaders.</p>
        </div>

        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-purple">PHASE 04</span>
            <i data-lucide="layers" style="width: 18px; height: 18px; color: #7e22ce;"></i>
          </div>
          <h4 class="phase-title">Commercial Keyword Clustering</h4>
          <p class="phase-desc">Semantic grouping of terms by transactional intent to eradicate keyword cannibalization and maximize conversions.</p>
        </div>

        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-rose">PHASE 05</span>
            <i data-lucide="layout" style="width: 18px; height: 18px; color: #e11d48;"></i>
          </div>
          <h4 class="phase-title">On-Page &amp; UX Refactoring</h4>
          <p class="phase-desc">Optimizing H1-H3 hierarchies, contextual internal linking, OpenGraph schemas, and mobile micro-interactions.</p>
        </div>

        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-amber">PHASE 06</span>
            <i data-lucide="book-open" style="width: 18px; height: 18px; color: #d97706;"></i>
          </div>
          <h4 class="phase-title">Topical Authority Content Engine</h4>
          <p class="phase-desc">Production of comprehensive pillar guides and technical whitepapers engineered for Google &amp; LLM ingestion.</p>
        </div>

        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-indigo">PHASE 07</span>
            <i data-lucide="share-2" style="width: 18px; height: 18px; color: #4f46e5;"></i>
          </div>
          <h4 class="phase-title">Editorial Authority &amp; Digital PR</h4>
          <p class="phase-desc">Manual outreach to top industry publications to secure permanent contextual backlinks on DA 60+ domains.</p>
        </div>

        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-teal">PHASE 08</span>
            <i data-lucide="sparkles" style="width: 18px; height: 18px; color: #0d9488;"></i>
          </div>
          <h4 class="phase-title">AI Engine Optimization (GEO)</h4>
          <p class="phase-desc">Structuring knowledge graphs and Wikidata entity footprints so ChatGPT, Gemini, and Perplexity recommend your brand.</p>
        </div>

        <div class="phase-item-card tilt-card">
          <div class="phase-top">
            <span class="phase-badge phase-badge-green">PHASE 09</span>
            <i data-lucide="bar-chart-3" style="width: 18px; height: 18px; color: #16a34a;"></i>
          </div>
          <h4 class="phase-title">Continuous CRO &amp; Attribution</h4>
          <p class="phase-desc">Real-time rank tracking, revenue attribution dashboards, bounce-rate reduction, and iterative bi-weekly sprints.</p>
        </div>
      </div>
    </div>
  </section>'''

# 2. UPGRADE COMPARISON SECTION
new_comparison_html = '''  <!-- ========================================================================= -->
  <!-- 10. COMPETITIVE ADVANTAGE MATRIX (LUXURY SAAS FEATURE MATRIX)             -->
  <!-- ========================================================================= -->
  <section class="comparison-section" id="comparison">
    <div class="container">
      <div class="section-header-center">
        <div class="section-pill">THE WEBFLIKR ADVANTAGE</div>
        <h2 class="section-title">Why Industry Leaders Choose Us Over Others</h2>
        <p class="section-desc">
          How our integrated engineering and creative model outpaces traditional siloed agencies and isolated freelancers.
        </p>
      </div>

      <!-- Luxury Feature Matrix Container -->
      <div class="luxury-matrix-wrap">
        <table class="luxury-matrix-table">
          <thead>
            <tr>
              <th class="col-feature">Capability &amp; Deliverables</th>
              <th class="col-webflikr">
                <div class="matrix-brand-badge">WEBFLIKR AGENCY</div>
                <div class="matrix-sub">Integrated Enterprise Pod</div>
              </th>
              <th class="col-other">Typical Freelancer</th>
              <th class="col-other">Legacy Agency</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="feature-title">
                <strong>Team Scale &amp; Delivery</strong>
                <span>Direct senior architect steering with 0 junior hand-offs</span>
              </td>
              <td class="cell-webflikr">
                <span class="badge-check">✓ 120+ In-House Specialists</span>
              </td>
              <td class="cell-other">Solo Individual (Single Point of Failure)</td>
              <td class="cell-other">Outsourced Junior Subcontractors</td>
            </tr>
            <tr>
              <td class="feature-title">
                <strong>AI Search Optimization (AEO 2026)</strong>
                <span>Optimization for ChatGPT, Gemini, Perplexity &amp; SGE</span>
              </td>
              <td class="cell-webflikr">
                <span class="badge-check">✓ Full LLM Entity Ingestion</span>
              </td>
              <td class="cell-other">Not Covered</td>
              <td class="cell-other">Outdated Keyword Stuffing</td>
            </tr>
            <tr>
              <td class="feature-title">
                <strong>3D WebGL &amp; E-Commerce Craft</strong>
                <span>Interactive customizers, headless Shopify Plus &amp; Next.js</span>
              </td>
              <td class="cell-webflikr">
                <span class="badge-check">✓ Custom 60 FPS Interactive</span>
              </td>
              <td class="cell-other">Off-the-shelf Templates</td>
              <td class="cell-other">Heavy Bloated Themes</td>
            </tr>
            <tr>
              <td class="feature-title">
                <strong>Attribution &amp; Live Reporting</strong>
                <span>Transparent revenue attribution and real-time dashboards</span>
              </td>
              <td class="cell-webflikr">
                <span class="badge-check">✓ Real-Time Looker Dashboard</span>
              </td>
              <td class="cell-other">Ad-hoc Screenshots</td>
              <td class="cell-other">End-of-month Static PDF</td>
            </tr>
            <tr>
              <td class="feature-title">
                <strong>Core Web Vitals Guarantee</strong>
                <span>Sub-second LCP, perfect mobile CLS &amp; INP benchmarks</span>
              </td>
              <td class="cell-webflikr">
                <span class="badge-check">✓ 90+ Mobile Score Guaranteed</span>
              </td>
              <td class="cell-other">No Guarantee</td>
              <td class="cell-other">Extra Add-on Charge</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>'''

# 3. UPGRADE MILESTONES TIMELINE SECTION
new_milestones_html = '''  <!-- ========================================================================= -->
  <!-- 11. AGENCY HERITAGE & 24-YEAR MILESTONES TIMELINE                         -->
  <!-- ========================================================================= -->
  <section class="milestones-timeline-section" id="milestones">
    <div class="container">
      <div class="section-header-center">
        <div class="section-pill">AGENCY HERITAGE</div>
        <h2 class="section-title">An Agency Since Before SEO Was a Category.</h2>
        <p class="section-desc">
          From the infancy of web search in 2002 to generative AI answer engines in 2026, trace our 24-year evolution of search dominance.
        </p>
      </div>

      <!-- Glowing Timeline Track -->
      <div class="timeline-interactive-wrap">
        <div class="timeline-track-glow"></div>
        <div class="timeline-cards-row">
          
          <div class="timeline-card tilt-card">
            <div class="timeline-node-dot"></div>
            <span class="timeline-year-pill">2002</span>
            <h4 class="timeline-title">Agency Founded</h4>
            <p class="timeline-desc">Established with a founding mission to help ambitious businesses acquire customers daily through pure organic search authority.</p>
          </div>

          <div class="timeline-card tilt-card">
            <div class="timeline-node-dot"></div>
            <span class="timeline-year-pill">2008</span>
            <h4 class="timeline-title">Red Herring Asia</h4>
            <p class="timeline-desc">Awarded the prestigious Red Herring 100 Asia Award for pioneering scalable search marketing technology and transparent rank reporting.</p>
          </div>

          <div class="timeline-card tilt-card">
            <div class="timeline-node-dot"></div>
            <span class="timeline-year-pill">2015</span>
            <h4 class="timeline-title">5,000+ Sprints</h4>
            <p class="timeline-desc">Surpassed 5,000 completed organic growth campaigns across North America, Europe, and Asia-Pacific with a 98.4% client retention rate.</p>
          </div>

          <div class="timeline-card tilt-card">
            <div class="timeline-node-dot"></div>
            <span class="timeline-year-pill">2021</span>
            <h4 class="timeline-title">Upxano &amp; 3D Lab</h4>
            <p class="timeline-desc">Deployed proprietary enterprise rank tracker Upxano and launched our 3D headless eCommerce engineering studio.</p>
          </div>

          <div class="timeline-card timeline-card-active tilt-card">
            <div class="timeline-node-dot active-pulse"></div>
            <span class="timeline-year-pill pill-active">2026</span>
            <h4 class="timeline-title text-white">Generative Engine AI</h4>
            <p class="timeline-desc text-slate">Pioneering Generative Engine Optimization (GEO) ensuring clients dominate AI answers on ChatGPT, Google Gemini, and Perplexity.</p>
          </div>

        </div>
      </div>
    </div>
  </section>'''

# 4. UPGRADE INSTANT DOMAIN SCANNER SECTION
new_scanner_html = '''  <!-- ========================================================================= -->
  <!-- 16. INSTANT 60-SECOND TECHNICAL DOMAIN SCANNER (HIGH-TECH TERMINAL)       -->
  <!-- ========================================================================= -->
  <section class="instant-scanner-section" id="instant-scanner">
    <div class="container">
      <div class="scanner-terminal-box">
        <!-- Terminal Header -->
        <div class="terminal-bar">
          <div class="term-dots">
            <span class="dot-red"></span>
            <span class="dot-yellow"></span>
            <span class="dot-green"></span>
          </div>
          <span class="terminal-label">upxano-engine://realtime-serp-audit.v26</span>
          <div class="terminal-status-live">
            <span class="live-blink-dot"></span> LIVE SCANNER
          </div>
        </div>

        <div class="terminal-inner-content">
          <div class="section-pill" style="margin-bottom: 12px; background: rgba(255, 94, 30, 0.15); border-color: rgba(255, 94, 30, 0.35); color: #ff7b39;">
            INSTANT SERP DIAGNOSTIC
          </div>
          <h2 class="scanner-heading">Test Your Website's Real Search Potential</h2>
          <p class="scanner-subheading">
            Enter your domain below to run a real-time diagnostic scan covering Core Web Vitals, crawl accessibility, and AI citation readiness.
          </p>

          <!-- Input Row -->
          <form class="scanner-form-row" onsubmit="event.preventDefault(); alert('Scanning ' + document.getElementById('scanDomain').value + '... Diagnostic report generated!');">
            <div class="scanner-input-group">
              <i data-lucide="globe" style="width: 18px; height: 18px; color: #94a3b8;"></i>
              <input type="url" id="scanDomain" placeholder="https://yourbrand.com" required class="scanner-field">
            </div>
            <div class="scanner-input-group">
              <i data-lucide="mail" style="width: 18px; height: 18px; color: #94a3b8;"></i>
              <input type="email" placeholder="corporate@yourbrand.com" required class="scanner-field">
            </div>
            <button type="submit" class="scanner-btn-submit">
              <span>RUN REAL-TIME AUDIT</span>
              <i data-lucide="zap" style="width: 16px; height: 16px;"></i>
            </button>
          </form>

          <!-- Live Audit Checklist Badges -->
          <div class="scanner-checklist-badges">
            <span><i data-lucide="check" style="width: 14px; height: 14px; color: #10b981;"></i> Core Web Vitals (LCP/INP/CLS)</span>
            <span><i data-lucide="check" style="width: 14px; height: 14px; color: #10b981;"></i> SGE &amp; Gemini Knowledge Ingestion</span>
            <span><i data-lucide="check" style="width: 14px; height: 14px; color: #10b981;"></i> Crawl Budget Waste &amp; 404 Leaks</span>
            <span><i data-lucide="check" style="width: 14px; height: 14px; color: #10b981;"></i> Competitor Authority Gap</span>
          </div>
        </div>
      </div>
    </div>
  </section>'''

# 5. UPGRADE GLOBAL HUBS SECTION
new_hubs_html = '''  <!-- ========================================================================= -->
  <!-- 17. STRATEGIC GLOBAL HUBS (INTERNATIONAL DELIVERY DIRECTORY)              -->
  <!-- ========================================================================= -->
  <section class="global-offices-section" id="global-hubs">
    <div class="container">
      <div class="section-header-center">
        <div class="section-pill">GLOBAL PRESENCE</div>
        <h2 class="section-title">Four Strategic Global Delivery Hubs.</h2>
        <p class="section-desc">
          Physical offices and enterprise search directors across premier commercial centers in India, the United Kingdom, and the United States.
        </p>
      </div>

      <div class="global-hubs-grid">
        <!-- Hub 1: Delhi -->
        <div class="hub-card tilt-card">
          <div class="hub-header-row">
            <span class="hub-flag">🇮🇳</span>
            <span class="hub-role-badge badge-hq">GLOBAL HQ</span>
          </div>
          <h3 class="hub-city-name">New Delhi, India</h3>
          <p class="hub-address">15F, Eros Corporate Tower, Nehru Place, New Delhi, 110019</p>
          <div class="hub-tz-row">
            <span class="tz-dot"></span> IST (UTC+5:30) • Full Engineering Pod
          </div>
          <a href="tel:+919212521444" class="hub-contact-link">
            <i data-lucide="phone" style="width: 15px; height: 15px;"></i> +91 92125 21444
          </a>
        </div>

        <!-- Hub 2: Mumbai -->
        <div class="hub-card tilt-card">
          <div class="hub-header-row">
            <span class="hub-flag">🇮🇳</span>
            <span class="hub-role-badge badge-fin">FINANCIAL HUB</span>
          </div>
          <h3 class="hub-city-name">Mumbai, India</h3>
          <p class="hub-address">Raheja Centre Point, 2nd Floor, 294 CST Road, Kalina, Santacruz (E), Mumbai, 400098</p>
          <div class="hub-tz-row">
            <span class="tz-dot"></span> IST (UTC+5:30) • Enterprise Client Services
          </div>
          <a href="tel:+919212521444" class="hub-contact-link">
            <i data-lucide="phone" style="width: 15px; height: 15px;"></i> +91 92125 21444
          </a>
        </div>

        <!-- Hub 3: London -->
        <div class="hub-card tilt-card">
          <div class="hub-header-row">
            <span class="hub-flag">🇬🇧</span>
            <span class="hub-role-badge badge-eur">EUROPEAN HUB</span>
          </div>
          <h3 class="hub-city-name">London, United Kingdom</h3>
          <p class="hub-address">2nd Floor Studio, 28 Poland St, Soho, London W1F 8QP, United Kingdom</p>
          <div class="hub-tz-row">
            <span class="tz-dot"></span> GMT/BST • Strategy &amp; Digital PR
          </div>
          <a href="tel:+442070978643" class="hub-contact-link">
            <i data-lucide="phone" style="width: 15px; height: 15px;"></i> +44 20 7097 8643
          </a>
        </div>

        <!-- Hub 4: Chicago -->
        <div class="hub-card tilt-card">
          <div class="hub-header-row">
            <span class="hub-flag">🇺🇸</span>
            <span class="hub-role-badge badge-us">NORTH AMERICA HUB</span>
          </div>
          <h3 class="hub-city-name">Chicago, United States</h3>
          <p class="hub-address">1024 N Western Ave, Chicago, IL 60622, United States</p>
          <div class="hub-tz-row">
            <span class="tz-dot"></span> CST (UTC-6) • Client Partnerships
          </div>
          <a href="tel:+18007187603" class="hub-contact-link">
            <i data-lucide="phone" style="width: 15px; height: 15px;"></i> +1 (800) 718-7603
          </a>
        </div>
      </div>
    </div>
  </section>'''

# Replace sections in index.html
# 1. Methodology
m1 = re.search(r'<section class="methodology-section".*?</section>', html, re.DOTALL)
if m1:
    html = html[:m1.start()] + new_methodology_html + html[m1.end():]
    print("Replaced methodology section")
else:
    print("Could not match methodology section")

# 2. Comparison
m2 = re.search(r'<section class="comparison-section".*?</section>', html, re.DOTALL)
if m2:
    html = html[:m2.start()] + new_comparison_html + html[m2.end():]
    print("Replaced comparison section")
else:
    print("Could not match comparison section")

# 3. Milestones
m3 = re.search(r'<section class="milestones-timeline-section".*?</section>', html, re.DOTALL)
if m3:
    html = html[:m3.start()] + new_milestones_html + html[m3.end():]
    print("Replaced milestones section")
else:
    print("Could not match milestones section")

# 4. Instant Scanner
m4 = re.search(r'<section class="instant-scanner-section".*?</section>', html, re.DOTALL)
if m4:
    html = html[:m4.start()] + new_scanner_html + html[m4.end():]
    print("Replaced instant scanner section")
else:
    print("Could not match scanner section")

# 5. Global Hubs
m5 = re.search(r'<section class="global-offices-section".*?</section>', html, re.DOTALL)
if m5:
    html = html[:m5.start()] + new_hubs_html + html[m5.end():]
    print("Replaced global hubs section")
else:
    print("Could not match global hubs section")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with elevated sections!")
