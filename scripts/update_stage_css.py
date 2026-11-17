with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .transformation-showcase-section background
css = css.replace(
'''  background: #060911 !important;
  color: #ffffff !important;
  padding: 110px 0 !important;
  overflow: hidden !important;
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;''',
'''  background: #ffffff !important;
  color: #ffffff !important;
  padding: 100px 0 !important;
  overflow: hidden !important;
  border: none !important;'''
)

# Replace .instant-scanner-section background
css = css.replace(
'''.instant-scanner-section {
  padding: 100px 0;
  background: #060911;
  position: relative;
  overflow: hidden;
}''',
'''.instant-scanner-section {
  padding: 100px 0;
  background: #fbf9f5;
  position: relative;
  overflow: hidden;
}'''
)

# Add .trans-stage-panel
stage_panel_css = '''
.trans-stage-panel {
  background: #141418;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 40px;
  padding: 70px 48px;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.25);
  position: relative;
  overflow: hidden;
}

@media (max-width: 768px) {
  .trans-stage-panel {
    padding: 40px 20px;
    border-radius: 28px;
  }
}
'''

if '.trans-stage-panel' not in css:
    css += stage_panel_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated stage panel and section backgrounds in styles.css!')
