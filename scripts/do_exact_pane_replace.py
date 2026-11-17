with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Legacy visual pane
leg_start = html.find('<div class="trans-3d-visual-pane legacy-visual-pane">')
leg_end_marker = '<!-- Right: Failure Items Checklist + Decline Chart -->'
leg_end = html.find(leg_end_marker, leg_start)

legacy_pane_replacement = '''<div class="trans-3d-visual-pane legacy-visual-pane">
                <div class="photoreal-3d-wrap floating-3d-legacy">
                  <img src="assets/3d/legacy_server_3d_photoreal.png" alt="3D Legacy Server Stack" class="photoreal-3d-img legacy-3d-img">
                </div>
              </div>

              '''

html = html[:leg_start] + legacy_pane_replacement + html[leg_end:]

# 2. Replace Modern visual pane
mod_start = html.find('<div class="trans-3d-visual-pane modern-visual-pane">')
mod_end_marker = '<!-- Right: Success Items Checklist + Revenue Curve -->'
mod_end = html.find(mod_end_marker, mod_start)

modern_pane_replacement = '''<div class="trans-3d-visual-pane modern-visual-pane">
                <div class="photoreal-3d-wrap floating-3d-modern">
                  <img src="assets/3d/modern_tech_3d_photoreal.png" alt="3D Modernized Headless Architecture Stack" class="photoreal-3d-img modern-3d-img">
                </div>
              </div>

              '''

html = html[:mod_start] + modern_pane_replacement + html[mod_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully replaced both 3D panes in index.html with photoreal 3D elements!")
