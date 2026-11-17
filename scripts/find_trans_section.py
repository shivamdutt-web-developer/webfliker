import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's locate the transformation section
pattern = re.compile(r'<section\s+class=["\']transformation-showcase-section["\']\s+id=["\']transformation-showcase["\']>.*?</section>', re.DOTALL)
m = pattern.search(html)
if m:
    print(f"Found section: start={m.start()}, end={m.end()}, length={len(m.group(0))}")
else:
    print("Not found with pattern")
