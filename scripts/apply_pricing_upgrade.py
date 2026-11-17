import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. UPGRADE PRICING SECTION HTML
new_pricing_html = '''<!-- ========================================================================= -->
  <!-- 8. TRANSPARENT PRICING & GROWTH RETAINERS (MOBIKASA 3-TIER ARCHITECTURE)   -->
  <!-- ========================================================================= -->
  <section class="pricing-matrix-section" id="pricing">
    <div class="container">
      <div class="section-header-center">
        <div class="section-pill">PREDICTABLE GROWTH RETAINERS</div>
        <h2 class="section-title">Transparent Monthly Sprints. <span style="font-family: 'Playfair Display', Georgia, serif; font-style: italic; color: #ff5e1e;">Zero Lock-In.</span></h2>
        <p class="section-desc">
          Senior-led organic search and AI citation engineering. No junior hand-offs, no bloated retainers, cancel anytime with 30-day notice.
        </p>

        <!-- Interactive Billing Toggle Switcher -->
        <div class="pricing-toggle-wrap">
          <span class="pricing-toggle-label active" id="labelMonthly">Monthly Sprints</span>
          <button class="pricing-toggle-switch" id="pricingToggleBtn" aria-label="Toggle quarterly billing">
            <span class="pricing-toggle-knob"></span>
          </button>
          <span class="pricing-toggle-label" id="labelQuarterly">
            Quarterly Retainer <span class="pricing-discount-pill">SAVE 15%</span>
          </span>
        </div>
      </div>

      <!-- 3-Tier Luxury Pricing Grid (No 4-card horizontal overflow!) -->
      <div class="luxury-pricing-grid">
        
        <!-- Tier 1: Growth Sprint -->
        <div class="luxury-price-card tilt-card">
          <div class="price-card-header">
            <span class="tier-pill tier-pill-slate">SMB &amp; EMERGING</span>
            <h3 class="tier-name">Growth Sprint</h3>
            <p class="tier-summary">For high-potential businesses establishing rank authority and fixing technical bottlenecks.</p>
          </div>
          <div class="price-figure-row">
            <span class="currency-symbol">₹</span>
            <span class="price-amount" data-monthly="35,000" data-quarterly="29,750">35,000</span>
            <span class="price-cadence">/ month</span>
          </div>
          <div class="price-deliverables-title">WHAT'S INCLUDED:</div>
          <ul class="luxury-features-list">
            <li><i data-lucide="check" class="feat-icon"></i> <strong>25 Target Search Entities</strong></li>
            <li><i data-lucide="check" class="feat-icon"></i> Core Web Vitals Sub-Second Fix</li>
            <li><i data-lucide="check" class="feat-icon"></i> 15 High-DA Editorial Contextual Links</li>
            <li><i data-lucide="check" class="feat-icon"></i> Technical Sitemap &amp; Canonical Overhaul</li>
            <li><i data-lucide="check" class="feat-icon"></i> Bi-Weekly Video Sprints &amp; Reporting</li>
          </ul>
          <a href="get-a-proposal.html?plan=growth" class="btn-price-tier btn-tier-secondary">
            <span>Start Growth Sprint</span>
            <i data-lucide="arrow-up-right" style="width: 16px; height: 16px;"></i>
          </a>
        </div>

        <!-- Tier 2: Market Dominance (Featured / Most Popular) -->
        <div class="luxury-price-card featured tilt-card">
          <div class="featured-top-glow"></div>
          <div class="price-card-header">
            <div class="featured-badge-row">
              <span class="tier-pill tier-pill-orange">MOST POPULAR • ROI LEADER</span>
              <span class="live-pulse-badge"><span class="pulse-dot"></span> Pod Active</span>
            </div>
            <h3 class="tier-name">Market Dominance</h3>
            <p class="tier-summary">Comprehensive multi-channel search authority and Generative AI citation dominance.</p>
          </div>
          <div class="price-figure-row">
            <span class="currency-symbol color-orange">₹</span>
            <span class="price-amount color-orange" data-monthly="75,000" data-quarterly="63,750">75,000</span>
            <span class="price-cadence">/ month</span>
          </div>
          <div class="price-deliverables-title">WHAT'S INCLUDED:</div>
          <ul class="luxury-features-list">
            <li><i data-lucide="check" class="feat-icon feat-orange"></i> <strong>60 High-Intent Commercial Entities</strong></li>
            <li><i data-lucide="check" class="feat-icon feat-orange"></i> <strong>AI &amp; GEO Engine Ingestion</strong> (ChatGPT, Gemini)</li>
            <li><i data-lucide="check" class="feat-icon feat-orange"></i> 35 Tier-1 Editorial Contextual Backlinks/mo</li>
            <li><i data-lucide="check" class="feat-icon feat-orange"></i> 3D Headless &amp; Interactive Storefront SEO</li>
            <li><i data-lucide="check" class="feat-icon feat-orange"></i> Dedicated Senior Search Director Pod</li>
            <li><i data-lucide="check" class="feat-icon feat-orange"></i> Real-Time Looker Revenue Attribution</li>
          </ul>
          <a href="get-a-proposal.html?plan=dominance" class="btn-price-tier btn-tier-primary">
            <span>Claim Market Dominance</span>
            <i data-lucide="zap" style="width: 16px; height: 16px;"></i>
          </a>
        </div>

        <!-- Tier 3: Enterprise Authority -->
        <div class="luxury-price-card tilt-card">
          <div class="price-card-header">
            <span class="tier-pill tier-pill-slate">GLOBAL &amp; E-COMMERCE</span>
            <h3 class="tier-name">Enterprise Authority</h3>
            <p class="tier-summary">For high-traffic national brands and multi-market e-commerce catalogs needing custom engineering.</p>
          </div>
          <div class="price-figure-row">
            <span class="currency-symbol">₹</span>
            <span class="price-amount" data-monthly="1,45,000" data-quarterly="1,23,250">1,45,000</span>
            <span class="price-cadence">/ month</span>
          </div>
          <div class="price-deliverables-title">WHAT'S INCLUDED:</div>
          <ul class="luxury-features-list">
            <li><i data-lucide="check" class="feat-icon"></i> <strong>150+ Semantic Topic Clusters</strong> (Multi-Region)</li>
            <li><i data-lucide="check" class="feat-icon"></i> Dedicated 5-Person Pod (Director, Dev, PR)</li>
            <li><i data-lucide="check" class="feat-icon"></i> Programmatic SEO &amp; Multi-Catalog Crawl</li>
            <li><i data-lucide="check" class="feat-icon"></i> Guaranteed 90+ Mobile Core Web Vitals</li>
            <li><i data-lucide="check" class="feat-icon"></i> Thought Leadership Digital PR Newsroom</li>
            <li><i data-lucide="check" class="feat-icon"></i> Weekly Boardroom Strategy &amp; 24/7 SLA</li>
          </ul>
          <a href="get-a-proposal.html?plan=enterprise" class="btn-price-tier btn-tier-secondary">
            <span>Schedule Enterprise Briefing</span>
            <i data-lucide="arrow-up-right" style="width: 16px; height: 16px;"></i>
          </a>
        </div>

      </div>

      <!-- Enterprise Dedicated Squad Banner (Mobikasa Style) -->
      <div class="enterprise-squad-banner">
        <div class="squad-info">
          <div class="squad-avatars">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80" alt="Specialist" class="squad-avatar">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80" alt="Specialist" class="squad-avatar">
            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=120&q=80" alt="Specialist" class="squad-avatar">
            <div class="squad-avatar-more">+120</div>
          </div>
          <div>
            <h4 class="squad-title">Need a Custom Dedicated Search &amp; 3D Engineering Pod?</h4>
            <p class="squad-desc">We embed cross-functional squads (SEO Architect, Full-Stack Dev, Digital PR Lead) directly into your Slack &amp; Jira workflows.</p>
          </div>
        </div>
        <a href="get-a-proposal.html?plan=custom-pod" class="btn-squad-action">
          <span>Build Custom Pod Scope</span>
          <i data-lucide="arrow-right" style="width: 16px; height: 16px;"></i>
        </a>
      </div>

    </div>
  </section>'''

# Replace pricing section in index.html
m_price = re.search(r'<section[^>]*id="pricing".*?</section>', html, re.DOTALL)
if m_price:
    html = html[:m_price.start()] + new_pricing_html + html[m_price.end():]
    print("Replaced pricing section successfully!")
else:
    print("Could not find pricing section")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html!")
