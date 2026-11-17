import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('scripts/new_trans_section.html', 'r', encoding='utf-8') as f:
    new_section = f.read()

pattern = re.compile(r'<section\s+class=["\']transformation-showcase-section["\']\s+id=["\']transformation-showcase["\']>.*?</section>', re.DOTALL)
m = pattern.search(html)
if not m:
    print("Could not find transformation section!")
    exit(1)

html_updated = html[:m.start()] + new_section + html[m.end():]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_updated)

print("Successfully replaced transformation section in index.html!")
