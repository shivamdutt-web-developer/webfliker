import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Upgraded Mobikasa Founder Spotlight Section
new_founder_html = '''<!-- ========================================================================= -->
  <!-- 5. FOUNDER & LEADERSHIP SPOTLIGHT ("LAST AGENCY YOU EVER WORK WITH")       -->
  <!-- ========================================================================= -->
  <section class="founder-spotlight-section" id="founder-spotlight">
    <div class="container">
      <div class="founder-stage-panel">
        <div class="founder-ambient-glow"></div>
        <div class="founder-grid-row">
          
          <!-- Left: Founder Portrait Card -->
          <div class="founder-portrait-col">
            <div class="founder-card-chassis">
              <div class="founder-img-wrapper">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=700&q=80" alt="Navneet Kaushal - Founder & Principal Strategist" class="founder-img">
                <div class="founder-badge-floating">
                  <span class="badge-dot-green"></span> 24+ Yrs Search Mastery
                </div>
              </div>
              <div class="founder-meta-bar">
                <div>
                  <h3 class="founder-name">Navneet Kaushal</h3>
                  <div class="founder-role">Founder &amp; Principal Search Architect</div>
                </div>
                <div class="founder-icon-seal">
                  <i data-lucide="shield-check" style="width: 20px; height: 20px; color: #ff5e1e;"></i>
                </div>
              </div>
            </div>
          </div>

          <!-- Right: The Founder Commitment -->
          <div class="founder-content-col">
            <div class="section-pill pill-warm-dark">
              <span style="color: #ff5e1e;">✦</span> EXECUTIVE COMMITMENT
            </div>
            
            <h2 class="founder-headline">
              "We'll Be the Last Search Agency You Ever Need to Hire."
            </h2>
            
            <div class="founder-quote-box">
              "Search has always been about earning unshakeable trust. Since 2002, we've helped 500+ brands earn it wherever customers search, compare, and decide. Now, that includes generative AI platforms like ChatGPT, Gemini, and SGE. We don't sell transient clicks; we build compound market equity."
            </div>
            
            <p class="founder-body-p">
              Every enterprise account is directly steered by senior search directors who have steered brands through every major algorithm shift from Florida (2003) and Panda (2011) to the Generative AI Search Core Updates of 2026.
            </p>
            
            <!-- High-Contrast Bulletproof Action Buttons -->
            <div class="founder-btn-group">
              <a href="get-a-proposal.html" class="founder-btn-primary">
                <span>Schedule Strategic Briefing</span>
                <i data-lucide="calendar" style="width: 17px; height: 17px;"></i>
              </a>
              <a href="our-story.html" class="founder-btn-secondary">
                <span>Read Full Story Since 2002</span>
                <i data-lucide="arrow-up-right" style="width: 17px; height: 17px;"></i>
              </a>
            </div>

          </div>

        </div>
      </div>
    </div>
  </section>'''

m_f = re.search(r'<section class="founder-spotlight-section".*?</section>', html, re.DOTALL)
if m_f:
    html = html[:m_f.start()] + new_founder_html + html[m_f.end():]
    print("Replaced founder-spotlight-section successfully!")
else:
    print("Could not match founder-spotlight-section")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html!")
