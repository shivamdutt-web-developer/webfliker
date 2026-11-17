import re

def clean_chunk(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.splitlines()
    code_lines = []
    for l in lines:
        m = re.match(r'^\s*(\d+):\s*(.*)', l)
        if m:
            code_lines.append(m.group(2))
    return code_lines

# Read current index.html (which has top bar, header, nav, hero)
with open('index.html', 'r', encoding='utf-8') as f:
    current_lines = f.readlines()

# Current index.html has hero up to the end of hero section
# Let's find where the hero section ends
hero_end_idx = -1
for idx, l in enumerate(current_lines):
    if '</section>' in l:
        hero_end_idx = idx + 1
        break

hero_part = ''.join(current_lines[:hero_end_idx])

# Read chunks
c2843_lines = clean_chunk('transcript_read_2843.txt')
c2845_lines = clean_chunk('transcript_read_2845.txt')
c2847_lines = clean_chunk('transcript_read_2847.txt')
c2849_lines = clean_chunk('transcript_read_2849.txt')
c2851_lines = clean_chunk('transcript_read_2851.txt')

print("Hero lines:", len(current_lines[:hero_end_idx]))
print("c2843 lines:", len(c2843_lines))
print("c2845 lines:", len(c2845_lines))
print("c2847 lines:", len(c2847_lines))
print("c2849 lines:", len(c2849_lines))
print("c2851 lines:", len(c2851_lines))

# In c2843, line 550 starts inside accreditations-media-section
# Let's see what line 515-549 had:
accred_start = '''
  <!-- ========================================================================= -->
  <!-- 2. TRUSTED ACCREDITATIONS & AUTHORITY MEDIA STRIP                         -->
  <!-- ========================================================================= -->
  <section class="accreditations-media-section" style="position: relative; z-index: 5;">
    <div class="container accreditations-grid">
      <div>
        <div style="font-size: 0.8rem; font-weight: 800; color: #64748b; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 16px;">
          ACCREDITED BY SEARCH LEADERS
        </div>
        <div style="display: flex; gap: 16px; align-items: center; flex-wrap: wrap;">
          <div class="trust-badge-pill">
            <span class="trust-logo-g" style="color: #4285F4; font-weight: 900; font-size: 1.15rem;">G</span>
            <div>
              <div style="font-size: 0.82rem; font-weight: 800; color: #0f172a; line-height: 1.2;">Google Premier Partner</div>
              <div style="font-size: 0.72rem; color: #10b981; font-weight: 700;">Verified ID 5391913525</div>
            </div>
          </div>
          <div class="trust-badge-pill">
            <span style="color: #005a9c; font-weight: 900; font-size: 0.95rem;">BBB</span>
            <div>
              <div style="font-size: 0.82rem; font-weight: 800; color: #0f172a; line-height: 1.2;">A+ Accredited</div>
              <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">24 Yrs Standing</div>
            </div>
          </div>
          <div class="trust-badge-pill">
            <span style="color: #00a4ef; font-weight: 900; font-size: 0.95rem;">MS</span>
            <div>
              <div style="font-size: 0.82rem; font-weight: 800; color: #0f172a; line-height: 1.2;">Microsoft Partner</div>
              <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Advertising Elite</div>
            </div>
          </div>
          <div class="trust-badge-pill">
            <span style="color: #96bf48; font-weight: 900; font-size: 0.95rem;">Shopify</span>
            <div>
              <div style="font-size: 0.82rem; font-weight: 800; color: #0f172a; line-height: 1.2;">Shopify Plus</div>
              <div style="font-size: 0.72rem; color: #10b981; font-weight: 700;">3D Headless Partner</div>
            </div>
          </div>
        </div>
      </div>
'''

# Connect c2843: starts at "      <div>\n        <div style=..."
# Let's inspect where c2843 and c2845 connect
# c2843 ends at line 790
# c2845 starts at line 791
chunk1 = accred_start + '\n'.join(c2843_lines)
chunk2 = '\n'.join(c2845_lines)
chunk3 = '\n'.join(c2847_lines)
chunk4 = '\n'.join(c2849_lines)
chunk5 = '\n'.join(c2851_lines)

# Footer closure after line 2000
footer_closure = '''
        <div>
          <h5 class="footer-col-title">Delivery Hubs</h5>
          <div class="footer-links">
            <span class="footer-link">New Delhi HQ (Eros Tower)</span>
            <span class="footer-link">Mumbai (Raheja Centre)</span>
            <span class="footer-link">London (28 Poland St)</span>
            <span class="footer-link">Chicago (1024 N Western)</span>
          </div>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <div>&copy; 2002&ndash;2026 Webflikr Search Engineering Pvt. Ltd. All rights reserved.</div>
        <div class="footer-bottom-links">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms.html">Terms of Service</a>
          <a href="seo-results.html">Security</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="app.js?v=1794800580"></script>
</body>
</html>
'''

full_html = hero_part + '\n' + chunk1 + '\n' + chunk2 + '\n' + chunk3 + '\n' + chunk4 + '\n' + chunk5 + '\n' + footer_closure

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Saved complete index.html! Total lines:", len(full_html.splitlines()))
