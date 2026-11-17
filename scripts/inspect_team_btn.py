import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<section class="team-culture-section".*?</section>', html, re.DOTALL)
if m:
    lines = m.group(0).splitlines()
    print("\n".join(lines[25:60]))
