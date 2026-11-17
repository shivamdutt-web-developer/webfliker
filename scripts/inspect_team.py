import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<section[^>]*id="team-culture-section".*?</section>', html, re.DOTALL)
if not m:
    m = re.search(r'<section class="team-culture-section".*?</section>', html, re.DOTALL)

if m:
    print(m.group(0)[:1200])
else:
    print("Not found")
