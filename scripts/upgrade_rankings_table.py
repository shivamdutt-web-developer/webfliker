with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = 1161
end_idx = 1231

print(f"Replacing lines {start_idx} to {end_idx}:")
print(lines[start_idx][:50], "...", lines[end_idx-1][:50])

new_content = '''      <!-- REAL CLIENT SERP RANKINGS PROOF (LUMERIXA & UPXANO LIVE DATA RADAR) -->
      <div class="rankings-proof-card tilt-card">
        <div class="rankings-table-header">
          <div>
            <div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 8px;">
              <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#10b981; box-shadow:0 0 10px #10b981;"></span>
              <span style="font-size: 0.76rem; font-weight: 800; color: #10b981; letter-spacing: 0.08em; text-transform: uppercase;">UPXANO LIVE SERP RADAR</span>
            </div>
            <h3 class="rankings-table-title">Real Ranking Dominance Across High-Commercial Queries</h3>
            <p style="color: #94a3b8; font-size: 0.92rem; margin: 6px 0 0;">Live verified keyword movements across competitive e-commerce, pharma, and enterprise clients.</p>
          </div>
          <div style="display: flex; gap: 10px; align-items: center;">
            <span class="rank-pill-badge rank-pill-first"><i data-lucide="check-circle-2" style="width:14px;height:14px;"></i> 14,000+ Keywords Page 1</span>
            <span class="rank-pill-badge rank-pill-top3"><i data-lucide="trending-up" style="width:14px;height:14px;"></i> 98.4% Retention</span>
          </div>
        </div>

        <div class="rankings-table-wrap">
          <table class="serp-proof-table">
            <thead>
              <tr>
                <th>Client / Enterprise Domain</th>
                <th>Target Commercial Keyword</th>
                <th>Monthly Volume</th>
                <th>Baseline Rank</th>
                <th>Current Google Rank</th>
                <th>Quantified Traffic Growth</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong style="color:#ffffff; font-size:0.98rem;">Dentalkart.com</strong> <span style="font-size:0.75rem; color:#94a3b8; display:block;">eCommerce &amp; Medical Supplies</span></td>
                <td><span class="serp-keyword-pill">dental products online</span></td>
                <td style="color:#cbd5e1; font-weight:600;">45,000 / mo</td>
                <td style="color:#94a3b8;">Position #42</td>
                <td><span class="rank-pill-badge rank-pill-first">#1 on Google</span></td>
                <td><span style="color:#34d399; font-weight:800; font-size:0.92rem;">+640% Organic GMV</span></td>
              </tr>
              <tr>
                <td><strong style="color:#ffffff; font-size:0.98rem;">LeaderBicycles.com</strong> <span style="font-size:0.75rem; color:#94a3b8; display:block;">Retail &amp; D2C Cycling</span></td>
                <td><span class="serp-keyword-pill">cycles for men</span></td>
                <td style="color:#cbd5e1; font-weight:600;">74,000 / mo</td>
                <td style="color:#94a3b8;">Position #54</td>
                <td><span class="rank-pill-badge rank-pill-top3">#3 on Google</span></td>
                <td><span style="color:#34d399; font-weight:800; font-size:0.92rem;">+490% Revenue</span></td>
              </tr>
              <tr>
                <td><strong style="color:#ffffff; font-size:0.98rem;">Vibcare.co.in</strong> <span style="font-size:0.75rem; color:#94a3b8; display:block;">Healthcare &amp; Pharma Hub</span></td>
                <td><span class="serp-keyword-pill">pharma franchise india</span></td>
                <td style="color:#cbd5e1; font-weight:600;">33,000 / mo</td>
                <td style="color:#94a3b8;">Position #68</td>
                <td><span class="rank-pill-badge rank-pill-first">#1 on Google</span></td>
                <td><span style="color:#34d399; font-weight:800; font-size:0.92rem;">+820% Inbound Leads</span></td>
              </tr>
              <tr>
                <td><strong style="color:#ffffff; font-size:0.98rem;">ArcmaxArchitect.com</strong> <span style="font-size:0.75rem; color:#94a3b8; display:block;">Architecture &amp; Resort Design</span></td>
                <td><span class="serp-keyword-pill">resort design architects</span></td>
                <td style="color:#cbd5e1; font-weight:600;">22,000 / mo</td>
                <td style="color:#94a3b8;">Position #38</td>
                <td><span class="rank-pill-badge rank-pill-top3">#2 on Google</span></td>
                <td><span style="color:#34d399; font-weight:800; font-size:0.92rem;">+350% High-Ticket Deals</span></td>
              </tr>
              <tr>
                <td><strong style="color:#ffffff; font-size:0.98rem;">Ekprint.in</strong> <span style="font-size:0.75rem; color:#94a3b8; display:block;">B2B Commercial Printing</span></td>
                <td><span class="serp-keyword-pill">visiting card printing</span></td>
                <td style="color:#cbd5e1; font-weight:600;">40,000 / mo</td>
                <td style="color:#94a3b8;">Position #49</td>
                <td><span class="rank-pill-badge rank-pill-top3">#3 on Google</span></td>
                <td><span style="color:#34d399; font-weight:800; font-size:0.92rem;">+510% Repeat B2B Orders</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
'''

lines[start_idx:end_idx] = [new_content]
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("REPLACED SUCCESSFULLY!")
