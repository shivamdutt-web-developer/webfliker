import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Wrap transformation showcase container in trans-stage-panel if not already
old_trans_pattern = r'<section class="transformation-showcase-section"[^>]*>.*?<div class="container"[^>]*>'
new_trans_header = '''<section class="transformation-showcase-section" id="transformation-showcase">
    <div class="container">
      <div class="trans-stage-panel">
        <div class="trans-ambient-glow trans-glow-orange"></div>'''

# Check if trans-stage-panel is already there
if 'trans-stage-panel' not in html:
    # Replace the section opening and container
    html = re.sub(
        r'<section class="transformation-showcase-section"[^>]*>.*?<div class="container"[^>]*>',
        new_trans_header,
        html,
        count=1,
        flags=re.DOTALL
    )
    # And close the trans-stage-panel before </section>
    html = re.sub(
        r'(</section>\s*<!-- ========================================================================= -->\s*<!-- 8\. TRANSPARENT PRICING)',
        r'      </div>\n    </div>\n  \1',
        html,
        count=1
    )
    print("Wrapped transformation-showcase in Mobikasa trans-stage-panel!")
else:
    print("trans-stage-panel already present")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
